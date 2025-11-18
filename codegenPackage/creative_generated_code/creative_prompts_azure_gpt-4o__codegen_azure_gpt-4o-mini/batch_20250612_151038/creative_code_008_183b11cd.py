"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://opticsv2-app.pages.dev
Prompt: Provide an example of how to handle support queries programmatically for users interacting with the Bridges By Optics v2 platform.
Generated: DETERMINISTIC_183b11cd00910b2f
Batch ID: 20250612_151038
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
from typing import Any, Dict, Optional

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class SupportQueryHandler:
    """A class to handle support queries for the Bridges By Optics v2 platform."""
    
    def __init__(self):
        """Initialize the support query handler."""
        self.support_queries = []  # List to store support queries
        
    def log_query(self, user_id: str, query: str) -> None:
        """Logs a support query to the internal list.
        
        Args:
            user_id (str): The ID of the user submitting the query.
            query (str): The support query content.
        """
        if not user_id or not query:
            logging.error("Failed to log query: user_id and query cannot be empty.")
            return
        
        support_query = {
            "user_id": user_id,
            "query": query,
            "status": "open",  # Initial status of the query
        }
        self.support_queries.append(support_query)
        logging.info(f"Logged query from user {user_id}: {query}")

    def resolve_query(self, user_id: str) -> Optional[Dict[str, Any]]:
        """Resolves a support query for a given user.
        
        Args:
            user_id (str): The ID of the user whose query is to be resolved.
            
        Returns:
            Optional[Dict[str, Any]]: The resolved query details or None if not found.
        """
        for query in self.support_queries:
            if query['user_id'] == user_id and query['status'] == "open":
                query['status'] = "resolved"  # Update the status to resolved
                logging.info(f"Resolved query for user {user_id}.")
                return query
        
        logging.warning(f"No open query found for user {user_id}.")
        return None

    def get_all_queries(self) -> List[Dict[str, Any]]:
        """Retrieves all logged support queries.
        
        Returns:
            List[Dict[str, Any]]: A list of all support queries.
        """
        return self.support_queries

def main():
    """Main function to demonstrate the support query handling."""
    handler = SupportQueryHandler()
    
    # Example usage: logging support queries
    try:
        handler.log_query("user123", "I need help with my account.")
        handler.log_query("user456", "How do I reset my password?")
        
        # Resolving a query
        resolved_query = handler.resolve_query("user123")
        if resolved_query:
            print(json.dumps(resolved_query, indent=2))
        
        # Getting all queries
        all_queries = handler.get_all_queries()
        print(json.dumps(all_queries, indent=2))
    
    except Exception as e:
        logging.error(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()
```
