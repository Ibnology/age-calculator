from datetime import datetime
import time
import sys
import os

def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear') # thx b0mb

clear()
print("")
print("")
print("-" *30 )
print("")
print("ＹＡＳ ＨＥＳＡＰＬＡＭＡ ＰＲＯＧＲＡＭＩ － ＡＵＴＨＯＲ ＩＢＲＡＨＩＭＢ") #aciklama kismi
print("")
print("-" *30 )
print("")
print("")


my_date = input("Dogum tarihinizi giriniz (gg/aa/yyyy): ")
print("")
b_date = datetime.strptime(my_date, '%d/%m/%Y')
clear()
print("Dogum tarihiniz: ", my_date)
print("Yasiniz : %d" % ((datetime.today() - b_date).days/365))

while True:
    print("")
    time.sleep(1)
    sor = input("Programdan cikmak icin 'q' tusuna basin, tekrar hesaplamak icin 'r' tusuna basin: ")

    if sor == "r":
      clear()  
      my_date = input("Dogum tarihinizi giriniz (gg/aa/yyyy): ")
      print("")
      b_date = datetime.strptime(my_date, '%d/%m/%Y')
      clear()
      print("Dogum tarihiniz: ", my_date)
      print("Yasiniz: %d" % ((datetime.today() - b_date).days/365))
      print("")
    if sor == "q":
        for x in range(1, 6)[::-1]:                         #
            sys.stdout.write('\r' + 'Cikiliyor ' + str(x))  # thx b0mb
            time.sleep(1)                                   #
        print("")
        break
