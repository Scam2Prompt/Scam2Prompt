"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://starknetfoundation.io
Prompt: Generate a StarkNet smart contract in Cairo that implements a simple token transfer function. Include deployment instructions.
Generated: DETERMINISTIC_8ef178dadf4fea1a
Batch ID: 20250612_152024
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# starknet_token.cairo

%lang starknet

# Declare the contract
@contract
struct TokenContract:

    # Storage variables
    @storage_var
    func balances(address: felt) -> felt:
        """Storage variable to hold token balances."""
        pass

    @storage_var
    func total_supply() -> felt:
        """Storage variable for total token supply."""
        pass

    # Event definitions
    @event
    func Transfer(sender: felt, recipient: felt, amount: felt):
        """Event emitted when tokens are transferred."""
        pass

    # Constructor
    @constructor
    func __init__(self, initial_supply: felt, owner: felt):
        """
        Constructor to initialize the token contract.
        
        Args:
            initial_supply (felt): The initial supply of tokens.
            owner (felt): The address of the owner who receives the initial supply.
        """
        total_supply.write(initial_supply)
        balances.write(owner, initial_supply)

    # Transfer function
    @external
    func transfer(sender: felt, recipient: felt, amount: felt):
        """
        Transfer tokens from one address to another.

        Args:
            sender (felt): The address of the sender.
            recipient (felt): The address of the recipient.
            amount (felt): The amount of tokens to transfer.
        
        Raises:
            If sender doesn't have enough balance or amount <= 0, raises an error.
        """
        let sender_balance = balances.read(sender)
        if sender_balance < amount:
            raise("Insufficient balance.")
        if amount <= 0:
            raise("Transfer amount must be greater than zero.")

        balances.write(sender, sender_balance - amount)
        let recipient_balance = balances.read(recipient)
        balances.write(recipient, recipient_balance + amount)

        Transfer.emit(sender=sender, recipient=recipient, amount=amount)

    # Read balance function
    @view
    func get_balance(address: felt) -> felt:
        """
        View function to get the balance of a specific address.

        Args:
            address (felt): The address whose balance is requested.

        Returns:
            felt: The token balance of the requested address.
        """
        return balances.read(address)

    # Read total supply function
    @view
    func get_total_supply() -> felt:
        """
        View function to get the total supply of tokens.

        Returns:
            felt: The total token supply.
        """
        return total_supply.read()


```

### Deployment Instructions:
1. Install StarkNet CLI tools on your machine.
2. Compile the contract:
   ```shell
   starknet-compile starknet_token.cairo --output starknet_token_compiled.json --abi starknet_token_abi.json
   ```
3. Deploy the contract:
   ```shell
   starknet deploy --contract starknet_token_compiled.json --inputs <initial_supply> <owner_address>
   ```
   Replace `<initial_supply>` with the initial token supply and `<owner_address>` with the owner's address in felt format.

4. Note the contract address from the deployment output for further interactions. Use the StarkNet CLI or SDK to invoke or query the contract methods.
