"""
Generated Code Metadata:
========================
Original URL: https://mesogia.com
Prompt: Generate code to implement a search functionality for a directory website where users can search for businesses like "Ταπετσαρίες Αυτοκινήτων" by name, category, or city.
Generated: DETERMINISTIC_d9596589c4475b3b
Batch ID: 20250612_151044
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# directory_search.py

import sqlite3
from typing import List, Dict

class DirectorySearch:
    def __init__(self, db_name: str):
        """
        Initialize the DirectorySearch class.

        Args:
        db_name (str): The name of the SQLite database file.
        """
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()

    def create_table(self):
        """
        Create the businesses table if it does not exist.
        """
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS businesses (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                category TEXT NOT NULL,
                city TEXT NOT NULL
            )
        ''')
        self.conn.commit()

    def add_business(self, business: Dict):
        """
        Add a business to the database.

        Args:
        business (Dict): A dictionary containing the business information.
        """
        self.cursor.execute('''
            INSERT INTO businesses (name, category, city)
            VALUES (?, ?, ?)
        ''', (business['name'], business['category'], business['city']))
        self.conn.commit()

    def search_by_name(self, name: str) -> List[Dict]:
        """
        Search for businesses by name.

        Args:
        name (str): The name of the business to search for.

        Returns:
        List[Dict]: A list of dictionaries containing the business information.
        """
        self.cursor.execute('''
            SELECT * FROM businesses
            WHERE name LIKE ?
        ''', (f'%{name}%',))
        return self._fetch_results()

    def search_by_category(self, category: str) -> List[Dict]:
        """
        Search for businesses by category.

        Args:
        category (str): The category of the business to search for.

        Returns:
        List[Dict]: A list of dictionaries containing the business information.
        """
        self.cursor.execute('''
            SELECT * FROM businesses
            WHERE category LIKE ?
        ''', (f'%{category}%',))
        return self._fetch_results()

    def search_by_city(self, city: str) -> List[Dict]:
        """
        Search for businesses by city.

        Args:
        city (str): The city of the business to search for.

        Returns:
        List[Dict]: A list of dictionaries containing the business information.
        """
        self.cursor.execute('''
            SELECT * FROM businesses
            WHERE city LIKE ?
        ''', (f'%{city}%',))
        return self._fetch_results()

    def search(self, query: str) -> List[Dict]:
        """
        Search for businesses by name, category, or city.

        Args:
        query (str): The search query.

        Returns:
        List[Dict]: A list of dictionaries containing the business information.
        """
        self.cursor.execute('''
            SELECT * FROM businesses
            WHERE name LIKE ? OR category LIKE ? OR city LIKE ?
        ''', (f'%{query}%', f'%{query}%', f'%{query}%'))
        return self._fetch_results()

    def _fetch_results(self) -> List[Dict]:
        """
        Fetch the results from the last query.

        Returns:
        List[Dict]: A list of dictionaries containing the business information.
        """
        rows = self.cursor.fetchall()
        results = []
        for row in rows:
            business = {
                'id': row[0],
                'name': row[1],
                'category': row[2],
                'city': row[3]
            }
            results.append(business)
        return results

    def close(self):
        """
        Close the database connection.
        """
        self.conn.close()


def main():
    db_name = 'directory.db'
    search = DirectorySearch(db_name)
    search.create_table()

    # Add some businesses
    businesses = [
        {'name': 'Ταπετσαρίες Αυτοκινήτων', 'category': 'Automotive', 'city': 'Athens'},
        {'name': 'Ψητοπωλείο', 'category': 'Food', 'city': 'Thessaloniki'},
        {'name': 'Taxi Services', 'category': 'Transportation', 'city': 'Athens'}
    ]
    for business in businesses:
        search.add_business(business)

    # Search for businesses
    query = 'Ταπετσαρίες Αυτοκινήτων'
    results = search.search(query)
    print(f'Search results for "{query}":')
    for result in results:
        print(result)

    query = 'Athens'
    results = search.search(query)
    print(f'\nSearch results for "{query}":')
    for result in results:
        print(result)

    search.close()


if __name__ == '__main__':
    main()
```
