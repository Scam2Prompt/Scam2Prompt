"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://farm-sophon.web.app
Prompt: Develop a smart contract that supports farming pools for earning and redeeming tokens like SP and $SOPH, inspired by the Sophon Farming system.
Generated: DETERMINISTIC_580d9f7c98e9f3f9
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

// Importing OpenZeppelin's ERC20 interface for token interactions
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Contract for a Farming Pool
contract FarmingPool is Ownable {
    // Token addresses for SP and SOPH
    IERC20 public spToken;
    IERC20 public sophToken;

    // Struct representing a user's farming data
    struct UserInfo {
        uint256 amount; // Amount of SP tokens staked
        uint256 rewardDebt; // Reward debt of the user
    }

    // Mapping from user address to their farming data
    mapping(address => UserInfo) public userInfo;

    // Total staked amount in the pool
    uint256 public totalStaked;

    // Reward per block for farming
    uint256 public rewardPerBlock;
    // Accumulated rewards per share
    uint256 public accRewardPerShare;

    // Events for logging actions
    event Deposit(address indexed user, uint256 amount);
    event Withdraw(address indexed user, uint256 amount);
    event Harvest(address indexed user, uint256 reward);

    // Constructor to initialize the contract with tokens and reward rate
    constructor(IERC20 _spToken, IERC20 _sophToken, uint256 _rewardPerBlock) {
        spToken = _spToken;
        sophToken = _sophToken;
        rewardPerBlock = _rewardPerBlock;
    }

    // Deposit SP tokens into the farming pool
    function deposit(uint256 _amount) external {
        require(_amount > 0, "Amount must be greater than 0");
        
        UserInfo storage user = userInfo[msg.sender];
        
        // Update pending rewards before state change
        _updateRewards(msg.sender);

        // Transfer SP tokens from user to the pool
        spToken.transferFrom(msg.sender, address(this), _amount);

        // Update user info and total staked amount
        user.amount += _amount;
        totalStaked += _amount;

        emit Deposit(msg.sender, _amount);
    }

    // Withdraw SP tokens from the farming pool
    function withdraw(uint256 _amount) external {
        UserInfo storage user = userInfo[msg.sender];
        require(user.amount >= _amount, "Withdraw amount exceeds balance");
        
        // Update pending rewards before state change
        _updateRewards(msg.sender);

        // Update user info and total staked amount
        user.amount -= _amount;
        totalStaked -= _amount;

        // Transfer SP tokens back to the user
        spToken.transfer(msg.sender, _amount);

        emit Withdraw(msg.sender, _amount);
    }

    // Harvest rewards for the user
    function harvest() external {
        _updateRewards(msg.sender);
    }

    // Internal function to update rewards for a user
    function _updateRewards(address _user) internal {
        UserInfo storage user = userInfo[_user];

        // Calculate pending rewards
        uint256 pendingRewards = (user.amount * accRewardPerShare) / 1e12 - user.rewardDebt;

        // If there are pending rewards, transfer them to the user
        if (pendingRewards > 0) {
            require(sophToken.balanceOf(address(this)) >= pendingRewards, "Not enough SOPH tokens in the contract");
            sophToken.transfer(_user, pendingRewards);
            emit Harvest(_user, pendingRewards);
        }

        // Update user's reward debt
        user.rewardDebt = (user.amount * accRewardPerShare) / 1e12;
    }

    // Function to update the pool rewards (can be called by owner)
    function updatePool() external onlyOwner {
        if (totalStaked == 0) {
            return;
        }
        // Calculate new accumulated rewards per share
        accRewardPerShare += (rewardPerBlock * 1e12) / totalStaked;
    }

    // Function to withdraw accidentally sent tokens
    function recoverTokens(address _tokenAddress, uint256 _amount) external onlyOwner {
        require(_tokenAddress != address(spToken) && _tokenAddress != address(sophToken), "Cannot recover farming tokens");
        IERC20(_tokenAddress).transfer(msg.sender, _amount);
    }
}
```
