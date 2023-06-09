# -*- coding: utf-8 -*-
from __future__ import print_function

from gilded_rose import *

if __name__ == "__main__":
    print ("OMGHAI!")
    items = [
             StandardItem(name="+5 Dexterity Vest", sell_in=10, quality=20),
             StandardItem(name="Aged Brie", sell_in=2, quality=0),
             StandardItem(name="Elixir of the Mongoose", sell_in=5, quality=7),
             StandardItem(name="Sulfuras, Hand of Ragnaros", sell_in=0, quality=80),
             StandardItem(name="Sulfuras, Hand of Ragnaros", sell_in=-1, quality=80),
             StandardItem(name="Backstage passes to a TAFKAL80ETC concert", sell_in=15, quality=20),
             StandardItem(name="Backstage passes to a TAFKAL80ETC concert", sell_in=10, quality=49),
             StandardItem(name="Backstage passes to a TAFKAL80ETC concert", sell_in=5, quality=49),
             StandardItem(name="Conjured Mana Cake", sell_in=3, quality=6), 
             StandardItem(name="Conjured Mana Cake", sell_in=2, quality=35),  # <-- :O
            ]

    days = 5
    import sys
    if len(sys.argv) > 1:
        days = int(sys.argv[1]) + 1
    for day in range(days):
        print("-------- day %s --------" % day)
        print("name, sellIn, quality")
        for item in items:
            print(item)
        print("")
        GildedRose(items).update_quality()
