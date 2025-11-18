"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cryptoallstars-3ts.pages.dev
Prompt: Write a Solidity function that calculates dynamic APY rewards for staking $STARS tokens, based on the reward structure outlined in the Crypto All-Stars staking mechanism.
Generated: DETERMINISTIC_0484773140f925bf
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
 * @title APY Reward Calculation for Crypto All-Stars Staking
 * @dev This contract calculates dynamic rewards based on staking duration and APY percentages.
 */
contract StarsStaking {

    // Variable to store APY percentage (e.g., 10% would be represented as 10)
    uint256 public baseAPY;

    // Mapping to store user staking information
    mapping(address => uint256) public stakingStartTime;
    mapping(address => uint256) public stakedAmount;

    /**
     * @dev Constructor to initialize the base APY.
     * @param _baseAPY Initial base APY percentage (e.g., 10 for 10% annual return).
     */
    constructor(uint256 _baseAPY) {
        require(_baseAPY > 0, "Base APY must be greater than zero");
        baseAPY = _baseAPY;
    }

    /**
     * @dev Function to calculate the dynamic APY rewards for a staker.
     * @param staker Address of the staker.
     * @return rewards Amount of $STARS tokens rewarded based on staking duration and APY.
     */
    function calculateRewards(address staker) public view returns (uint256 rewards) {
        // Ensure the staker has staked tokens
        require(stakedAmount[staker] > 0, "No tokens staked by this address");

        // Calculate staking duration in seconds
        uint256 stakingDuration = block.timestamp - stakingStartTime[staker];

        // APY is annual, so we calculate rewards for the duration
        // Formula: (stakedAmount * baseAPY * stakingDuration) / (100 * 365 * 24 * 60 * 60)
        // Division by (100 * seconds in a year) to normalize annual APY to staking duration
        rewards = (stakedAmount[staker] * baseAPY * stakingDuration) / (100 * 365 * 24 * 60 * 60);

        return rewards;
    }

    /**
     * @dev Function to stake $STARS tokens.
     * @param amount Amount of tokens to stake.
     */
    function stakeTokens(uint256 amount) external {
        require(amount > 0, "Staking amount must be greater than zero");

        // Transfer the tokens from the staker to this contract (requires ERC20 approval)
        // Assuming $STARS token implements ERC20 and has a standard transferFrom method
        IERC20 starsToken = IERC20(address(this)); // Replace with actual $STARS token contract address
        require(starsToken.transferFrom(msg.sender, address(this), amount), "Token transfer failed");

        // Update staking information
        stakedAmount[msg.sender] += amount;
        stakingStartTime[msg.sender] = block.timestamp;
    }

    /**
     * @dev Function to withdraw staked tokens and claim rewards.
     */
    function withdrawAndClaimRewards() external {
        require(stakedAmount[msg.sender] > 0, "No tokens staked");

        // Calculate rewards before resetting staking info
        uint256 rewards = calculateRewards(msg.sender);

        // Transfer staked tokens back to the user
        IERC20 starsToken = IERC20(address(this)); // Replace with actual $STARS token contract address
        uint256 amount = stakedAmount[msg.sender];
        require(starsToken.transfer(msg.sender, amount), "Token transfer failed");

        // Reset staking information
        stakedAmount[msg.sender] = 0;
        stakingStartTime[msg.sender] = 0;

        // Transfer rewards to the user
        require(starsToken.transfer(msg.sender, rewards), "Reward transfer failed");
    }
}

/**
 * @dev Minimal interface for ERC20 tokens.
 */
interface IERC20 {
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function transfer(address recipient, uint256 amount) external returns (bool);
}
```
