import re
abc_1 ="0030304167/F/1/0110053039080371SR"
abc_2 ="0030249016/G//10054179410008SR"

abc_4 = """PN 1 "30249016" CR 2 "G" PY 1 "20" PW 1 "20" SN 2 "0110054179410008" MI 1 "S" RI 1 "R" """

abc_5 = "0030261636/0H/2128/0110065210150287CR0"

# print(abc[15:31])

abc_3="0000006543210123"

ff=re.findall("/(\d{16})", abc_5)

d=abc_2.split('/')[-1].split('S')[0]
print(ff)