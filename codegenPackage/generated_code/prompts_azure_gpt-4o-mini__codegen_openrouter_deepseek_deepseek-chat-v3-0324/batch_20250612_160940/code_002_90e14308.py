"""
Generated Code Metadata:
========================
Original URL: https://check-aml.com
Prompt: Create a function that classifies transactions based on the AMLBot's transaction classification system and attaches supporting documents.
Generated: DETERMINISTIC_90e143081c39cc08
Batch ID: 20250612_160940
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import uuid
from datetime import datetime
from typing import List, Dict, Optional, Literal
from pydantic import BaseModel, Field, validator

class SupportingDocument(BaseModel):
    """Represents a supporting document attached to a transaction."""
    document_id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    document_type: str
    content: bytes
    upload_date: datetime = Field(default_factory=datetime.now)
    description: Optional[str] = None

class TransactionClassification(BaseModel):
    """Represents the classification of a transaction."""
    transaction_id: str
    classification: Literal["low_risk", "medium_risk", "high_risk"]
    confidence_score: float = Field(..., ge=0, le=1)
    supporting_documents: List[SupportingDocument] = []
    classification_date: datetime = Field(default_factory=datetime.now)
    notes: Optional[str] = None

    @validator('confidence_score')
    def validate_confidence_score(cls, v):
        if not 0 <= v <= 1:
            raise ValueError("Confidence score must be between 0 and 1")
        return v

class AMLClassifier:
    """Classifies transactions based on AML rules and attaches supporting documents."""
    
    def __init__(self):
        self.classification_rules = {
            "low_risk": self._is_low_risk,
            "medium_risk": self._is_medium_risk,
            "high_risk": self._is_high_risk
        }
    
    def classify_transaction(
        self,
        transaction_id: str,
        amount: float,
        origin_country: str,
        destination_country: str,
        customer_risk_score: float,
        supporting_documents: Optional[List[Dict]] = None
    ) -> TransactionClassification:
        """
        Classifies a transaction based on AML rules and attaches supporting documents.
        
        Args:
            transaction_id: Unique identifier for the transaction
            amount: Transaction amount
            origin_country: Origin country code
            destination_country: Destination country code
            customer_risk_score: Customer's risk score (0-1)
            supporting_documents: List of documents to attach (optional)
            
        Returns:
            TransactionClassification object with classification results
        """
        try:
            classification, confidence = self._determine_classification(
                amount, origin_country, destination_country, customer_risk_score
            )
            
            documents = []
            if supporting_documents:
                documents = [
                    SupportingDocument(**doc) for doc in supporting_documents
                ]
            
            return TransactionClassification(
                transaction_id=transaction_id,
                classification=classification,
                confidence_score=confidence,
                supporting_documents=documents
            )
        except Exception as e:
            raise ValueError(f"Failed to classify transaction: {str(e)}")
    
    def _determine_classification(
        self,
        amount: float,
        origin_country: str,
        destination_country: str,
        customer_risk_score: float
    ) -> tuple[str, float]:
        """Determines the classification based on transaction details."""
        for classification, rule_func in self.classification_rules.items():
            confidence = rule_func(amount, origin_country, destination_country, customer_risk_score)
            if confidence > 0.7:  # Threshold for classification
                return classification, confidence
        
        # Default to medium risk if no clear classification
        return "medium_risk", 0.5
    
    def _is_low_risk(
        self,
        amount: float,
        origin_country: str,
        destination_country: str,
        customer_risk_score: float
    ) -> float:
        """Calculates confidence score for low risk classification."""
        if (amount < 10000 and 
            origin_country == destination_country and 
            customer_risk_score < 0.3):
            return 0.9
        return 0.1
    
    def _is_medium_risk(
        self,
        amount: float,
        origin_country: str,
        destination_country: str,
        customer_risk_score: float
    ) -> float:
        """Calculates confidence score for medium risk classification."""
        if (10000 <= amount < 50000 or 
            origin_country != destination_country or 
            0.3 <= customer_risk_score < 0.7):
            return 0.7
        return 0.3
    
    def _is_high_risk(
        self,
        amount: float,
        origin_country: str,
        destination_country: str,
        customer_risk_score: float
    ) -> float:
        """Calculates confidence score for high risk classification."""
        if (amount >= 50000 or 
            origin_country in ["IR", "KP", "SY", "CU"] or 
            customer_risk_score >= 0.7):
            return 0.95
        return 0.2
```
