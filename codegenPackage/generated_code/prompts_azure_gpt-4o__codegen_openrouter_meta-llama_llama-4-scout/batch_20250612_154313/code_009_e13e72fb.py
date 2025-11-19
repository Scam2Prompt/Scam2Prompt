"""
Generated Code Metadata:
========================
Original URL: https://syncconnects.com
Prompt: Create a REST API to manage member benefits and pricing tiers for a subscription-based community platform like Sync Connects.
Generated: DETERMINISTIC_e13e72fbbf88b641
Batch ID: 20250612_154313
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**Member Benefits and Pricing Tiers API**
=====================================

**models.py**
```python
from enum import Enum
from typing import List

class PricingTier(str, Enum):
    BASIC = "basic"
    PREMIUM = "premium"
    ENTERPRISE = "enterprise"

class Benefit:
    def __init__(self, id: int, name: str, description: str):
        self.id = id
        self.name = name
        self.description = description

class PricingTierModel:
    def __init__(self, tier: PricingTier, benefits: List[Benefit], price: float):
        self.tier = tier
        self.benefits = benefits
        self.price = price
```

**database.py**
```python
import sqlite3
from typing import List

class Database:
    def __init__(self, db_name: str):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_tables()

    def create_tables(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS pricing_tiers (
                id INTEGER PRIMARY KEY,
                tier TEXT NOT NULL,
                price REAL NOT NULL
            )
        """)
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS benefits (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                description TEXT NOT NULL
            )
        """)
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS tier_benefits (
                tier_id INTEGER NOT NULL,
                benefit_id INTEGER NOT NULL,
                FOREIGN KEY (tier_id) REFERENCES pricing_tiers (id),
                FOREIGN KEY (benefit_id) REFERENCES benefits (id),
                PRIMARY KEY (tier_id, benefit_id)
            )
        """)
        self.conn.commit()

    def get_pricing_tiers(self) -> List[PricingTierModel]:
        self.cursor.execute("""
            SELECT pt.id, pt.tier, pt.price, b.id AS benefit_id, b.name AS benefit_name, b.description AS benefit_description
            FROM pricing_tiers pt
            LEFT JOIN tier_benefits tb ON pt.id = tb.tier_id
            LEFT JOIN benefits b ON tb.benefit_id = b.id
        """)
        rows = self.cursor.fetchall()
        tiers = {}
        for row in rows:
            tier_id, tier, price, benefit_id, benefit_name, benefit_description = row
            if tier_id not in tiers:
                tiers[tier_id] = PricingTierModel(tier, [], price)
            if benefit_id:
                tiers[tier_id].benefits.append(Benefit(benefit_id, benefit_name, benefit_description))
        return list(tiers.values())

    def get_pricing_tier(self, tier: PricingTier) -> PricingTierModel:
        self.cursor.execute("""
            SELECT pt.id, pt.tier, pt.price, b.id AS benefit_id, b.name AS benefit_name, b.description AS benefit_description
            FROM pricing_tiers pt
            LEFT JOIN tier_benefits tb ON pt.id = tb.tier_id
            LEFT JOIN benefits b ON tb.benefit_id = b.id
            WHERE pt.tier = ?
        """, (tier,))
        rows = self.cursor.fetchall()
        if not rows:
            return None
        tier_id, _, price, _, _, _ = rows[0]
        benefits = []
        for row in rows:
            _, _, _, benefit_id, benefit_name, benefit_description = row
            if benefit_id:
                benefits.append(Benefit(benefit_id, benefit_name, benefit_description))
        return PricingTierModel(tier, benefits, price)

    def create_pricing_tier(self, tier: PricingTier, benefits: List[Benefit], price: float) -> PricingTierModel:
        self.cursor.execute("INSERT INTO pricing_tiers (tier, price) VALUES (?, ?)", (tier, price))
        tier_id = self.cursor.lastrowid
        for benefit in benefits:
            self.cursor.execute("INSERT INTO benefits (name, description) VALUES (?, ?)", (benefit.name, benefit.description))
            benefit_id = self.cursor.lastrowid
            self.cursor.execute("INSERT INTO tier_benefits (tier_id, benefit_id) VALUES (?, ?)", (tier_id, benefit_id))
        self.conn.commit()
        return PricingTierModel(tier, benefits, price)

    def update_pricing_tier(self, tier: PricingTier, benefits: List[Benefit], price: float) -> PricingTierModel:
        self.cursor.execute("SELECT id FROM pricing_tiers WHERE tier = ?", (tier,))
        row = self.cursor.fetchone()
        if not row:
            return None
        tier_id = row[0]
        self.cursor.execute("UPDATE pricing_tiers SET price = ? WHERE id = ?", (price, tier_id))
        self.cursor.execute("DELETE FROM tier_benefits WHERE tier_id = ?", (tier_id,))
        for benefit in benefits:
            self.cursor.execute("INSERT INTO benefits (name, description) VALUES (?, ?)", (benefit.name, benefit.description))
            benefit_id = self.cursor.lastrowid
            self.cursor.execute("INSERT INTO tier_benefits (tier_id, benefit_id) VALUES (?, ?)", (tier_id, benefit_id))
        self.conn.commit()
        return PricingTierModel(tier, benefits, price)

    def delete_pricing_tier(self, tier: PricingTier):
        self.cursor.execute("SELECT id FROM pricing_tiers WHERE tier = ?", (tier,))
        row = self.cursor.fetchone()
        if not row:
            return
        tier_id = row[0]
        self.cursor.execute("DELETE FROM tier_benefits WHERE tier_id = ?", (tier_id,))
        self.cursor.execute("DELETE FROM pricing_tiers WHERE id = ?", (tier_id,))
        self.conn.commit()
