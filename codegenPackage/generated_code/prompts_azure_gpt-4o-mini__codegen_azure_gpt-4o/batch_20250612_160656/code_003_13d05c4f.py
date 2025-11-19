"""
Generated Code Metadata:
========================
Original URL: https://pad-chaingpt.pages.dev
Prompt: Explain how the decentralized job economy of Work X operates without commercial middlemen like UpWork or Indeed.
Generated: DETERMINISTIC_13d05c4fcc03614f
Batch ID: 20250612_160656
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
This script simulates the decentralized job economy of Work X, where job seekers and employers interact directly
without commercial middlemen like UpWork or Indeed. It uses blockchain-like principles to ensure transparency,
trust, and direct communication between parties.
"""

import hashlib
import json
from datetime import datetime


class WorkXPlatform:
    """
    A class representing the decentralized job economy platform.
    """

    def __init__(self):
        # Initialize the blockchain with a genesis block
        self.blockchain = []
        self.create_block(previous_hash="0", data="Genesis Block")
        self.users = {}  # Dictionary to store user profiles

    def create_block(self, previous_hash, data):
        """
        Creates a new block in the blockchain.

        :param previous_hash: Hash of the previous block
        :param data: Data to be stored in the block (e.g., job postings, applications)
        :return: The newly created block
        """
        block = {
            "index": len(self.blockchain) + 1,
            "timestamp": str(datetime.utcnow()),
            "data": data,
            "previous_hash": previous_hash,
            "hash": self.hash_block(previous_hash, data),
        }
        self.blockchain.append(block)
        return block

    @staticmethod
    def hash_block(previous_hash, data):
        """
        Generates a hash for a block.

        :param previous_hash: Hash of the previous block
        :param data: Data to be stored in the block
        :return: A SHA-256 hash of the block
        """
        block_string = f"{previous_hash}{json.dumps(data, sort_keys=True)}"
        return hashlib.sha256(block_string.encode()).hexdigest()

    def register_user(self, user_id, profile):
        """
        Registers a new user on the platform.

        :param user_id: Unique identifier for the user
        :param profile: Dictionary containing user profile information
        :return: Success message or error
        """
        if user_id in self.users:
            return "Error: User ID already exists."
        self.users[user_id] = profile
        return f"User {user_id} registered successfully."

    def post_job(self, employer_id, job_details):
        """
        Posts a new job to the blockchain.

        :param employer_id: ID of the employer posting the job
        :param job_details: Dictionary containing job details
        :return: Success message or error
        """
        if employer_id not in self.users:
            return "Error: Employer not registered."
        job_data = {
            "employer_id": employer_id,
            "job_details": job_details,
        }
        self.create_block(previous_hash=self.blockchain[-1]["hash"], data=job_data)
        return "Job posted successfully."

    def apply_for_job(self, job_index, applicant_id, application_details):
        """
        Allows a user to apply for a job.

        :param job_index: Index of the job in the blockchain
        :param applicant_id: ID of the applicant
        :param application_details: Dictionary containing application details
        :return: Success message or error
        """
        if applicant_id not in self.users:
            return "Error: Applicant not registered."
        if job_index < 1 or job_index > len(self.blockchain):
            return "Error: Invalid job index."
        job_block = self.blockchain[job_index - 1]
        application_data = {
            "job_index": job_index,
            "applicant_id": applicant_id,
            "application_details": application_details,
        }
        self.create_block(previous_hash=self.blockchain[-1]["hash"], data=application_data)
        return "Application submitted successfully."

    def view_blockchain(self):
        """
        Returns the entire blockchain.

        :return: List of all blocks in the blockchain
        """
        return self.blockchain


# Example usage
if __name__ == "__main__":
    # Initialize the platform
    platform = WorkXPlatform()

    # Register users
    print(platform.register_user("user1", {"name": "Alice", "skills": ["Python", "Blockchain"]}))
    print(platform.register_user("user2", {"name": "Bob", "skills": ["JavaScript", "React"]}))
    print(platform.register_user("employer1", {"name": "TechCorp", "industry": "Software"}))

    # Post a job
    job_details = {
        "title": "Blockchain Developer",
        "description": "Looking for an experienced blockchain developer.",
        "requirements": ["Python", "Blockchain"],
        "salary": "100k/year",
    }
    print(platform.post_job("employer1", job_details))

    # Apply for a job
    application_details = {
        "cover_letter": "I am passionate about blockchain development.",
        "resume": "Link to resume",
    }
    print(platform.apply_for_job(2, "user1", application_details))

    # View the blockchain
    print(json.dumps(platform.view_blockchain(), indent=4))
```
