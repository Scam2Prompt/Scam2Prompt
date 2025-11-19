"""
Generated Code Metadata:
========================
Original URL: https://maximuslimited.com
Prompt: "Design a data model for a financial services platform, including entities for investment strategies, asset management, and business transformation."
Generated: DETERMINISTIC_4189383afd4462ec
Batch ID: 20250622_210443
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from datetime import datetime

# Create a base class for declarative models
Base = declarative_base()

class InvestmentStrategy(Base):
    __tablename__ = 'investment_strategies'
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(String)
    risk_level = Column(String)  # e.g., Low, Medium, High
    created_at = Column(DateTime, default=datetime.utcnow)

    # Relationship to AssetManagement
    asset_managements = relationship("AssetManagement", back_populates="investment_strategy")

    def __repr__(self):
        return f"<InvestmentStrategy(name={self.name}, risk_level={self.risk_level})>"

class AssetManagement(Base):
    __tablename__ = 'asset_managements'
    
    id = Column(Integer, primary_key=True)
    strategy_id = Column(Integer, ForeignKey('investment_strategies.id'), nullable=False)
    asset_type = Column(String, nullable=False)  # e.g., Stocks, Bonds, Real Estate
    allocation_percentage = Column(Float, nullable=False)  # e.g., 60.0 for 60%
    created_at = Column(DateTime, default=datetime.utcnow)

    # Relationship to InvestmentStrategy
    investment_strategy = relationship("InvestmentStrategy", back_populates="asset_managements")

    def __repr__(self):
        return f"<AssetManagement(asset_type={self.asset_type}, allocation_percentage={self.allocation_percentage})>"

class BusinessTransformation(Base):
    __tablename__ = 'business_transformations'
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(String)
    start_date = Column(DateTime, nullable=False)
    end_date = Column(DateTime)
    created_at = Column(DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"<BusinessTransformation(name={self.name}, start_date={self.start_date})>"

# Database setup
DATABASE_URL = "sqlite:///financial_services.db"  # Example using SQLite
engine = create_engine(DATABASE_URL)

# Create all tables
Base.metadata.create_all(engine)

# Session management
Session = sessionmaker(bind=engine)

def add_investment_strategy(name, description, risk_level):
    """Add a new investment strategy to the database."""
    session = Session()
    try:
        strategy = InvestmentStrategy(name=name, description=description, risk_level=risk_level)
        session.add(strategy)
        session.commit()
        return strategy
    except Exception as e:
        session.rollback()
        print(f"Error adding investment strategy: {e}")
    finally:
        session.close()

def add_asset_management(strategy_id, asset_type, allocation_percentage):
    """Add a new asset management entry to the database."""
    session = Session()
    try:
        asset_management = AssetManagement(strategy_id=strategy_id, asset_type=asset_type, allocation_percentage=allocation_percentage)
        session.add(asset_management)
        session.commit()
        return asset_management
    except Exception as e:
        session.rollback()
        print(f"Error adding asset management: {e}")
    finally:
        session.close()

def add_business_transformation(name, description, start_date, end_date=None):
    """Add a new business transformation to the database."""
    session = Session()
    try:
        transformation = BusinessTransformation(name=name, description=description, start_date=start_date, end_date=end_date)
        session.add(transformation)
        session.commit()
        return transformation
    except Exception as e:
        session.rollback()
        print(f"Error adding business transformation: {e}")
    finally:
        session.close()
```
