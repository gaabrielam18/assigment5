n = int(input("Enter the length of the sequence: ")) # Do not change this line

# Notandinn byrjar á því að slá inn tölu sem táknar hversu langa röð hann vill hafa 
# Síðan eru fyrstu 3 stökin plúsuð saman (summa fyrstu 3 staka) til þess að fá 4 stakið og svo frm.
# byrjum á því að skilgreika fyrstu 3 stökin til þess að fá 4 stakið 
# sem dæmi 1+2+3=6 og 6 er 4 stakið 

n1 = 0
n2 = 1 
n3 = 2

for i in range(n):
    sum_n = n1 + n2 + n3 
    n1 = n2 
    n2 = n3
    n3 = sum_n
    print(n1)


