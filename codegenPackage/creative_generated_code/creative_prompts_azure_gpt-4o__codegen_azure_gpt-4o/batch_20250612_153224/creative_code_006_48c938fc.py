"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://instrumentacionum.com
Prompt: Develop a dashboard in Python to visualize data from flow meters, temperature sensors, and pressure transmitters, using Instrumentación UM's instrumentation products as a model.
Generated: DETERMINISTIC_48c938fc8164ee24
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import ttk, messagebox
import random

# Define mock data generation for Instrumentación UM's products
def generate_mock_data():
    """
    Generate mock data for flow meters, temperature sensors, and pressure transmitters.
    Returns a DataFrame with the generated data.
    """
    data = {
        "Timestamp": pd.date_range(start="2023-10-01", periods=100, freq="T"),
        "Flow_Meter": [random.uniform(1, 100) for _ in range(100)],  # Simulated flow rate (L/min)
        "Temperature_Sensor": [random.uniform(10, 50) for _ in range(100)],  # Simulated temperature (°C)
        "Pressure_Transmitter": [random.uniform(0.5, 5) for _ in range(100)]  # Simulated pressure (Bar)
    }
    return pd.DataFrame(data)

# Generate data
mock_data = generate_mock_data()

# Define the dashboard application
class DashboardApp:
    def __init__(self, root):
        """
        Initialize the dashboard application.
        :param root: The Tkinter root window.
        """
        self.root = root
        self.root.title("Instrumentation Dashboard")
        self.root.geometry("800x600")

        # Add a notebook for tabs
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(expand=True, fill="both")

        # Tab for Flow Meter Data Visualization
        self.flow_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.flow_tab, text="Flow Meter")

        # Tab for Temperature Sensor Data Visualization
        self.temperature_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.temperature_tab, text="Temperature Sensor")

        # Tab for Pressure Transmitter Data Visualization
        self.pressure_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.pressure_tab, text="Pressure Transmitter")

        # Add visualization plots
        self.setup_plots()

    def setup_plots(self):
        """
        Setup data visualization plots for the dashboard.
        """
        # Flow Meter Plot
        self.plot_data(mock_data["Timestamp"], mock_data["Flow_Meter"],
                       "Flow Meter Data", "Time", "Flow Rate (L/min)", self.flow_tab)

        # Temperature Sensor Plot
        self.plot_data(mock_data["Timestamp"], mock_data["Temperature_Sensor"],
                       "Temperature Sensor Data", "Time", "Temperature (°C)", self.temperature_tab)

        # Pressure Transmitter Plot
        self.plot_data(mock_data["Timestamp"], mock_data["Pressure_Transmitter"],
                       "Pressure Transmitter Data", "Time", "Pressure (Bar)", self.pressure_tab)

    def plot_data(self, x, y, title, xlabel, ylabel, parent):
        """
        Create a matplotlib plot embedded in a Tkinter frame.
        :param x: Data for the x-axis.
        :param y: Data for the y-axis.
        :param title: Title of the plot.
        :param xlabel: Label for the x-axis.
        :param ylabel: Label for the y-axis.
        :param parent: The parent Tkinter frame.
        """
        fig, ax = plt.subplots(figsize=(5, 4))
        ax.plot(x, y, label=title, color="blue")
        ax.set_title(title)
        ax.set_xlabel(xlabel)
        ax.set_ylabel(ylabel)
        ax.legend()

        # Embed the plot in the Tkinter frame
        canvas = plt.backends.backend_tkagg.FigureCanvasTkAgg(fig, master=parent)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

# Error handling for running the application
try:
    root = tk.Tk()
    app = DashboardApp(root)
    root.mainloop()
except Exception as e:
    messagebox.showerror("Error", f"An unexpected error occurred: {e}")
```
