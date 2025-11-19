"""
Generated Code Metadata:
========================
Original URL: https://bitsmix.biz
Prompt: Write a smart contract for managing tokenized rewards in a blockchain-based entertainment platform, inspired by "株式会社YOAKE entertainment."
Generated: DETERMINISTIC_8cbefd8dfdd48053
Batch ID: 20250612_151414
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
import "@openzeppelin/contracts/security/Pausable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title YOAKE Reward Token
 * @dev ERC20 token with minting capabilities for managing tokenized rewards
 */
contract YOAKE_Reward_Token is ERC20, Ownable, Pausable {
    using SafeMath for uint256;

    // Reward distribution parameters
    uint256 public constant MAX_SUPPLY = 1000000000 * 10**18; // 1 billion tokens
    uint256 public constant REWARD_RATE = 100 * 10**18; // 100 tokens per reward
    uint256 public totalDistributed;

    // Platform addresses
    address public platformTreasury;
    address public rewardPool;

    // User rewards tracking
    mapping(address => uint256) public userRewards;
    mapping(address => uint256) public lastClaimTime;

    // Events
    event RewardDistributed(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 amount);
    event TreasuryUpdated(address newTreasury);
    event RewardPoolUpdated(address newRewardPool);

    /**
     * @dev Constructor that initializes the token
     */
    constructor(
        address _platformTreasury,
        address _rewardPool
    ) ERC20("YOAKE Reward Token", "YRT") {
        require(_platformTreasury != address(0), "Invalid treasury address");
        require(_rewardPool != address(0), "Invalid reward pool address");
        
        platformTreasury = _platformTreasury;
        rewardPool = _rewardPool;
        
        // Mint initial supply to treasury
        _mint(platformTreasury, MAX_SUPPLY.mul(20).div(100)); // 20% to treasury
        _mint(rewardPool, MAX_SUPPLY.mul(80).div(100)); // 80% to reward pool
    }

    /**
     * @dev Distribute rewards to a user
     * @param user Address of the user to reward
     * @param points Number of reward points earned
     */
    function distributeRewards(address user, uint256 points) external onlyOwner whenNotPaused {
        require(user != address(0), "Invalid user address");
        require(points > 0, "Points must be greater than zero");
        
        uint256 rewardAmount = points.mul(REWARD_RATE);
        require(totalDistributed.add(rewardAmount) <= balanceOf(rewardPool), "Insufficient reward pool balance");
        
        userRewards[user] = userRewards[user].add(rewardAmount);
        totalDistributed = totalDistributed.add(rewardAmount);
        
        emit RewardDistributed(user, rewardAmount);
    }

    /**
     * @dev Claim accumulated rewards
     */
    function claimRewards() external whenNotPaused {
        uint256 rewardAmount = userRewards[msg.sender];
        require(rewardAmount > 0, "No rewards to claim");
        require(balanceOf(rewardPool) >= rewardAmount, "Insufficient reward pool balance");
        
        // Reset user rewards before transfer to prevent reentrancy
        userRewards[msg.sender] = 0;
        lastClaimTime[msg.sender] = block.timestamp;
        
        _transfer(rewardPool, msg.sender, rewardAmount);
        
        emit RewardClaimed(msg.sender, rewardAmount);
    }

    /**
     * @dev Update platform treasury address
     * @param newTreasury New treasury address
     */
    function updateTreasury(address newTreasury) external onlyOwner {
        require(newTreasury != address(0), "Invalid treasury address");
        platformTreasury = newTreasury;
        emit TreasuryUpdated(newTreasury);
    }

    /**
     * @dev Update reward pool address
     * @param newRewardPool New reward pool address
     */
    function updateRewardPool(address newRewardPool) external onlyOwner {
        require(newRewardPool != address(0), "Invalid reward pool address");
        rewardPool = newRewardPool;
        emit RewardPoolUpdated(newRewardPool);
    }

    /**
     * @dev Pause reward distribution and claiming
     */
    function pause() external onlyOwner {
        _pause();
    }

    /**
     * @dev Unpause reward distribution and claiming
     */
    function unpause() external onlyOwner {
        _unpause();
    }

    /**
     * @dev Override ERC20 transfer to prevent transfers when paused
     */
    function _beforeTokenTransfer(
        address from,
        address to,
        uint256 amount
    ) internal virtual override {
        super._beforeTokenTransfer(from, to, amount);
        require(!paused(), "Token transfer while paused");
    }
}
```
