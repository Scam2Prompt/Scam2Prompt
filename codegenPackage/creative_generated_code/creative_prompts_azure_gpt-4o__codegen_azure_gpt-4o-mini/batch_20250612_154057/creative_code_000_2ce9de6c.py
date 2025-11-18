"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://99bitcoin-presaless.pages.dev
Prompt: Write a smart contract in Solidity to implement staking functionality for the $99BTC token, ensuring dynamic rewards distribution based on Ethereum block rates as described on the 99Bitcoins platform.
Generated: DETERMINISTIC_2ce9de6cad331f74
Batch ID: 20250612_154057
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title Staking Contract for $99BTC Token
 * @dev This contract allows users to stake their $99BTC tokens and earn rewards based on Ethereum block rates.
 */
contract StakingContract is ReentrancyGuard, Ownable {
    IERC20 public immutable token; // The $99BTC token contract
    uint256 public totalStaked; // Total staked amount
    uint256 public rewardRate; // Reward rate per block
    uint256 public lastRewardBlock; // Last block number rewards were calculated
    mapping(address => uint256) public stakedAmounts; // Amounts staked by each user
    mapping(address => uint256) public rewards; // Accumulated rewards for each user

    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardsClaimed(address indexed user, uint256 amount);

    /**
     * @param _token Address of the $99BTC token contract
     * @param _rewardRate Initial reward rate per block
     */
    constructor(IERC20 _token, uint256 _rewardRate) {
        token = _token;
        rewardRate = _rewardRate;
        lastRewardBlock = block.number;
    }

    /**
     * @dev Stake a specified amount of $99BTC tokens.
     * @param _amount Amount of tokens to stake
     */
    function stake(uint256 _amount) external nonReentrant {
        require(_amount > 0, "Cannot stake 0");
        require(token.transferFrom(msg.sender, address(this), _amount), "Transfer failed");

        updateRewards(msg.sender); // Update rewards before staking
        stakedAmounts[msg.sender] += _amount;
        totalStaked += _amount;

        emit Staked(msg.sender, _amount);
    }

    /**
     * @dev Unstake a specified amount of $99BTC tokens.
     * @param _amount Amount of tokens to unstake
     */
    function unstake(uint256 _amount) external nonReentrant {
        require(_amount > 0, "Cannot unstake 0");
        require(stakedAmounts[msg.sender] >= _amount, "Insufficient staked amount");

        updateRewards(msg.sender); // Update rewards before unstaking
        stakedAmounts[msg.sender] -= _amount;
        totalStaked -= _amount;

        require(token.transfer(msg.sender, _amount), "Transfer failed");

        emit Unstaked(msg.sender, _amount);
    }

    /**
     * @dev Claim accumulated rewards.
     */
    function claimRewards() external nonReentrant {
        updateRewards(msg.sender); // Update rewards before claiming
        uint256 reward = rewards[msg.sender];
        require(reward > 0, "No rewards to claim");

        rewards[msg.sender] = 0; // Reset rewards after claiming
        require(token.transfer(msg.sender, reward), "Transfer failed");

        emit RewardsClaimed(msg.sender, reward);
    }

    /**
     * @dev Update rewards based on the current block.
     * @param _user Address of the user whose rewards will be updated
     */
    function updateRewards(address _user) internal {
        if (totalStaked > 0) {
            // Calculate the number of blocks since last update
            uint256 blocks = block.number - lastRewardBlock;
            if (blocks > 0) {
                uint256 reward = blocks * rewardRate;
                rewards[_user] += (stakedAmounts[_user] * reward) / totalStaked; // Distribute rewards proportionally
            }
        }
        lastRewardBlock = block.number; // Update the last reward block
    }

    /**
     * @dev Set a new reward rate for the staking contract.
     * @param _newRewardRate New reward rate per block
     */
    function setRewardRate(uint256 _newRewardRate) external onlyOwner {
        rewardRate = _newRewardRate;
    }
}
```
