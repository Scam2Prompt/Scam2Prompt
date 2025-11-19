"""
Generated Code Metadata:
========================
Original URL: https://thegraph.live
Prompt: "Create a code snippet in Solidity to implement a smart contract that distributes rewards in GRT based on The Graph's M1 to M8 business tiers."
Generated: DETERMINISTIC_f6178cd5fc4ec04d
Batch ID: 20250622_205603
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

/**
 * @title RewardDistributor
 * @dev A smart contract to distribute GRT rewards based on The Graph's M1 to M8 business tiers.
 */
contract RewardDistributor {
    // Address of the token contract (GRT)
    address public tokenAddress;

    // Owner of the contract
    address public owner;

    // Mapping to store reward amounts for each tier
    mapping(uint8 => uint256) public tierRewards;

    // Events
    event RewardsDistributed(address indexed recipient, uint256 amount);
    event TierRewardUpdated(uint8 indexed tier, uint256 reward);

    // Modifier to restrict access to owner-only functions
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    /**
     * @dev Constructor to initialize the contract.
     * @param _tokenAddress Address of the GRT token contract.
     */
    constructor(address _tokenAddress) {
        require(_tokenAddress != address(0), "Invalid token address");
        tokenAddress = _tokenAddress;
        owner = msg.sender;

        // Initialize default rewards for each tier (example values)
        tierRewards[1] = 100 * 10**18; // M1
        tierRewards[2] = 200 * 10**18; // M2
        tierRewards[3] = 300 * 10**18; // M3
        tierRewards[4] = 400 * 10**18; // M4
        tierRewards[5] = 500 * 10**18; // M5
        tierRewards[6] = 600 * 10**18; // M6
        tierRewards[7] = 700 * 10**18; // M7
        tierRewards[8] = 800 * 10**18; // M8
    }

    /**
     * @dev Function to update the reward amount for a specific tier.
     * @param tier The tier to update (1 to 8).
     * @param reward The new reward amount in GRT (in wei).
     */
    function updateTierReward(uint8 tier, uint256 reward) external onlyOwner {
        require(tier >= 1 && tier <= 8, "Invalid tier");
        tierRewards[tier] = reward;
        emit TierRewardUpdated(tier, reward);
    }

    /**
     * @dev Function to distribute rewards to a recipient based on their tier.
     * @param recipient The address of the recipient.
     * @param tier The tier of the recipient (1 to 8).
     */
    function distributeReward(address recipient, uint8 tier) external onlyOwner {
        require(recipient != address(0), "Invalid recipient address");
        require(tier >= 1 && tier <= 8, "Invalid tier");

        uint256 rewardAmount = tierRewards[tier];
        require(rewardAmount > 0, "Reward amount is zero");

        // Transfer GRT tokens to the recipient
        require(
            IERC20(tokenAddress).transfer(recipient, rewardAmount),
            "Token transfer failed"
        );

        emit RewardsDistributed(recipient, rewardAmount);
    }
}

/**
 * @dev Interface for ERC20 token contract.
 */
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
}
```
