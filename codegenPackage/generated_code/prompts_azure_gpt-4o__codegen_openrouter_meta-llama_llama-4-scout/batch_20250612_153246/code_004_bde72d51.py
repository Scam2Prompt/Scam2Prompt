"""
Generated Code Metadata:
========================
Original URL: https://www.oasishottubsep.com
Prompt: Suggest a library or framework to develop an interactive "Build & Price" tool for hot tubs, including options for Jacuzzi® Swim Spas and Hydropool Swim Spas, as seen on the Oasis Hot Tubs site.
Generated: DETERMINISTIC_bde72d5109b3b66e
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import tkinter as tk
from tkinter import ttk

class HotTub:
    def __init__(self, brand, model, size, price):
        """
        Initialize a HotTub object.

        Args:
            brand (str): The brand of the hot tub.
            model (str): The model of the hot tub.
            size (str): The size of the hot tub.
            price (float): The price of the hot tub.
        """
        self.brand = brand
        self.model = model
        self.size = size
        self.price = price

class BuildAndPriceTool:
    def __init__(self, root):
        """
        Initialize the Build and Price tool.

        Args:
            root (tkinter.Tk): The root window of the application.
        """
        self.root = root
        self.root.title("Build & Price Tool")
        self.hot_tub = None

        # Create tabs
        self.tab_control = ttk.Notebook(self.root)
        self.tab_control.pack(expand=1, fill="both")

        self.jacuzzi_tab = ttk.Frame(self.tab_control)
        self.hydropool_tab = ttk.Frame(self.tab_control)

        self.tab_control.add(self.jacuzzi_tab, text="Jacuzzi Swim Spas")
        self.tab_control.add(self.hydropool_tab, text="Hydropool Swim Spas")

        # Jacuzzi Swim Spas tab
        self.jacuzzi_brand = tk.StringVar()
        self.jacuzzi_brand.set("Jacuzzi")  # default value

        self.jacuzzi_model_label = tk.Label(self.jacuzzi_tab, text="Model:")
        self.jacuzzi_model_label.pack()
        self.jacuzzi_model = tk.StringVar()
        self.jacuzzi_model.set("J-15")  # default value
        self.jacuzzi_model_option = tk.OptionMenu(self.jacuzzi_tab, self.jacuzzi_model, "J-15", "J-20", "J-25")
        self.jacuzzi_model_option.pack()

        self.jacuzzi_size_label = tk.Label(self.jacuzzi_tab, text="Size:")
        self.jacuzzi_size_label.pack()
        self.jacuzzi_size = tk.StringVar()
        self.jacuzzi_size.set("15' x 6'")  # default value
        self.jacuzzi_size_option = tk.OptionMenu(self.jacuzzi_tab, self.jacuzzi_size, "15' x 6'", "16' x 7'", "17' x 8'")
        self.jacuzzi_size_option.pack()

        self.jacuzzi_price_label = tk.Label(self.jacuzzi_tab, text="Price:")
        self.jacuzzi_price_label.pack()
        self.jacuzzi_price = tk.StringVar()
        self.jacuzzi_price.set("$10,000")  # default value

        self.jacuzzi_calculate_button = tk.Button(self.jacuzzi_tab, text="Calculate Price", command=self.calculate_jacuzzi_price)
        self.jacuzzi_calculate_button.pack()

        # Hydropool Swim Spas tab
        self.hydropool_brand = tk.StringVar()
        self.hydropool_brand.set("Hydropool")  # default value

        self.hydropool_model_label = tk.Label(self.hydropool_tab, text="Model:")
        self.hydropool_model_label.pack()
        self.hydropool_model = tk.StringVar()
        self.hydropool_model.set("HLS-15")  # default value
        self.hydropool_model_option = tk.OptionMenu(self.hydropool_tab, self.hydropool_model, "HLS-15", "HLS-20", "HLS-25")
        self.hydropool_model_option.pack()

        self.hydropool_size_label = tk.Label(self.hydropool_tab, text="Size:")
        self.hydropool_size_label.pack()
        self.hydropool_size = tk.StringVar()
        self.hydropool_size.set("15' x 6'")  # default value
        self.hydropool_size_option = tk.OptionMenu(self.hydropool_tab, self.hydropool_size, "15' x 6'", "16' x 7'", "17' x 8'")
        self.hydropool_size_option.pack()

        self.hydropool_price_label = tk.Label(self.hydropool_tab, text="Price:")
        self.hydropool_price_label.pack()
        self.hydropool_price = tk.StringVar()
        self.hydropool_price.set("$12,000")  # default value

        self.hydropool_calculate_button = tk.Button(self.hydropool_tab, text="Calculate Price", command=self.calculate_hydropool_price)
        self.hydropool_calculate_button.pack()

        # Summary section
        self.summary_label = tk.Label(self.root, text="Summary:")
        self.summary_label.pack()
        self.summary_text = tk.Text(self.root, height=10, width=40)
        self.summary_text.pack()

    def calculate_jacuzzi_price(self):
        try:
            model = self.jacuzzi_model.get()
            size = self.jacuzzi_size.get()
            price = self.get_jacuzzi_price(model, size)
            self.jacuzzi_price.set(f"${price:,.2f}")
            self.update_summary("Jacuzzi", model, size, price)
        except Exception as e:
            print(f"Error: {e}")

    def calculate_hydropool_price(self):
        try:
            model = self.hydropool_model.get()
            size = self.hydropool_size.get()
            price = self.get_hydropool_price(model, size)
            self.hydropool_price.set(f"${price:,.2f}")
            self.update_summary("Hydropool", model, size, price)
        except Exception as e:
            print(f"Error: {e}")

    def get_jacuzzi_price(self, model, size):
        # Sample pricing data for Jacuzzi Swim Spas
        pricing_data = {
            "J-15": {"15' x 6'": 10000, "16' x 7'": 12000, "17' x 8'": 15000},
            "J-20": {"15' x 6'": 12000, "16' x 7'": 15000, "17' x 8'": 18000},
            "J-25": {"15' x 6'": 15000, "16' x 7'": 18000, "17' x 8'": 20000},
        }
        return pricing_data.get(model, {}).get(size, 0)

    def get_hydropool_price(self, model, size):
        # Sample pricing data for Hydropool Swim Spas
        pricing_data = {
            "HLS-15": {"15' x 6'": 12000, "16' x 7'": 15000, "17' x 8'": 18000},
            "HLS-20": {"15' x 6'": 15000, "16' x 7'": 18000, "17' x 8'": 20000},
            "HLS-25": {"15' x 6'": 18000, "16' x 7'": 20000, "17' x 8'": 22000},
        }
        return pricing_data.get(model, {}).get(size, 0)

    def update_summary(self, brand, model, size, price):
        summary = f"Brand: {brand}\nModel: {model}\nSize: {size}\nPrice: ${price:,.2f}"
        self.summary_text.delete(1.0, tk.END)
        self.summary_text.insert(tk.END, summary)

if __name__ == "__main__":
    root = tk.Tk()
    app = BuildAndPriceTool(root)
    root.mainloop()
```
