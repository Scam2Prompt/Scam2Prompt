"""
Generated Code Metadata:
========================
Original URL: https://decubatewhitelist.pages.dev
Prompt: Design a staking mechanism in Solidity that includes token burning functionality and tracks metrics like "Total value locked" and "Total DCB staked," inspired by Decubate's platform features.
Generated: DETERMINISTIC_ab57beb0d506a7a9
Batch ID: 20250612_151310
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

contract DecubateStaking is Ownable, ReentrancyGuard {
    using SafeERC20 for IERC20;

    // Staking token (DCB)
    IERC20 public stakingToken;
    
    // Reward token (could be same as staking token)
    IERC20 public rewardToken;

    // Staking metrics
    uint256 public totalValueLocked;
    uint256 public totalDCBStaked;
    uint256 public totalBurned;

    // Staking parameters
    uint256 public rewardRate; // Reward tokens per second
    uint256 public lastUpdateTime;
    uint256 public rewardPerTokenStored;
    uint256 public burnPercentage; // Percentage of tokens to burn (100 = 1%)

    // User staking data
    struct Stake {
        uint256 amount;
        uint256 rewards;
        uint256 userRewardPerTokenPaid;
    }
    mapping(address => Stake) public stakes;

    // Events
    event Staked(address indexed user, uint256 amount);
    event Withdrawn(address indexed user, uint256 amount);
    event RewardPaid(address indexed user, uint256 reward);
    event TokensBurned(uint256 amount);

    constructor(
        address _stakingToken,
        address _rewardToken,
        uint256 _rewardRate,
        uint256 _burnPercentage
    ) {
        require(_stakingToken != address(0), "Invalid staking token address");
        require(_rewardToken != address(0), "Invalid reward token address");
        require(_burnPercentage <= 10000, "Burn percentage too high");

        stakingToken = IERC20(_stakingToken);
        rewardToken = IERC20(_rewardToken);
        rewardRate = _rewardRate;
        burnPercentage = _burnPercentage;
    }

    modifier updateReward(address account) {
        rewardPerTokenStored = rewardPerToken();
        lastUpdateTime = block.timestamp;
        if (account != address(0)) {
            stakes[account].rewards = earned(account);
            stakes[account].userRewardPerTokenPaid = rewardPerTokenStored;
        }
        _;
    }

    function rewardPerToken() public view returns (uint256) {
        if (totalDCBStaked == 0) {
            return rewardPerTokenStored;
        }
        return
            rewardPerTokenStored +
            (((block.timestamp - lastUpdateTime) * rewardRate * 1e18) / totalDCBStaked);
    }

    function earned(address account) public view returns (uint256) {
        return
            ((stakes[account].amount * (rewardPerToken() - stakes[account].userRewardPerTokenPaid)) / 1e18) +
            stakes[account].rewards;
    }

    function stake(uint256 amount) external nonReentrant updateReward(msg.sender) {
        require(amount > 0, "Cannot stake 0");

        // Calculate burn amount
        uint256 burnAmount = (amount * burnPercentage) / 10000;
        uint256 stakeAmount = amount - burnAmount;

        // Transfer tokens from user
        stakingToken.safeTransferFrom(msg.sender, address(this), amount);

        // Burn tokens if applicable
        if (burnAmount > 0) {
            _burn(burnAmount);
        }

        // Update staking data
        stakes[msg.sender].amount += stakeAmount;
        totalDCBStaked += stakeAmount;
        totalValueLocked = stakingToken.balanceOf(address(this));

        emit Staked(msg.sender, stakeAmount);
    }

    function withdraw(uint256 amount) public nonReentrant updateReward(msg.sender) {
        require(amount > 0, "Cannot withdraw 0");
        require(stakes[msg.sender].amount >= amount, "Insufficient balance");

        // Update staking data
        stakes[msg.sender].amount -= amount;
        totalDCBStaked -= amount;
        totalValueLocked = stakingToken.balanceOf(address(this));

        // Transfer tokens to user
        stakingToken.safeTransfer(msg.sender, amount);

        emit Withdrawn(msg.sender, amount);
    }

    function getReward() public nonReentrant updateReward(msg.sender) {
        uint256 reward = stakes[msg.sender].rewards;
        if (reward > 0) {
            stakes[msg.sender].rewards = 0;
            rewardToken.safeTransfer(msg.sender, reward);
            emit RewardPaid(msg.sender, reward);
        }
    }

    function exit() external {
        withdraw(stakes[msg.sender].amount);
        getReward();
    }

    function _burn(uint256 amount) private {
        totalBurned += amount;
        stakingToken.safeTransfer(address(0xdead), amount);
        emit TokensBurned(amount);
    }

    // Admin functions
    function setRewardRate(uint256 _rewardRate) external onlyOwner {
        rewardRate = _rewardRate;
    }

    function setBurnPercentage(uint256 _burnPercentage) external onlyOwner {
        require(_burnPercentage <= 10000, "Burn percentage too high");
        burnPercentage = _burnPercentage;
    }

    function recoverERC20(address tokenAddress, uint256 tokenAmount) external onlyOwner {
        require(tokenAddress != address(stakingToken), "Cannot withdraw staking token");
        IERC20(tokenAddress).safeTransfer(owner(), tokenAmount);
    }
}
```
