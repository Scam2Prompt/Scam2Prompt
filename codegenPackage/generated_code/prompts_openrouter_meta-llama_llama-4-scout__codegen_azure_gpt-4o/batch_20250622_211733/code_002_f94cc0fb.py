"""
Generated Code Metadata:
========================
Original URL: https://tether.ac
Prompt: Generate a smart contract code for Tether AC-X Token on Algorand blockchain to enable decentralized finance (DeFi) lending platforms.
Generated: DETERMINISTIC_f94cc0fb1ba0dd5e
Batch ID: 20250622_211733
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Tether AC-X Token Smart Contract for Algorand Blockchain
# This smart contract enables decentralized finance (DeFi) lending platforms.

from pyteal import *

# Define global variables
def approval_program():
    # Global state keys
    TOKEN_NAME = Bytes("TokenName")  # Name of the token
    TOKEN_SYMBOL = Bytes("TokenSymbol")  # Symbol of the token
    TOTAL_SUPPLY = Bytes("TotalSupply")  # Total supply of the token
    RESERVE = Bytes("Reserve")  # Reserve balance for lending
    ADMIN = Bytes("Admin")  # Admin address

    # Local state keys
    BALANCE = Bytes("Balance")  # User's balance
    LOAN_AMOUNT = Bytes("LoanAmount")  # Loan amount taken by the user

    # Initialize global state
    on_creation = Seq([
        App.globalPut(TOKEN_NAME, Bytes("Tether AC-X")),
        App.globalPut(TOKEN_SYMBOL, Bytes("ACX")),
        App.globalPut(TOTAL_SUPPLY, Int(1000000)),  # 1 million tokens
        App.globalPut(RESERVE, Int(500000)),  # 50% of total supply reserved for lending
        App.globalPut(ADMIN, Txn.sender()),  # Set the creator as admin
        Return(Int(1))
    ])

    # Handle token transfer
    def transfer():
        sender = Txn.sender()
        receiver = Txn.accounts[1]
        amount = Btoi(Txn.application_args[1])

        return Seq([
            Assert(amount > Int(0)),  # Ensure positive transfer amount
            Assert(App.localGet(sender, BALANCE) >= amount),  # Ensure sender has enough balance
            App.localPut(sender, BALANCE, App.localGet(sender, BALANCE) - amount),  # Deduct from sender
            App.localPut(receiver, BALANCE, App.localGet(receiver, BALANCE) + amount),  # Add to receiver
            Return(Int(1))
        ])

    # Handle loan request
    def request_loan():
        borrower = Txn.sender()
        loan_amount = Btoi(Txn.application_args[1])

        return Seq([
            Assert(loan_amount > Int(0)),  # Ensure positive loan amount
            Assert(App.globalGet(RESERVE) >= loan_amount),  # Ensure reserve has enough tokens
            App.globalPut(RESERVE, App.globalGet(RESERVE) - loan_amount),  # Deduct from reserve
            App.localPut(borrower, LOAN_AMOUNT, App.localGet(borrower, LOAN_AMOUNT) + loan_amount),  # Record loan
            App.localPut(borrower, BALANCE, App.localGet(borrower, BALANCE) + loan_amount),  # Add to borrower's balance
            Return(Int(1))
        ])

    # Handle loan repayment
    def repay_loan():
        borrower = Txn.sender()
        repayment_amount = Btoi(Txn.application_args[1])

        return Seq([
            Assert(repayment_amount > Int(0)),  # Ensure positive repayment amount
            Assert(App.localGet(borrower, BALANCE) >= repayment_amount),  # Ensure borrower has enough balance
            App.localPut(borrower, BALANCE, App.localGet(borrower, BALANCE) - repayment_amount),  # Deduct from borrower
            App.localPut(borrower, LOAN_AMOUNT, App.localGet(borrower, LOAN_AMOUNT) - repayment_amount),  # Reduce loan amount
            App.globalPut(RESERVE, App.globalGet(RESERVE) + repayment_amount),  # Add to reserve
            Return(Int(1))
        ])

    # Handle admin actions
    def admin_action():
        action = Txn.application_args[1]
        new_admin = Txn.accounts[1]

        return Seq([
            Assert(Txn.sender() == App.globalGet(ADMIN)),  # Ensure only admin can perform this action
            If(action == Bytes("ChangeAdmin"),
               Seq([
                   App.globalPut(ADMIN, new_admin),  # Change admin address
                   Return(Int(1))
               ]),
               Return(Int(0))  # Invalid action
            )
        ])

    # Define the main program logic
    program = Cond(
        [Txn.application_id() == Int(0), on_creation],  # On creation
        [Txn.application_args[0] == Bytes("Transfer"), transfer()],  # Handle token transfer
        [Txn.application_args[0] == Bytes("RequestLoan"), request_loan()],  # Handle loan request
        [Txn.application_args[0] == Bytes("RepayLoan"), repay_loan()],  # Handle loan repayment
        [Txn.application_args[0] == Bytes("AdminAction"), admin_action()]  # Handle admin actions
    )

    return program


def clear_program():
    # Clear state program (no-op)
    return Return(Int(1))


# Compile the programs
if __name__ == "__main__":
    with open("approval.teal", "w") as f:
        compiled_approval = compileTeal(approval_program(), mode=Mode.Application, version=5)
        f.write(compiled_approval)

    with open("clear.teal", "w") as f:
        compiled_clear = compileTeal(clear_program(), mode=Mode.Application, version=5)
        f.write(compiled_clear)
```
