"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://scottytheai-xyz.pages.dev
Prompt: Using the tokenomics details provided, create a Solidity smart contract for $SCOTTY that includes functionality for staking, presale allocation, and reward distribution.
Generated: DETERMINISTIC_68a4412416238871
Batch ID: 20250612_153420
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
 * @title ScottyToken Smart Contract
 * @dev ERC20 token contract with staking, presale allocation, and reward distribution functionalities.
 */
contract ScottyToken {
    // Token details
    string public name = "$SCOTTY";
    string public symbol = "SCOTTY";
    uint8 public decimals = 18;
    uint256 public totalSupply;

    // Tokenomics
    uint256 public presaleAllocation; // Total tokens allocated for presale
    uint256 public stakingRewardsPool; // Total tokens reserved for staking rewards

    // State variables
    mapping(address => uint256) public balanceOf; // Tracks balances of token holders
    mapping(address => mapping(address => uint256)) public allowance; // Tracks allowance for token spending

    // Staking variables
    mapping(address => uint256) public stakedBalances; // Tracks staked balances
    mapping(address => uint256) public stakingTimestamps; // Tracks staking start times
    uint256 public stakingRewardRate = 10; // Reward rate in percentage per year

    // Events
    event Transfer(address indexed from, address indexed to, uint256 value);
    event Approval(address indexed owner, address indexed spender, uint256 value);
    event Staked(address indexed staker, uint256 amount);
    event Unstaked(address indexed staker, uint256 amount);
    event RewardClaimed(address indexed staker, uint256 reward);

    // Constructor to initialize the contract with supply and allocations
    constructor(uint256 _totalSupply, uint256 _presaleAllocation, uint256 _stakingRewardsPool) {
        require(_totalSupply >= _presaleAllocation + _stakingRewardsPool, "Invalid allocations");

        totalSupply = _totalSupply;
        presaleAllocation = _presaleAllocation;
        stakingRewardsPool = _stakingRewardsPool;

        // Assign the entire supply to the contract deployer
        balanceOf[msg.sender] = _totalSupply;
        emit Transfer(address(0), msg.sender, _totalSupply);
    }

    // Basic ERC20 transfer function
    function transfer(address _to, uint256 _value) external returns (bool) {
        require(balanceOf[msg.sender] >= _value, "Insufficient balance");
        balanceOf[msg.sender] -= _value;
        balanceOf[_to] += _value;
        emit Transfer(msg.sender, _to, _value);
        return true;
    }

    // Approve spender function
    function approve(address _spender, uint256 _value) external returns (bool) {
        allowance[msg.sender][_spender] = _value;
        emit Approval(msg.sender, _spender, _value);
        return true;
    }

    // TransferFrom function for delegated transfers
    function transferFrom(address _from, address _to, uint256 _value) external returns (bool) {
        require(balanceOf[_from] >= _value, "Insufficient balance");
        require(allowance[_from][msg.sender] >= _value, "Allowance exceeded");

        balanceOf[_from] -= _value;
        balanceOf[_to] += _value;
        allowance[_from][msg.sender] -= _value;
        emit Transfer(_from, _to, _value);
        return true;
    }

    // Staking function
    function stake(uint256 _amount) external {
        require(balanceOf[msg.sender] >= _amount, "Insufficient balance to stake");

        balanceOf[msg.sender] -= _amount;
        stakedBalances[msg.sender] += _amount;
        stakingTimestamps[msg.sender] = block.timestamp;

        emit Staked(msg.sender, _amount);
    }

    // Unstaking function
    function unstake() external {
        require(stakedBalances[msg.sender] > 0, "No staked balance");

        uint256 stakedAmount = stakedBalances[msg.sender];
        uint256 stakingDuration = block.timestamp - stakingTimestamps[msg.sender];
        uint256 reward = calculateReward(stakedAmount, stakingDuration);

        require(stakingRewardsPool >= reward, "Insufficient reward pool");

        stakedBalances[msg.sender] = 0;
        stakingRewardsPool -= reward;
        balanceOf[msg.sender] += stakedAmount + reward;

        emit RewardClaimed(msg.sender, reward);
        emit Unstaked(msg.sender, stakedAmount);
    }

    // Reward calculation function
    function calculateReward(uint256 _amount, uint256 _duration) public view returns (uint256) {
        uint256 reward = (_amount * stakingRewardRate * _duration) / (365 days * 100);
        return reward;
    }

    // Function to allocate tokens for presale
    function allocatePresale(address _to, uint256 _amount) external {
        require(presaleAllocation >= _amount, "Presale allocation exceeded");
        presaleAllocation -= _amount;
        balanceOf[_to] += _amount;
        emit Transfer(address(0), _to, _amount);
    }
}
```
