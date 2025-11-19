"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aitechpad-io.pages.dev
Prompt: Write a smart contract for a staking pool that supports different reward rates and compounding options for AITECH tokens, similar to those outlined on the Solidus AI Tech platform.
Generated: DETERMINISTIC_1317dc25a3084b73
Batch ID: 20250612_161500
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

// Importing OpenZeppelin's ERC20 interface for AITECH token interaction
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Staking Pool contract
contract StakingPool is Ownable {
    // IERC20 interface for AITECH tokens
    IERC20 public aitechToken;

    // Structure to hold user staking data
    struct UserInfo {
        uint256 amount;         // Amount of tokens staked
        uint256 rewardDebt;     // Reward debt for user
        uint256 lastRewardTime; // Last time rewards were calculated
    }

    // Mapping of user address to UserInfo
    mapping(address => UserInfo) public userInfo;

    // Total staked tokens in the pool
    uint256 public totalStaked;

    // Reward per token per second
    uint256 public rewardRate;

    // Event to emit on staking
    event Staked(address indexed user, uint256 amount);
    
    // Event to emit on withdrawing
    event Withdrawn(address indexed user, uint256 amount);

    // Event to emit on claiming rewards
    event RewardClaimed(address indexed user, uint256 amount);

    // Constructor to set the AITECH token address and initial reward rate
    constructor(IERC20 _aitechToken, uint256 _initialRewardRate) {
        aitechToken = _aitechToken;
        rewardRate = _initialRewardRate;
    }

    // Function to stake tokens
    function stake(uint256 _amount) external {
        require(_amount > 0, "Amount must be greater than 0");

        // Transfer AITECH tokens from user to contract
        aitechToken.transferFrom(msg.sender, address(this), _amount);

        // Update user and pool state
        UserInfo storage user = userInfo[msg.sender];
        user.amount += _amount;
        user.rewardDebt += _pendingReward(msg.sender);

        totalStaked += _amount;

        emit Staked(msg.sender, _amount);
    }

    // Function to withdraw staked tokens
    function withdraw(uint256 _amount) external {
        UserInfo storage user = userInfo[msg.sender];
        require(user.amount >= _amount, "Withdraw amount exceeds staked amount");

        // Calculate pending rewards and update state
        user.rewardDebt += _pendingReward(msg.sender);
        user.amount -= _amount;
        totalStaked -= _amount;

        // Transfer AITECH tokens back to user
        aitechToken.transfer(msg.sender, _amount);

        emit Withdrawn(msg.sender, _amount);
    }

    // Function to claim rewards
    function claimRewards() external {
        UserInfo storage user = userInfo[msg.sender];
        uint256 pending = _pendingReward(msg.sender);
        require(pending > 0, "No rewards available");

        // Update user reward debt
        user.rewardDebt += pending;
        
        // Transfer rewards to user
        aitechToken.transfer(msg.sender, pending);

        emit RewardClaimed(msg.sender, pending);
    }

    // Internal function to calculate pending rewards for a user
    function _pendingReward(address _user) internal view returns (uint256) {
        UserInfo storage user = userInfo[_user];
        return (user.amount * rewardRate * (block.timestamp - user.lastRewardTime)) / 1e18;
    }

    // Function to update the reward rate, can only be called by the owner
    function updateRewardRate(uint256 _newRate) external onlyOwner {
        rewardRate = _newRate;
    }

    // Function to view the user's total rewards
    function viewRewards(address _user) external view returns (uint256) {
        return _pendingReward(_user) + userInfo[_user].rewardDebt;
    }
}
```
