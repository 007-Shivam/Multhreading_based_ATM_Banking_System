# Multhreading based ATM Banking System

This is a simple multithreading-based ATM banking system implemented in Python using the Tkinter library for GUI. The system allows users to perform various banking transactions such as withdrawal, deposit, and balance inquiry. The ATM class provides the core functionality for handling account authentication and transaction processing, while the ATM_GUI class creates a graphical user interface for interacting with the ATM.


# Features
* Account Authentication: Users are required to enter their account number and PIN to authenticate themselves before performing any transactions. This ensures the security and privacy of their accounts.

* Withdrawal: Users can withdraw a specified amount from their account. The system verifies the account credentials and checks if the account has sufficient funds before processing the withdrawal transaction.

* Deposit: Users can deposit a specified amount into their account. The system validates the account credentials and updates the account balance accordingly.

* Check Balance: Users can check the current balance of their account. The system verifies the account credentials and displays the balance information.

* Multithreading: Each transaction (withdrawal, deposit, and balance inquiry) is executed in a separate thread. This allows concurrent execution of transactions and improves system responsiveness.

* Thread Safety: To ensure data integrity and prevent race conditions, a lock mechanism is implemented using the threading module. The lock ensures that only one thread can access shared data (e.g., account balances) at a time.

# User Interface
The user interface of the system is a simple console-based interface. The interface allows users to
input their account number and PIN and select the type of transaction they want to perform. The
interface displays the result of the transaction, including the current account balance.

# Screenshot

![Cover Page](https://github.com/007-Shivam/Multhreading_based_ATM_Banking_System/assets/101915190/e95d4569-07f7-41f1-9d27-f85f1faa6fac)
