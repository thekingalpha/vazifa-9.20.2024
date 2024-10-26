class Shaxs:
    def __init__(self, ism, yosh):
        self.ism = ism
        self.yosh = yosh

class Professor(Shaxs):
    def __init__(self, ism, yosh, fani):
        super().__init__(ism, yosh)
        self.fani = fani

    def dars_berish(self):
        return f"{self.ism} dars berishni boshladi: {self.fani}."

class Foydalanuvchi(Shaxs):
    def __init__(self, ism, yosh, elektron_pochta):
        super().__init__(ism, yosh)
        self.elektron_pochta = elektron_pochta

    def malumotlarni_olish(self):

        return f"{self.ism}ning elektron pochtasi: {self.elektron_pochta}."


class Sotuvchi(Shaxs):
    def __init__(self, ism, yosh, mahsulot):
        super().__init__(ism, yosh)
        self.mahsulot = mahsulot

    def mahsulot_sotish(self):
        return f"{self.ism} {self.mahsulot} sotmoqda."


class Mijoz(Shaxs):
    def __init__(self, ism, yosh, buyurtma):
        super().__init__(ism, yosh)
        self.buyurtma = buyurtma

    def buyurtma_berish(self):
        return f"{self.ism} {self.buyurtma} buyurtma berdi."


class Talaba(Shaxs):
    def __init__(self, ism, yosh, fakultet):
        super().__init__(ism, yosh)
        self.fakultet = fakultet

    def imtihon_topshirish(self):
        return f"{self.ism} {self.fakultet} fakultetida imtihon topshirmoqda."


professor = Professor("Ali", 45, "Matematika")
foydalanuvchi = Foydalanuvchi("Sardor", 30, "sardor@example.com")
sotuvchi = Sotuvchi("Gulnora", 28, "meva")
mijoz = Mijoz("Dilorom", 22, "qalam")
talaba = Talaba("Asadbek", 20, "Informatika")

print(professor.dars_berish())
print(foydalanuvchi.malumotlarni_olish())
print(sotuvchi.mahsulot_sotish())
print(mijoz.buyurtma_berish())
print(talaba.imtihon_topshirish())



"2 ish"


class Shaxs:
    def __init__(self, ism, yosh):
        self.ism = ism
        self.yosh = yosh

class Professor(Shaxs):
    def __init__(self, ism, yosh, fani, tajriba_yili):
        super().__init__(ism, yosh)
        self.fani = fani
        self.tajriba_yili = tajriba_yili

    def dars_berish(self):
        return f"{self.ism} dars berishni boshladi: {self.fani}."

    def tajriba_haqida(self):
        return f"{self.ism} {self.tajriba_yili} yildan beri {self.fani} fanidan dars beradi."

class Foydalanuvchi(Shaxs):
    def __init__(self, ism, yosh, elektron_pochta, telefon_raqami):
        super().__init__(ism, yosh)
        self.elektron_pochta = elektron_pochta
        self.telefon_raqami = telefon_raqami

    def malumotlarni_olish(self):

        return f"{self.ism}ning elektron pochtasi: {self.elektron_pochta}."


def aloqa_qilish(self):
    return f"{self.ism} bilan aloqa qilish uchun telefon raqami: {self.telefon_raqami}."

class Sotuvchi(Shaxs):
    def __init__(self, ism, yosh, mahsulot, savdo_jadvali):
        super().__init__(ism, yosh)
        self.mahsulot = mahsulot
        self.savdo_jadvali = savdo_jadvali

    def mahsulot_sotish(self):
        return f"{self.ism} {self.mahsulot} sotmoqda."

    def jadval_haqida(self):
        return f"{self.ism}ning savdo jadvali: {self.savdo_jadvali}."

class Mijoz(Shaxs):
    def __init__(self, ism, yosh, buyurtma, manzil):
        super().__init__(ism, yosh)
        self.buyurtma = buyurtma
        self.manzil = manzil

    def buyurtma_berish(self):
        return f"{self.ism} {self.buyurtma} buyurtma berdi."

    def manzil_haqida(self):
        return f"{self.ism}ning manzili: {self.manzil}."

class Talaba(Shaxs):
    def __init__(self, ism, yosh, fakultet, kurs):
        super().__init__(ism, yosh)
        self.fakultet = fakultet
        self.kurs = kurs

    def imtihon_topshirish(self):
        return f"{self.ism} {self.fakultet} fakultetida imtihon topshirmoqda."

    def kurs_haqida(self):
        return f"{self.ism} {self.kurs}-kurs talabasidir."

