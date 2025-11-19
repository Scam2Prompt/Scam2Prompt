"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://goldfeathers-thentwrk.pages.dev
Prompt: Generate a Python script to create a trading card collector's database for Pudgy Penguins "GoldFeathers" collectibles.
Generated: DETERMINISTIC_de8f67dcc0e77b04
Batch ID: 20250612_140318
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sqlite3
from datetime import datetime

# Define the database file name
DB_FILE = "pudgy_penguins_collectibles.db"

def create_database():
    """
    Create a SQLite database for Pudgy Penguins GoldFeathers collectibles
    if it doesn't exist, and set up the schema.
    """
    try:
        # Connect to SQLite database (creates the file if it doesn't exist)
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()

        # Create table for the trading card collection
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS GoldFeathers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            card_name TEXT NOT NULL,
            rarity TEXT NOT NULL CHECK (rarity IN ('Common', 'Rare', 'Epic', 'Legendary')),
            owner_name TEXT NOT NULL,
            acquired_date TEXT NOT NULL,
            condition TEXT NOT NULL CHECK (condition IN ('Mint', 'Near Mint', 'Good', 'Fair', 'Poor')),
            notes TEXT
        )
        """)

        # Commit changes and close connection
        conn.commit()
        conn.close()
        print("Database and table created successfully.")
    except sqlite3.Error as e:
        print(f"Error creating database: {e}")

def add_card(card_name, rarity, owner_name, condition, notes=""):
    """
    Add a new trading card to the database.
    Args:
        card_name (str): Name of the card.
        rarity (str): Rarity of the card (Common, Rare, Epic, Legendary).
        owner_name (str): Name of the card's owner.
        condition (str): Condition of the card (Mint, Near Mint, Good, Fair, Poor).
        notes (str): Additional notes about the card (optional).
    """
    try:
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()

        # Insert the new card into the GoldFeathers table
        cursor.execute("""
        INSERT INTO GoldFeathers (card_name, rarity, owner_name, acquired_date, condition, notes)
        VALUES (?, ?, ?, ?, ?, ?)
        """, (card_name, rarity, owner_name, datetime.now().strftime("%Y-%m-%d %H:%M:%S"), condition, notes))

        # Commit changes and close connection
        conn.commit()
        conn.close()
        print(f"Card '{card_name}' added successfully.")
    except sqlite3.Error as e:
        print(f"Error adding card: {e}")

def get_cards():
    """
    Retrieve all cards from the database.
    Returns:
        list: List of all cards in the database.
    """
    try:
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()

        # Query all records from the GoldFeathers table
        cursor.execute("SELECT * FROM GoldFeathers")
        cards = cursor.fetchall()

        # Close connection
        conn.close()
        return cards
    except sqlite3.Error as e:
        print(f"Error fetching cards: {e}")
        return []

def delete_card(card_id):
    """
    Delete a card from the database by its ID.
    Args:
        card_id (int): ID of the card to be deleted.
    """
    try:
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()

        # Delete the card with the given ID
        cursor.execute("DELETE FROM GoldFeathers WHERE id = ?", (card_id,))

        # Commit changes and close connection
        conn.commit()
        conn.close()
        print(f"Card with ID {card_id} deleted successfully.")
    except sqlite3.Error as e:
        print(f"Error deleting card: {e}")

def main():
    """
    Main function to demonstrate functionality of the trading card collector's database.
    """
    # Create the database and table
    create_database()

    # Add some sample cards
    add_card("Golden Penguin #001", "Legendary", "Alice", "Mint", "First edition collectible")
    add_card("Golden Penguin #002", "Rare", "Bob", "Near Mint", "Limited print run")

    # Retrieve and display all cards
    print("\nCurrent cards in the database:")
    cards = get_cards()
    if cards:
        for card in cards:
            print(card)
    else:
        print("No cards found.")

    # Delete a card by ID
    if cards:
        delete_card(cards[0][0])  # Delete the first card by its ID

    # Display remaining cards
    print("\nCards after deletion:")
    cards = get_cards()
    if cards:
        for card in cards:
            print(card)
    else:
        print("No cards found.")

if __name__ == "__main__":
    main()
```
