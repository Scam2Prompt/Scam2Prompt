"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://galaxyfox-in.pages.dev
Prompt: Write a smart contract in Solidity for a play-to-earn game that incorporates token burning mechanics similar to the $GFOX token described on Galaxy Fox's website. Include staking rewards and deflationary features.
Generated: DETERMINISTIC_39785db3a84a70b6
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
 * @title PlayToEarnGameToken
 * @dev A smart contract for a play-to-earn game token with staking rewards and deflationary token-burning mechanics.
 */
contract PlayToEarnGameToken {
    // Token details
    string public constant name = "GameFox Token";
    string public constant symbol = "GFOX";
    uint8 public constant decimals = 18;
    uint256 public totalSupply;

    // Balances and allowances
    mapping(address => uint256) private balances;
    mapping(address => mapping(address => uint256)) private allowances;

    // Staking details
    mapping(address => uint256) private stakedBalances;
    mapping(address => uint256) private stakingRewards;
    mapping(address => uint256) private lastStakeTime;

    // Token burning details
    uint256 public constant burnRate = 2; // 2% burn rate per transaction
    uint256 public constant stakingRewardRate = 5; // 5% annual staking reward

    // Events
    event Transfer(address indexed from, address indexed to, uint256 value);
    event Approval(address indexed owner, address indexed spender, uint256 value);
    event Burn(address indexed from, uint256 value);
    event Stake(address indexed staker, uint256 value);
    event Unstake(address indexed staker, uint256 value);
    event ClaimRewards(address indexed staker, uint256 value);

    // Constructor
    constructor(uint256 _initialSupply) {
        totalSupply = _initialSupply * 10**decimals;
        balances[msg.sender] = totalSupply; // Assign entire supply to contract deployer
    }

    /**
     * @dev Transfers tokens and burns a percentage based on the burn rate.
     * @param _to The recipient address.
     * @param _value The amount to transfer.
     */
    function transfer(address _to, uint256 _value) external returns (bool) {
        require(_to != address(0), "Transfer to zero address");
        require(balances[msg.sender] >= _value, "Insufficient balance");

        uint256 burnAmount = (_value * burnRate) / 100;
        uint256 transferAmount = _value - burnAmount;

        // Adjust balances
        balances[msg.sender] -= _value;
        balances[_to] += transferAmount;
        totalSupply -= burnAmount; // Burn tokens

        emit Transfer(msg.sender, _to, transferAmount);
        emit Burn(msg.sender, burnAmount);

        return true;
    }

    /**
     * @dev Approves a spender to spend tokens on behalf of the owner.
     */
    function approve(address _spender, uint256 _value) external returns (bool) {
        require(_spender != address(0), "Approve to zero address");
        allowances[msg.sender][_spender] = _value;
        emit Approval(msg.sender, _spender, _value);
        return true;
    }

    /**
     * @dev Transfers tokens on behalf of the owner.
     */
    function transferFrom(
        address _from,
        address _to,
        uint256 _value
    ) external returns (bool) {
        require(_to != address(0), "Transfer to zero address");
        require(balances[_from] >= _value, "Insufficient balance");
        require(allowances[_from][msg.sender] >= _value, "Transfer amount exceeds allowance");

        uint256 burnAmount = (_value * burnRate) / 100;
        uint256 transferAmount = _value - burnAmount;

        // Adjust balances and allowance
        balances[_from] -= _value;
        balances[_to] += transferAmount;
        allowances[_from][msg.sender] -= _value;
        totalSupply -= burnAmount;

        emit Transfer(_from, _to, transferAmount);
        emit Burn(_from, burnAmount);

        return true;
    }

    /**
     * @dev Stakes tokens to earn rewards.
     */
    function stake(uint256 _amount) external {
        require(balances[msg.sender] >= _amount, "Insufficient balance to stake");
        require(_amount > 0, "Stake amount must be greater than 0");

        // Transfer tokens to staking
        balances[msg.sender] -= _amount;
        stakedBalances[msg.sender] += _amount;
        lastStakeTime[msg.sender] = block.timestamp;

        emit Stake(msg.sender, _amount);
    }

    /**
     * @dev Unstakes tokens and claims rewards.
     */
    function unstake() external {
        uint256 stakedBalance = stakedBalances[msg.sender];
        require(stakedBalance > 0, "No staked balance to unstake");

        uint256 rewards = calculateRewards(msg.sender);

        // Unstake tokens and claim rewards
        balances[msg.sender] += stakedBalance + rewards;
        stakedBalances[msg.sender] = 0;
        stakingRewards[msg.sender] = 0;
        lastStakeTime[msg.sender] = 0;

        emit Unstake(msg.sender, stakedBalance);
        emit ClaimRewards(msg.sender, rewards);
    }

    /**
     * @dev Calculates staking rewards for a staker.
     */
    function calculateRewards(address _staker) public view returns (uint256) {
        uint256 stakedBalance = stakedBalances[_staker];
        if (stakedBalance == 0) return 0;

        uint256 stakingDuration = block.timestamp - lastStakeTime[_staker];
        uint256 reward = (stakedBalance * stakingRewardRate * stakingDuration) / (365 days * 100);
        return reward;
    }

    /**
     * @dev Checks the balance of an account.
     */
    function balanceOf(address _account) external view returns (uint256) {
        return balances[_account];
    }

    /**
     * @dev Checks the staked balance of an account.
     */
    function stakedBalanceOf(address _account) external view returns (uint256) {
        return stakedBalances[_account];
    }

    /**
     * @dev Checks the allowance set by an owner to a spender.
     */
    function allowance(address _owner, address _spender) external view returns (uint256) {
        return allowances[_owner][_spender];
    }
}
```
