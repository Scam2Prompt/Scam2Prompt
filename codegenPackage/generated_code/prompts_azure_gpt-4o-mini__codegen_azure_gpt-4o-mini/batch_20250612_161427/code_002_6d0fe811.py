"""
Generated Code Metadata:
========================
Original URL: https://testai-qhn.pages.dev
Prompt: Explain how to implement a smart contract for managing staking tiers and rewards for the AITECH token.
Generated: DETERMINISTIC_6d0fe811362759ca
Batch ID: 20250612_161427
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

// Importing OpenZeppelin's ERC20 interface for token interactions
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Smart contract for managing staking tiers and rewards for the AITECH token
contract AITECHStaking is Ownable {
    // Struct to define a staking tier
    struct Tier {
        uint256 minStake; // Minimum amount to stake for this tier
        uint256 rewardRate; // Reward rate for this tier (in percentage)
    }

    // Mapping of tier levels to their respective Tier struct
    mapping(uint256 => Tier) public tiers;
    // Mapping of user addresses to their staked amounts and tier levels
    mapping(address => uint256) public stakedAmounts;
    mapping(address => uint256) public userTiers;

    // The AITECH token contract
    IERC20 public aitechToken;

    // Event emitted when a user stakes tokens
    event Staked(address indexed user, uint256 amount, uint256 tier);
    // Event emitted when a user unstakes tokens
    event Unstaked(address indexed user, uint256 amount);
    // Event emitted when rewards are claimed
    event RewardsClaimed(address indexed user, uint256 amount);

    // Constructor to initialize the contract with the AITECH token address
    constructor(address _aitechToken) {
        aitechToken = IERC20(_aitechToken);
    }

    // Function to add a new staking tier
    function addTier(uint256 tierLevel, uint256 minStake, uint256 rewardRate) external onlyOwner {
        require(minStake > 0, "Minimum stake must be greater than zero");
        require(rewardRate > 0, "Reward rate must be greater than zero");
        tiers[tierLevel] = Tier(minStake, rewardRate);
    }

    // Function to stake tokens
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        require(aitechToken.transferFrom(msg.sender, address(this), amount), "Transfer failed");

        // Update user's staked amount
        stakedAmounts[msg.sender] += amount;

        // Determine the user's tier based on their staked amount
        uint256 tierLevel = determineTier(msg.sender);
        userTiers[msg.sender] = tierLevel;

        emit Staked(msg.sender, amount, tierLevel);
    }

    // Function to unstake tokens
    function unstake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        require(stakedAmounts[msg.sender] >= amount, "Insufficient staked amount");

        // Update user's staked amount
        stakedAmounts[msg.sender] -= amount;
        require(aitechToken.transfer(msg.sender, amount), "Transfer failed");

        emit Unstaked(msg.sender, amount);
    }

    // Function to claim rewards based on the user's tier
    function claimRewards() external {
        uint256 tierLevel = userTiers[msg.sender];
        require(tierLevel > 0, "User is not in any tier");

        uint256 reward = calculateRewards(msg.sender, tierLevel);
        require(reward > 0, "No rewards to claim");

        // Transfer rewards to the user
        require(aitechToken.transfer(msg.sender, reward), "Transfer failed");

        emit RewardsClaimed(msg.sender, reward);
    }

    // Internal function to determine the user's tier based on their staked amount
    function determineTier(address user) internal view returns (uint256) {
        uint256 amountStaked = stakedAmounts[user];
        for (uint256 i = 1; i <= 10; i++) { // Assuming a maximum of 10 tiers
            if (amountStaked >= tiers[i].minStake) {
                return i;
            }
        }
        return 0; // No tier found
    }

    // Internal function to calculate rewards based on the user's tier
    function calculateRewards(address user, uint256 tierLevel) internal view returns (uint256) {
        uint256 amountStaked = stakedAmounts[user];
        uint256 rewardRate = tiers[tierLevel].rewardRate;
        return (amountStaked * rewardRate) / 100; // Simple reward calculation
    }
}
```
