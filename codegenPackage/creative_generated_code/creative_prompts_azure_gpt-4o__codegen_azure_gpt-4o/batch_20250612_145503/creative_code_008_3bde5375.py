"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://omikamicoin-ie.web.app
Prompt: Provide an example of a smart contract for a layer 1 blockchain similar to Omichain (OMI20) with Web3 integration.
Generated: DETERMINISTIC_3bde53758d6ea0dc
Batch ID: 20250612_145503
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/**
 * @title OMI20 Token Smart Contract
 * @dev Implementation of a basic fungible token following a simplified version of ERC20 standard
 */
contract OMI20Token {
    // Token metadata
    string public name = "OMI20Token";
    string public symbol = "OMI20";
    uint8 public decimals = 18;
    uint256 public totalSupply;

    // Mapping to track balances and allowances
    mapping(address => uint256) private balances;
    mapping(address => mapping(address => uint256)) private allowances;

    // Events for transfer and approval
    event Transfer(address indexed from, address indexed to, uint256 value);
    event Approval(address indexed owner, address indexed spender, uint256 value);

    // Constructor to initialize the total supply and assign to the deployer
    constructor(uint256 _initialSupply) {
        totalSupply = _initialSupply * (10 ** uint256(decimals));
        balances[msg.sender] = totalSupply;
        emit Transfer(address(0), msg.sender, totalSupply);
    }

    /**
     * @dev Get the balance of an account.
     * @param account Address to query the balance of.
     * @return The balance of the account.
     */
    function balanceOf(address account) public view returns (uint256) {
        return balances[account];
    }

    /**
     * @dev Transfer tokens to a recipient.
     * @param recipient Address of the recipient.
     * @param amount Amount of tokens to be transferred.
     * @return Success status of the transfer.
     */
    function transfer(address recipient, uint256 amount) public returns (bool) {
        require(recipient != address(0), "Transfer to zero address is not allowed");
        require(balances[msg.sender] >= amount, "Insufficient balance");

        // Adjust balances
        balances[msg.sender] -= amount;
        balances[recipient] += amount;

        emit Transfer(msg.sender, recipient, amount);
        return true;
    }

    /**
     * @dev Approve a spender to spend tokens on behalf of the caller.
     * @param spender Address of the spender.
     * @param amount Amount of tokens to approve.
     * @return Success status of the approval.
     */
    function approve(address spender, uint256 amount) public returns (bool) {
        require(spender != address(0), "Approval to zero address is not allowed");

        allowances[msg.sender][spender] = amount;
        emit Approval(msg.sender, spender, amount);
        return true;
    }

    /**
     * @dev Check the allowance of a spender for a given owner.
     * @param owner Address of the token owner.
     * @param spender Address of the spender.
     * @return Remaining allowance for the spender.
     */
    function allowance(address owner, address spender) public view returns (uint256) {
        return allowances[owner][spender];
    }

    /**
     * @dev Transfer tokens from one account to another on behalf of the owner.
     * @param sender Address of the token owner.
     * @param recipient Address of the recipient.
     * @param amount Amount of tokens to be transferred.
     * @return Success status of the transfer.
     */
    function transferFrom(address sender, address recipient, uint256 amount) public returns (bool) {
        require(sender != address(0), "Transfer from zero address is not allowed");
        require(recipient != address(0), "Transfer to zero address is not allowed");
        require(balances[sender] >= amount, "Insufficient balance");
        require(allowances[sender][msg.sender] >= amount, "Transfer amount exceeds allowance");

        // Adjust balances and allowance
        balances[sender] -= amount;
        balances[recipient] += amount;
        allowances[sender][msg.sender] -= amount;

        emit Transfer(sender, recipient, amount);
        return true;
    }
}
```

```javascript
// Web3 Integration for interacting with the OMI20Token contract

// Importing Web3 (Ensure web3 is installed: npm install web3)
const Web3 = require('web3');

// ABI of the deployed contract (replace with the actual ABI from your compiled contract)
const abi = [
  /* ABI JSON here */
];

// Address of the deployed contract (replace with the actual contract address)
const contractAddress = "0x...";

// Initialize Web3 instance (Assumes a provider like MetaMask is injected)
const web3 = new Web3(window.ethereum);

// Connect to the contract
const omi20Contract = new web3.eth.Contract(abi, contractAddress);

/**
 * @dev Get token balance of an account
 * @param account Address to check the balance for.
 */
async function getBalance(account) {
  try {
    const balance = await omi20Contract.methods.balanceOf(account).call();
    console.log(`Balance of ${account}: ${web3.utils.fromWei(balance, 'ether')} OMI20`);
  } catch (error) {
    console.error("Error fetching balance:", error);
  }
}

/**
 * @dev Transfer tokens to a recipient
 * @param sender Address of the sender (must be connected to Web3 wallet).
 * @param recipient Address of the recipient.
 * @param amount Amount of tokens to transfer (in Wei).
 */
async function transferTokens(sender, recipient, amount) {
  try {
    const amountInWei = web3.utils.toWei(amount.toString(), 'ether');
    await omi20Contract.methods.transfer(recipient, amountInWei).send({ from: sender });
    console.log(`Successfully transferred ${amount} OMI20 to ${recipient}`);
  } catch (error) {
    console.error("Error transferring tokens:", error);
  }
}

/**
 * @dev Approve a spender to transfer tokens on behalf of the sender.
 * @param sender Address of the owner (must be connected to Web3 wallet).
 * @param spender Address of the spender.
 * @param amount Amount to approve (in Wei).
 */
async function approveSpender(sender, spender, amount) {
  try {
    const amountInWei = web3.utils.toWei(amount.toString(), 'ether');
    await omi20Contract.methods.approve(spender, amountInWei).send({ from: sender });
    console.log(`Approved ${spender} to spend ${amount} OMI20`);
  } catch (error) {
    console.error("Error approving allowance:", error);
  }
}

/**
 * @dev Transfer tokens on behalf of a sender.
 * @param sender Address of the token owner.
 * @param spender Address of the caller/approved spender (must be connected to Web3 wallet).
 * @param recipient Address of the recipient.
 * @param amount Amount to transfer (in Wei).
 */
async function transferFrom(sender, spender, recipient, amount) {
  try {
    const amountInWei = web3.utils.toWei(amount.toString(), 'ether');
    await omi20Contract.methods.transferFrom(sender, recipient, amountInWei).send({ from: spender });
    console.log(`Transferred ${amount} OMI20 from ${sender} to ${recipient}`);
  } catch (error) {
    console.error("Error transferring tokens:", error);
  }
}

// Example Usage:
// Make sure to connect a wallet (e.g., MetaMask) before calling these functions
// getBalance("0xYourAddressHere");
// transferTokens("0xYourAddressHere", "0xRecipientAddressHere", 100);
// approveSpender("0xYourAddressHere", "0xSpenderAddressHere", 50);
// transferFrom("0xOwnerAddressHere", "0xYourAddressHere", "0xRecipientAddressHere", 25);
```
