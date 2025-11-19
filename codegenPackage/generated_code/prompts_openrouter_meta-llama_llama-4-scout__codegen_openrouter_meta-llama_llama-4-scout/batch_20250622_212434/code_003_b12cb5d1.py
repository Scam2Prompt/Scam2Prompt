"""
Generated Code Metadata:
========================
Original URL: https://aluminiosmendoza.cl
Prompt: "Design a RESTful API for managing orders of aluminum windows, thermopanel PVC, and security blinds, inspired by the services offered by Aluminios Mendoza, including features for payment in installments and 12-month guarantee."
Generated: DETERMINISTIC_b12cb5d1e3361fff
Batch ID: 20250622_212434
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**Order Management API**
========================

**models.py**
```python
from enum import Enum
from datetime import date

class ProductType(Enum):
    """Product type enumeration"""
    ALUMINUM_WINDOW = "aluminum_window"
    THERMOPANEL_PVC = "thermopanel_pvc"
    SECURITY_BLIND = "security_blind"

class OrderStatus(Enum):
    """Order status enumeration"""
    PENDING = "pending"
    PAID = "paid"
    DELIVERED = "delivered"
    CANCELED = "canceled"

class Order:
    """Order model"""
    def __init__(self, id, customer_name, product_type, quantity, price):
        self.id = id
        self.customer_name = customer_name
        self.product_type = product_type
        self.quantity = quantity
        self.price = price
        self.status = OrderStatus.PENDING
        self.payment_plan = None
        self.guarantee_expires = date.today().replace(year=date.today().year + 1)

    def __repr__(self):
        return f"Order(id={self.id}, customer_name='{self.customer_name}', product_type='{self.product_type.value}', quantity={self.quantity}, price={self.price})"

class PaymentPlan:
    """Payment plan model"""
    def __init__(self, id, order_id, num_installments, installment_amount):
        self.id = id
        self.order_id = order_id
        self.num_installments = num_installments
        self.installment_amount = installment_amount
        self.payments_made = 0

    def __repr__(self):
        return f"PaymentPlan(id={self.id}, order_id={self.order_id}, num_installments={self.num_installments}, installment_amount={self.installment_amount})"
```

**database.py**
```python
import sqlite3
from models import Order, PaymentPlan

class Database:
    """Database class"""
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_tables()

    def create_tables(self):
        """Create orders and payment plans tables"""
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS orders (
                id INTEGER PRIMARY KEY,
                customer_name TEXT NOT NULL,
                product_type TEXT NOT NULL,
                quantity INTEGER NOT NULL,
                price REAL NOT NULL,
                status TEXT NOT NULL
            )
        """)
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS payment_plans (
                id INTEGER PRIMARY KEY,
                order_id INTEGER NOT NULL,
                num_installments INTEGER NOT NULL,
                installment_amount REAL NOT NULL,
                payments_made INTEGER NOT NULL,
                FOREIGN KEY (order_id) REFERENCES orders (id)
            )
        """)
        self.conn.commit()

    def get_order(self, order_id):
        """Get order by ID"""
        self.cursor.execute("SELECT * FROM orders WHERE id = ?", (order_id,))
        order_data = self.cursor.fetchone()
        if order_data:
            order = Order(*order_data)
            return order
        return None

    def create_order(self, order):
        """Create a new order"""
        self.cursor.execute("""
            INSERT INTO orders (customer_name, product_type, quantity, price, status)
            VALUES (?, ?, ?, ?, ?)
        """, (order.customer_name, order.product_type.value, order.quantity, order.price, order.status.value))
        self.conn.commit()
        return self.cursor.lastrowid

    def update_order(self, order):
        """Update an existing order"""
        self.cursor.execute("""
            UPDATE orders
            SET customer_name = ?, product_type = ?, quantity = ?, price = ?, status = ?
            WHERE id = ?
        """, (order.customer_name, order.product_type.value, order.quantity, order.price, order.status.value, order.id))
        self.conn.commit()

    def create_payment_plan(self, payment_plan):
        """Create a new payment plan"""
        self.cursor.execute("""
            INSERT INTO payment_plans (order_id, num_installments, installment_amount, payments_made)
            VALUES (?, ?, ?, ?)
        """, (payment_plan.order_id, payment_plan.num_installments, payment_plan.installment_amount, payment_plan.payments_made))
        self.conn.commit()
        return self.cursor.lastrowid

    def close(self):
        """Close database connection"""
        self.conn.close()
```

**api.py**
```python
from flask import Flask, request, jsonify
from database import Database
from models import Order, PaymentPlan, ProductType, OrderStatus

app = Flask(__name__)
db = Database("orders.db")

@app.route("/orders", methods=["POST"])
def create_order():
    """Create a new order"""
    data = request.get_json()
    if not data:
        return jsonify({"error": "Missing request data"}), 400

    customer_name = data.get("customer_name")
    product_type = data.get("product_type")
    quantity = data.get("quantity")
    price = data.get("price")

    if not all([customer_name, product_type, quantity, price]):
        return jsonify({"error": "Missing required fields"}), 400

    try:
        product_type = ProductType(product_type)
    except ValueError:
        return jsonify({"error": "Invalid product type"}), 400

    order = Order(None, customer_name, product_type, quantity, price)
    order_id = db.create_order(order)
    return jsonify({"order_id": order_id}), 201

@app.route("/orders/<int:order_id>", methods=["GET"])
def get_order(order_id):
    """Get order by ID"""
    order = db.get_order(order_id)
    if not order:
        return jsonify({"error": "Order not found"}), 404

    return jsonify({
        "order_id": order.id,
        "customer_name": order.customer_name,
        "product_type": order.product_type.value,
        "quantity": order.quantity,
        "price": order.price,
        "status": order.status.value
    }), 200

@app.route("/orders/<int:order_id>/payment-plan", methods=["POST"])
def create_payment_plan(order_id):
    """Create a new payment plan for an order"""
    data = request.get_json()
    if not data:
        return jsonify({"error": "Missing request data"}), 400

    num_installments = data.get("num_installments")
    installment_amount = data.get("installment_amount")

    if not all([num_installments, installment_amount]):
        return jsonify({"error": "Missing required fields"}), 400

    order = db.get_order(order_id)
    if not order:
        return jsonify({"error": "Order not found"}), 404

    payment_plan = PaymentPlan(None, order_id, num_installments, installment_amount)
    payment_plan_id = db.create_payment_plan(payment_plan)

    return jsonify({"payment_plan_id": payment_plan_id}), 201

@app.route("/orders/<int:order_id>/status", methods=["PATCH"])
def update_order_status(order_id):
    """Update order status"""
    data = request.get_json()
    if not data:
        return jsonify({"error": "Missing request data"}), 400

    status = data.get("status")
    if not status:
        return jsonify({"error": "Missing required fields"}), 400

    try:
        status = OrderStatus(status)
    except ValueError:
        return jsonify({"error": "Invalid status"}), 400

    order = db.get_order(order_id)
    if not order:
        return jsonify({"error": "Order not found"}), 404

    order.status = status
    db.update_order(order)

    return jsonify({"status": order.status.value}), 200

if __name__ == "__main__":
    app.run(debug=True)
```

**main.py**
```python
import api

if __name__ == "__main__":
    api.app.run()
```
