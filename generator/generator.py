from data.data import Person
from faker import Faker

faker_eu = Faker('ru_RU')


def generated_person():
    yield Person(
        full_name=faker_eu.first_name() + ' ' + faker_eu.last_name(),
        email=faker_eu.email(),
        current_address=faker_eu.address(),
        permanent_address=faker_eu.address(),
    )
