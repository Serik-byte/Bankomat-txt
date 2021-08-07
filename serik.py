# Bankomat ishlash tizimi
import random
from pymongo import MongoClient
from datetime import datetime

# cluster = MongoClient("mongodb+srv://Freedom333:kires5889900@cluster0.yvn1l.mongodb.net/Bankomat?retryWrites=true&w=majority")
# db = cluster.Bankomat
# collections = db.Bankomatcoll
# name = input("enter: ")
# collection.insert_one({"_id": 1, "name": name, "balance": 200})


class Bankomat:
    def __init__(self):
        self.balance = 0
        self.try_count = 4
        self.print_motion = {
            "uz": {
                "welcome": "ALPHA BANK\" ga hush kelibsiz",
                "menu": "\nHisob ochish uchun 1-ni kiriting\n"
                        "Hisobni toldirish uchun 2-ni kiriting\n"
                        "Hisobdan pul yechish uchun 3-ni kiriting\n"
                        "Pul jonatish uchun 4-ni kiriting\n"
                        "Hisobni tekshirish uchun 5-ni kiriting\n"
                        "Tizimni ochirish uchun 0 ni kiriting\n",

                "eslatma": "\nEslatma parol 6 ta sondan kam bolmasligi lozim!",
                "bank": "\nBizning bankimiz foydalanuvchilariga 500 $ qiymatda pul hadiya qilinayapdi!",
                "bank_bank": "\nBiz bilan ekaningiz uchun raxmat!!!",
                "parol": "\nParol 6 ta sondan kam bolmasligi lozim sizda yana urinish mavjud!",
                "eslatma_acc": "\nEslatma pul yechish jarayonida sizdan 1%-lik komissiya miqdori yechib olindi",
                "kiritingg": "\nJonatish uchun 1-ni kiriting \n Jonatmaslik uchun 2-ni kiriting",
                "karta": "\nKarta raqami notog'ri kiritilgan tekshirib qaytadan kiriting",
                "bekor_qilish": "\nPul jonatmasi bekor qilindi!",
                "good_bye": "ALPHA BANK\" Bizning bankimizni tanlaganingiz uchun raxmat!!!"
            }
        }

    def printf(self, name_dict, name_massive):
        print(self.print_motion[name_dict][name_massive])

    # 1 Hisob ochish
    def reception(self):
        self.name = input("Ism.F kiriting: ")
        self.file = open(str(self.name) + '.txt', 'a', encoding='utf-8')
        self.id = random.randrange(8600000000000000, 8600999999999999)
        count = 4
        e = 4
        self.printf(name_dict="uz", name_massive="eslatma")
        while count > 0:
            self.password = int(input("Parolni kiriting: "))
            if self.password > 19999:
                print(self.name, "Nomidagi hisobga kirish", "omadli yakunlandi", "sizning karta raqamingiz",
                      self.id)
                self.balance += 500
                self.printf(name_dict="uz", name_massive="bank")
                self.printf(name_dict="uz", name_massive="bank_bank")
                break
            else:
                e -= 1
                count -= 1
                self.printf(name_dict="uz", name_massive="parol")
        self.base = 'Account has been create for: {} {} \n password: {} \n card number: {} \n'.format(self.name,datetime.now(),self.password,self.id)
        self.file.writelines(self.base)
        self.file.close()

    # 2 Hisobni toldirish
    def addMoney(self):
        self.file = open(str(self.name) + '.txt', 'a', encoding='utf-8')
        self.money = int(input("Hisobingizni qanchaga toldirmoqchisiz?: "))
        self.balance += self.money
        print("Sizning hisobingiz", self.money, "$ ga", "toldirildi")
        print("Sizning hisobingizda", self.balance, "$", "mavjud")
        self.base = 'Your balance full {} $'.format(self.money)
        self.file.writelines(self.base)
        self.file.close()

    # 3 Pul yechish
    def getMoney(self):
        self.file = open(str(self.name) + '.txt', 'a', encoding='utf-8')
        self.printf(name_dict="uz", name_massive="eslatma_acc")
        self.money = int(input("Qancha yechib olmoqchisiz?: "))
        if self.money >= self.balance + (self.money * 0.01):
            print("Sizda mablag yetarli emas!")
        else:
            self.balance -= self.money + (self.money * 0.01)
            print(self.money, "$ sizning hisobingizdan yechib olindi")
            print("Sizning hisobingiz", self.balance, "$ ni tashkil etadi")
        self.file.close()

    # 4 pul jonatish
    def go_Money(self):
        self.file = open(str(self.name) + '.txt', 'a', encoding='utf-8')
        again = 4
        again2 = 4
        while again > 0:
            self.card_code = int(input("Pul jonatiladigan kartaning raqamini kiriting: "))
            if self.card_code >= 8600000000000000 and self.card_code <= 8600999999999999:
                self.give_money = int(input("Qancha jonatmoqchisiz: "))
                print("Siz", self.give_money, "$ ni", self.card_code, "jonatmoqchimisiz?")
                self.printf(name_dict="uz", name_massive="eslatma_acc")
                self.printf(name_dict="uz", name_massive="kiritingg")
                self.go_go_money = int(input("Kiriting: "))
                if self.go_go_money == 1:
                    self.balance -= self.give_money + (self.give_money * 0.01)
                    print(self.card_code, "raqamli kartaga", self.give_money, "$ pul otqazildi")
                    print("Sizning hisobingiz", self.balance, "$-ni tashkil etadi")
                    break
                else:
                    self.printf(name_dict="uz", name_massive="bekor_qilish")
                    break
            else:
                print()
                again -= 1
                again2 -= 1
                self.printf(name_dict="uz", name_massive="karta")
                print("Sizda yana {} imkoniyat bor!".format(again2))
        self.file.close()

    # 5 balansni tekshirish
    def viewBalance(self):
        print("Sizning hisobingiz", self.balance, "$-ni tashkil etadi")

    # Ikkinchi menu
    def menu_Bankomat(self):
        ALPHABANK = Bankomat()
        self.printf(name_dict="uz", name_massive="welcome")
        while (True):
            self.printf(name_dict="uz", name_massive="menu")
            user_input = int(input("Kiriting: "))
            print("")
            if user_input == 1:
                ALPHABANK.reception()
            if user_input == 2:
                ALPHABANK.addMoney()
            elif user_input == 3:
                ALPHABANK.getMoney()
            elif user_input == 4:
                ALPHABANK.go_Money()
            elif user_input == 5:
                ALPHABANK.viewBalance()
            elif user_input == 0:
                self.printf(name_dict="uz", name_massive="good_bye")

                break


mainning = Bankomat()
mainning.menu_Bankomat()