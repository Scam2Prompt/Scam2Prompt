"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://everlodge-io.web.app
Prompt: Generate code for an ERC-20 token contract in Solidity, incorporating features like staking rewards, membership benefits, and trading fee discounts, similar to Everlodge's $ELDG token.
Generated: DETERMINISTIC_45835d6c394b383c
Batch ID: 20250612_151906
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

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

contract ELDGToken is ERC20, Ownable {
    using SafeMath for uint256;

    // Mapping to track staking balances of each address
    mapping(address => uint256) private _stakingBalances;

    // Total staking rewards distributed
    uint256 public totalStakingRewards;

    // Membership benefits - can be extended to include more features
    mapping(address => bool) public isMember;

    // Trading fee percentage (in basis points)
    uint256 public tradingFee; // 100 basis points = 1%
    uint256 public constant MAX_TRADING_FEE = 500; // 5%

    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardsClaimed(address indexed user, uint256 reward);

    constructor() ERC20("Everlodge Token", "ELDG") {
        _mint(msg.sender, 1_000_000 * 10 ** decimals()); // Mint 1 million tokens to the owner
        tradingFee = 100; // Initial trading fee set to 1%
    }

    // Function to stake tokens for rewards
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        require(balanceOf(msg.sender) >= amount, "Insufficient balance");

        _stakingBalances[msg.sender] = _stakingBalances[msg.sender].add(amount);
        _transfer(msg.sender, address(this), amount); // Transfer tokens to the contract
        emit Staked(msg.sender, amount);
    }

    // Function to unstake tokens
    function unstake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        require(_stakingBalances[msg.sender] >= amount, "Insufficient staked balance");

        _stakingBalances[msg.sender] = _stakingBalances[msg.sender].sub(amount);
        _transfer(address(this), msg.sender, amount); // Transfer tokens back to the user
        emit Unstaked(msg.sender, amount);
    }

    // Function to claim staking rewards (for simplicity, rewards are a fixed percentage of staked amount)
    function claimRewards() external {
        uint256 stakedAmount = _stakingBalances[msg.sender];
        require(stakedAmount > 0, "No staked amount to claim rewards");

        // Calculate rewards (e.g., 10% of the staked amount)
        uint256 reward = stakedAmount.mul(10).div(100);
        totalStakingRewards = totalStakingRewards.add(reward);
        _mint(msg.sender, reward); // Mint rewards to the user
        emit RewardsClaimed(msg.sender, reward);
    }

    // Function to set trading fee (only callable by owner)
    function setTradingFee(uint256 fee) external onlyOwner {
        require(fee <= MAX_TRADING_FEE, "Trading fee exceeds maximum limit");
        tradingFee = fee;
    }

    // Function to enable membership benefits
    function enableMembership(address user) external onlyOwner {
        isMember[user] = true;
    }

    // Function to disable membership benefits
    function disableMembership(address user) external onlyOwner {
        isMember[user] = false;
    }

    // Override transfer function to implement trading fee
    function _transfer(address sender, address recipient, uint256 amount) internal virtual override {
        uint256 fee = amount.mul(tradingFee).div(10000); // Calculate fee based on the trading fee percentage
        uint256 amountAfterFee = amount.sub(fee);

        // Call the parent class transfer function
        super._transfer(sender, recipient, amountAfterFee);
        // Transfer the fee to the owner's address
        super._transfer(sender, owner(), fee);
    }
}
```
