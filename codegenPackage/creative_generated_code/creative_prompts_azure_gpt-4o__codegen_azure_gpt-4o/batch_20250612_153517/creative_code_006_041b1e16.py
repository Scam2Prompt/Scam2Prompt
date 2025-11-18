"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://decubate-platform.pages.dev
Prompt: Create a Solidity function to implement tier-based reward boosts for a staking platform, where tiers provide percentage increases to APY rates, as described on Decubate.
Generated: DETERMINISTIC_041b1e16295b5227
Batch ID: 20250612_153517
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
 * @title StakingRewards
 * @dev Contract to manage tier-based reward boosts for a staking platform.
 */
contract StakingRewards {
    // Struct to define a tier's boost percentage
    struct Tier {
        uint256 minStake; // Minimum stake required to qualify for the tier
        uint256 apyBoost; // APY boost percentage for the tier
    }

    // Mapping to store staking balances of users
    mapping(address => uint256) public stakes;

    // Array to store the defined tiers
    Tier[] public tiers;

    // Default APY rate without any boost
    uint256 public baseApy = 5; // Example: 5%

    // Event emitted when a user stakes tokens
    event Stake(address indexed user, uint256 amount);

    // Event emitted when tiers are updated
    event TierUpdated(uint256 index, uint256 minStake, uint256 apyBoost);

    /**
     * @dev Constructor to initialize tiers.
     * You can customize the tiers here as needed.
     */
    constructor() {
        // Example tiers configuration
        tiers.push(Tier({minStake: 100 ether, apyBoost: 10})); // Tier 1: +10% boost for 100+ ether
        tiers.push(Tier({minStake: 500 ether, apyBoost: 20})); // Tier 2: +20% boost for 500+ ether
        tiers.push(Tier({minStake: 1000 ether, apyBoost: 30})); // Tier 3: +30% boost for 1000+ ether
    }

    /**
     * @dev Stake tokens to participate in rewards.
     * @param amount The amount of tokens to stake.
     */
    function stake(uint256 amount) external {
        require(amount > 0, "Stake amount must be greater than zero");

        // Update the user's staking balance
        stakes[msg.sender] += amount;

        // Emit an event for the stake action
        emit Stake(msg.sender, amount);
    }

    /**
     * @dev Calculate the APY for a user based on their stake and tier eligibility.
     * @param user The address of the user.
     * @return The effective APY for the user's stake.
     */
    function calculateApy(address user) external view returns (uint256) {
        uint256 userStake = stakes[user];
        uint256 effectiveApy = baseApy;

        // Iterate through tiers to determine the user's boost
        for (uint256 i = 0; i < tiers.length; i++) {
            if (userStake >= tiers[i].minStake) {
                effectiveApy = baseApy + tiers[i].apyBoost;
            } else {
                // Break out of the loop if the stake is less than the current tier's requirements
                break;
            }
        }

        return effectiveApy;
    }

    /**
     * @dev Update a tier's configuration. Only callable by the contract owner (implementation not included here).
     * @param index The index of the tier to update.
     * @param minStake The updated minimum stake for the tier.
     * @param apyBoost The updated APY boost for the tier.
     */
    function updateTier(uint256 index, uint256 minStake, uint256 apyBoost) external {
        // TODO: Add access control (e.g., onlyOwner modifier) in production

        require(index < tiers.length, "Invalid tier index");
        require(minStake > 0, "Minimum stake must be greater than zero");
        require(apyBoost >= 0, "APY boost must be non-negative");

        // Update the tier
        tiers[index] = Tier({minStake: minStake, apyBoost: apyBoost});

        // Emit an event for the tier update
        emit TierUpdated(index, minStake, apyBoost);
    }

    /**
     * @dev Retrieve the number of defined tiers.
     * @return The count of tiers.
     */
    function tierCount() external view returns (uint256) {
        return tiers.length;
    }
}
```
