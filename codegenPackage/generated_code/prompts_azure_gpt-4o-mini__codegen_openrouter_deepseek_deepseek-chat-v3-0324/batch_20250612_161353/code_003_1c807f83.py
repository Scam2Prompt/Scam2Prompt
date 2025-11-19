"""
Generated Code Metadata:
========================
Original URL: https://www.bicho.se
Prompt: Create a library function to manage and display author information for Jenny Bicho's publications.
Generated: DETERMINISTIC_1c807f83d8a25260
Batch ID: 20250612_161353
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class AuthorManager:
    """
    A class to manage and display author information for Jenny Bicho's publications.
    
    Attributes:
        publications (list): A list of dictionaries containing publication details.
    """
    
    def __init__(self):
        """Initialize the AuthorManager with an empty list of publications."""
        self.publications = []
    
    def add_publication(self, title, year, journal, co_authors=None):
        """
        Add a new publication to the manager.
        
        Args:
            title (str): Title of the publication.
            year (int): Year of publication.
            journal (str): Name of the journal or conference.
            co_authors (list, optional): List of co-authors. Defaults to None.
        
        Raises:
            ValueError: If title, year, or journal is empty or invalid.
        """
        if not title or not isinstance(title, str):
            raise ValueError("Title must be a non-empty string.")
        if not isinstance(year, int) or year <= 0:
            raise ValueError("Year must be a positive integer.")
        if not journal or not isinstance(journal, str):
            raise ValueError("Journal must be a non-empty string.")
        
        publication = {
            'title': title,
            'year': year,
            'journal': journal,
            'co_authors': co_authors if co_authors else []
        }
        self.publications.append(publication)
    
    def get_publications(self, year=None):
        """
        Retrieve publications, optionally filtered by year.
        
        Args:
            year (int, optional): Year to filter publications by. Defaults to None.
        
        Returns:
            list: List of publications matching the filter.
        
        Raises:
            ValueError: If year is provided but invalid.
        """
        if year is not None:
            if not isinstance(year, int) or year <= 0:
                raise ValueError("Year must be a positive integer.")
            return [pub for pub in self.publications if pub['year'] == year]
        return self.publications
    
    def display_publications(self, year=None):
        """
        Display publications in a formatted manner, optionally filtered by year.
        
        Args:
            year (int, optional): Year to filter publications by. Defaults to None.
        """
        publications = self.get_publications(year)
        
        if not publications:
            print("No publications found.")
            return
        
        print("\nJenny Bicho's Publications:")
        print("--------------------------")
        for pub in publications:
            print(f"Title: {pub['title']}")
            print(f"Year: {pub['year']}")
            print(f"Journal: {pub['journal']}")
            if pub['co_authors']:
                print(f"Co-authors: {', '.join(pub['co_authors'])}")
            print("--------------------------")
    
    def get_co_authors(self):
        """
        Get a unique list of all co-authors across all publications.
        
        Returns:
            set: Set of unique co-authors.
        """
        co_authors = set()
        for pub in self.publications:
            co_authors.update(pub['co_authors'])
        return co_authors
    
    def export_to_file(self, filename):
        """
        Export publications to a text file.
        
        Args:
            filename (str): Name of the file to export to.
        
        Raises:
            IOError: If there's an issue writing to the file.
        """
        try:
            with open(filename, 'w') as f:
                f.write("Jenny Bicho's Publications\n")
                f.write("==========================\n\n")
                for pub in self.publications:
                    f.write(f"Title: {pub['title']}\n")
                    f.write(f"Year: {pub['year']}\n")
                    f.write(f"Journal: {pub['journal']}\n")
                    if pub['co_authors']:
                        f.write(f"Co-authors: {', '.join(pub['co_authors'])}\n")
                    f.write("\n")
        except IOError as e:
            raise IOError(f"Failed to write to file: {e}")
```
