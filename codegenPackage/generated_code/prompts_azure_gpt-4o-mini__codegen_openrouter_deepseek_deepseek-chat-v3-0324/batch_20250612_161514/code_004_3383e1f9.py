"""
Generated Code Metadata:
========================
Original URL: https://www.napatablets.com
Prompt: Create a tutorial on how to use the Delivery Tracker for tracking deliveries and analyzing performance metrics in an auto parts business.
Generated: DETERMINISTIC_3383e1f9900a5f7e
Batch ID: 20250612_161514
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Delivery Tracker for Auto Parts Business

This module provides functionality to track deliveries and analyze performance metrics
for an auto parts business. It includes features to add deliveries, update statuses,
generate reports, and calculate key performance indicators (KPIs).

Features:
- Add new deliveries with relevant details
- Update delivery status (Pending, In Transit, Delivered, Failed)
- Generate delivery reports (daily, weekly, monthly)
- Calculate performance metrics (on-time delivery rate, average delivery time)
"""

import csv
import datetime
from enum import Enum
import os
from typing import List, Dict, Optional

class DeliveryStatus(Enum):
    """Enum representing possible delivery statuses."""
    PENDING = "Pending"
    IN_TRANSIT = "In Transit"
    DELIVERED = "Delivered"
    FAILED = "Failed"

class Delivery:
    """Class representing a single delivery record."""
    
    def __init__(self, delivery_id: str, customer_name: str, parts: List[str], 
                 order_date: datetime.date, estimated_delivery: datetime.date,
                 status: DeliveryStatus = DeliveryStatus.PENDING):
        """
        Initialize a delivery record.
        
        Args:
            delivery_id: Unique identifier for the delivery
            customer_name: Name of the customer
            parts: List of parts in the delivery
            order_date: Date when order was placed
            estimated_delivery: Estimated delivery date
            status: Current status of delivery (default: Pending)
        """
        self.delivery_id = delivery_id
        self.customer_name = customer_name
        self.parts = parts
        self.order_date = order_date
        self.estimated_delivery = estimated_delivery
        self.status = status
        self.actual_delivery: Optional[datetime.date] = None
        self.notes: str = ""

    def update_status(self, new_status: DeliveryStatus, 
                     actual_delivery: Optional[datetime.date] = None,
                     notes: str = "") -> None:
        """
        Update the delivery status and related information.
        
        Args:
            new_status: New status to set
            actual_delivery: Actual delivery date (required if status is Delivered)
            notes: Any additional notes about the delivery
        """
        if new_status == DeliveryStatus.DELIVERED and actual_delivery is None:
            raise ValueError("Actual delivery date is required for Delivered status")
            
        self.status = new_status
        self.actual_delivery = actual_delivery
        self.notes = notes

    def is_on_time(self) -> bool:
        """Check if delivery was completed on or before estimated date."""
        if self.status != DeliveryStatus.DELIVERED or self.actual_delivery is None:
            return False
        return self.actual_delivery <= self.estimated_delivery

    def delivery_time_days(self) -> Optional[int]:
        """Calculate delivery time in days (order to delivery)."""
        if self.status != DeliveryStatus.DELIVERED or self.actual_delivery is None:
            return None
        return (self.actual_delivery - self.order_date).days

