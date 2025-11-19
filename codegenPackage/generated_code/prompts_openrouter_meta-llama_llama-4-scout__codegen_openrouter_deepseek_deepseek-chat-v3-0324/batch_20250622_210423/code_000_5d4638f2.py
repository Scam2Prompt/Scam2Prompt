"""
Generated Code Metadata:
========================
Original URL: https://rabbittherious.pages.dev
Prompt: Write a smart contract in Solidity for a token named Rious The Rabbit that combines staking and gaming features.
Generated: DETERMINISTIC_5d4638f2744e78a9
Batch ID: 20250622_210423
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

contract RiousTheRabbit is ERC20, Ownable, ReentrancyGuard {
    uint256 public constant INITIAL_SUPPLY = 1_000_000 * 10**18;
    uint256 public constant STAKING_REWARD_RATE = 10; // 10% annual reward
    uint256 public constant MIN_STAKE_AMOUNT = 100 * 10**18;
    uint256 public constant GAME_ENTRY_FEE = 50 * 10**18;
    uint256 public constant GAME_WIN_REWARD = 100 * 10**18;
    
    struct Stake {
        uint256 amount;
        uint256 startTime;
    }

    mapping(address => Stake) public stakes;
    mapping(address => uint256) public lastClaimTime;
    mapping(address => uint256) public gameWins;

    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 amount);
    event GamePlayed(address indexed player, bool won);

    constructor() ERC20("Rious The Rabbit", "RIOUS") {
        _mint(msg.sender, INITIAL_SUPPLY);
    }

    function stake(uint256 amount) external nonReentrant {
        require(amount >= MIN_STAKE_AMOUNT, "Amount below minimum stake");
        require(balanceOf(msg.sender) >= amount, "Insufficient balance");
        
        if (stakes[msg.sender].amount > 0) {
            claimReward();
        }

        _transfer(msg.sender, address(this), amount);
        stakes[msg.sender] = Stake({
            amount: stakes[msg.sender].amount + amount,
            startTime: block.timestamp
        });
        
        lastClaimTime[msg.sender] = block.timestamp;
        emit Staked(msg.sender, amount);
    }

    function unstake(uint256 amount) external nonReentrant {
        require(stakes[msg.sender].amount >= amount, "Insufficient staked amount");
        
        claimReward();
        
        stakes[msg.sender].amount -= amount;
        _transfer(address(this), msg.sender, amount);
        
        emit Unstaked(msg.sender, amount);
    }

    function claimReward() public nonReentrant {
        require(stakes[msg.sender].amount > 0, "No staked amount");
        
        uint256 reward = calculateReward(msg.sender);
        if (reward > 0) {
            _mint(msg.sender, reward);
            lastClaimTime[msg.sender] = block.timestamp;
            emit RewardClaimed(msg.sender, reward);
        }
    }

    function calculateReward(address user) public view returns (uint256) {
        if (stakes[user].amount == 0) return 0;
        
        uint256 stakedTime = block.timestamp - lastClaimTime[user];
        uint256 reward = (stakes[user].amount * STAKING_REWARD_RATE * stakedTime) / 
                        (100 * 365 days);
        
        return reward;
    }

    function playGame() external nonReentrant {
        require(balanceOf(msg.sender) >= GAME_ENTRY_FEE, "Insufficient balance for game fee");
        require(stakes[msg.sender].amount > 0, "Must be staking to play");
        
        _transfer(msg.sender, address(this), GAME_ENTRY_FEE);
        
        // Simulate random game outcome (50% chance to win)
        bool won = (uint256(keccak256(abi.encodePacked(block.timestamp, msg.sender))) % 2) == 0;
        
        if (won) {
            _mint(msg.sender, GAME_WIN_REWARD);
            gameWins[msg.sender]++;
        }
        
        emit GamePlayed(msg.sender, won);
    }

    function getStakedAmount(address user) external view returns (uint256) {
        return stakes[user].amount;
    }

    function getPendingReward(address user) external view returns (uint256) {
        return calculateReward(user);
    }

    function getGameWins(address user) external view returns (uint256) {
        return gameWins[user];
    }
}
```
