"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://d-510.pages.dev
Prompt: Generate a sample smart contract for a utility token like Lingo that supports a gamified rewards system.
Generated: DETERMINISTIC_bb2f408173170978
Batch ID: 20250612_163338
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
 * @title LingoToken
 * @dev ERC20-based utility token with a gamified rewards system.
 */
contract LingoToken {
    // Public variables
    string public constant name = "LingoToken";
    string public constant symbol = "LINGO";
    uint8 public constant decimals = 18;
    uint256 public totalSupply;

    // Mappings for balances and allowances
    mapping(address => uint256) private balances;
    mapping(address => mapping(address => uint256)) private allowances;

    // Owner of the contract
    address public owner;

    // Event declarations
    event Transfer(address indexed from, address indexed to, uint256 value);
    event Approval(address indexed owner, address indexed spender, uint256 value);
    event RewardsEarned(address indexed player, uint256 rewardAmount);

    // Modifier to restrict access to owner-only functions
    modifier onlyOwner() {
        require(msg.sender == owner, "You are not the owner.");
        _;
    }

    // Constructor to initialize token supply
    constructor(uint256 _initialSupply) {
        owner = msg.sender;
        totalSupply = _initialSupply * 10**decimals;
        balances[owner] = totalSupply;
        emit Transfer(address(0), owner, totalSupply);
    }

    // Function to check balance of an account
    function balanceOf(address account) external view returns (uint256) {
        return balances[account];
    }

    // Function to transfer tokens
    function transfer(address to, uint256 amount) external returns (bool) {
        require(to != address(0), "Transfer to zero address not allowed.");
        require(balances[msg.sender] >= amount, "Insufficient balance.");

        balances[msg.sender] -= amount;
        balances[to] += amount;

        emit Transfer(msg.sender, to, amount);
        return true;
    }

    // Function to approve spending by another account
    function approve(address spender, uint256 amount) external returns (bool) {
        allowances[msg.sender][spender] = amount;
        emit Approval(msg.sender, spender, amount);
        return true;
    }

    // Function to check allowance
    function allowance(address owner, address spender) external view returns (uint256) {
        return allowances[owner][spender];
    }

    // Function to transfer tokens on behalf of another account
    function transferFrom(
        address from,
        address to,
        uint256 amount
    ) external returns (bool) {
        require(to != address(0), "Transfer to zero address not allowed.");
        require(balances[from] >= amount, "Insufficient balance.");
        require(allowances[from][msg.sender] >= amount, "Allowance exceeded.");

        allowances[from][msg.sender] -= amount;
        balances[from] -= amount;
        balances[to] += amount;

        emit Transfer(from, to, amount);
        return true;
    }

    // Function to mint new tokens (owner-only)
    function mint(address to, uint256 amount) external onlyOwner {
        require(to != address(0), "Mint to zero address not allowed.");

        uint256 mintAmount = amount * 10**decimals;
        totalSupply += mintAmount;
        balances[to] += mintAmount;

        emit Transfer(address(0), to, mintAmount);
    }

    // Function to burn tokens (owner-only)
    function burn(address from, uint256 amount) external onlyOwner {
        require(from != address(0), "Burn from zero address not allowed.");
        require(balances[from] >= amount, "Insufficient balance.");

        uint256 burnAmount = amount * 10**decimals;
        totalSupply -= burnAmount;
        balances[from] -= burnAmount;

        emit Transfer(from, address(0), burnAmount);
    }

    // Gamified rewards system: issue reward tokens based on game logic
    function issueRewards(address player, uint256 rewardAmount) external onlyOwner {
        require(player != address(0), "Reward to zero address not allowed.");
        require(rewardAmount > 0, "Reward amount must be greater than zero.");

        uint256 scaledReward = rewardAmount * 10**decimals;
        totalSupply += scaledReward;
        balances[player] += scaledReward;

        emit RewardsEarned(player, rewardAmount);
        emit Transfer(address(0), player, scaledReward);
    }
}
```
