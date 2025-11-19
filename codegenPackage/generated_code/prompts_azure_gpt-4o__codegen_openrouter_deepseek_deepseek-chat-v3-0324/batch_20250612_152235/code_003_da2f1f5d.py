"""
Generated Code Metadata:
========================
Original URL: https://humanxpert.com
Prompt: Provide a Python script for tracking and collecting unpaid medical accounts receivable, inspired by Human Xpert's specialized services.
Generated: DETERMINISTIC_da2f1f5d74d25a51
Batch ID: 20250612_152235
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Medical Accounts Receivable Tracker

This script helps track and collect unpaid medical accounts receivable.
It provides functionality to manage patient records, track unpaid invoices,
and generate reports for follow-up actions.

Features:
- Patient record management
- Invoice tracking with aging reports
- Collection status updates
- Reporting capabilities
"""

import csv
import datetime
from dataclasses import dataclass
from typing import List, Optional, Dict
import os
import json
from enum import Enum, auto


class CollectionStatus(Enum):
    """Enum representing different collection statuses"""
    CURRENT = auto()
    PAST_DUE_30 = auto()
    PAST_DUE_60 = auto()
    PAST_DUE_90 = auto()
    PAST_DUE_120 = auto()
    IN_COLLECTIONS = auto()
    WRITTEN_OFF = auto()
    PAID = auto()


@dataclass
class Patient:
    """Data class representing a patient"""
    patient_id: str
    first_name: str
    last_name: str
    date_of_birth: str
    address: str
    phone: str
    email: Optional[str] = None
    insurance_provider: Optional[str] = None
    insurance_id: Optional[str] = None


@dataclass
class Invoice:
    """Data class representing an invoice"""
    invoice_id: str
    patient_id: str
    service_date: str
    service_description: str
    amount: float
    amount_paid: float = 0.0
    date_issued: str = datetime.date.today().isoformat()
    due_date: str = (datetime.date.today() + datetime.timedelta(days=30)).isoformat()
    status: CollectionStatus = CollectionStatus.CURRENT

    @property
    def balance(self) -> float:
        """Calculate remaining balance"""
        return self.amount - self.amount_paid

    @property
    def days_overdue(self) -> int:
        """Calculate days overdue"""
        due_date = datetime.date.fromisoformat(self.due_date)
        today = datetime.date.today()
        return (today - due_date).days if today > due_date else 0

    def update_status(self) -> None:
        """Update collection status based on days overdue"""
        days = self.days_overdue
        if days <= 0:
            self.status = CollectionStatus.CURRENT
        elif 1 <= days <= 30:
            self.status = CollectionStatus.PAST_DUE_30
        elif 31 <= days <= 60:
            self.status = CollectionStatus.PAST_DUE_60
        elif 61 <= days <= 90:
            self.status = CollectionStatus.PAST_DUE_90
        elif 91 <= days <= 120:
            self.status = CollectionStatus.PAST_DUE_120
        else:
            self.status = CollectionStatus.IN_COLLECTIONS


