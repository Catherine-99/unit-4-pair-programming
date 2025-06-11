class BirthdayTracker:

    def __init__(self):
        self.tracker = {}
        #no parameters
        #side effect: creating dict
        pass

    def add_birthday(self, name, birthday):
        #parameters:
            #name: string
            #birthday: string
        
        #returns: nothing 
        #side effect: appends entry to dict 
        #calculate age of the user and save it to age property 
        pass

    def edit_birthday(self, name, birthday):
        #parameters:
            #name: string
            #birthday: string
        
        #returns: nothing 
        #side effect: checks name exists and updates entry to dict
        #recalculate age based on new date 
        pass

    def edit_name(self, old_name, new_name):
        #parameters:
            #names: strings

        #returns: nothing 
        #side effect: checks name exists and updates the name in dict

        pass

    def upcoming_birthdays(self):
        #assume upcoming in next 30 days
        #no parameters 
        #returns: 
            #list of friends with birthdays in next 30 days 
        #no sideeffects 
        pass 

    def calculate_age(self, name):
        #parameter:
            #name: string 
        #returns: age from the name
        #no side effects 
        #use list from upcoming birthdays 
        pass 
