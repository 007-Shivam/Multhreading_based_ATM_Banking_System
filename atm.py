#By Shivam Bhosle
import threading
import time
import tkinter as tk

class ATM:
    def __init__(self):
        self.accounts = {
            123456789: {"pin": 1234, "balance": 10000},
            987654321: {"pin": 5678, "balance": 2000},
            456789123: {"pin": 9012, "balance": 500},
        }
        self.lock = threading.Lock()

    def authenticate(self, account_number, pin):
        if account_number in self.accounts and self.accounts[account_number]["pin"] == pin:
            return True
        return False

    def withdraw(self, account_number, pin, amount):
        print("Thread ID:", threading.get_ident(), "- Starting withdrawal transaction")
        time.sleep(1)
        if not self.authenticate(account_number, pin):
            return "Invalid credentials"

        with self.lock:
            if self.accounts[account_number]["balance"] < amount:
                return "Insufficient funds"
            self.accounts[account_number]["balance"] -= amount
            return "Transaction successful"

    def deposit(self, account_number, pin, amount):
        print("Thread ID:", threading.get_ident(), "- Starting deposit transaction")
        time.sleep(1)
        if not self.authenticate(account_number, pin):
            return "Invalid credentials"

        with self.lock:
            self.accounts[account_number]["balance"] += amount
            return "Transaction successful"

    def check_balance(self, account_number, pin):
        print("Thread ID:", threading.get_ident(), "- Starting check balance transaction")
        time.sleep(1)
        if not self.authenticate(account_number, pin):
            return "Invalid credentials"

        with self.lock:
            return f"Your balance is {self.accounts[account_number]['balance']}"

class ATM_GUI:
    def __init__(self):
        self.atm = ATM()

        self.window = tk.Tk()
        self.window.title("ATM")
        self.window.geometry("400x350")
        self.window.config(bg='#FFFFE0')

        self.account_label = tk.Label(self.window, text="Account number:", font=("Arial", 12), bg='#FFFFE0')
        self.account_label.pack()
        self.account_entry = tk.Entry(self.window, font=("Arial", 12))
        self.account_entry.pack()

        self.pin_label = tk.Label(self.window, text="PIN:", font=("Arial", 12), bg='#FFFFE0')
        self.pin_label.pack()
        self.pin_entry = tk.Entry(self.window, show="*", font=("Arial", 12))
        self.pin_entry.pack()

        self.amount_label = tk.Label(self.window, text="Amount:", font=("Arial", 12), bg='#FFFFE0')
        self.amount_label.pack()
        self.amount_entry = tk.Entry(self.window, font=("Arial", 12))
        self.amount_entry.pack()

        self.balance_label = tk.Label(self.window, text="", font=("Arial", 12), bg='#FFFFE0')
        self.balance_label.pack()

        self.withdraw_button = tk.Button(self.window, text="Withdraw", font=("Arial", 12), command=self.withdraw, bg='#FF5733', fg='white', padx=10, pady=5, bd=5)
        self.withdraw_button.pack(pady=5)

        self.deposit_button = tk.Button(self.window, text="Deposit", font=("Arial", 12), command=self.deposit, bg='#6A5ACD', fg='white', padx=10, pady=5, bd=5)
        self.deposit_button.pack(pady=5)

        self.balance_button = tk.Button(self.window, text="Check balance", font=("Arial", 12), command=self.check_balance, bg='#20B2AA', fg='white', padx=10, pady=5, bd=5)
        self.balance_button.pack(pady=5)

        self.message_label = tk.Label(self.window, text="", font=("Arial", 12), bg='#FFFFE0', fg='red')
        self.message_label.pack()

        self.window.mainloop()

    def withdraw(self):
        try:
            account_number = int(self.account_entry.get())
        except ValueError:
            self.message_label.config(text="Please enter a valid account number")
            
            return
        try:
            pin = int(self.pin_entry.get())
        except ValueError:
            self.message_label.config(text="Incorrect PIN")
            return
    
        try:
            amount = int(self.amount_entry.get())
        except ValueError:
            self.message_label.config(text="Please enter a valid amount")
            return
        threading.Thread(target=self.do_withdraw, args=(account_number, pin, amount)).start()

    def do_withdraw(self, account_number, pin, amount):
        result = self.atm.withdraw(account_number, pin, amount)
        self.message_label.config(text=result)
        self.amount_entry.delete(0, tk.END)

    def deposit(self):
        try:
            account_number = int(self.account_entry.get())
        except ValueError:
            self.message_label.config(text="Please enter a valid account number")
            
            return
        try:
            pin = int(self.pin_entry.get())
        except ValueError:
            self.message_label.config(text="Incorrect PIN")
            return
    
        try:
            amount = int(self.amount_entry.get())
        except ValueError:
            self.message_label.config(text="Please enter a valid amount")
            return
        threading.Thread(target=self.do_deposit, args=(account_number, pin, amount)).start()

    def do_deposit(self, account_number, pin, amount):
        result = self.atm.deposit(account_number, pin, amount)
        self.message_label.config(text=result)
        self.amount_entry.delete(0, tk.END)

    def check_balance(self):
        try:
            account_number = int(self.account_entry.get())
        except ValueError:
            self.message_label.config(text="Please enter a valid account number")
            
        try:
            pin = int(self.pin_entry.get())
        except ValueError:
            self.message_label.config(text="Incorrect PIN")
            return
        threading.Thread(target=self.do_check_balance, args=(account_number, pin)).start()

    def do_check_balance(self, account_number, pin):
        result = self.atm.check_balance(account_number, pin)
        self.balance_label.config(text=result)
        self.message_label.config(text="")
        self.amount_entry.delete(0, tk.END)

if __name__ == "__main__":
    ATM_GUI()