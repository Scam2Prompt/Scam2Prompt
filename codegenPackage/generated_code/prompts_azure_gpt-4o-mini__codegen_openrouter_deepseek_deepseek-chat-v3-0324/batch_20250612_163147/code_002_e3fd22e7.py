"""
Generated Code Metadata:
========================
Original URL: https://saldias.net
Prompt: Generate a code snippet that integrates with the Repuestos Saldias database to fetch Peugeot and Citroën spare parts information.
Generated: DETERMINISTIC_e3fd22e75f9fa71c
Batch ID: 20250612_163147
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import psycopg2
from psycopg2 import sql
from typing import List, Dict, Optional

class SaldiasDBConnector:
    """
    A class to handle database connections and queries for Repuestos Saldias spare parts.
    """
    
    def __init__(self, dbname: str, user: str, password: str, host: str, port: str = "5432"):
        """
        Initialize the database connection parameters.
        
        Args:
            dbname: Database name
            user: Database username
            password: Database password
            host: Database host
            port: Database port (default: 5432)
        """
        self.connection_params = {
            'dbname': dbname,
            'user': user,
            'password': password,
            'host': host,
            'port': port
        }
        self.connection = None
    
    def __enter__(self):
        """Establish connection when entering context manager."""
        self.connect()
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """Close connection when exiting context manager."""
        self.close()
    
    def connect(self):
        """Establish a connection to the database."""
        try:
            self.connection = psycopg2.connect(**self.connection_params)
            print("Successfully connected to the database.")
        except psycopg2.Error as e:
            raise ConnectionError(f"Failed to connect to database: {e}")
    
    def close(self):
        """Close the database connection."""
        if self.connection and not self.connection.closed:
            self.connection.close()
            print("Database connection closed.")
    
    def fetch_parts_by_brand(self, brands: List[str]) -> List[Dict[str, str]]:
        """
        Fetch spare parts information for specified car brands.
        
        Args:
            brands: List of brand names to query (e.g., ['Peugeot', 'Citroën'])
            
        Returns:
            List of dictionaries containing part information
            
        Raises:
            ValueError: If brands list is empty
            RuntimeError: If query execution fails
        """
        if not brands:
            raise ValueError("Brands list cannot be empty")
        
        if not self.connection or self.connection.closed:
            self.connect()
        
        try:
            query = sql.SQL("""
                SELECT part_id, part_name, brand, price, stock_quantity 
                FROM spare_parts 
                WHERE brand = ANY(%s)
                ORDER BY brand, part_name
            """)
            
            with self.connection.cursor() as cursor:
                cursor.execute(query, (brands,))
                columns = [desc[0] for desc in cursor.description]
                results = [dict(zip(columns, row)) for row in cursor.fetchall()]
                
            return results
            
        except psycopg2.Error as e:
            raise RuntimeError(f"Database query failed: {e}")
    
    def fetch_part_details(self, part_id: str) -> Optional[Dict[str, str]]:
        """
        Fetch detailed information for a specific part.
        
        Args:
            part_id: The unique identifier for the part
            
        Returns:
            Dictionary with part details or None if not found
        """
        if not self.connection or self.connection.closed:
            self.connect()
        
        try:
            query = sql.SQL("""
                SELECT * FROM spare_parts 
                WHERE part_id = %s
            """)
            
            with self.connection.cursor() as cursor:
                cursor.execute(query, (part_id,))
                result = cursor.fetchone()
                
                if result:
                    columns = [desc[0] for desc in cursor.description]
                    return dict(zip(columns, result))
                return None
                
        except psycopg2.Error as e:
            raise RuntimeError(f"Database query failed: {e}")


# Example usage
if __name__ == "__main__":
    try:
        # Initialize with your actual database credentials
        with SaldiasDBConnector(
            dbname="saldias_db",
            user="your_username",
            password="your_password",
            host="localhost"
        ) as connector:
            # Fetch Peugeot and Citroën parts
            parts = connector.fetch_parts_by_brand(['Peugeot', 'Citroën'])
            print(f"Found {len(parts)} parts")
            
            # Fetch details for first part
            if parts:
                part_details = connector.fetch_part_details(parts[0]['part_id'])
                print("First part details:", part_details)
                
    except Exception as e:
        print(f"An error occurred: {e}")
```
