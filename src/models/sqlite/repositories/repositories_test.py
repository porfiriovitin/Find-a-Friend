import pytest
from src.models.sqlite.settings.connection import dbconnectionhandler
from .pets_repository import PetsRepository
from .people_repository import PeopleRepository

dbconnectionhandler.connect_to_db()

@pytest.mark.skip(reason="db iter")
def test_list_pets():
    repo = PetsRepository(db_connection=dbconnectionhandler)
    response = repo.list_pets()
    print(response)

@pytest.mark.skip(reason="db iter")
def test_delete_pet():
    pet_name = "cobra"
    repo = PetsRepository(db_connection=dbconnectionhandler)
    repo.delete_pets(pet_name)

@pytest.mark.skip(reason="db iter")
def test_insert_person():
    first_name= "Juliana"
    last_name = "Leite"
    age = 22
    pet_id = 9

    repo = PeopleRepository(dbconnectionhandler)
    repo.insert_person(first_name, last_name, age, pet_id)

@pytest.mark.skip(reason="db iter")
def test_get_person():
    person_id = 1

    repo = PeopleRepository(dbconnectionhandler)
    response = repo.get_person(person_id)
    print()
    print(response)

    