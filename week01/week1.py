from datetime import datetime
discount_rate =.1
tax_rate =.06


today = datetime.now ()
dow = today.weekday()
subtotal =float(input("enter subtotal: "))
print(f"total order {subtotal}")
discount = 0
print = int(input("what is the quantity?: "))
while quantity !=0:
    quantity = int(input("what is the quantity?: "))
    if quantity !=0:
       price = float(input("what is the price?: "))
discount = 0
if dow ==2 or dow ==3 or dow == 5:
    if subtotal >50:

       discount = subtotal*discount_rate

print(f"discount {discount}")
print (f"you can get a discount{discount}")
subtotal-=discount
tax = subtotal * tax_rate
total = subtotal + tax
print(f"tax {tax}")
print(F"total due {total}")
