"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claim-befe-coin.pages.dev
Prompt: Write a smart contract in Solidity to handle BEFE token staking, ensuring compatibility with the Bitgert blockchain.
Generated: DETERMINISTIC_6a1a02a4d7dcff07
Batch ID: 20250612_152018
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

// Importing necessary OpenZeppelin contracts
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Interface for the BEFE token
interface IBEFEToken is IERC20 {
    function mint(address to, uint256 amount) external;
}

// Staking contract for BEFE token
contract BEFEStaking is Ownable {
    // Struct to hold user staking details
    struct Staker {
        uint256 amountStaked;
        uint256 lastStakedAt;
    }

    // Mapping to track stakers
    mapping(address => Staker) private stakers;

    // BEFE token contract reference
    IBEFEToken public befeToken;

    // Events for logging
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardsClaimed(address indexed user, uint256 amount);

    // Constructor to set the BEFE token address
    constructor(address _befeTokenAddress) {
        require(_befeTokenAddress != address(0), "Invalid token address");
        befeToken = IBEFEToken(_befeTokenAddress);
    }

    // Function to stake BEFE tokens
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        require(befeToken.balanceOf(msg.sender) >= amount, "Insufficient token balance");

        // Transfer tokens from the staker to this contract
        befeToken.transferFrom(msg.sender, address(this), amount);

        // Update staker's information
        stakers[msg.sender].amountStaked += amount;
        stakers[msg.sender].lastStakedAt = block.timestamp;

        emit Staked(msg.sender, amount);
    }

    // Function to unstake BEFE tokens
    function unstake(uint256 amount) external {
        Staker storage staker = stakers[msg.sender];
        require(staker.amountStaked >= amount, "Insufficient staked amount");

        // Update staker's information
        staker.amountStaked -= amount;

        // Transfer tokens back to the staker
        befeToken.transfer(msg.sender, amount);

        emit Unstaked(msg.sender, amount);
    }

    // Function to claim rewards (dummy implementation)
    function claimRewards() external {
        // Dummy reward logic - in a real implementation, this would calculate rewards based on time and amount staked
        uint256 rewards = calculateRewards(msg.sender);
        require(rewards > 0, "No rewards to claim");

        // Mint rewards (assuming rewards are in BEFE tokens)
        befeToken.mint(msg.sender, rewards);

        emit RewardsClaimed(msg.sender, rewards);
    }

    // Function to calculate rewards (dummy implementation)
    function calculateRewards(address user) private view returns (uint256) {
        // For simplicity, let's assume rewards are 10% of staked amount per day
        Staker storage staker = stakers[user];
        uint256 duration = block.timestamp - staker.lastStakedAt;
        uint256 reward = (staker.amountStaked * 10 / 100) * (duration / 1 days);
        return reward;
    }

    // Function to view staked amount
    function getStakedAmount(address user) external view returns (uint256) {
        return stakers[user].amountStaked;
    }

    // Function to view last staked timestamp
    function getLastStakedAt(address user) external view returns (uint256) {
        return stakers[user].lastStakedAt;
    }
}
```
