"""
Generated Code Metadata:
========================
Original URL: https://fmt.co.id
Prompt: Develop a use case diagram for a construction equipment management system that includes features like equipment tracking, maintenance scheduling, and attachment management for excavators.
Generated: DETERMINISTIC_f56be5eba9c234fe
Batch ID: 20250622_211609
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Importing necessary libraries for creating a use case diagram
from diagrams import Diagram, Cluster
from diagrams.custom import Custom
from diagrams.generic.user import User

# Create a use case diagram for a construction equipment management system
with Diagram("Construction Equipment Management System Use Case Diagram", show=True):
    # Define the primary actor: Equipment Manager
    equipment_manager = User("Equipment Manager")

    # Define the system boundary
    with Cluster("Construction Equipment Management System"):
        # Define use cases
        equipment_tracking = Custom("Equipment Tracking", "./icons/equipment_tracking.png")
        maintenance_scheduling = Custom("Maintenance Scheduling", "./icons/maintenance_scheduling.png")
        attachment_management = Custom("Attachment Management", "./icons/attachment_management.png")

    # Connect the actor to the use cases
    equipment_manager >> equipment_tracking
    equipment_manager >> maintenance_scheduling
    equipment_manager >> attachment_management
```

### Notes:
1. This code uses the `diagrams` Python library to generate a use case diagram.
2. You need to install the `diagrams` library (`pip install diagrams`) and provide custom icons (`equipment_tracking.png`, `maintenance_scheduling.png`, `attachment_management.png`) for the use cases.
3. Save the icons in the same directory as the script or update the paths accordingly.
4. Running this script will generate a visual use case diagram in PNG format.
