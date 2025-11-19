"""
Generated Code Metadata:
========================
Original URL: https://binqutab.ae
Prompt: Create a use case diagram for a logistics company offering warehousing, transportation, and customs clearance services, inspired by Bin Qutab Logistics L.L.C's service portfolio.
Generated: DETERMINISTIC_57554f7dec521ed9
Batch ID: 20250622_205836
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from diagrams import Diagram
from diagrams.aws.general import User
from diagrams.aws.storage import SimpleStorageServiceS3Bucket
from diagrams.aws.mobile import APIGateway
from diagrams.aws.compute import Lambda
from diagrams.aws.network import Route53
from diagrams.aws.analytics import DataPipeline
from diagrams.aws.integration import SQS
from diagrams.aws.management import Cloudwatch
from diagrams.aws.security import IAM
from diagrams.aws.database import Dynamodb

with Diagram("Logistics Company Use Case Diagram", show=False, direction="TB"):
    customer = User("Customer")
    
    # Main services
    warehousing = SimpleStorageServiceS3Bucket("Warehousing")
    transportation = APIGateway("Transportation")
    customs_clearance = Lambda("Customs Clearance")
    
    # Supporting systems
    tracking_system = Route53("Tracking System")
    billing_system = Dynamodb("Billing System")
    customer_portal = APIGateway("Customer Portal")
    reporting = DataPipeline("Reporting")
    notifications = SQS("Notifications")
    monitoring = Cloudwatch("Monitoring")
    auth = IAM("Authentication")
    
    # Connections
    customer >> customer_portal
    customer_portal >> warehousing
    customer_portal >> transportation
    customer_portal >> customs_clearance
    customer_portal >> tracking_system
    customer_portal >> billing_system
    
    warehousing >> reporting
    transportation >> reporting
    customs_clearance >> reporting
    
    warehousing >> notifications
    transportation >> notifications
    customs_clearance >> notifications
    
    customer_portal >> auth
    monitoring << warehousing
    monitoring << transportation
    monitoring << customs_clearance
```