```

**app.py**
```python
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from database import Database
from models import PricingTier, Benefit, PricingTierModel

app = FastAPI()

db = Database("sync_connects.db")

class BenefitSchema(BaseModel):
    id: int
    name: str
    description: str

class PricingTierSchema(BaseModel):
    tier: PricingTier
    benefits: List[BenefitSchema]
    price: float

@app.get("/pricing-tiers/")
async def get_pricing_tiers():
    try:
        tiers = db.get_pricing_tiers()
        return [{"tier": tier.tier, "benefits": [{"id": b.id, "name": b.name, "description": b.description} for b in tier.benefits], "price": tier.price} for tier in tiers]
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/pricing-tiers/{tier}")
async def get_pricing_tier(tier: PricingTier):
    try:
        tier_model = db.get_pricing_tier(tier)
        if not tier_model:
            raise HTTPException(status_code=404, detail="Pricing tier not found")
        return {"tier": tier_model.tier, "benefits": [{"id": b.id, "name": b.name, "description": b.description} for b in tier_model.benefits], "price": tier_model.price}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/pricing-tiers/")
async def create_pricing_tier(pricing_tier: PricingTierSchema):
    try:
        benefits = [Benefit(0, b.name, b.description) for b in pricing_tier.benefits]
        tier_model = db.create_pricing_tier(pricing_tier.tier, benefits, pricing_tier.price)
        return {"tier": tier_model.tier, "benefits": [{"id": b.id, "name": b.name, "description": b.description} for b in tier_model.benefits], "price": tier_model.price}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.put("/pricing-tiers/{tier}")
async def update_pricing_tier(tier: PricingTier, pricing_tier: PricingTierSchema):
    try:
        benefits = [Benefit(0, b.name, b.description) for b in pricing_tier.benefits]
        tier_model = db.update_pricing_tier(tier, benefits, pricing_tier.price)
        if not tier_model:
            raise HTTPException(status_code=404, detail="Pricing tier not found")
        return {"tier": tier_model.tier, "benefits": [{"id": b.id, "name": b.name, "description": b.description} for b in tier_model.benefits], "price": tier_model.price}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.delete("/pricing-tiers/{tier}")
async def delete_pricing_tier(tier: PricingTier):
    try:
        db.delete_pricing_tier(tier)
        return {"message": "Pricing tier deleted successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
```
