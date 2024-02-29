class MenuItem:
    """Models each Menu Item."""
    def __init__(self,code, name, count):
        self.code = code
        self.name = name
        self.count = count

class Menu:
    """Designs the menu with the books in the library."""
    def __init__(self):
        self.menu = [
            MenuItem(code =1, name="עשרים ואחד בבית אחד.", count=20),
            MenuItem(code =2, name="ילדים מספרים על עצמם.", count=30),
            MenuItem(code =3, name="הבלשים.", count=2),
            MenuItem(code =4, name="הנורמלי האחרון.", count=25),
            MenuItem(code =5, name="מטפסי הרים.", count=32),
            MenuItem(code =6, name="אפשר לקרוא לך אמא.", count=28)
        ]

    def get_items(self):
        """Returns all the names of the available menu items"""
        print('הספרים בספרייה: ')
        print_items = lambda menu:[print(f'קוד הספר:{item.code}   שם הספר:{item.name}   כמות הספרים שיש מספר זה:{item.count}') for item in menu]
        print_items(self.menu)


    def find(self, codes):
        """Searches in the menu for a specific book by name. Returns the item if it exists, otherwise returns none"""
        if codes == 'off':
            return 'off'
        for i in codes:
            if int(i) >= 1 or int(i) <= 6:
                print(f' {self.menu[int(i)-1].name}')
                self.menu[int(i) - 1].count = self.menu[int(i) - 1].count - 1
        return codes


    def enter_your_choice(self):
        """Enters the book he wants according to the book code"""
        self.get_items()
        choice = input("הזן את הקוד של הספר שאתה רוצה לקחת, אם אתה רוצה לסיים את ההזמנה, הזן OFF: ")
        if choice == 'off':
            return 'off'
        else:
            return self.find(choice.split())

