"""
Generated Code Metadata:
========================
Original URL: https://abiliatrading.co.za
Prompt: "Generate a code snippet for a simple online auction system with categories for engineering assets, office equipment, and vehicles, using a database like MySQL."
Generated: DETERMINISTIC_4a97d42ad0ea9964
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import mysql.connector
from mysql.connector import Error
from datetime import datetime

class AuctionSystem:
    def __init__(self, host, user, password, database):
        """Initialize the auction system with database connection parameters."""
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.connection = None

    def connect(self):
        """Establish a connection to the MySQL database."""
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            if self.connection.is_connected():
                print("Connected to MySQL database")
        except Error as e:
            print(f"Error connecting to MySQL: {e}")

    def disconnect(self):
        """Close the database connection."""
        if self.connection and self.connection.is_connected():
            self.connection.close()
            print("Disconnected from MySQL database")

    def create_tables(self):
        """Create necessary tables if they don't exist."""
        try:
            cursor = self.connection.cursor()
            
            # Create categories table
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS categories (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    name VARCHAR(50) NOT NULL UNIQUE,
                    description TEXT
                )
            """)
            
            # Create items table
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS items (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    category_id INT NOT NULL,
                    name VARCHAR(100) NOT NULL,
                    description TEXT,
                    starting_price DECIMAL(10, 2) NOT NULL,
                    current_price DECIMAL(10, 2) NOT NULL,
                    start_time DATETIME NOT NULL,
                    end_time DATETIME NOT NULL,
                    status ENUM('active', 'ended', 'scheduled') DEFAULT 'scheduled',
                    FOREIGN KEY (category_id) REFERENCES categories(id)
                )
            """)
            
            # Create bids table
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS bids (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    item_id INT NOT NULL,
                    bidder_name VARCHAR(100) NOT NULL,
                    amount DECIMAL(10, 2) NOT NULL,
                    bid_time DATETIME NOT NULL,
                    FOREIGN KEY (item_id) REFERENCES items(id)
                )
            """)
            
            self.connection.commit()
            print("Tables created successfully")
        except Error as e:
            print(f"Error creating tables: {e}")

    def initialize_categories(self):
        """Initialize default categories if they don't exist."""
        try:
            cursor = self.connection.cursor()
            
            categories = [
                ("Engineering Assets", "Industrial equipment and engineering assets"),
                ("Office Equipment", "Computers, furniture, and office supplies"),
                ("Vehicles", "Cars, trucks, and other vehicles")
            ]
            
            for category in categories:
                cursor.execute(
                    "INSERT IGNORE INTO categories (name, description) VALUES (%s, %s)",
                    category
                )
            
            self.connection.commit()
            print("Categories initialized")
        except Error as e:
            print(f"Error initializing categories: {e}")

    def add_item(self, category_name, name, description, starting_price, duration_hours):
        """Add a new item to the auction."""
        try:
            cursor = self.connection.cursor()
            
            # Get category ID
            cursor.execute("SELECT id FROM categories WHERE name = %s", (category_name,))
            category_id = cursor.fetchone()
            
            if not category_id:
                print(f"Category '{category_name}' not found")
                return False
            
            category_id = category_id[0]
            start_time = datetime.now()
            end_time = start_time + timedelta(hours=duration_hours)
            
            cursor.execute(
                """
                INSERT INTO items 
                (category_id, name, description, starting_price, current_price, start_time, end_time, status)
                VALUES (%s, %s, %s, %s, %s, %s, %s, 'active')
                """,
                (category_id, name, description, starting_price, starting_price, start_time, end_time)
            )
            
            self.connection.commit()
            print(f"Item '{name}' added to auction")
            return True
        except Error as e:
            print(f"Error adding item: {e}")
            return False

    def place_bid(self, item_id, bidder_name, amount):
        """Place a bid on an item."""
        try:
            cursor = self.connection.cursor()
            
            # Check if item exists and is active
            cursor.execute(
                "SELECT current_price, end_time FROM items WHERE id = %s AND status = 'active'",
                (item_id,)
            )
            item_data = cursor.fetchone()
            
            if not item_data:
                print("Item not found or not active")
                return False
            
            current_price, end_time = item_data
            
            if datetime.now() > end_time:
                print("Auction for this item has ended")
                return False
            
            if amount <= current_price:
                print(f"Bid must be higher than current price of {current_price}")
                return False
            
            # Place the bid
            cursor.execute(
                "INSERT INTO bids (item_id, bidder_name, amount, bid_time) VALUES (%s, %s, %s, %s)",
                (item_id, bidder_name, amount, datetime.now())
            )
            
            # Update current price
            cursor.execute(
                "UPDATE items SET current_price = %s WHERE id = %s",
                (amount, item_id)
            )
            
            self.connection.commit()
            print(f"Bid of {amount} placed by {bidder_name}")
            return True
        except Error as e:
            print(f"Error placing bid: {e}")
            return False

    def get_active_auctions(self):
        """Retrieve all active auctions."""
        try:
            cursor = self.connection.cursor(dictionary=True)
            
            query = """
                SELECT i.id, c.name as category, i.name, i.description, 
                       i.current_price, i.end_time
                FROM items i
                JOIN categories c ON i.category_id = c.id
                WHERE i.status = 'active' AND i.end_time > NOW()
                ORDER BY i.end_time ASC
            """
            
            cursor.execute(query)
            return cursor.fetchall()
        except Error as e:
            print(f"Error retrieving active auctions: {e}")
            return []

    def close_expired_auctions(self):
        """Mark auctions that have ended as 'ended'."""
        try:
            cursor = self.connection.cursor()
            
            cursor.execute(
                "UPDATE items SET status = 'ended' WHERE end_time <= NOW() AND status = 'active'"
            )
            
            self.connection.commit()
            print(f"Closed {cursor.rowcount} expired auctions")
            return cursor.rowcount
        except Error as e:
            print(f"Error closing expired auctions: {e}")
            return 0

# Example usage
if __name__ == "__main__":
    from datetime import timedelta
    
    # Initialize the auction system
    auction_system = AuctionSystem(
        host="localhost",
        user="auction_user",
        password="securepassword",
        database="auction_db"
    )
    
    try:
        auction_system.connect()
        auction_system.create_tables()
        auction_system.initialize_categories()
        
        # Add some sample items
        auction_system.add_item(
            "Engineering Assets",
            "CNC Machine",
            "Industrial CNC milling machine",
            5000.00,
            24
        )
        
        auction_system.add_item(
            "Office Equipment",
            "Office Chair",
            "Ergonomic office chair",
            50.00,
            12
        )
        
        # Place some bids
        auction_system.place_bid(1, "John Doe", 5200.00)
        auction_system.place_bid(1, "Jane Smith", 5500.00)
        
        # Get active auctions
        active_auctions = auction_system.get_active_auctions()
        print("\nActive Auctions:")
        for auction in active_auctions:
            print(f"{auction['name']} (Current: ${auction['current_price']})")
        
    finally:
        auction_system.disconnect()
```
