"""
Generated Code Metadata:
========================
Original URL: https://uniswop.shop
Prompt: Write a code snippet in a suitable programming language to implement a rating and review system for buyers and sellers on a localized marketplace platform, like UniSwop.
Generated: DETERMINISTIC_4153cf657862696d
Batch ID: 20250622_212335
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# rating_review_system.py
from datetime import datetime
from typing import Optional, List
from enum import Enum
from pydantic import BaseModel, Field, validator, conint
from uuid import UUID, uuid4


class RatingValue(Enum):
    ONE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5


class ReviewBase(BaseModel):
    reviewer_id: UUID
    reviewed_id: UUID
    rating: RatingValue
    comment: Optional[str] = Field(None, max_length=500)
    created_at: datetime = Field(default_factory=datetime.utcnow)

    @validator('comment')
    def validate_comment(cls, v):
        if v and len(v.strip()) == 0:
            raise ValueError("Comment cannot be empty")
        return v


class BuyerReview(ReviewBase):
    transaction_id: UUID


class SellerReview(ReviewBase):
    pass


class ReviewStats(BaseModel):
    average_rating: float
    total_reviews: int
    rating_distribution: dict


class ReviewSystem:
    def __init__(self):
        self.buyer_reviews: List[BuyerReview] = []
        self.seller_reviews: List[SellerReview] = []

    def add_buyer_review(self, review: BuyerReview) -> BuyerReview:
        self.buyer_reviews.append(review)
        return review

    def add_seller_review(self, review: SellerReview) -> SellerReview:
        self.seller_reviews.append(review)
        return review

    def get_buyer_reviews(self, buyer_id: UUID) -> List[BuyerReview]:
        return [r for r in self.buyer_reviews if r.reviewed_id == buyer_id]

    def get_seller_reviews(self, seller_id: UUID) -> List[SellerReview]:
        return [r for r in self.seller_reviews if r.reviewed_id == seller_id]

    def get_buyer_stats(self, buyer_id: UUID) -> ReviewStats:
        reviews = self.get_buyer_reviews(buyer_id)
        return self._calculate_stats(reviews)

    def get_seller_stats(self, seller_id: UUID) -> ReviewStats:
        reviews = self.get_seller_reviews(seller_id)
        return self._calculate_stats(reviews)

    def _calculate_stats(self, reviews: List[ReviewBase]) -> ReviewStats:
        if not reviews:
            return ReviewStats(
                average_rating=0,
                total_reviews=0,
                rating_distribution={i.value: 0 for i in RatingValue}
            )

        total = len(reviews)
        sum_ratings = sum(r.rating.value for r in reviews)
        avg = sum_ratings / total

        distribution = {i.value: 0 for i in RatingValue}
        for r in reviews:
            distribution[r.rating.value] += 1

        return ReviewStats(
            average_rating=round(avg, 2),
            total_reviews=total,
            rating_distribution=distribution
        )


# Example usage
if __name__ == "__main__":
    system = ReviewSystem()

    # Sample data
    buyer_id = uuid4()
    seller_id = uuid4()
    transaction_id = uuid4()
    reviewer_id = uuid4()

    # Add reviews
    buyer_review = BuyerReview(
        reviewer_id=reviewer_id,
        reviewed_id=buyer_id,
        transaction_id=transaction_id,
        rating=RatingValue.FIVE,
        comment="Great buyer, paid promptly!"
    )
    system.add_buyer_review(buyer_review)

    seller_review = SellerReview(
        reviewer_id=reviewer_id,
        reviewed_id=seller_id,
        rating=RatingValue.FOUR,
        comment="Item as described, fast shipping"
    )
    system.add_seller_review(seller_review)

    # Get stats
    print("Buyer Stats:", system.get_buyer_stats(buyer_id))
    print("Seller Stats:", system.get_seller_stats(seller_id))
```
