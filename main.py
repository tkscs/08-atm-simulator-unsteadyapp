"""
Options:
- check the balance: prints current balance
- withdraw money:
    ask you how much to withdraw
    reduce the balance by that amount
    if you try to withdraw more than you have...
        print error don't update the balance
    don't withdraw a negative amount
- deposit money:
    ask you how to deposit
    increase the balance by that amount
    don't deposit a negative amount
- loop (with a while loop) until the user says "exit"
"""

# start with 1 million dollars
balance = 1000000

while True:
    UInput = input("Enter Action: ").lower().replace(" ","")
    if(UInput == "checkbalence"):
        print(f"Your balence is :{balance}")
    elif(UInput == "widthdraw"):
        try:
            howmuch = int(input("how much to widthdraw? "))
        except TypeError:
            print("must be an integer!")
        else:
            if(balance>=howmuch and howmuch>=0):
                balance = balance - howmuch
                print(f"You widthdrew {howmuch} & have {balance} left.")
            else:
                print("Negitive or greater than balance")
    elif(UInput=="deposit"):
        try:
            howmuch = int(input("how much to deposit? "))
        except TypeError:
            print("must be an integer!")
        else:
            if(howmuch>=0):
                balance = balance + howmuch
                print(f"You deposited {howmuch} & have {balance} left.")
            else:
                print("howmuch must be postive!")
    else:
        print(f"unrecognized input: {UInput}. Try checkbalence, deposit, or widthdraw")
        
        
        


