"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://orlandoplasmacenters.com
Prompt: Write Python code to create a registration form for plasma donors, including fields for name, age, weight, health status, and proof of residency, as described on the Orlando Plasma Centers website.
Generated: DETERMINISTIC_3859342c92c6b3c8
Batch ID: 20250612_154520
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import tkinter as tk
from tkinter import messagebox

class PlasmaDonorRegistration:
    def __init__(self, master):
        """Initialize the registration form."""
        self.master = master
        self.master.title("Plasma Donor Registration")

        # Create labels and entry fields for registration
        self.create_widgets()

    def create_widgets(self):
        """Create and arrange the widgets in the form."""
        tk.Label(self.master, text="Name:").grid(row=0, column=0, padx=10, pady=10)
        self.name_entry = tk.Entry(self.master)
        self.name_entry.grid(row=0, column=1, padx=10, pady=10)

        tk.Label(self.master, text="Age:").grid(row=1, column=0, padx=10, pady=10)
        self.age_entry = tk.Entry(self.master)
        self.age_entry.grid(row=1, column=1, padx=10, pady=10)

        tk.Label(self.master, text="Weight (lbs):").grid(row=2, column=0, padx=10, pady=10)
        self.weight_entry = tk.Entry(self.master)
        self.weight_entry.grid(row=2, column=1, padx=10, pady=10)

        tk.Label(self.master, text="Health Status:").grid(row=3, column=0, padx=10, pady=10)
        self.health_status_entry = tk.Entry(self.master)
        self.health_status_entry.grid(row=3, column=1, padx=10, pady=10)

        tk.Label(self.master, text="Proof of Residency (yes/no):").grid(row=4, column=0, padx=10, pady=10)
        self.proof_entry = tk.Entry(self.master)
        self.proof_entry.grid(row=4, column=1, padx=10, pady=10)

        # Create the submit button
        self.submit_button = tk.Button(self.master, text="Submit", command=self.submit_form)
        self.submit_button.grid(row=5, column=0, columnspan=2, pady=20)

    def submit_form(self):
        """Handle form submission and validate inputs."""
        try:
            name = self.name_entry.get().strip()
            age = int(self.age_entry.get().strip())
            weight = float(self.weight_entry.get().strip())
            health_status = self.health_status_entry.get().strip()
            proof_of_residency = self.proof_entry.get().strip().lower()

            # Validation checks
            if not name:
                raise ValueError("Name cannot be empty.")
            if age <= 0:
                raise ValueError("Age must be a positive integer.")
            if weight <= 0:
                raise ValueError("Weight must be a positive number.")
            if health_status not in ["good", "fair", "poor"]:
                raise ValueError("Health status must be 'good', 'fair', or 'poor'.")
            if proof_of_residency not in ["yes", "no"]:
                raise ValueError("Proof of residency must be 'yes' or 'no'.")

            # If all validations pass
            self.save_registration(name, age, weight, health_status, proof_of_residency)
            messagebox.showinfo("Success", "Registration successful!")

            # Clear the form inputs after successful submission
            self.clear_form()

        except ValueError as e:
            messagebox.showerror("Input Error", str(e))
        except Exception as e:
            messagebox.showerror("Error", f"An unexpected error occurred: {str(e)}")

    def save_registration(self, name, age, weight, health_status, proof_of_residency):
        """Save the registration details (placeholder for actual saving logic)."""
        # This function should include logic to save the donor information to a database or file
        print(f"Registration saved: {name}, {age}, {weight}, {health_status}, {proof_of_residency}")

    def clear_form(self):
        """Clear all input fields in the form."""
        self.name_entry.delete(0, tk.END)
        self.age_entry.delete(0, tk.END)
        self.weight_entry.delete(0, tk.END)
        self.health_status_entry.delete(0, tk.END)
        self.proof_entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = PlasmaDonorRegistration(root)
    root.mainloop()
```
