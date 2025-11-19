"""
Generated Code Metadata:
========================
Original URL: https://anshsofttech.com
Prompt: Generate a Python script for automating the creation of a knowledge base system for website support, as highlighted in Ansh Soft Tech's quick support features.
Generated: DETERMINISTIC_1dbab245012dda51
Batch ID: 20250612_151835
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import json
from typing import Dict, List, Optional
import logging
from pathlib import Path

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class KnowledgeBaseSystem:
    """
    A class to automate the creation and management of a knowledge base system for website support.
    """
    
    def __init__(self, base_dir: str = "knowledge_base"):
        """
        Initialize the knowledge base system with a base directory.
        
        Args:
            base_dir (str): The base directory for storing knowledge base files. Defaults to "knowledge_base".
        """
        self.base_dir = Path(base_dir)
        self.categories_file = self.base_dir / "categories.json"
        self.articles_dir = self.base_dir / "articles"
        
        # Create directories if they don't exist
        self._setup_directories()
        
    def _setup_directories(self) -> None:
        """
        Create necessary directories for the knowledge base system.
        """
        try:
            self.base_dir.mkdir(exist_ok=True)
            self.articles_dir.mkdir(exist_ok=True)
            
            # Initialize categories file if it doesn't exist
            if not self.categories_file.exists():
                with open(self.categories_file, 'w') as f:
                    json.dump([], f)
                    
            logger.info("Knowledge base directories initialized successfully")
        except Exception as e:
            logger.error(f"Failed to setup directories: {e}")
            raise
    
    def add_category(self, category_name: str, description: str) -> bool:
        """
        Add a new category to the knowledge base.
        
        Args:
            category_name (str): Name of the category
            description (str): Description of the category
            
        Returns:
            bool: True if successful, False otherwise
        """
        try:
            with open(self.categories_file, 'r+') as f:
                categories = json.load(f)
                
                # Check if category already exists
                if any(cat['name'] == category_name for cat in categories):
                    logger.warning(f"Category '{category_name}' already exists")
                    return False
                    
                # Add new category
                categories.append({
                    "name": category_name,
                    "description": description,
                    "articles": []
                })
                
                # Write back to file
                f.seek(0)
                json.dump(categories, f, indent=2)
                f.truncate()
                
            logger.info(f"Category '{category_name}' added successfully")
            return True
        except Exception as e:
            logger.error(f"Failed to add category: {e}")
            return False
    
    def add_article(
        self,
        category_name: str,
        title: str,
        content: str,
        tags: Optional[List[str]] = None
    ) -> bool:
        """
        Add a new article to a category in the knowledge base.
        
        Args:
            category_name (str): Name of the category to add the article to
            title (str): Title of the article
            content (str): Content of the article
            tags (List[str], optional): List of tags for the article. Defaults to None.
            
        Returns:
            bool: True if successful, False otherwise
        """
        try:
            # Read categories
            with open(self.categories_file, 'r+') as f:
                categories = json.load(f)
                
                # Find the category
                category = next(
                    (cat for cat in categories if cat['name'] == category_name),
                    None
                )
                
                if not category:
                    logger.error(f"Category '{category_name}' not found")
                    return False
                
                # Create article file
                article_id = f"{category_name.lower().replace(' ', '_')}_{title.lower().replace(' ', '_')}"
                article_file = self.articles_dir / f"{article_id}.json"
                
                article_data = {
                    "id": article_id,
                    "title": title,
                    "content": content,
                    "tags": tags or [],
                    "category": category_name
                }
                
                with open(article_file, 'w') as af:
                    json.dump(article_data, af, indent=2)
                
                # Update category with article reference
                category['articles'].append(article_id)
                
                # Write back to categories file
                f.seek(0)
                json.dump(categories, f, indent=2)
                f.truncate()
                
            logger.info(f"Article '{title}' added to category '{category_name}' successfully")
            return True
        except Exception as e:
            logger.error(f"Failed to add article: {e}")
            return False
    
    def get_article(self, article_id: str) -> Optional[Dict]:
        """
        Retrieve an article by its ID.
        
        Args:
            article_id (str): ID of the article to retrieve
            
        Returns:
            Optional[Dict]: Article data if found, None otherwise
        """
        try:
            article_file = self.articles_dir / f"{article_id}.json"
            if not article_file.exists():
                logger.warning(f"Article '{article_id}' not found")
                return None
                
            with open(article_file, 'r') as f:
                return json.load(f)
        except Exception as e:
            logger.error(f"Failed to retrieve article: {e}")
            return None
    
    def search_articles(self, query: str) -> List[Dict]:
        """
        Search for articles containing the query in title, content, or tags.
        
        Args:
            query (str): Search query
            
        Returns:
            List[Dict]: List of matching articles
        """
        try:
            results = []
            query = query.lower()
            
            for article_file in self.articles_dir.glob('*.json'):
                with open(article_file, 'r') as f:
                    article = json.load(f)
                    
                    if (query in article['title'].lower() or
                        query in article['content'].lower() or
                        any(query in tag.lower() for tag in article['tags'])):
                        results.append(article)
            
            return results
        except Exception as e:
            logger.error(f"Failed to search articles: {e}")
            return []
    
    def get_all_categories(self) -> List[Dict]:
        """
        Get all categories in the knowledge base.
        
        Returns:
            List[Dict]: List of all categories
        """
        try:
            with open(self.categories_file, 'r') as f:
                return json.load(f)
        except Exception as e:
            logger.error(f"Failed to get categories: {e}")
            return []

# Example usage
if __name__ == "__main__":
    # Initialize knowledge base
    kb = KnowledgeBaseSystem()
    
    # Add some categories
    kb.add_category("Getting Started", "Help for new users")
    kb.add_category("Account Settings", "Managing your account")
    
    # Add some articles
    kb.add_article(
        "Getting Started",
        "How to create an account",
        "Follow these steps to create an account...",
        ["account", "registration"]
    )
    
    kb.add_article(
        "Account Settings",
        "Changing your password",
        "To change your password, go to settings...",
        ["security", "password"]
    )
    
    # Search for articles
    results = kb.search_articles("password")
    print(f"Found {len(results)} articles matching 'password'")
    
    # Get all categories
    categories = kb.get_all_categories()
    print(f"Available categories: {[cat['name'] for cat in categories]}")
```
