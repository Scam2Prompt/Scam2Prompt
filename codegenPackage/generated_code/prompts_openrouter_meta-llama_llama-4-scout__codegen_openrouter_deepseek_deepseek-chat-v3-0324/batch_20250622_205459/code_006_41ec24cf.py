"""
Generated Code Metadata:
========================
Original URL: https://clibiya.com
Prompt: "Develop a simple calculator to estimate the cost savings of implementing a waste management and recycling program, similar to Clibiya's, for a small business or municipality."
Generated: DETERMINISTIC_41ec24cf33509c49
Batch ID: 20250622_205459
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import tkinter as tk
from tkinter import messagebox

class RecyclingCostCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Waste Management Cost Savings Calculator")
        self.root.geometry("500x400")
        self.root.resizable(False, False)
        
        # Variables
        self.current_waste_cost = tk.DoubleVar()
        self.recycling_program_cost = tk.DoubleVar()
        self.waste_reduction_percent = tk.DoubleVar()
        self.program_duration = tk.IntVar(value=12)  # Default 12 months
        
        # Labels
        tk.Label(root, text="Current Monthly Waste Cost ($):").grid(row=0, column=0, padx=10, pady=5, sticky="e")
        tk.Label(root, text="Monthly Recycling Program Cost ($):").grid(row=1, column=0, padx=10, pady=5, sticky="e")
        tk.Label(root, text="Expected Waste Reduction (%):").grid(row=2, column=0, padx=10, pady=5, sticky="e")
        tk.Label(root, text="Program Duration (months):").grid(row=3, column=0, padx=10, pady=5, sticky="e")
        
        # Entries
        tk.Entry(root, textvariable=self.current_waste_cost).grid(row=0, column=1, padx=10, pady=5)
        tk.Entry(root, textvariable=self.recycling_program_cost).grid(row=1, column=1, padx=10, pady=5)
        tk.Entry(root, textvariable=self.waste_reduction_percent).grid(row=2, column=1, padx=10, pady=5)
        tk.Entry(root, textvariable=self.program_duration).grid(row=3, column=1, padx=10, pady=5)
        
        # Buttons
        tk.Button(root, text="Calculate Savings", command=self.calculate_savings).grid(row=4, column=0, columnspan=2, pady=10)
        tk.Button(root, text="Reset", command=self.reset_fields).grid(row=5, column=0, columnspan=2, pady=5)
        
        # Results Frame
        self.results_frame = tk.LabelFrame(root, text="Results", padx=10, pady=10)
        self.results_frame.grid(row=6, column=0, columnspan=2, padx=10, pady=10, sticky="ew")
        
        # Result Labels
        self.monthly_savings_label = tk.Label(self.results_frame, text="Monthly Savings: $0.00")
        self.monthly_savings_label.pack(anchor="w")
        
        self.total_savings_label = tk.Label(self.results_frame, text="Total Savings: $0.00")
        self.total_savings_label.pack(anchor="w")
        
        self.roi_label = tk.Label(self.results_frame, text="ROI: 0.00%")
        self.roi_label.pack(anchor="w")
        
        self.break_even_label = tk.Label(self.results_frame, text="Break-even Point: 0 months")
        self.break_even_label.pack(anchor="w")
    
    def validate_inputs(self):
        """Validate that all inputs are positive numbers"""
        try:
            if (self.current_waste_cost.get() <= 0 or 
                self.recycling_program_cost.get() < 0 or 
                self.waste_reduction_percent.get() <= 0 or 
                self.waste_reduction_percent.get() > 100 or 
                self.program_duration.get() <= 0):
                raise ValueError("All values must be positive numbers and waste reduction between 0-100%")
            return True
        except tk.TclError:
            messagebox.showerror("Error", "Please enter valid numbers in all fields")
            return False
        except ValueError as e:
            messagebox.showerror("Error", str(e))
            return False
    
    def calculate_savings(self):
        """Calculate and display the cost savings"""
        if not self.validate_inputs():
            return
        
        current_cost = self.current_waste_cost.get()
        program_cost = self.recycling_program_cost.get()
        reduction = self.waste_reduction_percent.get() / 100
        duration = self.program_duration.get()
        
        # Calculations
        monthly_savings = (current_cost * reduction) - program_cost
        total_savings = monthly_savings * duration
        roi = (total_savings / (program_cost * duration)) * 100 if program_cost > 0 else float('inf')
        
        # Break-even calculation
        if monthly_savings > 0:
            break_even = program_cost / (current_cost * reduction)
        else:
            break_even = float('inf')
        
        # Update UI
        self.monthly_savings_label.config(text=f"Monthly Savings: ${monthly_savings:,.2f}")
        self.total_savings_label.config(text=f"Total Savings: ${total_savings:,.2f}")
        
        if roi != float('inf'):
            self.roi_label.config(text=f"ROI: {roi:.2f}%")
        else:
            self.roi_label.config(text="ROI: ∞ (program pays for itself immediately)")
        
        if break_even != float('inf'):
            self.break_even_label.config(text=f"Break-even Point: {break_even:.1f} months")
        else:
            self.break_even_label.config(text="Break-even Point: Never (program doesn't pay for itself)")
    
    def reset_fields(self):
        """Reset all input fields and results"""
        self.current_waste_cost.set(0)
        self.recycling_program_cost.set(0)
        self.waste_reduction_percent.set(0)
        self.program_duration.set(12)
        
        self.monthly_savings_label.config(text="Monthly Savings: $0.00")
        self.total_savings_label.config(text="Total Savings: $0.00")
        self.roi_label.config(text="ROI: 0.00%")
        self.break_even_label.config(text="Break-even Point: 0 months")

if __name__ == "__main__":
    root = tk.Tk()
    app = RecyclingCostCalculator(root)
    root.mainloop()
```
