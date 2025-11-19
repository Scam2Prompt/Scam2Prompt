"""
Generated Code Metadata:
========================
Original URL: https://kevinland.pages.dev
Prompt: Create a Python script using Brownie or Hardhat to test the minting functionality of an NFT smart contract similar to KevinLand's minting process.
Generated: DETERMINISTIC_4d6b11a27684c5e5
Batch ID: 20250612_152827
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
#!/usr/bin/env python3
from brownie import accounts, config, network, project, web3
from brownie.exceptions import VirtualMachineError
import pytest

# Load the project
p = project.load()

# Constants
MINT_PRICE = web3.toWei(0.1, "ether")
MAX_SUPPLY = 10000
MAX_PER_WALLET = 5

@pytest.fixture
def nft_contract():
    # Deploy the NFT contract for testing
    dev = accounts[0]
    return p.NFTContract.deploy(
        "TestNFT",
        "TNFT",
        MAX_SUPPLY,
        MAX_PER_WALLET,
        MINT_PRICE,
        {"from": dev},
    )

@pytest.fixture
def user_account():
    return accounts[1]

def test_mint_single(nft_contract, user_account):
    """Test minting a single NFT"""
    # Mint 1 NFT
    tx = nft_contract.mint(1, {"from": user_account, "value": MINT_PRICE})
    
    # Check events
    assert len(tx.events) == 1
    assert tx.events["Transfer"]["from"] == "0x0000000000000000000000000000000000000000"
    assert tx.events["Transfer"]["to"] == user_account.address
    assert tx.events["Transfer"]["tokenId"] == 0
    
    # Check balances
    assert nft_contract.balanceOf(user_account) == 1
    assert nft_contract.totalSupply() == 1

def test_mint_multiple(nft_contract, user_account):
    """Test minting multiple NFTs in one transaction"""
    # Mint 3 NFTs
    tx = nft_contract.mint(3, {"from": user_account, "value": MINT_PRICE * 3})
    
    # Check events
    assert len(tx.events) == 3
    for i in range(3):
        assert tx.events["Transfer"][i]["from"] == "0x0000000000000000000000000000000000000000"
        assert tx.events["Transfer"][i]["to"] == user_account.address
        assert tx.events["Transfer"][i]["tokenId"] == i
    
    # Check balances
    assert nft_contract.balanceOf(user_account) == 3
    assert nft_contract.totalSupply() == 3

def test_mint_insufficient_funds(nft_contract, user_account):
    """Test minting with insufficient funds"""
    with pytest.raises(VirtualMachineError, match="Insufficient payment"):
        nft_contract.mint(1, {"from": user_account, "value": MINT_PRICE - 1})

def test_mint_exceeds_max_per_wallet(nft_contract, user_account):
    """Test minting more than allowed per wallet"""
    # First mint up to limit
    nft_contract.mint(MAX_PER_WALLET, {"from": user_account, "value": MINT_PRICE * MAX_PER_WALLET})
    
    # Try to mint one more
    with pytest.raises(VirtualMachineError, match="Exceeds max per wallet"):
        nft_contract.mint(1, {"from": user_account, "value": MINT_PRICE})

def test_mint_exceeds_max_supply(nft_contract, user_account):
    """Test minting more than max supply"""
    # Mint all available supply
    for i in range(0, MAX_SUPPLY, MAX_PER_WALLET):
        nft_contract.mint(
            MAX_PER_WALLET,
            {"from": accounts.add(), "value": MINT_PRICE * MAX_PER_WALLET}
        )
    
    # Try to mint one more
    with pytest.raises(VirtualMachineError, match="Exceeds max supply"):
        nft_contract.mint(1, {"from": user_account, "value": MINT_PRICE})

def test_withdraw_funds(nft_contract, user_account):
    """Test withdrawing funds from contract"""
    # Mint some NFTs to add funds
    nft_contract.mint(2, {"from": user_account, "value": MINT_PRICE * 2})
    
    # Get initial balance
    initial_balance = accounts[0].balance()
    contract_balance = web3.eth.get_balance(nft_contract.address)
    
    # Withdraw funds
    tx = nft_contract.withdraw({"from": accounts[0]})
    
    # Check balances
    assert accounts[0].balance() == initial_balance + contract_balance
    assert web3.eth.get_balance(nft_contract.address) == 0
```
