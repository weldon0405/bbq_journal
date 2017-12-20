import datetime

class BbqJournal:
    def __init__(self, title, meat, recipe, weather):
        self.title = title
        self.meat = meat
        self.recipe = recipe
        self.weather = weather
        self.day = datetime.date.today()

    def __str__(self):
        journal_entry = []

        # for key in self.__dict__:
        #     journal_entry[key] = self.__dict__[key]

        # return str(journal_entry)
        return f"Title: {self.title}, \nDate: {self.day}, \nMeat: {self.meat}, \nRecipe: {self.recipe}, \nWeather {self.weather}"
 
    def __repr__(self):
        journal_entry = {}

        for key in self.__dict__:
            journal_entry[key] = self.__dict__[key]

        return journal_entry

# new_entry = None

def create_journal():
    title = input("Please enter a title for this journal entry: ")
    meat = input("Please enter the type of meat: ")
    # Refactor the recipe input as a detailed class
    recipe = input("Enter your recipe: ")
    # Retrieve the weather data from somewhere
    weather = input("Enter weather notes: ")
    new_entry = BbqJournal(title, meat, recipe, weather)
    print(new_entry)
    return new_entry



print("\n\n######################### BBQ JOURNAL #########################\n\n"
            "Welcome to the BBQ Journal. This is your place to document your\n"
            "current cooks in pursuit of that perfect smoked meat flavor.\n"
        )

user_start = input("\n\nTo create a new journal entry type NEW, otherwise press the ENTER\n"
             "key.\n\n")

if user_start.lower() == "new":
    create_journal()
        # title = input("Please enter a title for this journal entry: ")
        # meat = input("Please enter the type of meat: ")
        # # Refactor the recipe input as a detailed class
        # recipe = input("Enter your recipe: ")
        # # Retrieve the weather data from somewhere
        # weather = input("Enter weather notes: ")
        # new_entry = BbqJournal(title, meat, recipe, weather)
        # return new_entry
else:
    pass
    