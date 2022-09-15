class Bill:
    """
    Represents a bill with its corresponding amount ant the period to be paid
    """

    def __init__(self, amount: int, period: str) -> None:
        """Create a simple bill for a period of time and a given amount"""
        self.amount = amount
        self.period = period


class FlatMate:
    def __init__(self, name: str, days_in_house: int = 30):
        self.name = name
        self.days_in_house = days_in_house

    def pays(self, bill: Bill, flatmate2: 'FlatMate'):
        """Given a Bill and another flatmate, this method returns the
        split amount each flatmate should pay
        """
        weight = self.days_in_house / (self.days_in_house + flatmate2.days_in_house)
        return round(weight * bill.amount, 2)
