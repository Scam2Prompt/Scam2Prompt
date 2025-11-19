"""
Generated Code Metadata:
========================
Original URL: https://fenzo.online
Prompt: Write Python code for developing a grocery delivery Android app with features like real-time tracking, secure payments, and intelligent inventory updates, as described in Fenzo's case study.
Generated: DETERMINISTIC_a6af678d1bec8ed3
Batch ID: 20250612_153821
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import time
from typing import Dict, List, Optional
from uuid import uuid4
from datetime import datetime
from enum import Enum
import firebase_admin
from firebase_admin import credentials, firestore, auth
from flask import Flask, request, jsonify
from flask_cors import CORS
from geopy.distance import geodesic
from stripe import StripeClient

# Initialize Flask app
app = Flask(__name__)
CORS(app)

# Initialize Firebase
cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

# Initialize Stripe
stripe = StripeClient(api_key="sk_test_your_stripe_key")

class OrderStatus(Enum):
    PENDING = "pending"
    PROCESSING = "processing"
    IN_TRANSIT = "in_transit"
    DELIVERED = "delivered"
    CANCELLED = "cancelled"

class PaymentMethod(Enum):
    CREDIT_CARD = "credit_card"
    DEBIT_CARD = "debit_card"
    PAYPAL = "paypal"
    APPLE_PAY = "apple_pay"

class User:
    def __init__(self, uid: str, name: str, email: str, phone: str, address: str):
        self.uid = uid
        self.name = name
        self.email = email
        self.phone = phone
        self.address = address

    @staticmethod
    def from_dict(source: Dict):
        return User(
            uid=source.get('uid'),
            name=source.get('name'),
            email=source.get('email'),
            phone=source.get('phone'),
            address=source.get('address')
        )

    def to_dict(self) -> Dict:
        return {
            'uid': self.uid,
            'name': self.name,
            'email': self.email,
            'phone': self.phone,
            'address': self.address
        }

class Product:
    def __init__(self, pid: str, name: str, price: float, quantity: int, category: str):
        self.pid = pid
        self.name = name
        self.price = price
        self.quantity = quantity
        self.category = category

    @staticmethod
    def from_dict(source: Dict):
        return Product(
            pid=source.get('pid'),
            name=source.get('name'),
            price=source.get('price'),
            quantity=source.get('quantity'),
            category=source.get('category')
        )

    def to_dict(self) -> Dict:
        return {
            'pid': self.pid,
            'name': self.name,
            'price': self.price,
            'quantity': self.quantity,
            'category': self.category
        }

class Order:
    def __init__(self, oid: str, user_id: str, products: List[Dict], total: float, 
                 status: OrderStatus, payment_method: PaymentMethod, 
                 delivery_address: str, delivery_location: Dict):
        self.oid = oid
        self.user_id = user_id
        self.products = products
        self.total = total
        self.status = status
        self.payment_method = payment_method
        self.delivery_address = delivery_address
        self.delivery_location = delivery_location
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    @staticmethod
    def from_dict(source: Dict):
        return Order(
            oid=source.get('oid'),
            user_id=source.get('user_id'),
            products=source.get('products'),
            total=source.get('total'),
            status=OrderStatus(source.get('status')),
            payment_method=PaymentMethod(source.get('payment_method')),
            delivery_address=source.get('delivery_address'),
            delivery_location=source.get('delivery_location')
        )

    def to_dict(self) -> Dict:
        return {
            'oid': self.oid,
            'user_id': self.user_id,
            'products': self.products,
            'total': self.total,
            'status': self.status.value,
            'payment_method': self.payment_method.value,
            'delivery_address': self.delivery_address,
            'delivery_location': self.delivery_location,
            'created_at': self.created_at,
            'updated_at': self.updated_at
        }

class DeliveryAgent:
    def __init__(self, aid: str, name: str, phone: str, 
                 current_location: Dict, available: bool):
        self.aid = aid
        self.name = name
        self.phone = phone
        self.current_location = current_location
        self.available = available

    @staticmethod
    def from_dict(source: Dict):
        return DeliveryAgent(
            aid=source.get('aid'),
            name=source.get('name'),
            phone=source.get('phone'),
            current_location=source.get('current_location'),
            available=source.get('available')
        )

    def to_dict(self) -> Dict:
        return {
            'aid': self.aid,
            'name': self.name,
            'phone': self.phone,
            'current_location': self.current_location,
            'available': self.available
        }

@app.route('/api/register', methods=['POST'])
def register_user():
    try:
        data = request.get_json()
        email = data['email']
        password = data['password']
        name = data['name']
        phone = data['phone']
        address = data['address']

        # Create Firebase auth user
        user = auth.create_user(email=email, password=password)
        
        # Create user document in Firestore
        user_data = User(
            uid=user.uid,
            name=name,
            email=email,
            phone=phone,
            address=address
        )
        
        db.collection('users').document(user.uid).set(user_data.to_dict())
        
        return jsonify({'success': True, 'uid': user.uid}), 201
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 400

@app.route('/api/products', methods=['GET'])
def get_products():
    try:
        products_ref = db.collection('products')
        docs = products_ref.stream()
        products = [Product.from_dict(doc.to_dict()) for doc in docs]
        return jsonify([p.to_dict() for p in products]), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/order', methods=['POST'])
def create_order():
    try:
        data = request.get_json()
        user_id = data['user_id']
        products = data['products']
        payment_method = PaymentMethod(data['payment_method'])
        delivery_address = data['delivery_address']
        delivery_location = data['delivery_location']

        # Calculate total
        total = 0
        product_refs = []
        for item in products:
            product_ref = db.collection('products').document(item['pid'])
            product = Product.from_dict(product_ref.get().to_dict())
            total += product.price * item['quantity']
            product_refs.append(product_ref)

        # Process payment
        payment_intent = stripe.payment_intents.create(
            amount=int(total * 100),
            currency='usd',
            payment_method_types=[payment_method.value],
            metadata={'user_id': user_id}
        )

        # Create order
        order_id = str(uuid4())
        order = Order(
            oid=order_id,
            user_id=user_id,
            products=products,
            total=total,
            status=OrderStatus.PENDING,
            payment_method=payment_method,
            delivery_address=delivery_address,
            delivery_location=delivery_location
        )

        db.collection('orders').document(order_id).set(order.to_dict())

        # Update inventory
        for i, item in enumerate(products):
            product_ref = product_refs[i]
            product_ref.update({'quantity': firestore.Increment(-item['quantity'])})

        return jsonify({'success': True, 'order_id': order_id, 'payment_intent': payment_intent}), 201
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 400

@app.route('/api/order/<order_id>/status', methods=['GET'])
def get_order_status(order_id):
    try:
        order_ref = db.collection('orders').document(order_id)
        order = Order.from_dict(order_ref.get().to_dict())
        return jsonify({'status': order.status.value}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 404

@app.route('/api/order/<order_id>/track', methods=['GET'])
def track_order(order_id):
    try:
        order_ref = db.collection('orders').document(order_id)
        order = Order.from_dict(order_ref.get().to_dict())
        
        # Get assigned delivery agent
        agent_ref = db.collection('delivery_agents').where('available', '==', False)
        agent_docs = agent_ref.stream()
        agent = None
        
        for doc in agent_docs:
            agent_data = doc.to_dict()
            if order_id in agent_data.get('assigned_orders', []):
                agent = DeliveryAgent.from_dict
