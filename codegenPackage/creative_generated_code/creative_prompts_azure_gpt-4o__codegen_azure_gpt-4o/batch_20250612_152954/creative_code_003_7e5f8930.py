"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://stake-catecoin-club.pages.dev
Prompt: Write a Solidity smart contract snippet to implement a staking mechanism for Catecoin, including penalties for unstaking before 32 days.
Generated: DETERMINISTIC_7e5f8930776907af
Batch ID: 20250612_152954
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
 * @title Catecoin Staking Contract
 * @dev Implements a staking mechanism with penalties for unstaking before 32 days.
 */
contract CatecoinStaking {
    IERC20 public catecoin; // Catecoin token interface
    uint256 public constant PENALTY_PERIOD = 32 days; // Minimum staking period
    uint256 public constant PENALTY_PERCENT = 10; // 10% penalty for early unstaking

    struct StakeInfo {
        uint256 amount; // Amount of tokens staked
        uint256 stakeTimestamp; // Timestamp when the stake started
    }

    mapping(address => StakeInfo) public stakes;
    mapping(address => uint256) public rewards;

    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount, uint256 penalty);

    constructor(IERC20 _catecoin) {
        catecoin = _catecoin;
    }

    /**
     * @dev Allows a user to stake Catecoin.
     * @param amount The amount of Catecoin to stake.
     */
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        require(
            catecoin.transferFrom(msg.sender, address(this), amount),
            "Transfer failed"
        );

        // If user already has a stake, add to it
        StakeInfo storage stakeInfo = stakes[msg.sender];
        stakeInfo.amount += amount;
        stakeInfo.stakeTimestamp = block.timestamp;

        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Allows a user to unstake their Catecoin.
     */
    function unstake() external {
        StakeInfo storage stakeInfo = stakes[msg.sender];
        require(stakeInfo.amount > 0, "No stake to unstake");

        uint256 amount = stakeInfo.amount;
        uint256 penalty = 0;

        // Apply penalty if unstaking before 32 days
        if (block.timestamp < stakeInfo.stakeTimestamp + PENALTY_PERIOD) {
            penalty = (amount * PENALTY_PERCENT) / 100;
            amount -= penalty;
        }

        // Clear user's stake
        stakeInfo.amount = 0;
        stakeInfo.stakeTimestamp = 0;

        // Transfer tokens back to the user
        require(
            catecoin.transfer(msg.sender, amount),
            "Transfer failed"
        );

        // Emit event with penalty details
        emit Unstaked(msg.sender, amount, penalty);
    }

    /**
     * @dev Get the staking details for a specific user.
     * @param user The address of the user.
     * @return amount Amount staked and stakeTimestamp Timestamp of the stake.
     */
    function getStakeInfo(address user)
        external
        view
        returns (uint256 amount, uint256 stakeTimestamp)
    {
        StakeInfo storage stakeInfo = stakes[user];
        return (stakeInfo.amount, stakeInfo.stakeTimestamp);
    }
}

// Interface for the Catecoin ERC20 token
interface IERC20 {
    function transferFrom(
        address sender,
        address recipient,
        uint256 amount
    ) external returns (bool);

    function transfer(address recipient, uint256 amount) external returns (bool);
}
```
