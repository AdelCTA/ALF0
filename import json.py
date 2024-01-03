import json

# Your JSON data
json_data = [
    {
        "age": 3,
        "donor_id": 2,
        "created_at": "2022-01-01T12:00:00",
        "location": "Liverpool",
        "model": "Dell",
        "status": "Active",
        "type": "Type A",
        "updated_at": "2022-01-02T10:30:00",
        "attributes": {"color": "red", "size": "small"},
        "coordinates": {"latitude": 51.5074, "longitude": -0.1278},
        "archived": "0",
        "organisation_id": 1,
    },
    {
        "age": 1,
        "donor_id": 1,
        "created_at": "2022-01-01T12:00:00",
        "location": "Manchester",
        "model": "Dell",
        "status": "Active",
        "type": "Type A",
        "updated_at": "2022-01-02T10:30:00",
        "attributes": {"color": "red", "size": "small"},
        "coordinates": {"latitude": 51.5074, "longitude": -0.1278},
        "archived": "0",
        "organisation_id": 1,
    },
    {
        "age": 5,
        "donor_id": 2,
        "created_at": "2022-01-01T12:00:00",
        "location": "London",
        "model": "Dell",
        "status": "Active",
        "type": "Type A",
        "updated_at": "2022-01-02T10:30:00",
        "attributes": {"color": "red", "size": "small"},
        "coordinates": {"latitude": 51.5074, "longitude": -0.1278},
        "archived": "0",
        "organisation_id": 1,
    },
    {
        "age": 3,
        "donor_id": 1,
        "created_at": "2022-01-01T12:00:00",
        "location": "London",
        "model": "Dell",
        "status": "Active",
        "type": "Type A",
        "updated_at": "2022-01-02T10:30:00",
        "attributes": {"color": "red", "size": "small"},
        "coordinates": {"latitude": 51.5074, "longitude": -0.1278},
        "archived": "0",
        "organisation_id": 1,
    }
]

# Iterate over the JSON objects
for i, obj in enumerate(json_data, start=1):
    # Generate filename with leading zeros (e.g., kit0001.txt, kit0002.txt, ...)
    filename = f'kit{str(i).zfill(4)}.txt'

    # Write JSON object to a file
    with open(filename, 'w') as file:
        json.dump(obj, file, indent=4)

    print(f'File saved: {filename}')
