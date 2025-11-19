"""
Generated Code Metadata:
========================
Original URL: https://poweredproductions.com.au
Prompt: Design a data model for storing frequently asked questions and answers about armourer services, uniform hire, and prop rentals for a film production company website.
Generated: DETERMINISTIC_74969e99ee8cd624
Batch ID: 20250622_204920
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# models.py

from typing import Optional
from pydantic import BaseModel, validator
from datetime import datetime

class FAQ(BaseModel):
    """Frequently Asked Question model"""
    id: Optional[int] = None
    question: str
    answer: str
    category: str  # armourer services, uniform hire, prop rentals
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    @validator('category')
    def category_must_be_valid(cls, v):
        valid_categories = ['armourer services', 'uniform hire', 'prop rentals']
        if v not in valid_categories:
            raise ValueError('Invalid category')
        return v

class FAQDB:
    """In-memory FAQ database"""
    def __init__(self):
        self.faqs = []

    def get_faqs(self, category: Optional[str] = None) -> list[FAQ]:
        """Retrieve all FAQs or by category"""
        if category:
            return [faq for faq in self.faqs if faq.category == category]
        return self.faqs

    def get_faq(self, id: int) -> Optional[FAQ]:
        """Retrieve FAQ by ID"""
        for faq in self.faqs:
            if faq.id == id:
                return faq
        return None

    def create_faq(self, faq: FAQ) -> FAQ:
        """Create a new FAQ"""
        faq.id = len(self.faqs) + 1
        faq.created_at = datetime.now()
        faq.updated_at = datetime.now()
        self.faqs.append(faq)
        return faq

    def update_faq(self, id: int, faq: FAQ) -> Optional[FAQ]:
        """Update an existing FAQ"""
        existing_faq = self.get_faq(id)
        if existing_faq:
            existing_faq.question = faq.question
            existing_faq.answer = faq.answer
            existing_faq.category = faq.category
            existing_faq.updated_at = datetime.now()
            return existing_faq
        return None

    def delete_faq(self, id: int) -> bool:
        """Delete an FAQ by ID"""
        for faq in self.faqs:
            if faq.id == id:
                self.faqs.remove(faq)
                return True
        return False


# Example usage
if __name__ == "__main__":
    db = FAQDB()

    faq1 = FAQ(question="What is armourer services?", answer="Armourer services provide...")
    faq2 = FAQ(question="Can I hire uniforms?", answer="Yes, we offer uniform hire services...")
    faq3 = FAQ(question="What types of props do you rent?", answer="We rent a variety of props...")

    db.create_faq(faq1)
    db.create_faq(faq2)
    db.create_faq(faq3)

    print("All FAQs:")
    for faq in db.get_faqs():
        print(faq)

    print("\nFAQs by category:")
    for faq in db.get_faqs(category="armourer services"):
        print(faq)

    updated_faq = FAQ(question="Updated question", answer="Updated answer", category="armourer services")
    db.update_faq(1, updated_faq)

    print("\nUpdated FAQ:")
    print(db.get_faq(1))

    db.delete_faq(2)

    print("\nFAQs after deletion:")
    for faq in db.get_faqs():
        print(faq)
```
