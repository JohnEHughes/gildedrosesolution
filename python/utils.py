
def increase_quality(self, amount):
    self.quality+=amount

def decrease_quality(self, amount):
    self.quality-=amount

def quality_check_less_than(self, check_no):
    return self.quality < check_no

def quality_check_greater_than(self, check_no):
    return self.quality > check_no

def quality_check_greater_than_or_equal_to(self, check_no):
    return self.quality >= check_no

def quality_check_less_than_or_equal(self, check_no):
    return self.quality <= check_no

def sell_in_check(self, days):
    return self.sell_in <= days

def standard_quality_check_and_quality_increase(self):
    if quality_check_less_than(self, 50):
        increase_quality(self, 1)

def decrement_sell_in(self):
    self.sell_in -= 1

def quality_set_to_zero(self):
    self.quality = 0