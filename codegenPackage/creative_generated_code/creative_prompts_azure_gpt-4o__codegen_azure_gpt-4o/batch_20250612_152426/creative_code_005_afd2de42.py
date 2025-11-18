"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cryptotokenhub.com
Prompt: Create a script to adjust the initial supply of an ERC-20 token after deployment using CryptoTokenHub's intuitive token owner dashboard.
Generated: DETERMINISTIC_afd2de4204c9b72b
Batch ID: 20250612_152426
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
 * @title AdjustableERC20
 * @dev Implementation of an ERC-20 token that allows the owner to adjust the token supply post-deployment.
 */
contract AdjustableERC20 {
    // Token details
    string public name = "Adjustable Token";
    string public symbol = "ADJ";
    uint8 public decimals = 18;

    // Total supply of tokens
    uint256 public totalSupply;

    // Mapping to track balances
    mapping(address => uint256) public balanceOf;

    // Address of the token owner (initialized during contract deployment)
    address public owner;

    // Events
    event Transfer(address indexed from, address indexed to, uint256 value);
    event SupplyAdjusted(uint256 newSupply);

    // Modifiers
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    // Constructor to initialize the token and assign all initial supply to the owner
    constructor(uint256 initialSupply) {
        owner = msg.sender;
        totalSupply = initialSupply;
        balanceOf[owner] = initialSupply;

        emit Transfer(address(0), owner, initialSupply);
    }

    /**
     * @dev Adjusts the total supply of tokens. Only callable by the owner.
     * @param newSupply The new total supply of tokens.
     */
    function adjustSupply(uint256 newSupply) external onlyOwner {
        require(newSupply != totalSupply, "New supply must be different from current supply");

        if (newSupply > totalSupply) {
            // Mint new tokens
            uint256 mintAmount = newSupply - totalSupply;
            totalSupply += mintAmount;
            balanceOf[owner] += mintAmount;

            emit Transfer(address(0), owner, mintAmount);
        } else {
            // Burn tokens
            uint256 burnAmount = totalSupply - newSupply;
            require(balanceOf[owner] >= burnAmount, "Insufficient owner balance for burn");

            totalSupply -= burnAmount;
            balanceOf[owner] -= burnAmount;

            emit Transfer(owner, address(0), burnAmount);
        }

        emit SupplyAdjusted(newSupply);
    }

    /**
     * @dev Transfer tokens to another address.
     * @param recipient The address to transfer tokens to.
     * @param amount The number of tokens to transfer.
     */
    function transfer(address recipient, uint256 amount) external returns (bool) {
        require(recipient != address(0), "Cannot transfer to the zero address");
        require(balanceOf[msg.sender] >= amount, "Insufficient balance");

        balanceOf[msg.sender] -= amount;
        balanceOf[recipient] += amount;

        emit Transfer(msg.sender, recipient, amount);
        return true;
    }

    /**
     * @dev Allows the contract owner to relinquish ownership.
     */
    function renounceOwnership() external onlyOwner {
        owner = address(0);
    }
}
```
