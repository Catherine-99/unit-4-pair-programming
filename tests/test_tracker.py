import pytest
from lib.tracker import BirthdayTracker

"""
Given a tracker is created 
An empty dictonary is created 
"""
def test_tracker_is_created_as_empty_dictionary():
    birthday_tracker = BirthdayTracker()
    assert birthday_tracker.tracker == {}

"""
Given we add an entry to the dictonary 
The entry can be accessed in the dictionary
"""
def test_adding_entry_to_dictionary_and_access():
    birthday_tracker = BirthdayTracker()
    birthday_tracker.add_birthday('Jim', '2020-06-11') 
    assert birthday_tracker.tracker == {'Jim': '2020-06-11'}
    # ==> birthday_tracker.tracker == {'name': 'birthday'}

"""
Given we edit a birthday 
The new birthday is updated in the dictionary 
"""
def test_editing_birthday_date():
    birthday_tracker = BirthdayTracker()
    birthday_tracker.add_birthday('Jim', '2020-06-11') 
    assert birthday_tracker.tracker == {'Jim': '2020-06-11'}
    birthday_tracker.edit_birthday('Jim', '2019-06-11')
    assert birthday_tracker.tracker == {'Jim': '2019-06-11'}


def test_editing_birthday_date_no_existing_entry():
    birthday_tracker = BirthdayTracker()
    with pytest.raises(Exception) as err:
        birthday_tracker.edit_birthday('Jim', '2019-06-11')
    err_message = "No exisiting entry to update"
    assert str(err.value) == err_message

"""
Given we edit the name passing in old name and new name 
The old name is searched and updated to the new name 
"""
def test_editing_name_existing_entry():
    birthday_tracker = BirthdayTracker()
    birthday_tracker.add_birthday('Jim', '2020-06-11') 
    birthday_tracker.edit_name('Jim', 'Jam') 
    assert birthday_tracker.tracker == {'Jam': '2020-06-11'}

def test_editing_name_no_existing_entry():
    birthday_tracker = BirthdayTracker()
    birthday_tracker.add_birthday('Jim', '2020-06-11') 
    with pytest.raises(Exception) as err:
        birthday_tracker.edit_name('Bob', 'Bill') 
    err_message = "No entry found"
    assert str(err.value) == err_message

"""
Given we call the method of upcoming birthdays 
We see a list of names and birthdays in the nexy 30 days
"""
def test_show_birthdays_next_30_days():
    birthday_tracker = BirthdayTracker()
    birthday_tracker.add_birthday('Jim', '2025-06-20') 
    birthday_tracker.add_birthday('Bob', '2025-07-20') 
    assert birthday_tracker.upcoming_birthdays() == {'Jim': '2025-06-20'}

"""
Given we want to calculate the upcoming ages of friend with birthdays in next 30 days 
We see a list of names and ages 
"""
#birthday_tracker = BirthdayTracker()
#birthday_tracker.calculate_ages() ==> {'name': 'age'}