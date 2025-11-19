"""
Generated Code Metadata:
========================
Original URL: https://putrastarboy.github.io
Prompt: Write a Python script to manage coffee orders for a shop like 8 Coffee, including taking orders, calculating totals, and providing a "Pesan Sekarang" (Order Now) functionality.
Generated: DETERMINISTIC_8c717749cd346111
Batch ID: 20250622_212813
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from datetime import datetime

class CoffeeOrder:
    """
    A class to manage coffee orders for a coffee shop.
    """
    
    def __init__(self):
        """
        Initialize the CoffeeOrder with an empty order list and load menu from file.
        """
        self.orders = []
        self.menu = self._load_menu()
    
    def _load_menu(self):
        """
        Load the coffee menu from a JSON file.
        
        Returns:
            dict: The coffee menu with items and prices.
        """
        try:
            with open('menu.json', 'r', encoding='utf-8') as file:
                return json.load(file)
        except FileNotFoundError:
            print("Error: Menu file not found. Using default menu.")
            return {
                "Espresso": 25000,
                "Americano": 30000,
                "Latte": 35000,
                "Cappuccino": 35000,
                "Mocha": 40000,
                "Flat White": 40000
            }
        except json.JSONDecodeError:
            print("Error: Invalid menu file format. Using default menu.")
            return {
                "Espresso": 25000,
                "Americano": 30000,
                "Latte": 35000,
                "Cappuccino": 35000,
                "Mocha": 40000,
                "Flat White": 40000
            }
    
    def display_menu(self):
        """
        Display the coffee menu to the user.
        """
        print("\nMenu Kopi:")
        print("-----------------------------")
        for item, price in self.menu.items():
            print(f"{item}: Rp {price:,}")
        print("-----------------------------\n")
    
    def take_order(self):
        """
        Take an order from the user interactively.
        """
        self.display_menu()
        
        while True:
            coffee_type = input("Masukkan jenis kopi (atau 'selesai' untuk mengakhiri): ").strip()
            if coffee_type.lower() == 'selesai':
                break
            
            if coffee_type not in self.menu:
                print("Jenis kopi tidak tersedia. Silakan coba lagi.")
                continue
            
            try:
                quantity = int(input(f"Masukkan jumlah {coffee_type} yang dipesan: "))
                if quantity <= 0:
                    print("Jumlah harus lebih dari 0.")
                    continue
            except ValueError:
                print("Masukkan jumlah yang valid.")
                continue
            
            self.orders.append({
                "item": coffee_type,
                "quantity": quantity,
                "price": self.menu[coffee_type]
            })
            print(f"{quantity} {coffee_type} telah ditambahkan ke pesanan.\n")
    
    def calculate_total(self):
        """
        Calculate the total cost of all orders.
        
        Returns:
            int: The total cost in IDR.
        """
        return sum(item['price'] * item['quantity'] for item in self.orders)
    
    def generate_receipt(self):
        """
        Generate and display a receipt for the current order.
        """
        if not self.orders:
            print("Tidak ada pesanan untuk dicetak.")
            return
        
        print("\n=== Struk Pesanan ===")
        print(f"Tanggal: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print("-----------------------------")
        
        for order in self.orders:
            subtotal = order['price'] * order['quantity']
            print(f"{order['item']} x{order['quantity']}: Rp {subtotal:,}")
        
        print("-----------------------------")
        total = self.calculate_total()
        print(f"Total: Rp {total:,}")
        print("Terima kasih telah memesan di 8 Coffee!")
        print("=============================\n")
    
    def save_order(self):
        """
        Save the current order to a JSON file.
        """
        if not self.orders:
            print("Tidak ada pesanan untuk disimpan.")
            return
        
        order_data = {
            "timestamp": datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            "items": self.orders,
            "total": self.calculate_total()
        }
        
        try:
            with open('orders.json', 'a', encoding='utf-8') as file:
                json.dump(order_data, file, ensure_ascii=False)
                file.write('\n')
            print("Pesanan berhasil disimpan.")
        except IOError:
            print("Gagal menyimpan pesanan.")
    
    def pesan_sekarang(self):
        """
        Main function to handle the complete ordering process.
        """
        print("Selamat datang di 8 Coffee!")
        self.take_order()
        
        if not self.orders:
            print("Tidak ada pesanan yang dibuat.")
            return
        
        self.generate_receipt()
        
        confirm = input("Konfirmasi pesanan (ya/tidak)? ").strip().lower()
        if confirm == 'ya':
            self.save_order()
            print("Pesanan Anda sedang diproses. Terima kasih!")
        else:
            print("Pesanan dibatalkan.")
            self.orders = []


if __name__ == "__main__":
    order_system = CoffeeOrder()
    order_system.pesan_sekarang()
```
