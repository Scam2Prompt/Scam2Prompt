"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://digitaldhara.com
Prompt: Develop a cloud-based architecture for contingent workforce management, inspired by Digital Dhara’s contingent workforce outsourcing solutions.
Generated: DETERMINISTIC_77e2b3348068c8b6
Batch ID: 20250612_154312
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# contingent_workforce_management.py

import boto3
from botocore.exceptions import ClientError
import json
from flask import Flask, request, jsonify

app = Flask(__name__)

# Initialize AWS resources
dynamodb = boto3.resource('dynamodb')
s3 = boto3.client('s3')

# DynamoDB table name
TABLE_NAME = 'ContingentWorkforce'

# S3 bucket name for storing resumes
RESUME_BUCKET_NAME = 'contingent-workforce-resumes'

def create_table():
    """Create DynamoDB table if it doesn't exist."""
    try:
        dynamodb.create_table(
            TableName=TABLE_NAME,
            KeySchema=[
                {
                    'AttributeName': 'worker_id',
                    'KeyType': 'HASH'  # Partition key
                }
            ],
            AttributeDefinitions=[
                {
                    'AttributeName': 'worker_id',
                    'AttributeType': 'S'
                }
            ],
            ProvisionedThroughput={
                'ReadCapacityUnits': 5,
                'WriteCapacityUnits': 5
            }
        )
        print(f'Table {TABLE_NAME} created successfully.')
    except ClientError as e:
        print(f'Error creating table: {e.response["Error"]["Message"]}')

def upload_resume(worker_id, resume_file):
    """Upload worker resume to S3 bucket."""
    try:
        s3.upload_file(resume_file, RESUME_BUCKET_NAME, f'{worker_id}/resume.pdf')
        return f'Resume uploaded for worker {worker_id}.'
    except ClientError as e:
        return f'Error uploading resume: {e.response["Error"]["Message"]}'

@app.route('/add_worker', methods=['POST'])
def add_worker():
    """Add a new worker to the database."""
    data = request.json
    worker_id = data.get('worker_id')
    
    if not worker_id:
        return jsonify({"error": "worker_id is required"}), 400

    # Save worker information in DynamoDB
    table = dynamodb.Table(TABLE_NAME)
    try:
        table.put_item(Item=data)
        return jsonify({"message": "Worker added successfully"}), 201
    except ClientError as e:
        return jsonify({"error": e.response['Error']['Message']}), 500

@app.route('/upload_resume', methods=['POST'])
def handle_upload_resume():
    """Handle resume upload for a worker."""
    worker_id = request.form.get('worker_id')
    resume_file = request.files['resume']

    if not worker_id or resume_file is None:
        return jsonify({"error": "worker_id and resume file are required"}), 400

    # Save resume to S3
    resume_path = f'/tmp/{worker_id}_resume.pdf'
    resume_file.save(resume_path)
    result = upload_resume(worker_id, resume_path)

    return jsonify({"message": result}), 200

if __name__ == '__main__':
    create_table()  # Create the DynamoDB table when the application starts
    app.run(host='0.0.0.0', port=5000)  # Run the Flask application
```

### Requirements:
- Ensure you have the required packages installed:
  ```bash
  pip install Flask boto3
  ```
- Set up AWS credentials in your environment.
- The code assumes an S3 bucket named 'contingent-workforce-resumes' already exists.
