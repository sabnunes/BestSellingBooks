import unittest
import sys
from BestSellers import *

class Test_BestSellers(unittest.TestCase):

    def test_books_in_year_range_1_1(self):
        try:
            output = """Best selling books between 2011-2012 (inclusive):
2011: 23337
2011: A Dance With Dragons
2011: Against All Enemies
2011: Chasing Fire
2011: Cold Vengeance
2011: Dead Reckoning
2011: Dreams of Joy
2011: Explosive Eighteen
2011: Flash and Bones
2011: Ghost Story
2011: Heat Rises
2011: Hit List
2011: Kill Alex Cross
2011: Kill Me If You Can
2011: Live Wire
2011: New York to Dallas
2011: Now You See Her
2011: Shadowfever
2011: Shock Wave
2011: Smokin' Seventeen
2011: The Affair
2011: The Best of Me
2011: The Drop
2011: The Fifth Witness
2011: The Inner Circle
2011: The Jungle
2011: The Land of the Painted Caves
2011: The Litigators
2011: The Omen Machine
2011: The Sixth Man
2011: The Wise Man's Fear
2011: Tick Tock
2011: Toys
2011: Treachery In Death
2011: What the Night Knows
2011: Zero Day
2011: A Stolen Life
2011: Bossypants
2011: In My Time
2011: In the Garden of Beasts
2011: Jacqueline Kennedy: Historic Conversations On Life With John F. Kennedy
2011: Killing Lincoln
2011: Known and Unknown
2011: Lies That Chelsea Handler Told Me
2011: Onward
2011: Red
2011: Steve Jobs
2011: The Greater Journey
2011: The Social Animal
2011: Those Guys Have All the Fun
2011: Unbroken
2012: 77 Shadow Street 
2012: Private: #1 Suspect 
2012: Believing the Lie 
2012: Taken 
2012: Home Front 
2012: Kill Shot 
2012: Private Games 
2012: Celebrity In Death 
2012: Lone Wolf 
2012: The Thief 
2012: Stay Close 
2012: Lover Reborn 
2012: The Lost Years 
2012: Calico Joe 
2012: The Innocent 
2012: The Wind Through the Keyhole 
2012: Deadlocked 
2012: 11th Hour 
2012: Stolen Prey 
2012: The Storm 
2012: Kiss the Dead 
2012: Wicked Business 
2012: Gone Girl 
2012: Shadow of Night 
2012: The Fallen Angel 
2012: The Time Keeper 
2012: A Wanted Man 
2012: Winter of the World 
2012: The Casual Vacancy 
2012: The Panther 
2012: The Racketeer 
2012: The Last Man 
2012: Notorious Nineteen 
2012: Cold Days 
2012: Threat Vector 
"""
            self.test=books_in_year_range(2011,2012)
            self.assertEqual(books_in_year_range(2011,2012), output)
            print("Function 1_1 - OK")
        except NameError:
            print("Function 1_1 missing - books_in_year_range")
        except:
            print("Error Function 1_1" + str(sys.exc_info()))
    def test_books_in_year_range_1_2(self):
        try:
            output = 'No match found.'
            self.test=books_in_year_range(2022,2023)
            self.assertEqual(books_in_year_range(2022,2023), output)
            print("Function 1_2 - OK")
        except NameError:
            print("Function 1_2 missing - books_in_year_range")
        except:
            print("Error Function 1_2" + str(sys.exc_info()))
    def test_books_in_month_year_2_1(self):
        try:
            output = """Best selling books in 11/2005:
"A Feast For Crows" by George R. R. Martin
"At First Sight" by Nicholas Sparks
"Predator" by Patricia Cornwell
"Our Endangered Values" by Jimmy Carter
"The Truth (With Jokes)" by Al Franken
"""
            self.test=books_in_month_year(11,2005)
            self.assertEqual(books_in_month_year(11,2005), output)
            print("Function 2_1 - OK")
        except NameError:
            print("Function 2_1 missing - books_in_month_year")
        except:
            print("Error Function 2_1" + str(sys.exc_info()))
    def test_books_in_month_year_2_2(self):
        try:
            output = 'No match found.'
            self.test=books_in_month_year(2,2023)
            self.assertEqual(books_in_month_year(2,2023), output)
            print("Function 2_2 - OK")
        except NameError:
            print("Function 2_2 missing - books_in_month_year")
        except:
            print("Error Function 2_2" + str(sys.exc_info()))
    def test_books_by_author_3_1(self):
        try:
            output = """Books by author:
"Going Rogue" by Sarah Palin
"""
            self.test=books_by_author('arah')
            self.assertEqual(books_by_author('arah'), output)
            print("Function 3_1 - OK")
        except NameError:
            print("Function 3_1 missing - books_by_author")
        except:
            print("Error Function 3_1" + str(sys.exc_info()))
    def test_books_by_author_3_2(self):
        try:
            output = 'No match found.'
            self.test=books_by_author('sabrina')
            self.assertEqual(books_by_author('sabrina'), output)
            print("Function 3_2 - OK")
        except NameError:
            print("Function 3_2 missing - books_by_author")
        except:
            print("Error Function 3_2" + str(sys.exc_info()))
    def test_books_by_title_4_1(self):
        try:
            output = """Books with title:
"Black Hills" by Nora Roberts
"Chill Factor" by Sandra Brown
"The Children of the Hurin" by J.R.R. Tolkein
"The Hollow Hills" by Mary Stewart
"While My Pretty Once Sleeps" by Mary Higgins Clark
"Between Parent and Child" by Hiam Ginott
"The Beverly Hills Diet" by Judy Mazel
"The Rothchilds" by Frederic Morton
"""
            self.test=books_by_title('hil')
            self.assertEqual(books_by_title('hil'), output)
            print("Function 4_1 - OK")
        except NameError:
            print("Function 4_1 missing - books_by_title")
        except:
            print("Error Function 4_1" + str(sys.exc_info()))
    def test_books_by_title_4_2(self):
        try:
            output = 'No match found.'
            self.test=books_by_title('philo')
            self.assertEqual(books_by_title('philo'), output)
            print("Function 4_2 - OK")
        except NameError:
            print("Function 4_2 missing - books_by_title")
        except:
            print("Error Function 4_2" + str(sys.exc_info()))

if __name__ == "__main__":
    unittest.main()
