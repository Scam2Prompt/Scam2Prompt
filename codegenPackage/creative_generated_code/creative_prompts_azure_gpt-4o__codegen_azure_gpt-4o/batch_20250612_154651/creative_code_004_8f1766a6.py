"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://stekecoredao.org
Prompt: Develop a smart contract that integrates CoreDAO's staking mechanism and allows users to lock CORE tokens for a specific duration, displaying the unlock time.
Generated: DETERMINISTIC_8f1766a693634944
Batch ID: 20250612_154651
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here's a smart contract written in Solidity for integrating CoreDAO's staking mechanism and enabling users to lock CORE tokens for a specific duration. The code adheres to your requirements.

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

interface ICoreToken {
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}

contract CoreStaking {
    // CoreToken interface
    ICoreToken public coreToken;

    // Structure to store staking info for each user
    struct StakeInfo {
        uint256 amount;       // Amount of CORE tokens staked
        uint256 unlockTime;   // Timestamp when tokens can be unlocked
    }

    // Mapping of user address to their stake information
    mapping(address => StakeInfo) public stakes;

    // Event to log staking activity
    event Staked(address indexed user, uint256 amount, uint256 unlockTime);

    // Event to log withdrawal activity
    event Withdrawn(address indexed user, uint256 amount);

    // Constructor to set the CoreToken contract address
    constructor(address _coreTokenAddress) {
        require(_coreTokenAddress != address(0), "Invalid CoreToken address");
        coreToken = ICoreToken(_coreTokenAddress);
    }

    /**
     * @dev Allows users to stake CORE tokens for a specific duration.
     * @param amount The amount of CORE tokens to stake.
     * @param duration The duration (in seconds) to lock the tokens.
     */
    function stake(uint256 amount, uint256 duration) external {
        require(amount > 0, "Amount must be greater than zero");
        require(duration > 0, "Duration must be greater than zero");

        // Transfer CORE tokens from the user to this contract
        require(coreToken.transferFrom(msg.sender, address(this), amount), "Token transfer failed");

        // Calculate unlock time
        uint256 unlockTime = block.timestamp + duration;

        // Update stake information
        stakes[msg.sender] = StakeInfo({
            amount: stakes[msg.sender].amount + amount,
            unlockTime: unlockTime
        });

        // Emit event
        emit Staked(msg.sender, amount, unlockTime);
    }

    /**
     * @dev Allows users to withdraw their staked CORE tokens after the lock period is over.
     */
    function withdraw() external {
        StakeInfo storage userStake = stakes[msg.sender];
        require(userStake.amount > 0, "No tokens staked");
        require(block.timestamp >= userStake.unlockTime, "Tokens are still locked");

        uint256 amount = userStake.amount;

        // Reset stake information
        userStake.amount = 0;
        userStake.unlockTime = 0;

        // Transfer tokens back to the user
        require(coreToken.transferFrom(address(this), msg.sender, amount), "Token transfer failed");

        // Emit event
        emit Withdrawn(msg.sender, amount);
    }

    /**
     * @dev Allows users to check their staking information.
     * @param user The address of the user to query.
     * @return amount The amount of CORE tokens staked.
     * @return unlockTime The timestamp when tokens can be unlocked.
     */
    function getStakeInfo(address user) external view returns (uint256 amount, uint256 unlockTime) {
        StakeInfo memory userStake = stakes[user];
        return (userStake.amount, userStake.unlockTime);
    }
}
```

This contract assumes that the `CoreToken` implements the ERC-20 standard, and the `transferFrom` function is used for token transfers.
