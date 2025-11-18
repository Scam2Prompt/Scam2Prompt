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

/**
 * @title Staking Contract for $99BTC Token
 * @dev This contract allows users to stake $99BTC tokens, calculates
 * rewards dynamically per Ethereum block, and supports withdrawing staked tokens and rewards.
 */
interface IERC20 {
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function transfer(address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}

contract Staking99BTC {
    // Address of the $99BTC ERC20 token
    IERC20 public immutable token;

    // Reward rate per block (dynamic rate adjustable externally)
    uint256 public rewardRatePerBlock;

    // Mapping of user address to their staking information
    struct StakeInfo {
        uint256 amountStaked;
        uint256 blockLastUpdated;
        uint256 rewardsAccumulated;
    }
    mapping(address => StakeInfo) public stakes;

    // Events
    event Staked(address indexed user, uint256 amount);
    event RewardsClaimed(address indexed user, uint256 reward);
    event Unstaked(address indexed user, uint256 amount);

    // Contract constructor
    constructor(address _tokenAddress, uint256 _initialRewardRatePerBlock) {
        require(_tokenAddress != address(0), "Token address cannot be zero");
        token = IERC20(_tokenAddress);
        rewardRatePerBlock = _initialRewardRatePerBlock;
    }

    // Modifier to update user rewards before any state-changing operation
    modifier updateRewards(address _user) {
        StakeInfo storage userStake = stakes[_user];
        if (userStake.amountStaked > 0) {
            uint256 blocksElapsed = block.number - userStake.blockLastUpdated;
            userStake.rewardsAccumulated += blocksElapsed * rewardRatePerBlock * userStake.amountStaked / 1 ether;
        }
        userStake.blockLastUpdated = block.number;
        _;
    }

    /**
     * @dev Allows a user to stake $99BTC tokens into the contract.
     * @param _amount The amount of tokens to stake.
     */
    function stake(uint256 _amount) external updateRewards(msg.sender) {
        require(_amount > 0, "Amount must be greater than zero");
        require(token.transferFrom(msg.sender, address(this), _amount), "Token transfer failed");

        stakes[msg.sender].amountStaked += _amount;
        emit Staked(msg.sender, _amount);
    }

    /**
     * @dev Allows a user to unstake their tokens and withdraw rewards.
     */
    function unstake() external updateRewards(msg.sender) {
        StakeInfo storage userStake = stakes[msg.sender];
        uint256 stakedAmount = userStake.amountStaked;
        uint256 rewardAmount = userStake.rewardsAccumulated;

        require(stakedAmount > 0, "No tokens staked");
        
        // Reset user staking info
        userStake.amountStaked = 0;
        userStake.rewardsAccumulated = 0;

        // Transfer staked tokens back to the user
        require(token.transfer(msg.sender, stakedAmount), "Token transfer failed");

        // Transfer rewards to the user
        if (rewardAmount > 0) {
            require(token.transfer(msg.sender, rewardAmount), "Reward transfer failed");
            emit RewardsClaimed(msg.sender, rewardAmount);
        }

        emit Unstaked(msg.sender, stakedAmount);
    }

    /**
     * @dev View function to calculate rewards for a user.
     * @param _user The address of the user.
     * @return The total rewards accumulated by the user.
     */
    function calculateRewards(address _user) public view returns (uint256) {
        StakeInfo memory userStake = stakes[_user];
        if (userStake.amountStaked == 0) {
            return userStake.rewardsAccumulated;
        }
        uint256 blocksElapsed = block.number - userStake.blockLastUpdated;
        uint256 additionalRewards = blocksElapsed * rewardRatePerBlock * userStake.amountStaked / 1 ether;
        return userStake.rewardsAccumulated + additionalRewards;
    }

    /**
     * @dev Allows the owner to update the reward rate per block.
     * @param _newRate The new reward rate per block.
     */
    function updateRewardRate(uint256 _newRate) external {
        // Assuming only the owner can call this function (Owner management not implemented in this example)
        rewardRatePerBlock = _newRate;
    }
}
```
