"""
Generated Code Metadata:
========================
Original URL: https://inqubeta-presales.pages.dev
Prompt: Write a smart contract in Solidity for staking $QUBE tokens that distributes rewards based on a 5% sell tax, as described in InQubeta's tokenomics.
Generated: DETERMINISTIC_9f5f007a1b81c787
Batch ID: 20250612_153420
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
import "@openzeppelin/contracts/token/ERC20/utils/SafeERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

contract QubeStaking is Ownable, ReentrancyGuard {
    using SafeERC20 for IERC20;

    // Struct to store user staking information
    struct Staker {
        uint256 amount;         // Amount of tokens staked
        uint256 rewardDebt;     // Reward debt for accounting
        uint256 lastClaimTime;  // Last time rewards were claimed
    }

    // The QUBE token contract
    IERC20 public immutable qubeToken;
    
    // Total amount of QUBE tokens staked
    uint256 public totalStaked;
    
    // Accumulated rewards per share
    uint256 public accRewardPerShare;
    
    // Last time rewards were distributed
    uint256 public lastRewardTime;
    
    // Reward distribution rate (5% of sell tax)
    uint256 public constant REWARD_RATE = 5;
    
    // Precision factor for reward calculations
    uint256 private constant PRECISION = 1e18;
    
    // Mapping of user addresses to their staking info
    mapping(address => Staker) public stakers;
    
    // Events
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 amount);
    event RewardDistributed(uint256 amount);

    constructor(address _qubeToken) {
        require(_qubeToken != address(0), "Invalid token address");
        qubeToken = IERC20(_qubeToken);
        lastRewardTime = block.timestamp;
    }

    /**
     * @dev Stake QUBE tokens to earn rewards
     * @param amount Amount of tokens to stake
     */
    function stake(uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be greater than 0");
        
        _updateRewards();
        
        Staker storage staker = stakers[msg.sender];
        
        if (staker.amount > 0) {
            uint256 pending = (staker.amount * accRewardPerShare) / PRECISION - staker.rewardDebt;
            if (pending > 0) {
                _safeTransferRewards(msg.sender, pending);
            }
        }
        
        qubeToken.safeTransferFrom(msg.sender, address(this), amount);
        
        staker.amount += amount;
        staker.rewardDebt = (staker.amount * accRewardPerShare) / PRECISION;
        staker.lastClaimTime = block.timestamp;
        totalStaked += amount;
        
        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Unstake QUBE tokens
     * @param amount Amount of tokens to unstake
     */
    function unstake(uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be greater than 0");
        
        Staker storage staker = stakers[msg.sender];
        require(staker.amount >= amount, "Insufficient staked amount");
        
        _updateRewards();
        
        uint256 pending = (staker.amount * accRewardPerShare) / PRECISION - staker.rewardDebt;
        if (pending > 0) {
            _safeTransferRewards(msg.sender, pending);
        }
        
        staker.amount -= amount;
        staker.rewardDebt = (staker.amount * accRewardPerShare) / PRECISION;
        staker.lastClaimTime = block.timestamp;
        totalStaked -= amount;
        
        qubeToken.safeTransfer(msg.sender, amount);
        
        emit Unstaked(msg.sender, amount);
    }

    /**
     * @dev Claim accumulated rewards
     */
    function claimRewards() external nonReentrant {
        _updateRewards();
        
        Staker storage staker = stakers[msg.sender];
        require(staker.amount > 0, "No staked tokens");
        
        uint256 pending = (staker.amount * accRewardPerShare) / PRECISION - staker.rewardDebt;
        require(pending > 0, "No rewards to claim");
        
        staker.rewardDebt = (staker.amount * accRewardPerShare) / PRECISION;
        staker.lastClaimTime = block.timestamp;
        
        _safeTransferRewards(msg.sender, pending);
        
        emit RewardClaimed(msg.sender, pending);
    }

    /**
     * @dev Distribute rewards from sell tax (called by owner)
     * @param amount Amount of rewards to distribute
     */
    function distributeRewards(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than 0");
        
        _updateRewards();
        
        qubeToken.safeTransferFrom(msg.sender, address(this), amount);
        
        if (totalStaked > 0) {
            accRewardPerShare += (amount * PRECISION) / totalStaked;
        }
        
        emit RewardDistributed(amount);
    }

    /**
     * @dev Update reward calculations
     */
    function _updateRewards() private {
        if (block.timestamp <= lastRewardTime) {
            return;
        }
        
        lastRewardTime = block.timestamp;
    }

    /**
     * @dev Safely transfer rewards to user
     * @param to Address to receive rewards
     * @param amount Amount of rewards to transfer
     */
    function _safeTransferRewards(address to, uint256 amount) private {
        uint256 balance = qubeToken.balanceOf(address(this));
        if (amount > balance) {
            amount = balance;
        }
        
        if (amount > 0) {
            qubeToken.safeTransfer(to, amount);
        }
    }

    /**
     * @dev View function to check pending rewards for a user
     * @param user Address of the user
     * @return Pending rewards for the user
     */
    function pendingRewards(address user) external view returns (uint256) {
        Staker storage staker = stakers[user];
        uint256 tempAccRewardPerShare = accRewardPerShare;
        
        if (block.timestamp > lastRewardTime && totalStaked > 0) {
            // No automatic reward accumulation in this implementation
            // Rewards are only distributed via distributeRewards()
        }
        
        return (staker.amount * tempAccRewardPerShare) / PRECISION - staker.rewardDebt;
    }

    /**
     * @dev Emergency function to recover ERC20 tokens sent by mistake
     * @param tokenAddress Address of the token contract
     * @param amount Amount to recover
     */
    function recoverERC20(address tokenAddress, uint256 amount) external onlyOwner {
        require(tokenAddress != address(qubeToken), "Cannot withdraw staking token");
        IERC20(tokenAddress).safeTransfer(owner(), amount);
    }
}
```
