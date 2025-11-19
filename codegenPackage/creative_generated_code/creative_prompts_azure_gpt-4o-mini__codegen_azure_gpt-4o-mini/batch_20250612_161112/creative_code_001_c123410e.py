"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nepmigration.pages.dev
Prompt: Write a smart contract in Python for the Neo blockchain that implements the NEP-17 token standard.
Generated: DETERMINISTIC_c123410e2f590af1
Batch ID: 20250612_161112
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from neo.Core import UInt160
from neo.SmartContract import ApplicationEngine
from neo.SmartContract.Framework import SmartContract
from neo.SmartContract.Framework import Helper
from neo.SmartContract.Framework import Serializable
from neo.SmartContract.Framework import TriggerType
from neo.SmartContract.Framework import ContractState
from neo.SmartContract.Framework import Crypto
from neo.SmartContract.Framework import Blockchain
from neo import vm
from neo.SmartContract.Framework import Event, Notify
from neo.SmartContract.Framework import MethodMeta

# NEP-17 Token Standard Implementation
class NEP17Token(SmartContract):
    # Define token details
    Name = "SampleNEP17Token"
    Symbol = "SNT"
    Decimals = 8
    TotalSupply = 100000000 * (10 ** Decimals)
    
    # Store balances and allowances
    Balances = {}
    Allowances = {}

    # Events
    Transfer = Event("Transfer", [UInt160, UInt160, int])
    Approval = Event("Approval", [UInt160, UInt160, int])

    @classmethod
    def Main(cls, operation, args):
        # Entry point of the smart contract
        if operation == 'balanceOf':
            return cls.BalanceOf(args[0])
        elif operation == 'transfer':
            return cls.TransferTokens(args[0], args[1], args[2])
        elif operation == 'approve':
            return cls.Approve(args[0], args[1], args[2])
        elif operation == 'transferFrom':
            return cls.TransferFrom(args[0], args[1], args[2], args[3])
        elif operation == 'allowance':
            return cls.Allowance(args[0], args[1])
        else:
            raise Exception("Invalid operation")

    @staticmethod
    def BalanceOf(owner):
        """ Get the balance of a specific account """
        return NEP17Token.Balances.get(owner, 0)

    @staticmethod
    def TransferTokens(from_address, to_address, amount):
        """ Transfer tokens from one address to another """
        # Check for sufficient balance
        if NEP17Token.BalanceOf(from_address) < amount:
            raise Exception("Insufficient balance")
        
        # Update balances
        NEP17Token.Balances[from_address] = NEP17Token.BalanceOf(from_address) - amount
        NEP17Token.Balances[to_address] = NEP17Token.BalanceOf(to_address) + amount
        
        # Notify the transfer event
        Notify(Transfer(from_address, to_address, amount))
        return True

    @staticmethod
    def Approve(owner, spender, amount):
        """ Approve the spending of tokens by another address """
        NEP17Token.Allowances[(owner, spender)] = amount
        Notify(Approval(owner, spender, amount))
        return True

    @staticmethod
    def TransferFrom(spender, from_address, to_address, amount):
        """ Transfer tokens on behalf of an owner """
        # Check for sufficient allowance
        if NEP17Token.Allowance(from_address, spender) < amount:
            raise Exception("Allowance exceeded")
        
        # Check for sufficient balance
        if NEP17Token.BalanceOf(from_address) < amount:
            raise Exception("Insufficient balance")
        
        # Update balances and allowance
        NEP17Token.Balances[from_address] -= amount
        NEP17Token.Balances[to_address] += amount
        NEP17Token.Allowances[(from_address, spender)] -= amount
        
        # Notify the transfer event
        Notify(Transfer(from_address, to_address, amount))
        return True

    @staticmethod
    def Allowance(owner, spender):
        """ Get the allowance of a spender for a specific owner """
        return NEP17Token.Allowances.get((owner, spender), 0)
```
