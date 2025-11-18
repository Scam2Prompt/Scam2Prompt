"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://siduspad.xyz
Prompt: Develop a feature in Solidity that increases an investor's tier by a percentage (e.g., +50%) based on their staking duration, as outlined in SidusPad's staking pool details.
Generated: DETERMINISTIC_265c2f54a2e0f7be
Batch ID: 20250612_152235
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
 * @title SidusPadStaking
 * @dev This contract manages staking and increases an investor's tier based on the staking duration.
 */
contract SidusPadStaking {
    // Struct to represent an investor's staking details
    struct Staker {
        uint256 tier; // Current tier of the staker
        uint256 stakedAt; // Timestamp when the staking started
        bool isStaking; // Indicates if the staker is actively staking
    }

    // Mapping to store staking details for each address
    mapping(address => Staker) public stakers;

    // Percentage increment for the tier based on staking duration (e.g., 50%)
    uint256 public constant TIER_INCREMENT_PERCENTAGE = 50;

    // Minimum required staking duration to qualify for tier increment (e.g., 30 days)
    uint256 public constant MINIMUM_STAKING_DURATION = 30 days;

    // Event emitted when a staker's tier is updated
    event TierUpdated(address indexed staker, uint256 oldTier, uint256 newTier);

    // Modifier to ensure the caller is actively staking
    modifier isActiveStaker(address _staker) {
        require(stakers[_staker].isStaking, "Not actively staking");
        _;
    }

    /**
     * @notice Starts staking for a given address with an initial tier.
     * @param _tier Initial tier assigned to the staker.
     */
    function startStaking(uint256 _tier) external {
        require(!stakers[msg.sender].isStaking, "Already staking");
        require(_tier > 0, "Initial tier must be greater than 0");

        stakers[msg.sender] = Staker({
            tier: _tier,
            stakedAt: block.timestamp,
            isStaking: true
        });
    }

    /**
     * @notice Ends staking for the caller and resets their staking details.
     */
    function endStaking() external isActiveStaker(msg.sender) {
        delete stakers[msg.sender];
    }

    /**
     * @notice Increases the staker's tier by a percentage if they meet the staking duration requirement.
     */
    function increaseTier() external isActiveStaker(msg.sender) {
        Staker storage staker = stakers[msg.sender];

        // Ensure the minimum staking duration is met
        require(
            block.timestamp >= staker.stakedAt + MINIMUM_STAKING_DURATION,
            "Staking duration not met"
        );

        // Calculate the new tier
        uint256 oldTier = staker.tier;
        uint256 increment = (oldTier * TIER_INCREMENT_PERCENTAGE) / 100;
        uint256 newTier = oldTier + increment;

        // Update the staker's tier
        staker.tier = newTier;

        // Emit the TierUpdated event
        emit TierUpdated(msg.sender, oldTier, newTier);
    }

    /**
     * @notice Fetches the details of an active staker.
     * @param _staker Address of the staker.
     * @return tier Current tier of the staker.
     * @return stakedAt Timestamp when the staking started.
     * @return isStaking Whether the staker is actively staking.
     */
    function getStakerDetails(address _staker)
        external
        view
        returns (
            uint256 tier,
            uint256 stakedAt,
            bool isStaking
        )
    {
        Staker memory staker = stakers[_staker];
        return (staker.tier, staker.stakedAt, staker.isStaking);
    }
}
```
