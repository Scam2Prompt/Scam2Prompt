"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://testai-qhn.pages.dev
Prompt: Create a Solidity function that locks staked AITECH tokens for a specified duration and applies tier-based reward boosts, ensuring compatibility with EVM chains.
Generated: DETERMINISTIC_693de21611dba2e2
Batch ID: 20250612_152656
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

contract AITechStaking {
    IERC20 public aitechToken;

    // Struct to hold staking information
    struct Stake {
        uint256 amount;
        uint256 unlockTime;
        uint256 rewardMultiplier; // Tier-based reward multiplier
    }

    // Mapping of user addresses to their staking information
    mapping(address => Stake) public stakes;

    // Tier-based reward multipliers (example values)
    uint256 public constant TIER_1_MULTIPLIER = 110; // 10% boost
    uint256 public constant TIER_2_MULTIPLIER = 120; // 20% boost
    uint256 public constant TIER_3_MULTIPLIER = 130; // 30% boost

    // Minimum staking duration in seconds (example: 30 days)
    uint256 public constant MINIMUM_STAKING_DURATION = 30 days;

    // Event to notify when tokens are staked
    event TokensStaked(address indexed user, uint256 amount, uint256 unlockTime, uint256 rewardMultiplier);

    constructor(address _aitechToken) {
        require(_aitechToken != address(0), "Invalid token address");
        aitechToken = IERC20(_aitechToken);
    }

    /**
     * @dev Function to stake AITECH tokens.
     * @param _amount The amount of AITECH tokens to stake.
     * @param _duration The staking duration in seconds.
     */
    function stakeTokens(uint256 _amount, uint256 _duration) external {
        require(_amount > 0, "Stake amount must be greater than zero");
        require(_duration >= MINIMUM_STAKING_DURATION, "Staking duration must be at least the minimum duration");

        // Transfer tokens from the user to the contract
        require(aitechToken.transferFrom(msg.sender, address(this), _amount), "Token transfer failed");

        // Determine the reward multiplier based on staking amount
        uint256 rewardMultiplier = getRewardMultiplier(_amount);

        // Set staking information
        stakes[msg.sender] = Stake({
            amount: _amount,
            unlockTime: block.timestamp + _duration,
            rewardMultiplier: rewardMultiplier
        });

        // Emit event
        emit TokensStaked(msg.sender, _amount, stakes[msg.sender].unlockTime, rewardMultiplier);
    }

    /**
     * @dev Function to get the reward multiplier based on the staking amount.
     * @param _amount The amount of tokens staked.
     * @return The reward multiplier.
     */
    function getRewardMultiplier(uint256 _amount) public pure returns (uint256) {
        if (_amount >= 1000 * 10**18) {
            return TIER_3_MULTIPLIER; // Tier 3
        } else if (_amount >= 500 * 10**18) {
            return TIER_2_MULTIPLIER; // Tier 2
        } else {
            return TIER_1_MULTIPLIER; // Tier 1
        }
    }

    /**
     * @dev Function to check the staking details of a user.
     * @param _user The address of the user.
     * @return amount, unlockTime, and rewardMultiplier.
     */
    function getStakeDetails(address _user) external view returns (uint256, uint256, uint256) {
        Stake memory stake = stakes[_user];
        return (stake.amount, stake.unlockTime, stake.rewardMultiplier);
    }

    /**
     * @dev Interface for ERC20 token to interact with AITECH tokens.
     */
    interface IERC20 {
        function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    }
}
```
