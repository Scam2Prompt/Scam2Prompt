"""
Generated Code Metadata:
========================
Original URL: https://scottyweb.pages.dev
Prompt: Generate a smart contract code in Solidity that handles the distribution of $SCOTTY token rewards to users based on their staking balance and the number of ETH blocks.
Generated: DETERMINISTIC_734c45538dc60d91
Batch ID: 20250622_210216
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
import "@openzeppelin/contracts/token/ERC20/extensions/ERC20Burnable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title ScottyTokenRewardContract
 * @author [Your Name]
 * @notice A smart contract for distributing $SCOTTY token rewards to users based on their staking balance and the number of ETH blocks.
 */
contract ScottyTokenRewardContract is ReentrancyGuard {
    using SafeMath for uint256;

    // Mapping of user staking balances
    mapping (address => uint256) public stakingBalances;

    // Mapping of user reward debt
    mapping (address => uint256) public rewardDebt;

    // The $SCOTTY token contract
    ERC20 public scottyToken;

    // Reward per block
    uint256 public rewardPerBlock;

    // Last block number that reward was distributed
    uint256 public lastRewardBlock;

    // Total staking balance
    uint256 public totalStakingBalance;

    // Event emitted when a user stakes tokens
    event Staked(address indexed user, uint256 amount);

    // Event emitted when a user unstakes tokens
    event Unstaked(address indexed user, uint256 amount);

    // Event emitted when rewards are distributed
    event RewardsDistributed(address indexed user, uint256 amount);

    /**
     * @notice Constructor
     * @param _scottyTokenAddress The address of the $SCOTTY token contract
     * @param _rewardPerBlock The reward per block
     */
    constructor(address _scottyTokenAddress, uint256 _rewardPerBlock) public {
        require(_scottyTokenAddress != address(0), "ScottyTokenRewardContract: Invalid token address");
        scottyToken = ERC20(_scottyTokenAddress);
        rewardPerBlock = _rewardPerBlock;
        lastRewardBlock = block.number;
    }

    /**
     * @notice Stake tokens
     * @param _amount The amount of tokens to stake
     */
    function stake(uint256 _amount) external nonReentrant {
        require(_amount > 0, "ScottyTokenRewardContract: Invalid stake amount");
        require(scottyToken.transferFrom(msg.sender, address(this), _amount), "ScottyTokenRewardContract: Failed to transfer tokens");

        // Update user's staking balance
        stakingBalances[msg.sender] = stakingBalances[msg.sender].add(_amount);
        totalStakingBalance = totalStakingBalance.add(_amount);

        emit Staked(msg.sender, _amount);
    }

    /**
     * @notice Unstake tokens
     * @param _amount The amount of tokens to unstake
     */
    function unstake(uint256 _amount) external nonReentrant {
        require(_amount > 0, "ScottyTokenRewardContract: Invalid unstake amount");
        require(stakingBalances[msg.sender] >= _amount, "ScottyTokenRewardContract: Insufficient staking balance");

        // Update user's staking balance
        stakingBalances[msg.sender] = stakingBalances[msg.sender].sub(_amount);
        totalStakingBalance = totalStakingBalance.sub(_amount);

        // Transfer tokens back to user
        require(scottyToken.transfer(msg.sender, _amount), "ScottyTokenRewardContract: Failed to transfer tokens");

        emit Unstaked(msg.sender, _amount);
    }

    /**
     * @notice Update reward per block
     * @param _newRewardPerBlock The new reward per block
     */
    function updateRewardPerBlock(uint256 _newRewardPerBlock) external {
        require(msg.sender == owner(), "ScottyTokenRewardContract: Only owner can update reward per block");
        rewardPerBlock = _newRewardPerBlock;
    }

    /**
     * @notice Get user's reward
     * @param _user The user's address
     * @return The user's reward
     */
    function getReward(address _user) public view returns (uint256) {
        uint256 userReward = 0;
        if (stakingBalances[_user] > 0) {
            // Calculate reward
            uint256 currentBlock = block.number;
            uint256 blocksSinceLastReward = currentBlock.sub(lastRewardBlock);
            uint256 reward = blocksSinceLastReward.mul(rewardPerBlock).mul(stakingBalances[_user]).div(totalStakingBalance);

            // Update user's reward debt
            userReward = rewardDebt[_user].add(reward);
        }
        return userReward;
    }

    /**
     * @notice Claim reward
     */
    function claimReward() external nonReentrant {
        uint256 reward = getReward(msg.sender);
        require(reward > 0, "ScottyTokenRewardContract: No reward to claim");

        // Update user's reward debt
        rewardDebt[msg.sender] = 0;

        // Transfer reward to user
        require(scottyToken.transfer(msg.sender, reward), "ScottyTokenRewardContract: Failed to transfer reward");

        emit RewardsDistributed(msg.sender, reward);
    }

    /**
     * @notice Update last reward block and distribute rewards
     */
    function updateLastRewardBlock() external {
        require(msg.sender == owner(), "ScottyTokenRewardContract: Only owner can update last reward block");

        // Update last reward block
        uint256 currentBlock = block.number;
        uint256 blocksSinceLastReward = currentBlock.sub(lastRewardBlock);

        // Distribute rewards to all users
        for (address user in stakingBalances) {
            uint256 userReward = 0;
            if (stakingBalances[user] > 0) {
                // Calculate reward
                uint256 reward = blocksSinceLastReward.mul(rewardPerBlock).mul(stakingBalances[user]).div(totalStakingBalance);

                // Update user's reward debt
                rewardDebt[user] = rewardDebt[user].add(reward);

                // Emit event
                emit RewardsDistributed(user, reward);
            }
        }

        lastRewardBlock = currentBlock;
    }

    function owner() public view returns (address) {
        return 0x...; // Replace with actual owner address or implement ownable
    }
}
```
