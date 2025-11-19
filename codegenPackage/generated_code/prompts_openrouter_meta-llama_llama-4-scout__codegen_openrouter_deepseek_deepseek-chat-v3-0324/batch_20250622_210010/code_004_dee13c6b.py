"""
Generated Code Metadata:
========================
Original URL: https://airdrop-stepngo.asia
Prompt: Generate a checklist for troubleshooting common FASTPANEL errors, including domain name configuration, SSL certificate installation, and IPv4/IPv6 compatibility issues.
Generated: DETERMINISTIC_dee13c6b5b2e8ec9
Batch ID: 20250622_210010
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
#!/usr/bin/env python3
"""
FASTPANEL Troubleshooting Checklist Generator
Generates a structured checklist for common FASTPANEL issues.
"""

import sys
from typing import List, Dict

class FASTPanelChecklist:
    """
    Class to generate and manage FASTPANEL troubleshooting checklists.
    """
    
    def __init__(self):
        self.checklist = {
            'domain_configuration': [
                "Verify DNS records (A/AAAA) point to correct server IP",
                "Check domain is properly registered in FASTPANEL",
                "Ensure domain is not expired",
                "Confirm nameservers are correctly set",
                "Check for DNS propagation delays",
                "Verify domain is not blacklisted"
            ],
            'ssl_certificates': [
                "Check certificate is properly installed in FASTPANEL",
                "Verify certificate chain is complete",
                "Confirm private key matches certificate",
                "Check certificate expiration date",
                "Validate SAN (Subject Alternative Names) includes all domains",
                "Test SSL configuration using online tools (SSL Labs)"
            ],
            'ip_compatibility': [
                "Verify server has both IPv4 and IPv6 addresses assigned",
                "Check firewall allows both IPv4 and IPv6 traffic",
                "Test connectivity using both IP versions",
                "Confirm DNS has both A and AAAA records",
                "Check IPv6 routing is properly configured",
                "Validate application listens on both IP versions"
            ],
            'general_issues': [
                "Check FASTPANEL service status",
                "Verify disk space availability",
                "Review error logs (/var/log/fastpanel/)",
                "Check for pending updates",
                "Confirm correct PHP version is running",
                "Validate database connectivity"
            ]
        }
    
    def generate_checklist(self, selected_categories: List[str] = None) -> Dict[str, List[str]]:
        """
        Generate checklist for selected categories or all categories if none specified.
        
        Args:
            selected_categories: List of categories to include
            
        Returns:
            Dictionary of categories with their checklist items
        """
        if selected_categories is None:
            return self.checklist
        
        return {category: self.checklist[category] 
                for category in selected_categories 
                if category in self.checklist}
    
    def print_checklist(self, checklist_items: Dict[str, List[str]]):
        """
        Print formatted checklist to stdout.
        
        Args:
            checklist_items: Dictionary of checklist items to print
        """
        print("\nFASTPANEL Troubleshooting Checklist")
        print("=" * 40 + "\n")
        
        for category, items in checklist_items.items():
            print(f"[{category.upper().replace('_', ' ')}]")
            for i, item in enumerate(items, 1):
                print(f"{i}. {item}")
            print()

def main():
    try:
        checklist = FASTPanelChecklist()
        
        # Get user input for categories
        print("Available categories:")
        for i, category in enumerate(checklist.checklist.keys(), 1):
            print(f"{i}. {category.replace('_', ' ')}")
        
        selected = input("\nEnter categories to include (comma-separated numbers or 'all'): ")
        
        if selected.strip().lower() == 'all':
            selected_categories = None
        else:
            try:
                selected_indices = [int(x.strip()) - 1 for x in selected.split(',')]
                categories = list(checklist.checklist.keys())
                selected_categories = [categories[i] for i in selected_indices]
            except (ValueError, IndexError):
                print("Invalid input. Showing all categories by default.", file=sys.stderr)
                selected_categories = None
        
        # Generate and print checklist
        items = checklist.generate_checklist(selected_categories)
        checklist.print_checklist(items)
        
    except Exception as e:
        print(f"Error generating checklist: {str(e)}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
```
