class Cars:
    """ A Value-Object used to hold the car data

    """
    def __init__(self, code, brand, pick_up_place, days_reserved):  # FIXME: This is supposed to be a Car aggregate
        self.code = code
        self.brand = brand
        self.pick_up_place = pick_up_place
        self.days_reserved = days_reserved
