"""
Generated Code Metadata:
========================
Original URL: https://hellohosting.pages.dev
Prompt: Design a data model to track the performance milestones and contest rules for the Wealth Coin (WEL) incentive plan, including fields for market capitalization targets, estimated price/share, and total coins in each wallet.
Generated: DETERMINISTIC_3efde5e690171808
Batch ID: 20250622_204621
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from datetime import datetime

# Create a base class for declarative models
Base = declarative_base()

class Wallet(Base):
    """Model to represent a user's wallet in the Wealth Coin incentive plan."""
    __tablename__ = 'wallets'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, nullable=False)
    total_coins = Column(Float, nullable=False, default=0.0)

    # Relationship to track performance milestones
    milestones = relationship("PerformanceMilestone", back_populates="wallet")

    def __repr__(self):
        return f"<Wallet(user_id={self.user_id}, total_coins={self.total_coins})>"

class PerformanceMilestone(Base):
    """Model to represent performance milestones for the Wealth Coin incentive plan."""
    __tablename__ = 'performance_milestones'

    id = Column(Integer, primary_key=True)
    wallet_id = Column(Integer, ForeignKey('wallets.id'), nullable=False)
    market_cap_target = Column(Float, nullable=False)
    estimated_price_per_share = Column(Float, nullable=False)
    achieved_at = Column(DateTime, default=datetime.utcnow)

    # Relationship to link back to the wallet
    wallet = relationship("Wallet", back_populates="milestones")

    def __repr__(self):
        return (f"<PerformanceMilestone(wallet_id={self.wallet_id}, "
                f"market_cap_target={self.market_cap_target}, "
                f"estimated_price_per_share={self.estimated_price_per_share}, "
                f"achieved_at={self.achieved_at})>")

# Database setup
DATABASE_URL = "sqlite:///wealth_coin.db"  # Change to your database URL
engine = create_engine(DATABASE_URL)

# Create all tables in the database
try:
    Base.metadata.create_all(engine)
except Exception as e:
    print(f"Error creating database tables: {e}")

# Session management
Session = sessionmaker(bind=engine)

def add_wallet(user_id, total_coins):
    """Add a new wallet to the database."""
    session = Session()
    try:
        new_wallet = Wallet(user_id=user_id, total_coins=total_coins)
        session.add(new_wallet)
        session.commit()
        return new_wallet
    except Exception as e:
        session.rollback()
        print(f"Error adding wallet: {e}")
    finally:
        session.close()

def add_performance_milestone(wallet_id, market_cap_target, estimated_price_per_share):
    """Add a new performance milestone for a specific wallet."""
    session = Session()
    try:
        new_milestone = PerformanceMilestone(
            wallet_id=wallet_id,
            market_cap_target=market_cap_target,
            estimated_price_per_share=estimated_price_per_share
        )
        session.add(new_milestone)
        session.commit()
        return new_milestone
    except Exception as e:
        session.rollback()
        print(f"Error adding performance milestone: {e}")
    finally:
        session.close()
```
