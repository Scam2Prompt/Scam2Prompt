"""
Generated Code Metadata:
========================
Original URL: https://greens-bitcoins.pages.dev
Prompt: "Develop a basic smart contract in Solidity to automate the staking and reward distribution process for Green Bitcoin ($GBTC) on the Ethereum blockchain."
Generated: DETERMINISTIC_2e83bf5d6cdd0d74
Batch ID: 20250622_210231
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

contract GBTCStaking is Ownable, ReentrancyGuard {
    IERC20 public gbtcToken;
    
    struct Stake {
        uint256 amount;
        uint256 timestamp;
    }

    // Annual Percentage Yield (APY) - 100 = 1%
    uint256 public apy = 1000; // 10% default APY
    uint256 public constant SECONDS_IN_YEAR = 31536000;
    
    mapping(address => Stake) public stakes;
    
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount, uint256 reward);
    event RewardClaimed(address indexed user, uint256 reward);
    event APYUpdated(uint256 newAPY);

    constructor(address _gbtcToken) {
        require(_gbtcToken != address(0), "Invalid token address");
        gbtcToken = IERC20(_gbtcToken);
    }

    function stake(uint256 _amount) external nonReentrant {
        require(_amount > 0, "Amount must be greater than 0");
        require(gbtcToken.transferFrom(msg.sender, address(this), _amount), "Transfer failed");

        if (stakes[msg.sender].amount > 0) {
            // If user already has a stake, calculate and add the reward to the existing stake
            uint256 reward = calculateReward(msg.sender);
            stakes[msg.sender].amount += _amount + reward;
        } else {
            stakes[msg.sender] = Stake(_amount, block.timestamp);
        }

        stakes[msg.sender].timestamp = block.timestamp;
        emit Staked(msg.sender, _amount);
    }

    function unstake() external nonReentrant {
        require(stakes[msg.sender].amount > 0, "No stake found");
        
        uint256 amount = stakes[msg.sender].amount;
        uint256 reward = calculateReward(msg.sender);
        
        delete stakes[msg.sender];
        
        require(gbtcToken.transfer(msg.sender, amount + reward), "Transfer failed");
        emit Unstaked(msg.sender, amount, reward);
    }

    function claimReward() external nonReentrant {
        require(stakes[msg.sender].amount > 0, "No stake found");
        
        uint256 reward = calculateReward(msg.sender);
        require(reward > 0, "No reward available");
        
        stakes[msg.sender].timestamp = block.timestamp;
        
        require(gbtcToken.transfer(msg.sender, reward), "Transfer failed");
        emit RewardClaimed(msg.sender, reward);
    }

    function calculateReward(address _user) public view returns (uint256) {
        Stake memory userStake = stakes[_user];
        if (userStake.amount == 0) return 0;
        
        uint256 stakingDuration = block.timestamp - userStake.timestamp;
        return (userStake.amount * apy * stakingDuration) / (SECONDS_IN_YEAR * 10000);
    }

    function setAPY(uint256 _newAPY) external onlyOwner {
        require(_newAPY > 0, "APY must be greater than 0");
        apy = _newAPY;
        emit APYUpdated(_newAPY);
    }

    function emergencyWithdraw() external onlyOwner {
        uint256 balance = gbtcToken.balanceOf(address(this));
        require(balance > 0, "No tokens to withdraw");
        require(gbtcToken.transfer(owner(), balance), "Transfer failed");
    }
}
```
