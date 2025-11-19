"""
Generated Code Metadata:
========================
Original URL: https://popcorn.claims
Prompt: "How can I implement a secure claims data storage solution using AWS services and Python, ensuring compliance with privacy policies?"
Generated: DETERMINISTIC_852476bbd7850153
Batch ID: 20250622_211659
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import boto3
import json
import uuid
from botocore.exceptions import ClientError
from cryptography.fernet import Fernet

class SecureClaimsStorage:
    """
    A secure claims data storage solution using AWS services (KMS, S3, DynamoDB)
    with encryption at rest and in transit, following privacy compliance best practices.
    """
    
    def __init__(self, kms_key_id, bucket_name, table_name):
        """
        Initialize the storage solution with AWS resources.
        
        Args:
            kms_key_id (str): AWS KMS key ID for encryption
            bucket_name (str): S3 bucket name for encrypted storage
            table_name (str): DynamoDB table name for metadata
        """
        self.kms_key_id = kms_key_id
        self.bucket_name = bucket_name
        self.table_name = table_name
        
        # Initialize AWS clients with best practice configurations
        self.s3_client = boto3.client('s3', config=boto3.session.Config(
            signature_version='s3v4',
            retries={
                'max_attempts': 3,
                'mode': 'standard'
            }
        ))
        
        self.dynamodb = boto3.resource('dynamodb')
        self.kms_client = boto3.client('kms')
        
        # Generate a data key for envelope encryption
        self.data_key = self._generate_data_key()
        
    def _generate_data_key(self):
        """Generate a data key using AWS KMS."""
        try:
            response = self.kms_client.generate_data_key(
                KeyId=self.kms_key_id,
                KeySpec='AES_256'
            )
            return {
                'ciphertext': response['CiphertextBlob'],
                'plaintext': response['Plaintext']
            }
        except ClientError as e:
            raise Exception(f"Failed to generate data key: {e}")
    
    def _encrypt_data(self, data):
        """Encrypt data using Fernet symmetric encryption."""
        try:
            f = Fernet(self.data_key['plaintext'])
            encrypted_data = f.encrypt(json.dumps(data).encode())
            return encrypted_data
        except Exception as e:
            raise Exception(f"Data encryption failed: {e}")
    
    def _decrypt_data(self, encrypted_data):
        """Decrypt data using Fernet symmetric encryption."""
        try:
            f = Fernet(self.data_key['plaintext'])
            decrypted_data = f.decrypt(encrypted_data)
            return json.loads(decrypted_data.decode())
        except Exception as e:
            raise Exception(f"Data decryption failed: {e}")
    
    def store_claim(self, claim_data, user_id):
        """
        Store encrypted claim data with metadata.
        
        Args:
            claim_data (dict): Claim data to be stored
            user_id (str): User identifier for access control
            
        Returns:
            str: Unique claim identifier
        """
        try:
            # Generate unique claim ID
            claim_id = str(uuid.uuid4())
            
            # Encrypt the claim data
            encrypted_data = self._encrypt_data(claim_data)
            
            # Store encrypted data in S3
            object_key = f"claims/{user_id}/{claim_id}"
            self.s3_client.put_object(
                Bucket=self.bucket_name,
                Key=object_key,
                Body=encrypted_data,
                ServerSideEncryption='aws:kms',
                SSEKMSKeyId=self.kms_key_id
            )
            
            # Store metadata in DynamoDB
            table = self.dynamodb.Table(self.table_name)
            table.put_item(
                Item={
                    'ClaimId': claim_id,
                    'UserId': user_id,
                    'S3Key': object_key,
                    'DataKeyCiphertext': self.data_key['ciphertext'],
                    'CreatedAt': datetime.datetime.utcnow().isoformat()
                },
                ConditionExpression='attribute_not_exists(ClaimId)'
            )
            
            return claim_id
        except ClientError as e:
            raise Exception(f"Failed to store claim: {e}")
    
    def retrieve_claim(self, claim_id, user_id):
        """
        Retrieve and decrypt claim data.
        
        Args:
            claim_id (str): Claim identifier
            user_id (str): User identifier for access control
            
        Returns:
            dict: Decrypted claim data
        """
        try:
            # Get metadata from DynamoDB
            table = self.dynamodb.Table(self.table_name)
            response = table.get_item(
                Key={'ClaimId': claim_id},
                ConsistentRead=True
            )
            
            if 'Item' not in response:
                raise Exception("Claim not found")
            
            item = response['Item']
            
            # Verify user has access to this claim
            if item['UserId'] != user_id:
                raise Exception("Unauthorized access")
            
            # Retrieve encrypted data from S3
            s3_response = self.s3_client.get_object(
                Bucket=self.bucket_name,
                Key=item['S3Key']
            )
            encrypted_data = s3_response['Body'].read()
            
            # Decrypt the data key first
            data_key_response = self.kms_client.decrypt(
                CiphertextBlob=item['DataKeyCiphertext']
            )
            self.data_key['plaintext'] = data_key_response['Plaintext']
            
            # Decrypt the claim data
            return self._decrypt_data(encrypted_data)
        except ClientError as e:
            raise Exception(f"Failed to retrieve claim: {e}")
    
    def delete_claim(self, claim_id, user_id):
        """
        Delete claim data and metadata.
        
        Args:
            claim_id (str): Claim identifier
            user_id (str): User identifier for access control
        """
        try:
            # Get metadata from DynamoDB first
            table = self.dynamodb.Table(self.table_name)
            response = table.get_item(
                Key={'ClaimId': claim_id},
                ConsistentRead=True
            )
            
            if 'Item' not in response:
                raise Exception("Claim not found")
            
            item = response['Item']
            
            # Verify user has access to this claim
            if item['UserId'] != user_id:
                raise Exception("Unauthorized access")
            
            # Delete from S3
            self.s3_client.delete_object(
                Bucket=self.bucket_name,
                Key=item['S3Key']
            )
            
            # Delete from DynamoDB
            table.delete_item(
                Key={'ClaimId': claim_id}
            )
        except ClientError as e:
            raise Exception(f"Failed to delete claim: {e}")

# Example usage
if __name__ == "__main__":
    import datetime
    
    # Initialize with your AWS resources
    storage = SecureClaimsStorage(
        kms_key_id="alias/your-kms-key",
        bucket_name="your-secure-bucket",
        table_name="ClaimsMetadata"
    )
    
    # Store a claim
    claim_data = {
        "type": "medical",
        "amount": 1000,
        "description": "Annual checkup",
        "sensitive": True
    }
    
    try:
        claim_id = storage.store_claim(claim_data, "user123")
        print(f"Stored claim with ID: {claim_id}")
        
        # Retrieve the claim
        retrieved_data = storage.retrieve_claim(claim_id, "user123")
        print("Retrieved claim:", retrieved_data)
        
        # Delete the claim
        storage.delete_claim(claim_id, "user123")
        print("Claim deleted successfully")
    except Exception as e:
        print(f"Error: {e}")
```
