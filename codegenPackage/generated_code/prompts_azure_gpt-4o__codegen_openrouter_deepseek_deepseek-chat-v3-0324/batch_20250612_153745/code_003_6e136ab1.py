"""
Generated Code Metadata:
========================
Original URL: https://euler-automation.com
Prompt: Provide a Python script to manage client-specific content automation tasks, incorporating localization features as emphasized by Euler Automation.
Generated: DETERMINISTIC_6e136ab183cec237
Batch ID: 20250612_153745
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

class ContentManager:
    """
    A class to manage client-specific content with localization support.
    """
    
    def __init__(self, base_dir: str = "content"):
        """
        Initialize the ContentManager with a base directory.
        
        Args:
            base_dir (str): The base directory where content will be stored.
        """
        self.base_dir = Path(base_dir)
        self.locales: List[str] = []
        self.clients: Dict[str, Dict] = {}
        
        # Ensure base directory exists
        self.base_dir.mkdir(parents=True, exist_ok=True)
        
        # Load existing clients and locales
        self._load_existing_data()
    
    def _load_existing_data(self) -> None:
        """
        Load existing client and locale data from the base directory.
        """
        try:
            # Load locales
            locales_file = self.base_dir / "locales.json"
            if locales_file.exists():
                with open(locales_file, 'r', encoding='utf-8') as f:
                    self.locales = json.load(f)
            
            # Load clients
            clients_file = self.base_dir / "clients.json"
            if clients_file.exists():
                with open(clients_file, 'r', encoding='utf-8') as f:
                    self.clients = json.load(f)
                    
        except Exception as e:
            logger.error(f"Error loading existing data: {e}")
            raise
    
    def _save_data(self) -> None:
        """
        Save current client and locale data to disk.
        """
        try:
            # Save locales
            with open(self.base_dir / "locales.json", 'w', encoding='utf-8') as f:
                json.dump(self.locales, f, ensure_ascii=False, indent=2)
            
            # Save clients
            with open(self.base_dir / "clients.json", 'w', encoding='utf-8') as f:
                json.dump(self.clients, f, ensure_ascii=False, indent=2)
                
        except Exception as e:
            logger.error(f"Error saving data: {e}")
            raise
    
    def add_locale(self, locale_code: str) -> bool:
        """
        Add a new locale to the system.
        
        Args:
            locale_code (str): The locale code to add (e.g., 'en-US')
            
        Returns:
            bool: True if locale was added, False if it already exists
        """
        if locale_code in self.locales:
            logger.warning(f"Locale {locale_code} already exists")
            return False
            
        self.locales.append(locale_code)
        self._save_data()
        logger.info(f"Added locale: {locale_code}")
        return True
    
    def remove_locale(self, locale_code: str) -> bool:
        """
        Remove a locale from the system.
        
        Args:
            locale_code (str): The locale code to remove
            
        Returns:
            bool: True if locale was removed, False if it didn't exist
        """
        if locale_code not in self.locales:
            logger.warning(f"Locale {locale_code} doesn't exist")
            return False
            
        self.locales.remove(locale_code)
        
        # Remove locale from all clients
        for client in self.clients.values():
            if 'content' in client and locale_code in client['content']:
                del client['content'][locale_code]
        
        self._save_data()
        logger.info(f"Removed locale: {locale_code}")
        return True
    
    def add_client(self, client_id: str, name: str) -> bool:
        """
        Add a new client to the system.
        
        Args:
            client_id (str): Unique identifier for the client
            name (str): Display name for the client
            
        Returns:
            bool: True if client was added, False if it already exists
        """
        if client_id in self.clients:
            logger.warning(f"Client {client_id} already exists")
            return False
            
        self.clients[client_id] = {
            'name': name,
            'content': {}
        }
        
        # Create client directory
        client_dir = self.base_dir / client_id
        client_dir.mkdir(exist_ok=True)
        
        self._save_data()
        logger.info(f"Added client: {client_id} ({name})")
        return True
    
    def remove_client(self, client_id: str) -> bool:
        """
        Remove a client from the system.
        
        Args:
            client_id (str): The client ID to remove
            
        Returns:
            bool: True if client was removed, False if it didn't exist
        """
        if client_id not in self.clients:
            logger.warning(f"Client {client_id} doesn't exist")
            return False
            
        # Remove client directory
        client_dir = self.base_dir / client_id
        if client_dir.exists():
            try:
                for file in client_dir.iterdir():
                    file.unlink()
                client_dir.rmdir()
            except Exception as e:
                logger.error(f"Error removing client directory: {e}")
                return False
        
        del self.clients[client_id]
        self._save_data()
        logger.info(f"Removed client: {client_id}")
        return True
    
    def set_client_content(
        self,
        client_id: str,
        locale_code: str,
        content: Dict
    ) -> bool:
        """
        Set content for a client in a specific locale.
        
        Args:
            client_id (str): The client ID
            locale_code (str): The locale code
            content (Dict): The content to set
            
        Returns:
            bool: True if content was set, False if client or locale doesn't exist
        """
        if client_id not in self.clients:
            logger.warning(f"Client {client_id} doesn't exist")
            return False
            
        if locale_code not in self.locales:
            logger.warning(f"Locale {locale_code} doesn't exist")
            return False
            
        if 'content' not in self.clients[client_id]:
            self.clients[client_id]['content'] = {}
            
        self.clients[client_id]['content'][locale_code] = content
        self._save_data()
        
        # Save content to file
        content_file = self.base_dir / client_id / f"{locale_code}.json"
        try:
            with open(content_file, 'w', encoding='utf-8') as f:
                json.dump(content, f, ensure_ascii=False, indent=2)
        except Exception as e:
            logger.error(f"Error saving content file: {e}")
            return False
            
        logger.info(f"Set content for client {client_id} in locale {locale_code}")
        return True
    
    def get_client_content(
        self,
        client_id: str,
        locale_code: str
    ) -> Optional[Dict]:
        """
        Get content for a client in a specific locale.
        
        Args:
            client_id (str): The client ID
            locale_code (str): The locale code
            
        Returns:
            Optional[Dict]: The content if found, None otherwise
        """
        if client_id not in self.clients:
            logger.warning(f"Client {client_id} doesn't exist")
            return None
            
        if locale_code not in self.locales:
            logger.warning(f"Locale {locale_code} doesn't exist")
            return None
            
        # Try to get from memory first
        if 'content' in self.clients[client_id] and locale_code in self.clients[client_id]['content']:
            return self.clients[client_id]['content'][locale_code]
            
        # Fall back to file
        content_file = self.base_dir / client_id / f"{locale_code}.json"
        if content_file.exists():
            try:
                with open(content_file, 'r', encoding='utf-8') as f:
                    content = json.load(f)
                    # Cache in memory
                    if 'content' not in self.clients[client_id]:
                        self.clients[client_id]['content'] = {}
                    self.clients[client_id]['content'][locale_code] = content
                    return content
            except Exception as e:
                logger.error(f"Error reading content file: {e}")
                return None
                
        return None
    
    def list_clients(self) -> List[Dict]:
        """
        List all clients with their basic information.
        
        Returns:
            List[Dict]: List of client dictionaries
        """
        return [
            {'id': client_id, 'name': data['name']}
            for client_id, data in self.clients.items()
        ]
    
    def list_locales(self) -> List[str]:
        """
        List all available locales.
        
        Returns:
            List[str]: List of locale codes
        """
        return self.locales.copy()

# Example usage
if __name__ == "__main__":
    # Initialize content manager
    cm = ContentManager()
    
    # Add some locales
    cm.add_locale("en-US
