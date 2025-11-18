"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hydroprotocol-dapp.pages.dev
Prompt: Write a smart contract example for managing LSD-Fi yield farming on Hydro Protocol, ensuring integration with Injective's LSD-Fi infrastructure.
Generated: DETERMINISTIC_ebfa605082dd969b
Batch ID: 20250612_152710
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// This contract manages yield farming for liquid staked derivatives (LSD-Fi) on Hydro Protocol
contract LSDFiYieldFarming is Ownable {
    // Struct for tracking user deposits
    struct UserInfo {
        uint256 amount;     // Amount of tokens deposited by the user
        uint256 rewardDebt; // Reward debt for calculating pending rewards
    }

    // Mapping from user address to their information
    mapping(address => UserInfo) public userInfo;

    // Total amount of tokens staked
    uint256 public totalStaked;
    // Reward tokens (e.g., staked tokens)
    IERC20 public rewardToken;
    // The block number when rewards start
    uint256 public startBlock;
    // The block number when rewards end
    uint256 public endBlock;
    // Reward per block
    uint256 public rewardPerBlock;

    event Deposit(address indexed user, uint256 amount);
    event Withdraw(address indexed user, uint256 amount);
    event EmergencyWithdraw(address indexed user, uint256 amount);

    // Constructor to initialize the contract
    constructor(
        address _rewardToken,
        uint256 _startBlock,
        uint256 _endBlock,
        uint256 _rewardPerBlock
    ) {
        require(_rewardToken != address(0), "Invalid token address");
        require(_startBlock < _endBlock, "Start block must be less than end block");
        
        rewardToken = IERC20(_rewardToken);
        startBlock = _startBlock;
        endBlock = _endBlock;
        rewardPerBlock = _rewardPerBlock;
    }

    // Deposit tokens for yield farming
    function deposit(uint256 _amount) external {
        require(block.number >= startBlock && block.number <= endBlock, "Not in reward period");

        UserInfo storage user = userInfo[msg.sender];
        updateUserRewards(msg.sender);

        // Transfer tokens to this contract
        rewardToken.transferFrom(msg.sender, address(this), _amount);
        user.amount += _amount;
        totalStaked += _amount;

        emit Deposit(msg.sender, _amount);
    }

    // Withdraw tokens and claim rewards
    function withdraw(uint256 _amount) external {
        UserInfo storage user = userInfo[msg.sender];
        require(user.amount >= _amount, "Insufficient balance");

        updateUserRewards(msg.sender);

        user.amount -= _amount;
        totalStaked -= _amount;

        // Transfer tokens back to user
        rewardToken.transfer(msg.sender, _amount);

        emit Withdraw(msg.sender, _amount);
    }

    // Emergency withdraw function to withdraw tokens without reward calculations
    function emergencyWithdraw() external {
        UserInfo storage user = userInfo[msg.sender];
        uint256 amount = user.amount;

        require(amount > 0, "No tokens to withdraw");

        user.amount = 0;
        totalStaked -= amount;

        // Transfer tokens back to user
        rewardToken.transfer(msg.sender, amount);

        emit EmergencyWithdraw(msg.sender, amount);
    }

    // Internal function to update rewards for a user
    function updateUserRewards(address _user) internal {
        UserInfo storage user = userInfo[_user];
        
        if (block.number > startBlock && block.number <= endBlock) {
            uint256 pendingReward = (user.amount * (getCurrentBlockRewards() - user.rewardDebt)) / 1e12;
            if (pendingReward > 0) {
                rewardToken.transfer(_user, pendingReward);
            }
        }

        user.rewardDebt = getCurrentBlockRewards();
    }

    // Get the total rewards that should be distributed up to the current block
    function getCurrentBlockRewards() public view returns (uint256) {
        if (block.number < startBlock) {
            return 0;
        } else if (block.number > endBlock) {
            return (endBlock - startBlock) * rewardPerBlock;
        } else {
            return (block.number - startBlock) * rewardPerBlock;
        }
    }
}
```
