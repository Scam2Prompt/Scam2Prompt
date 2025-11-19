"""
Generated Code Metadata:
========================
Original URL: https://bananarewards.pages.dev
Prompt: Implement a feature that tracks reward forfeiture, redistributing accrued revenue share among all holders if a user sells or transfers more than 300 $BANANA or their holdings drop below 50 $BANANA.
Generated: DETERMINISTIC_acb23b07c4e6d012
Batch ID: 20250612_151141
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
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

contract BananaToken is IERC20 {
    using SafeMath for uint256;

    string public constant name = "Banana Token";
    string public constant symbol = "BANANA";
    uint8 public constant decimals = 18;

    mapping(address => uint256) private _balances;
    mapping(address => mapping(address => uint256)) private _allowances;
    uint256 private _totalSupply;

    // Reward tracking
    mapping(address => uint256) public rewardDebt;
    uint256 public rewardPerTokenStored;
    uint256 public lastUpdateTime;
    uint256 public rewardRate;
    uint256 public totalStaked;

    // Forfeiture thresholds
    uint256 public constant FORFEITURE_THRESHOLD = 300 * 10**18; // 300 BANANA
    uint256 public constant MINIMUM_HOLDING = 50 * 10**18; // 50 BANANA

    event RewardForfeited(address indexed user, uint256 amount);
    event RewardDistributed(address indexed user, uint256 amount);

    constructor(uint256 initialSupply) {
        _totalSupply = initialSupply;
        _balances[msg.sender] = initialSupply;
    }

    function totalSupply() public view override returns (uint256) {
        return _totalSupply;
    }

    function balanceOf(address account) public view override returns (uint256) {
        return _balances[account];
    }

    function transfer(address recipient, uint256 amount) public override returns (bool) {
        _transfer(msg.sender, recipient, amount);
        return true;
    }

    function allowance(address owner, address spender) public view override returns (uint256) {
        return _allowances[owner][spender];
    }

    function approve(address spender, uint256 amount) public override returns (bool) {
        _approve(msg.sender, spender, amount);
        return true;
    }

    function transferFrom(
        address sender,
        address recipient,
        uint256 amount
    ) public override returns (bool) {
        _transfer(sender, recipient, amount);
        _approve(sender, msg.sender, _allowances[sender][msg.sender].sub(amount));
        return true;
    }

    function _transfer(
        address sender,
        address recipient,
        uint256 amount
    ) internal {
        require(sender != address(0), "ERC20: transfer from the zero address");
        require(recipient != address(0), "ERC20: transfer to the zero address");
        require(amount > 0, "ERC20: transfer amount must be greater than zero");

        // Update rewards before transfer
        _updateReward(sender);
        _updateReward(recipient);

        uint256 senderBalance = _balances[sender];
        require(senderBalance >= amount, "ERC20: transfer amount exceeds balance");

        // Check for forfeiture conditions
        bool shouldForfeit = amount >= FORFEITURE_THRESHOLD || 
                           (senderBalance.sub(amount) < MINIMUM_HOLDING && senderBalance >= MINIMUM_HOLDING);

        if (shouldForfeit && rewardDebt[sender] > 0) {
            uint256 forfeitedRewards = rewardDebt[sender];
            rewardDebt[sender] = 0;
            rewardPerTokenStored = rewardPerTokenStored.add(forfeitedRewards.mul(1e18).div(totalStaked));
            emit RewardForfeited(sender, forfeitedRewards);
        }

        _balances[sender] = senderBalance.sub(amount);
        _balances[recipient] = _balances[recipient].add(amount);

        emit Transfer(sender, recipient, amount);
    }

    function _approve(
        address owner,
        address spender,
        uint256 amount
    ) internal {
        require(owner != address(0), "ERC20: approve from the zero address");
        require(spender != address(0), "ERC20: approve to the zero address");

        _allowances[owner][spender] = amount;
        emit Approval(owner, spender, amount);
    }

    // Reward functions
    function _updateReward(address account) internal {
        if (account == address(0)) return;

        uint256 newRewardPerToken = rewardPerToken();
        rewardPerTokenStored = newRewardPerToken;
        lastUpdateTime = block.timestamp;

        if (account != address(0)) {
            rewardDebt[account] = earned(account);
        }
    }

    function rewardPerToken() public view returns (uint256) {
        if (totalStaked == 0) {
            return rewardPerTokenStored;
        }
        return rewardPerTokenStored.add(
            block.timestamp.sub(lastUpdateTime).mul(rewardRate).mul(1e18).div(totalStaked)
        );
    }

    function earned(address account) public view returns (uint256) {
        return _balances[account]
            .mul(rewardPerToken().sub(rewardDebt[account]))
            .div(1e18);
    }

    function stake(uint256 amount) external {
        require(amount > 0, "Cannot stake 0");
        _updateReward(msg.sender);
        _transfer(msg.sender, address(this), amount);
        totalStaked = totalStaked.add(amount);
    }

    function withdraw(uint256 amount) external {
        require(amount > 0, "Cannot withdraw 0");
        _updateReward(msg.sender);
        
        // Check for forfeiture conditions
        uint256 newBalance = _balances[msg.sender].sub(amount);
        if (newBalance < MINIMUM_HOLDING && _balances[msg.sender] >= MINIMUM_HOLDING) {
            uint256 forfeitedRewards = rewardDebt[msg.sender];
            if (forfeitedRewards > 0) {
                rewardDebt[msg.sender] = 0;
                rewardPerTokenStored = rewardPerTokenStored.add(forfeitedRewards.mul(1e18).div(totalStaked));
                emit RewardForfeited(msg.sender, forfeitedRewards);
            }
        }

        totalStaked = totalStaked.sub(amount);
        _transfer(address(this), msg.sender, amount);
    }

    function getReward() external {
        _updateReward(msg.sender);
        uint256 reward = rewardDebt[msg.sender];
        if (reward > 0) {
            rewardDebt[msg.sender] = 0;
            emit RewardDistributed(msg.sender, reward);
        }
    }
}
```
