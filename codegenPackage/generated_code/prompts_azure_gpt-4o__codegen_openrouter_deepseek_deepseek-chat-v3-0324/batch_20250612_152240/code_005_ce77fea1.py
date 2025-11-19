"""
Generated Code Metadata:
========================
Original URL: https://bamboomeme.pages.dev
Prompt: Develop a smart contract for a tokenized casino experience that rewards players, inspired by the `$BAMBOO` token's connection to a casino in the crypto space.
Generated: DETERMINISTIC_ce77fea195199089
Batch ID: 20250612_152240
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

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

contract CasinoToken is ERC20, Ownable, ReentrancyGuard {
    uint256 public constant HOUSE_EDGE_PERCENT = 5; // 5% house edge
    uint256 public constant REWARD_RATE = 10; // 10% reward rate for staking
    uint256 public constant MIN_BET = 1 ether; // Minimum bet amount
    uint256 public constant MAX_BET = 1000 ether; // Maximum bet amount
    
    mapping(address => uint256) public lastClaimTime;
    mapping(address => uint256) public stakedBalance;
    mapping(address => uint256) public rewardBalance;
    
    event BetPlaced(address indexed player, uint256 amount, bool win, uint256 payout);
    event TokensStaked(address indexed staker, uint256 amount);
    event TokensUnstaked(address indexed staker, uint256 amount);
    event RewardsClaimed(address indexed claimer, uint256 amount);
    
    constructor() ERC20("Casino Token", "CST") {
        _mint(msg.sender, 1000000 * 10 ** decimals());
    }
    
    // Place a bet (1 = win, 2 = lose)
    function placeBet(uint256 betAmount, uint256 choice) external nonReentrant {
        require(betAmount >= MIN_BET && betAmount <= MAX_BET, "Bet amount out of range");
        require(choice == 1 || choice == 2, "Invalid choice");
        require(balanceOf(msg.sender) >= betAmount, "Insufficient balance");
        
        _burn(msg.sender, betAmount);
        
        uint256 randomNumber = uint256(keccak256(abi.encodePacked(block.timestamp, block.difficulty, msg.sender))) % 100;
        bool win = (choice == 1 && randomNumber < 50) || (choice == 2 && randomNumber >= 50);
        
        uint256 payout = 0;
        if (win) {
            payout = (betAmount * 2 * (100 - HOUSE_EDGE_PERCENT)) / 100;
            _mint(msg.sender, payout);
        }
        
        emit BetPlaced(msg.sender, betAmount, win, payout);
    }
    
    // Stake tokens to earn rewards
    function stake(uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be greater than 0");
        require(balanceOf(msg.sender) >= amount, "Insufficient balance");
        
        _transfer(msg.sender, address(this), amount);
        stakedBalance[msg.sender] += amount;
        lastClaimTime[msg.sender] = block.timestamp;
        
        emit TokensStaked(msg.sender, amount);
    }
    
    // Unstake tokens
    function unstake(uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be greater than 0");
        require(stakedBalance[msg.sender] >= amount, "Insufficient staked balance");
        
        _claimRewards();
        stakedBalance[msg.sender] -= amount;
        _transfer(address(this), msg.sender, amount);
        
        emit TokensUnstaked(msg.sender, amount);
    }
    
    // Claim rewards
    function claimRewards() external nonReentrant {
        _claimRewards();
    }
    
    // Internal function to calculate and claim rewards
    function _claimRewards() private {
        uint256 rewards = calculateRewards(msg.sender);
        if (rewards > 0) {
            rewardBalance[msg.sender] = 0;
            lastClaimTime[msg.sender] = block.timestamp;
            _mint(msg.sender, rewards);
            emit RewardsClaimed(msg.sender, rewards);
        }
    }
    
    // Calculate pending rewards
    function calculateRewards(address staker) public view returns (uint256) {
        if (stakedBalance[staker] == 0) return 0;
        
        uint256 timeElapsed = block.timestamp - lastClaimTime[staker];
        uint256 rewards = (stakedBalance[staker] * REWARD_RATE * timeElapsed) / (365 days * 100);
        return rewards + rewardBalance[staker];
    }
    
    // Mint new tokens (owner only)
    function mint(address to, uint256 amount) external onlyOwner {
        _mint(to, amount);
    }
    
    // Burn tokens (owner only)
    function burn(address from, uint256 amount) external onlyOwner {
        _burn(from, amount);
    }
}
```
