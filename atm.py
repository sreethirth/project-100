class Atm(object):

    def __init__(self,cardNumber,pinNumber):
            self.cardNumber=cardNumber
            self.pinNumber=pinNumber

    def cashWithDrawl(self):
        print("withDrawed")

    def balanceEnquiry(self):
        print('notEnquired')


sbi = Atm(4235,1234)

print(sbi.cardNumber)
print(sbi.cashWithDrawl())