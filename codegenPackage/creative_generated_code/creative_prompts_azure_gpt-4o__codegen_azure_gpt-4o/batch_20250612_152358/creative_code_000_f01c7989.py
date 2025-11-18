"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://milady-dfk.pages.dev
Prompt: Write a smart contract in Solidity for a token similar to $CULT, incorporating features like algorithmic distribution and loyalty-based claims as described in the Milady Cult ecosystem.
Generated: DETERMINISTIC_f01c7989845c9078
Batch ID: 20250612_152358
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
 * @title CultToken
 * @dev ERC20-like token with algorithmic distribution and loyalty-based claims.
 */
contract CultToken {
    // Token metadata
    string public name = "CultToken";
    string public symbol = "CULT";
    uint8 public decimals = 18;
    uint256 public totalSupply;

    // Mapping to track balances and allowances
    mapping(address => uint256) private balances;
    mapping(address => mapping(address => uint256)) private allowances;

    // Loyalty program tracking
    mapping(address => uint256) private loyaltyPoints;
    mapping(address => uint256) private lastClaimed;

    // Events for transparency and logging
    event Transfer(address indexed from, address indexed to, uint256 value);
    event Approval(address indexed owner, address indexed spender, uint256 value);
    event LoyaltyClaimed(address indexed user, uint256 points, uint256 reward);

    // Distribution settings
    uint256 public constant ALGORITHM_DISTRIBUTION_RATE = 5; // Percentage
    uint256 public constant LOYALTY_REWARD_RATE = 2;        // Percentage
    uint256 public constant CLAIM_COOLDOWN = 1 days;

    // Owner of the contract
    address public owner;

    // Modifier to restrict functions to owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    // Constructor to initialize the token and set the owner
    constructor(uint256 initialSupply) {
        owner = msg.sender;
        totalSupply = initialSupply * (10**decimals);
        balances[owner] = totalSupply;
        emit Transfer(address(0), owner, totalSupply);
    }

    /**
     * @dev Transfer tokens to a specified address while applying algorithmic distribution.
     */
    function transfer(address to, uint256 amount) external returns (bool) {
        require(to != address(0), "Transfer to zero address is not allowed");
        require(balances[msg.sender] >= amount, "Insufficient balance");

        // Applying algorithmic distribution
        uint256 distributionAmount = (amount * ALGORITHM_DISTRIBUTION_RATE) / 100;
        uint256 transferAmount = amount - distributionAmount;

        balances[msg.sender] -= amount;
        balances[to] += transferAmount;
        balances[owner] += distributionAmount; // Distribution added to owner's balance as an example

        // Update loyalty points
        loyaltyPoints[to] += transferAmount;

        emit Transfer(msg.sender, to, transferAmount);
        return true;
    }

    /**
     * @dev Approve another address to spend tokens on behalf of the sender.
     */
    function approve(address spender, uint256 amount) external returns (bool) {
        require(spender != address(0), "Approve to zero address not allowed");

        allowances[msg.sender][spender] = amount;
        emit Approval(msg.sender, spender, amount);
        return true;
    }

    /**
     * @dev Transfer tokens from one address to another, using an allowance.
     */
    function transferFrom(
        address from,
        address to,
        uint256 amount
    ) external returns (bool) {
        require(from != address(0), "Transfer from zero address not allowed");
        require(to != address(0), "Transfer to zero address not allowed");
        require(balances[from] >= amount, "Insufficient balance");
        require(allowances[from][msg.sender] >= amount, "Allowance exceeded");

        // Applying algorithmic distribution
        uint256 distributionAmount = (amount * ALGORITHM_DISTRIBUTION_RATE) / 100;
        uint256 transferAmount = amount - distributionAmount;

        balances[from] -= amount;
        balances[to] += transferAmount;
        balances[owner] += distributionAmount; // Distribution added to owner's balance as an example
        allowances[from][msg.sender] -= amount;

        // Update loyalty points
        loyaltyPoints[to] += transferAmount;

        emit Transfer(from, to, transferAmount);
        return true;
    }

    /**
     * @dev Check the balance of an address.
     */
    function balanceOf(address account) external view returns (uint256) {
        return balances[account];
    }

    /**
     * @dev Check the allowance set for a spender by an owner.
     */
    function allowance(address owner, address spender) external view returns (uint256) {
        return allowances[owner][spender];
    }

    /**
     * @dev Allow users to claim their loyalty rewards based on accumulated points.
     */
    function claimLoyaltyRewards() external {
        require(block.timestamp > lastClaimed[msg.sender] + CLAIM_COOLDOWN, "Claim cooldown active");

        uint256 points = loyaltyPoints[msg.sender];
        require(points > 0, "No loyalty points available");

        // Calculate reward based on loyalty points
        uint256 reward = (points * LOYALTY_REWARD_RATE) / 100;
        require(balances[owner] >= reward, "Insufficient reward balance in contract");

        // Reset loyalty points and update claim timestamps
        loyaltyPoints[msg.sender] = 0;
        lastClaimed[msg.sender] = block.timestamp;

        // Transfer reward from owner to the claimant
        balances[owner] -= reward;
        balances[msg.sender] += reward;

        emit LoyaltyClaimed(msg.sender, points, reward);
    }

    /**
     * @dev Mint new tokens to the owner's balance.
     * Restricted to the contract owner.
     */
    function mint(uint256 amount) external onlyOwner {
        uint256 mintedAmount = amount * (10**decimals);
        totalSupply += mintedAmount;
        balances[owner] += mintedAmount;
        emit Transfer(address(0), owner, mintedAmount);
    }

    /**
     * @dev Burn tokens from the owner's balance, reducing total supply.
     * Restricted to the contract owner.
     */
    function burn(uint256 amount) external onlyOwner {
        require(balances[owner] >= amount, "Insufficient balance to burn");

        uint256 burnedAmount = amount * (10**decimals);
        totalSupply -= burnedAmount;
        balances[owner] -= burnedAmount;
        emit Transfer(owner, address(0), burnedAmount);
    }
}
```
