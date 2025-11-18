"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dogecoin20presale-claim.pages.dev
Prompt: Provide a step-by-step guide to deploy a staking smart contract for DOGE20 on Ethereum, including reward distribution logic.
Generated: DETERMINISTIC_5af85a2bb372873a
Batch ID: 20250612_152235
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is a clean, well-documented, production-ready Solidity code for deploying a staking smart contract for DOGE20 on Ethereum, including reward distribution logic. Please note that this code assumes the DOGE20 token follows the ERC20 standard.

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/**
 * @title DOGE20 Staking Contract
 * @dev This contract allows users to stake DOGE20 tokens and earn rewards.
 */
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

contract Doge20Staking is Ownable, ReentrancyGuard {
    // Address of the DOGE20 token contract
    IERC20 public immutable doge20Token;

    // Reward rate per second
    uint256 public rewardRate;

    // Total amount of tokens staked in the contract
    uint256 public totalStaked;

    // Mapping of user address to their staked amount
    mapping(address => uint256) public stakedBalance;

    // Mapping of user address to their last update time for rewards
    mapping(address => uint256) public lastUpdateTime;

    // Mapping of user address to their unclaimed rewards
    mapping(address => uint256) public rewards;

    /**
     * @dev Event emitted when a user stakes tokens.
     */
    event Staked(address indexed user, uint256 amount);

    /**
     * @dev Event emitted when a user withdraws their tokens.
     */
    event Withdrawn(address indexed user, uint256 amount);

    /**
     * @dev Event emitted when a user claims their rewards.
     */
    event RewardPaid(address indexed user, uint256 reward);

    /**
     * @dev Constructor to initialize the staking contract.
     * @param _doge20Token Address of the DOGE20 token contract.
     * @param _rewardRate Reward rate per second.
     */
    constructor(IERC20 _doge20Token, uint256 _rewardRate) {
        doge20Token = _doge20Token;
        rewardRate = _rewardRate;
    }

    /**
     * @dev Modifier to update rewards for a user before performing certain actions.
     * @param user Address of the user.
     */
    modifier updateReward(address user) {
        if (user != address(0)) {
            rewards[user] += earned(user);
            lastUpdateTime[user] = block.timestamp;
        }
        _;
    }

    /**
     * @dev Stake DOGE20 tokens in the contract.
     * @param amount Amount of tokens to stake.
     */
    function stake(uint256 amount) external nonReentrant updateReward(msg.sender) {
        require(amount > 0, "Cannot stake 0 tokens");
        doge20Token.transferFrom(msg.sender, address(this), amount);
        stakedBalance[msg.sender] += amount;
        totalStaked += amount;
        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Withdraw staked tokens from the contract.
     * @param amount Amount of tokens to withdraw.
     */
    function withdraw(uint256 amount) external nonReentrant updateReward(msg.sender) {
        require(amount > 0, "Cannot withdraw 0 tokens");
        require(stakedBalance[msg.sender] >= amount, "Insufficient staked balance");
        stakedBalance[msg.sender] -= amount;
        totalStaked -= amount;
        doge20Token.transfer(msg.sender, amount);
        emit Withdrawn(msg.sender, amount);
    }

    /**
     * @dev Claim earned rewards.
     */
    function claimReward() external nonReentrant updateReward(msg.sender) {
        uint256 reward = rewards[msg.sender];
        require(reward > 0, "No rewards to claim");
        rewards[msg.sender] = 0;
        doge20Token.transfer(msg.sender, reward);
        emit RewardPaid(msg.sender, reward);
    }

    /**
     * @dev Calculate the rewards earned by a user.
     * @param user Address of the user.
     * @return Earned rewards.
     */
    function earned(address user) public view returns (uint256) {
        uint256 staked = stakedBalance[user];
        if (staked == 0) return 0;
        uint256 timeElapsed = block.timestamp - lastUpdateTime[user];
        return (staked * rewardRate * timeElapsed) / 1e18;
    }

    /**
     * @dev Set a new reward rate.
     * @param _rewardRate New reward rate per second.
     */
    function setRewardRate(uint256 _rewardRate) external onlyOwner {
        rewardRate = _rewardRate;
    }
}
```

### Deployment Steps
1. Make sure you have an Ethereum development environment set up (e.g., Hardhat or Remix).
2. Update the constructor parameters (`_doge20Token` and `_rewardRate`) with your DOGE20 token address and desired reward rate.
3. Compile the contract using Solidity 0.8.0 or higher.
4. Deploy the contract to the Ethereum network.
5. Interact with the contract to allow users to stake DOGE20 tokens and claim rewards.

This code implements staking functionality for DOGE20 tokens with proper reward distribution, error handling, and security features like `ReentrancyGuard`.
