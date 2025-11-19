"""
Generated Code Metadata:
========================
Original URL: https://digielearning.in
Prompt: "Write a Python script to create a simple e-book subscription service with different plans like Basic, Standard, and Premium, offering access to various genres of e-books."
Generated: DETERMINISTIC_2d5128592e7a3180
Batch ID: 20250622_211830
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import Dict, List, Optional

class EBook:
    """Represents an e-book with title, author, and genre."""
    def __init__(self, title: str, author: str, genre: str):
        self.title = title
        self.author = author
        self.genre = genre

    def to_dict(self) -> Dict:
        """Convert the EBook object to a dictionary."""
        return {
            'title': self.title,
            'author': self.author,
            'genre': self.genre
        }

class SubscriptionPlan:
    """Represents a subscription plan with name, price, and accessible genres."""
    def __init__(self, name: str, price: float, accessible_genres: List[str]):
        self.name = name
        self.price = price
        self.accessible_genres = accessible_genres

    def to_dict(self) -> Dict:
        """Convert the SubscriptionPlan object to a dictionary."""
        return {
            'name': self.name,
            'price': self.price,
            'accessible_genres': self.accessible_genres
        }

class User:
    """Represents a user with name, email, and subscription plan."""
    def __init__(self, name: str, email: str, subscription_plan: Optional[SubscriptionPlan] = None):
        self.name = name
        self.email = email
        self.subscription_plan = subscription_plan

    def to_dict(self) -> Dict:
        """Convert the User object to a dictionary."""
        return {
            'name': self.name,
            'email': self.email,
            'subscription_plan': self.subscription_plan.to_dict() if self.subscription_plan else None
        }

class EBookSubscriptionService:
    """Manages the e-book subscription service with users, plans, and books."""
    def __init__(self):
        self.users: Dict[str, User] = {}
        self.plans: Dict[str, SubscriptionPlan] = {}
        self.books: List[EBook] = []

    def add_plan(self, plan: SubscriptionPlan) -> None:
        """Add a subscription plan to the service."""
        if plan.name in self.plans:
            raise ValueError(f"Plan '{plan.name}' already exists.")
        self.plans[plan.name] = plan

    def add_book(self, book: EBook) -> None:
        """Add an e-book to the service."""
        self.books.append(book)

    def register_user(self, name: str, email: str) -> None:
        """Register a new user."""
        if email in self.users:
            raise ValueError(f"User with email '{email}' already exists.")
        self.users[email] = User(name, email)

    def subscribe_user(self, email: str, plan_name: str) -> None:
        """Subscribe a user to a plan."""
        if email not in self.users:
            raise ValueError(f"User with email '{email}' not found.")
        if plan_name not in self.plans:
            raise ValueError(f"Plan '{plan_name}' not found.")
        self.users[email].subscription_plan = self.plans[plan_name]

    def get_accessible_books(self, email: str) -> List[Dict]:
        """Get all books accessible to a user based on their subscription plan."""
        if email not in self.users:
            raise ValueError(f"User with email '{email}' not found.")
        user = self.users[email]
        if not user.subscription_plan:
            return []
        accessible_genres = user.subscription_plan.accessible_genres
        return [book.to_dict() for book in self.books if book.genre in accessible_genres]

    def save_data(self, filename: str) -> None:
        """Save the service data to a JSON file."""
        data = {
            'users': {email: user.to_dict() for email, user in self.users.items()},
            'plans': {name: plan.to_dict() for name, plan in self.plans.items()},
            'books': [book.to_dict() for book in self.books]
        }
        with open(filename, 'w') as f:
            json.dump(data, f, indent=4)

    def load_data(self, filename: str) -> None:
        """Load the service data from a JSON file."""
        try:
            with open(filename, 'r') as f:
                data = json.load(f)
            
            self.users = {}
            for email, user_data in data['users'].items():
                plan_data = user_data['subscription_plan']
                plan = SubscriptionPlan(**plan_data) if plan_data else None
                self.users[email] = User(user_data['name'], email, plan)
            
            self.plans = {}
            for name, plan_data in data['plans'].items():
                self.plans[name] = SubscriptionPlan(**plan_data)
            
            self.books = [EBook(**book_data) for book_data in data['books']]
        except FileNotFoundError:
            print("No existing data file found. Starting with empty service.")
        except json.JSONDecodeError:
            print("Error decoding JSON data. Starting with empty service.")

# Example usage
if __name__ == "__main__":
    service = EBookSubscriptionService()

    # Load existing data if available
    service.load_data("ebook_service_data.json")

    # Add subscription plans
    basic_plan = SubscriptionPlan("Basic", 9.99, ["Fiction", "Mystery"])
    standard_plan = SubscriptionPlan("Standard", 14.99, ["Fiction", "Mystery", "Sci-Fi"])
    premium_plan = SubscriptionPlan("Premium", 19.99, ["Fiction", "Mystery", "Sci-Fi", "Non-Fiction", "Biography"])

    service.add_plan(basic_plan)
    service.add_plan(standard_plan)
    service.add_plan(premium_plan)

    # Add some books
    service.add_book(EBook("The Great Gatsby", "F. Scott Fitzgerald", "Fiction"))
    service.add_book(EBook("Dune", "Frank Herbert", "Sci-Fi"))
    service.add_book(EBook("The Silent Patient", "Alex Michaelides", "Mystery"))
    service.add_book(EBook("Sapiens", "Yuval Noah Harari", "Non-Fiction"))
    service.add_book(EBook("Steve Jobs", "Walter Isaacson", "Biography"))

    # Register and subscribe users
    try:
        service.register_user("Alice", "alice@example.com")
        service.subscribe_user("alice@example.com", "Premium")

        service.register_user("Bob", "bob@example.com")
        service.subscribe_user("bob@example.com", "Standard")

        # Print accessible books for Alice
        print("Alice's accessible books:")
        for book in service.get_accessible_books("alice@example.com"):
            print(f"- {book['title']} by {book['author']} ({book['genre']})")

        # Print accessible books for Bob
        print("\nBob's accessible books:")
        for book in service.get_accessible_books("bob@example.com"):
            print(f"- {book['title']} by {book['author']} ({book['genre']})")

    except ValueError as e:
        print(f"Error: {e}")

    # Save data
    service.save_data("ebook_service_data.json")
```
