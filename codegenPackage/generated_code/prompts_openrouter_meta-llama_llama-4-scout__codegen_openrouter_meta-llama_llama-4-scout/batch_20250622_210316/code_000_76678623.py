"""
Generated Code Metadata:
========================
Original URL: https://metis2020.com
Prompt: Write a Python code snippet to implement a simple slot machine game using the QRIS payment method, considering the RTP and transaction ease mentioned on Satria4D.
Generated: DETERMINISTIC_76678623b41f4935
Batch ID: 20250622_210316
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
import hashlib

class SlotMachine:
    """
    A simple slot machine game.
    """
    def __init__(self):
        self.symbols = ['Cherry', 'Lemon', 'Orange', 'Plum', 'Bell', 'Bar', 'Seven']
        self.rtp = 0.95  # Return to player (RTP) percentage
        self.balance = 0

    def spin(self, bet):
        """
        Spin the slot machine.

        Args:
            bet (float): The bet amount.

        Returns:
            list: A list of three symbols.
        """
        if bet > self.balance:
            raise ValueError("Insufficient balance")

        self.balance -= bet
        reels = [random.choice(self.symbols) for _ in range(3)]

        # Simple win condition
        if reels[0] == reels[1] == reels[2]:
            win_amount = bet * 10
            self.balance += win_amount
            return reels, win_amount
        elif reels[0] == reels[1] or reels[1] == reels[2] or reels[0] == reels[2]:
            win_amount = bet * 2
            self.balance += win_amount
            return reels, win_amount
        else:
            return reels, 0

    def get_balance(self):
        return self.balance

    def deposit(self, amount):
        self.balance += amount


class QRISPayment:
    """
    A simple QRIS payment gateway.
    """
    def __init__(self):
        self.transaction_id = None

    def generate_qr_code(self, amount):
        """
        Generate a QR code for payment.

        Args:
            amount (float): The payment amount.

        Returns:
            str: A QR code string (simulated).
        """
        # Simulated QR code generation
        self.transaction_id = hashlib.sha256(str(amount).encode()).hexdigest()
        return f"QR Code: {self.transaction_id}"

    def verify_transaction(self, amount):
        """
        Verify a transaction.

        Args:
            amount (float): The payment amount.

        Returns:
            bool: True if the transaction is successful, False otherwise.
        """
        # Simulated transaction verification
        return self.transaction_id == hashlib.sha256(str(amount).encode()).hexdigest()


def main():
    slot_machine = SlotMachine()
    qris_payment = QRISPayment()

    print("Welcome to Satria4D Slot Machine!")
    print(f"RTP: {slot_machine.rtp * 100}%")

    while True:
        print("\n1. Deposit")
        print("2. Play")
        print("3. Check Balance")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            amount = float(input("Enter deposit amount: "))
            slot_machine.deposit(amount)
            print(f"Balance: {slot_machine.get_balance()}")
        elif choice == "2":
            if slot_machine.get_balance() < 100:
                print("Insufficient balance. Please deposit first.")
                continue

            bet = float(input("Enter bet amount: "))
            try:
                reels, win_amount = slot_machine.spin(bet)
                print(f"You spun: {reels[0]} | {reels[1]} | {reels[2]}")
                if win_amount > 0:
                    print(f"You won: {win_amount}")
                else:
                    print("Better luck next time!")

                print(f"Balance: {slot_machine.get_balance()}")

                # Optional: Pay using QRIS
                pay_with_qris = input("Pay using QRIS? (yes/no): ")
                if pay_with_qris.lower() == "yes":
                    qr_code = qris_payment.generate_qr_code(bet)
                    print(qr_code)

                    # Verify transaction
                    transaction_verified = qris_payment.verify_transaction(bet)
                    if transaction_verified:
                        print("Transaction successful!")
                    else:
                        print("Transaction failed. Please try again.")
            except ValueError as e:
                print(e)
        elif choice == "3":
            print(f"Balance: {slot_machine.get_balance()}")
        elif choice == "4":
            break
        else:
            print("Invalid option. Please choose again.")

if __name__ == "__main__":
    main()
```
