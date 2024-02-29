from menu import Menu, MenuItem
from subscribers import subscribers
import  datetime
dade = datetime.date.today()
menu1 = Menu()
subscribers1 = subscribers()


class acceptance:
    """Opening a file - receipt. and listed the private invitation into it."""
    def Receipt_file(self,id,data_user):
        user = data_user[id]
        data_book = menu1.menu
        with open('Acceptance.txt', 'a') as Acceptance:
            for i in user:
                for j in data_book:
                    if int(i) == int(j.code):
                        Acceptance.write(f'  קוד הספר:{j.code}  שם הספר: {j.name}\n  ,')

                        # Acceptance.write(f'קוד הספר: {j.code}\n , שם הספר:{j.name}\n  תאריך לקיחת הספר:   ,')
            for i in user:
                if user[i]==3:
                    user[i]=2
