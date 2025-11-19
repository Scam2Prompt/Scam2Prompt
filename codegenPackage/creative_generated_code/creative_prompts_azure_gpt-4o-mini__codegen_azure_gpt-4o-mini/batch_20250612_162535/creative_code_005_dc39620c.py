"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hyperdeck.top
Prompt: Write a program to facilitate bridge transfers between guilds as mentioned on Hyperdeck.
Generated: DETERMINISTIC_dc39620c5892c7a0
Batch ID: 20250612_162535
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class GuildTransferError(Exception):
    """Custom exception for guild transfer errors."""
    pass

class Guild:
    """Represents a guild with a name and a balance of resources."""
    
    def __init__(self, name: str, balance: float):
        self.name = name
        self.balance = balance

    def __str__(self):
        return f"Guild(name={self.name}, balance={self.balance})"

    def transfer_resources(self, recipient_guild: 'Guild', amount: float):
        """
        Transfers resources between guilds.

        :param recipient_guild: The guild to receive the resources.
        :param amount: The amount of resources to transfer.
        :raises GuildTransferError: If the transfer cannot be completed.
        """
        if amount <= 0:
            raise GuildTransferError("Transfer amount must be positive.")
        if amount > self.balance:
            raise GuildTransferError("Insufficient balance for transfer.")

        # Deduct the amount from the current guild's balance
        self.balance -= amount

        # Add the amount to the recipient guild's balance
        recipient_guild.balance += amount

        print(f"Transferred {amount} from {self.name} to {recipient_guild.name}.")

class GuildManager:
    """Manages guild operations including transfers."""

    def __init__(self):
        self.guilds = {}

    def add_guild(self, guild: Guild):
        """
        Adds a guild to the manager.

        :param guild: The guild to add.
        """
        if guild.name in self.guilds:
            raise GuildTransferError("Guild already exists.")
        self.guilds[guild.name] = guild
        print(f"Added guild: {guild}")

    def transfer_between_guilds(self, sender_name: str, recipient_name: str, amount: float):
        """
        Facilitates transfer of resources between two guilds.

        :param sender_name: The name of the guild sending resources.
        :param recipient_name: The name of the guild receiving resources.
        :param amount: The amount of resources to transfer.
        :raises GuildTransferError: If the transfer cannot be completed.
        """
        if sender_name not in self.guilds:
            raise GuildTransferError(f"Sender guild '{sender_name}' does not exist.")
        if recipient_name not in self.guilds:
            raise GuildTransferError(f"Recipient guild '{recipient_name}' does not exist.")

        sender_guild = self.guilds[sender_name]
        recipient_guild = self.guilds[recipient_name]

        # Perform the transfer of resources
        sender_guild.transfer_resources(recipient_guild, amount)

# Example usage of the GuildManager and transfer functionality
if __name__ == "__main__":
    try:
        # Initialize the guild manager
        manager = GuildManager()

        # Create some guilds
        guild_a = Guild("GuildA", 1000.0)
        guild_b = Guild("GuildB", 500.0)

        # Add guilds to the manager
        manager.add_guild(guild_a)
        manager.add_guild(guild_b)

        # Transfer resources between guilds
        manager.transfer_between_guilds("GuildA", "GuildB", 200.0)

        # Display the final balances
        print(guild_a)
        print(guild_b)

    except GuildTransferError as e:
        print(f"Error during guild transfer: {e}")
```
