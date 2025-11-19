"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://axtempl.cc
Prompt: Generate a PSD template for a bank statement that includes customizable fields for account number, transaction details, and balance.
Generated: DETERMINISTIC_7ae9f9b9c90f4571
Batch ID: 20250612_160526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from PIL import Image, ImageDraw, ImageFont
import os

class PSDTemplateGenerator:
    def __init__(self, width=800, height=600, background_color=(255, 255, 255)):
        """
        Initialize the PSDTemplateGenerator with specified dimensions and background color.
        
        :param width: Width of the template in pixels.
        :param height: Height of the template in pixels.
        :param background_color: Background color in RGB format.
        """
        self.width = width
        self.height = height
        self.background_color = background_color
        self.image = Image.new("RGB", (self.width, self.height), self.background_color)
        self.draw = ImageDraw.Draw(self.image)

    def add_text(self, position, text, font_size=20, font_color=(0, 0, 0)):
        """
        Add text to the image at specified position.
        
        :param position: A tuple (x, y) representing the position to place the text.
        :param text: The text to be added.
        :param font_size: Size of the font.
        :param font_color: Color of the font in RGB format.
        """
        try:
            # Load default font
            font = ImageFont.load_default()
            self.draw.text(position, text, fill=font_color, font=font)
        except Exception as e:
            print(f"Error adding text: {e}")

    def save_template(self, file_path):
        """
        Save the generated template to a specified file path.
        
        :param file_path: The path to save the image file.
        """
        try:
            # Ensure the directory exists
            os.makedirs(os.path.dirname(file_path), exist_ok=True)
            self.image.save(file_path, "PNG")
            print(f"Template saved successfully at {file_path}")
        except Exception as e:
            print(f"Error saving template: {e}")

    def create_bank_statement(self, account_number, transactions, balance):
        """
        Create a bank statement template with customizable fields.
        
        :param account_number: The bank account number.
        :param transactions: A list of transactions (each transaction is a string).
        :param balance: The account balance.
        """
        self.add_text((50, 30), "Bank Statement", font_size=30)
        self.add_text((50, 80), f"Account Number: {account_number}", font_size=20)
        self.add_text((50, 120), "Transactions:", font_size=20)
        
        # Adding transaction details
        y_offset = 150
        for transaction in transactions:
            self.add_text((50, y_offset), transaction, font_size=18)
            y_offset += 30

        self.add_text((50, y_offset + 20), f"Balance: {balance}", font_size=20)

# Example usage
if __name__ == "__main__":
    generator = PSDTemplateGenerator()
    account_number = "123456789"
    transactions = [
        "Deposit: $1000.00",
        "Withdrawal: $200.00",
        "Transfer: $300.00",
        "Deposit: $500.00"
    ]
    balance = "$1000.00"

    generator.create_bank_statement(account_number, transactions, balance)
    generator.save_template("output/bank_statement_template.png")
```

This code creates a simple bank statement template with customizable fields for the account number, transaction details, and balance. It uses the `PIL` library to create and manipulate images. Ensure that you have the `Pillow` library installed by running `pip install Pillow` before executing the code.
