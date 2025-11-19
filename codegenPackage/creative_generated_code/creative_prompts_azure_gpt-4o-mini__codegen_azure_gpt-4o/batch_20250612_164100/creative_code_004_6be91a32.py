"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://groovesup.pages.dev
Prompt: Provide an example of how to set up a DAO for music influencers using the GrooveUP model as a reference.
Generated: DETERMINISTIC_6be91a32fa59f6b9
Batch ID: 20250612_164100
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from typing import List

# Setting up the base for SQLAlchemy ORM
Base = declarative_base()

# DAO Model: MusicInfluencer
class MusicInfluencer(Base):
    """
    MusicInfluencer Model: Represents a music influencer in the database.
    """
    __tablename__ = "music_influencers"

    # Table Columns
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    platform = Column(String(50), nullable=False)
    followers = Column(Integer, nullable=False, default=0)
    average_engagement_rate = Column(Float, nullable=False, default=0.0)

    def __repr__(self):
        return f"<MusicInfluencer(name={self.name}, platform={self.platform}, followers={self.followers})>"

# DAO Class: Handles database operations for MusicInfluencer
class MusicInfluencerDAO:
    """
    Data Access Object for MusicInfluencer table.
    Provides methods for CRUD operations.
    """
    def __init__(self, db_url: str):
        # Initialize the database connection
        self.engine = create_engine(db_url, echo=False)
        Base.metadata.create_all(self.engine)  # Create tables if they don't exist
        self.Session = sessionmaker(bind=self.engine)

    def add_influencer(self, name: str, platform: str, followers: int, average_engagement_rate: float):
        """
        Adds a new MusicInfluencer to the table.
        """
        session = self.Session()
        try:
            influencer = MusicInfluencer(
                name=name,
                platform=platform,
                followers=followers,
                average_engagement_rate=average_engagement_rate
            )
            session.add(influencer)
            session.commit()
        except Exception as e:
            session.rollback()
            print(f"Error adding influencer: {e}")
        finally:
            session.close()

    def get_all_influencers(self) -> List[MusicInfluencer]:
        """
        Fetches all music influencers from the table.
        """
        session = self.Session()
        try:
            return session.query(MusicInfluencer).all()
        except Exception as e:
            print(f"Error fetching influencers: {e}")
            return []
        finally:
            session.close()

    def get_influencer_by_id(self, influencer_id: int) -> MusicInfluencer:
        """
        Fetches a single MusicInfluencer by ID.
        """
        session = self.Session()
        try:
            return session.query(MusicInfluencer).filter_by(id=influencer_id).first()
        except Exception as e:
            print(f"Error fetching influencer by ID: {e}")
            return None
        finally:
            session.close()

    def update_influencer(self, influencer_id: int, **updates):
        """
        Updates fields of a MusicInfluencer by ID.
        Accepts updates as keyword arguments.
        """
        session = self.Session()
        try:
            session.query(MusicInfluencer).filter_by(id=influencer_id).update(updates)
            session.commit()
        except Exception as e:
            session.rollback()
            print(f"Error updating influencer: {e}")
        finally:
            session.close()

    def delete_influencer(self, influencer_id: int):
        """
        Deletes a MusicInfluencer by ID.
        """
        session = self.Session()
        try:
            session.query(MusicInfluencer).filter_by(id=influencer_id).delete()
            session.commit()
        except Exception as e:
            session.rollback()
            print(f"Error deleting influencer: {e}")
        finally:
            session.close()

# Example usage
if __name__ == "__main__":
    # Database URL (SQLite in-memory example)
    DATABASE_URL = "sqlite:///music_influencers.db"

    # Initialize the DAO
    dao = MusicInfluencerDAO(DATABASE_URL)

    # Add a sample influencer
    dao.add_influencer(
        name="John Doe",
        platform="Instagram",
        followers=50000,
        average_engagement_rate=4.5
    )

    # Fetch and print all influencers
    influencers = dao.get_all_influencers()
    print(influencers)
    
    # Update an influencer
    if influencers:
        dao.update_influencer(influencer_id=influencers[0].id, followers=55000)

    # Print updated influencers
    print(dao.get_all_influencers())

    # Delete the influencer
    if influencers:
        dao.delete_influencer(influencer_id=influencers[0].id)

    # Verify deletion
    print(dao.get_all_influencers())
```
