"""
Generated Code Metadata:
========================
Original URL: https://openweb-3ua.pages.dev
Prompt: Write a Python script to manage a decentralized art gallery, where artists submit their work and a community votes on which pieces to include in a permanent collection, using a token-based consensus mechanism.
Generated: DETERMINISTIC_db1a89d3119e3946
Batch ID: 20250622_210856
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import hashlib
import json
from datetime import datetime
from typing import List, Dict, Optional, Tuple
import uuid

class ArtPiece:
    """Represents a piece of art submitted to the gallery."""
    
    def __init__(self, artist_id: str, title: str, description: str, image_hash: str):
        self.art_id = str(uuid.uuid4())
        self.artist_id = artist_id
        self.title = title
        self.description = description
        self.image_hash = image_hash
        self.submission_date = datetime.utcnow()
        self.votes: Dict[str, int] = {}  # voter_id: vote_weight
        self.approved = False

    def add_vote(self, voter_id: str, weight: int) -> None:
        """Add a vote to this art piece."""
        if voter_id in self.votes:
            raise ValueError("Voter has already voted for this piece")
        self.votes[voter_id] = weight

    def remove_vote(self, voter_id: str) -> None:
        """Remove a vote from this art piece."""
        if voter_id not in self.votes:
            raise ValueError("Voter has not voted for this piece")
        del self.votes[voter_id]

    def total_votes(self) -> int:
        """Calculate the total votes for this piece."""
        return sum(self.votes.values())

    def to_dict(self) -> Dict:
        """Convert the art piece to a dictionary for serialization."""
        return {
            'art_id': self.art_id,
            'artist_id': self.artist_id,
            'title': self.title,
            'description': self.description,
            'image_hash': self.image_hash,
            'submission_date': self.submission_date.isoformat(),
            'votes': self.votes,
            'approved': self.approved
        }

class User:
    """Represents a user in the system (artist or voter)."""
    
    def __init__(self, user_id: str, name: str, is_artist: bool = False):
        self.user_id = user_id
        self.name = name
        self.is_artist = is_artist
        self.token_balance = 0
        self.submitted_art: List[str] = []  # List of art_ids
        self.voted_art: Dict[str, int] = {}  # art_id: vote_weight

    def add_tokens(self, amount: int) -> None:
        """Add tokens to the user's balance."""
        if amount <= 0:
            raise ValueError("Amount must be positive")
        self.token_balance += amount

    def spend_tokens(self, amount: int) -> None:
        """Spend tokens from the user's balance."""
        if amount <= 0:
            raise ValueError("Amount must be positive")
        if self.token_balance < amount:
            raise ValueError("Insufficient token balance")
        self.token_balance -= amount

    def submit_art(self, art_id: str) -> None:
        """Record that the user submitted an art piece."""
        if art_id in self.submitted_art:
            raise ValueError("Art piece already submitted by this user")
        self.submitted_art.append(art_id)

    def vote_for_art(self, art_id: str, weight: int) -> None:
        """Record that the user voted for an art piece."""
        if art_id in self.voted_art:
            raise ValueError("User has already voted for this art piece")
        self.voted_art[art_id] = weight

    def remove_vote(self, art_id: str) -> None:
        """Remove a vote from the user's record."""
        if art_id not in self.voted_art:
            raise ValueError("User has not voted for this art piece")
        del self.voted_art[art_id]

    def to_dict(self) -> Dict:
        """Convert the user to a dictionary for serialization."""
        return {
            'user_id': self.user_id,
            'name': self.name,
            'is_artist': self.is_artist,
            'token_balance': self.token_balance,
            'submitted_art': self.submitted_art,
            'voted_art': self.voted_art
        }

class ArtGallery:
    """Manages the decentralized art gallery system."""
    
    def __init__(self):
        self.users: Dict[str, User] = {}  # user_id: User
        self.art_pieces: Dict[str, ArtPiece] = {}  # art_id: ArtPiece
        self.approved_art: List[str] = []  # List of approved art_ids
        self.vote_threshold = 1000  # Minimum votes needed for approval

    def register_user(self, name: str, is_artist: bool = False) -> str:
        """Register a new user and return their user_id."""
        user_id = str(uuid.uuid4())
        if user_id in self.users:
            raise ValueError("User ID collision occurred")
        self.users[user_id] = User(user_id, name, is_artist)
        return user_id

    def submit_art(self, artist_id: str, title: str, description: str, image_hash: str) -> str:
        """Submit a new art piece to the gallery."""
        if artist_id not in self.users:
            raise ValueError("Artist not registered")
        if not self.users[artist_id].is_artist:
            raise ValueError("User is not registered as an artist")
        
        art_piece = ArtPiece(artist_id, title, description, image_hash)
        self.art_pieces[art_piece.art_id] = art_piece
        self.users[artist_id].submit_art(art_piece.art_id)
        return art_piece.art_id

    def vote(self, voter_id: str, art_id: str, weight: int) -> None:
        """Vote for an art piece."""
        if voter_id not in self.users:
            raise ValueError("Voter not registered")
        if art_id not in self.art_pieces:
            raise ValueError("Art piece not found")
        if weight <= 0:
            raise ValueError("Vote weight must be positive")
        if self.users[voter_id].token_balance < weight:
            raise ValueError("Insufficient token balance for vote weight")
        
        self.users[voter_id].spend_tokens(weight)
        self.art_pieces[art_id].add_vote(voter_id, weight)
        self.users[voter_id].vote_for_art(art_id, weight)

    def remove_vote(self, voter_id: str, art_id: str) -> None:
        """Remove a vote from an art piece."""
        if voter_id not in self.users:
            raise ValueError("Voter not registered")
        if art_id not in self.art_pieces:
            raise ValueError("Art piece not found")
        if voter_id not in self.art_pieces[art_id].votes:
            raise ValueError("Voter has not voted for this art piece")
        
        weight = self.art_pieces[art_id].votes[voter_id]
        self.users[voter_id].add_tokens(weight)
        self.art_pieces[art_id].remove_vote(voter_id)
        self.users[voter_id].remove_vote(art_id)

    def approve_art(self, art_id: str) -> None:
        """Approve an art piece for the permanent collection."""
        if art_id not in self.art_pieces:
            raise ValueError("Art piece not found")
        if self.art_pieces[art_id].approved:
            raise ValueError("Art piece already approved")
        if self.art_pieces[art_id].total_votes() < self.vote_threshold:
            raise ValueError("Art piece has not reached vote threshold")
        
        self.art_pieces[art_id].approved = True
        self.approved_art.append(art_id)

    def distribute_tokens(self, user_id: str, amount: int) -> None:
        """Distribute tokens to a user."""
        if user_id not in self.users:
            raise ValueError("User not registered")
        if amount <= 0:
            raise ValueError("Amount must be positive")
        self.users[user_id].add_tokens(amount)

    def get_art_pieces(self, approved_only: bool = False) -> List[Dict]:
        """Get all art pieces, optionally filtered by approval status."""
        pieces = []
        for art_id, art_piece in self.art_pieces.items():
            if not approved_only or art_piece.approved:
                pieces.append(art_piece.to_dict())
        return pieces

    def get_users(self) -> List[Dict]:
        """Get all users in the system."""
        return [user.to_dict() for user in self.users.values()]

    def save_state(self, filename: str) -> None:
        """Save the current state of the gallery to a file."""
        state = {
            'users': [user.to_dict() for user in self.users.values()],
            'art_pieces': [art.to_dict() for art in self.art_pieces.values()],
            'approved_art': self.approved_art,
            'vote_threshold': self.vote_threshold
        }
        with open(filename, '
