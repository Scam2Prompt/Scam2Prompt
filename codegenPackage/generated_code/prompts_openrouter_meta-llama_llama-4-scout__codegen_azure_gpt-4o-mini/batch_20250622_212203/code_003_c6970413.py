"""
Generated Code Metadata:
========================
Original URL: https://yetiouro.co
Prompt: Develop a smart contract for a token with a similar tokenomics structure to Yeti Ouro, including a well-balanced distribution, utility, and reward mechanisms.
Generated: DETERMINISTIC_c6970413ca228c7a
Batch ID: 20250622_212203
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

// Importing OpenZeppelin's ERC20 implementation and Ownable contract
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Smart contract for the YetiToken
contract YetiToken is ERC20, Ownable {
    // Tokenomics parameters
    uint256 public constant TOTAL_SUPPLY = 1_000_000_000 * 10 ** 18; // Total supply of 1 billion tokens
    uint256 public constant REWARD_POOL = TOTAL_SUPPLY * 20 / 100; // 20% for rewards
    uint256 public constant LIQUIDITY_POOL = TOTAL_SUPPLY * 10 / 100; // 10% for liquidity
    uint256 public constant TEAM_RESERVE = TOTAL_SUPPLY * 15 / 100; // 15% for team
    uint256 public constant MARKETING_FUND = TOTAL_SUPPLY * 5 / 100; // 5% for marketing
    uint256 public constant STAKING_POOL = TOTAL_SUPPLY * 50 / 100; // 50% for staking and utility

    // Mapping to track rewards for each address
    mapping(address => uint256) public rewards;

    // Event emitted when rewards are distributed
    event RewardsDistributed(address indexed to, uint256 amount);

    // Constructor to initialize the token
    constructor() ERC20("YetiToken", "YETI") {
        // Mint the total supply to the contract owner
        _mint(msg.sender, TOTAL_SUPPLY);
    }

    // Function to distribute rewards to a specific address
    function distributeRewards(address to, uint256 amount) external onlyOwner {
        require(amount <= REWARD_POOL, "Amount exceeds reward pool");
        require(to != address(0), "Invalid address");

        // Update the rewards mapping
        rewards[to] += amount;
        // Emit the rewards distributed event
        emit RewardsDistributed(to, amount);
    }

    // Function to claim rewards
    function claimRewards() external {
        uint256 rewardAmount = rewards[msg.sender];
        require(rewardAmount > 0, "No rewards to claim");

        // Reset the user's reward balance
        rewards[msg.sender] = 0;
        // Transfer the reward amount to the user
        _transfer(address(this), msg.sender, rewardAmount);
    }

    // Function to withdraw tokens from the contract (for owner)
    function withdrawTokens(uint256 amount) external onlyOwner {
        require(amount <= balanceOf(address(this)), "Insufficient balance");
        _transfer(address(this), msg.sender, amount);
    }

    // Function to get the current reward balance of an address
    function getRewardBalance(address account) external view returns (uint256) {
        return rewards[account];
    }
}
```
