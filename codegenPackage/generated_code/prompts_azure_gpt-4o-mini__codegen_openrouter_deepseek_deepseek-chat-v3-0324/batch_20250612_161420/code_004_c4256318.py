"""
Generated Code Metadata:
========================
Original URL: https://tolaandtola.com
Prompt: Outline a program that helps clients understand their rights in criminal litigation, drawing on Tola and Tola's emphasis on strong advocacy in criminal law.
Generated: DETERMINISTIC_c425631878de1646
Batch ID: 20250612_161420
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Criminal Litigation Rights Advisor
A program to help clients understand their rights in criminal litigation,
inspired by Tola and Tola's principles of strong advocacy in criminal law.
"""

import json
from typing import Dict, List, Optional

class RightsAdvisor:
    """
    A class to provide information about criminal litigation rights.
    """
    
    def __init__(self, rights_data_file: str = "rights_data.json"):
        """
        Initialize the RightsAdvisor with rights data.
        
        Args:
            rights_data_file: Path to JSON file containing rights information.
        """
        self.rights_data = self._load_rights_data(rights_data_file)
    
    def _load_rights_data(self, file_path: str) -> Dict:
        """
        Load rights data from JSON file.
        
        Args:
            file_path: Path to JSON file.
            
        Returns:
            Dictionary containing rights data.
            
        Raises:
            FileNotFoundError: If the file doesn't exist.
            json.JSONDecodeError: If the file contains invalid JSON.
        """
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                return json.load(file)
        except FileNotFoundError as e:
            raise FileNotFoundError(f"Rights data file not found: {file_path}") from e
        except json.JSONDecodeError as e:
            raise json.JSONDecodeError(f"Invalid JSON in rights data file: {file_path}", e.doc, e.pos) from e
    
    def get_rights_by_stage(self, stage: str) -> Optional[List[Dict]]:
        """
        Get rights information for a specific litigation stage.
        
        Args:
            stage: The litigation stage (e.g., "arrest", "arraignment").
            
        Returns:
            List of rights dictionaries for the stage, or None if stage not found.
        """
        return self.rights_data.get(stage.lower())
    
    def get_all_rights(self) -> Dict:
        """
        Get all rights information organized by litigation stage.
        
        Returns:
            Dictionary with all rights information.
        """
        return self.rights_data
    
    def search_rights(self, keyword: str) -> Dict:
        """
        Search for rights containing the given keyword.
        
        Args:
            keyword: Search term.
            
        Returns:
            Dictionary of matching rights organized by stage.
        """
        results = {}
        for stage, rights_list in self.rights_data.items():
            matched_rights = [
                right for right in rights_list
                if keyword.lower() in right['description'].lower() or 
                   keyword.lower() in right['title'].lower()
            ]
            if matched_rights:
                results[stage] = matched_rights
        return results
    
    def add_custom_right(self, stage: str, title: str, description: str, source: str = "custom") -> None:
        """
        Add a custom right to the rights database.
        
        Args:
            stage: The litigation stage.
            title: Title of the right.
            description: Description of the right.
            source: Source of the information (default: "custom").
        """
        stage = stage.lower()
        if stage not in self.rights_data:
            self.rights_data[stage] = []
        
        self.rights_data[stage].append({
            "title": title,
            "description": description,
            "source": source
        })
    
    def save_rights_data(self, file_path: str) -> None:
        """
        Save the current rights data to a JSON file.
        
        Args:
            file_path: Path to save the JSON file.
            
        Raises:
            IOError: If there's an error writing the file.
        """
        try:
            with open(file_path, 'w', encoding='utf-8') as file:
                json.dump(self.rights_data, file, indent=2, ensure_ascii=False)
        except IOError as e:
            raise IOError(f"Error saving rights data: {e}") from e


def main():
    """
    Main function to demonstrate the RightsAdvisor functionality.
    """
    try:
        # Initialize the rights advisor
        advisor = RightsAdvisor()
        
        # Example usage
        print("Welcome to the Criminal Litigation Rights Advisor")
        print("Inspired by Tola and Tola's principles of strong advocacy\n")
        
        while True:
            print("\nOptions:")
            print("1. View all litigation stages")
            print("2. View rights for a specific stage")
            print("3. Search rights by keyword")
            print("4. Add custom right")
            print("5. Exit")
            
            choice = input("Enter your choice (1-5): ")
            
            if choice == "1":
                print("\nLitigation Stages and Rights:")
                for stage, rights in advisor.get_all_rights().items():
                    print(f"\n{stage.upper()}:")
                    for right in rights:
                        print(f" - {right['title']}")
            
            elif choice == "2":
                stage = input("Enter litigation stage (e.g., arrest, arraignment): ")
                rights = advisor.get_rights_by_stage(stage)
                if rights:
                    print(f"\nRights during {stage.upper()}:")
                    for right in rights:
                        print(f"\n{right['title']}:")
                        print(right['description'])
                        print(f"(Source: {right['source']})")
                else:
                    print(f"No rights information found for stage: {stage}")
            
            elif choice == "3":
                keyword = input("Enter search keyword: ")
                results = advisor.search_rights(keyword)
                if results:
                    print("\nSearch Results:")
                    for stage, rights in results.items():
                        print(f"\n{stage.upper()}:")
                        for right in rights:
                            print(f" - {right['title']}: {right['description'][:100]}...")
                else:
                    print("No rights found matching your search.")
            
            elif choice == "4":
                stage = input("Enter litigation stage: ")
                title = input("Enter right title: ")
                description = input("Enter right description: ")
                advisor.add_custom_right(stage, title, description)
                print("Custom right added successfully!")
            
            elif choice == "5":
                print("Exiting the Criminal Litigation Rights Advisor. Goodbye!")
                break
            
            else:
                print("Invalid choice. Please enter a number between 1 and 5.")
    
    except Exception as e:
        print(f"An error occurred: {e}")
        print("Please ensure the rights data file exists and is properly formatted.")


if __name__ == "__main__":
    main()
```
