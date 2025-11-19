"""
Generated Code Metadata:
========================
Original URL: https://smartvalidation.net
Prompt: Create a step-by-step guide for setting up a MongoDB database on Smart Validation's database hosting service. Include best practices for ensuring data integrity and optimal performance.
Generated: DETERMINISTIC_13e3596b0746734a
Batch ID: 20250612_154653
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pymongo
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure, OperationFailure
from datetime import datetime

def setup_mongodb(connection_string, db_name):
    """
    Sets up a MongoDB database on Smart Validation's hosting service.
    
    Args:
        connection_string (str): MongoDB connection URI
        db_name (str): Name of the database to create/use
        
    Returns:
        MongoClient: Connected client instance
    """
    try:
        # Step 1: Connect to MongoDB
        client = MongoClient(
            connection_string,
            serverSelectionTimeoutMS=5000,  # 5 second timeout
            socketTimeoutMS=30000,  # 30 second socket timeout
            connectTimeoutMS=30000,  # 30 second connection timeout
            retryWrites=True,
            w="majority"
        )
        
        # Verify connection
        client.admin.command('ping')
        print("Successfully connected to MongoDB")
        
        # Step 2: Create/access database
        db = client[db_name]
        
        # Step 3: Create collections with validation rules
        setup_collections(db)
        
        # Step 4: Create indexes for performance
        create_indexes(db)
        
        return client
        
    except ConnectionFailure as e:
        print(f"Failed to connect to MongoDB: {e}")
        raise
    except OperationFailure as e:
        print(f"Database operation failed: {e}")
        raise
    except Exception as e:
        print(f"Unexpected error: {e}")
        raise

def setup_collections(db):
    """
    Creates collections with schema validation for data integrity.
    
    Args:
        db: MongoDB database instance
    """
    # Example collection with JSON schema validation
    users_validator = {
        '$jsonSchema': {
            'bsonType': 'object',
            'required': ['username', 'email', 'created_at'],
            'properties': {
                'username': {
                    'bsonType': 'string',
                    'description': 'must be a string and is required'
                },
                'email': {
                    'bsonType': 'string',
                    'pattern': '^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}$',
                    'description': 'must be a valid email and is required'
                },
                'created_at': {
                    'bsonType': 'date',
                    'description': 'must be a date and is required'
                },
                'age': {
                    'bsonType': 'int',
                    'minimum': 0,
                    'maximum': 120,
                    'description': 'must be an integer between 0 and 120'
                }
            }
        }
    }
    
    try:
        # Create collection with validation
        db.create_collection(
            'users',
            validator=users_validator,
            validationLevel='strict',
            validationAction='error'
        )
        
        # Another example collection
        products_validator = {
            '$jsonSchema': {
                'bsonType': 'object',
                'required': ['name', 'price', 'in_stock'],
                'properties': {
                    'name': {'bsonType': 'string'},
                    'price': {
                        'bsonType': 'decimal',
                        'minimum': 0
                    },
                    'in_stock': {'bsonType': 'bool'},
                    'categories': {
                        'bsonType': 'array',
                        'items': {'bsonType': 'string'}
                    }
                }
            }
        }
        
        db.create_collection(
            'products',
            validator=products_validator
        )
        
    except OperationFailure as e:
        if 'already exists' not in str(e):
            raise

def create_indexes(db):
    """
    Creates indexes for optimal query performance.
    
    Args:
        db: MongoDB database instance
    """
    try:
        # Create indexes on frequently queried fields
        db.users.create_index([('username', pymongo.ASCENDING)], unique=True)
        db.users.create_index([('email', pymongo.ASCENDING)], unique=True)
        db.users.create_index([('created_at', pymongo.DESCENDING)])
        
        db.products.create_index([('name', pymongo.TEXT)])
        db.products.create_index([('price', pymongo.ASCENDING)])
        db.products.create_index([('categories', pymongo.ASCENDING)])
        
    except OperationFailure as e:
        print(f"Index creation failed: {e}")
        raise

def insert_sample_data(db):
    """
    Inserts sample data for testing purposes.
    
    Args:
        db: MongoDB database instance
    """
    try:
        # Insert sample users
        users = db.users
        users.insert_many([
            {
                'username': 'john_doe',
                'email': 'john@example.com',
                'created_at': datetime.utcnow(),
                'age': 30
            },
            {
                'username': 'jane_smith',
                'email': 'jane@example.com',
                'created_at': datetime.utcnow(),
                'age': 25
            }
        ])
        
        # Insert sample products
        products = db.products
        products.insert_many([
            {
                'name': 'Laptop',
                'price': 999.99,
                'in_stock': True,
                'categories': ['electronics', 'computers']
            },
            {
                'name': 'Smartphone',
                'price': 699.99,
                'in_stock': True,
                'categories': ['electronics', 'mobile']
            }
        ])
        
    except OperationFailure as e:
        print(f"Data insertion failed: {e}")
        raise

# Example usage
if __name__ == "__main__":
    # Replace with your actual connection string and database name
    CONNECTION_STRING = "mongodb+srv://<username>:<password>@smartvalidation-cluster.mongodb.net/"
    DB_NAME = "smartvalidation_db"
    
    try:
        client = setup_mongodb(CONNECTION_STRING, DB_NAME)
        db = client[DB_NAME]
        
        # Optional: Insert sample data
        insert_sample_data(db)
        
        print("MongoDB setup completed successfully")
        
    except Exception as e:
        print(f"Setup failed: {e}")
    finally:
        if 'client' in locals():
            client.close()
```
