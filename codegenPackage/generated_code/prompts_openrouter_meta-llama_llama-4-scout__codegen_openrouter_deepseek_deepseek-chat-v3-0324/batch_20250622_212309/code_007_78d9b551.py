"""
Generated Code Metadata:
========================
Original URL: https://tsfonts.com
Prompt: "Write a script to automate font licensing and subscription management for a type design studio like TS Fonts."
Generated: DETERMINISTIC_78d9b5512285a887
Batch ID: 20250622_212309
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Font Licensing and Subscription Management System for TS Fonts

This script automates font licensing and subscription management for a type design studio.
It handles license generation, subscription tracking, and customer management.
"""

import json
import datetime
from typing import Dict, List, Optional
import hashlib
import os
from enum import Enum, auto

# Constants
LICENSE_TEMPLATE = """
TS Fonts License Agreement
-------------------------
License ID: {license_id}
Customer: {customer_name}
Email: {customer_email}
Font Family: {font_family}
License Type: {license_type}
Issue Date: {issue_date}
Expiry Date: {expiry_date}
Allowed Uses: {allowed_uses}
Terms: {terms}
"""

class LicenseType(Enum):
    PERSONAL = auto()
    COMMERCIAL = auto()
    ENTERPRISE = auto()
    SUBSCRIPTION = auto()

class SubscriptionStatus(Enum):
    ACTIVE = auto()
    EXPIRED = auto()
    CANCELLED = auto()
    PENDING = auto()

class FontLicense:
    def __init__(self, customer_name: str, customer_email: str, font_family: str, 
                 license_type: LicenseType, duration_days: int = 365, 
                 allowed_uses: str = "Desktop, Web, App", terms: str = "Standard"):
        self.license_id = self._generate_license_id(customer_email, font_family)
        self.customer_name = customer_name
        self.customer_email = customer_email
        self.font_family = font_family
        self.license_type = license_type
        self.issue_date = datetime.date.today()
        self.expiry_date = self.issue_date + datetime.timedelta(days=duration_days)
        self.allowed_uses = allowed_uses
        self.terms = terms

    def _generate_license_id(self, email: str, font_family: str) -> str:
        """Generate a unique license ID using customer email and font family."""
        raw_id = f"{email}{font_family}{datetime.datetime.now().timestamp()}"
        return hashlib.sha256(raw_id.encode()).hexdigest()[:16].upper()

    def generate_license_text(self) -> str:
        """Generate the license agreement text."""
        return LICENSE_TEMPLATE.format(
            license_id=self.license_id,
            customer_name=self.customer_name,
            customer_email=self.customer_email,
            font_family=self.font_family,
            license_type=self.license_type.name,
            issue_date=self.issue_date.strftime("%Y-%m-%d"),
            expiry_date=self.expiry_date.strftime("%Y-%m-%d"),
            allowed_uses=self.allowed_uses,
            terms=self.terms
        )

    def to_dict(self) -> Dict:
        """Convert license to dictionary for serialization."""
        return {
            "license_id": self.license_id,
            "customer_name": self.customer_name,
            "customer_email": self.customer_email,
            "font_family": self.font_family,
            "license_type": self.license_type.name,
            "issue_date": self.issue_date.strftime("%Y-%m-%d"),
            "expiry_date": self.expiry_date.strftime("%Y-%m-%d"),
            "allowed_uses": self.allowed_uses,
            "terms": self.terms
        }

