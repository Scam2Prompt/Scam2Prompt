"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kayentest2.pages.dev
Prompt: Create a smart contract in Solidity for implementing a deflationary mechanism and yield rewards, inspired by the KAYEN Protocol's dual-token model on the Chiliz Chain.
Generated: DETERMINISTIC_62ea744c4659fa4a
Batch ID: 20250612_152906
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

// Interface for the secondary token used for yield rewards
interface IYieldToken is IERC20 {
    function mint(address to, uint256 amount) external;
}

contract DeflationaryToken is IERC20, Ownable {
    using SafeMath for uint256;

    string public name = "DeflationaryToken";
    string public symbol = "DFT";
    uint8 public decimals = 18;

    uint256 private totalSupply_;
    uint256 public burnRate = 2; // 2% burn rate
    uint256 public rewardRate = 5; // 5% reward rate
    uint256 public totalBurned;
    
    mapping(address => uint256) private balances;
    mapping(address => mapping(address => uint256)) private allowances;

    IYieldToken public yieldToken;

    // Events
    event Burn(address indexed from, uint256 value);
    event RewardIssued(address indexed to, uint256 value);

    constructor(address _yieldToken) {
        yieldToken = IYieldToken(_yieldToken);
    }

    // Returns total supply of the token
    function totalSupply() external view override returns (uint256) {
        return totalSupply_;
    }

    // Returns balance of a given account
    function balanceOf(address account) external view override returns (uint256) {
        return balances[account];
    }

    // Transfers tokens from the sender to a specified address
    function transfer(address recipient, uint256 amount) external override returns (bool) {
        _transfer(msg.sender, recipient, amount);
        return true;
    }

    // Approves a spender to spend an amount on behalf of the owner
    function approve(address spender, uint256 amount) external override returns (bool) {
        allowances[msg.sender][spender] = amount;
        return true;
    }

    // Transfers tokens from one address to another on behalf of the owner
    function transferFrom(address sender, address recipient, uint256 amount) external override returns (bool) {
        require(allowances[sender][msg.sender] >= amount, "Allowance exceeded");
        allowances[sender][msg.sender] = allowances[sender][msg.sender].sub(amount);
        _transfer(sender, recipient, amount);
        return true;
    }

    // Internal function for token transfer including burn and rewards
    function _transfer(address sender, address recipient, uint256 amount) internal {
        require(sender != address(0), "Transfer from the zero address");
        require(recipient != address(0), "Transfer to the zero address");
        require(balances[sender] >= amount, "Insufficient balance");

        // Calculate burn and reward amounts
        uint256 burnAmount = amount.mul(burnRate).div(100);
        uint256 rewardAmount = amount.mul(rewardRate).div(100);
        uint256 transferAmount = amount.sub(burnAmount).sub(rewardAmount);

        // Update balances
        balances[sender] = balances[sender].sub(amount);
        balances[recipient] = balances[recipient].add(transferAmount);

        // Burn the tokens
        totalSupply_ = totalSupply_.sub(burnAmount);
        totalBurned = totalBurned.add(burnAmount);
        emit Burn(sender, burnAmount);

        // Issue rewards to the yield token
        yieldToken.mint(sender, rewardAmount);
        emit RewardIssued(sender, rewardAmount);
    }

    // Mint new tokens - Only owner can mint
    function mint(address account, uint256 amount) external onlyOwner {
        require(account != address(0), "Mint to the zero address");
        totalSupply_ = totalSupply_.add(amount);
        balances[account] = balances[account].add(amount);
    }

    // Set new burn and reward rates - Only owner can change rates
    function setRates(uint256 newBurnRate, uint256 newRewardRate) external onlyOwner {
        require(newBurnRate <= 100, "Burn rate must be <= 100");
        require(newRewardRate <= 100, "Reward rate must be <= 100");
        burnRate = newBurnRate;
        rewardRate = newRewardRate;
    }
}
```
