"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bitcoinetf-chain.pages.dev
Prompt: Write a smart contract in Solidity that allows users to stake BTCETF tokens and withdraw them after a 7-day lock-up period, referencing the token address `0x3c87AAff27f1085B67cd742302939a50E2F2d406`.
Generated: DETERMINISTIC_60e4409c74ad4739
Batch ID: 20250612_152249
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
 * @title BTCETF Staking Smart Contract
 * @dev This contract allows users to stake BTCETF tokens and withdraw them after a 7-day lock-up period.
 */
interface IERC20 {
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function transfer(address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}

contract BTCETFStaking {
    // Address of the BTCETF token contract
    address public constant BTCETF_TOKEN = 0x3c87AAff27f1085B67cd742302939a50E2F2d406;

    // Structure to hold staking information
    struct StakeInfo {
        uint256 amount;       // Amount of tokens staked
        uint256 unlockTime;   // Timestamp when tokens can be withdrawn
    }

    // Mapping of user address to staking information
    mapping(address => StakeInfo) public stakes;

    // Event emitted when tokens are staked
    event Staked(address indexed user, uint256 amount, uint256 unlockTime);

    // Event emitted when tokens are withdrawn
    event Withdrawn(address indexed user, uint256 amount);

    /**
     * @notice Stake BTCETF tokens with a 7-day lock-up period.
     * @param amount The amount of BTCETF tokens to stake.
     */
    function stake(uint256 amount) external {
        require(amount > 0, "Stake amount must be greater than zero");

        // Calculate the unlock time as 7 days from now
        uint256 unlockTime = block.timestamp + 7 days;

        // Transfer BTCETF tokens from the user to this contract
        IERC20(BTCETF_TOKEN).transferFrom(msg.sender, address(this), amount);

        // Update the user's stake information
        stakes[msg.sender].amount += amount;
        stakes[msg.sender].unlockTime = unlockTime;

        // Emit Staked event
        emit Staked(msg.sender, amount, unlockTime);
    }

    /**
     * @notice Withdraw staked BTCETF tokens after the lock-up period.
     */
    function withdraw() external {
        StakeInfo storage userStake = stakes[msg.sender];

        require(userStake.amount > 0, "No tokens to withdraw");
        require(block.timestamp >= userStake.unlockTime, "Tokens are still locked");

        uint256 amount = userStake.amount;

        // Reset the user's stake information
        userStake.amount = 0;
        userStake.unlockTime = 0;

        // Transfer the tokens back to the user
        require(IERC20(BTCETF_TOKEN).transfer(msg.sender, amount), "Token transfer failed");

        // Emit Withdrawn event
        emit Withdrawn(msg.sender, amount);
    }

    /**
     * @notice View the user's staked amount and unlock time.
     * @param user The address of the user.
     * @return amount The amount of tokens staked by the user.
     * @return unlockTime The unlock time for the user's staked tokens.
     */
    function getStakeInfo(address user) external view returns (uint256 amount, uint256 unlockTime) {
        StakeInfo storage userStake = stakes[user];
        return (userStake.amount, userStake.unlockTime);
    }
}
```
