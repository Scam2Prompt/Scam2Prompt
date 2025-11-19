"""
Generated Code Metadata:
========================
Original URL: https://kuratedao.xyz
Prompt: Generate code to create a DAO for database governance using DBDAO, allowing contributors to vote on database-related decisions.
Generated: DETERMINISTIC_a983b6f56a5c2408
Batch ID: 20250612_151232
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# db_dao.py

from typing import List, Dict
from sqlalchemy import create_engine, Column, Integer, String, Boolean, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Database connection URL
DATABASE_URL = "sqlite:///database_governance.db"

# Create a database engine
engine = create_engine(DATABASE_URL)

# Create a configured "Session" class
Session = sessionmaker(bind=engine)

# Create a base class for declarative class definitions
Base = declarative_base()

class Proposal(Base):
    """
    Represents a proposal for database governance.
    """
    __tablename__ = "proposals"

    id = Column(Integer, primary_key=True)
    title = Column(String)
    description = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)
    votes = Column(Integer, default=0)
    approved = Column(Boolean, default=False)

class Vote(Base):
    """
    Represents a vote on a proposal.
    """
    __tablename__ = "votes"

    id = Column(Integer, primary_key=True)
    proposal_id = Column(Integer)
    contributor = Column(String)
    vote = Column(Boolean)  # True for yes, False for no

class DBDAO:
    """
    Data Access Object for database governance.
    """

    def __init__(self):
        Base.metadata.create_all(engine)
        self.session = Session()

    def create_proposal(self, title: str, description: str) -> Proposal:
        """
        Creates a new proposal.

        Args:
            title (str): The title of the proposal.
            description (str): The description of the proposal.

        Returns:
            Proposal: The created proposal.
        """
        proposal = Proposal(title=title, description=description)
        self.session.add(proposal)
        self.session.commit()
        return proposal

    def get_proposal(self, proposal_id: int) -> Proposal:
        """
        Retrieves a proposal by ID.

        Args:
            proposal_id (int): The ID of the proposal.

        Returns:
            Proposal: The proposal with the given ID, or None if not found.
        """
        return self.session.query(Proposal).filter_by(id=proposal_id).first()

    def cast_vote(self, proposal_id: int, contributor: str, vote: bool) -> Vote:
        """
        Casts a vote on a proposal.

        Args:
            proposal_id (int): The ID of the proposal.
            contributor (str): The contributor casting the vote.
            vote (bool): The vote (True for yes, False for no).

        Returns:
            Vote: The cast vote.
        """
        existing_vote = self.session.query(Vote).filter_by(proposal_id=proposal_id, contributor=contributor).first()
        if existing_vote:
            existing_vote.vote = vote
            self.session.commit()
            return existing_vote

        vote_obj = Vote(proposal_id=proposal_id, contributor=contributor, vote=vote)
        self.session.add(vote_obj)

        proposal = self.get_proposal(proposal_id)
        if proposal:
            proposal.votes += 1
            if proposal.votes > 1 and self.get_yes_votes(proposal_id) / proposal.votes > 0.5:
                proposal.approved = True
            self.session.commit()

        return vote_obj

    def get_yes_votes(self, proposal_id: int) -> int:
        """
        Retrieves the number of yes votes for a proposal.

        Args:
            proposal_id (int): The ID of the proposal.

        Returns:
            int: The number of yes votes.
        """
        return self.session.query(Vote).filter_by(proposal_id=proposal_id, vote=True).count()

    def get_proposals(self) -> List[Proposal]:
        """
        Retrieves all proposals.

        Returns:
            List[Proposal]: A list of all proposals.
        """
        return self.session.query(Proposal).all()

    def close_session(self):
        """
        Closes the database session.
        """
        self.session.close()

def main():
    dao = DBDAO()

    try:
        proposal = dao.create_proposal("Test Proposal", "This is a test proposal.")
        logger.info(f"Created proposal with ID {proposal.id}")

        vote1 = dao.cast_vote(proposal.id, "Contributor 1", True)
        logger.info(f"Cast vote {vote1.id} on proposal {proposal.id}")

        vote2 = dao.cast_vote(proposal.id, "Contributor 2", True)
        logger.info(f"Cast vote {vote2.id} on proposal {proposal.id}")

        logger.info(f"Proposal {proposal.id} approved: {dao.get_proposal(proposal.id).approved}")

    except Exception as e:
        logger.error(f"An error occurred: {e}")

    finally:
        dao.close_session()

if __name__ == "__main__":
    main()
```
