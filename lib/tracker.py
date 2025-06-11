from datetime import datetime, timedelta
from math import ceil


class BirthdayTracker:

    def __init__(self):
        self.tracker = {}

    def add_birthday(self, name, birthday):
        #parameters:
            #name: string
            #birthday: string
        
        #returns: nothing 
        #side effect: appends entry to dict 
        #calculate age of the user and save it to age property 
        self.tracker[name] = birthday

    def edit_birthday(self, name, birthday):
        #parameters:
            #name: string
            #birthday: string
        
        #returns: nothing 
        #side effect: checks name exists and updates entry to dict
        #recalculate age based on new date 
        if name in self.tracker.keys():
            self.tracker[name] = birthday
        else:
            raise Exception("No exisiting entry to update")


    def edit_name(self, old_name, new_name):
        #parameters:
            #names: strings

        #returns: nothing 
        #side effect: checks name exists and updates the name in dict
        if old_name in self.tracker.keys():
            self.tracker[new_name] = self.tracker[old_name]
            del self.tracker[old_name]
        else:
            raise Exception("No entry found")


    def upcoming_birthdays(self):
        today = datetime.now()
        thirty_days_future = today + timedelta(days=30)
        next_thirty_days = dict(filter(lambda friend: 
                                    datetime.strptime(friend[1], "%Y-%m-%d").replace(year=today.year) <= thirty_days_future 
                                    and datetime.strptime(friend[1], "%Y-%m-%d").replace(year=today.year) >= today, 
                                    self.tracker.items()
                                    ))
#      if next_thirty_days == {}:
#          return next_thirty_days
#           print(next_thirty_days)
#          raise Exception("No upcoming birthdays")
        return next_thirty_days

    def calculate_age(self):
        #returns: age from the name
        #no side effects 
        #use list from upcoming birthdays 
        upcoming = self.upcoming_birthdays().items()
        today = datetime.now()
        name_age_dict ={}
        for friend in upcoming:
            datetime_birthday = datetime.strptime(friend[1], "%Y-%m-%d")
            age = today - datetime_birthday
            age_in_years = ceil(age.days / 365.25)
            name_age_dict[friend[0]] = age_in_years

        return name_age_dict

