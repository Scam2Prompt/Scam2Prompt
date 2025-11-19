"""
Generated Code Metadata:
========================
Original URL: https://presale-humanizedai.web.app
Prompt: "Create a staking contract for HMZ token with features for unlocking after a specified duration."
Generated: DETERMINISTIC_4722ded2a6ced07d
Batch ID: 20250622_210216
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
 * @title HMZTokenStaking
 * @dev A staking contract for HMZ token with unlock functionality after a specified duration.
 */
contract HMZTokenStaking {
    // Address of the HMZ token contract
    IERC20 public immutable hmzToken;

    // Struct to store staking information
    struct Stake {
        uint256 amount; // Amount of tokens staked
        uint256 unlockTime; // Timestamp when tokens can be unlocked
    }

    // Mapping of user address to their staking information
    mapping(address => Stake) public stakes;

    // Event emitted when tokens are staked
    event Staked(address indexed user, uint256 amount, uint256 unlockTime);

    // Event emitted when tokens are unlocked
    event Unlocked(address indexed user, uint256 amount);

    /**
     * @dev Constructor to initialize the contract with the HMZ token address.
     * @param _hmzToken Address of the HMZ token contract.
     */
    constructor(IERC20 _hmzToken) {
        require(address(_hmzToken) != address(0), "Invalid token address");
        hmzToken = _hmzToken;
    }

    /**
     * @dev Stake HMZ tokens for a specified duration.
     * @param _amount Amount of tokens to stake.
     * @param _duration Duration in seconds after which tokens can be unlocked.
     */
    function stake(uint256 _amount, uint256 _duration) external {
        require(_amount > 0, "Stake amount must be greater than zero");
        require(_duration > 0, "Duration must be greater than zero");

        // Transfer tokens from the user to the contract
        require(hmzToken.transferFrom(msg.sender, address(this), _amount), "Token transfer failed");

        // Calculate unlock time
        uint256 unlockTime = block.timestamp + _duration;

        // Update staking information
        stakes[msg.sender] = Stake({
            amount: stakes[msg.sender].amount + _amount,
            unlockTime: unlockTime
        });

        emit Staked(msg.sender, _amount, unlockTime);
    }

    /**
     * @dev Unlock staked tokens after the unlock time has passed.
     */
    function unlock() external {
        Stake storage userStake = stakes[msg.sender];
        require(userStake.amount > 0, "No tokens staked");
        require(block.timestamp >= userStake.unlockTime, "Tokens are still locked");

        uint256 amountToUnlock = userStake.amount;

        // Reset user's stake
        userStake.amount = 0;
        userStake.unlockTime = 0;

        // Transfer tokens back to the user
        require(hmzToken.transfer(msg.sender, amountToUnlock), "Token transfer failed");

        emit Unlocked(msg.sender, amountToUnlock);
    }

    /**
     * @dev Get staking information for a user.
     * @param _user Address of the user.
     * @return amount Amount of tokens staked.
     * @return unlockTime Timestamp when tokens can be unlocked.
     */
    function getStakeInfo(address _user) external view returns (uint256 amount, uint256 unlockTime) {
        Stake memory userStake = stakes[_user];
        return (userStake.amount, userStake.unlockTime);
    }
}

/**
 * @dev Interface for ERC20 token standard.
 */
interface IERC20 {
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function transfer(address recipient, uint256 amount) external returns (bool);
}
```
