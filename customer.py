#Customer Class Initialization
class Customer:
    def __init__(self,first_name, last_name, account_num, rented_dvds):
        self.first_name = first_name
        self.last_name = last_name
        self.account_num = account_num
        self.rented_dvds = rented_dvds
    #Setters and Getters
    def set_first_name(self,first_name):
        self.first_name = first_name

    def get_first_name(self):
        return self.first_name

    def set_last_name(self,last_name):
        self.last_name = last_name

    def get_last_name(self):
        return self.last_name

    def set_account_num(self,account_num):
        self.account_num = account_num

    def get_account_num(self):
        return self.account_num

    def set_rented_dvds(self,rented_dvds):
        self.rented_dvds = rented_dvds

    def get_rented_dvds(self):
        return self.rented_dvds

    # override Comparison functions

    def __eq__(self, other):
        return self.account_num == other.account_num

    def __lt__(self, other):
        return self.account_num < other.account_num

    def __le__(self, other):
        return self.account_num <= other.account_num

    def __gt__(self, other):
        return self.account_num > other.account_num

    def __ge__(self, other):
        return self.account_num >= other.account_num

    def __str__(self):
        output = f"Name: {self.first_name} {self.last_name}, " \
                 f"Account Number: {self.account_num},  " \
                 f" Rented DVDs : {self.rented_dvds} "
        return output