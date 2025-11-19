"""
Generated Code Metadata:
========================
Original URL: https://rakhshandamemorial.org
Prompt: Write Python code to simulate a "Food ATM" system where users can purchase meals at subsidized rates. Include features for meal selection, payment processing, and tracking daily transactions.
Generated: DETERMINISTIC_7af413c5a0a0cc99
Batch ID: 20250612_152240
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import datetime
from typing import Dict, List, Optional

class FoodItem:
    """Represents a food item available in the Food ATM."""
    def __init__(self, id: int, name: str, price: float, stock: int):
        self.id = id
        self.name = name
        self.price = price
        self.stock = stock

    def to_dict(self) -> Dict:
        """Convert FoodItem to dictionary for serialization."""
        return {
            'id': self.id,
            'name': self.name,
            'price': self.price,
            'stock': self.stock
        }

    @classmethod
    def from_dict(cls, data: Dict) -> 'FoodItem':
        """Create FoodItem from dictionary."""
        return cls(
            id=data['id'],
            name=data['name'],
            price=data['price'],
            stock=data['stock']
        )

class Transaction:
    """Represents a transaction in the Food ATM."""
    def __init__(self, transaction_id: int, user_id: str, items: List[Dict], total: float, timestamp: str):
        self.transaction_id = transaction_id
        self.user_id = user_id
        self.items = items
        self.total = total
        self.timestamp = timestamp

    def to_dict(self) -> Dict:
        """Convert Transaction to dictionary for serialization."""
        return {
            'transaction_id': self.transaction_id,
            'user_id': self.user_id,
            'items': self.items,
            'total': self.total,
            'timestamp': self.timestamp
        }

    @classmethod
    def from_dict(cls, data: Dict) -> 'Transaction':
        """Create Transaction from dictionary."""
        return cls(
            transaction_id=data['transaction_id'],
            user_id=data['user_id'],
            items=data['items'],
            total=data['total'],
            timestamp=data['timestamp']
        )

class FoodATM:
    """Main class representing the Food ATM system."""
    def __init__(self, data_file: str = 'food_atm_data.json'):
        self.data_file = data_file
        self.food_items: Dict[int, FoodItem] = {}
        self.transactions: List[Transaction] = []
        self.load_data()

    def load_data(self) -> None:
        """Load data from JSON file."""
        try:
            with open(self.data_file, 'r') as f:
                data = json.load(f)
                self.food_items = {item['id']: FoodItem.from_dict(item) for item in data.get('food_items', [])}
                self.transactions = [Transaction.from_dict(tx) for tx in data.get('transactions', [])]
        except FileNotFoundError:
            self.food_items = {}
            self.transactions = []
        except json.JSONDecodeError:
            raise ValueError("Invalid data file format")

    def save_data(self) -> None:
        """Save data to JSON file."""
        data = {
            'food_items': [item.to_dict() for item in self.food_items.values()],
            'transactions': [tx.to_dict() for tx in self.transactions]
        }
        with open(self.data_file, 'w') as f:
            json.dump(data, f, indent=2)

    def add_food_item(self, name: str, price: float, stock: int) -> int:
        """Add a new food item to the system."""
        if price <= 0:
            raise ValueError("Price must be positive")
        if stock < 0:
            raise ValueError("Stock cannot be negative")
        
        item_id = max(self.food_items.keys(), default=0) + 1
        self.food_items[item_id] = FoodItem(item_id, name, price, stock)
        self.save_data()
        return item_id

    def get_available_items(self) -> List[Dict]:
        """Get list of available food items with stock."""
        return [item.to_dict() for item in self.food_items.values() if item.stock > 0]

    def process_purchase(self, user_id: str, items: List[Dict]) -> Transaction:
        """
        Process a purchase transaction.
        
        Args:
            user_id: ID of the user making the purchase
            items: List of dictionaries with 'item_id' and 'quantity'
            
        Returns:
            Transaction object representing the purchase
        """
        if not user_id:
            raise ValueError("User ID is required")
        if not items:
            raise ValueError("At least one item must be selected")
        
        purchased_items = []
        total = 0.0
        
        for item in items:
            item_id = item['item_id']
            quantity = item['quantity']
            
            if item_id not in self.food_items:
                raise ValueError(f"Item ID {item_id} not found")
            
            food_item = self.food_items[item_id]
            
            if quantity <= 0:
                raise ValueError(f"Invalid quantity for item {food_item.name}")
            if quantity > food_item.stock:
                raise ValueError(f"Insufficient stock for item {food_item.name}")
            
            item_total = food_item.price * quantity
            purchased_items.append({
                'item_id': item_id,
                'name': food_item.name,
                'quantity': quantity,
                'price': food_item.price,
                'item_total': item_total
            })
            
            total += item_total
            food_item.stock -= quantity
        
        transaction_id = max([tx.transaction_id for tx in self.transactions], default=0) + 1
        timestamp = datetime.datetime.now().isoformat()
        
        transaction = Transaction(
            transaction_id=transaction_id,
            user_id=user_id,
            items=purchased_items,
            total=total,
            timestamp=timestamp
        )
        
        self.transactions.append(transaction)
        self.save_data()
        return transaction

    def get_daily_transactions(self, date: Optional[str] = None) -> List[Dict]:
        """
        Get transactions for a specific date (default: today).
        
        Args:
            date: Date in YYYY-MM-DD format (optional)
            
        Returns:
            List of transaction dictionaries for the specified date
        """
        if date is None:
            date = datetime.datetime.now().strftime('%Y-%m-%d')
        
        try:
            target_date = datetime.datetime.strptime(date, '%Y-%m-%d').date()
        except ValueError:
            raise ValueError("Invalid date format. Use YYYY-MM-DD")
        
        daily_transactions = []
        
        for tx in self.transactions:
            tx_date = datetime.datetime.fromisoformat(tx.timestamp).date()
            if tx_date == target_date:
                daily_transactions.append(tx.to_dict())
        
        return daily_transactions

    def get_transaction_by_id(self, transaction_id: int) -> Optional[Dict]:
        """Get a transaction by its ID."""
        for tx in self.transactions:
            if tx.transaction_id == transaction_id:
                return tx.to_dict()
        return None

# Example usage
if __name__ == "__main__":
    atm = FoodATM()
    
    # Add some sample food items
    try:
        atm.add_food_item("Vegetable Meal", 2.50, 10)
        atm.add_food_item("Protein Meal", 3.00, 8)
        atm.add_food_item("Fruit Pack", 1.50, 15)
    except ValueError as e:
        print(f"Error adding food items: {e}")
    
    # Display available items
    print("Available Items:")
    for item in atm.get_available_items():
        print(f"{item['id']}: {item['name']} - ${item['price']:.2f} (Stock: {item['stock']})")
    
    # Process a purchase
    try:
        purchase = atm.process_purchase(
            user_id="user123",
            items=[
                {'item_id': 1, 'quantity': 2},
                {'item_id': 3, 'quantity': 1}
            ]
        )
        print(f"\nPurchase successful! Transaction ID: {purchase.transaction_id}")
        print(f"Total: ${purchase.total:.2f}")
    except ValueError as e:
        print(f"\nPurchase failed: {e}")
    
    # View today's transactions
    print("\nToday's Transactions:")
    for tx in atm.get_daily_transactions():
        print(f"TX {tx['transaction_id']}: User {tx['user_id']} - ${tx['total']:.2f}")
```