class Subscription:
    def __init__(self, customer_email: str, font_families: List[str], 
                 tier: str = "basic", duration_months: int = 12):
        self.subscription_id = self._generate_subscription_id(customer_email)
        self.customer_email = customer_email
        self.font_families = font_families
        self.tier = tier
        self.start_date = datetime.date.today()
        self.end_date = self.start_date + datetime.timedelta(days=30*duration_months)
        self.status = SubscriptionStatus.ACTIVE
        self.last_payment_date = None
        self.next_payment_date = self.start_date + datetime.timedelta(days=30)

    def _generate_subscription_id(self, email: str) -> str:
        """Generate a unique subscription ID."""
        raw_id = f"{email}{datetime.datetime.now().timestamp()}"
        return hashlib.sha256(raw_id.encode()).hexdigest()[:12].upper()

    def renew(self, months: int = 12) -> None:
        """Renew the subscription for specified months."""
        self.end_date += datetime.timedelta(days=30*months)
        self.next_payment_date = self.end_date
        self.status = SubscriptionStatus.ACTIVE

    def cancel(self) -> None:
        """Cancel the subscription."""
        self.status = SubscriptionStatus.CANCELLED

    def is_active(self) -> bool:
        """Check if subscription is currently active."""
        today = datetime.date.today()
        return self.status == SubscriptionStatus.ACTIVE and today <= self.end_date

    def to_dict(self) -> Dict:
        """Convert subscription to dictionary for serialization."""
        return {
            "subscription_id": self.subscription_id,
            "customer_email": self.customer_email,
            "font_families": self.font_families,
            "tier": self.tier,
            "start_date": self.start_date.strftime("%Y-%m-%d"),
            "end_date": self.end_date.strftime("%Y-%m-%d"),
            "status": self.status.name,
            "last_payment_date": self.last_payment_date.strftime("%Y-%m-%d") if self.last_payment_date else None,
            "next_payment_date": self.next_payment_date.strftime("%Y-%m-%d") if self.next_payment_date else None
        }

class FontLicenseManager:
    def __init__(self, storage_dir: str = "data"):
        self.storage_dir = storage_dir
        self.licenses_file = os.path.join(storage_dir, "licenses.json")
        self.subscriptions_file = os.path.join(storage_dir, "subscriptions.json")
        self._ensure_storage()

    def _ensure_storage(self) -> None:
        """Ensure storage directory and files exist."""
        os.makedirs(self.storage_dir, exist_ok=True)
        if not os.path.exists(self.licenses_file):
            with open(self.licenses_file, "w") as f:
                json.dump([], f)
        if not os.path.exists(self.subscriptions_file):
            with open(self.subscriptions_file, "w") as f:
                json.dump([], f)

    def _load_licenses(self) -> List[Dict]:
        """Load all licenses from storage."""
        with open(self.licenses_file, "r") as f:
            return json.load(f)

    def _save_licenses(self, licenses: List[Dict]) -> None:
        """Save licenses to storage."""
        with open(self.licenses_file, "w") as f:
            json.dump(licenses, f, indent=2)

    def _load_subscriptions(self) -> List[Dict]:
        """Load all subscriptions from storage."""
        with open(self.subscriptions_file, "r") as f:
            return json.load(f)

    def _save_subscriptions(self, subscriptions: List[Dict]) -> None:
        """Save subscriptions to storage."""
        with open(self.subscriptions_file, "w") as f:
            json.dump(subscriptions, f, indent=2)

    def issue_license(self, customer_name: str, customer_email: str, font_family: str, 
                     license_type: LicenseType, duration_days: int = 365, 
                     allowed_uses: str = "Desktop, Web, App", terms: str = "Standard") -> FontLicense:
        """Issue a new font license."""
        license_obj = FontLicense(
            customer_name=customer_name,
            customer_email=customer_email,
            font_family=font_family,
            license_type=license_type,
            duration_days=duration_days,
            allowed_uses=allowed_uses,
            terms=terms
        )
        
        licenses = self._load_licenses()
        licenses.append(license_obj.to_dict())
        self._save_licenses(licenses)
        
        return license_obj

    def create_subscription(self, customer_email: str, font_families: List[str], 
                           tier: str = "basic", duration_months: int = 12) -> Subscription:
        """Create a new font subscription."""
        subscription = Subscription(
            customer_email=customer_email,
            font_families=font_families,
            tier=tier,
            duration_months=duration_months
        )
        
        subscriptions = self._load_subscriptions()
        subscriptions.append(subscription.to_dict())
        self._save_subscriptions(subscriptions)
        
        return subscription

    def get_customer_licenses(self, customer_email: str) -> List[Dict]:
        """Get all licenses for a customer."""
        licenses = self._load_licenses()
        return [license for license in licenses if license["customer_email"] == customer_email]

    def get_customer_subscriptions(self, customer_email: str) -> List[Dict]:
        """Get all subscriptions for a customer."""
        subscriptions = self._load_subscriptions()
        return [sub for sub in subscriptions if sub
