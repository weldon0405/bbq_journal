import datetime
import logging
from time import strftime

from colorama import Fore, Back, Style


now = datetime.datetime.now().timetuple()
tm_stamp = strftime("%Y_%m_%d", now)


class BbqJournal:
    def __init__(self, title, meat, recipe, weather):
        self.title = title
        self.meat = meat
        self.recipe = recipe
        self.weather = weather
        self.day = datetime.date.today()

    def __str__(self):
        journal_entry = Style.BRIGHT + Fore.GREEN + f"\n\n############### {self.title.upper()} ###############\n\n" + Fore.RED + f"Cooked on {self.day}" + Style.NORMAL + Fore.CYAN + "\nMeat: " + Style.BRIGHT + Fore.WHITE + f"{self.meat}" + Style.NORMAL + Fore.CYAN + "\nRecipe: " + Style.BRIGHT + Fore.WHITE + f"{self.recipe}" + Style.NORMAL + Fore.CYAN + "\nWeather " + Style.BRIGHT + Fore.WHITE + f"{self.weather}"

        return journal_entry
 
    def __repr__(self):
        journal_entry = {}

        for key in self.__dict__:
            journal_entry[key] = self.__dict__[key]

        return journal_entry


def create_journal():
    title = input(Fore.CYAN + "\nPlease enter a title for this journal entry: "
                    + Style.BRIGHT + Fore.MAGENTA)
    meat = input(Fore.CYAN + Style.NORMAL + "Please enter the type of meat: "
                    + Style.BRIGHT + Fore.MAGENTA)
    # Refactor the recipe input as a detailed class
    recipe = input(Fore.CYAN + Style.NORMAL + "Enter your recipe: "
                    + Style.BRIGHT + Fore.MAGENTA)
    # Retrieve the weather data from somewhere
    weather = input(Fore.CYAN + Style.NORMAL + "Enter weather notes: "
                    + Style.BRIGHT + Fore.MAGENTA)
    new_entry = BbqJournal(title, meat, recipe, weather)
    logging.info(f'New Journal Entry, {new_entry.title} Created')
    print(new_entry)
    return new_entry

def app_start():
    print(Fore.GREEN + Style.BRIGHT +
            "\n\n######################### BBQ JOURNAL #########################\n\n" +
            Fore.RED + "Welcome to the BBQ Journal. This is your place to document " +
            "your\ncurrent cooks in pursuit of that perfect smoked meat flavor.\n"
            )

    user_start = input(Fore.GREEN + Style.NORMAL + "\n\nTo create a new journal " +
                        "entry type " +
                        Fore.WHITE + Style.BRIGHT + "NEW" +
                        Fore.GREEN + Style.NORMAL + ", otherwise press " +
                        Fore.WHITE + Style.BRIGHT + "ENTER" +
                        Fore.GREEN + Style.NORMAL + ".\n\n")

    if user_start.lower().startswith("n"):
        create_journal()
    else:
        pass


def main():
    logging.basicConfig(filename=f'./logs/journal_log_{tm_stamp}.log',
                        format='%(asctime)s | %(message)s',
                        datefmt='%Y%m%d_%H:%M:%S',
                        level=logging.DEBUG
                        )
    logging.info('App Started')
    app_start()
    logging.info('App Finished')


if __name__ == '__main__':
    main()
