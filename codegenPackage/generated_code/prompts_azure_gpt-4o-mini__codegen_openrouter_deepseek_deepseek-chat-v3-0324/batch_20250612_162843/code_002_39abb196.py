"""
Generated Code Metadata:
========================
Original URL: https://waveexcellentwork.net
Prompt: Describe how to implement staking and unstaking functionalities in a DApp utilizing MainnetSync's tools.
Generated: DETERMINISTIC_39abb196fd9b8085
Batch ID: 20250612_162843
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Here's a Solidity smart contract implementation for staking and unstaking functionalities that could be integrated with MainnetSync's tools:

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title StakingContract
 * @dev Implements staking and unstaking functionality with reward distribution
 */
contract StakingContract is ReentrancyGuard, Ownable {
    IERC20 public stakingToken;
    IERC20 public rewardToken;

    // Staking parameters
    uint256 public rewardRate; // Reward tokens per second per token staked
    uint256 public lastUpdateTime;
    uint256 public rewardPerTokenStored;

    // User staking data
    mapping(address => uint256) public userRewardPerTokenPaid;
    mapping(address => uint256) public rewards;
    mapping(address => uint256) private _balances;
    uint256 private _totalSupply;

    // Events
    event Staked(address indexed user, uint256 amount);
    event Withdrawn(address indexed user, uint256 amount);
    event RewardPaid(address indexed user, uint256 reward);

    constructor(address _stakingToken, address _rewardToken) {
        stakingToken = IERC20(_stakingToken);
        rewardToken = IERC20(_rewardToken);
    }

    /**
     * @dev Updates the reward for a specific user
     */
    modifier updateReward(address account) {
        rewardPerTokenStored = rewardPerToken();
        lastUpdateTime = block.timestamp;
        if (account != address(0)) {
            rewards[account] = earned(account);
            userRewardPerTokenPaid[account] = rewardPerTokenStored;
        }
        _;
    }

    /**
     * @return Total amount of tokens staked
     */
    function totalSupply() external view returns (uint256) {
        return _totalSupply;
    }

    /**
     * @param account The address to query
     * @return Amount staked by account
     */
    function balanceOf(address account) external view returns (uint256) {
        return _balances[account];
    }

    /**
     * @dev Calculates the current reward per token
     */
    function rewardPerToken() public view returns (uint256) {
        if (_totalSupply == 0) {
            return rewardPerTokenStored;
        }
        return
            rewardPerTokenStored +
            (((block.timestamp - lastUpdateTime) * rewardRate * 1e18) / _totalSupply);
    }

    /**
     * @param account The address to calculate rewards for
     * @return Earned reward amount for account
     */
    function earned(address account) public view returns (uint256) {
        return
            ((_balances[account] *
                (rewardPerToken() - userRewardPerTokenPaid[account])) / 1e18) +
            rewards[account];
    }

    /**
     * @dev Stake tokens to earn rewards
     * @param amount Amount of tokens to stake
     */
    function stake(uint256 amount) external nonReentrant updateReward(msg.sender) {
        require(amount > 0, "Cannot stake 0");
        _totalSupply += amount;
        _balances[msg.sender] += amount;
        require(
            stakingToken.transferFrom(msg.sender, address(this), amount),
            "Transfer failed"
        );
        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Withdraw staked tokens
     * @param amount Amount of tokens to withdraw
     */
    function withdraw(uint256 amount) public nonReentrant updateReward(msg.sender) {
        require(amount > 0, "Cannot withdraw 0");
        _totalSupply -= amount;
        _balances[msg.sender] -= amount;
        require(stakingToken.transfer(msg.sender, amount), "Transfer failed");
        emit Withdrawn(msg.sender, amount);
    }

    /**
     * @dev Claim earned rewards
     */
    function getReward() public nonReentrant updateReward(msg.sender) {
        uint256 reward = rewards[msg.sender];
        if (reward > 0) {
            rewards[msg.sender] = 0;
            require(rewardToken.transfer(msg.sender, reward), "Transfer failed");
            emit RewardPaid(msg.sender, reward);
        }
    }

    /**
     * @dev Withdraw all stake and claim rewards
     */
    function exit() external {
        withdraw(_balances[msg.sender]);
        getReward();
    }

    /**
     * @dev Set the reward rate (only owner)
     * @param _rewardRate New reward rate
     */
    function setRewardRate(uint256 _rewardRate) external onlyOwner {
        rewardRate = _rewardRate;
    }

    /**
     * @dev Recover any ERC20 tokens sent to the contract by mistake
     * @param tokenAddress Address of token to recover
     * @param amount Amount to recover
     */
    function recoverERC20(address tokenAddress, uint256 amount) external onlyOwner {
        require(
            tokenAddress != address(stakingToken) && tokenAddress != address(rewardToken),
            "Cannot withdraw staking or reward tokens"
        );
        IERC20(tokenAddress).transfer(owner(), amount);
    }
}
```

And here's a simple JavaScript interaction example using ethers.js that could work with MainnetSync:

```javascript
const { ethers } = require('ethers');

// Connect to MainnetSync
const provider = new ethers.providers.JsonRpcProvider('YOUR_MAINNETSYNC_RPC_URL');
const stakingContractAddress = 'YOUR_STAKING_CONTRACT_ADDRESS';
const stakingTokenAddress = 'YOUR_STAKING_TOKEN_ADDRESS';

// ABI for staking contract
const stakingContractABI = [
    "function stake(uint256 amount)",
    "function withdraw(uint256 amount)",
    "function getReward()",
    "function exit()",
    "function balanceOf(address account) view returns (uint256)",
    "function earned(address account) view returns (uint256)"
];

// ABI for ERC20 token
const erc20ABI = [
    "function approve(address spender, uint256 amount) returns (bool)",
    "function allowance(address owner, address spender) view returns (uint256)"
];

class StakingService {
    constructor(signer) {
        this.signer = signer;
        this.stakingContract = new ethers.Contract(stakingContractAddress, stakingContractABI, signer);
        this.stakingToken = new ethers.Contract(stakingTokenAddress, erc20ABI, signer);
    }

    async stake(amount) {
        // Approve the staking contract to spend tokens
        const tx1 = await this.stakingToken.approve(stakingContractAddress, amount);
        await tx1.wait();
        
        // Stake tokens
        const tx2 = await this.stakingContract.stake(amount);
        return tx2.wait();
    }

    async withdraw(amount) {
        const tx = await this.stakingContract.withdraw(amount);
        return tx.wait();
    }

    async getReward() {
        const tx = await this.stakingContract.getReward();
        return tx.wait();
    }

    async exit() {
        const tx = await this.stakingContract.exit();
        return tx.wait();
    }

    async getStakedBalance(address) {
        return this.stakingContract.balanceOf(address);
    }

    async getEarnedRewards(address) {
        return this.stakingContract.earned(address);
    }
}
```
