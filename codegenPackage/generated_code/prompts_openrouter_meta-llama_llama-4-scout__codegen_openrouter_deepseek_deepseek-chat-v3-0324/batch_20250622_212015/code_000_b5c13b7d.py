"""
Generated Code Metadata:
========================
Original URL: https://rewardusdctoken.com
Prompt: Write a smart contract in Solidity that distributes USDC rewards to holders of a token, similar to the RewardUSDC (RUSDC) token.
Generated: DETERMINISTIC_b5c13b7d6df61690
Batch ID: 20250622_212015
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

contract RewardUSDC is Ownable, ReentrancyGuard {
    using SafeERC20 for IERC20;

    // Token to be held for rewards
    IERC20 public immutable stakedToken;
    // Reward token (USDC)
    IERC20 public immutable rewardToken;

    // Reward variables
    uint256 public rewardRate;
    uint256 public lastUpdateTime;
    uint256 public rewardPerTokenStored;

    // User rewards tracking
    mapping(address => uint256) public userRewardPerTokenPaid;
    mapping(address => uint256) public rewards;

    // Total staked
    uint256 private _totalStaked;
    mapping(address => uint256) private _balances;

    // Events
    event Staked(address indexed user, uint256 amount);
    event Withdrawn(address indexed user, uint256 amount);
    event RewardPaid(address indexed user, uint256 reward);
    event RewardRateUpdated(uint256 newRate);

    constructor(address _stakedToken, address _rewardToken) {
        stakedToken = IERC20(_stakedToken);
        rewardToken = IERC20(_rewardToken);
    }

    // Update reward variables
    modifier updateReward(address account) {
        rewardPerTokenStored = rewardPerToken();
        lastUpdateTime = block.timestamp;
        if (account != address(0)) {
            rewards[account] = earned(account);
            userRewardPerTokenPaid[account] = rewardPerTokenStored;
        }
        _;
    }

    // View total staked
    function totalStaked() public view returns (uint256) {
        return _totalStaked;
    }

    // View user balance
    function balanceOf(address account) public view returns (uint256) {
        return _balances[account];
    }

    // Calculate reward per token
    function rewardPerToken() public view returns (uint256) {
        if (_totalStaked == 0) {
            return rewardPerTokenStored;
        }
        return rewardPerTokenStored + (
            (block.timestamp - lastUpdateTime) * rewardRate * 1e18 / _totalStaked
        );
    }

    // Calculate earned rewards
    function earned(address account) public view returns (uint256) {
        return _balances[account] * (rewardPerToken() - userRewardPerTokenPaid[account]) / 1e18 + rewards[account];
    }

    // Stake tokens
    function stake(uint256 amount) external nonReentrant updateReward(msg.sender) {
        require(amount > 0, "Cannot stake 0");
        _totalStaked += amount;
        _balances[msg.sender] += amount;
        stakedToken.safeTransferFrom(msg.sender, address(this), amount);
        emit Staked(msg.sender, amount);
    }

    // Withdraw staked tokens
    function withdraw(uint256 amount) public nonReentrant updateReward(msg.sender) {
        require(amount > 0, "Cannot withdraw 0");
        _totalStaked -= amount;
        _balances[msg.sender] -= amount;
        stakedToken.safeTransfer(msg.sender, amount);
        emit Withdrawn(msg.sender, amount);
    }

    // Claim rewards
    function getReward() public nonReentrant updateReward(msg.sender) {
        uint256 reward = rewards[msg.sender];
        if (reward > 0) {
            rewards[msg.sender] = 0;
            rewardToken.safeTransfer(msg.sender, reward);
            emit RewardPaid(msg.sender, reward);
        }
    }

    // Exit (withdraw + claim)
    function exit() external {
        withdraw(_balances[msg.sender]);
        getReward();
    }

    // Set reward rate (only owner)
    function setRewardRate(uint256 _rewardRate) external onlyOwner {
        rewardRate = _rewardRate;
        lastUpdateTime = block.timestamp;
        emit RewardRateUpdated(_rewardRate);
    }

    // Recover ERC20 tokens (only owner)
    function recoverERC20(address tokenAddress, uint256 amount) external onlyOwner {
        require(tokenAddress != address(stakedToken), "Cannot withdraw staked token");
        IERC20(tokenAddress).safeTransfer(owner(), amount);
    }
}
```
