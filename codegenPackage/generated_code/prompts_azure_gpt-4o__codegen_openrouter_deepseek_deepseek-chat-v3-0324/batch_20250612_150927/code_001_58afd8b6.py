"""
Generated Code Metadata:
========================
Original URL: https://aero-q62.pages.dev
Prompt: Generate Solidity code for a smart contract that locks $AERO tokens and converts them to veAERO, allowing users to vote on pool emissions and earn incentives.
Generated: DETERMINISTIC_58afd8b6278d2984
Batch ID: 20250612_150927
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/token/ERC20/utils/SafeERC20.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/utils/math/Math.sol";

contract VeAERO is ReentrancyGuard {
    using SafeERC20 for IERC20;

    struct LockedBalance {
        uint256 amount;
        uint256 end;
    }

    IERC20 public immutable token;
    string public constant name = "Vote-escrowed AERO";
    string public constant symbol = "veAERO";
    uint256 public constant decimals = 18;
    uint256 public constant WEEK = 7 days;
    uint256 public constant MAX_TIME = 4 * 365 days;
    uint256 public constant MIN_LOCK_TIME = 1 weeks;

    mapping(address => LockedBalance) public locked;
    uint256 public totalSupply;

    mapping(address => uint256) public balanceOf;
    mapping(address => uint256) public votingPower;
    mapping(address => uint256) public rewards;

    event Deposit(address indexed provider, uint256 value, uint256 indexed locktime, uint256 timestamp);
    event Withdraw(address indexed provider, uint256 value, uint256 timestamp);
    event Vote(address indexed voter, uint256 poolId, uint256 weight);
    event RewardPaid(address indexed user, uint256 reward);

    constructor(address _token) {
        token = IERC20(_token);
    }

    function createLock(uint256 _value, uint256 _unlockTime) external nonReentrant {
        require(_value > 0, "Cannot lock 0 tokens");
        require(_unlockTime > block.timestamp + MIN_LOCK_TIME, "Lock time too short");
        require(_unlockTime <= block.timestamp + MAX_TIME, "Lock time too long");

        LockedBalance storage userLock = locked[msg.sender];
        require(userLock.amount == 0, "Withdraw old tokens first");

        uint256 unlockTime = (_unlockTime / WEEK) * WEEK;
        uint256 duration = unlockTime - block.timestamp;
        uint256 votingPowerAmount = _value * duration / MAX_TIME;

        token.safeTransferFrom(msg.sender, address(this), _value);

        userLock.amount = _value;
        userLock.end = unlockTime;
        totalSupply += _value;
        balanceOf[msg.sender] += _value;
        votingPower[msg.sender] += votingPowerAmount;

        emit Deposit(msg.sender, _value, unlockTime, block.timestamp);
    }

    function increaseAmount(uint256 _value) external nonReentrant {
        require(_value > 0, "Cannot lock 0 tokens");
        LockedBalance storage userLock = locked[msg.sender];
        require(userLock.amount > 0, "No existing lock");
        require(userLock.end > block.timestamp, "Lock expired");

        token.safeTransferFrom(msg.sender, address(this), _value);

        uint256 duration = userLock.end - block.timestamp;
        uint256 votingPowerAmount = _value * duration / MAX_TIME;

        userLock.amount += _value;
        totalSupply += _value;
        balanceOf[msg.sender] += _value;
        votingPower[msg.sender] += votingPowerAmount;

        emit Deposit(msg.sender, _value, userLock.end, block.timestamp);
    }

    function increaseUnlockTime(uint256 _unlockTime) external nonReentrant {
        LockedBalance storage userLock = locked[msg.sender];
        require(userLock.amount > 0, "No existing lock");
        require(_unlockTime > userLock.end, "Can only increase lock time");
        require(_unlockTime <= block.timestamp + MAX_TIME, "Lock time too long");

        uint256 unlockTime = (_unlockTime / WEEK) * WEEK;
        uint256 oldDuration = userLock.end - block.timestamp;
        uint256 newDuration = unlockTime - block.timestamp;
        uint256 votingPowerAmount = userLock.amount * (newDuration - oldDuration) / MAX_TIME;

        userLock.end = unlockTime;
        votingPower[msg.sender] += votingPowerAmount;

        emit Deposit(msg.sender, 0, unlockTime, block.timestamp);
    }

    function withdraw() external nonReentrant {
        LockedBalance storage userLock = locked[msg.sender];
        require(block.timestamp >= userLock.end, "Lock not expired");
        require(userLock.amount > 0, "Nothing to withdraw");

        uint256 value = userLock.amount;
        userLock.amount = 0;
        totalSupply -= value;
        balanceOf[msg.sender] -= value;
        votingPower[msg.sender] = 0;

        token.safeTransfer(msg.sender, value);

        emit Withdraw(msg.sender, value, block.timestamp);
    }

    function vote(uint256 poolId, uint256 weight) external {
        require(votingPower[msg.sender] > 0, "No voting power");
        require(weight <= votingPower[msg.sender], "Weight exceeds voting power");
        
        // In a real implementation, you would have additional checks and logic
        // for pool emissions and vote tracking
        emit Vote(msg.sender, poolId, weight);
    }

    function claimRewards() external nonReentrant {
        uint256 reward = rewards[msg.sender];
        require(reward > 0, "No rewards to claim");

        rewards[msg.sender] = 0;
        token.safeTransfer(msg.sender, reward);

        emit RewardPaid(msg.sender, reward);
    }

    // Admin function to distribute rewards (simplified)
    function distributeRewards(address[] calldata users, uint256[] calldata amounts) external {
        require(users.length == amounts.length, "Arrays length mismatch");
        
        for (uint256 i = 0; i < users.length; i++) {
            rewards[users[i]] += amounts[i];
        }
    }
}
```
