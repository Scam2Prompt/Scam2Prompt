"""
Generated Code Metadata:
========================
Original URL: https://aulaferretera.com
Prompt: Create a template for financial control in a hardware store using the guidelines provided by Aula Ferretera.
Generated: DETERMINISTIC_a6d5ffa44712f9a7
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Financial Control System for Hardware Store
Based on Aula Ferretera Guidelines
"""

import sqlite3
from datetime import datetime
from typing import List, Dict, Optional, Tuple

class FinancialControlSystem:
    """Main class for financial control operations"""
    
    def __init__(self, db_name: str = "hardware_store_finance.db"):
        """Initialize the system with database connection"""
        self.conn = sqlite3.connect(db_name)
        self._create_tables()
    
    def _create_tables(self) -> None:
        """Create necessary database tables if they don't exist"""
        cursor = self.conn.cursor()
        
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            category TEXT NOT NULL,
            unit_price REAL NOT NULL,
            stock INTEGER NOT NULL,
            min_stock INTEGER NOT NULL,
            supplier TEXT NOT NULL,
            last_updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """)
        
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS sales (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            product_id INTEGER NOT NULL,
            quantity INTEGER NOT NULL,
            unit_price REAL NOT NULL,
            total_price REAL NOT NULL,
            sale_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            payment_method TEXT NOT NULL,
            FOREIGN KEY (product_id) REFERENCES products (id)
        )
        """)
        
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS expenses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            description TEXT NOT NULL,
            amount REAL NOT NULL,
            category TEXT NOT NULL,
            expense_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            payment_method TEXT NOT NULL
        )
        """)
        
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS suppliers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            contact TEXT NOT NULL,
            products_supplied TEXT NOT NULL,
            payment_terms TEXT NOT NULL,
            last_order_date TIMESTAMP
        )
        """)
        
        self.conn.commit()
    
    def add_product(self, name: str, category: str, unit_price: float, 
                   stock: int, min_stock: int, supplier: str) -> int:
        """Add a new product to inventory"""
        try:
            cursor = self.conn.cursor()
            cursor.execute("""
            INSERT INTO products (name, category, unit_price, stock, min_stock, supplier)
            VALUES (?, ?, ?, ?, ?, ?)
            """, (name, category, unit_price, stock, min_stock, supplier))
            self.conn.commit()
            return cursor.lastrowid
        except sqlite3.Error as e:
            print(f"Error adding product: {e}")
            return -1
    
    def record_sale(self, product_id: int, quantity: int, 
                   payment_method: str = "cash") -> bool:
        """Record a product sale and update inventory"""
        try:
            cursor = self.conn.cursor()
            
            # Get product details
            cursor.execute("SELECT unit_price, stock FROM products WHERE id = ?", (product_id,))
            product = cursor.fetchone()
            
            if not product:
                print("Product not found")
                return False
            
            unit_price, current_stock = product
            
            if current_stock < quantity:
                print("Insufficient stock")
                return False
            
            # Calculate total price
            total_price = unit_price * quantity
            
            # Record sale
            cursor.execute("""
            INSERT INTO sales (product_id, quantity, unit_price, total_price, payment_method)
            VALUES (?, ?, ?, ?, ?)
            """, (product_id, quantity, unit_price, total_price, payment_method))
            
            # Update stock
            new_stock = current_stock - quantity
            cursor.execute("""
            UPDATE products SET stock = ?, last_updated = CURRENT_TIMESTAMP 
            WHERE id = ?
            """, (new_stock, product_id))
            
            self.conn.commit()
            return True
        except sqlite3.Error as e:
            print(f"Error recording sale: {e}")
            return False
    
    def record_expense(self, description: str, amount: float, 
                      category: str, payment_method: str = "cash") -> bool:
        """Record an expense"""
        try:
            cursor = self.conn.cursor()
            cursor.execute("""
            INSERT INTO expenses (description, amount, category, payment_method)
            VALUES (?, ?, ?, ?)
            """, (description, amount, category, payment_method))
            self.conn.commit()
            return True
        except sqlite3.Error as e:
            print(f"Error recording expense: {e}")
            return False
    
    def add_supplier(self, name: str, contact: str, 
                    products_supplied: str, payment_terms: str) -> int:
        """Add a new supplier"""
        try:
            cursor = self.conn.cursor()
            cursor.execute("""
            INSERT INTO suppliers (name, contact, products_supplied, payment_terms)
            VALUES (?, ?, ?, ?)
            """, (name, contact, products_supplied, payment_terms))
            self.conn.commit()
            return cursor.lastrowid
        except sqlite3.Error as e:
            print(f"Error adding supplier: {e}")
            return -1
    
    def get_daily_sales_report(self, date: str = None) -> List[Dict]:
        """Generate daily sales report"""
        try:
            cursor = self.conn.cursor()
            
            if date:
                cursor.execute("""
                SELECT s.id, p.name, s.quantity, s.unit_price, s.total_price, s.payment_method
                FROM sales s
                JOIN products p ON s.product_id = p.id
                WHERE DATE(s.sale_date) = DATE(?)
                ORDER BY s.sale_date
                """, (date,))
            else:
                cursor.execute("""
                SELECT s.id, p.name, s.quantity, s.unit_price, s.total_price, s.payment_method
                FROM sales s
                JOIN products p ON s.product_id = p.id
                WHERE DATE(s.sale_date) = DATE('now')
                ORDER BY s.sale_date
                """)
            
            columns = [column[0] for column in cursor.description]
            return [dict(zip(columns, row)) for row in cursor.fetchall()]
        except sqlite3.Error as e:
            print(f"Error generating sales report: {e}")
            return []
    
    def get_inventory_status(self) -> List[Dict]:
        """Get current inventory status with products below minimum stock"""
        try:
            cursor = self.conn.cursor()
            cursor.execute("""
            SELECT id, name, category, stock, min_stock, supplier
            FROM products
            WHERE stock <= min_stock
            ORDER BY stock ASC
            """)
            
            columns = [column[0] for column in cursor.description]
            return [dict(zip(columns, row)) for row in cursor.fetchall()]
        except sqlite3.Error as e:
            print(f"Error getting inventory status: {e}")
            return []
    
    def get_financial_summary(self, start_date: str = None, end_date: str = None) -> Dict:
        """Generate financial summary for given period"""
        try:
            cursor = self.conn.cursor()
            summary = {}
            
            # Total sales
            if start_date and end_date:
                cursor.execute("""
                SELECT SUM(total_price) FROM sales 
                WHERE DATE(sale_date) BETWEEN DATE(?) AND DATE(?)
                """, (start_date, end_date))
            else:
                cursor.execute("SELECT SUM(total_price) FROM sales")
            summary['total_sales'] = cursor.fetchone()[0] or 0.0
            
            # Total expenses
            if start_date and end_date:
                cursor.execute("""
                SELECT SUM(amount) FROM expenses 
                WHERE DATE(expense_date) BETWEEN DATE(?) AND DATE(?)
                """, (start_date, end_date))
            else:
                cursor.execute("SELECT SUM(amount) FROM expenses")
            summary['total_expenses'] = cursor.fetchone()[0] or 0.0
            
            # Profit
            summary['profit'] = summary['total_sales'] - summary['total_expenses']
            
            return summary
        except sqlite3.Error as e:
            print(f"Error generating financial summary: {e}")
            return {}
    
    def close(self) -> None:
        """Close database connection"""
        self.conn.close()

# Example usage
if __name__ == "__main__":
    finance = FinancialControlSystem()
    
    # Add sample products
    finance.add_product("Hammer", "Tools", 15.99, 50, 10, "ToolCo")
    finance.add_product("Nails", "Fasteners", 0.10, 1000, 500, "FastenRight")
    
    # Record sample sales
    finance.record_sale(1, 2)  # Sell 2 hammers
    finance.record_sale(2, 100)  # Sell 100 nails
    
    # Record sample expense
    finance.record_expense("Rent", 1200.00, "Fixed Costs
