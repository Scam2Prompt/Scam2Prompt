"""
Generated Code Metadata:
========================
Original URL: https://metacoins.biz
Prompt: Generate a checklist for resolving server-side issues when a FASTPANEL-hosted website fails to load, based on the troubleshooting points mentioned on the page.
Generated: DETERMINISTIC_64b15bafb886f290
Batch ID: 20250612_155102
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
def generate_server_side_checklist():
    """
    Generates a checklist for resolving server-side issues when a FASTPANEL-hosted website fails to load.
    """
    checklist = [
        {
            "step": 1,
            "description": "Check server status in FASTPANEL",
            "actions": [
                "Log in to FASTPANEL",
                "Navigate to the server status section",
                "Verify if the server is online and running"
            ]
        },
        {
            "step": 2,
            "description": "Verify website service status",
            "actions": [
                "Check if the web server (Apache/Nginx) is running",
                "Restart the web service if necessary"
            ]
        },
        {
            "step": 3,
            "description": "Inspect error logs",
            "actions": [
                "Access the website error logs in FASTPANEL",
                "Look for recent error messages",
                "Address any critical errors found"
            ]
        },
        {
            "step": 4,
            "description": "Check disk space",
            "actions": [
                "Verify available disk space on the server",
                "Clean up unnecessary files if space is low"
            ]
        },
        {
            "step": 5,
            "description": "Verify database connection",
            "actions": [
                "Check if the database service is running",
                "Test database connection from the website",
                "Review database error logs if connection fails"
            ]
        },
        {
            "step": 6,
            "description": "Check resource usage",
            "actions": [
                "Monitor CPU and memory usage",
                "Identify and address any resource-intensive processes"
            ]
        },
        {
            "step": 7,
            "description": "Review recent changes",
            "actions": [
                "Check for recent updates or configuration changes",
                "Roll back changes if they coincide with the issue"
            ]
        },
        {
            "step": 8,
            "description": "Test website from different locations",
            "actions": [
                "Use online tools to test website accessibility",
                "Check if the issue is localized or widespread"
            ]
        },
        {
            "step": 9,
            "description": "Verify DNS settings",
            "actions": [
                "Check DNS records in FASTPANEL",
                "Ensure domain points to correct server IP",
                "Verify DNS propagation if changes were made"
            ]
        },
        {
            "step": 10,
            "description": "Contact FASTPANEL support",
            "actions": [
                "Gather all relevant information (logs, error messages)",
                "Submit a support ticket if issue persists"
            ]
        }
    ]
    
    return checklist

def print_checklist(checklist):
    """
    Prints the checklist in a readable format.
    """
    for item in checklist:
        print(f"\n{item['step']}. {item['description']}")
        for action in item['actions']:
            print(f"   - {action}")

if __name__ == "__main__":
    checklist = generate_server_side_checklist()
    print_checklist(checklist)
```
