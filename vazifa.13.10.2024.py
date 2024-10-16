# def kopaytma(*sonlar):
#     natija = 1
#     for son in sonlar:
#         natija *= son
#     return natija
#
#
# natija = kopaytma(2, 3, 4)
# print(natija)



# 2 ish


# def kvadratga_yoz(param1, param2, param3, *sonlar):
#     kvadratlar = [param1 ** 2, param2 ** 2, param3 ** 2]
#
#     for son in sonlar:
#         kvadratlar.append(son ** 2)
#
#     return kvadratlar
#
# natija = kvadratga_yoz(2, 3, 4, 5, 6)
# print(natija)  # Natija: [4, 9, 16, 25, 36]



# 3 ish


# def talaba_malumotlari(ism, familiya, qoshimcha_mlumotlar):
# talaba = {
#     'Ism': ism,
#     'Familiya': familiya
# }
#
# for kalit, qiymat in qoshimcha_malumotlar.items():
#     talaba[kalit] = qiymat
#
# return talaba
#
# talaba_info = talaba_ma
# 'lumotlari('Ali', 'Valiyev', yosh=20, fakultet='Matematika', kurs=2)
# print(talaba_info)

