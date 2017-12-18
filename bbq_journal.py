import datetime

class BbqJournal:
    def __init__(self, title, meat, recipe, weather):
        self.title = title
        self.meat = meat
        self.recipe = recipe
        self.weather = weather
        self.day = datetime.date.today()


def create_journal():
    title = input("Please enter a title for this journal entry: ")
    meat = input("Please enter the type of meat: ")
    # Refactor the recipe input as a detailed class
    recipe = input("Enter your recipe: ")
    # Retrieve the weather data from somewhere
    weather = input("Enter weather notes: ")
    


print("\n\n######################### BBQ JOURNAL #########################\n\n"
            "Welcome to the BBQ Journal. This is your place to document your\n"
            "current cooks in pursuit of that perfect smoked flavor.\n"
        )

user_start = input("\n\nTo create a new journal entry type NEW, otherwise press the ENTER\n"
             "key.\n\n")

if user_start.lower() == "new":
    create_journal()
else:
    pass
    