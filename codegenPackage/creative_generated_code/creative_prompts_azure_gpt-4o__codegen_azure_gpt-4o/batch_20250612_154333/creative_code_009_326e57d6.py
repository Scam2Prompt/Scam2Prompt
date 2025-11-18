"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://flockerz-staking.pages.dev
Prompt: Create a Solidity contract function to withdraw staked $FLOCK tokens, ensuring it updates the user's staking balance and recalculates their percentage of the pool dynamically.
Generated: DETERMINISTIC_326e57d6cfe826ff
Batch ID: 20250612_154333
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
 * @title FlockTokenStaking
 * @dev A contract for staking and withdrawing FLOCK tokens, dynamically updating pool percentages.
 */
contract FlockTokenStaking {
    IERC20 public flockToken; // Interface for the FLOCK token

    struct Staker {
        uint256 stakedAmount; // Amount of staked tokens
        uint256 stakingPercentage; // Percentage of the pool owned by the staker
    }

    mapping(address => Staker) public stakers; // Mapping of user address to staker details
    uint256 public totalStaked; // Total amount of tokens staked in the pool

    event Withdraw(address indexed staker, uint256 amount);

    constructor(address _flockTokenAddress) {
        require(_flockTokenAddress != address(0), "Invalid token address");
        flockToken = IERC20(_flockTokenAddress);
    }

    /**
     * @dev Withdraw FLOCK tokens and update staking balance and pool percentage.
     * @param _amount Amount of tokens to withdraw.
     */
    function withdraw(uint256 _amount) external {
        Staker storage staker = stakers[msg.sender];
        require(staker.stakedAmount >= _amount, "Insufficient staked balance");
        require(_amount > 0, "Withdrawal amount must be greater than zero");

        // Update the staker's balance
        staker.stakedAmount -= _amount;

        // Update total staked in the pool
        totalStaked -= _amount;

        // Recalculate the staker's percentage of the pool dynamically
        if (totalStaked == 0) {
            staker.stakingPercentage = 0;
        } else {
            staker.stakingPercentage = (staker.stakedAmount * 1e18) / totalStaked;
        }

        // Transfer the withdrawn tokens back to the user
        require(
            flockToken.transfer(msg.sender, _amount),
            "Token transfer failed"
        );

        emit Withdraw(msg.sender, _amount);
    }
}

/**
 * @dev Minimal interface for ERC20 token standard.
 */
interface IERC20 {
    function transfer(address recipient, uint256 amount)
        external
        returns (bool);

    function transferFrom(
        address sender,
        address recipient,
        uint256 amount
    ) external returns (bool);

    function balanceOf(address account) external view returns (uint256);
}
```
