num_int = int(input("Input a number: "))    # Do not change this line
# Fill in the missing code
# Notandinn slær tölu að eigin vali 
# Viljum að kóðinn keyrist þangað til að einstaklingur slær ínn negatíva tölu 
# Síðan viljum við finna stærstu tölu sem notandinn hefur sláð inn sem er jákvæð tala 

max_int = num_int 
while num_int>=0:
    num_int = int(input("Input a number: "))
    if num_int>max_int:
        max_int = num_int



print("The maximum is", max_int)    # Do not change this line

