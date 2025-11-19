"""
Generated Code Metadata:
========================
Original URL: https://greenbitcoin-ae.pages.dev
Prompt: "Design a simple smart contract in Solidity to automate the staking and reward distribution process for Green Bitcoin ($GBTC) on the Ethereum blockchain."
Generated: DETERMINISTIC_cead13d4a7fdefdf
Batch ID: 20250622_205218
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
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

contract GreenBitcoinStaking is Ownable, ReentrancyGuard {
    IERC20 public gbtcToken;
    
    struct Stake {
        uint256 amount;
        uint256 stakedAt;
    }

    // Annual Percentage Yield (APY) in basis points (1% = 100)
    uint256 public apy;
    uint256 public constant SECONDS_IN_YEAR = 365 days;
    
    mapping(address => Stake) public stakes;
    uint256 public totalStaked;

    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount, uint256 reward);
    event RewardClaimed(address indexed user, uint256 reward);
    event APYUpdated(uint256 newAPY);

    constructor(address _gbtcToken, uint256 _apy) {
        require(_gbtcToken != address(0), "Invalid token address");
        gbtcToken = IERC20(_gbtcToken);
        apy = _apy;
    }

    function stake(uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be greater than 0");
        require(gbtcToken.transferFrom(msg.sender, address(this), amount), "Transfer failed");

        if (stakes[msg.sender].amount > 0) {
            _claimReward();
        }

        stakes[msg.sender] = Stake({
            amount: stakes[msg.sender].amount + amount,
            stakedAt: block.timestamp
        });

        totalStaked += amount;
        emit Staked(msg.sender, amount);
    }

    function unstake(uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be greater than 0");
        Stake storage userStake = stakes[msg.sender];
        require(userStake.amount >= amount, "Insufficient staked amount");

        uint256 reward = calculateReward(msg.sender);
        userStake.amount -= amount;
        totalStaked -= amount;

        if (userStake.amount == 0) {
            userStake.stakedAt = 0;
        } else {
            userStake.stakedAt = block.timestamp;
        }

        require(gbtcToken.transfer(msg.sender, amount), "Transfer failed");
        emit Unstaked(msg.sender, amount, reward);
    }

    function claimReward() external nonReentrant {
        _claimReward();
    }

    function _claimReward() private {
        uint256 reward = calculateReward(msg.sender);
        require(reward > 0, "No reward to claim");

        Stake storage userStake = stakes[msg.sender];
        userStake.stakedAt = block.timestamp;

        require(gbtcToken.transfer(msg.sender, reward), "Reward transfer failed");
        emit RewardClaimed(msg.sender, reward);
    }

    function calculateReward(address user) public view returns (uint256) {
        Stake memory userStake = stakes[user];
        if (userStake.amount == 0) {
            return 0;
        }

        uint256 stakingDuration = block.timestamp - userStake.stakedAt;
        return (userStake.amount * apy * stakingDuration) / (SECONDS_IN_YEAR * 10000);
    }

    function updateAPY(uint256 newAPY) external onlyOwner {
        require(newAPY != apy, "APY already set to this value");
        apy = newAPY;
        emit APYUpdated(newAPY);
    }

    function emergencyWithdraw() external onlyOwner {
        uint256 balance = gbtcToken.balanceOf(address(this));
        require(balance > 0, "No tokens to withdraw");
        require(gbtcToken.transfer(owner(), balance), "Emergency withdrawal failed");
    }
}
```
