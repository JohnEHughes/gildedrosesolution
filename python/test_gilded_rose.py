# -*- coding: utf-8 -*-
import pdb
import pytest
import sys

from gilded_rose import Item, GildedRose
from models import *


class TestGildedRose:
    def test_foo(self):
        items = [Item("foo", 0, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        assert "foo" == items[0].name


class TestAllItems:

    def test_standard(self):
        # initialise item
        item = Item("+5 Dexterity Vest", 2, 15)
        gilded_rose = GildedRose([item])
        assert "+5 Dexterity Vest" == item.name

        # forward one day
        gilded_rose.update_quality()
        assert 14 == item.quality
        assert 1 == item.sell_in

        # check quality stays the same and sell_in is correct
        for i in range(3): gilded_rose.update_quality()
        assert 9 == item.quality
        assert -2 == item.sell_in

        # check quality decreases at twice the rate
        gilded_rose.update_quality()
        assert 7 == item.quality
        assert -3 == item.sell_in

        item.quality_calculator(1)


    def test_sulfuras(self):
        # initialise item
        item = Sulfuras("Sulfuras, Hand of Ragnaros", 2, 80)
        gilded_rose = GildedRose([item])
        assert "Sulfuras, Hand of Ragnaros" == item.name

        # forward one day
        gilded_rose.update_quality()
        assert 80 == item.quality
        assert 1 == item.sell_in

        # forward 3 more days so sell_in == -2
        for i in range(3): gilded_rose.update_quality()

        # check quality stays the same and sell_in is correct
        assert 80 == item.quality
        assert -2 == item.sell_in


    def test_aged_brie(self):
        # initialise item
        item = AgedBrie("Aged Brie", 2, 15)
        gilded_rose = GildedRose([item])
        assert "Aged Brie" == item.name

        # forward one day
        gilded_rose.update_quality()
        assert 16 == item.quality
        assert 1 == item.sell_in

        # check quality increases +3 and sell_in is correct
        for i in range(3): gilded_rose.update_quality()

        assert 19 == item.quality
        assert -2 == item.sell_in


    def test_backstage_passes(self):
        # initialise item
        item = BackStagePasses("Backstage passes to a TAFKAL80ETC concert", 11, 15)
        gilded_rose = GildedRose([item])
        assert "Backstage passes to a TAFKAL80ETC concert" == item.name

        # forward one day - quality +1 / sell_in -1
        gilded_rose.update_quality()
        assert 16 == item.quality
        assert 10 == item.sell_in

        # forward one day - quality +2 / sell_in -1
        gilded_rose.update_quality()
        assert 18 == item.quality
        assert 9 == item.sell_in

        # forward 4 days - quality +8 / sell_in -4
        for i in range(4): gilded_rose.update_quality()

        assert 26 == item.quality
        assert 5 == item.sell_in

        # forward 1 day - quality +3 / sell_in -1
        gilded_rose.update_quality()
        assert 29 == item.quality
        assert 4 == item.sell_in

        # forward 4 days - quality +12 / sell_in -4
        for i in range(4): gilded_rose.update_quality()

        # concert day
        assert 41 == item.quality
        assert 0 == item.sell_in

        # forward 1 day - quality +12 / sell_in -4
        gilded_rose.update_quality()

        # day after concert
        assert 0 == item.quality
        assert -1 == item.sell_in


    def test_conjured(self):
        # initialise item
        item = Conjured("Conjured Mana Cake", 7, 19)
        gilded_rose = GildedRose([item])
        assert "Conjured Mana Cake" == item.name

        # forward one day - quality -2 / sell_in -1
        gilded_rose.update_quality()
        assert 17 == item.quality
        assert 6 == item.sell_in

        # forward one day - quality -2 / sell_in -1
        gilded_rose.update_quality()
        assert 15 == item.quality
        assert 5 == item.sell_in

        # forward 5 days - quality -10 / sell_in -5
        for i in range(5): gilded_rose.update_quality()

        # sell_in == 0
        assert 5 == item.quality
        assert 0 == item.sell_in

        # forward 1 day - quality -4 / sell_in -1
        gilded_rose.update_quality()
        assert 1 == item.quality
        assert -1 == item.sell_in

        # forward 1 day - quality -4 / sell_in -1
        gilded_rose.update_quality()
        assert 0 == item.quality
        assert -2 == item.sell_in
