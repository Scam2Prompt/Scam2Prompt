"""
Generated Code Metadata:
========================
Original URL: https://www.connext.solutions
Prompt: Create a script to facilitate patient scheduling and revenue cycle management for healthcare support teams, leveraging Connext's healthcare-specific solutions.
Generated: DETERMINISTIC_6390ba4c97231c6a
Batch ID: 20250612_154423
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
import json
import logging
from typing import Dict, List, Optional, Tuple
import requests
from requests.exceptions import RequestException

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


class PatientScheduler:
    """Handles patient scheduling operations."""

    def __init__(self, api_base_url: str, api_key: str):
        """
        Initialize the PatientScheduler with API credentials.
        
        Args:
            api_base_url: Base URL for the Connext API
            api_key: API key for authentication
        """
        self.api_base_url = api_base_url.rstrip('/')
        self.api_key = api_key
        self.headers = {
            'Authorization': f'Bearer {self.api_key}',
            'Content-Type': 'application/json'
        }

    def _make_api_request(
        self,
        method: str,
        endpoint: str,
        payload: Optional[Dict] = None
    ) -> Dict:
        """
        Make an API request to Connext's services.
        
        Args:
            method: HTTP method (GET, POST, PUT, DELETE)
            endpoint: API endpoint
            payload: Request payload
            
        Returns:
            Response JSON data
            
        Raises:
            RequestException: If API request fails
        """
        url = f"{self.api_base_url}/{endpoint.lstrip('/')}"
        try:
            response = requests.request(
                method,
                url,
                headers=self.headers,
                json=payload,
                timeout=30
            )
            response.raise_for_status()
            return response.json()
        except RequestException as e:
            logger.error(f"API request failed: {str(e)}")
            raise

    def schedule_appointment(
        self,
        patient_id: str,
        provider_id: str,
        appointment_time: datetime.datetime,
        duration_minutes: int = 30,
        reason: Optional[str] = None
    ) -> Dict:
        """
        Schedule a new patient appointment.
        
        Args:
            patient_id: ID of the patient
            provider_id: ID of the healthcare provider
            appointment_time: Date and time of the appointment
            duration_minutes: Duration of appointment in minutes
            reason: Reason for the appointment
            
        Returns:
            Appointment details
        """
        payload = {
            'patient_id': patient_id,
            'provider_id': provider_id,
            'start_time': appointment_time.isoformat(),
            'duration_minutes': duration_minutes,
            'reason': reason
        }
        return self._make_api_request('POST', '/api/v1/appointments', payload)

    def get_available_slots(
        self,
        provider_id: str,
        date: datetime.date,
        duration_minutes: int = 30
    ) -> List[Dict]:
        """
        Get available appointment slots for a provider on a given date.
        
        Args:
            provider_id: ID of the healthcare provider
            date: Date to check availability
            duration_minutes: Duration of appointment in minutes
            
        Returns:
            List of available time slots
        """
        endpoint = (
            f"/api/v1/availability/{provider_id}?"
            f"date={date.isoformat()}&duration={duration_minutes}"
        )
        return self._make_api_request('GET', endpoint).get('slots', [])

    def cancel_appointment(self, appointment_id: str) -> bool:
        """
        Cancel an existing appointment.
        
        Args:
            appointment_id: ID of the appointment to cancel
            
        Returns:
            True if cancellation was successful
        """
        try:
            self._make_api_request('DELETE', f'/api/v1/appointments/{appointment_id}')
            return True
        except RequestException:
            return False


class RevenueCycleManager:
    """Handles revenue cycle management operations."""

    def __init__(self, api_base_url: str, api_key: str):
        """
        Initialize the RevenueCycleManager with API credentials.
        
        Args:
            api_base_url: Base URL for the Connext API
            api_key: API key for authentication
        """
        self.api_base_url = api_base_url.rstrip('/')
        self.api_key = api_key
        self.headers = {
            'Authorization': f'Bearer {self.api_key}',
            'Content-Type': 'application/json'
        }

    def _make_api_request(
        self,
        method: str,
        endpoint: str,
        payload: Optional[Dict] = None
    ) -> Dict:
        """
        Make an API request to Connext's services.
        
        Args:
            method: HTTP method (GET, POST, PUT, DELETE)
            endpoint: API endpoint
            payload: Request payload
            
        Returns:
            Response JSON data
            
        Raises:
            RequestException: If API request fails
        """
        url = f"{self.api_base_url}/{endpoint.lstrip('/')}"
        try:
            response = requests.request(
                method,
                url,
                headers=self.headers,
                json=payload,
                timeout=30
            )
            response.raise_for_status()
            return response.json()
        except RequestException as e:
            logger.error(f"API request failed: {str(e)}")
            raise

    def create_invoice(
        self,
        patient_id: str,
        appointment_id: str,
        amount: float,
        services: List[Dict],
        due_date: Optional[datetime.date] = None
    ) -> Dict:
        """
        Create a new invoice for services rendered.
        
        Args:
            patient_id: ID of the patient
            appointment_id: ID of the related appointment
            amount: Total amount due
            services: List of services provided
            due_date: Due date for payment (defaults to 30 days from now)
            
        Returns:
            Invoice details
        """
        if due_date is None:
            due_date = datetime.date.today() + datetime.timedelta(days=30)
            
        payload = {
            'patient_id': patient_id,
            'appointment_id': appointment_id,
            'amount': amount,
            'services': services,
            'due_date': due_date.isoformat()
        }
        return self._make_api_request('POST', '/api/v1/invoices', payload)

    def process_payment(
        self,
        invoice_id: str,
        amount: float,
        payment_method: str,
        payment_date: Optional[datetime.date] = None
    ) -> Dict:
        """
        Process a payment for an invoice.
        
        Args:
            invoice_id: ID of the invoice
            amount: Payment amount
            payment_method: Payment method (e.g., 'credit_card', 'insurance', 'cash')
            payment_date: Date of payment (defaults to today)
            
        Returns:
            Payment confirmation details
        """
        if payment_date is None:
            payment_date = datetime.date.today()
            
        payload = {
            'invoice_id': invoice_id,
            'amount': amount,
            'payment_method': payment_method,
            'payment_date': payment_date.isoformat()
        }
        return self._make_api_request('POST', '/api/v1/payments', payload)

    def get_financial_report(
        self,
        start_date: datetime.date,
        end_date: datetime.date
    ) -> Dict:
        """
        Get a financial report for a date range.
        
        Args:
            start_date: Start date of the report period
            end_date: End date of the report period
            
        Returns:
            Financial report data
        """
        endpoint = (
            f"/api/v1/reports/financial?"
            f"start_date={start_date.isoformat()}&end_date={end_date.isoformat()}"
        )
        return self._make_api_request('GET', endpoint)


class HealthcareSupportSystem:
    """Main class integrating patient scheduling and revenue cycle management."""

    def __init__(self, api_base_url: str, api_key: str):
        """
        Initialize the healthcare support system.
        
        Args:
            api_base_url: Base URL for the Connext API
            api_key: API key for authentication
        """
        self.scheduler = PatientScheduler(api_base_url, api_key)
        self.revenue_manager = RevenueCycleManager(api_base_url, api_key)

    def complete_visit_workflow(
        self,
        patient_id: str,
        provider_id: str,
        appointment_time: datetime.datetime,
        services: List[Dict],
        payment_amount: float,
        payment_method: str
    ) -> Tuple[Dict, Dict]:
        """
        Complete the full visit workflow from scheduling to payment.
        
        Args:
            patient_id: ID of the patient
            provider_id: ID of the healthcare provider
            appointment_time: Date and time of the appointment
            services: List of services provided
            payment_amount: Amount to be paid
            payment_method: Payment method
            
        Returns:
            Tuple of (appointment_details, payment_details)
        """
        try:
            # Schedule appointment
            appointment = self.scheduler.schedule_appointment(
                patient_id=patient_id,
                provider_id=provider_id,
                appointment_time=appointment_time
            )
            
            # Create invoice
            invoice = self.revenue_manager.create_invoice(
                patient_id=patient_id,
                appointment_id=appointment
