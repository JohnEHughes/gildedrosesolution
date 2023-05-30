from utils import *
from dataclasses import dataclass


@dataclass
class Item:
    """ A class for a standard item
    @name: name of the item
    @quality: the quality value between 0 and 50
    @sell_in: the number  of days left to sell in"""

    name: str
    sell_in: int
    quality: int

    def update_quality(self):
        if quality_check_greater_than_or_equal_to(self, 2) and quality_check_less_than(self, 50):
            decrease_quality(self, 2) if sell_in_check(self, 0) else decrease_quality(self, 1)
        else:
            if quality_check_greater_than(self, 0):
                decrease_quality(self, 1)
        decrement_sell_in(self)

    def __str__(self):
        return f"Item {self.name} - has a quality value of {self.quality} with {self.sell_in} sell in date"
    
    def quality_calculator(self, days):
        for day in range(days):
            self.update_quality()
        print(self.__str__())


@dataclass              
class Sulfuras(Item):
    """ Legendary item, never has to be sold and quality never changes"""

    def update_quality(self):
        decrement_sell_in(self)
        pass


@dataclass    
class AgedBrie(Item):
    """ Increases quality the older it gets"""

    def update_quality(self):
        standard_quality_check_and_quality_increase(self)
        decrement_sell_in(self)
   

@dataclass    
class BackStagePasses(Item):
    """ Increases quality as sell in value approaches
    increases by 2 when there are less than 10 days or less
    increases by 3 when there are less than 5 days or less
    quality drops to 0 after the concert"""

    def update_quality(self):
        if sell_in_check(self, 0):
            quality_set_to_zero(self)
        elif sell_in_check(self, 5) and quality_check_less_than_or_equal(self, 47):
            increase_quality(self, 3)
        elif sell_in_check(self, 10) and quality_check_less_than_or_equal(self, 48):
            increase_quality(self, 2)
        elif quality_check_less_than_or_equal(self, 49):
            increase_quality(self, 1)
        decrement_sell_in(self)


@dataclass    
class Conjured(Item):
    """ Quality degrades twice as quick as a standard item"""

    def update_quality(self):
        if not(quality_check_less_than(self, 2)) and sell_in_check(self, 0):
            decrease_quality(self, 2)
        if not(quality_check_less_than(self, 2)):
            decrease_quality(self, 2)
        else:
            quality_set_to_zero(self)
        decrement_sell_in(self)

