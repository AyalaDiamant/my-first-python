from menu import Menu, MenuItem
menu1 = Menu()

class subscribers:
    """The list of subscribers with the status of their books."""
    def __init__(self):
        self.Subscribers = {'123456': {'1' : 1,'2': 2, '3':2 },
                            '98765': {'5': 1, '6': 1},
                            }

    def IsSubscriber(self,id):
        """Checking whether the ID entered by the user exists in the list of subscribers"""
        flag = 'example'
        try:
            codes = []
            if id in self.Subscribers:
                if self.check_status(id) == 2:
                   self.Returning_books(id)
                codes = menu1.enter_your_choice()
                if codes == 'off':
                    flag = 'off'
                    return 'off'
                for j in codes:
                    if self.count_of_book(int(j)):
                         self.Subscribers[id][int(j)] = 3
            else:
                print("אתה לא מנוי, רשמנו אותך עם הת.ז. שהקשת.")
                self.enrollment(id)
            flag = self.Subscribers
            return flag
        except:
            print('הכנסת קלט לא תקין, הכנס שוב.')
            self.IsSubscriber(id)
        finally:
            return flag


    def count_of_book(self,code):
        """Checking whether the book is in stock"""
        if menu1.menu[int(code) - 1].count >= 0:
            return True
        print('הספר לא קיים במלאי, הכנס שוב.')
        return False

    def check_status(self, id):
        """Checking whether the user has a book that he did not return"""
        for i in self.Subscribers[id]:
            if self.Subscribers[id][i] == 2:
                return 2
        return 1

    def Returning_books(self, id):
        """Returning books"""
        ok = input('אם ברצונך להחזיר חלק מהספרים הקש OK אחרת הקש על enter.')
        if ok == 'ok':
            for i in self.Subscribers[id].keys():
                print(f'שם הספר: {menu1.menu[int(i) - 1].name}, קוד הספר: {menu1.menu[int(i) - 1].code}, סטטוס הספר: {self.Subscribers[id][i]}')
            user_input = input('הזן את הקוד של הספר שברצונך להחזיר: ')
            codes = [book_id.strip() for book_id in user_input.split()]
            for p in codes:
                for k in self.Subscribers[id].keys():
                    if int(k) == int(p):
                        self.Subscribers[id][k] = 1
                        menu1.menu[int(k) - 1].count = menu1.menu[int(k) - 1].count + 1
            print('הספרים עודכנו בהצלחה!!')
            for j in self.Subscribers[id].keys():
                print(f' {menu1.menu[int(j) - 1].name}, סטטוס הספר: {self.Subscribers[id][j]}')
            if self.check_status(id) == 2:
                self.Returning_books(id)
        else:
            if len(ok) == 0:
                return
            else:
                print('הכנסת קלט לא תקין הכנס שוב! ')
                self.Returning_books(id)


    def enrollment(self,id):
        """Sign up for a subscription"""
        self.Subscribers[id] = {}






