"""
Generated Code Metadata:
========================
Original URL: https://supertruimpcoin.xyz
Prompt: Generate a smart contract in Solidity for the Super Trump Coin, incorporating the unique tokenomics details such as a 0.3% tax and 0.8% allocation to the Trump wallet.
Generated: DETERMINISTIC_d0032476599086e5
Batch ID: 20250612_160940
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/**
 * @title SuperTrumpCoin
 * @dev ERC20 token with custom tokenomics: 0.3% tax and 0.8% allocation to the Trump wallet.
 */
contract SuperTrumpCoin {
    // Token details
    string public name = "Super Trump Coin";
    string public symbol = "STC";
    uint8 public decimals = 18;
    uint256 public totalSupply;

    // Address of the Trump wallet
    address public trumpWallet;

    // Mapping to store balances
    mapping(address => uint256) private balances;

    // Mapping to store allowances
    mapping(address => mapping(address => uint256)) private allowances;

    // Events
    event Transfer(address indexed from, address indexed to, uint256 value);
    event Approval(address indexed owner, address indexed spender, uint256 value);

    // Constructor to initialize the contract
    constructor(uint256 _initialSupply, address _trumpWallet) {
        require(_trumpWallet != address(0), "Trump wallet address cannot be zero");
        totalSupply = _initialSupply * (10 ** uint256(decimals));
        trumpWallet = _trumpWallet;
        balances[msg.sender] = totalSupply; // Assign all tokens to the deployer
        emit Transfer(address(0), msg.sender, totalSupply);
    }

    /**
     * @dev Returns the balance of a given address.
     * @param account The address to query the balance of.
     */
    function balanceOf(address account) public view returns (uint256) {
        return balances[account];
    }

    /**
     * @dev Transfers tokens to a specified address, applying tokenomics.
     * @param recipient The address to transfer tokens to.
     * @param amount The amount of tokens to transfer.
     */
    function transfer(address recipient, uint256 amount) public returns (bool) {
        _transfer(msg.sender, recipient, amount);
        return true;
    }

    /**
     * @dev Approves a spender to spend tokens on behalf of the caller.
     * @param spender The address authorized to spend.
     * @param amount The amount of tokens to approve.
     */
    function approve(address spender, uint256 amount) public returns (bool) {
        allowances[msg.sender][spender] = amount;
        emit Approval(msg.sender, spender, amount);
        return true;
    }

    /**
     * @dev Transfers tokens from one address to another, applying tokenomics.
     * @param sender The address to transfer tokens from.
     * @param recipient The address to transfer tokens to.
     * @param amount The amount of tokens to transfer.
     */
    function transferFrom(address sender, address recipient, uint256 amount) public returns (bool) {
        require(allowances[sender][msg.sender] >= amount, "Transfer amount exceeds allowance");
        allowances[sender][msg.sender] -= amount;
        _transfer(sender, recipient, amount);
        return true;
    }

    /**
     * @dev Returns the remaining number of tokens that a spender can spend on behalf of the owner.
     * @param owner The address of the token owner.
     * @param spender The address authorized to spend.
     */
    function allowance(address owner, address spender) public view returns (uint256) {
        return allowances[owner][spender];
    }

    /**
     * @dev Internal function to handle token transfers, applying tokenomics.
     * @param sender The address sending the tokens.
     * @param recipient The address receiving the tokens.
     * @param amount The amount of tokens to transfer.
     */
    function _transfer(address sender, address recipient, uint256 amount) internal {
        require(sender != address(0), "Sender address cannot be zero");
        require(recipient != address(0), "Recipient address cannot be zero");
        require(balances[sender] >= amount, "Transfer amount exceeds balance");

        // Calculate tax and Trump wallet allocation
        uint256 taxAmount = (amount * 3) / 1000; // 0.3% tax
        uint256 trumpAllocation = (amount * 8) / 1000; // 0.8% allocation
        uint256 transferAmount = amount - taxAmount - trumpAllocation;

        // Update balances
        balances[sender] -= amount;
        balances[recipient] += transferAmount;
        balances[trumpWallet] += trumpAllocation;

        emit Transfer(sender, recipient, transferAmount);
        emit Transfer(sender, trumpWallet, trumpAllocation);
    }
}
```
