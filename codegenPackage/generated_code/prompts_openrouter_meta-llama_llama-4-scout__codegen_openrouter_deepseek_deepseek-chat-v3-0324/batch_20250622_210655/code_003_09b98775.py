"""
Generated Code Metadata:
========================
Original URL: https://instrumentacionum.com
Prompt: "Design a control panel for an industrial setting using Instrumentación UM's tableros de control and sensores de presion, including a wiring diagram."
Generated: DETERMINISTIC_09b98775e7c835f7
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import json
import serial
import threading
import time

class IndustrialControlPanel:
    def __init__(self, root):
        self.root = root
        self.root.title("Instrumentación UM - Control Panel")
        self.root.geometry("1000x700")
        
        # Serial connection variables
        self.serial_connection = None
        self.is_connected = False
        self.serial_thread = None
        self.stop_thread = False
        
        # Sensor data storage
        self.pressure_data = []
        self.max_data_points = 100
        
        # Initialize UI
        self.setup_ui()
        
        # Load default configuration
        self.load_config()
        
    def setup_ui(self):
        """Initialize all UI components"""
        # Main frame
        self.main_frame = ttk.Frame(self.root, padding="10")
        self.main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Control panel section
        self.control_frame = ttk.LabelFrame(self.main_frame, text="Control Panel", padding="10")
        self.control_frame.pack(side=tk.LEFT, fill=tk.Y, padx=5, pady=5)
        
        # Connection controls
        self.connection_frame = ttk.LabelFrame(self.control_frame, text="Connection Settings", padding="5")
        self.connection_frame.pack(fill=tk.X, pady=5)
        
        self.port_label = ttk.Label(self.connection_frame, text="Port:")
        self.port_label.pack(side=tk.LEFT)
        
        self.port_entry = ttk.Entry(self.connection_frame, width=10)
        self.port_entry.pack(side=tk.LEFT, padx=5)
        self.port_entry.insert(0, "COM3")
        
        self.baud_label = ttk.Label(self.connection_frame, text="Baud Rate:")
        self.baud_label.pack(side=tk.LEFT, padx=(10,0))
        
        self.baud_combo = ttk.Combobox(self.connection_frame, values=["9600", "19200", "38400", "57600", "115200"], width=8)
        self.baud_combo.pack(side=tk.LEFT, padx=5)
        self.baud_combo.set("9600")
        
        self.connect_btn = ttk.Button(self.connection_frame, text="Connect", command=self.toggle_connection)
        self.connect_btn.pack(side=tk.RIGHT)
        
        # Pressure sensor controls
        self.sensor_frame = ttk.LabelFrame(self.control_frame, text="Pressure Sensors", padding="5")
        self.sensor_frame.pack(fill=tk.X, pady=5)
        
        self.sensor1_label = ttk.Label(self.sensor_frame, text="Sensor 1 (PSI):")
        self.sensor1_label.pack(side=tk.LEFT)
        
        self.sensor1_value = ttk.Label(self.sensor_frame, text="0.00", width=8)
        self.sensor1_value.pack(side=tk.LEFT, padx=5)
        
        self.sensor2_label = ttk.Label(self.sensor_frame, text="Sensor 2 (PSI):")
        self.sensor2_label.pack(side=tk.LEFT, padx=(10,0))
        
        self.sensor2_value = ttk.Label(self.sensor_frame, text="0.00", width=8)
        self.sensor2_value.pack(side=tk.LEFT, padx=5)
        
        # Alarm settings
        self.alarm_frame = ttk.LabelFrame(self.control_frame, text="Alarm Settings", padding="5")
        self.alarm_frame.pack(fill=tk.X, pady=5)
        
        self.high_alarm_label = ttk.Label(self.alarm_frame, text="High Alarm (PSI):")
        self.high_alarm_label.pack(side=tk.LEFT)
        
        self.high_alarm_entry = ttk.Entry(self.alarm_frame, width=8)
        self.high_alarm_entry.pack(side=tk.LEFT, padx=5)
        self.high_alarm_entry.insert(0, "100.0")
        
        self.low_alarm_label = ttk.Label(self.alarm_frame, text="Low Alarm (PSI):")
        self.low_alarm_label.pack(side=tk.LEFT, padx=(10,0))
        
        self.low_alarm_entry = ttk.Entry(self.alarm_frame, width=8)
        self.low_alarm_entry.pack(side=tk.LEFT, padx=5)
        self.low_alarm_entry.insert(0, "10.0")
        
        self.set_alarm_btn = ttk.Button(self.alarm_frame, text="Set Alarms", command=self.set_alarms)
        self.set_alarm_btn.pack(side=tk.RIGHT)
        
        # System controls
        self.system_frame = ttk.LabelFrame(self.control_frame, text="System Controls", padding="5")
        self.system_frame.pack(fill=tk.X, pady=5)
        
        self.pump_btn = ttk.Button(self.system_frame, text="Start Pump", command=self.toggle_pump)
        self.pump_btn.pack(side=tk.LEFT)
        
        self.valve_btn = ttk.Button(self.system_frame, text="Open Valve", command=self.toggle_valve)
        self.valve_btn.pack(side=tk.LEFT, padx=10)
        
        self.emergency_btn = ttk.Button(self.system_frame, text="EMERGENCY STOP", style="Emergency.TButton")
        self.emergency_btn.pack(side=tk.RIGHT)
        
        # Status indicators
        self.status_frame = ttk.LabelFrame(self.control_frame, text="Status Indicators", padding="5")
        self.status_frame.pack(fill=tk.X, pady=5)
        
        self.connection_status = ttk.Label(self.status_frame, text="Disconnected", foreground="red")
        self.connection_status.pack(side=tk.LEFT)
        
        self.pump_status = ttk.Label(self.status_frame, text="Pump: OFF", foreground="red")
        self.pump_status.pack(side=tk.LEFT, padx=10)
        
        self.valve_status = ttk.Label(self.status_frame, text="Valve: CLOSED", foreground="red")
        self.valve_status.pack(side=tk.LEFT)
        
        # Data visualization frame
        self.viz_frame = ttk.LabelFrame(self.main_frame, text="Pressure Data Visualization", padding="10")
        self.viz_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        self.figure = plt.Figure(figsize=(6, 4), dpi=100)
        self.plot = self.figure.add_subplot(111)
        self.plot.set_title("Pressure Sensor Readings")
        self.plot.set_xlabel("Time")
        self.plot.set_ylabel("Pressure (PSI)")
        self.plot.grid(True)
        
        self.canvas = FigureCanvasTkAgg(self.figure, self.viz_frame)
        self.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
        
        # Wiring diagram button
        self.wiring_btn = ttk.Button(self.control_frame, text="Show Wiring Diagram", command=self.show_wiring_diagram)
        self.wiring_btn.pack(side=tk.BOTTOM, pady=10)
        
        # Configure styles
        self.style = ttk.Style()
        self.style.configure("Emergency.TButton", foreground="white", background="red", font=('Helvetica', 10, 'bold'))
        
    def toggle_connection(self):
        """Toggle serial connection"""
        if not self.is_connected:
            port = self.port_entry.get()
            baud = int(self.baud_combo.get())
            
            try:
                self.serial_connection = serial.Serial(port, baud, timeout=1)
                self.is_connected = True
                self.connect_btn.config(text="Disconnect")
                self.connection_status.config(text="Connected", foreground="green")
                
                # Start thread for reading serial data
                self.stop_thread = False
                self.serial_thread = threading.Thread(target=self.read_serial_data)
                self.serial_thread.daemon = True
                self.serial_thread.start()
                
            except serial.SerialException as e:
                self.show_error(f"Connection Error: {str(e)}")
        else:
            self.stop_thread = True
            if self.serial_thread and self.serial_thread.is_alive():
                self.serial_thread.join(1)
            
            self.serial_connection.close()
            self.is_connected = False
            self.connect_btn.config(text="Connect")
            self.connection_status.config(text="Disconnected", foreground="red")
    
    def read_serial_data(self):
        """Read data from serial port in
