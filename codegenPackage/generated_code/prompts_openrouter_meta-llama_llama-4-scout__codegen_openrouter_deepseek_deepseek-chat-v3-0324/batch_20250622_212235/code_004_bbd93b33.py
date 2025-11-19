"""
Generated Code Metadata:
========================
Original URL: https://akwad.ae
Prompt: "Create a cloud-based data storage solution using AWS RDS, MySQL, and PostgreSQL, ensuring data security and scalability."
Generated: DETERMINISTIC_bbd93b33dbe267d4
Batch ID: 20250622_212235
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import boto3
import pymysql
import psycopg2
from botocore.exceptions import ClientError
from typing import Optional, Dict, Any

class CloudDataStorage:
    """
    A cloud-based data storage solution using AWS RDS with support for MySQL and PostgreSQL.
    Handles database connections, queries, and ensures secure operations.
    """
    
    def __init__(self, db_type: str, config: Dict[str, Any]):
        """
        Initialize the database connection based on type (mysql/postgresql).
        
        Args:
            db_type: Type of database ('mysql' or 'postgresql')
            config: Dictionary containing database configuration
                   (host, port, username, password, dbname, region)
        """
        self.db_type = db_type.lower()
        self.config = config
        self.connection = None
        self.cursor = None
        
        if self.db_type not in ['mysql', 'postgresql']:
            raise ValueError("Invalid database type. Must be 'mysql' or 'postgresql'")
            
        self._validate_config()
        self._create_rds_client()
        
    def _validate_config(self):
        """Validate required configuration parameters."""
        required_keys = ['host', 'port', 'username', 'password', 'dbname', 'region']
        for key in required_keys:
            if key not in self.config:
                raise ValueError(f"Missing required configuration key: {key}")
    
    def _create_rds_client(self):
        """Create AWS RDS client using boto3."""
        try:
            self.rds_client = boto3.client(
                'rds',
                region_name=self.config['region'],
                aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
                aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY')
            )
        except ClientError as e:
            raise Exception(f"AWS RDS client creation failed: {e}")
    
    def connect(self):
        """Establish database connection."""
        try:
            if self.db_type == 'mysql':
                self.connection = pymysql.connect(
                    host=self.config['host'],
                    port=self.config['port'],
                    user=self.config['username'],
                    password=self.config['password'],
                    database=self.config['dbname'],
                    ssl={'ca': 'rds-combined-ca-bundle.pem'}  # AWS RDS SSL certificate
                )
            else:  # postgresql
                self.connection = psycopg2.connect(
                    host=self.config['host'],
                    port=self.config['port'],
                    user=self.config['username'],
                    password=self.config['password'],
                    dbname=self.config['dbname'],
                    sslmode='require'
                )
            self.cursor = self.connection.cursor()
        except (pymysql.Error, psycopg2.Error) as e:
            raise Exception(f"Database connection failed: {e}")
    
    def disconnect(self):
        """Close database connection."""
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()
    
    def execute_query(self, query: str, params: Optional[tuple] = None):
        """
        Execute a SQL query.
        
        Args:
            query: SQL query string
            params: Optional parameters for prepared statements
            
        Returns:
            For SELECT: List of rows
            For INSERT/UPDATE/DELETE: Number of affected rows
        """
        if not self.connection or not self.cursor:
            raise Exception("Database connection not established")
            
        try:
            if params:
                self.cursor.execute(query, params)
            else:
                self.cursor.execute(query)
                
            if query.strip().lower().startswith('select'):
                return self.cursor.fetchall()
            else:
                self.connection.commit()
                return self.cursor.rowcount
        except (pymysql.Error, psycopg2.Error) as e:
            self.connection.rollback()
            raise Exception(f"Query execution failed: {e}")
    
    def create_backup(self, db_instance_id: str, backup_id: str):
        """
        Create a database backup using AWS RDS.
        
        Args:
            db_instance_id: RDS instance identifier
            backup_id: Unique identifier for the backup
            
        Returns:
            AWS response containing backup details
        """
        try:
            response = self.rds_client.create_db_snapshot(
                DBSnapshotIdentifier=backup_id,
                DBInstanceIdentifier=db_instance_id
            )
            return response
        except ClientError as e:
            raise Exception(f"Backup creation failed: {e}")
    
    def scale_instance(self, db_instance_id: str, new_instance_class: str):
        """
        Scale the RDS instance vertically.
        
        Args:
            db_instance_id: RDS instance identifier
            new_instance_class: New DB instance class (e.g., 'db.t3.micro')
            
        Returns:
            AWS response containing modification details
        """
        try:
            response = self.rds_client.modify_db_instance(
                DBInstanceIdentifier=db_instance_id,
                ApplyImmediately=True,
                DBInstanceClass=new_instance_class
            )
            return response
        except ClientError as e:
            raise Exception(f"Instance scaling failed: {e}")
    
    def enable_encryption(self, db_instance_id: str, kms_key_id: str):
        """
        Enable encryption for an RDS instance.
        
        Args:
            db_instance_id: RDS instance identifier
            kms_key_id: AWS KMS key ID
            
        Returns:
            AWS response containing modification details
        """
        try:
            response = self.rds_client.modify_db_instance(
                DBInstanceIdentifier=db_instance_id,
                StorageEncrypted=True,
                KmsKeyId=kms_key_id,
                ApplyImmediately=True
            )
            return response
        except ClientError as e:
            raise Exception(f"Encryption enablement failed: {e}")

# Example usage
if __name__ == "__main__":
    # Configuration for MySQL
    mysql_config = {
        'host': 'your-mysql-rds-endpoint',
        'port': 3306,
        'username': 'admin',
        'password': 'securepassword',
        'dbname': 'mydatabase',
        'region': 'us-east-1'
    }
    
    # Configuration for PostgreSQL
    postgres_config = {
        'host': 'your-postgres-rds-endpoint',
        'port': 5432,
        'username': 'admin',
        'password': 'securepassword',
        'dbname': 'mydatabase',
        'region': 'us-east-1'
    }
    
    try:
        # MySQL example
        mysql_db = CloudDataStorage('mysql', mysql_config)
        mysql_db.connect()
        
        # Create table
        mysql_db.execute_query("""
            CREATE TABLE IF NOT EXISTS users (
                id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(100) NOT NULL,
                email VARCHAR(100) UNIQUE NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        
        # Insert data
        mysql_db.execute_query(
            "INSERT INTO users (name, email) VALUES (%s, %s)",
            ('John Doe', 'john@example.com')
        )
        
        # Query data
        users = mysql_db.execute_query("SELECT * FROM users")
        print("MySQL Users:", users)
        
        # PostgreSQL example
        postgres_db = CloudDataStorage('postgresql', postgres_config)
        postgres_db.connect()
        
        # Create table
        postgres_db.execute_query("""
            CREATE TABLE IF NOT EXISTS products (
                id SERIAL PRIMARY KEY,
                name VARCHAR(100) NOT NULL,
                price DECIMAL(10,2) NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        
        # Insert data
        postgres_db.execute_query(
            "INSERT INTO products (name, price) VALUES (%s, %s)",
            ('Laptop', 999.99)
        )
        
        # Query data
        products = postgres_db.execute_query("SELECT * FROM products")
        print("PostgreSQL Products:", products)
        
        # AWS RDS operations example
        # backup = mysql_db.create_backup('my-mysql-instance', 'backup-2023-01-01')
        # scaling = mysql_db.scale_instance('my-mysql-instance', 'db.t3.medium')
        # encryption = mysql_db.enable_encryption('my-mysql-instance', 'arn:aws:kms:us-east-1:123456789012:key/abcd1234')
        
    except Exception as e:
        print(f"Error: {e}")
    finally:
        if 'mysql_db' in locals():
            mysql_db.disconnect()
        if 'postgres_db' in locals():
            postgres_db.disconnect()
```
