"""
Generated Code Metadata:
========================
Original URL: https://connectautofixing.vercel.app
Prompt: Design a staking system for a cryptocurrency using a smart contract, including functions for staking, unstaking, and rewarding stakers with additional coins or tokens.
Generated: DETERMINISTIC_91cb2f6bb6e2fadf
Batch ID: 20250622_211021
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

# Solidity Staking Contract

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title CryptoStaking
 * @dev A staking contract that allows users to stake ERC20 tokens and earn rewards
 */
contract CryptoStaking is ReentrancyGuard, Ownable {
    // The staking token
    IERC20 public stakingToken;
    // The reward token
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

    event Staked(address indexed user, uint256 amount);
    event Withdrawn(address indexed user, uint256 amount);
    event RewardPaid(address indexed user, uint256 reward);

    /**
     * @dev Constructor
     * @param _stakingToken Address of the staking token
     * @param _rewardToken Address of the reward token
     * @param _rewardRate Reward rate (tokens per second per token staked)
     */
    constructor(
        address _stakingToken,
        address _rewardToken,
        uint256 _rewardRate
    ) {
        stakingToken = IERC20(_stakingToken);
        rewardToken = IERC20(_rewardToken);
        rewardRate = _rewardRate;
    }

    /**
     * @dev Updates reward for a given account
     * @param account The account to update rewards for
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
     * @dev Calculates the current reward per token
     * @return The updated reward per token
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
     * @dev Calculates the earned rewards for an account
     * @param account The account to check rewards for
     * @return The earned rewards
     */
    function earned(address account) public view returns (uint256) {
        return
            (_balances[account] *
                (rewardPerToken() - userRewardPerTokenPaid[account])) /
            1e18 +
            rewards[account];
    }

    /**
     * @dev Stake tokens to earn rewards
     * @param amount The amount of tokens to stake
     */
    function stake(uint256 amount) external nonReentrant updateReward(msg.sender) {
        require(amount > 0, "Cannot stake 0");
        _totalSupply += amount;
        _balances[msg.sender] += amount;
        stakingToken.transferFrom(msg.sender, address(this), amount);
        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Withdraw staked tokens
     * @param amount The amount of tokens to withdraw
     */
    function withdraw(uint256 amount) public nonReentrant updateReward(msg.sender) {
        require(amount > 0, "Cannot withdraw 0");
        require(_balances[msg.sender] >= amount, "Insufficient balance");
        _totalSupply -= amount;
        _balances[msg.sender] -= amount;
        stakingToken.transfer(msg.sender, amount);
        emit Withdrawn(msg.sender, amount);
    }

    /**
     * @dev Claim earned rewards
     */
    function getReward() public nonReentrant updateReward(msg.sender) {
        uint256 reward = rewards[msg.sender];
        if (reward > 0) {
            rewards[msg.sender] = 0;
            rewardToken.transfer(msg.sender, reward);
            emit RewardPaid(msg.sender, reward);
        }
    }

    /**
     * @dev Exit the staking system by withdrawing all staked tokens and claiming rewards
     */
    function exit() external {
        withdraw(_balances[msg.sender]);
        getReward();
    }

    /**
     * @dev Returns the total staked tokens
     * @return The total staked tokens
     */
    function totalSupply() external view returns (uint256) {
        return _totalSupply;
    }

    /**
     * @dev Returns the staked balance of an account
     * @param account The account to check balance for
     * @return The staked balance
     */
    function balanceOf(address account) external view returns (uint256) {
        return _balances[account];
    }

    /**
     * @dev Updates the reward rate (owner only)
     * @param _rewardRate The new reward rate
     */
    function setRewardRate(uint256 _rewardRate) external onlyOwner {
        rewardRate = _rewardRate;
    }

    /**
     * @dev Recovers any ERC20 token sent to the contract (owner only)
     * @param tokenAddress The token address
     * @param tokenAmount The amount to recover
     */
    function recoverERC20(address tokenAddress, uint256 tokenAmount) external onlyOwner {
        require(
            tokenAddress != address(stakingToken) && tokenAddress != address(rewardToken),
            "Cannot withdraw staking or reward tokens"
        );
        IERC20(tokenAddress).transfer(owner(), tokenAmount);
    }
}
```
