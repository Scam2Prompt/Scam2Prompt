"""
Generated Code Metadata:
========================
Original URL: https://novax-profit-system.com
Prompt: Design a user interface for a Novax Profit System demo account that allows traders to refine and validate their trading parameters before engaging in live trading.
Generated: DETERMINISTIC_29b9686f72a69d8e
Batch ID: 20250622_211830
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
import json
import os

class NovaxProfitSystemUI:
    """User interface for Novax Profit System demo account."""

    def __init__(self, root):
        """Initialize the UI components."""
        self.root = root
        self.root.title("Novax Profit System - Demo Account")
        self.root.geometry("800x600")
        self.root.resizable(False, False)

        # Configuration file path
        self.config_file = "trading_params.json"

        # Initialize trading parameters
        self.params = {
            "symbol": "BTC/USDT",
            "timeframe": "1h",
            "risk_per_trade": 1.0,
            "take_profit": 2.0,
            "stop_loss": 1.0,
            "strategy": "Mean Reversion"
        }

        # Load saved parameters if config file exists
        self.load_config()

        # Create UI components
        self.create_widgets()

    def create_widgets(self):
        """Create and arrange UI widgets."""
        # Main frame
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.pack(fill=tk.BOTH, expand=True)

        # Trading Parameters Section
        params_frame = ttk.LabelFrame(main_frame, text="Trading Parameters", padding="10")
        params_frame.pack(fill=tk.X, pady=5)

        # Symbol
        ttk.Label(params_frame, text="Trading Pair:").grid(row=0, column=0, sticky=tk.W, pady=2)
        self.symbol_entry = ttk.Entry(params_frame)
        self.symbol_entry.grid(row=0, column=1, sticky=tk.EW, padx=5, pady=2)
        self.symbol_entry.insert(0, self.params["symbol"])

        # Timeframe
        ttk.Label(params_frame, text="Timeframe:").grid(row=1, column=0, sticky=tk.W, pady=2)
        self.timeframe_combo = ttk.Combobox(params_frame, values=["1m", "5m", "15m", "30m", "1h", "4h", "1d"])
        self.timeframe_combo.grid(row=1, column=1, sticky=tk.EW, padx=5, pady=2)
        self.timeframe_combo.set(self.params["timeframe"])

        # Risk per trade
        ttk.Label(params_frame, text="Risk per Trade (%):").grid(row=2, column=0, sticky=tk.W, pady=2)
        self.risk_entry = ttk.Entry(params_frame)
        self.risk_entry.grid(row=2, column=1, sticky=tk.EW, padx=5, pady=2)
        self.risk_entry.insert(0, str(self.params["risk_per_trade"]))

        # Take Profit
        ttk.Label(params_frame, text="Take Profit (%):").grid(row=3, column=0, sticky=tk.W, pady=2)
        self.tp_entry = ttk.Entry(params_frame)
        self.tp_entry.grid(row=3, column=1, sticky=tk.EW, padx=5, pady=2)
        self.tp_entry.insert(0, str(self.params["take_profit"]))

        # Stop Loss
        ttk.Label(params_frame, text="Stop Loss (%):").grid(row=4, column=0, sticky=tk.W, pady=2)
        self.sl_entry = ttk.Entry(params_frame)
        self.sl_entry.grid(row=4, column=1, sticky=tk.EW, padx=5, pady=2)
        self.sl_entry.insert(0, str(self.params["stop_loss"]))

        # Strategy
        ttk.Label(params_frame, text="Strategy:").grid(row=5, column=0, sticky=tk.W, pady=2)
        self.strategy_combo = ttk.Combobox(params_frame, values=["Mean Reversion", "Trend Following", "Breakout"])
        self.strategy_combo.grid(row=5, column=1, sticky=tk.EW, padx=5, pady=2)
        self.strategy_combo.set(self.params["strategy"])

        # Button Frame
        button_frame = ttk.Frame(main_frame)
        button_frame.pack(fill=tk.X, pady=10)

        # Validate Button
        validate_btn = ttk.Button(button_frame, text="Validate Parameters", command=self.validate_params)
        validate_btn.pack(side=tk.LEFT, padx=5)

        # Save Button
        save_btn = ttk.Button(button_frame, text="Save Parameters", command=self.save_params)
        save_btn.pack(side=tk.LEFT, padx=5)

        # Demo Trade Button
        demo_btn = ttk.Button(button_frame, text="Run Demo Trade", command=self.run_demo_trade)
        demo_btn.pack(side=tk.RIGHT, padx=5)

        # Log Area
        log_frame = ttk.LabelFrame(main_frame, text="Log", padding="10")
        log_frame.pack(fill=tk.BOTH, expand=True)

        self.log_text = tk.Text(log_frame, height=10, state=tk.DISABLED)
        self.log_text.pack(fill=tk.BOTH, expand=True)

        # Add scrollbar
        scrollbar = ttk.Scrollbar(self.log_text)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.log_text.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.log_text.yview)

    def log_message(self, message):
        """Add a message to the log area."""
        self.log_text.config(state=tk.NORMAL)
        self.log_text.insert(tk.END, message + "\n")
        self.log_text.config(state=tk.DISABLED)
        self.log_text.see(tk.END)

    def validate_params(self):
        """Validate the trading parameters."""
        try:
            # Get values from UI
            symbol = self.symbol_entry.get().strip()
            timeframe = self.timeframe_combo.get().strip()
            risk = float(self.risk_entry.get())
            take_profit = float(self.tp_entry.get())
            stop_loss = float(self.sl_entry.get())
            strategy = self.strategy_combo.get().strip()

            # Validate values
            if not symbol:
                raise ValueError("Trading pair cannot be empty")
            if not timeframe:
                raise ValueError("Timeframe cannot be empty")
            if risk <= 0 or risk > 100:
                raise ValueError("Risk per trade must be between 0 and 100")
            if take_profit <= 0:
                raise ValueError("Take profit must be positive")
            if stop_loss <= 0:
                raise ValueError("Stop loss must be positive")
            if not strategy:
                raise ValueError("Strategy cannot be empty")

            # Update params dictionary
            self.params = {
                "symbol": symbol,
                "timeframe": timeframe,
                "risk_per_trade": risk,
                "take_profit": take_profit,
                "stop_loss": stop_loss,
                "strategy": strategy
            }

            self.log_message("Parameters validated successfully!")
            return True

        except ValueError as e:
            messagebox.showerror("Validation Error", str(e))
            self.log_message(f"Validation failed: {str(e)}")
            return False

    def save_params(self):
        """Save the trading parameters to a config file."""
        if not self.validate_params():
            return

        try:
            with open(self.config_file, "w") as f:
                json.dump(self.params, f, indent=4)
            self.log_message("Parameters saved successfully!")
        except Exception as e:
            messagebox.showerror("Save Error", f"Failed to save parameters: {str(e)}")
            self.log_message(f"Save failed: {str(e)}")

    def load_config(self):
        """Load trading parameters from config file if it exists."""
        if os.path.exists(self.config_file):
            try:
                with open(self.config_file, "r") as f:
                    self.params = json.load(f)
            except Exception as e:
                messagebox.showerror("Load Error", f"Failed to load parameters: {str(e)}")
                self.log_message(f"Load failed: {str(e)}")

    def run_demo_trade(self):
        """Simulate a demo trade with the current parameters."""
        if not self.validate_params():
            return

        try:
            # Simulate trade execution
            self.log_message("\n=== Starting Demo Trade ===")
            self.log_message(f"Symbol: {self.params['symbol']}")
            self.log_message(f"Timeframe: {self.params['timeframe']}")
            self.log_message(f"Strategy: {self.params['strategy']}")
            self.log_message(f"Risk: {self.params['risk_per_trade']}%")
            self.log_message(f"Take Profit: {self.params['take_profit']}%")
            self.log_message(f"Stop Loss: {self.params['stop_loss']}%")
