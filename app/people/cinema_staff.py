class Cleaner:
    def __init__(self, name) -> None:
        self.name = name

    def clean_hall(self, hall_number: int) -> None:
        return print(f"Cleaner {self.name} is cleaning hall number {hall_number}.")
