"""
Generated Code Metadata:
========================
Original URL: https://memekombat-chain.pages.dev
Prompt: Design a system to manage meme battles and rewards on the Meme Kombat platform, including a database schema and API endpoints.
Generated: DETERMINISTIC_beefc815c9a44ffc
Batch ID: 20250622_205751
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**Meme Kombat Platform API**
==========================

**Database Schema**
------------------

```sql
CREATE TABLE Users (
  id SERIAL PRIMARY KEY,
  username VARCHAR(255) NOT NULL UNIQUE,
  email VARCHAR(255) NOT NULL UNIQUE,
  password VARCHAR(255) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE Memes (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255) NOT NULL,
  image_url VARCHAR(255) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE Battles (
  id SERIAL PRIMARY KEY,
  meme1_id INTEGER NOT NULL,
  meme2_id INTEGER NOT NULL,
  winner_id INTEGER,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY (meme1_id) REFERENCES Memes(id),
  FOREIGN KEY (meme2_id) REFERENCES Memes(id),
  FOREIGN KEY (winner_id) REFERENCES Memes(id)
);

CREATE TABLE Rewards (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255) NOT NULL,
  description TEXT NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE User_Rewards (
  user_id INTEGER NOT NULL,
  reward_id INTEGER NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (user_id, reward_id),
  FOREIGN KEY (user_id) REFERENCES Users(id),
  FOREIGN KEY (reward_id) REFERENCES Rewards(id)
);

CREATE TABLE User_Battles (
  user_id INTEGER NOT NULL,
  battle_id INTEGER NOT NULL,
  vote INTEGER NOT NULL CHECK (vote IN (1, 2)),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (user_id, battle_id),
  FOREIGN KEY (user_id) REFERENCES Users(id),
  FOREIGN KEY (battle_id) REFERENCES Battles(id)
);
```

**API Endpoints**
----------------

### User Endpoints

```python
from fastapi import FastAPI, HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from typing import Optional

app = FastAPI()

# Database Connection
SQLALCHEMY_DATABASE_URL = "postgresql://user:password@host:port/dbname"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# User Model
class User(Base):
    __tablename__ = "Users"
    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True)
    email = Column(String, unique=True)
    password = Column(String)

# Reward Model
class Reward(Base):
    __tablename__ = "Rewards"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)

# Battle Model
class Battle(Base):
    __tablename__ = "Battles"
    id = Column(Integer, primary_key=True)
    meme1_id = Column(Integer)
    meme2_id = Column(Integer)
    winner_id = Column(Integer)

# Meme Model
class Meme(Base):
    __tablename__ = "Memes"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    image_url = Column(String)

# User Reward Model
class UserReward(Base):
    __tablename__ = "User_Rewards"
    user_id = Column(Integer, primary_key=True)
    reward_id = Column(Integer, primary_key=True)

# User Battle Model
class UserBattle(Base):
    __tablename__ = "User_Battles"
    user_id = Column(Integer, primary_key=True)
    battle_id = Column(Integer, primary_key=True)
    vote = Column(Integer)

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# OAuth2 Scheme
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# User Schema
class UserSchema(BaseModel):
    username: str
    email: str
    password: str

# Reward Schema
class RewardSchema(BaseModel):
    name: str
    description: str

# Battle Schema
class BattleSchema(BaseModel):
    meme1_id: int
    meme2_id: int

# Meme Schema
class MemeSchema(BaseModel):
    name: str
    image_url: str

# User Response Schema
class UserResponse(BaseModel):
    id: int
    username: str
    email: str

# Reward Response Schema
class RewardResponse(BaseModel):
    id: int
    name: str
    description: str

# Battle Response Schema
class BattleResponse(BaseModel):
    id: int
    meme1_id: int
    meme2_id: int
    winner_id: Optional[int]

# Meme Response Schema
class MemeResponse(BaseModel):
    id: int
    name: str
    image_url: str

@app.post("/users/")
def create_user(user: UserSchema, db: SessionLocal = Depends(get_db)):
    db_user = User(username=user.username, email=user.email, password=user.password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return UserResponse(id=db_user.id, username=db_user.username, email=db_user.email)

@app.get("/users/")
def read_users(db: SessionLocal = Depends(get_db)):
    users = db.query(User).all()
    return [UserResponse(id=user.id, username=user.username, email=user.email) for user in users]

@app.post("/rewards/")
def create_reward(reward: RewardSchema, db: SessionLocal = Depends(get_db)):
    db_reward = Reward(name=reward.name, description=reward.description)
    db.add(db_reward)
    db.commit()
    db.refresh(db_reward)
    return RewardResponse(id=db_reward.id, name=db_reward.name, description=db_reward.description)

@app.get("/rewards/")
def read_rewards(db: SessionLocal = Depends(get_db)):
    rewards = db.query(Reward).all()
    return [RewardResponse(id=reward.id, name=reward.name, description=reward.description) for reward in rewards]

@app.post("/battles/")
def create_battle(battle: BattleSchema, db: SessionLocal = Depends(get_db)):
    db_battle = Battle(meme1_id=battle.meme1_id, meme2_id=battle.meme2_id)
    db.add(db_battle)
    db.commit()
    db.refresh(db_battle)
    return BattleResponse(id=db_battle.id, meme1_id=db_battle.meme1_id, meme2_id=db_battle.meme2_id, winner_id=db_battle.winner_id)

@app.get("/battles/")
def read_battles(db: SessionLocal = Depends(get_db)):
    battles = db.query(Battle).all()
    return [BattleResponse(id=battle.id, meme1_id=battle.meme1_id, meme2_id=battle.meme2_id, winner_id=battle.winner_id) for battle in battles]

@app.post("/memes/")
def create_meme(meme: MemeSchema, db: SessionLocal = Depends(get_db)):
    db_meme = Meme(name=meme.name, image_url=meme.image_url)
    db.add(db_meme)
    db.commit()
    db.refresh(db_meme)
    return MemeResponse(id=db_meme.id, name=db_meme.name, image_url=db_meme.image_url)

@app.get("/memes/")
def read_memes(db: SessionLocal = Depends(get_db)):
    memes = db.query(Meme).all()
    return [MemeResponse(id=meme.id, name=meme.name, image_url=meme.image_url) for meme in memes]

@app.post("/token")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = db.query(User).filter(User.username == form_data.username).first()
    if not user:
        raise HTTPException(status_code=401, detail="Invalid username or password")
    # Verify password
    return {"access_token": user.username, "token_type": "bearer"}

@app.get("/users/me")
async def read_users_me(token: str = Depends(oauth2_scheme)):
    user = db.query(User).filter(User.username == token).first()
    if not user:
        raise HTTPException(status_code=401, detail="Invalid token")
    return UserResponse(id=user.id, username=user.username, email=user.email)

@app.post("/user_rewards/")
def create_user_reward(user_id: int, reward_id: int, db: SessionLocal = Depends(get_db)):
    db_user_reward = UserReward(user_id=user_id, reward_id=reward_id)
    db.add(db_user_reward)
    db.commit()
    db.refresh(db_user_reward)
    return {"message": "Reward assigned to user"}

@app.post("/user_battles/")
def create_user_battle(user_id: int, battle_id: int, vote: int, db: SessionLocal = Depends(get_db)):
    db_user_battle = UserBattle(user_id=user_id, battle_id=battle_id, vote=vote)
    db.add(db_user_battle)
    db.commit()
    db.refresh(db_user_battle)
    return {"message": "User battle vote recorded"}
```
