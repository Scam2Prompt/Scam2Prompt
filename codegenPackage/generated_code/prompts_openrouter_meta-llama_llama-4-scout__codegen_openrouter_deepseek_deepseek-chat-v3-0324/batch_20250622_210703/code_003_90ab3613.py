"""
Generated Code Metadata:
========================
Original URL: https://econtrolsa.ch
Prompt: "Design a simple database schema to store information about electric vehicles, including their mileage on a single charge, traction battery capacity, and price, inspired by the car models listed on eControl SA's website."
Generated: DETERMINISTIC_90ab361378e6b8b5
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import sqlite3
from typing import Optional

def create_database(db_name: str = "electric_vehicles.db") -> None:
    """
    Creates a SQLite database with a table for storing electric vehicle information.
    
    Args:
        db_name: Name of the SQLite database file.
    """
    conn = None
    try:
        conn = sqlite3.connect(db_name)
        cursor = conn.cursor()
        
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS vehicles (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            make TEXT NOT NULL,
            model TEXT NOT NULL,
            year INTEGER NOT NULL,
            mileage_per_charge REAL NOT NULL,
            battery_capacity_kwh REAL NOT NULL,
            price_usd REAL NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """)
        
        # Create trigger to update timestamp on row update
        cursor.execute("""
        CREATE TRIGGER IF NOT EXISTS update_vehicle_timestamp
        AFTER UPDATE ON vehicles
        FOR EACH ROW
        BEGIN
            UPDATE vehicles SET updated_at = CURRENT_TIMESTAMP WHERE id = OLD.id;
        END
        """)
        
        conn.commit()
        
    except sqlite3.Error as e:
        print(f"Database error: {e}")
    finally:
        if conn:
            conn.close()

def add_vehicle(
    make: str,
    model: str,
    year: int,
    mileage_per_charge: float,
    battery_capacity_kwh: float,
    price_usd: float,
    db_name: str = "electric_vehicles.db"
) -> Optional[int]:
    """
    Adds a new electric vehicle to the database.
    
    Args:
        make: Vehicle manufacturer (e.g., "Tesla")
        model: Vehicle model (e.g., "Model 3")
        year: Manufacturing year
        mileage_per_charge: Estimated mileage on single charge (miles)
        battery_capacity_kwh: Battery capacity in kilowatt-hours
        price_usd: Price in US dollars
        db_name: Name of the SQLite database file
        
    Returns:
        ID of the newly inserted vehicle or None if insertion failed
    """
    conn = None
    try:
        conn = sqlite3.connect(db_name)
        cursor = conn.cursor()
        
        cursor.execute("""
        INSERT INTO vehicles (
            make, model, year, mileage_per_charge, battery_capacity_kwh, price_usd
        ) VALUES (?, ?, ?, ?, ?, ?)
        """, (make, model, year, mileage_per_charge, battery_capacity_kwh, price_usd))
        
        conn.commit()
        return cursor.lastrowid
        
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return None
    finally:
        if conn:
            conn.close()

def get_vehicle_by_id(
    vehicle_id: int,
    db_name: str = "electric_vehicles.db"
) -> Optional[dict]:
    """
    Retrieves a vehicle by its ID.
    
    Args:
        vehicle_id: ID of the vehicle to retrieve
        db_name: Name of the SQLite database file
        
    Returns:
        Dictionary with vehicle data or None if not found
    """
    conn = None
    try:
        conn = sqlite3.connect(db_name)
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        
        cursor.execute("""
        SELECT * FROM vehicles WHERE id = ?
        """, (vehicle_id,))
        
        result = cursor.fetchone()
        return dict(result) if result else None
        
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return None
    finally:
        if conn:
            conn.close()

def get_all_vehicles(db_name: str = "electric_vehicles.db") -> list:
    """
    Retrieves all vehicles from the database.
    
    Args:
        db_name: Name of the SQLite database file
        
    Returns:
        List of dictionaries with vehicle data
    """
    conn = None
    try:
        conn = sqlite3.connect(db_name)
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        
        cursor.execute("SELECT * FROM vehicles")
        return [dict(row) for row in cursor.fetchall()]
        
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return []
    finally:
        if conn:
            conn.close()

def update_vehicle(
    vehicle_id: int,
    make: Optional[str] = None,
    model: Optional[str] = None,
    year: Optional[int] = None,
    mileage_per_charge: Optional[float] = None,
    battery_capacity_kwh: Optional[float] = None,
    price_usd: Optional[float] = None,
    db_name: str = "electric_vehicles.db"
) -> bool:
    """
    Updates vehicle information.
    
    Args:
        vehicle_id: ID of the vehicle to update
        make: Updated vehicle manufacturer
        model: Updated vehicle model
        year: Updated manufacturing year
        mileage_per_charge: Updated mileage on single charge
        battery_capacity_kwh: Updated battery capacity
        price_usd: Updated price
        db_name: Name of the SQLite database file
        
    Returns:
        True if update was successful, False otherwise
    """
    conn = None
    try:
        conn = sqlite3.connect(db_name)
        cursor = conn.cursor()
        
        # Build dynamic update query
        updates = []
        params = []
        
        if make is not None:
            updates.append("make = ?")
            params.append(make)
        if model is not None:
            updates.append("model = ?")
            params.append(model)
        if year is not None:
            updates.append("year = ?")
            params.append(year)
        if mileage_per_charge is not None:
            updates.append("mileage_per_charge = ?")
            params.append(mileage_per_charge)
        if battery_capacity_kwh is not None:
            updates.append("battery_capacity_kwh = ?")
            params.append(battery_capacity_kwh)
        if price_usd is not None:
            updates.append("price_usd = ?")
            params.append(price_usd)
            
        if not updates:
            return False
            
        query = f"UPDATE vehicles SET {', '.join(updates)} WHERE id = ?"
        params.append(vehicle_id)
        
        cursor.execute(query, params)
        conn.commit()
        return cursor.rowcount > 0
        
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return False
    finally:
        if conn:
            conn.close()

def delete_vehicle(
    vehicle_id: int,
    db_name: str = "electric_vehicles.db"
) -> bool:
    """
    Deletes a vehicle from the database.
    
    Args:
        vehicle_id: ID of the vehicle to delete
        db_name: Name of the SQLite database file
        
    Returns:
        True if deletion was successful, False otherwise
    """
    conn = None
    try:
        conn = sqlite3.connect(db_name)
        cursor = conn.cursor()
        
        cursor.execute("DELETE FROM vehicles WHERE id = ?", (vehicle_id,))
        conn.commit()
        return cursor.rowcount > 0
        
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return False
    finally:
        if conn:
            conn.close()

# Initialize the database when this module is imported
create_database()
```
