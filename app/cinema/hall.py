from app.people import customer, cinema_staff


class CinemaHall:
    def __init__(self, number: int) -> None:
        self.number = number

    def movie_session(self, movie_name: str, customers: list[customer.Customer],
                      cleaning_staff: cinema_staff.Cleaner) -> None:
        print(f"{movie_name} start in the hall number {self.number}.")
        for customer in customers:
            customer.watch_movie(movie_name)
        print(f"{movie_name} ended.")
        cleaning_staff.clean_hall(self.number)
