"""
Generated Code Metadata:
========================
Original URL: https://arbitum.cz
Prompt: Design a user interface component that allows clients to input their financial situation and receive tailored advice, similar to the personalized services offered by Arbitum Consulting.
Generated: DETERMINISTIC_0c1b3a45b383c745
Batch ID: 20250612_155131
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import tkinter as tk
from tkinter import ttk, messagebox
from typing import Dict, List, Optional

class FinancialAdvisorUI:
    """A user interface component for financial advice based on user input."""

    def __init__(self, root: tk.Tk):
        """Initialize the financial advisor UI.
        
        Args:
            root: The root Tkinter window.
        """
        self.root = root
        self.root.title("Arbitum Financial Advisor")
        self.root.geometry("600x400")
        self.root.resizable(False, False)
        
        # Configure style
        self.style = ttk.Style()
        self.style.configure('TFrame', background='#f0f0f0')
        self.style.configure('TLabel', background='#f0f0f0', font=('Arial', 10))
        self.style.configure('TButton', font=('Arial', 10))
        self.style.configure('Header.TLabel', font=('Arial', 14, 'bold'))
        
        self.create_widgets()
        self.setup_layout()

    def create_widgets(self):
        """Create all UI widgets."""
        # Header
        self.header = ttk.Label(
            self.root,
            text="Personalized Financial Advice",
            style='Header.TLabel'
        )
        
        # Input Frame
        self.input_frame = ttk.Frame(self.root)
        
        # Financial Inputs
        self.income_label = ttk.Label(
            self.input_frame,
            text="Annual Income ($):"
        )
        self.income_entry = ttk.Entry(self.input_frame)
        
        self.expenses_label = ttk.Label(
            self.input_frame,
            text="Monthly Expenses ($):"
        )
        self.expenses_entry = ttk.Entry(self.input_frame)
        
        self.savings_label = ttk.Label(
            self.input_frame,
            text="Current Savings ($):"
        )
        self.savings_entry = ttk.Entry(self.input_frame)
        
        self.debt_label = ttk.Label(
            self.input_frame,
            text="Current Debt ($):"
        )
        self.debt_entry = ttk.Entry(self.input_frame)
        
        self.risk_label = ttk.Label(
            self.input_frame,
            text="Risk Tolerance:"
        )
        self.risk_combobox = ttk.Combobox(
            self.input_frame,
            values=["Low", "Medium", "High"],
            state="readonly"
        )
        self.risk_combobox.set("Medium")
        
        # Buttons
        self.submit_button = ttk.Button(
            self.root,
            text="Get Advice",
            command=self.generate_advice
        )
        
        # Advice Display
        self.advice_frame = ttk.Frame(self.root)
        self.advice_text = tk.Text(
            self.advice_frame,
            wrap=tk.WORD,
            height=10,
            width=60,
            state=tk.DISABLED
        )
        self.scrollbar = ttk.Scrollbar(
            self.advice_frame,
            orient=tk.VERTICAL,
            command=self.advice_text.yview
        )
        self.advice_text.configure(yscrollcommand=self.scrollbar.set)

    def setup_layout(self):
        """Arrange widgets in the UI."""
        self.header.pack(pady=10)
        
        # Input Frame Layout
        self.input_frame.pack(pady=10, padx=20, fill=tk.X)
        
        self.income_label.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
        self.income_entry.grid(row=0, column=1, padx=5, pady=5, sticky=tk.EW)
        
        self.expenses_label.grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)
        self.expenses_entry.grid(row=1, column=1, padx=5, pady=5, sticky=tk.EW)
        
        self.savings_label.grid(row=2, column=0, padx=5, pady=5, sticky=tk.W)
        self.savings_entry.grid(row=2, column=1, padx=5, pady=5, sticky=tk.EW)
        
        self.debt_label.grid(row=3, column=0, padx=5, pady=5, sticky=tk.W)
        self.debt_entry.grid(row=3, column=1, padx=5, pady=5, sticky=tk.EW)
        
        self.risk_label.grid(row=4, column=0, padx=5, pady=5, sticky=tk.W)
        self.risk_combobox.grid(row=4, column=1, padx=5, pady=5, sticky=tk.EW)
        
        # Configure column weights
        self.input_frame.columnconfigure(1, weight=1)
        
        # Submit Button
        self.submit_button.pack(pady=10)
        
        # Advice Frame
        self.advice_frame.pack(pady=10, padx=20, fill=tk.BOTH, expand=True)
        self.advice_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    def validate_inputs(self) -> Optional[Dict[str, float]]:
        """Validate and parse user inputs.
        
        Returns:
            Dictionary of parsed financial data if valid, None otherwise.
        """
        try:
            income = float(self.income_entry.get())
            expenses = float(self.expenses_entry.get())
            savings = float(self.savings_entry.get())
            debt = float(self.debt_entry.get())
            
            if any(value < 0 for value in [income, expenses, savings, debt]):
                raise ValueError("Values cannot be negative")
                
            return {
                "income": income,
                "expenses": expenses,
                "savings": savings,
                "debt": debt,
                "risk": self.risk_combobox.get()
            }
        except ValueError as e:
            messagebox.showerror(
                "Input Error",
                f"Please enter valid numbers for all fields.\nError: {str(e)}"
            )
            return None

    def generate_advice(self):
        """Generate and display financial advice based on user inputs."""
        financial_data = self.validate_inputs()
        if not financial_data:
            return
            
        try:
            advice = self.calculate_advice(financial_data)
            self.display_advice(advice)
        except Exception as e:
            messagebox.showerror(
                "Error",
                f"An error occurred while generating advice.\nError: {str(e)}"
            )

    def calculate_advice(self, data: Dict[str, float]) -> List[str]:
        """Calculate financial advice based on user data.
        
        Args:
            data: Dictionary containing financial information.
            
        Returns:
            List of advice strings.
        """
        advice = []
        
        # Basic calculations
        monthly_income = data["income"] / 12
        savings_ratio = data["savings"] / data["income"] if data["income"] > 0 else 0
        debt_ratio = data["debt"] / data["income"] if data["income"] > 0 else 0
        
        # Savings advice
        if savings_ratio < 0.1:
            advice.append(
                "⚠️ Your savings are low relative to your income. "
                "Aim to save at least 10-20% of your annual income."
            )
        elif savings_ratio < 0.3:
            advice.append(
                "✅ Your savings are at a reasonable level. "
                "Consider increasing to 30% for better financial security."
            )
        else:
            advice.append(
                "👍 Excellent savings ratio! You're well prepared for emergencies."
            )
        
        # Debt advice
        if data["debt"] > 0:
            if debt_ratio > 0.5:
                advice.append(
                    "🚨 High debt burden detected. Focus on paying down debt "
                    "before additional investments."
                )
            elif debt_ratio > 0.2:
                advice.append(
                    "⚠️ Moderate debt level. Consider a balanced approach "
                    "between debt repayment and savings."
                )
            else:
                advice.append(
                    "✅ Manageable debt level. Continue regular payments."
                )
        
        # Expense advice
        if data["expenses"] > monthly_income * 0.5:
            advice.append(
                "⚠️ Your expenses are high relative to income. "
                "Review your budget for potential savings."
            )
        
        # Investment advice based on risk tolerance
        risk = data["risk"]
        if risk == "Low":
            advice.append(
                "Based on your low risk tolerance, consider: "
                "High-yield savings accounts, CDs, and government bonds."
            )
        elif risk == "Medium":
            advice.append(
                "Based on your medium risk tolerance, consider: "
                "Balanced mutual funds, index funds, and blue-chip stocks."
            )
        else:
            advice.append(
                "Based on your high risk
