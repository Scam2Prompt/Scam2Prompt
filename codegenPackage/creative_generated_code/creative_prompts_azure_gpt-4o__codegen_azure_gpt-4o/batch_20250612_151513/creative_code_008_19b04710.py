"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://btc-etftoken.web.app
Prompt: Write a Solidity contract for an ERC-20 token that includes a dynamic staking reward system, where rewards depend on the total amount of tokens staked by the community, as described for BTCETF.
Generated: DETERMINISTIC_19b04710f052fb04
Batch ID: 20250612_151513
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
 * @title BTCETF ERC-20 Token with Dynamic Staking Rewards
 * @author Professional Software Developer
 * @notice This contract implements an ERC-20 token with a dynamic staking reward system.
 * @dev Follows the ERC-20 standard and includes staking functionality.
 */
contract BTCETFToken {
    // Token metadata
    string public name = "BTCETF Token";
    string public symbol = "BTCETF";
    uint8 public decimals = 18;
    uint256 public totalSupply;

    // Token balances mapping
    mapping(address => uint256) public balanceOf;

    // Staking balances mapping
    mapping(address => uint256) public stakingBalance;

    // Allowance mapping for ERC-20
    mapping(address => mapping(address => uint256)) public allowance;

    // Total amount of tokens currently staked in the contract
    uint256 public totalStaked;

    // Rewards pool
    uint256 public rewardsPool;

    // Events
    event Transfer(address indexed from, address indexed to, uint256 value);
    event Approval(address indexed owner, address indexed spender, uint256 value);
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardsDistributed(uint256 rewards);

    // Constructor to initialize the contract and mint initial supply
    constructor(uint256 _initialSupply) {
        totalSupply = _initialSupply * 10**decimals;
        balanceOf[msg.sender] = totalSupply; // Assign all tokens to contract deployer
        emit Transfer(address(0), msg.sender, totalSupply);
    }

    // ERC-20 Transfer function
    function transfer(address _to, uint256 _value) external returns (bool) {
        require(_to != address(0), "Invalid address");
        require(balanceOf[msg.sender] >= _value, "Insufficient balance");

        balanceOf[msg.sender] -= _value;
        balanceOf[_to] += _value;

        emit Transfer(msg.sender, _to, _value);
        return true;
    }

    // ERC-20 Approve function
    function approve(address _spender, uint256 _value) external returns (bool) {
        allowance[msg.sender][_spender] = _value;
        emit Approval(msg.sender, _spender, _value);
        return true;
    }

    // ERC-20 TransferFrom function
    function transferFrom(
        address _from,
        address _to,
        uint256 _value
    ) external returns (bool) {
        require(_to != address(0), "Invalid address");
        require(balanceOf[_from] >= _value, "Insufficient balance");
        require(allowance[_from][msg.sender] >= _value, "Allowance exceeded");

        balanceOf[_from] -= _value;
        balanceOf[_to] += _value;
        allowance[_from][msg.sender] -= _value;

        emit Transfer(_from, _to, _value);
        return true;
    }

    // Stake tokens in the contract
    function stake(uint256 _amount) external {
        require(_amount > 0, "Stake amount must be greater than zero");
        require(balanceOf[msg.sender] >= _amount, "Insufficient balance");

        // Transfer tokens to staking pool
        balanceOf[msg.sender] -= _amount;
        stakingBalance[msg.sender] += _amount;
        totalStaked += _amount;

        emit Staked(msg.sender, _amount);
    }

    // Unstake tokens from the contract
    function unstake(uint256 _amount) external {
        require(_amount > 0, "Unstake amount must be greater than zero");
        require(stakingBalance[msg.sender] >= _amount, "Insufficient staked balance");

        // Transfer tokens back to user's balance
        stakingBalance[msg.sender] -= _amount;
        balanceOf[msg.sender] += _amount;
        totalStaked -= _amount;

        emit Unstaked(msg.sender, _amount);
    }

    // Distribute rewards based on total staked amount
    function distributeRewards(uint256 _rewardAmount) external {
        require(_rewardAmount > 0, "Reward amount must be greater than zero");
        require(balanceOf[msg.sender] >= _rewardAmount, "Insufficient balance");

        // Transfer reward to reward pool
        balanceOf[msg.sender] -= _rewardAmount;
        rewardsPool += _rewardAmount;

        // Calculate and distribute rewards dynamically
        for (address user : getStakers()) {
            uint256 userStake = stakingBalance[user];
            uint256 reward = (_rewardAmount * userStake) / totalStaked; // Proportional reward
            balanceOf[user] += reward;
        }

        emit RewardsDistributed(_rewardAmount);
    }

    // Helper function to retrieve all stakers
    function getStakers() internal view returns (address[] memory) {
        // Placeholder for staker retrieval logic
    }
}
```
