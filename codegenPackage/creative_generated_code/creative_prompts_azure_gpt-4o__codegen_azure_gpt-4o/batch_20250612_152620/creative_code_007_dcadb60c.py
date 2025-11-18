"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://trustpad-link.pages.dev
Prompt: Write a Solidity contract to manage staking of TrustPad tokens, granting priority access to IDOs based on staking levels.
Generated: DETERMINISTIC_dcadb60c30c79498
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
 * @title TrustPadTokenStaking
 * @dev A contract to manage staking of TrustPad tokens, granting priority access to IDOs based on staking levels.
 */
contract TrustPadTokenStaking {
    // ERC20 interface for TrustPad token
    IERC20 public trustPadToken;

    // Struct to hold staking information
    struct StakeInfo {
        uint256 amount; // Amount of tokens staked
        uint256 stakeTime; // Timestamp when tokens were staked
    }

    // Mapping of stakers' addresses to their staking information
    mapping(address => StakeInfo) public stakes;

    // Tier thresholds for priority access based on staking levels
    uint256 public tier1Threshold; // Minimum amount for Tier 1 access
    uint256 public tier2Threshold; // Minimum amount for Tier 2 access
    uint256 public tier3Threshold; // Minimum amount for Tier 3 access

    // Events
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);

    /**
     * @dev Constructor initializes the staking contract.
     * @param _trustPadToken Address of the TrustPad token contract.
     * @param _tier1Threshold Minimum staking amount for Tier 1 access.
     * @param _tier2Threshold Minimum staking amount for Tier 2 access.
     * @param _tier3Threshold Minimum staking amount for Tier 3 access.
     */
    constructor(
        address _trustPadToken,
        uint256 _tier1Threshold,
        uint256 _tier2Threshold,
        uint256 _tier3Threshold
    ) {
        require(_trustPadToken != address(0), "Invalid token address");
        trustPadToken = IERC20(_trustPadToken);
        tier1Threshold = _tier1Threshold;
        tier2Threshold = _tier2Threshold;
        tier3Threshold = _tier3Threshold;
    }

    /**
     * @dev Stake TrustPad tokens to participate in IDOs.
     * @param amount The amount of tokens to stake.
     */
    function stake(uint256 amount) external {
        require(amount > 0, "Stake amount must be greater than zero");
        require(trustPadToken.balanceOf(msg.sender) >= amount, "Insufficient token balance");

        // Transfer tokens from user to contract
        bool success = trustPadToken.transferFrom(msg.sender, address(this), amount);
        require(success, "Token transfer failed");

        StakeInfo storage stakeInfo = stakes[msg.sender];
        stakeInfo.amount += amount; // Update staking amount
        stakeInfo.stakeTime = block.timestamp; // Update staking time

        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Unstake TrustPad tokens.
     */
    function unstake() external {
        StakeInfo storage stakeInfo = stakes[msg.sender];
        require(stakeInfo.amount > 0, "No tokens staked");

        uint256 amountToUnstake = stakeInfo.amount;

        // Reset staking information
        stakeInfo.amount = 0;
        stakeInfo.stakeTime = 0;

        // Transfer tokens back to the user
        bool success = trustPadToken.transfer(msg.sender, amountToUnstake);
        require(success, "Token transfer failed");

        emit Unstaked(msg.sender, amountToUnstake);
    }

    /**
     * @dev Get the staking level (tier) of a user based on their staked amount.
     * @param user Address of the user.
     * @return Tier level (0 for no access, 1 for Tier 1, 2 for Tier 2, and 3 for Tier 3).
     */
    function getStakingTier(address user) external view returns (uint8) {
        StakeInfo memory stakeInfo = stakes[user];
        if (stakeInfo.amount >= tier3Threshold) {
            return 3;
        } else if (stakeInfo.amount >= tier2Threshold) {
            return 2;
        } else if (stakeInfo.amount >= tier1Threshold) {
            return 1;
        } else {
            return 0; // No priority access
        }
    }
}

/**
 * @dev Minimal interface for ERC20 token functionality.
 */
interface IERC20 {
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function transfer(address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}
```
