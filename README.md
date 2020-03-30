## At the begining

https://hub.docker.com/editions/community/docker-ce-desktop-mac/

https://flask.palletsprojects.com/en/1.1.x/quickstart/#quickstart

https://dev.mysql.com/get/Downloads/MySQL-8.0/mysql-8.0.19-macos10.15-x86_64.dmg

https://flask.palletsprojects.com/en/1.1.x/patterns/sqlite3/

http://www.pythondoc.com/Flask-RESTful/quickstart.html


## Usage

All responses will have the form

```json
{
    "data": "Mixed type holding the content of the response",
    "message": "Description of what happened"
}
```

Subsequent response definitions will only detail the expected value of the `data field`

### List all maps

**Definition**

`GET /maps`

**Response**

- `200 OK` on success

```json
[
    {
        "mapId": "1001",
        "a0": "x@x@x@x@x@x@x@x@x@x@x@1@1@1@@@@x",
        "a1": "x@x@x@x@x@x@x@x@x@x@"
    },
    {
        "mapId": "1002",
        "a0": "x@x@x@x@x@x@x@x@x@x@x@1@1@1@@@@x",
        "a1": "x@x@x@x@x@x@x@x@x@x@"
    },
]
```

## Lookup map detail

** Definition ** 

`GET /map/<mapId>`

** Response **

- `404 Not Found` if the key is not exist
- `200 OK` on success

```json
{
    "mapId":"1001",
    "a0":"x@x@x@x@x@x@x@x@x@x@x",
    "a1":"x@x@x@x@x@x@x@x@x@x@x",
}
```

## Add a new solution

** Definition **

`POST /solutions`

** Arguments **

- "mapId":int a globally unique identifier for this device
- "solution":string the solution of the map

**Response**

- `201 Created` on success

```json
{
    "mapId":"1001",
    "solution":"1:2|3:4"
}
```

## Lookup solution details

** Definition ** 

`GET /solution/<mapId>`

** Response **

- `404 Not Found` if the solution is not exist
- `200 OK` on success

```json
{
    "mapId":1,
    "solution":"1:2|3:4"
}
```

## Delete a solution

**Definition**

`DELETE /solutions/<mapId>`

**Response**

- `404 Not Found` if the solution is not exist
- `204 No Content` on success