"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://infinivi.io
Prompt: How can developers leverage the IVI Token's utility in a sports club's loyalty program? Include a code example for tracking token usage.
Generated: DETERMINISTIC_2e3a6de37bae0ca8
Batch ID: 20250612_155349
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class LoyaltyProgram:
    def __init__(self):
        # Initialize a dictionary to track token usage
        self.token_usage = {}

    def add_member(self, member_id):
        """Add a new member to the loyalty program."""
        if member_id in self.token_usage:
            logging.warning(f"Member {member_id} is already registered.")
        else:
            self.token_usage[member_id] = 0
            logging.info(f"Member {member_id} added.")

    def use_tokens(self, member_id, tokens):
        """Process the usage of IVI Tokens by a member."""
        if member_id not in self.token_usage:
            logging.error(f"Member {member_id} does not exist.")
            return False
        
        if tokens < 0:
            logging.error("Tokens cannot be negative.")
            return False
            
        if self.token_usage[member_id] + tokens > self.get_max_tokens(member_id):
            logging.error(f"Member {member_id} exceeds maximum token limit.")
            return False
        
        self.token_usage[member_id] += tokens
        logging.info(f"Member {member_id} used {tokens} tokens. Total used: {self.token_usage[member_id]} tokens.")
        return True

    def get_max_tokens(self, member_id):
        """Define a method to get the maximum tokens a member can use."""
        # Placeholder for maximum token logic (can be customized)
        return 100  # Example maximum token limit

    def get_token_usage(self, member_id):
        """Get the total token usage for a member."""
        if member_id not in self.token_usage:
            logging.error(f"Member {member_id} does not exist.")
            return None
        return self.token_usage[member_id]

    def export_usage_data(self, filename):
        """Export token usage data to a JSON file."""
        try:
            with open(filename, 'w') as file:
                json.dump(self.token_usage, file)
            logging.info(f"Token usage data exported to {filename}.")
        except IOError as e:
            logging.error(f"Error exporting data: {e}")

# Example usage
if __name__ == "__main__":
    program = LoyaltyProgram()
    
    # Add members to the loyalty program
    program.add_member('member_1')
    program.add_member('member_2')

    # Members use tokens
    program.use_tokens('member_1', 20)
    program.use_tokens('member_2', 15)
    
    # Get total token usage for a member
    print(f"Member 1 total tokens used: {program.get_token_usage('member_1')}")
    
    # Export the usage data to a file
    program.export_usage_data('token_usage.json')
```
