"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://galaxyfox-en.pages.dev
Prompt: Write a smart contract in Solidity for staking $GFOX tokens, ensuring a 2% contribution to the staking rewards pool for every transaction, as described in the Galaxy Fox ecosystem.
Generated: DETERMINISTIC_de312d0506098c6a
Batch ID: 20250612_145913
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
 * @title GFOX Staking Contract
 * @dev This contract allows users to stake $GFOX tokens and automatically contributes 2% of each stake to the staking rewards pool.
 */
interface IERC20 {
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function transfer(address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}

contract GFOXStaking {
    // State variables
    IERC20 public gfoxToken; // ERC20 token contract
    address public rewardsPool; // Address of the staking rewards pool

    mapping(address => uint256) public stakes; // Tracks each user's staked amount

    event Staked(address indexed user, uint256 amount, uint256 rewardContribution);
    event Withdrawn(address indexed user, uint256 amount);

    /**
     * @dev Constructor to initialize the contract.
     * @param _gfoxToken Address of the $GFOX token contract.
     * @param _rewardsPool Address of the rewards pool.
     */
    constructor(IERC20 _gfoxToken, address _rewardsPool) {
        require(address(_gfoxToken) != address(0), "Invalid token address");
        require(_rewardsPool != address(0), "Invalid rewards pool address");

        gfoxToken = _gfoxToken;
        rewardsPool = _rewardsPool;
    }

    /**
     * @dev Allows users to stake $GFOX tokens.
     * @param amount The amount of $GFOX tokens to stake.
     */
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");

        // Calculate the 2% reward contribution
        uint256 rewardContribution = (amount * 2) / 100;

        // Ensure the sender has enough tokens and approves the transfer
        require(gfoxToken.transferFrom(msg.sender, address(this), amount), "Token transfer failed");

        // Transfer the 2% contribution to the rewards pool
        require(gfoxToken.transfer(rewardsPool, rewardContribution), "Reward transfer failed");

        // Update the staked amount (minus the 2% contribution)
        uint256 netStake = amount - rewardContribution;
        stakes[msg.sender] += netStake;

        emit Staked(msg.sender, netStake, rewardContribution);
    }

    /**
     * @dev Allows users to withdraw their staked $GFOX tokens.
     */
    function withdraw() external {
        uint256 stakedAmount = stakes[msg.sender];
        require(stakedAmount > 0, "No staked tokens to withdraw");

        // Reset the user's staked amount
        stakes[msg.sender] = 0;

        // Transfer the staked tokens back to the user
        require(gfoxToken.transfer(msg.sender, stakedAmount), "Token transfer failed");

        emit Withdrawn(msg.sender, stakedAmount);
    }

    /**
     * @dev Retrieves the staked amount of $GFOX tokens for a given user.
     * @param user The address of the user.
     * @return The staked amount of $GFOX tokens.
     */
    function getStakedAmount(address user) external view returns (uint256) {
        return stakes[user];
    }
}
```
