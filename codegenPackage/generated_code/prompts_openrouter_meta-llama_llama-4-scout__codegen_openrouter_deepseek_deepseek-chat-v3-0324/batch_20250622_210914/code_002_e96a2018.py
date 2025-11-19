"""
Generated Code Metadata:
========================
Original URL: https://blackder.pages.dev
Prompt: Generate a smart contract code for handling $BLD token staking, rewards, and withdrawals on a blockchain platform.
Generated: DETERMINISTIC_e96a2018e3a46de6
Batch ID: 20250622_210914
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

contract BLDStaking is Ownable, ReentrancyGuard {
    using SafeERC20 for IERC20;

    // State variables
    IERC20 public immutable stakingToken;
    IERC20 public immutable rewardsToken;

    uint256 public constant REWARD_RATE = 10; // 10% annual reward rate
    uint256 public constant REWARD_INTERVAL = 365 days;
    uint256 public constant MIN_STAKE_AMOUNT = 100 * 10**18; // 100 BLD tokens

    uint256 public totalStaked;
    uint256 public lastUpdateTime;
    uint256 public rewardPerTokenStored;

    mapping(address => uint256) public userRewardPerTokenPaid;
    mapping(address => uint256) public rewards;
    mapping(address => uint256) private _balances;

    // Events
    event Staked(address indexed user, uint256 amount);
    event Withdrawn(address indexed user, uint256 amount);
    event RewardPaid(address indexed user, uint256 reward);

    constructor(address _stakingToken, address _rewardsToken) {
        stakingToken = IERC20(_stakingToken);
        rewardsToken = IERC20(_rewardsToken);
    }

    modifier updateReward(address account) {
        rewardPerTokenStored = rewardPerToken();
        lastUpdateTime = block.timestamp;
        if (account != address(0)) {
            rewards[account] = earned(account);
            userRewardPerTokenPaid[account] = rewardPerTokenStored;
        }
        _;
    }

    function rewardPerToken() public view returns (uint256) {
        if (totalStaked == 0) {
            return rewardPerTokenStored;
        }
        return
            rewardPerTokenStored +
            (((block.timestamp - lastUpdateTime) * REWARD_RATE * 1e18) / REWARD_INTERVAL) /
            totalStaked;
    }

    function earned(address account) public view returns (uint256) {
        return
            (_balances[account] * (rewardPerToken() - userRewardPerTokenPaid[account])) /
            1e18 +
            rewards[account];
    }

    function balanceOf(address account) public view returns (uint256) {
        return _balances[account];
    }

    function stake(uint256 amount) external nonReentrant updateReward(msg.sender) {
        require(amount >= MIN_STAKE_AMOUNT, "Amount below minimum stake");
        require(stakingToken.balanceOf(msg.sender) >= amount, "Insufficient balance");

        totalStaked += amount;
        _balances[msg.sender] += amount;
        stakingToken.safeTransferFrom(msg.sender, address(this), amount);

        emit Staked(msg.sender, amount);
    }

    function withdraw(uint256 amount) public nonReentrant updateReward(msg.sender) {
        require(amount > 0, "Cannot withdraw 0");
        require(_balances[msg.sender] >= amount, "Insufficient staked balance");

        totalStaked -= amount;
        _balances[msg.sender] -= amount;
        stakingToken.safeTransfer(msg.sender, amount);

        emit Withdrawn(msg.sender, amount);
    }

    function getReward() public nonReentrant updateReward(msg.sender) {
        uint256 reward = rewards[msg.sender];
        if (reward > 0) {
            rewards[msg.sender] = 0;
            rewardsToken.safeTransfer(msg.sender, reward);
            emit RewardPaid(msg.sender, reward);
        }
    }

    function exit() external {
        withdraw(_balances[msg.sender]);
        getReward();
    }

    // Emergency functions for owner
    function emergencyWithdraw() external onlyOwner {
        uint256 balance = stakingToken.balanceOf(address(this));
        stakingToken.safeTransfer(owner(), balance);
    }

    function recoverERC20(address tokenAddress, uint256 tokenAmount) external onlyOwner {
        require(tokenAddress != address(stakingToken), "Cannot withdraw staking token");
        require(tokenAddress != address(rewardsToken), "Cannot withdraw rewards token");
        IERC20(tokenAddress).safeTransfer(owner(), tokenAmount);
    }
}
```
