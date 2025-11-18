"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://starknet.news
Prompt: Create a tutorial-style code snippet for deploying a zk-STARK-based token on Starknet. Include steps for testing and verifying the deployment.
Generated: DETERMINISTIC_bba52c7c135ffa10
Batch ID: 20250612_153809
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Tutorial: Deploying a zk-STARK-based token on Starknet
# Language: Python using Cairo (Starknet's programming language)

# Step 1: Install the necessary tools
# Ensure you have Starknet CLI installed and set up.

# Step 2: Write the Cairo contract for the token
# File: starknet_token.cairo
"""
%lang starknet

@contract_interface
namespace ERC20 {
    func name() -> (name: felt);
    func symbol() -> (symbol: felt);
    func decimals() -> (decimals: felt);
    func totalSupply() -> (totalSupply: felt);
    func balanceOf(account: felt) -> (balance: felt);
    func transfer(recipient: felt, amount: felt);
    func mint(recipient: felt, amount: felt);
}
"""

@storage_var
func balance(account: felt) -> (balance: felt) {
    # Storage variable for account balances
}

@storage_var
func total_supply() -> (totalSupply: felt) {
    # Storage variable for total supply
}

@external
func name() -> (name: felt) {
    return ("MyToken");
}

@external
func symbol() -> (symbol: felt) {
    return ("MTK");
}

@external
func decimals() -> (decimals: felt) {
    return (18);
}

@external
func totalSupply() -> (totalSupply: felt) {
    let (totalSupply) = total_supply.read();
    return (totalSupply);
}

@external
func balanceOf(account: felt) -> (balance: felt) {
    let (balance) = balance.read(account);
    return (balance);
}

@external
func transfer(recipient: felt, amount: felt) {
    let (sender_balance) = balance.read(caller_address());
    if sender_balance < amount {
        # Revert if insufficient balance
        panic("Insufficient balance");
    }
    balance.write(caller_address(), sender_balance - amount);
    let (recipient_balance) = balance.read(recipient);
    balance.write(recipient, recipient_balance + amount);
}

@external
func mint(recipient: felt, amount: felt) {
    let (current_total_supply) = total_supply.read();
    total_supply.write(current_total_supply + amount);
    let (recipient_balance) = balance.read(recipient);
    balance.write(recipient, recipient_balance + amount);
}
"""

# Step 3: Deploy the contract to Starknet
# Run the following command in your terminal:
# starknet-cli deploy --contract starknet_token.cairo --network testnet

# Step 4: Test the contract
# File: test_starknet_token.py
"""
import asyncio
from starknet_py.net.account.account import Account
from starknet_py.net.client import Client
from starknet_py.contract import Contract

async def test_token():
    # Connect to the Starknet testnet
    client = Client(net="testnet")
    
    # Use your deployed contract address
    contract_address = "0xYourContractAddress"
    token_contract = await Contract.from_address(contract_address, client)

    # Verify the token name
    name = await token_contract.functions["name"].call()
    print("Token Name:", name)

    # Verify the token symbol
    symbol = await token_contract.functions["symbol"].call()
    print("Token Symbol:", symbol)

    # Verify minting and transferring tokens
    account = Account(address="0xYourAccountAddress", private_key="YourPrivateKey", client=client)
    recipient = "0xRecipientAddress"
    mint_tx = await token_contract.functions["mint"].invoke(recipient, 1000, account=account)
    await mint_tx.wait_for_acceptance()
    print("Minted 1000 tokens")

    balance = await token_contract.functions["balanceOf"].call(recipient)
    print(f"Recipient Balance: {balance}")

    transfer_tx = await token_contract.functions["transfer"].invoke(recipient, 500, account=account)
    await transfer_tx.wait_for_acceptance()
    print("Transferred 500 tokens")

# Execute the test
asyncio.run(test_token())
"""

# Step 5: Verify the Deployment
# Use the Starknet block explorer or CLI tools to inspect the contract state.
# Confirm that the token contract is deployed and accessible.
```
