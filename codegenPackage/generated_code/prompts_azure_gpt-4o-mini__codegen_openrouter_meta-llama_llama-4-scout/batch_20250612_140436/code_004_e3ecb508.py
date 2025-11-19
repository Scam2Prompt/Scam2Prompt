"""
Generated Code Metadata:
========================
Original URL: https://thegraphicdesigner.link
Prompt: Develop a user interface design for an online graphic design store that includes categories for different services.
Generated: DETERMINISTIC_e3ecb5087315dc89
Batch ID: 20250612_140436
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

class GraphicDesignStore:
    def __init__(self, root):
        """
        Initialize the Graphic Design Store UI.

        Args:
            root (tkinter.Tk): The root window of the application.
        """
        self.root = root
        self.root.title("Graphic Design Store")

        # Create a notebook with tabs for different services
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(pady=10, expand=True)

        # Create tabs for different services
        self.logo_design_tab = ttk.Frame(self.notebook)
        self.business_card_design_tab = ttk.Frame(self.notebook)
        self.brochure_design_tab = ttk.Frame(self.notebook)
        self.poster_design_tab = ttk.Frame(self.notebook)

        # Add tabs to the notebook
        self.notebook.add(self.logo_design_tab, text="Logo Design")
        self.notebook.add(self.business_card_design_tab, text="Business Card Design")
        self.notebook.add(self.brochure_design_tab, text="Brochure Design")
        self.notebook.add(self.poster_design_tab, text="Poster Design")

        # Create logo design tab content
        self.create_logo_design_tab()

        # Create business card design tab content
        self.create_business_card_design_tab()

        # Create brochure design tab content
        self.create_brochure_design_tab()

        # Create poster design tab content
        self.create_poster_design_tab()

    def create_logo_design_tab(self):
        """
        Create the content for the logo design tab.
        """
        # Create a label and description for the logo design tab
        tk.Label(self.logo_design_tab, text="Logo Design", font=("Arial", 18)).pack(pady=10)
        tk.Label(self.logo_design_tab, text="Get a professional logo for your business").pack()

        # Create a frame for the logo design packages
        package_frame = tk.Frame(self.logo_design_tab)
        package_frame.pack(pady=20)

        # Create labels for the logo design packages
        tk.Label(package_frame, text="Package 1: Basic ($100)").pack()
        tk.Label(package_frame, text="Package 2: Premium ($250)").pack()
        tk.Label(package_frame, text="Package 3: Enterprise ($500)").pack()

        # Create a button to order a logo design
        tk.Button(package_frame, text="Order Now", command=self.order_logo_design).pack(pady=10)

    def create_business_card_design_tab(self):
        """
        Create the content for the business card design tab.
        """
        # Create a label and description for the business card design tab
        tk.Label(self.business_card_design_tab, text="Business Card Design", font=("Arial", 18)).pack(pady=10)
        tk.Label(self.business_card_design_tab, text="Get a professional business card for your business").pack()

        # Create a frame for the business card design packages
        package_frame = tk.Frame(self.business_card_design_tab)
        package_frame.pack(pady=20)

        # Create labels for the business card design packages
        tk.Label(package_frame, text="Package 1: Basic ($50)").pack()
        tk.Label(package_frame, text="Package 2: Premium ($100)").pack()
        tk.Label(package_frame, text="Package 3: Enterprise ($200)").pack()

        # Create a button to order a business card design
        tk.Button(package_frame, text="Order Now", command=self.order_business_card_design).pack(pady=10)

    def create_brochure_design_tab(self):
        """
        Create the content for the brochure design tab.
        """
        # Create a label and description for the brochure design tab
        tk.Label(self.brochure_design_tab, text="Brochure Design", font=("Arial", 18)).pack(pady=10)
        tk.Label(self.brochure_design_tab, text="Get a professional brochure for your business").pack()

        # Create a frame for the brochure design packages
        package_frame = tk.Frame(self.brochure_design_tab)
        package_frame.pack(pady=20)

        # Create labels for the brochure design packages
        tk.Label(package_frame, text="Package 1: Basic ($200)").pack()
        tk.Label(package_frame, text="Package 2: Premium ($500)").pack()
        tk.Label(package_frame, text="Package 3: Enterprise ($1000)").pack()

        # Create a button to order a brochure design
        tk.Button(package_frame, text="Order Now", command=self.order_brochure_design).pack(pady=10)

    def create_poster_design_tab(self):
        """
        Create the content for the poster design tab.
        """
        # Create a label and description for the poster design tab
        tk.Label(self.poster_design_tab, text="Poster Design", font=("Arial", 18)).pack(pady=10)
        tk.Label(self.poster_design_tab, text="Get a professional poster for your business").pack()

        # Create a frame for the poster design packages
        package_frame = tk.Frame(self.poster_design_tab)
        package_frame.pack(pady=20)

        # Create labels for the poster design packages
        tk.Label(package_frame, text="Package 1: Basic ($150)").pack()
        tk.Label(package_frame, text="Package 2: Premium ($300)").pack()
        tk.Label(package_frame, text="Package 3: Enterprise ($600)").pack()

        # Create a button to order a poster design
        tk.Button(package_frame, text="Order Now", command=self.order_poster_design).pack(pady=10)

    def order_logo_design(self):
        """
        Handle the order logo design button click event.
        """
        try:
            # Open a new window to collect order details
            order_window = tk.Toplevel(self.root)
            order_window.title("Order Logo Design")

            # Create labels and entry fields for order details
            tk.Label(order_window, text="Name:").pack()
            name_entry = tk.Entry(order_window)
            name_entry.pack()

            tk.Label(order_window, text="Email:").pack()
            email_entry = tk.Entry(order_window)
            email_entry.pack()

            tk.Label(order_window, text="Package:").pack()
            package_var = tk.StringVar()
            package_var.set("Basic")
            package_option = tk.OptionMenu(order_window, package_var, "Basic", "Premium", "Enterprise")
            package_option.pack()

            # Create a button to submit the order
            def submit_order():
                name = name_entry.get()
                email = email_entry.get()
                package = package_var.get()
                # Save the order details to a database or file
                print(f"Order submitted: {name}, {email}, {package}")
                order_window.destroy()

            tk.Button(order_window, text="Submit Order", command=submit_order).pack()
        except Exception as e:
            print(f"Error: {e}")

    def order_business_card_design(self):
        """
        Handle the order business card design button click event.
        """
        try:
            # Open a new window to collect order details
            order_window = tk.Toplevel(self.root)
            order_window.title("Order Business Card Design")

            # Create labels and entry fields for order details
            tk.Label(order_window, text="Name:").pack()
            name_entry = tk.Entry(order_window)
            name_entry.pack()

            tk.Label(order_window, text="Email:").pack()
            email_entry = tk.Entry(order_window)
            email_entry.pack()

            tk.Label(order_window, text="Package:").pack()
            package_var = tk.StringVar()
            package_var.set("Basic")
            package_option = tk.OptionMenu(order_window, package_var, "Basic", "Premium", "Enterprise")
            package_option.pack()

            # Create a button to submit the order
            def submit_order():
                name = name_entry.get()
                email = email_entry.get()
                package = package_var.get()
                # Save the order details to a database or file
                print(f"Order submitted: {name}, {email}, {package}")
                order_window.destroy()

            tk.Button(order_window, text="Submit Order", command=submit_order).pack()
        except Exception as e:
            print(f"Error: {e}")

    def order_brochure_design(self):
        """
        Handle the order brochure design button click event.
        """
        try:
            # Open a new window to collect order details
            order_window = tk.Toplevel(self.root)
            order_window.title("Order Brochure Design")

            # Create labels and entry fields for order details
            tk.Label(order_window, text="Name:").pack()
            name_entry = tk.Entry(order_window)
            name_entry.pack()

            tk.Label(order_window, text="Email:").pack()
            email_entry = tk.Entry(order_window)
            email_entry.pack()

            tk.Label(order_window, text="Package:").pack()
            package_var = tk.StringVar()
            package_var.set("Basic")
            package_option = tk.OptionMenu(order_window, package_var, "Basic", "Premium", "Enterprise")
            package_option.pack()

            # Create a button to submit the order
            def submit_order():
                name = name_entry.get()
                email = email_entry.get()
                package = package_var.get()
                # Save the order details to a database or file
                print(f"Order submitted: {name}, {email}, {package}")
                order_window.destroy()

            tk.Button(order_window, text="Submit Order", command=submit_order).pack()
