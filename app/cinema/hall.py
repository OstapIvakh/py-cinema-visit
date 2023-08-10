from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


class CinemaHall:
    def __init__(self, number: int) -> None:
        self.number = number

    def movie_session(
            self,
            movie_name: str,
            customers_list: list,
            cleaning_staff: "Cleaner"
    ) -> None:
        print(f'"{movie_name}" started in hall number {self.number}.')

        for person in customers_list:
            if isinstance(person, Customer):
                person_name = person.name
                person_food = person.food

                Customer(person_name, person_food).watch_movie(movie_name)

            else:
                person_name = person["name"]
                person_food = person["food"]

                Customer(person_name, person_food).watch_movie(movie_name)

        print(f'"{movie_name}" ended.')
        cleaning_staff.clean_hall(self.number)