"""
Generated Code Metadata:
========================
Original URL: https://yieldeth.org
Prompt: "Create a simple staking application using yieldETH's smart contracts, allowing users to stake ETH and earn rewards in the form of yieldETH tokens."
Generated: DETERMINISTIC_850be9a41a324837
Batch ID: 20250622_211141
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
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title YieldETHStaking
 * @dev A smart contract for staking ETH and earning yieldETH tokens as rewards.
 */
contract YieldETHStaking is ReentrancyGuard {
    using SafeMath for uint256;

    // State variables
    IERC20 public yieldETH;
    uint256 public totalStaked;
    uint256 public rewardRate; // Reward rate per block
    uint256 public lastUpdateBlock;
    uint256 public rewardPerTokenStored;

    mapping(address => uint256) public userStakes;
    mapping(address => uint256) public userRewards;
    mapping(address => uint256) public userRewardPerTokenPaid;

    // Events
    event Staked(address indexed user, uint256 amount);
    event Withdrawn(address indexed user, uint256 amount);
    event RewardPaid(address indexed user, uint256 reward);

    /**
     * @dev Constructor initializes the staking contract.
     * @param _yieldETH The address of the yieldETH token contract.
     * @param _rewardRate The reward rate per block.
     */
    constructor(address _yieldETH, uint256 _rewardRate) {
        yieldETH = IERC20(_yieldETH);
        rewardRate = _rewardRate;
        lastUpdateBlock = block.number;
    }

    /**
     * @dev Modifier to update reward for a given user.
     */
    modifier updateReward(address account) {
        rewardPerTokenStored = rewardPerToken();
        lastUpdateBlock = block.number;
        if (account != address(0)) {
            userRewards[account] = earned(account);
            userRewardPerTokenPaid[account] = rewardPerTokenStored;
        }
        _;
    }

    /**
     * @dev Calculate the current reward per token.
     * @return The reward per token.
     */
    function rewardPerToken() public view returns (uint256) {
        if (totalStaked == 0) {
            return rewardPerTokenStored;
        }
        return rewardPerTokenStored.add(
            block.number.sub(lastUpdateBlock).mul(rewardRate).mul(1e18).div(totalStaked)
        );
    }

    /**
     * @dev Calculate the earned rewards for a user.
     * @param account The address of the user.
     * @return The amount of rewards earned.
     */
    function earned(address account) public view returns (uint256) {
        return userStakes[account]
            .mul(rewardPerToken().sub(userRewardPerTokenPaid[account]))
            .div(1e18)
            .add(userRewards[account]);
    }

    /**
     * @dev Stake ETH into the contract.
     */
    function stake() external payable nonReentrant updateReward(msg.sender) {
        require(msg.value > 0, "Cannot stake 0 ETH");
        userStakes[msg.sender] = userStakes[msg.sender].add(msg.value);
        totalStaked = totalStaked.add(msg.value);
        emit Staked(msg.sender, msg.value);
    }

    /**
     * @dev Withdraw staked ETH and claim rewards.
     * @param amount The amount of ETH to withdraw.
     */
    function withdraw(uint256 amount) external nonReentrant updateReward(msg.sender) {
        require(amount > 0, "Cannot withdraw 0 ETH");
        require(userStakes[msg.sender] >= amount, "Insufficient staked balance");
        userStakes[msg.sender] = userStakes[msg.sender].sub(amount);
        totalStaked = totalStaked.sub(amount);
        (bool success, ) = msg.sender.call{value: amount}("");
        require(success, "ETH transfer failed");
        emit Withdrawn(msg.sender, amount);
    }

    /**
     * @dev Claim earned rewards.
     */
    function claimRewards() external nonReentrant updateReward(msg.sender) {
        uint256 reward = userRewards[msg.sender];
        require(reward > 0, "No rewards to claim");
        userRewards[msg.sender] = 0;
        require(yieldETH.transfer(msg.sender, reward), "Reward transfer failed");
        emit RewardPaid(msg.sender, reward);
    }

    /**
     * @dev Get the current stake balance of a user.
     * @param account The address of the user.
     * @return The staked balance.
     */
    function balanceOf(address account) external view returns (uint256) {
        return userStakes[account];
    }
}
```

```javascript
// Frontend interaction example (using ethers.js)
const { ethers } = require("ethers");

// Contract ABI (simplified)
const stakingABI = [
    "function stake() payable",
    "function withdraw(uint256 amount)",
    "function claimRewards()",
    "function balanceOf(address) view returns (uint256)",
    "function earned(address) view returns (uint256)",
    "event Staked(address indexed user, uint256 amount)",
    "event Withdrawn(address indexed user, uint256 amount)",
    "event RewardPaid(address indexed user, uint256 reward)"
];

// Initialize provider and signer
const provider = new ethers.providers.Web3Provider(window.ethereum);
const signer = provider.getSigner();

// Contract address (replace with actual deployed address)
const stakingAddress = "0x123...";

// Create contract instance
const stakingContract = new ethers.Contract(stakingAddress, stakingABI, signer);

// Stake ETH
async function stakeETH(amount) {
    try {
        const tx = await stakingContract.stake({ value: ethers.utils.parseEther(amount.toString()) });
        await tx.wait();
        console.log("Staked successfully");
    } catch (error) {
        console.error("Staking failed:", error);
    }
}

// Withdraw ETH
async function withdrawETH(amount) {
    try {
        const tx = await stakingContract.withdraw(ethers.utils.parseEther(amount.toString()));
        await tx.wait();
        console.log("Withdrawn successfully");
    } catch (error) {
        console.error("Withdrawal failed:", error);
    }
}

// Claim rewards
async function claimRewards() {
    try {
        const tx = await stakingContract.claimRewards();
        await tx.wait();
        console.log("Rewards claimed successfully");
    } catch (error) {
        console.error("Claim failed:", error);
    }
}

// Get user balance
async function getUserBalance() {
    try {
        const userAddress = await signer.getAddress();
        const balance = await stakingContract.balanceOf(userAddress);
        return ethers.utils.formatEther(balance);
    } catch (error) {
        console.error("Balance check failed:", error);
        return 0;
    }
}

// Get earned rewards
async function getEarnedRewards() {
    try {
        const userAddress = await signer.getAddress();
        const rewards = await stakingContract.earned(userAddress);
        return ethers.utils.formatEther(rewards);
    } catch (error) {
        console.error("Rewards check failed:", error);
        return 0;
    }
}
```
