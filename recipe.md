# {{PROBLEM}} Class Design Recipe

Copy this into a `recipe.md` in your project and fill it out.

As a user
So I don't forget the details
I want to keep a record of friends' names and birthdates

As a user
So I can make edits when I've got dates wrong
I want to be able to update a record by passing in a name and new date

As a user
So I can make edits when people change their name
I want to be able to update a record by passing in an old and a new name

As a user
So I can remember to send birthday cards at the right time
I want to be able to list friends whose birthdays are coming up soon and to whom I need to send a card

As a user
So I can buy age-appropriate birthday cards
I want to calculate the upcoming ages for friends with birthdays




_Put or write the user story here. Add any clarifying notes you might have._

## 2. Design the Class Interface
--> list of nouns (properties):
    details
    names
    birthdates 
    cards 
    mark complete 


--> list of verbs (methods):
    add friends
    edit or update with name and new date 
    pass old/new name 
    list of birthdays soon
    calculate age 


_Include the initializer, public properties, and public methods with all parameters, return values, and side-effects._

```python

# {name: {birthday: '01011999', age: '20' }}  self.tracker['name'][age]

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


```

## 3. Create Examples as Tests

_Make a list of examples of how the class will behave in different situations._

``` python

"""
Given a tracker is created 
An empty dictonary is created 
"""
birthday_tracker = BirthdayTracker()
birthday_tracker.tracker == {}

"""
Given we add an entry to the dictonary 
The entry can be accessed in the dictionary
"""
birthday_tracker = BirthdayTracker()
birthday_tracker.add('name', 'birthday') ==> birthday_tracker.tracker == {'name': 'birthday'}

"""
Given we edit a birthday 
The new birthday is updated in the dictionary 
"""
birthday_tracker = BirthdayTracker()
birthday_tracker.update_birthday('name', 'birthday') ==> birthday_tracker.tracker == {'name': 'birthday'}

"""
Given we edit the name passing in old name and new name 
The old name is searched and updated to the new name 
"""
birthday_tracker = BirthdayTracker()
birthday_tracker.update_name('old_name', 'new_name') ==> birthday_tracker.tracker == {'new_name': 'birthday'}

"""
Given we call the method of upcoming birthdays 
We see a list of names and birthdays in the nexy 30 days
"""
birthday_tracker = BirthdayTracker()
birthday_tracker.upcoming_birthdays() ==> {'name':'birthday'}

"""
Given we want to calculate the upcoming ages of friend with birthdays in next 30 days 
We see a list of names and ages 
"""
birthday_tracker = BirthdayTracker()
birthday_tracker.calculate_ages() ==> {'name': 'age'}

```

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._

