"""
Generated Code Metadata:
========================
Original URL: https://segrepin.com
Prompt: Design a data model for a company's operations in the Democratic Republic of Congo, including entities for customers, projects, and financial transactions.
Generated: DETERMINISTIC_f6ed953306c2f1ef
Batch ID: 20250622_210216
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from datetime import datetime
from typing import Optional, List
from pydantic import BaseModel, Field, EmailStr, validator
from enum import Enum

class CustomerType(str, Enum):
    INDIVIDUAL = "individual"
    BUSINESS = "business"
    GOVERNMENT = "government"
    NGO = "ngo"

class ProjectStatus(str, Enum):
    PLANNING = "planning"
    ACTIVE = "active"
    ON_HOLD = "on_hold"
    COMPLETED = "completed"
    CANCELLED = "cancelled"

class TransactionType(str, Enum):
    INVOICE = "invoice"
    PAYMENT = "payment"
    REFUND = "refund"
    EXPENSE = "expense"

class Currency(str, Enum):
    CDF = "CDF"
    USD = "USD"
    EUR = "EUR"

class Address(BaseModel):
    street: str = Field(..., max_length=100)
    city: str = Field(..., max_length=50)
    province: str = Field(..., max_length=50)
    postal_code: str = Field(..., max_length=20)
    country: str = Field(default="Democratic Republic of Congo", max_length=50)

class Customer(BaseModel):
    id: str = Field(..., min_length=1, description="Unique customer identifier")
    name: str = Field(..., max_length=100)
    type: CustomerType
    email: Optional[EmailStr] = None
    phone: str = Field(..., min_length=9, max_length=20)
    address: Address
    tax_id: Optional[str] = Field(None, max_length=50, description="Tax identification number")
    registration_date: datetime = Field(default_factory=datetime.now)
    is_active: bool = Field(default=True)

    @validator('phone')
    def validate_phone(cls, v):
        if not v.startswith('+'):
            raise ValueError("Phone number must start with country code (e.g., +243)")
        return v

class Project(BaseModel):
    id: str = Field(..., min_length=1, description="Unique project identifier")
    customer_id: str = Field(..., min_length=1)
    name: str = Field(..., max_length=100)
    description: Optional[str] = Field(None, max_length=500)
    start_date: datetime
    end_date: Optional[datetime] = None
    status: ProjectStatus = Field(default=ProjectStatus.PLANNING)
    budget: float = Field(..., gt=0)
    currency: Currency = Field(default=Currency.USD)
    manager: str = Field(..., max_length=100)
    created_at: datetime = Field(default_factory=datetime.now)

    @validator('end_date')
    def validate_dates(cls, v, values):
        if v and 'start_date' in values and v < values['start_date']:
            raise ValueError("End date must be after start date")
        return v

class FinancialTransaction(BaseModel):
    id: str = Field(..., min_length=1, description="Unique transaction identifier")
    project_id: str = Field(..., min_length=1)
    type: TransactionType
    amount: float = Field(..., gt=0)
    currency: Currency = Field(default=Currency.USD)
    date: datetime = Field(default_factory=datetime.now)
    description: Optional[str] = Field(None, max_length=200)
    reference: Optional[str] = Field(None, max_length=50)
    recorded_by: str = Field(..., max_length=100)
    approved: bool = Field(default=False)

class CompanyOperations(BaseModel):
    customers: List[Customer] = Field(default_factory=list)
    projects: List[Project] = Field(default_factory=list)
    transactions: List[FinancialTransaction] = Field(default_factory=list)

    def add_customer(self, customer: Customer):
        if any(c.id == customer.id for c in self.customers):
            raise ValueError("Customer with this ID already exists")
        self.customers.append(customer)

    def add_project(self, project: Project):
        if any(p.id == project.id for p in self.projects):
            raise ValueError("Project with this ID already exists")
        if not any(c.id == project.customer_id for c in self.customers):
            raise ValueError("Customer does not exist")
        self.projects.append(project)

    def add_transaction(self, transaction: FinancialTransaction):
        if any(t.id == transaction.id for t in self.transactions):
            raise ValueError("Transaction with this ID already exists")
        if not any(p.id == transaction.project_id for p in self.projects):
            raise ValueError("Project does not exist")
        self.transactions.append(transaction)
```
