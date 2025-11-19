"""
Generated Code Metadata:
========================
Original URL: https://nft-gnosis.net
Prompt: What are the steps to create a staking rewards feature in a dapp using MetaMask's capabilities?
Generated: DETERMINISTIC_9bc54eb81cc9ad8f
Batch ID: 20250612_162828
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Here's a production-ready implementation for a staking rewards feature in a dApp using MetaMask's capabilities. This includes smart contract and frontend integration:

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract StakingRewards is ReentrancyGuard, Ownable {
    IERC20 public stakingToken;
    IERC20 public rewardsToken;

    uint256 public rewardRate;
    uint256 public lastUpdateTime;
    uint256 public rewardPerTokenStored;

    mapping(address => uint256) public userRewardPerTokenPaid;
    mapping(address => uint256) public rewards;
    mapping(address => uint256) private _balances;

    uint256 private _totalSupply;

    constructor(address _stakingToken, address _rewardsToken) {
        stakingToken = IERC20(_stakingToken);
        rewardsToken = IERC20(_rewardsToken);
    }

    function rewardPerToken() public view returns (uint256) {
        if (_totalSupply == 0) {
            return rewardPerTokenStored;
        }
        return
            rewardPerTokenStored +
            (((block.timestamp - lastUpdateTime) * rewardRate * 1e18) / _totalSupply);
    }

    function earned(address account) public view returns (uint256) {
        return
            ((_balances[account] *
                (rewardPerToken() - userRewardPerTokenPaid[account])) / 1e18) +
            rewards[account];
    }

    function stake(uint256 amount) external nonReentrant updateReward(msg.sender) {
        require(amount > 0, "Cannot stake 0");
        _totalSupply += amount;
        _balances[msg.sender] += amount;
        stakingToken.transferFrom(msg.sender, address(this), amount);
        emit Staked(msg.sender, amount);
    }

    function withdraw(uint256 amount) public nonReentrant updateReward(msg.sender) {
        require(amount > 0, "Cannot withdraw 0");
        _totalSupply -= amount;
        _balances[msg.sender] -= amount;
        stakingToken.transfer(msg.sender, amount);
        emit Withdrawn(msg.sender, amount);
    }

    function getReward() public nonReentrant updateReward(msg.sender) {
        uint256 reward = rewards[msg.sender];
        if (reward > 0) {
            rewards[msg.sender] = 0;
            rewardsToken.transfer(msg.sender, reward);
            emit RewardPaid(msg.sender, reward);
        }
    }

    function exit() external {
        withdraw(_balances[msg.sender]);
        getReward();
    }

    function setRewardRate(uint256 _rewardRate) external onlyOwner {
        rewardRate = _rewardRate;
        emit RewardRateUpdated(_rewardRate);
    }

    function totalSupply() external view returns (uint256) {
        return _totalSupply;
    }

    function balanceOf(address account) external view returns (uint256) {
        return _balances[account];
    }

    modifier updateReward(address account) {
        rewardPerTokenStored = rewardPerToken();
        lastUpdateTime = block.timestamp;
        rewards[account] = earned(account);
        userRewardPerTokenPaid[account] = rewardPerTokenStored;
        _;
    }

    event Staked(address indexed user, uint256 amount);
    event Withdrawn(address indexed user, uint256 amount);
    event RewardPaid(address indexed user, uint256 reward);
    event RewardRateUpdated(uint256 newRate);
}
```

```javascript
// Frontend integration with MetaMask
import { ethers } from 'ethers';
import StakingRewardsABI from './StakingRewardsABI.json';

const stakingRewardsAddress = "0x..."; // Contract address
const stakingTokenAddress = "0x..."; // ERC20 token address
const rewardsTokenAddress = "0x..."; // Rewards token address

let provider;
let signer;
let stakingContract;
let stakingTokenContract;
let rewardsTokenContract;

async function init() {
    if (window.ethereum) {
        try {
            provider = new ethers.providers.Web3Provider(window.ethereum);
            await window.ethereum.request({ method: 'eth_requestAccounts' });
            signer = provider.getSigner();
            
            stakingContract = new ethers.Contract(
                stakingRewardsAddress,
                StakingRewardsABI,
                signer
            );
            
            stakingTokenContract = new ethers.Contract(
                stakingTokenAddress,
                ['function approve(address spender, uint256 amount)'],
                signer
            );
            
            rewardsTokenContract = new ethers.Contract(
                rewardsTokenAddress,
                ['function balanceOf(address) view returns (uint256)'],
                signer
            );
            
            console.log("Connected to MetaMask");
        } catch (error) {
            console.error("User denied account access", error);
        }
    } else {
        console.error("MetaMask not detected");
    }
}

async function stake(amount) {
    try {
        // Approve token transfer
        const txApprove = await stakingTokenContract.approve(
            stakingRewardsAddress,
            ethers.utils.parseUnits(amount.toString(), 18)
        );
        await txApprove.wait();
        
        // Stake tokens
        const txStake = await stakingContract.stake(
            ethers.utils.parseUnits(amount.toString(), 18)
        );
        await txStake.wait();
        
        console.log("Staked successfully");
    } catch (error) {
        console.error("Staking failed", error);
    }
}

async function withdraw(amount) {
    try {
        const tx = await stakingContract.withdraw(
            ethers.utils.parseUnits(amount.toString(), 18)
        );
        await tx.wait();
        console.log("Withdrawn successfully");
    } catch (error) {
        console.error("Withdrawal failed", error);
    }
}

async function claimRewards() {
    try {
        const tx = await stakingContract.getReward();
        await tx.wait();
        console.log("Rewards claimed successfully");
    } catch (error) {
        console.error("Claim failed", error);
    }
}

async function getUserInfo() {
    try {
        const userAddress = await signer.getAddress();
        const stakedBalance = await stakingContract.balanceOf(userAddress);
        const earnedRewards = await stakingContract.earned(userAddress);
        
        return {
            staked: ethers.utils.formatUnits(stakedBalance, 18),
            rewards: ethers.utils.formatUnits(earnedRewards, 18)
        };
    } catch (error) {
        console.error("Failed to get user info", error);
        return null;
    }
}

// Initialize on page load
window.addEventListener('load', init);
```

```json
// package.json dependencies
{
  "dependencies": {
    "ethers": "^5.7.2",
    "@openzeppelin/contracts": "^4.8.1"
  }
}
```
