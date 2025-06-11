from datetime import datetime, timedelta

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
                                    datetime.strptime(friend[1], "%Y-%m-%d") <= thirty_days_future 
                                    and datetime.strptime(friend[1], "%Y-%m-%d") >= today, 
                                    self.tracker.items()
                                    ))
        return next_thirty_days

    def calculate_age(self, name):
        #parameter:
            #name: string 
        #returns: age from the name
        #no side effects 
        #use list from upcoming birthdays 
        pass 
