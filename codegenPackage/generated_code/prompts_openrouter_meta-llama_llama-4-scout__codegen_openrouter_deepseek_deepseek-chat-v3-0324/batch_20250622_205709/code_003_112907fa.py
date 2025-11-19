"""
Generated Code Metadata:
========================
Original URL: https://gadgetexa.com
Prompt: "Generate a troubleshooting guide for common issues with laminators, such as jamming and uneven lamination."
Generated: DETERMINISTIC_112907fa3d377219
Batch ID: 20250622_205709
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Laminator Troubleshooting Guide
This script provides a troubleshooting guide for common laminator issues.
"""

class LaminatorTroubleshootingGuide:
    """
    A class to provide troubleshooting solutions for common laminator problems.
    """
    
    def __init__(self):
        self.issues = {
            'jamming': {
                'description': 'Document gets stuck in the laminator',
                'solutions': [
                    'Turn off and unplug the laminator',
                    'Remove any stuck documents carefully',
                    'Check for debris and clean rollers',
                    'Ensure documents are properly aligned before feeding',
                    'Use proper thickness pouches for your laminator'
                ]
            },
            'uneven_lamination': {
                'description': 'Lamination is uneven or has bubbles',
                'solutions': [
                    'Ensure pouch is properly centered before feeding',
                    'Clean rollers to ensure even heat distribution',
                    'Check that temperature settings match pouch thickness',
                    'Feed documents straight and at consistent speed',
                    'Pre-heat laminator fully before use'
                ]
            },
            'wrinkles': {
                'description': 'Laminated documents have wrinkles',
                'solutions': [
                    'Ensure document is flat before laminating',
                    'Use proper temperature setting for pouch thickness',
                    'Feed document slowly and evenly',
                    'Check for roller alignment issues',
                    'Allow laminated document to cool flat under weight'
                ]
            },
            'poor_adhesion': {
                'description': 'Lamination film not sticking properly',
                'solutions': [
                    'Increase temperature setting if too low',
                    'Ensure pouch is properly sealed on all edges',
                    'Clean rollers to remove any residue',
                    'Check pouch expiration date',
                    'Use fresh, high-quality laminating pouches'
                ]
            },
            'overheating': {
                'description': 'Laminator shuts off due to overheating',
                'solutions': [
                    'Allow laminator to cool down before continuing',
                    'Reduce continuous usage time',
                    'Ensure proper ventilation around laminator',
                    'Check for blocked air vents',
                    'Service unit if problem persists'
                ]
            }
        }
    
    def get_issue(self, issue_name):
        """
        Retrieve troubleshooting information for a specific issue.
        
        Args:
            issue_name (str): Name of the issue to troubleshoot
            
        Returns:
            dict: Dictionary containing issue description and solutions
            None: If issue is not found
        """
        return self.issues.get(issue_name.lower())
    
    def list_issues(self):
        """
        List all available issues with their descriptions.
        
        Returns:
            list: List of tuples containing (issue_name, description)
        """
        return [(name, data['description']) for name, data in self.issues.items()]
    
    def print_troubleshooting_guide(self):
        """
        Print a complete troubleshooting guide for all known issues.
        """
        print("LAMINATOR TROUBLESHOOTING GUIDE")
        print("===============================\n")
        
        for issue_name, issue_data in self.issues.items():
            print(f"Issue: {issue_name.replace('_', ' ').title()}")
            print(f"Description: {issue_data['description']}")
            print("Solutions:")
            for i, solution in enumerate(issue_data['solutions'], 1):
                print(f"  {i}. {solution}")
            print()


# Example usage
if __name__ == "__main__":
    guide = LaminatorTroubleshootingGuide()
    
    # Print complete guide
    guide.print_troubleshooting_guide()
    
    # Example of querying specific issue
    print("\nQuerying specific issue:")
    issue = guide.get_issue('jamming')
    if issue:
        print(f"\nIssue: Jamming")
        print(f"Description: {issue['description']}")
        print("Solutions:")
        for solution in issue['solutions']:
            print(f"- {solution}")
    else:
        print("Issue not found in troubleshooting guide.")
```
