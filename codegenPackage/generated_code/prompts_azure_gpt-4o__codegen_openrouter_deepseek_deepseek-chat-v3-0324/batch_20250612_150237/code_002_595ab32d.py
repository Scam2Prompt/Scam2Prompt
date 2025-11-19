"""
Generated Code Metadata:
========================
Original URL: https://proposal-b3.com
Prompt: Generate a smart contract for staking $B3 tokens within the hyper-operable gaming ecosystem described on the B3 platform.
Generated: DETERMINISTIC_595ab32dcc0c6be5
Batch ID: 20250612_150237
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
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title B3TokenStaking
 * @dev A smart contract for staking B3 tokens with reward distribution
 */
contract B3TokenStaking is ReentrancyGuard, Ownable {
    IERC20 public b3Token;

    // Struct to store user stake information
    struct Stake {
        uint256 amount;
        uint256 rewardDebt;
        uint256 lastStakeTime;
    }

    // Staking parameters
    uint256 public constant REWARD_RATE = 10; // 10% annual reward
    uint256 public constant REWARD_INTERVAL = 365 days;
    uint256 public totalStaked;
    uint256 public lastRewardUpdate;
    uint256 public accRewardPerShare;

    // Mapping from user address to their stake
    mapping(address => Stake) public stakes;

    // Events
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 amount);
    event EmergencyWithdraw(address indexed user, uint256 amount);

    /**
     * @dev Constructor
     * @param _b3Token Address of the B3 token contract
     */
    constructor(address _b3Token) {
        require(_b3Token != address(0), "Invalid token address");
        b3Token = IERC20(_b3Token);
        lastRewardUpdate = block.timestamp;
    }

    /**
     * @dev Update the reward variables
     */
    function updateReward() internal {
        if (totalStaked == 0) {
            lastRewardUpdate = block.timestamp;
            return;
        }

        uint256 timePassed = block.timestamp - lastRewardUpdate;
        if (timePassed > 0) {
            uint256 reward = (totalStaked * REWARD_RATE * timePassed) / (REWARD_INTERVAL * 100);
            accRewardPerShare += (reward * 1e12) / totalStaked;
            lastRewardUpdate = block.timestamp;
        }
    }

    /**
     * @dev Stake B3 tokens
     * @param amount Amount of tokens to stake
     */
    function stake(uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be greater than 0");
        updateReward();

        Stake storage userStake = stakes[msg.sender];
        if (userStake.amount > 0) {
            uint256 pending = (userStake.amount * accRewardPerShare) / 1e12 - userStake.rewardDebt;
            if (pending > 0) {
                safeTransferReward(msg.sender, pending);
            }
        }

        require(b3Token.transferFrom(msg.sender, address(this), amount), "Transfer failed");
        userStake.amount += amount;
        userStake.rewardDebt = (userStake.amount * accRewardPerShare) / 1e12;
        userStake.lastStakeTime = block.timestamp;
        totalStaked += amount;

        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Unstake B3 tokens and claim rewards
     * @param amount Amount of tokens to unstake
     */
    function unstake(uint256 amount) external nonReentrant {
        Stake storage userStake = stakes[msg.sender];
        require(userStake.amount >= amount, "Insufficient staked amount");
        require(block.timestamp >= userStake.lastStakeTime + 7 days, "Tokens are locked for 7 days");

        updateReward();
        uint256 pending = (userStake.amount * accRewardPerShare) / 1e12 - userStake.rewardDebt;
        
        if (pending > 0) {
            safeTransferReward(msg.sender, pending);
        }

        userStake.amount -= amount;
        userStake.rewardDebt = (userStake.amount * accRewardPerShare) / 1e12;
        totalStaked -= amount;

        require(b3Token.transfer(msg.sender, amount), "Transfer failed");
        emit Unstaked(msg.sender, amount);
    }

    /**
     * @dev Claim accumulated rewards
     */
    function claimReward() external nonReentrant {
        Stake storage userStake = stakes[msg.sender];
        updateReward();

        uint256 pending = (userStake.amount * accRewardPerShare) / 1e12 - userStake.rewardDebt;
        require(pending > 0, "No rewards to claim");

        userStake.rewardDebt = (userStake.amount * accRewardPerShare) / 1e12;
        safeTransferReward(msg.sender, pending);

        emit RewardClaimed(msg.sender, pending);
    }

    /**
     * @dev Emergency withdraw without claiming rewards
     */
    function emergencyWithdraw() external nonReentrant {
        Stake storage userStake = stakes[msg.sender];
        uint256 amount = userStake.amount;
        require(amount > 0, "No staked amount");

        totalStaked -= amount;
        userStake.amount = 0;
        userStake.rewardDebt = 0;

        require(b3Token.transfer(msg.sender, amount), "Transfer failed");
        emit EmergencyWithdraw(msg.sender, amount);
    }

    /**
     * @dev Safe transfer reward tokens
     * @param to Recipient address
     * @param amount Amount to transfer
     */
    function safeTransferReward(address to, uint256 amount) internal {
        uint256 balance = b3Token.balanceOf(address(this));
        if (amount > balance) {
            b3Token.transfer(to, balance);
        } else {
            b3Token.transfer(to, amount);
        }
    }

    /**
     * @dev View function to check pending rewards
     * @param user User address
     * @return Pending rewards for the user
     */
    function pendingReward(address user) external view returns (uint256) {
        Stake storage userStake = stakes[user];
        uint256 currentAccRewardPerShare = accRewardPerShare;
        
        if (block.timestamp > lastRewardUpdate && totalStaked != 0) {
            uint256 timePassed = block.timestamp - lastRewardUpdate;
            uint256 reward = (totalStaked * REWARD_RATE * timePassed) / (REWARD_INTERVAL * 100);
            currentAccRewardPerShare += (reward * 1e12) / totalStaked;
        }
        
        return (userStake.amount * currentAccRewardPerShare) / 1e12 - userStake.rewardDebt;
    }

    /**
     * @dev Recover any ERC20 tokens sent to the contract by mistake
     * @param tokenAddress Address of the token to recover
     * @param amount Amount to recover
     */
    function recoverERC20(address tokenAddress, uint256 amount) external onlyOwner {
        require(tokenAddress != address(b3Token), "Cannot withdraw staking token");
        IERC20(tokenAddress).transfer(owner(), amount);
    }
}
```
