"""
Generated Code Metadata:
========================
Original URL: https://rand-samp-934.pages.dev
Prompt: Design a simple staking system using Solidity and OpenZeppelin's contracts for BURYing SHIB tokens on the ShibaSwap platform, including functions for depositing and withdrawing tokens.
Generated: DETERMINISTIC_927705fed891bfdc
Batch ID: 20250622_204657
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

contract SHIBStaking is Ownable, ReentrancyGuard {
    using SafeERC20 for IERC20;

    // SHIB token contract
    IERC20 public immutable shibToken;

    // Struct to store user staking details
    struct Staker {
        uint256 amount;
        uint256 rewardDebt;
    }

    // Mapping of stakers
    mapping(address => Staker) public stakers;

    // Total staked SHIB tokens
    uint256 public totalStaked;

    // Reward rate (reward tokens per block per staked token)
    uint256 public rewardRate;

    // Last update block number
    uint256 public lastUpdateBlock;

    // Accumulated rewards per share
    uint256 public accRewardPerShare;

    // Events
    event Deposited(address indexed user, uint256 amount);
    event Withdrawn(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 amount);
    event RewardRateUpdated(uint256 newRate);

    constructor(address _shibToken) {
        require(_shibToken != address(0), "SHIB token address cannot be zero");
        shibToken = IERC20(_shibToken);
    }

    /**
     * @dev Update reward variables
     */
    function updateReward() internal {
        if (totalStaked == 0) {
            lastUpdateBlock = block.number;
            return;
        }

        uint256 blocksPassed = block.number - lastUpdateBlock;
        if (blocksPassed > 0) {
            uint256 reward = blocksPassed * rewardRate;
            accRewardPerShare += (reward * 1e12) / totalStaked;
            lastUpdateBlock = block.number;
        }
    }

    /**
     * @dev Deposit SHIB tokens to stake
     * @param amount Amount of SHIB tokens to stake
     */
    function deposit(uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be greater than zero");

        updateReward();

        Staker storage staker = stakers[msg.sender];

        if (staker.amount > 0) {
            uint256 pending = (staker.amount * accRewardPerShare) / 1e12 - staker.rewardDebt;
            if (pending > 0) {
                // Transfer pending rewards to user
                shibToken.safeTransfer(msg.sender, pending);
                emit RewardClaimed(msg.sender, pending);
            }
        }

        shibToken.safeTransferFrom(msg.sender, address(this), amount);
        staker.amount += amount;
        staker.rewardDebt = (staker.amount * accRewardPerShare) / 1e12;
        totalStaked += amount;

        emit Deposited(msg.sender, amount);
    }

    /**
     * @dev Withdraw staked SHIB tokens
     * @param amount Amount of SHIB tokens to withdraw
     */
    function withdraw(uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be greater than zero");
        Staker storage staker = stakers[msg.sender];
        require(staker.amount >= amount, "Insufficient staked balance");

        updateReward();

        uint256 pending = (staker.amount * accRewardPerShare) / 1e12 - staker.rewardDebt;
        if (pending > 0) {
            // Transfer pending rewards to user
            shibToken.safeTransfer(msg.sender, pending);
            emit RewardClaimed(msg.sender, pending);
        }

        staker.amount -= amount;
        staker.rewardDebt = (staker.amount * accRewardPerShare) / 1e12;
        totalStaked -= amount;

        shibToken.safeTransfer(msg.sender, amount);
        emit Withdrawn(msg.sender, amount);
    }

    /**
     * @dev Claim pending rewards
     */
    function claimReward() external nonReentrant {
        Staker storage staker = stakers[msg.sender];
        require(staker.amount > 0, "No staked tokens");

        updateReward();

        uint256 pending = (staker.amount * accRewardPerShare) / 1e12 - staker.rewardDebt;
        require(pending > 0, "No rewards to claim");

        staker.rewardDebt = (staker.amount * accRewardPerShare) / 1e12;
        shibToken.safeTransfer(msg.sender, pending);
        emit RewardClaimed(msg.sender, pending);
    }

    /**
     * @dev Set the reward rate
     * @param _rewardRate New reward rate (reward tokens per block per staked token)
     */
    function setRewardRate(uint256 _rewardRate) external onlyOwner {
        updateReward();
        rewardRate = _rewardRate;
        emit RewardRateUpdated(_rewardRate);
    }

    /**
     * @dev View function to see pending rewards
     * @param _user Address of the user
     * @return Pending rewards for user
     */
    function pendingReward(address _user) external view returns (uint256) {
        Staker storage staker = stakers[_user];
        uint256 currentAccRewardPerShare = accRewardPerShare;
        
        if (block.number > lastUpdateBlock && totalStaked != 0) {
            uint256 blocksPassed = block.number - lastUpdateBlock;
            uint256 reward = blocksPassed * rewardRate;
            currentAccRewardPerShare += (reward * 1e12) / totalStaked;
        }
        
        return (staker.amount * currentAccRewardPerShare) / 1e12 - staker.rewardDebt;
    }

    /**
     * @dev Emergency function to recover ERC20 tokens sent by mistake
     * @param tokenAddress Address of the token contract
     * @param tokenAmount Amount of tokens to recover
     */
    function recoverERC20(address tokenAddress, uint256 tokenAmount) external onlyOwner {
        require(tokenAddress != address(shibToken), "Cannot withdraw staking token");
        IERC20(tokenAddress).safeTransfer(owner(), tokenAmount);
    }
}
```
