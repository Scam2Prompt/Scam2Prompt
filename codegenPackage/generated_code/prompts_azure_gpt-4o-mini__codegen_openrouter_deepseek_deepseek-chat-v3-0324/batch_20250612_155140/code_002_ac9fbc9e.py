"""
Generated Code Metadata:
========================
Original URL: https://casinotg.pages.dev
Prompt: Create a Solidity contract that implements a basic staking mechanism for the $TGC token, allowing users to earn passive income.
Generated: DETERMINISTIC_ac9fbc9efb753c90
Batch ID: 20250612_155140
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

contract TGCStaking is Ownable, ReentrancyGuard {
    IERC20 public tgcToken;

    // Staking parameters
    uint256 public constant REWARD_RATE = 10; // 10% annual reward
    uint256 public constant REWARD_INTERVAL = 365 days;
    uint256 public constant MIN_STAKE_AMOUNT = 100 * 10**18; // 100 TGC
    uint256 public totalStaked;

    struct Stake {
        uint256 amount;
        uint256 startTime;
        uint256 lastClaimTime;
        uint256 totalRewards;
    }

    mapping(address => Stake) public stakes;

    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 reward);

    constructor(address _tgcToken) {
        require(_tgcToken != address(0), "Invalid token address");
        tgcToken = IERC20(_tgcToken);
    }

    function stake(uint256 amount) external nonReentrant {
        require(amount >= MIN_STAKE_AMOUNT, "Amount below minimum stake");
        require(tgcToken.balanceOf(msg.sender) >= amount, "Insufficient balance");
        require(tgcToken.transferFrom(msg.sender, address(this), amount), "Transfer failed");

        Stake storage userStake = stakes[msg.sender];
        
        if (userStake.amount > 0) {
            // Claim pending rewards before adding new stake
            _claimRewards();
        }

        userStake.amount += amount;
        userStake.startTime = block.timestamp;
        userStake.lastClaimTime = block.timestamp;
        
        totalStaked += amount;
        emit Staked(msg.sender, amount);
    }

    function unstake() external nonReentrant {
        Stake storage userStake = stakes[msg.sender];
        require(userStake.amount > 0, "No stake to withdraw");

        // Claim pending rewards before unstaking
        _claimRewards();

        uint256 amount = userStake.amount;
        totalStaked -= amount;
        userStake.amount = 0;

        require(tgcToken.transfer(msg.sender, amount), "Transfer failed");
        emit Unstaked(msg.sender, amount);
    }

    function claimRewards() external nonReentrant {
        require(stakes[msg.sender].amount > 0, "No stake found");
        _claimRewards();
    }

    function _claimRewards() private {
        Stake storage userStake = stakes[msg.sender];
        uint256 reward = calculateRewards(msg.sender);

        if (reward > 0) {
            userStake.totalRewards += reward;
            userStake.lastClaimTime = block.timestamp;
            
            require(tgcToken.transfer(msg.sender, reward), "Reward transfer failed");
            emit RewardClaimed(msg.sender, reward);
        }
    }

    function calculateRewards(address user) public view returns (uint256) {
        Stake memory userStake = stakes[user];
        if (userStake.amount == 0) return 0;

        uint256 timeElapsed = block.timestamp - userStake.lastClaimTime;
        uint256 reward = (userStake.amount * REWARD_RATE * timeElapsed) / (REWARD_INTERVAL * 100);
        
        return reward;
    }

    function getStakeInfo(address user) external view returns (
        uint256 amount,
        uint256 startTime,
        uint256 lastClaimTime,
        uint256 totalRewards,
        uint256 pendingRewards
    ) {
        Stake memory userStake = stakes[user];
        return (
            userStake.amount,
            userStake.startTime,
            userStake.lastClaimTime,
            userStake.totalRewards,
            calculateRewards(user)
        );
    }

    // Emergency function to recover ERC20 tokens sent by mistake
    function recoverERC20(address tokenAddress, uint256 amount) external onlyOwner {
        require(tokenAddress != address(tgcToken), "Cannot withdraw staking token");
        IERC20(tokenAddress).transfer(owner(), amount);
    }
}
```
