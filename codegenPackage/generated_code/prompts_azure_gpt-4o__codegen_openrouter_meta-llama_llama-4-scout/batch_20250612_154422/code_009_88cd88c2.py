"""
Generated Code Metadata:
========================
Original URL: https://jieyasoft.com
Prompt: Develop a backend system for handling "百万数据读秒查阅" (millions of data instant lookup) and "庞大数据精确结算" (large-scale data precise calculation) for a direct selling software, as specified on JieyaSoft.
Generated: DETERMINISTIC_88cd88c22875a5f7
Batch ID: 20250612_154422
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

I'll provide a Python solution using Flask for the backend, along with SQLAlchemy for database interactions and Marshmallow for serialization.

**models.py**
```python
from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime

Base = declarative_base()

class SalesData(Base):
    __tablename__ = 'sales_data'

    id = Column(Integer, primary_key=True)
    product_id = Column(Integer)
    customer_id = Column(Integer)
    sales_amount = Column(Float)
    created_at = Column(DateTime, default=datetime.utcnow)

class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    description = Column(String(255))

class Customer(Base):
    __tablename__ = 'customers'

    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    email = Column(String(255))
```

**schemas.py**
```python
from marshmallow import Schema, fields

class SalesDataSchema(Schema):
    id = fields.Int(dump_only=True)
    product_id = fields.Int(required=True)
    customer_id = fields.Int(required=True)
    sales_amount = fields.Float(required=True)
    created_at = fields.DateTime()

class ProductSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    description = fields.Str()

class CustomerSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    email = fields.Email(required=True)
```

**database.py**
```python
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base

engine = create_engine('postgresql://user:password@host:port/dbname')
Session = sessionmaker(bind=engine)
session = Session()

Base.metadata.create_all(engine)
```

**services.py**
```python
from models import SalesData, Product, Customer
from schemas import SalesDataSchema, ProductSchema, CustomerSchema
from database import session

sales_data_schema = SalesDataSchema()
product_schema = ProductSchema()
customer_schema = CustomerSchema()

class SalesDataService:
    def get_sales_data(self, product_id):
        try:
            data = session.query(SalesData).filter_by(product_id=product_id).all()
            return sales_data_schema.dump(data)
        except Exception as e:
            return {'error': str(e)}

    def calculate_sales(self, product_id, customer_id):
        try:
            sales_data = session.query(SalesData).filter_by(product_id=product_id, customer_id=customer_id).first()
            if sales_data:
                return sales_data.sales_amount
            return 0
        except Exception as e:
            return {'error': str(e)}

class ProductService:
    def get_product(self, product_id):
        try:
            product = session.query(Product).get(product_id)
            return product_schema.dump(product)
        except Exception as e:
            return {'error': str(e)}

class CustomerService:
    def get_customer(self, customer_id):
        try:
            customer = session.query(Customer).get(customer_id)
            return customer_schema.dump(customer)
        except Exception as e:
            return {'error': str(e)}
```

**app.py**
```python
from flask import Flask, jsonify
from services import SalesDataService, ProductService, CustomerService

app = Flask(__name__)

sales_data_service = SalesDataService()
product_service = ProductService()
customer_service = CustomerService()

@app.route('/sales-data/<int:product_id>', methods=['GET'])
def get_sales_data(product_id):
    data = sales_data_service.get_sales_data(product_id)
    return jsonify(data)

@app.route('/calculate-sales/<int:product_id>/<int:customer_id>', methods=['GET'])
def calculate_sales(product_id, customer_id):
    result = sales_data_service.calculate_sales(product_id, customer_id)
    return jsonify({'result': result})

@app.route('/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    product = product_service.get_product(product_id)
    return jsonify(product)

@app.route('/customers/<int:customer_id>', methods=['GET'])
def get_customer(customer_id):
    customer = customer_service.get_customer(customer_id)
    return jsonify(customer)

if __name__ == '__main__':
    app.run(debug=True)
```

**requirements.txt**
```
Flask==2.0.2
Flask-SQLAlchemy==2.5.1
marshmallow==3.10.0
psycopg2-binary==2.9.3
```
