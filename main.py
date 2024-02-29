

from menu import Menu
from subscribers import subscribers
from acceptance import acceptance

print("")
print("סטטוס הספרים בספריה:")
print("1: הספר הוחזר בהצלחה. 2: הספר ממתין להחזרה. 3: הספר נלקח על ידך.")
print("")
print("")

import datetime
dade = datetime.date.today()

with open('Acceptance.txt', 'w') as Acceptance:
    Acceptance.write(f'תאריך לקיחת הספרים: {dade}\n ')
    pass


menu1 = Menu()
subscribers1 = subscribers()
acceptance1 = acceptance()
data_user = 'example'
user = input('הכנס מספר תעודת זהות : ')
with open('Acceptance.txt', 'a') as A:
    A.write(f'תעודת הזהות שנרשמה בהשאלה זאת: {user}. \n')
    A.write(f'\n')
while user != 'off' and data_user != 'off':
    data_user = subscribers1.IsSubscriber(user)
    if data_user == 'off':
        # with open('Acceptance.txt', 'a') as Acceptance:
        print('הקבלה מחכה לך בתיקיה...')
        break
    else:
        acceptance1.Receipt_file(user,data_user)




