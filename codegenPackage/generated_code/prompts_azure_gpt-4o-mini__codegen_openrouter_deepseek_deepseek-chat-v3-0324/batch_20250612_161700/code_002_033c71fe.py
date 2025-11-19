"""
Generated Code Metadata:
========================
Original URL: https://mememoguls-en.pages.dev
Prompt: Create a Solidity contract that allows users to stake their $MGLS tokens and earn rewards based on their share of the staking pool.
Generated: DETERMINISTIC_033c71fe902a85d2
Batch ID: 20250612_161700
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
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract MGLSStaking is ReentrancyGuard, Ownable {
    using SafeERC20 for IERC20;

    // State variables
    IERC20 public immutable stakingToken;
    IERC20 public immutable rewardsToken;

    uint256 public rewardRate;
    uint256 public lastUpdateTime;
    uint256 public rewardPerTokenStored;

    mapping(address => uint256) public userRewardPerTokenPaid;
    mapping(address => uint256) public rewards;

    uint256 private _totalSupply;
    mapping(address => uint256) private _balances;

    // Events
    event Staked(address indexed user, uint256 amount);
    event Withdrawn(address indexed user, uint256 amount);
    event RewardPaid(address indexed user, uint256 reward);
    event RewardRateUpdated(uint256 newRate);

    // Constructor
    constructor(address _stakingToken, address _rewardsToken) {
        stakingToken = IERC20(_stakingToken);
        rewardsToken = IERC20(_rewardsToken);
    }

    // Modifier to update reward for caller
    modifier updateReward(address account) {
        rewardPerTokenStored = rewardPerToken();
        lastUpdateTime = lastTimeRewardApplicable();
        if (account != address(0)) {
            rewards[account] = earned(account);
            userRewardPerTokenPaid[account] = rewardPerTokenStored;
        }
        _;
    }

    // Returns the last time the reward was applicable
    function lastTimeRewardApplicable() public view returns (uint256) {
        return block.timestamp;
    }

    // Returns the reward per token staked
    function rewardPerToken() public view returns (uint256) {
        if (_totalSupply == 0) {
            return rewardPerTokenStored;
        }
        return
            rewardPerTokenStored +
            (((lastTimeRewardApplicable() - lastUpdateTime) * rewardRate * 1e18) / _totalSupply);
    }

    // Returns the earned rewards for an account
    function earned(address account) public view returns (uint256) {
        return
            ((_balances[account] * (rewardPerToken() - userRewardPerTokenPaid[account])) / 1e18) +
            rewards[account];
    }

    // Stake tokens to earn rewards
    function stake(uint256 amount) external nonReentrant updateReward(msg.sender) {
        require(amount > 0, "Cannot stake 0");
        _totalSupply += amount;
        _balances[msg.sender] += amount;
        stakingToken.safeTransferFrom(msg.sender, address(this), amount);
        emit Staked(msg.sender, amount);
    }

    // Withdraw staked tokens
    function withdraw(uint256 amount) public nonReentrant updateReward(msg.sender) {
        require(amount > 0, "Cannot withdraw 0");
        require(_balances[msg.sender] >= amount, "Insufficient balance");
        _totalSupply -= amount;
        _balances[msg.sender] -= amount;
        stakingToken.safeTransfer(msg.sender, amount);
        emit Withdrawn(msg.sender, amount);
    }

    // Claim earned rewards
    function getReward() public nonReentrant updateReward(msg.sender) {
        uint256 reward = rewards[msg.sender];
        if (reward > 0) {
            rewards[msg.sender] = 0;
            rewardsToken.safeTransfer(msg.sender, reward);
            emit RewardPaid(msg.sender, reward);
        }
    }

    // Exit the staking (withdraw all and claim rewards)
    function exit() external {
        withdraw(_balances[msg.sender]);
        getReward();
    }

    // Set the reward rate (only owner)
    function setRewardRate(uint256 _rewardRate) external onlyOwner {
        rewardRate = _rewardRate;
        emit RewardRateUpdated(_rewardRate);
    }

    // Get total staked amount
    function totalSupply() external view returns (uint256) {
        return _totalSupply;
    }

    // Get staked amount for an account
    function balanceOf(address account) external view returns (uint256) {
        return _balances[account];
    }

    // Recover ERC20 tokens (only owner)
    function recoverERC20(address tokenAddress, uint256 tokenAmount) external onlyOwner {
        require(
            tokenAddress != address(stakingToken) && tokenAddress != address(rewardsToken),
            "Cannot withdraw staking or rewards tokens"
        );
        IERC20(tokenAddress).safeTransfer(owner(), tokenAmount);
    }
}
```