class DeliveryTracker:
    """Main class for tracking deliveries and generating reports."""
    
    def __init__(self, data_file: str = "deliveries.csv"):
        """
        Initialize the delivery tracker.
        
        Args:
            data_file: Path to CSV file for storing delivery data
        """
        self.data_file = data_file
        self.deliveries: Dict[str, Delivery] = {}
        self._load_data()

    def _load_data(self) -> None:
        """Load delivery data from CSV file."""
        if not os.path.exists(self.data_file):
            return
            
        with open(self.data_file, mode='r', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                try:
                    delivery = Delivery(
                        delivery_id=row['delivery_id'],
                        customer_name=row['customer_name'],
                        parts=row['parts'].split(';'),
                        order_date=datetime.datetime.strptime(row['order_date'], '%Y-%m-%d').date(),
                        estimated_delivery=datetime.datetime.strptime(row['estimated_delivery'], '%Y-%m-%d').date(),
                        status=DeliveryStatus(row['status'])
                    )
                    if row['actual_delivery']:
                        delivery.actual_delivery = datetime.datetime.strptime(row['actual_delivery'], '%Y-%m-%d').date()
                    delivery.notes = row['notes']
                    self.deliveries[delivery.delivery_id] = delivery
                except (KeyError, ValueError) as e:
                    print(f"Error loading delivery {row.get('delivery_id', 'unknown')}: {str(e)}")

    def _save_data(self) -> None:
        """Save delivery data to CSV file."""
        fieldnames = [
            'delivery_id', 'customer_name', 'parts', 'order_date', 
            'estimated_delivery', 'status', 'actual_delivery', 'notes'
        ]
        
        with open(self.data_file, mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            
            for delivery in self.deliveries.values():
                writer.writerow({
                    'delivery_id': delivery.delivery_id,
                    'customer_name': delivery.customer_name,
                    'parts': ';'.join(delivery.parts),
                    'order_date': delivery.order_date.strftime('%Y-%m-%d'),
                    'estimated_delivery': delivery.estimated_delivery.strftime('%Y-%m-%d'),
                    'status': delivery.status.value,
                    'actual_delivery': delivery.actual_delivery.strftime('%Y-%m-%d') if delivery.actual_delivery else '',
                    'notes': delivery.notes
                })

    def add_delivery(self, delivery: Delivery) -> None:
        """
        Add a new delivery to the tracker.
        
        Args:
            delivery: Delivery object to add
            
        Raises:
            ValueError: If delivery ID already exists
        """
        if delivery.delivery_id in self.deliveries:
            raise ValueError(f"Delivery ID {delivery.delivery_id} already exists")
            
        self.deliveries[delivery.delivery_id] = delivery
        self._save_data()

    def update_delivery_status(self, delivery_id: str, new_status: DeliveryStatus,
                              actual_delivery: Optional[datetime.date] = None,
                              notes: str = "") -> None:
        """
        Update the status of an existing delivery.
        
        Args:
            delivery_id: ID of delivery to update
            new_status: New status to set
            actual_delivery: Actual delivery date (required if status is Delivered)
            notes: Any additional notes about the delivery
            
        Raises:
            ValueError: If delivery ID doesn't exist or invalid status change
        """
        if delivery_id not in self.deliveries:
            raise ValueError(f"Delivery ID {delivery_id} not found")
            
        self.deliveries[delivery_id].update_status(new_status, actual_delivery, notes)
        self._save_data()

    def get_delivery(self, delivery_id: str) -> Optional[Delivery]:
        """
        Retrieve a delivery by ID.
        
        Args:
            delivery_id: ID of delivery to retrieve
            
        Returns:
            Delivery object if found, None otherwise
        """
        return self.deliveries.get(delivery_id)

    def generate_delivery_report(self, start_date: datetime.date, 
                                end_date: datetime.date) -> List[Delivery]:
        """
        Generate a report of deliveries within a date range.
        
        Args:
            start_date: Start date of report period
            end_date: End date of report period
            
        Returns:
            List of deliveries within the date range
        """
        return [
            delivery for delivery in self.deliveries.values()
            if start_date <= delivery.order_date <= end_date
        ]

    def calculate_on_time_percentage(self, start_date: datetime.date,
                                    end_date: datetime.date) -> float:
        """
        Calculate the percentage of on-time deliveries in a date range.
        
        Args:
            start_date: Start date of period to analyze
            end_date: End date of period to analyze
            
        Returns:
            Percentage of on-time deliveries (0-100)
        """
        relevant_deliveries = [
            delivery for delivery in self.deliveries.values()
            if (delivery.status == DeliveryStatus.DELIVERED and 
                start_date <= delivery.order_date <= end_date)
        ]
        
        if not relevant_deliveries:
            return 0.0
            
        on_time_count = sum(1 for delivery in relevant_deliveries if delivery.is_on_time())
        return (on_time_count / len(relevant_deliveries)) * 100

    def calculate_average_delivery_time(self, start_date: datetime.date,
                                       end_date: datetime.date) -> Optional[float]:
        """
        Calculate average delivery time (in days) for completed deliveries.
        
        Args:
            start_date: Start date of period to analyze
            end_date: End date of period to analyze
            
        Returns:
            Average delivery time in
