"""
Generated Code Metadata:
========================
Original URL: https://astredex.com
Prompt: Create a smart contract code snippet for minting and staking pool tokens with USDT, BNB, and more on Aster to earn passive income and increase chances for future airdrops.
Generated: DETERMINISTIC_f735b94f6879e4e3
Batch ID: 20250622_212748
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

// Importing necessary interfaces and libraries
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

// Smart contract for minting and staking pool tokens
contract StakingPool is Ownable {
    using SafeMath for uint256;

    // Token to be staked (e.g., USDT, BNB)
    IERC20 public stakingToken;
    // Token to be minted as rewards
    IERC20 public rewardToken;

    // Struct to hold user staking information
    struct UserInfo {
        uint256 amount;     // Amount of tokens staked
        uint256 rewardDebt; // Reward debt
    }

    // Mapping of user addresses to their staking information
    mapping(address => UserInfo) public userInfo;

    // Total staked amount
    uint256 public totalStaked;
    // Accumulated rewards per share
    uint256 public accRewardPerShare;
    // Reward token per block
    uint256 public rewardPerBlock;

    // Events for logging
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 amount);

    // Constructor to initialize the contract
    constructor(IERC20 _stakingToken, IERC20 _rewardToken, uint256 _rewardPerBlock) {
        stakingToken = _stakingToken;
        rewardToken = _rewardToken;
        rewardPerBlock = _rewardPerBlock;
    }

    // Function to stake tokens
    function stake(uint256 _amount) external {
        require(_amount > 0, "Amount must be greater than 0");

        // Update user rewards before staking
        updateUserRewards(msg.sender);

        // Transfer staking tokens from user to contract
        stakingToken.transferFrom(msg.sender, address(this), _amount);

        // Update user info
        userInfo[msg.sender].amount = userInfo[msg.sender].amount.add(_amount);
        totalStaked = totalStaked.add(_amount);

        emit Staked(msg.sender, _amount);
    }

    // Function to unstake tokens
    function unstake(uint256 _amount) external {
        require(_amount > 0, "Amount must be greater than 0");
        require(userInfo[msg.sender].amount >= _amount, "Insufficient staked amount");

        // Update user rewards before unstaking
        updateUserRewards(msg.sender);

        // Transfer staking tokens back to user
        stakingToken.transfer(msg.sender, _amount);

        // Update user info
        userInfo[msg.sender].amount = userInfo[msg.sender].amount.sub(_amount);
        totalStaked = totalStaked.sub(_amount);

        emit Unstaked(msg.sender, _amount);
    }

    // Function to claim rewards
    function claimRewards() external {
        updateUserRewards(msg.sender);
        uint256 reward = userInfo[msg.sender].rewardDebt;

        require(reward > 0, "No rewards to claim");

        // Reset user's reward debt
        userInfo[msg.sender].rewardDebt = 0;

        // Transfer reward tokens to user
        rewardToken.transfer(msg.sender, reward);

        emit RewardClaimed(msg.sender, reward);
    }

    // Internal function to update user rewards
    function updateUserRewards(address _user) internal {
        if (totalStaked > 0) {
            // Calculate accumulated rewards per share
            uint256 blocks = block.number; // Simplified for demonstration
            accRewardPerShare = accRewardPerShare.add((blocks.mul(rewardPerBlock)).div(totalStaked));
        }

        // Calculate pending rewards for the user
        uint256 pending = userInfo[_user].amount.mul(accRewardPerShare).div(1e12).sub(userInfo[_user].rewardDebt);
        userInfo[_user].rewardDebt = userInfo[_user].amount.mul(accRewardPerShare).div(1e12);

        // If there are pending rewards, update the user's reward debt
        if (pending > 0) {
            userInfo[_user].rewardDebt = userInfo[_user].rewardDebt.add(pending);
        }
    }

    // Function to set reward per block (only owner)
    function setRewardPerBlock(uint256 _rewardPerBlock) external onlyOwner {
        rewardPerBlock = _rewardPerBlock;
    }
}
```
