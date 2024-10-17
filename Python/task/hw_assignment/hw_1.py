class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance
        self.receipt = list()

    def deposit(self):
        deposit_amount = int(input("입금할 금액을 입력하세요: "))
        self.balance += deposit_amount
        self.receipt.append(("입금", deposit_amount, self.balance))
        print(f"새로운 잔액: {self.balance}")

    def print_receipt(self):
        print("영수증:", self.receipt)

# BankAccount 객체 생성 및 입금
account = BankAccount(balance=1000)
account.deposit()

# 영수증 출력
account.print_receipt()
