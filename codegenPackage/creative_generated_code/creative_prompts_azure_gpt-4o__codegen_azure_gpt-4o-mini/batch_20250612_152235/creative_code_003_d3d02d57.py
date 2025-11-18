"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://presales99bitcoins.pages.dev
Prompt: Create a smart contract in Solidity that facilitates staking $99BTC tokens and calculates rewards per Ethereum block dynamically.
Generated: DETERMINISTIC_d3d02d57edec783e
Batch ID: 20250612_152235
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

interface IBTC {
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}

contract StakingContract {
    IBTC public btcToken; // Instance of the BTC token contract
    uint256 public totalStaked; // Total amount of BTC tokens staked
    uint256 public blockReward = 1e18; // Reward per Ethereum block (in wei)
    
    struct StakeInfo {
        uint256 amount; // Amount of BTC tokens staked
        uint256 lastRewardBlock; // Last block number when rewards were calculated
        uint256 rewards; // Accumulated rewards for the staker
    }

    mapping(address => StakeInfo) public stakes; // Mapping of staker addresses to their stake information

    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount, uint256 rewards);
    
    /**
     * @dev Constructor to initialize the BTC token contract address.
     * @param _btcTokenAddress Address of the BTC token contract.
     */
    constructor(address _btcTokenAddress) {
        btcToken = IBTC(_btcTokenAddress);
    }

    /**
     * @dev Function to stake BTC tokens.
     * @param amount The amount of BTC tokens to stake.
     */
    function stake(uint256 amount) external {
        require(amount > 0, "Cannot stake 0 tokens");
        
        // Update previous stake rewards before changing the stake
        _updateRewards(msg.sender);
        
        // Transfer BTC tokens from the user to this contract
        require(btcToken.transferFrom(msg.sender, address(this), amount), "Transfer failed");
        
        // Update staking information
        stakes[msg.sender].amount += amount;
        stakes[msg.sender].lastRewardBlock = block.number;
        totalStaked += amount;

        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Function to unstake BTC tokens and claim rewards.
     * @param amount The amount of BTC tokens to unstake.
     */
    function unstake(uint256 amount) external {
        StakeInfo storage stakeInfo = stakes[msg.sender];
        require(stakeInfo.amount >= amount, "Insufficient staked amount");
        
        // Update rewards before unstaking
        _updateRewards(msg.sender);
        
        // Update stake information
        stakeInfo.amount -= amount;
        totalStaked -= amount;
        
        // Transfer BTC tokens back to the user
        require(btcToken.transfer(msg.sender, amount), "Transfer failed");
        
        emit Unstaked(msg.sender, amount, stakeInfo.rewards);
    }

    /**
     * @dev Function to calculate and update the rewards for a staker.
     * @param user The address of the staker.
     */
    function _updateRewards(address user) internal {
        StakeInfo storage stakeInfo = stakes[user];
        if (stakeInfo.amount > 0) {
            // Calculate rewards based on the blocks since the last update
            uint256 blocksEarned = block.number - stakeInfo.lastRewardBlock;
            stakeInfo.rewards += blocksEarned * blockReward * stakeInfo.amount / totalStaked;
            stakeInfo.lastRewardBlock = block.number;
        }
    }

    /**
     * @dev Function to retrieve the staker's rewards.
     * @return The amount of rewards accumulated by the staker.
     */
    function getRewards() external view returns (uint256) {
        StakeInfo storage stakeInfo = stakes[msg.sender];
        uint256 tempStake = stakeInfo.amount;
        uint256 blocksEarned = block.number - stakeInfo.lastRewardBlock;
        uint256 rewards = stakeInfo.rewards + (blocksEarned * blockReward * tempStake / totalStaked);
        return rewards;
    }
}
```
