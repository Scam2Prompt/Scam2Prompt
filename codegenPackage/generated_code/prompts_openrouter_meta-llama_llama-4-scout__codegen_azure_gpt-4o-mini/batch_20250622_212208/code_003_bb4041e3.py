"""
Generated Code Metadata:
========================
Original URL: https://btcbull.io
Prompt: Design a tokenomics structure for a meme coin similar to $BTCBULL, including allocations for staking, airdrops, marketing, and liquidity.
Generated: DETERMINISTIC_bb4041e33232a732
Batch ID: 20250622_212208
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

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title MemeCoin
 * @dev Implementation of a meme coin with a tokenomics structure
 */
contract MemeCoin is ERC20, Ownable {
    // Total supply of the token
    uint256 public constant TOTAL_SUPPLY = 1_000_000_000 * 10 ** 18; // 1 billion tokens

    // Allocation percentages
    uint256 public constant STAKING_ALLOCATION = 20; // 20%
    uint256 public constant AIRDROP_ALLOCATION = 10; // 10%
    uint256 public constant MARKETING_ALLOCATION = 15; // 15%
    uint256 public constant LIQUIDITY_ALLOCATION = 25; // 25%
    uint256 public constant RESERVE_ALLOCATION = 30; // 30%

    // Mappings to track allocations
    mapping(address => uint256) public stakingRewards;
    mapping(address => uint256) public airdropBalances;

    // Events for tracking allocations
    event AirdropDistributed(address indexed recipient, uint256 amount);
    event StakingRewardsUpdated(address indexed staker, uint256 amount);

    /**
     * @dev Constructor that gives msg.sender all of existing tokens.
     */
    constructor() ERC20("MemeCoin", "MEME") {
        _mint(msg.sender, TOTAL_SUPPLY);
    }

    /**
     * @dev Function to distribute airdrop tokens to a list of addresses.
     * @param recipients List of addresses to receive airdrop tokens.
     * @param amounts List of amounts corresponding to each recipient.
     */
    function distributeAirdrop(address[] calldata recipients, uint256[] calldata amounts) external onlyOwner {
        require(recipients.length == amounts.length, "MemeCoin: Recipients and amounts length mismatch");
        
        for (uint256 i = 0; i < recipients.length; i++) {
            require(recipients[i] != address(0), "MemeCoin: Invalid address");
            require(amounts[i] > 0, "MemeCoin: Amount must be greater than zero");

            airdropBalances[recipients[i]] += amounts[i];
            _transfer(msg.sender, recipients[i], amounts[i]);
            emit AirdropDistributed(recipients[i], amounts[i]);
        }
    }

    /**
     * @dev Function to allocate staking rewards to a user.
     * @param user Address of the user to receive staking rewards.
     * @param amount Amount of tokens to allocate as staking rewards.
     */
    function allocateStakingRewards(address user, uint256 amount) external onlyOwner {
        require(user != address(0), "MemeCoin: Invalid address");
        require(amount > 0, "MemeCoin: Amount must be greater than zero");

        stakingRewards[user] += amount;
        emit StakingRewardsUpdated(user, amount);
    }

    /**
     * @dev Function to withdraw staking rewards.
     */
    function withdrawStakingRewards() external {
        uint256 reward = stakingRewards[msg.sender];
        require(reward > 0, "MemeCoin: No rewards to withdraw");

        stakingRewards[msg.sender] = 0;
        _transfer(address(this), msg.sender, reward);
    }

    /**
     * @dev Function to get the total allocation for a specific category.
     * @param category The category to check (0: Staking, 1: Airdrop, 2: Marketing, 3: Liquidity, 4: Reserve).
     * @return The total allocated amount for the specified category.
     */
    function getTotalAllocation(uint8 category) external pure returns (uint256) {
        if (category == 0) return (TOTAL_SUPPLY * STAKING_ALLOCATION) / 100;
        if (category == 1) return (TOTAL_SUPPLY * AIRDROP_ALLOCATION) / 100;
        if (category == 2) return (TOTAL_SUPPLY * MARKETING_ALLOCATION) / 100;
        if (category == 3) return (TOTAL_SUPPLY * LIQUIDITY_ALLOCATION) / 100;
        if (category == 4) return (TOTAL_SUPPLY * RESERVE_ALLOCATION) / 100;
        revert("MemeCoin: Invalid category");
    }
}
```
