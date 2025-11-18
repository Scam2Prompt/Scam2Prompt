"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aitech-c09.pages.dev
Prompt: Create a Solidity function to implement tier-based boosts for staking rewards, ensuring compatibility with EVM chains as mentioned on the webpage.
Generated: DETERMINISTIC_e7d4f17b632ef1ae
Batch ID: 20250612_152620
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
 * @title TieredStakingRewards
 * @dev Contract to implement tier-based boosts for staking rewards
 * This contract is compatible with EVM chains
 */
contract TieredStakingRewards {
    // Owner of the contract
    address public owner;

    // Mapping to store staking balances of users
    mapping(address => uint256) public stakingBalances;

    // Mapping to store reward tiers and their associated boost percentages
    mapping(uint256 => uint256) public rewardTiers;

    // Event for staking
    event Staked(address indexed user, uint256 amount);

    // Event for withdrawal
    event Withdrawn(address indexed user, uint256 amount);

    // Event for rewards calculation
    event RewardsCalculated(address indexed user, uint256 rewards);

    // Modifier to restrict access to the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    constructor() {
        // Initialize contract owner
        owner = msg.sender;

        // Initialize tier-based reward boosts (Percentage values in basis points: e.g., 500 = 5%)
        rewardTiers[0] = 0; // Tier 0: No boost
        rewardTiers[1] = 500; // Tier 1: 5% boost
        rewardTiers[2] = 1000; // Tier 2: 10% boost
        rewardTiers[3] = 1500; // Tier 3: 15% boost
    }

    /**
     * @dev Function to stake tokens
     * @param _amount The amount to stake
     */
    function stake(uint256 _amount) external {
        require(_amount > 0, "Stake amount must be greater than zero");

        // Update staking balance
        stakingBalances[msg.sender] += _amount;

        emit Staked(msg.sender, _amount);
    }

    /**
     * @dev Function to withdraw staked tokens
     */
    function withdraw() external {
        uint256 balance = stakingBalances[msg.sender];
        require(balance > 0, "No balance to withdraw");

        // Reset staking balance
        stakingBalances[msg.sender] = 0;

        emit Withdrawn(msg.sender, balance);
    }

    /**
     * @dev Function to calculate rewards based on staking tier
     * @param _user The address of the user
     * @return rewards Calculated rewards including tier-based boosts
     */
    function calculateRewards(address _user) external view returns (uint256 rewards) {
        uint256 balance = stakingBalances[_user];
        require(balance > 0, "No balance to calculate rewards");

        uint256 tier = getTier(balance);
        uint256 tierBoost = rewardTiers[tier];

        // Calculate rewards with the tier boost
        rewards = balance + ((balance * tierBoost) / 10000); // Using basis points for precise percentage calculation
    }

    /**
     * @dev Internal function to determine the tier based on staking balance
     * @param _balance The staking balance
     * @return tier The tier corresponding to the staking balance
     */
    function getTier(uint256 _balance) internal pure returns (uint256 tier) {
        if (_balance >= 1000 ether) {
            return 3; // Tier 3: Highest rewards
        } else if (_balance >= 500 ether) {
            return 2; // Tier 2
        } else if (_balance >= 100 ether) {
            return 1; // Tier 1
        } else {
            return 0; // Tier 0: No boost
        }
    }

    /**
     * @dev Function for the owner to update reward tiers
     * @param _tier The tier to update
     * @param _boost The new boost percentage in basis points
     */
    function updateRewardTier(uint256 _tier, uint256 _boost) external onlyOwner {
        require(_tier <= 3, "Invalid tier");
        require(_boost <= 5000, "Boost percentage too high");

        rewardTiers[_tier] = _boost;
    }
}
```
