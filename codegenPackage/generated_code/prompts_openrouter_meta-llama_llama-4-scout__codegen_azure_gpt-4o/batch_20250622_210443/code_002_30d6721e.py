"""
Generated Code Metadata:
========================
Original URL: https://scottytheai-web.pages.dev
Prompt: Design a smart contract for the $SCOTTY token, incorporating staking and reward mechanisms as described in the Scotty AI whitepaper.
Generated: DETERMINISTIC_30d6721ebee5e626
Batch ID: 20250622_210443
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

/**
 * @title SCOTTY Token Smart Contract
 * @dev Implements ERC20 token with staking and reward mechanisms.
 */
contract ScottyToken {
    // Token details
    string public name = "$SCOTTY";
    string public symbol = "SCOTTY";
    uint8 public decimals = 18;
    uint256 public totalSupply;

    // Mapping for balances and allowances
    mapping(address => uint256) public balanceOf;
    mapping(address => mapping(address => uint256)) public allowance;

    // Staking-related mappings
    mapping(address => uint256) public stakedBalance;
    mapping(address => uint256) public stakingStartTime;
    mapping(address => uint256) public rewards;

    // Reward rate (e.g., 10% annual reward rate)
    uint256 public rewardRate = 10; // 10% per year

    // Events
    event Transfer(address indexed from, address indexed to, uint256 value);
    event Approval(address indexed owner, address indexed spender, uint256 value);
    event Staked(address indexed staker, uint256 amount);
    event Unstaked(address indexed staker, uint256 amount);
    event RewardClaimed(address indexed staker, uint256 reward);

    // Constructor to initialize the token supply
    constructor(uint256 _initialSupply) {
        totalSupply = _initialSupply * (10 ** uint256(decimals));
        balanceOf[msg.sender] = totalSupply;
        emit Transfer(address(0), msg.sender, totalSupply);
    }

    // ERC20 transfer function
    function transfer(address _to, uint256 _value) public returns (bool success) {
        require(balanceOf[msg.sender] >= _value, "Insufficient balance");
        balanceOf[msg.sender] -= _value;
        balanceOf[_to] += _value;
        emit Transfer(msg.sender, _to, _value);
        return true;
    }

    // ERC20 approve function
    function approve(address _spender, uint256 _value) public returns (bool success) {
        allowance[msg.sender][_spender] = _value;
        emit Approval(msg.sender, _spender, _value);
        return true;
    }

    // ERC20 transferFrom function
    function transferFrom(address _from, address _to, uint256 _value) public returns (bool success) {
        require(balanceOf[_from] >= _value, "Insufficient balance");
        require(allowance[_from][msg.sender] >= _value, "Allowance exceeded");
        balanceOf[_from] -= _value;
        balanceOf[_to] += _value;
        allowance[_from][msg.sender] -= _value;
        emit Transfer(_from, _to, _value);
        return true;
    }

    // Stake tokens
    function stake(uint256 _amount) public {
        require(balanceOf[msg.sender] >= _amount, "Insufficient balance to stake");
        balanceOf[msg.sender] -= _amount;
        stakedBalance[msg.sender] += _amount;
        stakingStartTime[msg.sender] = block.timestamp;
        emit Staked(msg.sender, _amount);
    }

    // Unstake tokens
    function unstake() public {
        require(stakedBalance[msg.sender] > 0, "No staked balance to unstake");
        uint256 stakedAmount = stakedBalance[msg.sender];
        uint256 reward = calculateReward(msg.sender);

        stakedBalance[msg.sender] = 0;
        stakingStartTime[msg.sender] = 0;
        rewards[msg.sender] = 0;

        balanceOf[msg.sender] += stakedAmount + reward;
        emit Unstaked(msg.sender, stakedAmount);
        emit RewardClaimed(msg.sender, reward);
    }

    // Calculate staking rewards
    function calculateReward(address _staker) public view returns (uint256) {
        if (stakingStartTime[_staker] == 0) {
            return 0;
        }
        uint256 stakingDuration = block.timestamp - stakingStartTime[_staker];
        uint256 annualReward = (stakedBalance[_staker] * rewardRate) / 100;
        return (annualReward * stakingDuration) / 365 days;
    }

    // Claim rewards without unstaking
    function claimReward() public {
        uint256 reward = calculateReward(msg.sender);
        require(reward > 0, "No rewards available to claim");
        rewards[msg.sender] = 0;
        stakingStartTime[msg.sender] = block.timestamp; // Reset staking start time
        balanceOf[msg.sender] += reward;
        emit RewardClaimed(msg.sender, reward);
    }
}
```
