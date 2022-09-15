from flat import Bill


def test_bill_init():
    bill = Bill(120, 'march')

    assert bill.amount == 120
    assert bill.period == 'march'
