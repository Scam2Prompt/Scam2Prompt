"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wienersdog-ai-claim.pages.dev
Prompt: Write a smart contract in Solidity for a presale token similar to WienerAI ($WAI), including features for staking rewards and MEV protection.
Generated: DETERMINISTIC_1c5d9b1de732fc10
Batch ID: 20250612_152240
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
 * @title PresaleTokenWithStakingAndMEVProtection
 * @dev A presale token contract with staking rewards and basic MEV protection.
 */
contract PresaleToken {
    // Token details
    string public name = "PresaleToken";
    string public symbol = "PST";
    uint8 public decimals = 18;
    uint256 public totalSupply;

    // Tracking balances and allowances
    mapping(address => uint256) private balances;
    mapping(address => mapping(address => uint256)) private allowances;

    // Staking variables
    mapping(address => uint256) public stakedBalances;
    mapping(address => uint256) public stakingRewards;
    uint256 public stakingRewardRate = 100; // Rewards per block (adjustable)

    // MEV protection
    mapping(address => uint256) private lastTxBlock;

    // Owner of the contract
    address public owner;

    // Events
    event Transfer(address indexed from, address indexed to, uint256 value);
    event Approval(address indexed owner, address indexed spender, uint256 value);
    event Staked(address indexed staker, uint256 amount);
    event Unstaked(address indexed staker, uint256 amount);
    event ClaimedRewards(address indexed staker, uint256 rewards);

    // Modifiers
    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can call this function.");
        _;
    }

    modifier preventMEV() {
        require(lastTxBlock[msg.sender] != block.number, "MEV protection: Cannot execute multiple transactions in the same block.");
        _;
    }

    /**
     * @dev Constructor to initialize the token supply and set the owner.
     */
    constructor(uint256 _initialSupply) {
        owner = msg.sender;
        totalSupply = _initialSupply * (10 ** decimals);
        balances[msg.sender] = totalSupply;
    }

    /**
     * @dev Transfer tokens to a specified address.
     */
    function transfer(address _to, uint256 _amount) external preventMEV returns (bool) {
        require(_amount <= balances[msg.sender], "Insufficient balance.");
        require(_to != address(0), "Cannot transfer to the zero address.");

        balances[msg.sender] -= _amount;
        balances[_to] += _amount;

        // Update last transaction block
        lastTxBlock[msg.sender] = block.number;

        emit Transfer(msg.sender, _to, _amount);
        return true;
    }

    /**
     * @dev Approve an address to spend tokens on behalf of the owner.
     */
    function approve(address _spender, uint256 _amount) external returns (bool) {
        require(_spender != address(0), "Cannot approve the zero address.");

        allowances[msg.sender][_spender] = _amount;
        emit Approval(msg.sender, _spender, _amount);
        return true;
    }

    /**
     * @dev Transfer tokens from one address to another (using allowance).
     */
    function transferFrom(address _from, address _to, uint256 _amount) external preventMEV returns (bool) {
        require(_amount <= balances[_from], "Insufficient balance.");
        require(_amount <= allowances[_from][msg.sender], "Allowance exceeded.");
        require(_to != address(0), "Cannot transfer to the zero address.");

        balances[_from] -= _amount;
        balances[_to] += _amount;
        allowances[_from][msg.sender] -= _amount;

        // Update last transaction block
        lastTxBlock[_from] = block.number;

        emit Transfer(_from, _to, _amount);
        return true;
    }

    /**
     * @dev Stake tokens to earn rewards.
     */
    function stake(uint256 _amount) external preventMEV {
        require(_amount <= balances[msg.sender], "Insufficient balance.");
        require(_amount > 0, "Staking amount must be greater than zero.");

        balances[msg.sender] -= _amount;
        stakedBalances[msg.sender] += _amount;

        // Update last transaction block
        lastTxBlock[msg.sender] = block.number;

        emit Staked(msg.sender, _amount);
    }

    /**
     * @dev Unstake tokens and claim rewards.
     */
    function unstake() external preventMEV {
        uint256 stakedAmount = stakedBalances[msg.sender];
        require(stakedAmount > 0, "No tokens to unstake.");

        uint256 rewards = calculateRewards(msg.sender);

        stakedBalances[msg.sender] = 0;
        stakingRewards[msg.sender] = 0;

        balances[msg.sender] += stakedAmount + rewards;

        // Update last transaction block
        lastTxBlock[msg.sender] = block.number;

        emit Unstaked(msg.sender, stakedAmount);
        emit ClaimedRewards(msg.sender, rewards);
    }

    /**
     * @dev Calculate staking rewards for a user.
     */
    function calculateRewards(address _staker) public view returns (uint256) {
        return stakingRewards[_staker] + (stakedBalances[_staker] * stakingRewardRate);
    }

    /**
     * @dev Owner can adjust the staking reward rate.
     */
    function setStakingRewardRate(uint256 _rate) external onlyOwner {
        stakingRewardRate = _rate;
    }

    /**
     * @dev Retrieve the balance of an address.
     */
    function balanceOf(address _account) external view returns (uint256) {
        return balances[_account];
    }

    /**
     * @dev Retrieve the staked balance of an address.
     */
    function stakedBalanceOf(address _account) external view returns (uint256) {
        return stakedBalances[_account];
    }

    /**
     * @dev Retrieve the allowance of a spender for an owner's tokens.
     */
    function allowance(address _owner, address _spender) external view returns (uint256) {
        return allowances[_owner][_spender];
    }
}
```
