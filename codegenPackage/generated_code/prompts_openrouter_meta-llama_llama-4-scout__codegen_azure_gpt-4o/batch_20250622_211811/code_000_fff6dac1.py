"""
Generated Code Metadata:
========================
Original URL: https://berachain.pumpevm.net
Prompt: "Write a smart contract in Solidity for a blockchain project similar to BeraChain, using EVM-compatible features."
Generated: DETERMINISTIC_fff6dac1b9f503b7
Batch ID: 20250622_211811
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
 * @title BeraChain-like Smart Contract
 * @dev This contract implements a basic token system with staking functionality.
 * It is designed to be EVM-compatible and follows Solidity best practices.
 */
contract BeraChainToken {
    // State variables
    string public name = "BeraChainToken";
    string public symbol = "BCT";
    uint8 public decimals = 18;
    uint256 public totalSupply;

    mapping(address => uint256) private balances;
    mapping(address => mapping(address => uint256)) private allowances;

    // Staking-related variables
    mapping(address => uint256) private stakedBalances;
    mapping(address => uint256) private stakingStartTime;
    uint256 public stakingRewardRate = 10; // Reward rate in percentage

    // Events
    event Transfer(address indexed from, address indexed to, uint256 value);
    event Approval(address indexed owner, address indexed spender, uint256 value);
    event Staked(address indexed staker, uint256 amount);
    event Unstaked(address indexed staker, uint256 amount, uint256 reward);

    // Constructor
    constructor(uint256 _initialSupply) {
        totalSupply = _initialSupply * (10 ** uint256(decimals));
        balances[msg.sender] = totalSupply;
        emit Transfer(address(0), msg.sender, totalSupply);
    }

    // Modifier to check sufficient balance
    modifier hasSufficientBalance(address _account, uint256 _amount) {
        require(balances[_account] >= _amount, "Insufficient balance");
        _;
    }

    // Modifier to check sufficient staked balance
    modifier hasSufficientStakedBalance(address _account, uint256 _amount) {
        require(stakedBalances[_account] >= _amount, "Insufficient staked balance");
        _;
    }

    // Transfer function
    function transfer(address _to, uint256 _amount) external hasSufficientBalance(msg.sender, _amount) returns (bool) {
        require(_to != address(0), "Invalid recipient address");

        balances[msg.sender] -= _amount;
        balances[_to] += _amount;

        emit Transfer(msg.sender, _to, _amount);
        return true;
    }

    // Approve function
    function approve(address _spender, uint256 _amount) external returns (bool) {
        require(_spender != address(0), "Invalid spender address");

        allowances[msg.sender][_spender] = _amount;
        emit Approval(msg.sender, _spender, _amount);
        return true;
    }

    // TransferFrom function
    function transferFrom(address _from, address _to, uint256 _amount) external hasSufficientBalance(_from, _amount) returns (bool) {
        require(_to != address(0), "Invalid recipient address");
        require(allowances[_from][msg.sender] >= _amount, "Allowance exceeded");

        balances[_from] -= _amount;
        balances[_to] += _amount;
        allowances[_from][msg.sender] -= _amount;

        emit Transfer(_from, _to, _amount);
        return true;
    }

    // Stake function
    function stake(uint256 _amount) external hasSufficientBalance(msg.sender, _amount) {
        balances[msg.sender] -= _amount;
        stakedBalances[msg.sender] += _amount;
        stakingStartTime[msg.sender] = block.timestamp;

        emit Staked(msg.sender, _amount);
    }

    // Unstake function
    function unstake(uint256 _amount) external hasSufficientStakedBalance(msg.sender, _amount) {
        uint256 stakingDuration = block.timestamp - stakingStartTime[msg.sender];
        uint256 reward = (_amount * stakingRewardRate * stakingDuration) / (100 * 365 days);

        stakedBalances[msg.sender] -= _amount;
        balances[msg.sender] += _amount + reward;

        emit Unstaked(msg.sender, _amount, reward);
    }

    // BalanceOf function
    function balanceOf(address _account) external view returns (uint256) {
        return balances[_account];
    }

    // StakedBalanceOf function
    function stakedBalanceOf(address _account) external view returns (uint256) {
        return stakedBalances[_account];
    }

    // Allowance function
    function allowance(address _owner, address _spender) external view returns (uint256) {
        return allowances[_owner][_spender];
    }
}
```
