"""
Generated Code Metadata:
========================
Original URL: https://basedbrett.on-fleek.app
Prompt: Create a smart contract that interacts with the $Brett token on the Base Mainnet, allowing users to stake tokens and earn rewards based on their holdings.
Generated: DETERMINISTIC_b9c8417176d79b37
Batch ID: 20250612_153954
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

contract BrettStaking is ReentrancyGuard, Ownable {
    using SafeERC20 for IERC20;

    // State variables
    IERC20 public immutable brettToken;
    uint256 public rewardRate;
    uint256 public lastUpdateTime;
    uint256 public rewardPerTokenStored;
    uint256 public totalSupply;

    // Staking period in seconds (e.g., 30 days)
    uint256 public constant STAKING_PERIOD = 30 days;

    // User stakes
    struct Stake {
        uint256 amount;
        uint256 stakedAt;
        uint256 rewardDebt;
    }

    mapping(address => Stake) public stakes;
    mapping(address => uint256) public userRewardPerTokenPaid;
    mapping(address => uint256) public rewards;

    // Events
    event Staked(address indexed user, uint256 amount);
    event Withdrawn(address indexed user, uint256 amount);
    event RewardPaid(address indexed user, uint256 reward);
    event RewardRateUpdated(uint256 newRate);

    constructor(address _brettToken, uint256 _rewardRate) {
        require(_brettToken != address(0), "Invalid token address");
        brettToken = IERC20(_brettToken);
        rewardRate = _rewardRate;
        lastUpdateTime = block.timestamp;
    }

    // Update reward calculations
    modifier updateReward(address account) {
        rewardPerTokenStored = rewardPerToken();
        lastUpdateTime = lastTimeRewardApplicable();
        if (account != address(0)) {
            rewards[account] = earned(account);
            userRewardPerTokenPaid[account] = rewardPerTokenStored;
        }
        _;
    }

    // Get last applicable time for rewards
    function lastTimeRewardApplicable() public view returns (uint256) {
        return block.timestamp;
    }

    // Calculate reward per token
    function rewardPerToken() public view returns (uint256) {
        if (totalSupply == 0) {
            return rewardPerTokenStored;
        }
        return
            rewardPerTokenStored +
            (((lastTimeRewardApplicable() - lastUpdateTime) * rewardRate * 1e18) / totalSupply);
    }

    // Calculate earned rewards for an account
    function earned(address account) public view returns (uint256) {
        return
            ((stakes[account].amount *
                (rewardPerToken() - userRewardPerTokenPaid[account])) / 1e18) +
            rewards[account];
    }

    // Stake tokens
    function stake(uint256 amount) external nonReentrant updateReward(msg.sender) {
        require(amount > 0, "Cannot stake 0");
        require(
            brettToken.balanceOf(msg.sender) >= amount,
            "Insufficient token balance"
        );

        // Update stake
        if (stakes[msg.sender].amount > 0) {
            stakes[msg.sender].amount += amount;
        } else {
            stakes[msg.sender] = Stake(amount, block.timestamp, 0);
        }

        totalSupply += amount;
        stakes[msg.sender].rewardDebt = (stakes[msg.sender].amount * rewardPerTokenStored) / 1e18;

        // Transfer tokens from user to contract
        brettToken.safeTransferFrom(msg.sender, address(this), amount);

        emit Staked(msg.sender, amount);
    }

    // Withdraw staked tokens
    function withdraw(uint256 amount) public nonReentrant updateReward(msg.sender) {
        require(amount > 0, "Cannot withdraw 0");
        require(stakes[msg.sender].amount >= amount, "Insufficient stake");

        // Check if staking period has ended
        require(
            block.timestamp >= stakes[msg.sender].stakedAt + STAKING_PERIOD,
            "Staking period not ended"
        );

        totalSupply -= amount;
        stakes[msg.sender].amount -= amount;
        stakes[msg.sender].rewardDebt = (stakes[msg.sender].amount * rewardPerTokenStored) / 1e18;

        // Transfer tokens back to user
        brettToken.safeTransfer(msg.sender, amount);

        emit Withdrawn(msg.sender, amount);
    }

    // Claim rewards
    function getReward() public nonReentrant updateReward(msg.sender) {
        uint256 reward = rewards[msg.sender];
        if (reward > 0) {
            rewards[msg.sender] = 0;
            brettToken.safeTransfer(msg.sender, reward);
            emit RewardPaid(msg.sender, reward);
        }
    }

    // Exit (withdraw all and claim rewards)
    function exit() external {
        withdraw(stakes[msg.sender].amount);
        getReward();
    }

    // Update reward rate (owner only)
    function setRewardRate(uint256 _rewardRate) external onlyOwner {
        rewardRate = _rewardRate;
        emit RewardRateUpdated(_rewardRate);
    }

    // Recover ERC20 tokens (owner only)
    function recoverERC20(address tokenAddress, uint256 tokenAmount) external onlyOwner {
        require(tokenAddress != address(brettToken), "Cannot withdraw staking token");
        IERC20(tokenAddress).safeTransfer(owner(), tokenAmount);
    }
}
```
