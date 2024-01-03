import os
import json
import psycopg2
from datetime import datetime
from shutil import move

def main():
    # Database connection
    conn = psycopg2.connect("postgresql://postgres:BDC6dd*23C*efa*Gb2DBDC-EC142d13E@monorail.proxy.rlwy.net:36030/railway")
    cur = conn.cursor()

    # Create the 'kits' table in the database
    create_table_query = '''
    CREATE TABLE IF NOT EXISTS kits (
        id BIGSERIAL PRIMARY KEY,
        age INTEGER,
        created_at TIMESTAMP,
        location VARCHAR,
        model VARCHAR,
        status VARCHAR,
        type VARCHAR,
        updated_at TIMESTAMP,
        attributes JSON,
        coordinates JSON,
        archived CHAR(1) DEFAULT '0',
        organisation_id BIGINT,
        donor_id BIGINT,
        Test1 VARCHAR,
        Test2 VARCHAR
    )
    '''
    cur.execute(create_table_query)

    # Set the path to the directory containing JSON files
    files_folder = os.path.join(os.getcwd(), "logs/hardwareinfo")
    failure_folder = os.path.join(os.getcwd(), "logs/hardwareinfo/error")
    archive_folder = os.path.join(os.getcwd(), "logs/hardwareinfo/archive")
    
    # Check if the directory exists, create failure and archive folders if they don't exist
    if not os.path.exists(files_folder):
        print("The directory does not exist:", files_folder)
        return
    if not os.path.exists(failure_folder):
        os.makedirs(failure_folder)
    if not os.path.exists(archive_folder):
        os.makedirs(archive_folder)

    # Read and process each JSON file in the directory
    for root, folders, files in os.walk(files_folder):
        for file in files:
            if file.endswith('.json'):
                path = os.path.join(root, file)
                try:
                    with open(path, 'r') as file_info:
                        data = json.load(file_info)
                        # Prepare data for insertion
                        insert_data = (
                            data["age"],
                            datetime.fromisoformat(data["created_at"]),
                            data["location"],
                            data["model"],
                            data["status"],
                            data["type"],
                            datetime.fromisoformat(data["updated_at"]),
                            json.dumps(data["attributes"]),
                            json.dumps(data["coordinates"]),
                            data["archived"],
                            data["organisation_id"],
                            data["donor_id"],
                            '',  # Placeholder for Test1 (assuming empty string)
                            ''   # Placeholder for Test2 (assuming empty string)
                        )
                        # Insert data into the table
                        insert_query = '''
                        INSERT INTO kits 
                        (age, created_at, location, model, status, type, updated_at, attributes, coordinates, archived, organisation_id, donor_id, Test1, Test2)
                        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                        '''
                        cur.execute(insert_query, insert_data)
                        # Move the successfully processed file to the 'archive' directory
                        move(path, os.path.join(archive_folder, file))
                except IOError as e:
                    print(f"Error reading file {path}: {e}")
                    # Move the failed file to the 'failure' directory
                    move(path, os.path.join(failure_folder, file))
                except json.JSONDecodeError as e:
                    print(f"Error decoding JSON from file {path}: {e}")
                    # Move the failed file to the 'failure' directory
                    move(path, os.path.join(failure_folder, file))

    # Commit changes to the database
    conn.commit()
    cur.close()
    conn.close()

if __name__ == "__main__":
    main()