class AccountsReceivableTracker:
    """Main class for tracking medical accounts receivable"""
    
    def __init__(self, data_dir: str = "data"):
        """Initialize the tracker with data directory"""
        self.data_dir = data_dir
        self.patients: Dict[str, Patient] = {}
        self.invoices: Dict[str, Invoice] = {}
        
        # Create data directory if it doesn't exist
        os.makedirs(self.data_dir, exist_ok=True)
        
        # Load existing data
        self._load_data()

    def _load_data(self) -> None:
        """Load patient and invoice data from files"""
        try:
            # Load patients
            patients_path = os.path.join(self.data_dir, "patients.json")
            if os.path.exists(patients_path):
                with open(patients_path, "r") as f:
                    patients_data = json.load(f)
                    self.patients = {
                        pid: Patient(**data) for pid, data in patients_data.items()
                    }

            # Load invoices
            invoices_path = os.path.join(self.data_dir, "invoices.json")
            if os.path.exists(invoices_path):
                with open(invoices_path, "r") as f:
                    invoices_data = json.load(f)
                    self.invoices = {
                        inv_id: Invoice(**data) for inv_id, data in invoices_data.items()
                    }
        except Exception as e:
            print(f"Error loading data: {e}")

    def _save_data(self) -> None:
        """Save patient and invoice data to files"""
        try:
            # Save patients
            patients_path = os.path.join(self.data_dir, "patients.json")
            with open(patients_path, "w") as f:
                patients_data = {
                    pid: {
                        "patient_id": p.patient_id,
                        "first_name": p.first_name,
                        "last_name": p.last_name,
                        "date_of_birth": p.date_of_birth,
                        "address": p.address,
                        "phone": p.phone,
                        "email": p.email,
                        "insurance_provider": p.insurance_provider,
                        "insurance_id": p.insurance_id
                    } for pid, p in self.patients.items()
                }
                json.dump(patients_data, f, indent=2)

            # Save invoices
            invoices_path = os.path.join(self.data_dir, "invoices.json")
            with open(invoices_path, "w") as f:
                invoices_data = {
                    inv_id: {
                        "invoice_id": inv.invoice_id,
                        "patient_id": inv.patient_id,
                        "service_date": inv.service_date,
                        "service_description": inv.service_description,
                        "amount": inv.amount,
                        "amount_paid": inv.amount_paid,
                        "date_issued": inv.date_issued,
                        "due_date": inv.due_date,
                        "status": inv.status.name
                    } for inv_id, inv in self.invoices.items()
                }
                json.dump(invoices_data, f, indent=2)
        except Exception as e:
            print(f"Error saving data: {e}")

    def add_patient(self, patient: Patient) -> None:
        """Add a new patient to the system"""
        if patient.patient_id in self.patients:
            raise ValueError(f"Patient with ID {patient.patient_id} already exists")
        self.patients[patient.patient_id] = patient
        self._save_data()

    def update_patient(self, patient_id: str, **kwargs) -> None:
        """Update patient information"""
        if patient_id not in self.patients:
            raise ValueError(f"Patient with ID {patient_id} not found")
        
        patient = self.patients[patient_id]
        for key, value in kwargs.items():
            if hasattr(patient, key):
                setattr(patient, key, value)
        
        self._save_data()

    def add_invoice(self, invoice: Invoice) -> None:
        """Add a new invoice to the system"""
        if invoice.invoice_id in self.invoices:
            raise ValueError(f"Invoice with ID {invoice.invoice_id} already exists")
        if invoice.patient_id not in self.patients:
            raise ValueError(f"Patient with ID {invoice.patient_id} not found")
        
        invoice.update_status()
        self.invoices[invoice.invoice_id] = invoice
        self._save_data()

    def record_payment(self, invoice_id: str, amount: float) -> None:
        """Record a payment against an invoice"""
        if invoice_id not in self.invoices:
            raise ValueError(f"Invoice with ID {invoice_id} not found")
        
        invoice = self.invoices[invoice_id]
        invoice.amount_paid += amount
        
        if invoice.balance <= 0:
            invoice.status = CollectionStatus.PAID
        
        self._save_data()

    def update_invoice_statuses(self) -> None:
        """Update status for all invoices based on their due dates"""
        for invoice in self.invoices.values():
            if invoice.status != CollectionStatus.PAID and invoice.status != CollectionStatus.WRITTEN_OFF:
                invoice.update_status()
        self._save_data()

    def get_patient_invoices(self, patient_id: str) -> List[Invoice]:
        """Get all invoices for a specific patient"""
        if patient_id not in self.patients:
            raise ValueError(f"Patient with ID {patient_id} not found")
        
        return [inv for inv in self.invoices.values() if inv.patient_id == patient_id]

    def get_overdue_invoices(self, min_days: int = 1) -> List[Invoice]:
        """Get all invoices that are overdue by at least min_days"""
        self.update_invoice_statuses()
        return [inv for inv in self.invoices.values() 
                if inv.days_overdue >= min_days and inv.status != CollectionStatus.PAID]

    def generate_aging_report(self) -> Dict[str, List[Invoice]]:
        """Generate an aging report categorizing invoices by their status"""
        self.update_invoice_statuses()
        
        report = {
            "current": [],
            "30_days": [],
            "60_days": [],
            "90_days": [],
            "120_days": [],
            "collections": [],
            "written_off": []
        }
        
        for invoice in self.invoices.values():
            if invoice.status == CollectionStatus.CURRENT:
                report["current"].append(in
