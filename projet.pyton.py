print("welcome to saikrishna restaurant")
choice=input("enter the your choice:veg (or) nonveg:").lower()
if choice=="veg":
    print("he veg menu is below")
    print(f"{'ITEAM':<10}{'price':>50}")
    print("-"*75)
    print(f"{'idli':<10}{'50rs':>50}")
    print(f"{'dhosa':<10}{'50rs':>50}")
    print(f"{'vegbiriyanni':<10}{'100rs':>50}")
    print(f"{'chapathi':<10}{'50rs':>50}")
    print(f"{'parota':<10}{'50rs':>50}")
    print(f"{'pulihoraa':<10}{'50rs':>50}")
    print(f"{'veg friedrice':<10}{'100rs':>50}")
    print(f"{'veg noodles':<10}{'100rs':>50}")
    veg=input("enter your veg choice")
    q=int(input("enter your quantity"))
    if veg=='idli'or"dhosa"or"chapathi"or'parota'or'pulihoraa':
        totalbill=50*q
        print(f"total bill is:{totalbill}")
        print("thanking your's order")
    elif veg=='vegbiriyanni'or"veg friedrice"or"veg noodles":
        totalbill = 100 * q
        print(f"total bill is:{totalbill}")
        print("thanking your's order")

    else:
        print("please order in above menu")
elif choice=="nonveg":
    print("he veg menu is below")
    print(f"{'ITEAM':<10}{'price':>50}")
    print("-"*75)
    print(f"{'chickenidli':<10}{'100rs':>50}")
    print(f"{'chickendhosa':<10}{'100rs':>50}")
    print(f"{'biriyanni':<10}{'299rs':>50}")
    print(f"{'chickenchapathi':<10}{'100rs':>50}")
    print(f"{'chikenparota':<10}{'100rs':>50}")
    print(f"{'dumbiriyanni':<10}{'299rs':>50}")
    print(f"{'chicken friedrice':<10}{'299rs':>50}")
    print(f"{'egg friedrice':<10}{'100rs':>50}")
    print(f"{'egg noodles':<10}{'100rs':>50}")
    print(f"{'mandy':<10}{'299rs':>50}")
    print(f"{'stringbiriyanni':<10}{'299rs':>50}")
    print(f"{'chicken noodles':<10}{'299rs':>50}")
    print(f"{'froncebiriyanni':<10}{'299rs':>50}")
    print(f"{'chikenlollypop':<10}{'299rs':>50}")


    nonveg=input("enter your veg choice")
    q=int(input("enter your quantity"))
    if nonveg=="chickenidli"or"chickendhosa"or"chickenchapathi"or"chickenparota" or"egg friedrice"or"edd noddles":
        totalbill=100*q
        print(f"total bill is:{totalbill}")
        print("thanking your's order")
    elif veg == 'biriyanni' or "chicken friedrice" or "vhicken noodles"or"dumbiriyanni"or'mandy'or'stringbiriyanni'or"froncebiriyani"or"chekenlollypop":
        totalbill = 299 * q
        print(f"total bill is:{totalbill}")
        print("thanking your's order")

    else:
        print("please order in above menu")


        














