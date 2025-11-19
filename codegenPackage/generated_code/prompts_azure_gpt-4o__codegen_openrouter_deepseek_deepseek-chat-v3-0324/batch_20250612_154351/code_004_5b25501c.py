"""
Generated Code Metadata:
========================
Original URL: https://climax-polska.pl
Prompt: Suggest a library or framework for designing a user interface to manage and monitor the operation of electric mast lift trucks, based on the features described on the Climax Polska website.
Generated: DETERMINISTIC_5b25501ce5d49f25
Batch ID: 20250612_154351
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
UI Framework for Electric Mast Lift Truck Management System

This script provides a UI framework using PyQt5 for managing and monitoring
electric mast lift trucks based on features from Climax Polska.
"""

import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout,
                             QHBoxLayout, QLabel, QPushButton, QTabWidget,
                             QStatusBar, QMessageBox, QComboBox, QLineEdit,
                             QTableWidget, QTableWidgetItem, QGroupBox)
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QIcon


class LiftTruckUI(QMainWindow):
    """Main application window for the lift truck management system."""
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Electric Mast Lift Truck Manager")
        self.setWindowIcon(QIcon('truck_icon.png'))
        self.setMinimumSize(1024, 768)
        
        # Initialize UI components
        self.init_ui()
        
        # Setup status bar
        self.status_bar = QStatusBar()
        self.setStatusBar(self.status_bar)
        self.status_bar.showMessage("System Ready", 3000)
        
        # Setup data refresh timer
        self.refresh_timer = QTimer()
        self.refresh_timer.timeout.connect(self.update_data)
        self.refresh_timer.start(5000)  # Refresh every 5 seconds
        
    def init_ui(self):
        """Initialize all UI components."""
        # Main widget and layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout(central_widget)
        
        # Header section
        header = QLabel("Electric Mast Lift Truck Management System")
        header.setAlignment(Qt.AlignCenter)
        header.setStyleSheet("font-size: 24px; font-weight: bold; margin: 10px;")
        main_layout.addWidget(header)
        
        # Tab widget for different sections
        self.tabs = QTabWidget()
        main_layout.addWidget(self.tabs)
        
        # Add tabs
        self.add_dashboard_tab()
        self.add_control_tab()
        self.add_maintenance_tab()
        self.add_settings_tab()
        
        # Footer buttons
        footer_layout = QHBoxLayout()
        emergency_btn = QPushButton("EMERGENCY STOP")
        emergency_btn.setStyleSheet("background-color: red; color: white; font-weight: bold;")
        emergency_btn.clicked.connect(self.emergency_stop)
        footer_layout.addWidget(emergency_btn)
        
        refresh_btn = QPushButton("Refresh Data")
        refresh_btn.clicked.connect(self.update_data)
        footer_layout.addWidget(refresh_btn)
        
        main_layout.addLayout(footer_layout)
    
    def add_dashboard_tab(self):
        """Create the dashboard tab with operational metrics."""
        dashboard_tab = QWidget()
        layout = QVBoxLayout(dashboard_tab)
        
        # Status indicators
        status_group = QGroupBox("Current Status")
        status_layout = QHBoxLayout()
        
        # Add status indicators
        indicators = [
            ("Battery Level", "85%", "green"),
            ("Load Capacity", "1200 kg", "blue"),
            ("Height", "8.2 m", "blue"),
            ("Temperature", "24°C", "green"),
            ("Errors", "0", "green")
        ]
        
        for text, value, color in indicators:
            indicator = QLabel(f"<b>{text}:</b> {value}")
            indicator.setStyleSheet(f"color: {color}; font-size: 16px;")
            indicator.setAlignment(Qt.AlignCenter)
            status_layout.addWidget(indicator)
        
        status_group.setLayout(status_layout)
        layout.addWidget(status_group)
        
        # Operational data table
        self.data_table = QTableWidget()
        self.data_table.setColumnCount(4)
        self.data_table.setHorizontalHeaderLabels(["Parameter", "Value", "Unit", "Status"])
        self.data_table.setEditTriggers(QTableWidget.NoEditTriggers)
        layout.addWidget(self.data_table)
        
        self.tabs.addTab(dashboard_tab, "Dashboard")
    
    def add_control_tab(self):
        """Create the control tab for manual operations."""
        control_tab = QWidget()
        layout = QVBoxLayout(control_tab)
        
        # Movement controls
        move_group = QGroupBox("Movement Controls")
        move_layout = QVBoxLayout()
        
        # Height control
        height_layout = QHBoxLayout()
        height_layout.addWidget(QLabel("Height:"))
        self.height_slider = QComboBox()
        self.height_slider.addItems([f"{i}m" for i in range(1, 13)])
        height_layout.addWidget(self.height_slider)
        move_layout.addLayout(height_layout)
        
        # Direction buttons
        btn_layout = QHBoxLayout()
        directions = ["Up", "Down", "Left", "Right", "Stop"]
        for direction in directions:
            btn = QPushButton(direction)
            btn.clicked.connect(lambda _, d=direction: self.move_truck(d))
            btn_layout.addWidget(btn)
        move_layout.addLayout(btn_layout)
        
        move_group.setLayout(move_layout)
        layout.addWidget(move_group)
        
        # Speed control
        speed_group = QGroupBox("Speed Control")
        speed_layout = QHBoxLayout()
        speed_layout.addWidget(QLabel("Speed:"))
        self.speed_input = QLineEdit("50")
        self.speed_input.setValidator(Qt.QIntValidator(0, 100))
        speed_layout.addWidget(self.speed_input)
        speed_layout.addWidget(QLabel("%"))
        speed_group.setLayout(speed_layout)
        layout.addWidget(speed_group)
        
        self.tabs.addTab(control_tab, "Control")
    
    def add_maintenance_tab(self):
        """Create the maintenance tab for service operations."""
        maintenance_tab = QWidget()
        layout = QVBoxLayout(maintenance_tab)
        
        # Maintenance log
        log_group = QGroupBox("Maintenance Log")
        log_layout = QVBoxLayout()
        self.maintenance_log = QTableWidget()
        self.maintenance_log.setColumnCount(4)
        self.maintenance_log.setHorizontalHeaderLabels(["Date", "Service", "Technician", "Notes"])
        log_layout.addWidget(self.maintenance_log)
        log_group.setLayout(log_layout)
        layout.addWidget(log_group)
        
        # Add maintenance record
        add_group = QGroupBox("Add Maintenance Record")
        add_layout = QVBoxLayout()
        
        form_layout = QHBoxLayout()
        form_layout.addWidget(QLabel("Service:"))
        self.service_input = QLineEdit()
        form_layout.addWidget(self.service_input)
        add_layout.addLayout(form_layout)
        
        form_layout = QHBoxLayout()
        form_layout.addWidget(QLabel("Technician:"))
        self.tech_input = QLineEdit()
        form_layout.addWidget(self.tech_input)
        add_layout.addLayout(form_layout)
        
        form_layout = QHBoxLayout()
        form_layout.addWidget(QLabel("Notes:"))
        self.notes_input = QLineEdit()
        form_layout.addWidget(self.notes_input)
        add_layout.addLayout(form_layout)
        
        add_btn = QPushButton("Add Record")
        add_btn.clicked.connect(self.add_maintenance_record)
        add_layout.addWidget(add_btn)
        
        add_group.setLayout(add_layout)
        layout.addWidget(add_group)
        
        self.tabs.addTab(maintenance_tab, "Maintenance")
    
    def add_settings_tab(self):
        """Create the settings tab for system configuration."""
        settings_tab = QWidget()
        layout = QVBoxLayout(settings_tab)
        
        # System settings
        settings_group = QGroupBox("System Settings")
        settings_layout = QVBoxLayout()
        
        # Truck selection
        truck_layout = QHBoxLayout()
        truck_layout.addWidget(QLabel("Active Truck:"))
        self.truck_selector = QComboBox()
        self.truck_selector.addItems(["Truck 1", "Truck 2", "Truck 3"])
        truck_layout.addWidget(self.truck_selector)
        settings_layout.addLayout(truck_layout)
        
        # Refresh interval
        interval_layout = QHBoxLayout()
        interval_layout.addWidget(QLabel("Refresh Interval (s):"))
        self.interval_input = QLineEdit("5")
        self.interval_input.setValidator(Qt.QIntValidator(1, 60))
        interval_layout.addWidget(self.interval_input)
        interval_layout.addWidget(QLabel("seconds"))
        settings_layout.addLayout(interval_layout)
        
        # Save button
        save_btn = QPushButton("Save Settings")
        save_btn.clicked.connect(self.save_settings)
        settings_layout.addWidget(save_btn)
        
        settings_group.setLayout(settings_layout)
        layout.addWidget(settings_group)
        
        self.tabs.addTab(settings_tab, "Settings")
    
    def update_data(self):
        """Update all displayed data from the
