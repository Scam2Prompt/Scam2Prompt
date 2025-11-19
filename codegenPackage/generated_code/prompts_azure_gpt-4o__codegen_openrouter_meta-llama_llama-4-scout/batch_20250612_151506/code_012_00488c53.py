"""
Generated Code Metadata:
========================
Original URL: https://metlifeinvests.com
Prompt: Suggest a database schema to manage investment plans, user accounts, and referral commissions for a platform like MET LIFE INVESTS.
Generated: DETERMINISTIC_00488c5324e14645
Batch ID: 20250612_151506
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- schema.sql

-- Create database
CREATE DATABASE IF NOT EXISTS met_life_invests;

-- Use database
USE met_life_invests;

-- Create table for users
CREATE TABLE IF NOT EXISTS users (
  id INT AUTO_INCREMENT,
  email VARCHAR(255) NOT NULL UNIQUE,
  password_hash VARCHAR(255) NOT NULL,
  name VARCHAR(255) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create table for investment plans
CREATE TABLE IF NOT EXISTS investment_plans (
  id INT AUTO_INCREMENT,
  plan_name VARCHAR(255) NOT NULL,
  plan_description TEXT,
  min_investment DECIMAL(10, 2) NOT NULL,
  max_investment DECIMAL(10, 2) NOT NULL,
  interest_rate DECIMAL(5, 2) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create table for user accounts
CREATE TABLE IF NOT EXISTS user_accounts (
  id INT AUTO_INCREMENT,
  user_id INT NOT NULL,
  account_balance DECIMAL(10, 2) NOT NULL DEFAULT 0.00,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);

-- Create table for investments
CREATE TABLE IF NOT EXISTS investments (
  id INT AUTO_INCREMENT,
  user_id INT NOT NULL,
  investment_plan_id INT NOT NULL,
  investment_amount DECIMAL(10, 2) NOT NULL,
  investment_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
  FOREIGN KEY (investment_plan_id) REFERENCES investment_plans(id) ON DELETE CASCADE
);

-- Create table for referrals
CREATE TABLE IF NOT EXISTS referrals (
  id INT AUTO_INCREMENT,
  referrer_user_id INT NOT NULL,
  referred_user_id INT NOT NULL,
  referral_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (referrer_user_id) REFERENCES users(id) ON DELETE CASCADE,
  FOREIGN KEY (referred_user_id) REFERENCES users(id) ON DELETE CASCADE,
  UNIQUE KEY (referrer_user_id, referred_user_id)
);

-- Create table for referral commissions
CREATE TABLE IF NOT EXISTS referral_commissions (
  id INT AUTO_INCREMENT,
  referral_id INT NOT NULL,
  commission_amount DECIMAL(10, 2) NOT NULL,
  commission_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (referral_id) REFERENCES referrals(id) ON DELETE CASCADE
);

-- Create table for transactions
CREATE TABLE IF NOT EXISTS transactions (
  id INT AUTO_INCREMENT,
  user_id INT NOT NULL,
  transaction_type ENUM('deposit', 'withdrawal', 'investment') NOT NULL,
  transaction_amount DECIMAL(10, 2) NOT NULL,
  transaction_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);
```

```python
# models.py

from sqlalchemy import create_engine, Column, Integer, String, Decimal, DateTime, ForeignKey, Enum
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

engine = create_engine('mysql+pymysql://user:password@localhost/met_life_invests')
Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    email = Column(String(255), unique=True, nullable=False)
    password_hash = Column(String(255), nullable=False)
    name = Column(String(255), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    accounts = relationship('UserAccount', backref='user')

class InvestmentPlan(Base):
    __tablename__ = 'investment_plans'
    id = Column(Integer, primary_key=True)
    plan_name = Column(String(255), nullable=False)
    plan_description = Column(String(255))
    min_investment = Column(Decimal(10, 2), nullable=False)
    max_investment = Column(Decimal(10, 2), nullable=False)
    interest_rate = Column(Decimal(5, 2), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    investments = relationship('Investment', backref='plan')

class UserAccount(Base):
    __tablename__ = 'user_accounts'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    account_balance = Column(Decimal(10, 2), nullable=False, default=0.00)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

class Investment(Base):
    __tablename__ = 'investments'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    investment_plan_id = Column(Integer, ForeignKey('investment_plans.id'), nullable=False)
    investment_amount = Column(Decimal(10, 2), nullable=False)
    investment_date = Column(DateTime, default=datetime.utcnow)

class Referral(Base):
    __tablename__ = 'referrals'
    id = Column(Integer, primary_key=True)
    referrer_user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    referred_user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    referral_date = Column(DateTime, default=datetime.utcnow)

class ReferralCommission(Base):
    __tablename__ = 'referral_commissions'
    id = Column(Integer, primary_key=True)
    referral_id = Column(Integer, ForeignKey('referrals.id'), nullable=False)
    commission_amount = Column(Decimal(10, 2), nullable=False)
    commission_date = Column(DateTime, default=datetime.utcnow)

class Transaction(Base):
    __tablename__ = 'transactions'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    transaction_type = Column(Enum('deposit', 'withdrawal', 'investment'), nullable=False)
    transaction_amount = Column(Decimal(10, 2), nullable=False)
    transaction_date = Column(DateTime, default=datetime.utcnow)

Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()
```
