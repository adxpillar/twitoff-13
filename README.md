# twitoff-13

## Installation 

TODO: instructions 

## Setup 

TODO: instructions 

Migrate the db:

```sh
FLASK_APP=web_app flask db init #> generates app/migrations dir

#run both when changing the schema:
FLASK_APP=web_app flask db migrate #> creates the db (with "alembic_version" table)
FLASK_APP=web_app flask db upgrade #> creates the specified tables
```


## Usage

```sh
# Mac:
FLASK_APP = web_app flask run 

# Windows:
export FLASK_APP = web_app # one-time thing, to set the new var 
flask run 
```