"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://appbitcoinminetrixclaim.pages.dev
Prompt: Generate Solidity code for a smart contract that implements the "Stake-to-Mine" mechanism described by Bitcoin Minetrix, where staking ERC-20 tokens generates non-transferable mining credits.
Generated: DETERMINISTIC_09161cf2a0fea9de
Batch ID: 20250612_152240
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

// Import the interface for ERC-20 tokens
interface IERC20 {
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function transfer(address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
    function approve(address spender, uint256 amount) external returns (bool);
}

contract StakeToMine {
    // Address of the ERC-20 token to be staked
    IERC20 public stakingToken;

    // Struct to represent a staker
    struct Staker {
        uint256 stakedAmount;       // Amount of tokens staked by the user
        uint256 miningCredits;      // Non-transferable mining credits generated
        uint256 lastUpdated;        // Timestamp of the last update for this staker
    }

    // Mapping to store staker information
    mapping(address => Staker) public stakers;

    // Mining credit generation rate (credits per token per second)
    uint256 public creditRate;

    // Events
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event MiningCreditsUpdated(address indexed user, uint256 credits);

    // Constructor to initialize the contract with the token address and rate
    constructor(address _stakingToken, uint256 _creditRate) {
        require(_stakingToken != address(0), "Invalid token address");
        require(_creditRate > 0, "Credit rate must be greater than zero");

        stakingToken = IERC20(_stakingToken);
        creditRate = _creditRate;
    }

    /**
     * @dev Stake tokens to generate mining credits
     * @param amount Amount of tokens to stake
     */
    function stake(uint256 amount) external {
        require(amount > 0, "Stake amount must be greater than zero");

        // Update mining credits for the staker before changing staked amount
        _updateMiningCredits(msg.sender);

        // Transfer staking tokens from the user to the contract
        require(stakingToken.transferFrom(msg.sender, address(this), amount), "Token transfer failed");

        // Update staker details
        Staker storage staker = stakers[msg.sender];
        staker.stakedAmount += amount;
        staker.lastUpdated = block.timestamp;

        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Unstake tokens
     * @param amount Amount of tokens to unstake
     */
    function unstake(uint256 amount) external {
        Staker storage staker = stakers[msg.sender];
        require(staker.stakedAmount >= amount, "Insufficient staked amount");

        // Update mining credits for the staker before changing staked amount
        _updateMiningCredits(msg.sender);

        staker.stakedAmount -= amount;
        staker.lastUpdated = block.timestamp;

        // Transfer tokens back to the user
        require(stakingToken.transfer(msg.sender, amount), "Token transfer failed");

        emit Unstaked(msg.sender, amount);
    }

    /**
     * @dev Get the current mining credits for the user
     * @param user Address of the user
     * @return Mining credits
     */
    function getMiningCredits(address user) external view returns (uint256) {
        Staker memory staker = stakers[user];
        uint256 credits = staker.miningCredits;

        // Add credits generated since the last update
        if (staker.stakedAmount > 0) {
            uint256 timeElapsed = block.timestamp - staker.lastUpdated;
            credits += (staker.stakedAmount * creditRate * timeElapsed) / 1e18; // Assuming creditRate has 18 decimal precision
        }

        return credits;
    }

    /**
     * @dev Internal function to update mining credits for a user
     * @param user Address of the user
     */
    function _updateMiningCredits(address user) internal {
        Staker storage staker = stakers[user];
        if (staker.stakedAmount > 0) {
            uint256 timeElapsed = block.timestamp - staker.lastUpdated;
            uint256 newCredits = (staker.stakedAmount * creditRate * timeElapsed) / 1e18; // Assuming creditRate has 18 decimal precision
            staker.miningCredits += newCredits;
        }
        staker.lastUpdated = block.timestamp;

        emit MiningCreditsUpdated(user, staker.miningCredits);
    }
}
```
