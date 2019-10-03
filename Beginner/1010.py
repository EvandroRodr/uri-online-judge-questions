# PRODUCT 1
code1, qnt1, price1 = input().split()
product1 = int(qnt1) * float(price1)

#PRODUCT 2
code2, qnt2, price2 = input().split()
product2 = int(qnt2) * float(price2)

print("VALOR A PAGAR: R$ %0.2f" % (product1 + product2))