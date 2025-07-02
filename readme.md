
# **Find a Friend**

Python API for pet adoption


<br>

![Logo](./Find%20a%20Friend.jpg)

<br>

## Stacks:

**Framework:** Flask

**Database:** SQlite

**ORM:** SQLalchemy

**Tests:** PyTest

**Architeture:** MVC

<br>

## API Documentation

#### Create a person

```http
  POST /people
```

| Body params  | Type       | Description                           |
| :---------- | :--------- | :---------------------------------- |
| `first_name` | `string` | First person name |
| `last_name` | `string` | Last person name |
| `age` | `string` | Person's age |
| `pet_id` | `string` | Persons's adopted pet id (FK) |

#### List all Pets on db

```http
  GET /pets
```

#### Delete a pet on DB

```http
  DELETE /pets/<pet_name>
```

| Query params   | Type       | Description                           |
| :---------- | :--------- | :---------------------------------- |
| `pet_name` | `string` | Name of the pet to be deleted |

#### Delete a pet on DB

```http
  GET /people/<person_id>
```

| Query params   | Type       | Description                           |
| :---------- | :--------- | :---------------------------------- |
| `person_id` | `int` | Id of the person to be find |




