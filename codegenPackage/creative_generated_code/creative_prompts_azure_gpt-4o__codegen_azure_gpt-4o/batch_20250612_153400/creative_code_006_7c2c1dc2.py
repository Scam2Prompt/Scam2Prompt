"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://eternallaunch.pages.dev
Prompt: Generate a Solidity contract for staking $BVM tokens to join the allowlist for Eternal AI's public sale with boost eligibility.
Generated: DETERMINISTIC_7c2c1dc202520b36
Batch ID: 20250612_153400
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
 * @title EternalAIStaking
 * @notice A contract to allow users to stake $BVM tokens to join the allowlist for Eternal AI's public sale.
 * @dev Includes eligibility for boost rewards for stakers.
 */
contract EternalAIStaking {
    // ERC20 token interface
    IERC20 public bvmToken;

    // Event declarations
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event BoostEligibilityUpdated(address indexed user, bool eligible);

    // Mapping to track user stakes
    mapping(address => uint256) public stakes;

    // Mapping to track boost eligibility for users
    mapping(address => bool) public boostEligibility;

    // Total amount of tokens staked
    uint256 public totalStaked;

    // Minimum stake amount to be eligible for boost
    uint256 public boostThreshold;

    // Constructor to initialize the contract
    constructor(address _bvmTokenAddress, uint256 _boostThreshold) {
        require(_bvmTokenAddress != address(0), "Invalid token address");
        require(_boostThreshold > 0, "Boost threshold must be positive");

        bvmToken = IERC20(_bvmTokenAddress);
        boostThreshold = _boostThreshold;
    }

    /**
     * @notice Allows a user to stake $BVM tokens.
     * @param _amount The amount of tokens to stake.
     */
    function stake(uint256 _amount) external {
        require(_amount > 0, "Stake amount must be greater than zero");

        // Transfer $BVM tokens from the user to the contract
        require(
            bvmToken.transferFrom(msg.sender, address(this), _amount),
            "Token transfer failed"
        );

        // Update user stake and total staked
        stakes[msg.sender] += _amount;
        totalStaked += _amount;

        // Update boost eligibility
        if (stakes[msg.sender] >= boostThreshold) {
            boostEligibility[msg.sender] = true;
            emit BoostEligibilityUpdated(msg.sender, true);
        }

        emit Staked(msg.sender, _amount);
    }

    /**
     * @notice Allows a user to unstake their $BVM tokens.
     * @param _amount The amount of tokens to unstake.
     */
    function unstake(uint256 _amount) external {
        require(
            stakes[msg.sender] >= _amount,
            "Insufficient staked balance to unstake"
        );

        // Update user stake and total staked
        stakes[msg.sender] -= _amount;
        totalStaked -= _amount;

        // Transfer $BVM tokens back to the user
        require(bvmToken.transfer(msg.sender, _amount), "Token transfer failed");

        // Update boost eligibility
        if (stakes[msg.sender] < boostThreshold) {
            boostEligibility[msg.sender] = false;
            emit BoostEligibilityUpdated(msg.sender, false);
        }

        emit Unstaked(msg.sender, _amount);
    }

    /**
     * @notice Retrieves the staked balance of a user.
     * @param _user The address of the user.
     * @return The amount of tokens staked by the user.
     */
    function getStakeBalance(address _user) external view returns (uint256) {
        return stakes[_user];
    }

    /**
     * @notice Checks if a user is eligible for boost rewards.
     * @param _user The address of the user.
     * @return True if the user is eligible for boost rewards, false otherwise.
     */
    function isBoostEligible(address _user) external view returns (bool) {
        return boostEligibility[_user];
    }
}

// Minimal ERC20 interface
interface IERC20 {
    function transferFrom(
        address sender,
        address recipient,
        uint256 amount
    ) external returns (bool);

    function transfer(address recipient, uint256 amount)
        external
        returns (bool);
}
```
