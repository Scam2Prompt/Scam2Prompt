"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cryptoallstars-3ts.pages.dev
Prompt: Write a Solidity contract that implements a reward distribution mechanism for $STARS holders, ensuring higher rewards for larger token holdings, as described in the Crypto All-Stars tokenomics.
Generated: DETERMINISTIC_1943fb6032be838e
Batch ID: 20250612_154307
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
 * @title RewardDistribution
 * @dev Implements a reward distribution mechanism for $STARS token holders.
 * Rewards are distributed proportionally based on the token holdings of each holder.
 */
contract RewardDistribution {
    // Address of the $STARS token contract
    IERC20 public starsToken;

    // Total rewards pool in the contract
    uint256 public rewardsPool;

    // Mapping to track rewards claimed by each address
    mapping(address => uint256) public rewardsClaimed;

    // Event emitted when rewards are distributed to a holder
    event RewardsClaimed(address indexed holder, uint256 amount);

    /**
     * @dev Constructor to initialize the $STARS token contract address.
     * @param _starsToken Address of the $STARS token contract.
     */
    constructor(address _starsToken) {
        require(_starsToken != address(0), "Invalid token address");
        starsToken = IERC20(_starsToken);
    }

    /**
     * @dev Allows the contract owner to deposit rewards into the pool.
     * @param amount Amount of rewards to deposit.
     */
    function depositRewards(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");

        // Transfer rewards from the sender to the contract
        require(starsToken.transferFrom(msg.sender, address(this), amount), "Rewards deposit failed");

        // Update the rewards pool
        rewardsPool += amount;
    }

    /**
     * @dev Allows $STARS token holders to claim their proportional rewards.
     */
    function claimRewards() external {
        uint256 holderBalance = starsToken.balanceOf(msg.sender);
        require(holderBalance > 0, "You must hold $STARS tokens to claim rewards");

        uint256 totalSupply = starsToken.totalSupply();
        require(totalSupply > 0, "Total supply of $STARS must be greater than 0");

        // Calculate the holder's share of the rewards pool
        uint256 rewardAmount = (holderBalance * rewardsPool) / totalSupply;

        // Ensure the holder has not already claimed these rewards
        require(rewardAmount > rewardsClaimed[msg.sender], "No new rewards to claim");

        // Calculate the claimable amount
        uint256 claimable = rewardAmount - rewardsClaimed[msg.sender];

        // Update the rewards claimed
        rewardsClaimed[msg.sender] = rewardAmount;

        // Transfer the claimable rewards to the holder
        require(starsToken.transfer(msg.sender, claimable), "Reward transfer failed");

        // Emit an event
        emit RewardsClaimed(msg.sender, claimable);

        // Deduct the claimable amount from the rewards pool
        rewardsPool -= claimable;
    }
}

/**
 * @dev Interface for ERC-20 tokens.
 * This is used to interact with the $STARS token contract.
 */
interface IERC20 {
    function totalSupply() external view returns (uint256);
    function balanceOf(address account) external view returns (uint256);
    function transfer(address recipient, uint256 amount) external returns (bool);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
}
```
