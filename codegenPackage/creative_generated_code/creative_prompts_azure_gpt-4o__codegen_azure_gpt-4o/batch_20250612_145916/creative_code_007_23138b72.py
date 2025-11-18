"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tokenscreator-web3.pages.dev
Prompt: Provide a Solidity code snippet for ensuring 100% token ownership during token creation, as emphasized on the Tokens Creator website.
Generated: DETERMINISTIC_23138b72892d231f
Batch ID: 20250612_145916
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
 * @title TokenWithFullOwnership
 * @dev A simple ERC20-like token contract ensuring 100% ownership to the deployer during token creation.
 */
contract TokenWithFullOwnership {
    // Token details
    string public name;
    string public symbol;
    uint8 public decimals;
    uint256 public totalSupply;

    // Balances mapped to addresses
    mapping(address => uint256) private balances;

    // Events for logging transfers
    event Transfer(address indexed from, address indexed to, uint256 value);

    /**
     * @dev Initializes the contract with token details and assigns total supply to the deployer.
     * @param _name Name of the token.
     * @param _symbol Symbol of the token.
     * @param _decimals Number of decimal places for the token.
     * @param _totalSupply Initial total supply of the token.
     */
    constructor(
        string memory _name,
        string memory _symbol,
        uint8 _decimals,
        uint256 _totalSupply
    ) {
        // Validate input arguments
        require(_totalSupply > 0, "Total supply must be greater than zero");

        // Set token details
        name = _name;
        symbol = _symbol;
        decimals = _decimals;
        totalSupply = _totalSupply;

        // Assign the total supply to the deployer's address
        balances[msg.sender] = _totalSupply;

        // Emit a Transfer event for transparency
        emit Transfer(address(0), msg.sender, _totalSupply);
    }

    /**
     * @dev Returns the balance of a specific address.
     * @param account Address to query the balance of.
     */
    function balanceOf(address account) external view returns (uint256) {
        return balances[account];
    }

    /**
     * @dev Transfers tokens from the caller to a specified address.
     * @param recipient Address to transfer tokens to.
     * @param amount Amount of tokens to transfer.
     */
    function transfer(address recipient, uint256 amount) external returns (bool) {
        // Validate inputs
        require(recipient != address(0), "Transfer to the zero address is not allowed");
        require(amount > 0, "Transfer amount must be greater than zero");
        require(balances[msg.sender] >= amount, "Insufficient balance");

        // Perform the transfer
        balances[msg.sender] -= amount;
        balances[recipient] += amount;

        // Emit the Transfer event
        emit Transfer(msg.sender, recipient, amount);

        return true;
    }
}
```
