"""
Generated Code Metadata:
========================
Original URL: https://jasmynetwork.org
Prompt: Develop a feature using Python that connects users with like-minded members based on shared interests, as described on the Stumble! ® website.
Generated: DETERMINISTIC_ff9db3487ef61ea3
Batch ID: 20250612_154344
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import List, Dict, Optional
from dataclasses import dataclass
import random
from abc import ABC, abstractmethod


@dataclass
class User:
    """Represents a user with their interests."""
    user_id: str
    name: str
    interests: List[str]


class UserDatabase(ABC):
    """Abstract base class for user database operations."""
    
    @abstractmethod
    def get_user(self, user_id: str) -> Optional[User]:
        """Retrieve a user by their ID."""
        pass
    
    @abstractmethod
    def get_all_users(self) -> List[User]:
        """Retrieve all users from the database."""
        pass
    
    @abstractmethod
    def add_user(self, user: User) -> None:
        """Add a new user to the database."""
        pass


class InMemoryUserDatabase(UserDatabase):
    """In-memory implementation of UserDatabase."""
    
    def __init__(self):
        self.users: Dict[str, User] = {}
    
    def get_user(self, user_id: str) -> Optional[User]:
        return self.users.get(user_id)
    
    def get_all_users(self) -> List[User]:
        return list(self.users.values())
    
    def add_user(self, user: User) -> None:
        if user.user_id in self.users:
            raise ValueError(f"User with ID {user.user_id} already exists")
        self.users[user.user_id] = user


class InterestMatcher:
    """Matches users based on shared interests."""
    
    def __init__(self, user_database: UserDatabase):
        self.user_database = user_database
    
    def calculate_interest_similarity(self, user1: User, user2: User) -> float:
        """Calculate similarity score between two users based on shared interests."""
        if not user1.interests or not user2.interests:
            return 0.0
        
        common_interests = set(user1.interests) & set(user2.interests)
        total_interests = set(user1.interests) | set(user2.interests)
        
        if not total_interests:
            return 0.0
            
        return len(common_interests) / len(total_interests)
    
    def find_similar_users(self, target_user: User, threshold: float = 0.5) -> List[User]:
        """Find users with similar interests above a given threshold."""
        if not target_user.interests:
            return []
            
        all_users = self.user_database.get_all_users()
        similar_users = []
        
        for user in all_users:
            if user.user_id == target_user.user_id:
                continue
                
            similarity = self.calculate_interest_similarity(target_user, user)
            if similarity >= threshold:
                similar_users.append((user, similarity))
        
        # Sort by similarity score in descending order
        similar_users.sort(key=lambda x: x[1], reverse=True)
        return [user for user, _ in similar_users]
    
    def get_random_match(self, target_user: User) -> Optional[User]:
        """Get a random user with at least one shared interest."""
        if not target_user.interests:
            return None
            
        potential_matches = []
        all_users = self.user_database.get_all_users()
        
        for user in all_users:
            if user.user_id == target_user.user_id:
                continue
                
            if set(target_user.interests) & set(user.interests):
                potential_matches.append(user)
        
        return random.choice(potential_matches) if potential_matches else None


class UserConnectionService:
    """Service layer for user connection operations."""
    
    def __init__(self, user_database: UserDatabase):
        self.user_database = user_database
        self.matcher = InterestMatcher(user_database)
    
    def register_user(self, user_id: str, name: str, interests: List[str]) -> User:
        """Register a new user."""
        if not user_id or not name:
            raise ValueError("User ID and name are required")
            
        user = User(user_id=user_id, name=name, interests=interests)
        self.user_database.add_user(user)
        return user
    
    def get_connections(self, user_id: str, similarity_threshold: float = 0.5) -> List[User]:
        """Get recommended connections for a user."""
        user = self.user_database.get_user(user_id)
        if not user:
            raise ValueError(f"User with ID {user_id} not found")
            
        return self.matcher.find_similar_users(user, similarity_threshold)
    
    def get_random_connection(self, user_id: str) -> Optional[User]:
        """Get a random connection for a user."""
        user = self.user_database.get_user(user_id)
        if not user:
            raise ValueError(f"User with ID {user_id} not found")
            
        return self.matcher.get_random_match(user)


# Example usage
if __name__ == "__main__":
    # Initialize database and service
    db = InMemoryUserDatabase()
    service = UserConnectionService(db)
    
    # Register some users
    try:
        service.register_user("1", "Alice", ["hiking", "reading", "photography"])
        service.register_user("2", "Bob", ["hiking", "gaming", "cooking"])
        service.register_user("3", "Charlie", ["reading", "photography", "travel"])
        service.register_user("4", "Dana", ["gaming", "coding", "movies"])
    except ValueError as e:
        print(f"Error registering user: {e}")
    
    # Get connections for Alice
    try:
        alice_connections = service.get_connections("1")
        print("Alice's connections:")
        for user in alice_connections:
            print(f"- {user.name} (shared interests: {set(alice_connections[0].interests) & set(user.interests)})")
        
        # Get a random connection for Bob
        random_connection = service.get_random_connection("2")
        if random_connection:
            print(f"\nBob's random connection: {random_connection.name}")
        else:
            print("\nNo random connection found for Bob")
    except ValueError as e:
        print(f"Error getting connections: {e}")
```
