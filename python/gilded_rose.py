# -*- coding: utf-8 -*-
from models import Sulfuras, AgedBrie, BackStagePasses, Conjured, Item
from dataclasses import dataclass
from typing import List


@dataclass
class GildedRose:
    items: List[object]

    def update_quality(self):
        for item in self.items: item.__class__.update_quality(item)
