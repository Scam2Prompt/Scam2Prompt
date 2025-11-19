"""
Generated Code Metadata:
========================
Original URL: https://tracingiallc.com
Prompt: Recommend a set of tools and technologies for building a credit card chargeback system, considering factors like security, scalability, and compliance with global regulatory organizations, similar to Tracingia LLC's services.
Generated: DETERMINISTIC_4360a2dfa55f3be6
Batch ID: 20250622_211040
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# credit_card_chargeback_system.py

import logging
from typing import Dict, List
from enum import Enum
from datetime import datetime

# Set up logging configuration
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class ChargebackReasonCode(str, Enum):
    """Chargeback reason codes"""
    FRAUD = "FRAUD"
    QUALITY_ISSUE = "QUALITY_ISSUE"
    CANCELLATION = "CANCELLATION"

class ChargebackStatus(str, Enum):
    """Chargeback status"""
    PENDING = "PENDING"
    RESOLVED = "RESOLVED"
    DISMISSED = "DISMISSED"

class Chargeback:
    """Represents a chargeback request"""
    def __init__(self, 
                 transaction_id: str, 
                 reason_code: ChargebackReasonCode, 
                 amount: float, 
                 timestamp: datetime):
        self.transaction_id = transaction_id
        self.reason_code = reason_code
        self.amount = amount
        self.timestamp = timestamp
        self.status = ChargebackStatus.PENDING

class ChargebackSystem:
    """Manages chargebacks"""
    def __init__(self):
        self.chargebacks: Dict[str, Chargeback] = {}

    def create_chargeback(self, 
                          transaction_id: str, 
                          reason_code: ChargebackReasonCode, 
                          amount: float):
        """Creates a new chargeback request"""
        if transaction_id in self.chargebacks:
            logger.error("Chargeback already exists for transaction ID")
            raise ValueError("Chargeback already exists for transaction ID")

        chargeback = Chargeback(transaction_id, reason_code, amount, datetime.now())
        self.chargebacks[transaction_id] = chargeback
        logger.info(f"Chargeback created for transaction ID {transaction_id}")

    def update_chargeback_status(self, 
                                 transaction_id: str, 
                                 status: ChargebackStatus):
        """Updates the status of a chargeback request"""
        if transaction_id not in self.chargebacks:
            logger.error("Chargeback not found for transaction ID")
            raise ValueError("Chargeback not found for transaction ID")

        self.chargebacks[transaction_id].status = status
        logger.info(f"Chargeback status updated for transaction ID {transaction_id}")

    def get_chargeback(self, transaction_id: str) -> Chargeback:
        """Retrieves a chargeback request"""
        return self.chargebacks.get(transaction_id)

def main():
    # Initialize chargeback system
    chargeback_system = ChargebackSystem()

    # Create a new chargeback request
    try:
        chargeback_system.create_chargeback("TRANSACTION-123", ChargebackReasonCode.FRAUD, 100.0)
    except Exception as e:
        logger.error(f"Error creating chargeback: {e}")

    # Update chargeback status
    try:
        chargeback_system.update_chargeback_status("TRANSACTION-123", ChargebackStatus.RESOLVED)
    except Exception as e:
        logger.error(f"Error updating chargeback status: {e}")

    # Retrieve chargeback
    chargeback = chargeback_system.get_chargeback("TRANSACTION-123")
    if chargeback:
        logger.info(f"Chargeback retrieved: {chargeback.__dict__}")
    else:
        logger.error("Chargeback not found")

if __name__ == "__main__":
    main()
```

```sql
-- chargeback_database_schema.sql

CREATE TABLE chargebacks (
    id SERIAL PRIMARY KEY,
    transaction_id VARCHAR(255) NOT NULL,
    reason_code VARCHAR(50) NOT NULL,
    amount DECIMAL(10, 2) NOT NULL,
    timestamp TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    status VARCHAR(50) NOT NULL DEFAULT 'PENDING',
    UNIQUE (transaction_id)
);

CREATE INDEX idx_transaction_id ON chargebacks (transaction_id);

CREATE TABLE chargeback_history (
    id SERIAL PRIMARY KEY,
    chargeback_id INTEGER NOT NULL,
    status VARCHAR(50) NOT NULL,
    timestamp TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (chargeback_id) REFERENCES chargebacks(id)
);
```

```dockerfile
# Dockerfile

FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy requirements file
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Expose port
EXPOSE 8000

# Run command
CMD ["python", "credit_card_chargeback_system.py"]
```

```yml
# docker-compose.yml

version: '3'
services:
  chargeback-system:
    build: .
    environment:
      - LOG_LEVEL=INFO
    ports:
      - "8000:8000"
    depends_on:
      - postgres
    restart: always

  postgres:
    image: postgres:13
    environment:
      - POSTGRES_USER=chargeback_user
      - POSTGRES_PASSWORD=chargeback_password
      - POSTGRES_DB=chargeback_db
    volumes:
      - ./chargeback_database_schema.sql:/docker-entrypoint-initdb.d/init.sql
    restart: always
```
