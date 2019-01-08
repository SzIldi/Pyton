def spendMoney(money):
    if (money < 500 and money >= 200):
        print "Fagyit veszek"
    elif (money >= 500):
        print "sok fagyit veszek"
    elif (money < 200):
        print "nem veszek fagyit"


number = int(raw_input("Please enter a value: "))

spendMoney(number)


#Nagyon nehez#

