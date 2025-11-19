"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dogepreneur-in.pages.dev
Prompt: Generate a Solidity contract that represents a DogePreneur token and includes functions for purchasing and staking to earn passive income.
Generated: DETERMINISTIC_f20773db4afe18c1
Batch ID: 20250612_162504
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
 * @title DogePreneur Token Contract
 * @dev ERC-20 token with staking functionality to earn passive income.
 */
contract DogePreneur {
    // Token details
    string public name = "DogePreneur";
    string public symbol = "DOGEP";
    uint8 public decimals = 18;
    uint256 public totalSupply = 1_000_000 * 10 ** uint256(decimals);

    // Balances mapping
    mapping(address => uint256) public balanceOf;
    // Allowance mapping
    mapping(address => mapping(address => uint256)) public allowance;
    // Staking balances
    mapping(address => uint256) public stakedBalance;
    // Staking timestamps
    mapping(address => uint256) public stakingStartTime;

    // Owner of the contract
    address public owner;
    // Reward rate per second (e.g., 0.01% per second)
    uint256 public rewardRate = 1e14; // 0.0001 tokens per second

    // Events
    event Transfer(address indexed from, address indexed to, uint256 value);
    event Approval(address indexed owner, address indexed spender, uint256 value);
    event Staked(address indexed staker, uint256 value);
    event Unstaked(address indexed staker, uint256 value, uint256 reward);

    // Modifier to restrict access to owner-only functions
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can call this function.");
        _;
    }

    // Constructor
    constructor() {
        owner = msg.sender;
        balanceOf[owner] = totalSupply; // Assign initial supply to the owner
        emit Transfer(address(0), owner, totalSupply);
    }

    /**
     * @dev Transfer tokens to another account.
     * @param _to Address to transfer tokens to.
     * @param _value Amount of tokens to transfer.
     */
    function transfer(address _to, uint256 _value) public returns (bool) {
        require(_to != address(0), "Invalid recipient address.");
        require(balanceOf[msg.sender] >= _value, "Insufficient balance.");

        balanceOf[msg.sender] -= _value;
        balanceOf[_to] += _value;

        emit Transfer(msg.sender, _to, _value);
        return true;
    }

    /**
     * @dev Approve another account to spend your tokens.
     * @param _spender Address authorized to spend tokens.
     * @param _value Amount of tokens approved.
     */
    function approve(address _spender, uint256 _value) public returns (bool) {
        allowance[msg.sender][_spender] = _value;
        emit Approval(msg.sender, _spender, _value);
        return true;
    }

    /**
     * @dev Transfer tokens on behalf of another account.
     * @param _from Address transferring tokens from.
     * @param _to Address transferring tokens to.
     * @param _value Amount of tokens to transfer.
     */
    function transferFrom(address _from, address _to, uint256 _value) public returns (bool) {
        require(_to != address(0), "Invalid recipient address.");
        require(balanceOf[_from] >= _value, "Insufficient balance.");
        require(allowance[_from][msg.sender] >= _value, "Allowance exceeded.");

        balanceOf[_from] -= _value;
        allowance[_from][msg.sender] -= _value;
        balanceOf[_to] += _value;

        emit Transfer(_from, _to, _value);
        return true;
    }

    /**
     * @dev Stake tokens to earn passive income.
     * @param _value Amount of tokens to stake.
     */
    function stake(uint256 _value) public {
        require(balanceOf[msg.sender] >= _value, "Insufficient balance to stake.");
        require(_value > 0, "Cannot stake zero tokens.");

        // Transfer tokens to staking balance
        balanceOf[msg.sender] -= _value;
        stakedBalance[msg.sender] += _value;
        stakingStartTime[msg.sender] = block.timestamp;

        emit Staked(msg.sender, _value);
    }

    /**
     * @dev Unstake tokens and claim rewards.
     */
    function unstake() public {
        uint256 stakedAmount = stakedBalance[msg.sender];
        require(stakedAmount > 0, "No tokens are staked.");

        // Calculate staking rewards
        uint256 stakingDuration = block.timestamp - stakingStartTime[msg.sender];
        uint256 reward = stakingDuration * rewardRate * stakedAmount / 1e18;

        // Reset staking data
        stakedBalance[msg.sender] = 0;
        stakingStartTime[msg.sender] = 0;

        // Transfer original stake + rewards back to the user
        balanceOf[msg.sender] += stakedAmount + reward;

        emit Unstaked(msg.sender, stakedAmount, reward);
    }

    /**
     * @dev Owner can update the reward rate.
     * @param _newRewardRate New reward rate per second.
     */
    function updateRewardRate(uint256 _newRewardRate) public onlyOwner {
        rewardRate = _newRewardRate;
    }
}
```
