"""
Generated Code Metadata:
========================
Original URL: https://arbitum.cz
Prompt: Create a workflow automation script for handling leasing and loan applications for vehicle purchases, as facilitated by Arbitum Consulting.
Generated: DETERMINISTIC_1aa83961640c7e1a
Batch ID: 20250612_150347
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import os
from datetime import datetime
from typing import Dict, List, Optional, Union
import logging
from enum import Enum

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class ApplicationType(Enum):
    LEASE = "lease"
    LOAN = "loan"

class ApplicationStatus(Enum):
    RECEIVED = "received"
    UNDER_REVIEW = "under_review"
    APPROVED = "approved"
    REJECTED = "rejected"
    COMPLETED = "completed"

class VehicleType(Enum):
    CAR = "car"
    TRUCK = "truck"
    SUV = "suv"
    MOTORCYCLE = "motorcycle"

class Applicant:
    def __init__(
        self,
        name: str,
        email: str,
        phone: str,
        address: str,
        credit_score: int,
        annual_income: float
    ):
        self.name = name
        self.email = email
        self.phone = phone
        self.address = address
        self.credit_score = credit_score
        self.annual_income = annual_income

    def to_dict(self) -> Dict:
        return {
            "name": self.name,
            "email": self.email,
            "phone": self.phone,
            "address": self.address,
            "credit_score": self.credit_score,
            "annual_income": self.annual_income
        }

class Vehicle:
    def __init__(
        self,
        make: str,
        model: str,
        year: int,
        vehicle_type: VehicleType,
        price: float,
        vin: str
    ):
        self.make = make
        self.model = model
        self.year = year
        self.vehicle_type = vehicle_type
        self.price = price
        self.vin = vin

    def to_dict(self) -> Dict:
        return {
            "make": self.make,
            "model": self.model,
            "year": self.year,
            "vehicle_type": self.vehicle_type.value,
            "price": self.price,
            "vin": self.vin
        }

class Application:
    def __init__(
        self,
        application_id: str,
        application_type: ApplicationType,
        applicant: Applicant,
        vehicle: Vehicle,
        term_months: int,
        down_payment: float,
        status: ApplicationStatus = ApplicationStatus.RECEIVED,
        created_at: Optional[datetime] = None,
        updated_at: Optional[datetime] = None
    ):
        self.application_id = application_id
        self.application_type = application_type
        self.applicant = applicant
        self.vehicle = vehicle
        self.term_months = term_months
        self.down_payment = down_payment
        self.status = status
        self.created_at = created_at or datetime.now()
        self.updated_at = updated_at or datetime.now()

    def to_dict(self) -> Dict:
        return {
            "application_id": self.application_id,
            "application_type": self.application_type.value,
            "applicant": self.applicant.to_dict(),
            "vehicle": self.vehicle.to_dict(),
            "term_months": self.term_months,
            "down_payment": self.down_payment,
            "status": self.status.value,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat()
        }

    def update_status(self, new_status: ApplicationStatus):
        self.status = new_status
        self.updated_at = datetime.now()
        logger.info(f"Application {self.application_id} status updated to {new_status.value}")

class ApplicationProcessor:
    def __init__(self, data_dir: str = "data"):
        self.data_dir = data_dir
        os.makedirs(self.data_dir, exist_ok=True)

    def _get_file_path(self, application_id: str) -> str:
        return os.path.join(self.data_dir, f"{application_id}.json")

    def save_application(self, application: Application) -> bool:
        try:
            file_path = self._get_file_path(application.application_id)
            with open(file_path, 'w') as f:
                json.dump(application.to_dict(), f, indent=2)
            logger.info(f"Application {application.application_id} saved successfully")
            return True
        except Exception as e:
            logger.error(f"Error saving application {application.application_id}: {str(e)}")
            return False

    def load_application(self, application_id: str) -> Optional[Application]:
        try:
            file_path = self._get_file_path(application_id)
            if not os.path.exists(file_path):
                logger.warning(f"Application {application_id} not found")
                return None

            with open(file_path, 'r') as f:
                data = json.load(f)

            applicant_data = data['applicant']
            applicant = Applicant(
                name=applicant_data['name'],
                email=applicant_data['email'],
                phone=applicant_data['phone'],
                address=applicant_data['address'],
                credit_score=applicant_data['credit_score'],
                annual_income=applicant_data['annual_income']
            )

            vehicle_data = data['vehicle']
            vehicle = Vehicle(
                make=vehicle_data['make'],
                model=vehicle_data['model'],
                year=vehicle_data['year'],
                vehicle_type=VehicleType(vehicle_data['vehicle_type']),
                price=vehicle_data['price'],
                vin=vehicle_data['vin']
            )

            return Application(
                application_id=data['application_id'],
                application_type=ApplicationType(data['application_type']),
                applicant=applicant,
                vehicle=vehicle,
                term_months=data['term_months'],
                down_payment=data['down_payment'],
                status=ApplicationStatus(data['status']),
                created_at=datetime.fromisoformat(data['created_at']),
                updated_at=datetime.fromisoformat(data['updated_at'])
            )
        except Exception as e:
            logger.error(f"Error loading application {application_id}: {str(e)}")
            return None

    def process_application(self, application: Application) -> bool:
        try:
            logger.info(f"Processing application {application.application_id}")
            
            # Basic validation
            if not self._validate_application(application):
                application.update_status(ApplicationStatus.REJECTED)
                self.save_application(application)
                return False

            # Move to under review
            application.update_status(ApplicationStatus.UNDER_REVIEW)
            self.save_application(application)

            # Simulate underwriting process
            if self._underwrite_application(application):
                application.update_status(ApplicationStatus.APPROVED)
            else:
                application.update_status(ApplicationStatus.REJECTED)

            self.save_application(application)
            return application.status == ApplicationStatus.APPROVED
        except Exception as e:
            logger.error(f"Error processing application {application.application_id}: {str(e)}")
            return False

    def _validate_application(self, application: Application) -> bool:
        # Basic validation rules
        if not application.applicant.name or not application.applicant.email:
            logger.warning("Missing required applicant information")
            return False

        if application.vehicle.price <= 0:
            logger.warning("Invalid vehicle price")
            return False

        if application.term_months <= 0:
            logger.warning("Invalid term length")
            return False

        if application.down_payment < 0:
            logger.warning("Invalid down payment amount")
            return False

        return True

    def _underwrite_application(self, application: Application) -> bool:
        # Simple underwriting logic
        credit_score = application.applicant.credit_score
        income = application.applicant.annual_income
        monthly_payment = self._calculate_monthly_payment(application)

        # Basic approval criteria
        if credit_score < 600:
            logger.info("Credit score too low")
            return False

        if monthly_payment > (income * 0.15):
            logger.info("Debt-to-income ratio too high")
            return False

        return True

    def _calculate_monthly_payment(self, application: Application) -> float:
        # Simplified payment calculation
        principal = application.vehicle.price - application.down_payment
        if application.application_type == ApplicationType.LEASE:
            # Lease calculation (simplified)
            residual = application.vehicle.price * 0.6  # 40% depreciation
            lease_amount = principal - residual
            return lease_amount / application.term_months
        else:
            # Loan calculation (simplified)
            interest_rate = 0.05  # 5% annual interest
            monthly_rate = interest_rate / 12
            numerator = monthly_rate * principal
            denominator = 1 - (1 + monthly_rate) ** (-application.term_months)
            return numerator / denominator

    def list_applications(self, status: Optional[ApplicationStatus] = None) -> List[Dict]:
        applications = []
        try:
            for filename in os.listdir(self.data_dir):
                if filename.endswith('.
