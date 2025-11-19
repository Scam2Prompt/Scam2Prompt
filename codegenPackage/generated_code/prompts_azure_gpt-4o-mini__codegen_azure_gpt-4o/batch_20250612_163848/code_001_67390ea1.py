"""
Generated Code Metadata:
========================
Original URL: https://kangamoon-claim.pages.dev
Prompt: Generate a Solidity smart contract for a token similar to $KANG, ensuring it includes features for staking and rewards as described in the Kangamoon documentation.
Generated: DETERMINISTIC_67390ea1dcc52fb2
Batch ID: 20250612_163848
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
 * @title KangToken
 * @dev ERC20 Token with staking and rewards functionality.
 */
contract KangToken {
    // Token details
    string public name = "KangToken";
    string public symbol = "KANG";
    uint8 public decimals = 18;
    uint256 public totalSupply;

    // Balances and allowances
    mapping(address => uint256) private balances;
    mapping(address => mapping(address => uint256)) private allowances;

    // Staking details
    mapping(address => uint256) private stakedBalances;
    mapping(address => uint256) private stakingStartTime;
    uint256 public rewardRate = 10; // Reward rate in percentage per year

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

    // ERC20 Functions
    function balanceOf(address account) public view returns (uint256) {
        return balances[account];
    }

    function transfer(address recipient, uint256 amount) public returns (bool) {
        require(recipient != address(0), "Transfer to zero address");
        require(balances[msg.sender] >= amount, "Insufficient balance");

        balances[msg.sender] -= amount;
        balances[recipient] += amount;
        emit Transfer(msg.sender, recipient, amount);
        return true;
    }

    function approve(address spender, uint256 amount) public returns (bool) {
        require(spender != address(0), "Approve to zero address");

        allowances[msg.sender][spender] = amount;
        emit Approval(msg.sender, spender, amount);
        return true;
    }

    function allowance(address owner, address spender) public view returns (uint256) {
        return allowances[owner][spender];
    }

    function transferFrom(address sender, address recipient, uint256 amount) public returns (bool) {
        require(sender != address(0), "Transfer from zero address");
        require(recipient != address(0), "Transfer to zero address");
        require(balances[sender] >= amount, "Insufficient balance");
        require(allowances[sender][msg.sender] >= amount, "Allowance exceeded");

        balances[sender] -= amount;
        balances[recipient] += amount;
        allowances[sender][msg.sender] -= amount;
        emit Transfer(sender, recipient, amount);
        return true;
    }

    // Staking Functions
    function stake(uint256 amount) public {
        require(amount > 0, "Cannot stake zero tokens");
        require(balances[msg.sender] >= amount, "Insufficient balance to stake");

        // Transfer tokens to staking pool
        balances[msg.sender] -= amount;
        stakedBalances[msg.sender] += amount;
        stakingStartTime[msg.sender] = block.timestamp;

        emit Staked(msg.sender, amount);
    }

    function unstake() public {
        uint256 stakedAmount = stakedBalances[msg.sender];
        require(stakedAmount > 0, "No tokens staked");

        // Calculate rewards
        uint256 stakingDuration = block.timestamp - stakingStartTime[msg.sender];
        uint256 reward = (stakedAmount * rewardRate * stakingDuration) / (365 days * 100);

        // Update balances
        stakedBalances[msg.sender] = 0;
        stakingStartTime[msg.sender] = 0;
        balances[msg.sender] += stakedAmount + reward;

        emit Unstaked(msg.sender, stakedAmount, reward);
    }

    function stakedBalanceOf(address account) public view returns (uint256) {
        return stakedBalances[account];
    }

    function calculateReward(address account) public view returns (uint256) {
        uint256 stakedAmount = stakedBalances[account];
        if (stakedAmount == 0) {
            return 0;
        }

        uint256 stakingDuration = block.timestamp - stakingStartTime[account];
        uint256 reward = (stakedAmount * rewardRate * stakingDuration) / (365 days * 100);
        return reward;
    }
}
```
