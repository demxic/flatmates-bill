from flat import Bill, FlatMate


def test_flatmate_init():
    flatmate1 = FlatMate('Jose', 20)

    assert flatmate1.name == 'Jose'
    assert flatmate1.days_in_house == 20


def test_pays():
    bill = Bill(120, 'march')

    jose = FlatMate('Jose', 20)
    mary = FlatMate('Mary', 25)

    assert jose.pays(bill, mary) == 53.33
    assert mary.pays(bill, jose) == 66.67
