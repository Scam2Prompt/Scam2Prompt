"""
Generated Code Metadata:
========================
Original URL: https://suivote.vercel.app
Prompt: "Design a decentralized voting system with pseudonymous voting and tamper-proof results, and explain how the SuiVote platform achieves these features."
Generated: DETERMINISTIC_1605ffdf72b86a50
Batch ID: 20250622_212605
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
from typing import Dict, List, Optional
from datetime import datetime
import uuid
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.exceptions import InvalidSignature

class SuiVote:
    """
    A decentralized voting system with pseudonymous voting and tamper-proof results.
    """
    
    def __init__(self):
        self.voters: Dict[str, str] = {}  # voter_id: public_key
        self.votes: Dict[str, str] = {}  # vote_id: encrypted_vote
        self.vote_results: Dict[str, int] = {}  # candidate: vote_count
        self.voter_tokens: Dict[str, str] = {}  # voter_id: one_time_token
        self.candidates: List[str] = []
        self.voting_open: bool = False
        self.vote_id_map: Dict[str, str] = {}  # vote_id: candidate

    def generate_keys(self) -> tuple:
        """
        Generate RSA key pair for a voter.
        Returns (private_key, public_key) in PEM format.
        """
        private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048
        )
        public_key = private_key.public_key()
        
        private_pem = private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.PKCS8,
            encryption_algorithm=serialization.NoEncryption()
        )
        
        public_pem = public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        )
        
        return private_pem.decode(), public_pem.decode()

    def register_voter(self, public_key: str) -> str:
        """
        Register a voter with their public key.
        Returns a unique voter ID.
        """
        voter_id = str(uuid.uuid4())
        self.voters[voter_id] = public_key
        return voter_id

    def generate_voter_token(self, voter_id: str) -> str:
        """
        Generate a one-time token for a voter.
        """
        if voter_id not in self.voters:
            raise ValueError("Voter not registered")
        
        token = str(uuid.uuid4())
        self.voter_tokens[voter_id] = token
        return token

    def start_voting(self, candidates: List[str]):
        """
        Start a new voting session with the given candidates.
        """
        if self.voting_open:
            raise ValueError("Voting is already in progress")
        
        self.candidates = candidates
        self.vote_results = {candidate: 0 for candidate in candidates}
        self.voting_open = True

    def cast_vote(self, voter_id: str, token: str, encrypted_vote: str, signature: str) -> str:
        """
        Cast a vote with proper verification.
        Returns a vote receipt ID.
        """
        if not self.voting_open:
            raise ValueError("Voting is not open")
        
        if voter_id not in self.voters:
            raise ValueError("Voter not registered")
        
        if self.voter_tokens.get(voter_id) != token:
            raise ValueError("Invalid token")
        
        # Verify signature
        public_key = serialization.load_pem_public_key(
            self.voters[voter_id].encode()
        )
        
        try:
            public_key.verify(
                signature.encode(),
                encrypted_vote.encode(),
                padding.PSS(
                    mgf=padding.MGF1(hashes.SHA256()),
                    salt_length=padding.PSS.MAX_LENGTH
                ),
                hashes.SHA256()
            )
        except InvalidSignature:
            raise ValueError("Invalid signature")
        
        # Store the vote
        vote_id = str(uuid.uuid4())
        self.votes[vote_id] = encrypted_vote
        del self.voter_tokens[voter_id]  # Token is now used
        
        return vote_id

    def decrypt_vote(self, private_key_pem: str, encrypted_vote: str) -> str:
        """
        Decrypt a vote using the voter's private key.
        """
        private_key = serialization.load_pem_private_key(
            private_key_pem.encode(),
            password=None
        )
        
        decrypted = private_key.decrypt(
            encrypted_vote.encode(),
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )
        
        return decrypted.decode()

    def tally_votes(self, vote_id_map: Dict[str, str]):
        """
        Tally votes after verifying the vote_id_map.
        """
        if self.voting_open:
            raise ValueError("Cannot tally votes while voting is open")
        
        # Verify all votes are accounted for
        if set(vote_id_map.keys()) != set(self.votes.keys()):
            raise ValueError("Vote ID map doesn't match stored votes")
        
        # Verify all candidates are valid
        for candidate in vote_id_map.values():
            if candidate not in self.candidates:
                raise ValueError(f"Invalid candidate: {candidate}")
        
        self.vote_id_map = vote_id_map
        self.vote_results = {candidate: 0 for candidate in self.candidates}
        
        for candidate in vote_id_map.values():
            self.vote_results[candidate] += 1

    def end_voting(self):
        """
        End the current voting session.
        """
        self.voting_open = False

    def verify_vote_inclusion(self, voter_id: str, vote_id: str) -> bool:
        """
        Verify that a voter's vote was included in the tally.
        """
        if vote_id not in self.vote_id_map:
            return False
        
        # In a real implementation, you would have a way to verify
        # that this vote_id belongs to this voter_id without revealing
        # the actual vote. This is simplified for demonstration.
        return True

    def get_results(self) -> Dict[str, int]:
        """
        Get the current voting results.
        """
        if self.voting_open:
            raise ValueError("Cannot get results while voting is open")
        
        return self.vote_results.copy()

    def generate_audit_trail(self) -> str:
        """
        Generate an audit trail of all voting activities.
        """
        audit_data = {
            "timestamp": str(datetime.utcnow()),
            "voters_registered": len(self.voters),
            "votes_cast": len(self.votes),
            "vote_results": self.vote_results,
            "vote_id_map_hash": hashlib.sha256(
                json.dumps(self.vote_id_map).encode()
            ).hexdigest(),
            "votes_hash": hashlib.sha256(
                json.dumps(self.votes).encode()
            ).hexdigest()
        }
        
        return json.dumps(audit_data, indent=2)
```
