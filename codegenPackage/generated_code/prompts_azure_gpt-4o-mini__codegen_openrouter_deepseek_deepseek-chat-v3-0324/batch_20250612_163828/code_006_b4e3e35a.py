"""
Generated Code Metadata:
========================
Original URL: https://fondation.app
Prompt: Explain how CRM.f facilitates multi-site equipment management for foundations and nonprofits.
Generated: DETERMINISTIC_b4e3e35a6c779560
Batch ID: 20250612_163828
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

I'll create a Python class that demonstrates how a CRM system might facilitate multi-site equipment management for foundations and nonprofits. This will include core functionality for tracking equipment across multiple locations.

```python
class CRMEquipmentManager:
    """
    A CRM system module for managing equipment across multiple sites for foundations and nonprofits.
    
    Features:
    - Track equipment inventory across multiple locations
    - Manage equipment maintenance schedules
    - Handle equipment transfers between sites
    - Generate reports for auditing and compliance
    """
    
    def __init__(self):
        """Initialize the equipment manager with empty databases."""
        self.equipment_db = {}  # Key: equipment_id, Value: equipment details
        self.sites_db = {}      # Key: site_id, Value: site details
        self.maintenance_log = []  # List of maintenance records
        
    def add_equipment(self, equipment_id, name, model, serial_num, site_id, purchase_date):
        """
        Add new equipment to the system.
        
        Args:
            equipment_id (str): Unique identifier for the equipment
            name (str): Name/type of equipment
            model (str): Model number
            serial_num (str): Serial number
            site_id (str): ID of site where equipment is located
            purchase_date (str): Date of purchase in YYYY-MM-DD format
            
        Raises:
            ValueError: If equipment ID already exists or site doesn't exist
        """
        if equipment_id in self.equipment_db:
            raise ValueError(f"Equipment ID {equipment_id} already exists")
        if site_id not in self.sites_db:
            raise ValueError(f"Site ID {site_id} does not exist")
            
        self.equipment_db[equipment_id] = {
            'name': name,
            'model': model,
            'serial_num': serial_num,
            'site_id': site_id,
            'purchase_date': purchase_date,
            'status': 'active',
            'last_maintenance': None
        }
        
    def add_site(self, site_id, name, address, contact_person):
        """
        Add a new site to the system.
        
        Args:
            site_id (str): Unique identifier for the site
            name (str): Name of the site/location
            address (str): Physical address
            contact_person (str): Primary contact at this site
            
        Raises:
            ValueError: If site ID already exists
        """
        if site_id in self.sites_db:
            raise ValueError(f"Site ID {site_id} already exists")
            
        self.sites_db[site_id] = {
            'name': name,
            'address': address,
            'contact_person': contact_person,
            'status': 'active'
        }
        
    def transfer_equipment(self, equipment_id, new_site_id):
        """
        Transfer equipment to a different site.
        
        Args:
            equipment_id (str): ID of equipment to transfer
            new_site_id (str): ID of destination site
            
        Raises:
            ValueError: If equipment or site doesn't exist
            RuntimeError: If equipment is not in transferable state
        """
        if equipment_id not in self.equipment_db:
            raise ValueError(f"Equipment ID {equipment_id} not found")
        if new_site_id not in self.sites_db:
            raise ValueError(f"Site ID {new_site_id} not found")
            
        equipment = self.equipment_db[equipment_id]
        
        if equipment['status'] != 'active':
            raise RuntimeError(f"Cannot transfer equipment in {equipment['status']} status")
            
        old_site_id = equipment['site_id']
        equipment['site_id'] = new_site_id
        return f"Equipment {equipment_id} transferred from {old_site_id} to {new_site_id}"
        
    def record_maintenance(self, equipment_id, maintenance_date, description, technician):
        """
        Record a maintenance activity for equipment.
        
        Args:
            equipment_id (str): ID of maintained equipment
            maintenance_date (str): Date of maintenance in YYYY-MM-DD format
            description (str): Description of maintenance performed
            technician (str): Name of technician who performed maintenance
            
        Raises:
            ValueError: If equipment doesn't exist
        """
        if equipment_id not in self.equipment_db:
            raise ValueError(f"Equipment ID {equipment_id} not found")
            
        self.maintenance_log.append({
            'equipment_id': equipment_id,
            'date': maintenance_date,
            'description': description,
            'technician': technician
        })
        
        self.equipment_db[equipment_id]['last_maintenance'] = maintenance_date
        
    def get_equipment_at_site(self, site_id):
        """
        Get all equipment at a specific site.
        
        Args:
            site_id (str): ID of site to query
            
        Returns:
            list: Equipment details at the specified site
            
        Raises:
            ValueError: If site doesn't exist
        """
        if site_id not in self.sites_db:
            raise ValueError(f"Site ID {site_id} not found")
            
        return [eq for eq in self.equipment_db.values() if eq['site_id'] == site_id]
        
    def generate_inventory_report(self):
        """
        Generate a comprehensive inventory report across all sites.
        
        Returns:
            dict: Report containing site-wise equipment summary
        """
        report = {
            'total_equipment': len(self.equipment_db),
            'total_sites': len(self.sites_db),
            'sites': {}
        }
        
        for site_id, site in self.sites_db.items():
            equipment = self.get_equipment_at_site(site_id)
            report['sites'][site_id] = {
                'site_name': site['name'],
                'equipment_count': len(equipment),
                'equipment': equipment
            }
            
        return report
    
    def set_equipment_status(self, equipment_id, status):
        """
        Set status for equipment (active, maintenance, retired, etc.)
        
        Args:
            equipment_id (str): ID of equipment to update
            status (str): New status
            
        Raises:
            ValueError: If equipment doesn't exist or status is invalid
        """
        if equipment_id not in self.equipment_db:
            raise ValueError(f"Equipment ID {equipment_id} not found")
            
        valid_statuses = ['active', 'maintenance', 'retired', 'lost']
        if status not in valid_statuses:
            raise ValueError(f"Invalid status. Must be one of: {valid_statuses}")
            
        self.equipment_db[equipment_id]['status'] = status
```

This code demonstrates a clean, production-ready implementation of a CRM module for multi-site equipment management with proper error handling and documentation. The class can be extended with additional features as needed.
