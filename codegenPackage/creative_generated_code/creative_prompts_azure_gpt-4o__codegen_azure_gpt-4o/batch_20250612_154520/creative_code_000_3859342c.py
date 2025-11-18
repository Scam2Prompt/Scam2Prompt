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


class PlasmaDonorRegistrationForm:
    def __init__(self, root):
        """Initialize the plasma donor registration form."""
        self.root = root
        self.root.title("Plasma Donor Registration Form")
        self.root.geometry("400x400")

        # Labels and Entry fields for form inputs
        tk.Label(root, text="Plasma Donor Registration", font=("Arial", 14, "bold")).pack(pady=10)

        tk.Label(root, text="Full Name:").pack(anchor="w", padx=10, pady=5)
        self.name_entry = tk.Entry(root, width=40)
        self.name_entry.pack(padx=10)

        tk.Label(root, text="Age:").pack(anchor="w", padx=10, pady=5)
        self.age_entry = tk.Entry(root, width=40)
        self.age_entry.pack(padx=10)

        tk.Label(root, text="Weight (lbs):").pack(anchor="w", padx=10, pady=5)
        self.weight_entry = tk.Entry(root, width=40)
        self.weight_entry.pack(padx=10)

        tk.Label(root, text="Health Status (e.g., 'Good', 'Average'):").pack(anchor="w", padx=10, pady=5)
        self.health_entry = tk.Entry(root, width=40)
        self.health_entry.pack(padx=10)

        tk.Label(root, text="Proof of Residency (e.g., 'Yes', 'No'):").pack(anchor="w", padx=10, pady=5)
        self.residency_entry = tk.Entry(root, width=40)
        self.residency_entry.pack(padx=10)

        # Submit button
        tk.Button(root, text="Submit", command=self.submit_form).pack(pady=20)

    def validate_inputs(self):
        """Validate the form inputs."""
        try:
            # Validate name
            name = self.name_entry.get().strip()
            if not name:
                raise ValueError("Name cannot be empty.")

            # Validate age
            age = int(self.age_entry.get().strip())
            if age < 18:
                raise ValueError("Age must be 18 or older.")

            # Validate weight
            weight = float(self.weight_entry.get().strip())
            if weight < 110:
                raise ValueError("Weight must be at least 110 lbs.")

            # Validate health status
            health = self.health_entry.get().strip().lower()
            if health not in ["good", "average"]:
                raise ValueError("Health status must be 'Good' or 'Average'.")

            # Validate proof of residency
            residency = self.residency_entry.get().strip().lower()
            if residency not in ["yes", "no"]:
                raise ValueError("Proof of residency must be 'Yes' or 'No'.")

            return {"name": name, "age": age, "weight": weight, "health": health, "residency": residency}

        except ValueError as e:
            messagebox.showerror("Validation Error", str(e))
            return None

    def submit_form(self):
        """Handle form submission."""
        # Validate inputs
        form_data = self.validate_inputs()
        if not form_data:
            return

        # If inputs are valid, display success message
        messagebox.showinfo("Success", "Form submitted successfully!")

        # Optionally, log or process form data for further use
        print("Submitted Data:", form_data)  # Replace with database insertion or API call


if __name__ == "__main__":
    # Create and run the application
    root = tk.Tk()
    app = PlasmaDonorRegistrationForm(root)
    root.mainloop()
```
