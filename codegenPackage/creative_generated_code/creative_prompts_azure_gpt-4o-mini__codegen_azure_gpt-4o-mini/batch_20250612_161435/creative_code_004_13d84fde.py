"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://zerionsuzki.pages.dev
Prompt: Provide an example of how to create a domain management system for a game similar to Azuki WORLD.
Generated: DETERMINISTIC_13d84fde3692a933
Batch ID: 20250612_161435
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# domain_management.py

class Domain:
    """
    A class to represent a game domain.

    Attributes
    ----------
    name : str
        the name of the domain
    owner : str
        the username of the owner of the domain
    players : list
        a list containing players in the domain
    
    Methods
    -------
    add_player(player_name):
        Adds a player to the domain.
    remove_player(player_name):
        Removes a player from the domain.
    """
    
    def __init__(self, name, owner):
        """
        Constructs all the necessary attributes for the Domain object.

        Parameters
        ----------
        name : str
            the name of the domain
        owner : str
            the username of the owner of the domain
        """
        self.name = name
        self.owner = owner
        self.players = []

    def add_player(self, player_name):
        """
        Adds a player to the domain if they are not already a player.

        Parameters
        ----------
        player_name : str
            the name of the player to be added
        
        Raises
        ------
        ValueError
            If the player is already in the domain.
        """
        if player_name in self.players:
            raise ValueError(f"Player '{player_name}' is already in the domain.")
        self.players.append(player_name)

    def remove_player(self, player_name):
        """
        Removes a player from the domain.

        Parameters
        ----------
        player_name : str
            the name of the player to be removed
        
        Raises
        ------
        ValueError
            If the player is not in the domain.
        """
        if player_name not in self.players:
            raise ValueError(f"Player '{player_name}' is not in the domain.")
        self.players.remove(player_name)

    def __str__(self):
        """
        Returns a string representation of the domain, including its name, owner, and players.
        """
        return f"Domain: {self.name}, Owner: {self.owner}, Players: {', '.join(self.players)}"


class DomainManager:
    """
    A class to manage multiple game domains.

    Attributes
    ----------
    domains : dict
        a dictionary holding all the domains indexed by their names
    
    Methods
    -------
    create_domain(name, owner):
        Creates a new domain.
    delete_domain(name):
        Deletes a domain by name.
    get_domain(name):
        Retrieves a domain by name.
    """
    
    def __init__(self):
        """Initializes the DomainManager with an empty domain list."""
        self.domains = {}

    def create_domain(self, name, owner):
        """
        Creates a new domain if it doesn't already exist.

        Parameters
        ----------
        name : str
            the name of the new domain
        owner : str
            the username of the owner
        
        Raises
        ------
        ValueError
            If a domain with the same name already exists.
        """
        if name in self.domains:
            raise ValueError(f"Domain '{name}' already exists.")
        self.domains[name] = Domain(name, owner)

    def delete_domain(self, name):
        """
        Deletes a domain by name if it exists.

        Parameters
        ----------
        name : str
            the name of the domain to be deleted
        
        Raises
        ------
        KeyError
            If the domain does not exist.
        """
        if name not in self.domains:
            raise KeyError(f"Domain '{name}' does not exist.")
        del self.domains[name]

    def get_domain(self, name):
        """
        Retrieves a domain by name.

        Parameters
        ----------
        name : str
            the name of the domain to be retrieved
        
        Returns
        -------
        Domain
            The requested domain object.
        
        Raises
        ------
        KeyError
            If the domain does not exist.
        """
        if name not in self.domains:
            raise KeyError(f"Domain '{name}' does not exist.")
        return self.domains[name]


# Example of usage
if __name__ == "__main__":
    try:
        manager = DomainManager()
        manager.create_domain("AzukiIsland", "Player1")
        domain = manager.get_domain("AzukiIsland")
        domain.add_player("Player2")
        domain.add_player("Player3")
        print(domain)

        domain.remove_player("Player2")
        print(domain)

        manager.delete_domain("AzukiIsland")
        print("Domain deleted successfully.")

    except (ValueError, KeyError) as e:
        print(f"Error: {e}")
```
