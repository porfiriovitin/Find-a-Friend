import re
from src.models.sqlite.interfaces.people_repository import PeopleRepositoryInterface
from src.errors.error_types.http_bad_request import HttpBadRequestError
from .interfaces.person_creator_controller import PersonCreatorControllerInterface

class PersonCreatorController(PersonCreatorControllerInterface):
    def __init__(self, people_repository: PeopleRepositoryInterface)->None:
        self.__people_repository = people_repository
    
    def create(self, person_info: dict) -> dict:
        first_name = person_info["first_name"]
        last_name = person_info["last_name"]
        age = person_info["age"]
        pet_id = person_info["pet_id"]

        self.__validate_first_and_last_name(first_name, last_name)
        self.__insert_person_in_db(first_name, last_name, age, pet_id)
        formatted_response = self.__format_response(person_info)
        return formatted_response

    def __validate_first_and_last_name(self, first_name:str, last_name:str) -> None:
        # Regular expression for non word characters
        non_valid_characters = re.compile(r'[^a-zA-Z]')

        if non_valid_characters.search(first_name) or non_valid_characters.search(last_name):
            raise HttpBadRequestError("Invalid person's name")
    
    def __insert_person_in_db(self, first_name:str, last_name:str, age: int, pet_id:int) -> None:
        self.__people_repository.insert_person(first_name, last_name, age, pet_id)

    def __format_response(self, person_info:dict) -> dict:
        return {
            "data": {
                "type": "Person",
                "count": 1,
                "attributes": person_info
            }
        }