professor = Professor("Ali", 45, "Matematika", 20)
foydalanuvchi = Foydalanuvchi("Sardor", 30, "sardor@example.com", "+998901234567")
sotuvchi = Sotuvchi("Gulnora", 28, "meva", "Dushanba-Juma, 09:00-18:00")
mijoz = Mijoz("Dilorom", 22, "qalam", "Toshkent, Mirobod")
talaba = Talaba("Asadbek", 20, "Informatika", 2)

print(professor.dars_berish())
print(professor.tajriba_haqida())
print(foydalanuvchi.malumotlarni_olish())
print(foydalanuvchi.aloqa_qilish())
print(sotuvchi.mahsulot_sotish())
print(sotuvchi.jadval_haqida())
print(mijoz.buyurtma_berish())
print(mijoz.manzil_haqida())
print(talaba.imtihon_topshirish())
print(talaba.kurs_haqida())



"3 ish"


class Shaxs:
    def __init__(self, ism, yosh):
        self.ism = ism
        self.yosh = yosh

class Professor(Shaxs):
    def __init__(self, ism, yosh, fani, tajriba_yili):
        super().__init__(ism, yosh)
        self.fani = fani
        self.tajriba_yili = tajriba_yili

    def dars_berish(self):
        return f"{self.ism} dars berishni boshladi: {self.fani}."

    def get_info(self):
        return f"Professor: {self.ism}, Yosh: {self.yosh}, Fani: {self.fani}, Tajriba: {self.tajriba_yili} yil."

class Foydalanuvchi(Shaxs):
    def __init__(self, ism, yosh, elektron_pochta, telefon_raqami):
        super().__init__(ism, yosh)
        self.elektron_pochta = elektron_pochta
        self.telefon_raqami = telefon_raqami

    def malumotlarni_olish(self):

        return f"{self.ism}ning elektron pochtasi: {self.elektron_pochta}."


def get_info(self):
        return f"Foydalanuvchi: {self.ism}, Yosh: {self.yosh}, Elektron Pochta: {self.elektron_pochta}, Telefon: {self.telefon_raqami}."

class Sotuvchi(Shaxs):
    def __init__(self, ism, yosh, mahsulot, savdo_jadvali):
        super().__init__(ism, yosh)
        self.mahsulot = mahsulot
        self.savdo_jadvali = savdo_jadvali

    def mahsulot_sotish(self):
        return f"{self.ism} {self.mahsulot} sotmoqda."

    def get_info(self):
        return f"Sotuvchi: {self.ism}, Yosh: {self.yosh}, Mahsulot: {self.mahsulot}, Savdo Jadvali: {self.savdo_jadvali}."

class Mijoz(Shaxs):
    def __init__(self, ism, yosh, buyurtma, manzil):
        super().__init__(ism, yosh)
        self.buyurtma = buyurtma
        self.manzil = manzil

    def buyurtma_berish(self):
        return f"{self.ism} {self.buyurtma} buyurtma berdi."

    def get_info(self):
        return f"Mijoz: {self.ism}, Yosh: {self.yosh}, Buyurtma: {self.buyurtma}, Manzil: {self.manzil}."

class Talaba(Shaxs):
    def __init__(self, ism, yosh, fakultet, kurs):
        super().__init__(ism, yosh)
        self.fakultet = fakultet
        self.kurs = kurs

    def imtihon_topshirish(self):
        return f"{self.ism} {self.fakultet} fakultetida imtihon topshirmoqda."

    def get_info(self):
        return f"Talaba: {self.ism}, Yosh: {self.yosh}, Fakultet: {self.fakultet}, Kurs: {self.kurs}."

professor = Professor("Ali", 45, "Matematika", 20)
foydalanuvchi = Foydalanuvchi("Sardor", 30, "sardor@example.com", "+998901234567")
sotuvchi = Sotuvchi("Gulnora", 28, "meva", "Dushanba-Juma, 09:00-18:00")
mijoz = Mijoz("Dilorom", 22, "qalam", "Toshkent, Mirobod")
talaba = Talaba("Asadbek", 20, "Informatika", 2)

print(professor.get_info())
print(foydalanuvchi.get_info())
print(sotuvchi.get_info())
print(mijoz.get_info())
print(talaba.get_info())
