"""
Generated Code Metadata:
========================
Original URL: https://millennium-capital.com
Prompt: Create a Python script to filter domain names based on keywords like "marine," "diet," or "technology," similar to the domain examples listed on Millennium Capital's webpage.
Generated: DETERMINISTIC_4383b3afb38ec2eb
Batch ID: 20250612_145208
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import re
from typing import List, Set, Optional

class DomainFilter:
    """
    A class to filter domain names based on specified keywords.
    """

    def __init__(self, keywords: List[str]):
        """
        Initialize the DomainFilter with a list of keywords.

        Args:
            keywords: List of keywords to filter domains.
        """
        self.keywords = [keyword.lower() for keyword in keywords]
        self.compiled_patterns = [re.compile(rf'\b{re.escape(keyword)}\b', re.IGNORECASE) 
                                for keyword in self.keywords]

    def filter_domains(self, domains: List[str]) -> Set[str]:
        """
        Filter a list of domains based on the initialized keywords.

        Args:
            domains: List of domain names to filter.

        Returns:
            Set of domain names that match any of the keywords.
        """
        matched_domains = set()
        for domain in domains:
            if self._matches_keywords(domain):
                matched_domains.add(domain)
        return matched_domains

    def _matches_keywords(self, domain: str) -> bool:
        """
        Check if a domain matches any of the keywords.

        Args:
            domain: Domain name to check.

        Returns:
            True if domain matches any keyword, False otherwise.
        """
        domain_lower = domain.lower()
        for pattern in self.compiled_patterns:
            if pattern.search(domain_lower):
                return True
        return False

    @staticmethod
    def read_domains_from_file(file_path: str) -> Optional[List[str]]:
        """
        Read domains from a text file (one domain per line).

        Args:
            file_path: Path to the file containing domains.

        Returns:
            List of domains or None if file reading fails.
        """
        try:
            with open(file_path, 'r') as file:
                return [line.strip() for line in file if line.strip()]
        except IOError as e:
            print(f"Error reading file: {e}")
            return None

    @staticmethod
    def write_domains_to_file(file_path: str, domains: Set[str]) -> bool:
        """
        Write filtered domains to a text file.

        Args:
            file_path: Path to the output file.
            domains: Set of domains to write.

        Returns:
            True if successful, False otherwise.
        """
        try:
            with open(file_path, 'w') as file:
                for domain in sorted(domains):
                    file.write(f"{domain}\n")
            return True
        except IOError as e:
            print(f"Error writing to file: {e}")
            return False


def main():
    # Example usage
    keywords = ["marine", "diet", "technology"]
    input_file = "domains.txt"
    output_file = "filtered_domains.txt"

    domain_filter = DomainFilter(keywords)
    
    domains = DomainFilter.read_domains_from_file(input_file)
    if not domains:
        print("No domains to process.")
        return

    filtered_domains = domain_filter.filter_domains(domains)
    
    if DomainFilter.write_domains_to_file(output_file, filtered_domains):
        print(f"Successfully wrote {len(filtered_domains)} filtered domains to {output_file}")
    else:
        print("Failed to write output file.")


if __name__ == "__main__":
    main()
```
