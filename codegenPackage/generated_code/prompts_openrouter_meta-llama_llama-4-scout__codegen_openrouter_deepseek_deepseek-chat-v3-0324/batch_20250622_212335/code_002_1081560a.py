"""
Generated Code Metadata:
========================
Original URL: https://helpdesk.contact
Prompt: Generate a Python script that can be used to automate responses to frequently asked questions (FAQs) like those listed on The Prepper Codex helpdesk page.
Generated: DETERMINISTIC_1081560abd7e5361
Batch ID: 20250622_212335
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import re
from typing import Dict, List, Optional

class FAQBot:
    """
    A chatbot designed to automate responses to frequently asked questions (FAQs).
    """
    
    def __init__(self, faq_file: str = "faqs.json"):
        """
        Initialize the FAQ bot with a JSON file containing FAQs and answers.
        
        Args:
            faq_file (str): Path to the JSON file containing FAQs. Defaults to "faqs.json".
        """
        self.faqs = self._load_faqs(faq_file)
        self._build_keyword_index()
    
    def _load_faqs(self, faq_file: str) -> Dict[str, Dict]:
        """
        Load FAQs from a JSON file.
        
        Args:
            faq_file (str): Path to the JSON file.
            
        Returns:
            Dict[str, Dict]: Dictionary of FAQs with their metadata.
            
        Raises:
            FileNotFoundError: If the FAQ file doesn't exist.
            json.JSONDecodeError: If the file contains invalid JSON.
        """
        try:
            with open(faq_file, 'r', encoding='utf-8') as f:
                return json.load(f)
        except FileNotFoundError:
            raise FileNotFoundError(f"FAQ file not found: {faq_file}")
        except json.JSONDecodeError as e:
            raise json.JSONDecodeError(f"Invalid JSON in FAQ file: {e.msg}", e.doc, e.pos)
    
    def _build_keyword_index(self) -> None:
        """
        Build an index of keywords from FAQ questions for faster searching.
        """
        self.keyword_index = {}
        for faq_id, faq_data in self.faqs.items():
            question = faq_data['question'].lower()
            keywords = re.findall(r'\w+', question)
            for keyword in keywords:
                if keyword not in self.keyword_index:
                    self.keyword_index[keyword] = []
                self.keyword_index[keyword].append(faq_id)
    
    def find_best_match(self, query: str) -> Optional[str]:
        """
        Find the best matching FAQ for a given query.
        
        Args:
            query (str): The user's question.
            
        Returns:
            Optional[str]: The answer if a match is found, None otherwise.
        """
        query = query.lower()
        query_keywords = set(re.findall(r'\w+', query))
        
        # Score FAQs based on keyword matches
        scores = {}
        for keyword in query_keywords:
            if keyword in self.keyword_index:
                for faq_id in self.keyword_index[keyword]:
                    if faq_id not in scores:
                        scores[faq_id] = 0
                    scores[faq_id] += 1
        
        if not scores:
            return None
        
        # Get FAQ with highest score
        best_faq_id = max(scores.items(), key=lambda x: x[1])[0]
        return self.faqs[best_faq_id]['answer']
    
    def get_faq_list(self) -> List[Dict]:
        """
        Get a list of all FAQs.
        
        Returns:
            List[Dict]: List of FAQs with their questions and IDs.
        """
        return [{'id': faq_id, 'question': data['question']} for faq_id, data in self.faqs.items()]
    
    def get_faq_by_id(self, faq_id: str) -> Optional[Dict]:
        """
        Get a specific FAQ by its ID.
        
        Args:
            faq_id (str): The ID of the FAQ.
            
        Returns:
            Optional[Dict]: The FAQ data if found, None otherwise.
        """
        return self.faqs.get(faq_id)

# Example usage
if __name__ == "__main__":
    try:
        bot = FAQBot()
        
        while True:
            print("\nAvailable commands:")
            print("1. Ask a question")
            print("2. List all FAQs")
            print("3. Get FAQ by ID")
            print("4. Exit")
            
            choice = input("Enter your choice (1-4): ").strip()
            
            if choice == "1":
                question = input("Enter your question: ").strip()
                answer = bot.find_best_match(question)
                if answer:
                    print("\nAnswer:", answer)
                else:
                    print("\nSorry, I couldn't find an answer to your question.")
            
            elif choice == "2":
                faqs = bot.get_faq_list()
                print("\nAvailable FAQs:")
                for faq in faqs:
                    print(f"{faq['id']}: {faq['question']}")
            
            elif choice == "3":
                faq_id = input("Enter FAQ ID: ").strip()
                faq = bot.get_faq_by_id(faq_id)
                if faq:
                    print(f"\nQuestion: {faq['question']}")
                    print(f"Answer: {faq['answer']}")
                else:
                    print("\nFAQ not found.")
            
            elif choice == "4":
                print("Goodbye!")
                break
            
            else:
                print("Invalid choice. Please try again.")
    
    except Exception as e:
        print(f"An error occurred: {str(e)}")
```
