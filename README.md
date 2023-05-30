# gildedrosesolution

This is a refactoring project which provides a solution to the Gilded Rose kata.

I refactored the initial code then broke it up into several files. I decided to created separate classes for the different items in the shop using the Item class as the base. Then every other class inherits the basic attributes and overrides the upgrade quality function to deliver their unique requirements. 
There is a separate utils file to store the helper functions and then I created a test file using pytest to ensure the code meets the starting requirements.
