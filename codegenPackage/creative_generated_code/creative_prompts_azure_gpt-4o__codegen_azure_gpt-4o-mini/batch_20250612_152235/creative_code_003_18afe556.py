"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://enlist-paramgamingcom.pages.dev
Prompt: Create a smart contract in Solidity for staking tokens and distributing rewards, following the Param Network's tokenomics structure.
Generated: DETERMINISTIC_18afe55627ed4d62
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

// Importing OpenZeppelin's ERC20 interface for token interaction
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Staking contract for token staking and reward distribution
contract TokenStaking is Ownable {
    IERC20 public immutable stakingToken; // The token to be staked
    IERC20 public immutable rewardToken; // The token used for rewards

    // Struct to hold user information for staking
    struct UserInfo {
        uint256 amount; // Amount of tokens staked
        uint256 rewardDebt; // Reward debt for user
    }

    // Mapping of user address to their staking information
    mapping(address => UserInfo) public userInfo;

    // Total amount of staked tokens
    uint256 public totalStaked;

    // Accumulated rewards per staked token
    uint256 public accRewardPerShare;

    // Event emitted when tokens are staked
    event Staked(address indexed user, uint256 amount);
    
    // Event emitted when tokens are withdrawn
    event Withdrawn(address indexed user, uint256 amount);

    // Event emitted when rewards are claimed
    event RewardClaimed(address indexed user, uint256 amount);

    constructor(IERC20 _stakingToken, IERC20 _rewardToken) {
        stakingToken = _stakingToken;
        rewardToken = _rewardToken;
    }

    // Function to stake tokens
    function stake(uint256 _amount) external {
        require(_amount > 0, "Cannot stake 0");

        UserInfo storage user = userInfo[msg.sender];

        // Update rewards before staking
        _updateRewards(msg.sender);
        
        // Transfer tokens from user to contract
        stakingToken.transferFrom(msg.sender, address(this), _amount);

        // Update user information
        user.amount += _amount;
        totalStaked += _amount;

        emit Staked(msg.sender, _amount);
    }

    // Function to withdraw staked tokens
    function withdraw(uint256 _amount) external {
        UserInfo storage user = userInfo[msg.sender];
        require(user.amount >= _amount, "Insufficient staked amount");

        // Update rewards before withdrawal
        _updateRewards(msg.sender);
        
        // Transfer tokens back to user
        user.amount -= _amount;
        totalStaked -= _amount;
        stakingToken.transfer(msg.sender, _amount);

        emit Withdrawn(msg.sender, _amount);
    }

    // Function to claim rewards
    function claimRewards() external {
        UserInfo storage user = userInfo[msg.sender];

        // Update rewards before claiming
        _updateRewards(msg.sender);
        
        uint256 reward = user.rewardDebt;
        require(reward > 0, "No rewards to claim");

        // Reset user's reward debt
        user.rewardDebt = 0;
        rewardToken.transfer(msg.sender, reward);

        emit RewardClaimed(msg.sender, reward);
    }

    // Internal function to update rewards for a user
    function _updateRewards(address _user) internal {
        UserInfo storage user = userInfo[_user];
        
        if (totalStaked > 0) {
            // Calculate accumulated rewards per share
            accRewardPerShare += (rewardToken.balanceOf(address(this)) * 1e12) / totalStaked;
        }

        // Calculate user's pending rewards
        uint256 pending = (user.amount * accRewardPerShare) / 1e12 - user.rewardDebt;
        user.rewardDebt += pending; // Update user's reward debt
    }

    // Function to withdraw excess tokens from the contract (only owner)
    function withdrawExcessTokens(IERC20 _token, uint256 _amount) external onlyOwner {
        require(_token != stakingToken && _token != rewardToken, "Cannot withdraw staking or reward token");
        _token.transfer(msg.sender, _amount);
    }

    // Function to get pending rewards for a user
    function pendingRewards(address _user) external view returns (uint256) {
        UserInfo storage user = userInfo[_user];
        uint256 adjustedAccRewardPerShare = accRewardPerShare;
        
        if (totalStaked > 0) {
            adjustedAccRewardPerShare += (rewardToken.balanceOf(address(this)) * 1e12) / totalStaked;
        }

        return (user.amount * adjustedAccRewardPerShare) / 1e12 - user.rewardDebt;
    }
}
```
