#example 1
class MyClass:
    pass

print(MyClass.__dict__)


#example 2
class Student:
    def __init__(self, student_id, student_name):
        self.student_id = student_id
        self.student_name = student_name
        self.student_class = None

    def display_attributes(self):
        print("Attributes and values:")
        for attr, value in self.__dict__.items():
            print(f"{attr}: {value}")

    def remove_attribute(self, attribute_name):
        if hasattr(self, attribute_name):
            delattr(self, attribute_name)

student_instance = Student(student_id=1, student_name="John")

student_instance.display_attributes()

student_instance.remove_attribute('student_name')

student_instance.display_attributes()


#example3
class BankAccount:
    def __init__(self, accountNumber, name, balance):
        self.accountNumber = accountNumber
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposit of Rs.{amount} successful.")
        else:
            print("Invalid deposit amount")

    def withdrawal(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawal of Rs.{amount} successful.")
        else:
            print("Invalid withdrawal amount or insufficient funds")

    def bank_fees(self):
        fees = 0.05 * self.balance
        self.balance -= fees
        print(f"Bank fees of Rs.{fees} applied")

    def display(self):
        print(f"Account Number: {self.accountNumber}")
        print(f"Account Holder: {self.name}")
        print(f"Balance: Rs.{self.balance}")

account1 = BankAccount(accountNumber=123456, name="John Doe", balance=1000)

account1.display()

account1.deposit(500)
account1.withdrawal(200)
account1.bank_fees()

account1.display()
