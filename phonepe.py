class phonepe:

    def __init__(self,q,p,bt,m,u,t,b,pb):

        self.__scanqr=q
        self.__payphoneno=p
        self.__banktransfer=bt
        self.__mobilerecharge=m
        self.__payupiid=u
        self.__transfer=t
        self.__balcheck=b
        self.__paybills=pb

    def display(self):

        self.__safe="lock"

        print("safety lock")


        self.__bankacclink="enter bank acc no"

        print("bank acc no")

        self.__transactions= "recent payment"

        print("recentpayment")

        self.__search="search box"

        print("search box")

        self.__discoverbusiness="tickets"

        print("travel options")

        self.__transaction="history"

        print("transact history")


    def promotions(self):

        self.__cashback="scratch card"

        print("scratch card")

        self.__invite="invite contacts"

        print("invite contacts")



    def link(self):

        self.__linkacc="link google"

        print("link with gmail acc")


customer=phonepe("qr","phoneno","banktransfer","mobilerecharge","upiid","selftransfer","checkbal","paybill")
customer.display()
customer.promotions()


if ("bank account number<12"):
    raise ValueError("invalid bank acc no")
elif print("welcome"):

    if ("scratchcard"==0):

        print("better luck next time") 

elif print (" you won"):

    
    if ("linkedproperly"):
        print("welcome to phonepe,have a good day!")
              
