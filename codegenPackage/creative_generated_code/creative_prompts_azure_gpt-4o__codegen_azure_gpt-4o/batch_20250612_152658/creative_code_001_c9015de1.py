"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://thoreumdashboard.com
Prompt: Create a smart contract in Solidity that implements a token burning mechanism similar to Thoreum, where 1% of the supply is burned daily and 1% is burned on each transaction.
Generated: DETERMINISTIC_c9015de1756d6405
Batch ID: 20250612_152658
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
 * @title DailyBurnToken
 * @dev A smart contract implementing a token burning mechanism, where 1% of the total supply
 * is burned daily, and 1% is burned on each transaction.
 */
contract DailyBurnToken {
    string public name = "DailyBurnToken";
    string public symbol = "DBT";
    uint8 public decimals = 18;
    uint256 public totalSupply;

    mapping(address => uint256) public balanceOf;
    mapping(address => mapping(address => uint256)) public allowance;

    uint256 private constant DAILY_BURN_RATE = 100; // 1% (100 basis points)
    uint256 private constant TRANSACTION_BURN_RATE = 100; // 1% (100 basis points)

    uint256 private lastBurnTimestamp;

    event Transfer(address indexed from, address indexed to, uint256 value);
    event Approval(address indexed owner, address indexed spender, uint256 value);
    event Burn(uint256 amount);

    constructor(uint256 _initialSupply) {
        require(_initialSupply > 0, "Initial supply must be greater than zero");
        totalSupply = _initialSupply * (10**decimals);
        balanceOf[msg.sender] = totalSupply;
        lastBurnTimestamp = block.timestamp;
    }

    // Internal function to calculate the burn amount
    function _calculateBurnAmount(uint256 amount, uint256 rateBasisPoints) internal pure returns (uint256) {
        return (amount * rateBasisPoints) / 10000;
    }

    // Internal function to burn tokens
    function _burn(uint256 amount) internal {
        require(amount > 0, "Burn amount must be greater than zero");
        totalSupply -= amount;
        emit Burn(amount);
    }

    // Function to perform the daily burn (1% of total supply daily)
    function dailyBurn() external {
        require(block.timestamp >= lastBurnTimestamp + 1 days, "Daily burn can only be done once every 24 hours");
        uint256 burnAmount = _calculateBurnAmount(totalSupply, DAILY_BURN_RATE);
        _burn(burnAmount);
        lastBurnTimestamp = block.timestamp;
    }

    // Transfer function with 1% burn on each transaction
    function transfer(address to, uint256 value) external returns (bool) {
        require(to != address(0), "Invalid recipient address");
        require(balanceOf[msg.sender] >= value, "Insufficient balance");

        uint256 burnAmount = _calculateBurnAmount(value, TRANSACTION_BURN_RATE);
        uint256 transferAmount = value - burnAmount;

        balanceOf[msg.sender] -= value;
        balanceOf[to] += transferAmount;

        _burn(burnAmount);
        
        emit Transfer(msg.sender, to, transferAmount);
        return true;
    }

    // Function to approve allowance for a spender
    function approve(address spender, uint256 value) external returns (bool) {
        require(spender != address(0), "Invalid spender address");
        allowance[msg.sender][spender] = value;
        emit Approval(msg.sender, spender, value);
        return true;
    }

    // Transfer function with allowance (1% burn on each transaction)
    function transferFrom(address from, address to, uint256 value) external returns (bool) {
        require(to != address(0), "Invalid recipient address");
        require(balanceOf[from] >= value, "Insufficient balance");
        require(allowance[from][msg.sender] >= value, "Allowance exceeded");

        uint256 burnAmount = _calculateBurnAmount(value, TRANSACTION_BURN_RATE);
        uint256 transferAmount = value - burnAmount;

        balanceOf[from] -= value;
        balanceOf[to] += transferAmount;
        allowance[from][msg.sender] -= value;

        _burn(burnAmount);

        emit Transfer(from, to, transferAmount);
        return true;
    }
}
```
