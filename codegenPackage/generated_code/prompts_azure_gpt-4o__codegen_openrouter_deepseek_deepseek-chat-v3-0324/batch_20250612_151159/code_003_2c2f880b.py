"""
Generated Code Metadata:
========================
Original URL: https://web-wienerdog.pages.dev
Prompt: Develop a staking mechanism in Solidity that allows users to stake WienerAI ($WAI) tokens and earn rewards with an annual percentage yield (APY) of 120%.
Generated: DETERMINISTIC_2c2f880b84437e5c
Batch ID: 20250612_151159
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

contract WienerAIStaking is ReentrancyGuard, Ownable {
    using SafeERC20 for IERC20;

    // Constants
    uint256 public constant APY = 120; // 120% APY
    uint256 public constant SECONDS_IN_YEAR = 365 days;
    uint256 public constant REWARD_PRECISION = 1e18;

    // State variables
    IERC20 public stakingToken;
    uint256 public totalStaked;
    uint256 public lastUpdateTime;
    uint256 public rewardPerTokenStored;

    // User stakes
    struct Stake {
        uint256 amount;
        uint256 rewardDebt;
    }
    mapping(address => Stake) public stakes;

    // Events
    event Staked(address indexed user, uint256 amount);
    event Withdrawn(address indexed user, uint256 amount);
    event RewardPaid(address indexed user, uint256 reward);
    event EmergencyWithdraw(address indexed user, uint256 amount);

    constructor(address _stakingToken) {
        stakingToken = IERC20(_stakingToken);
        lastUpdateTime = block.timestamp;
    }

    // Update reward calculations
    modifier updateReward(address account) {
        rewardPerTokenStored = rewardPerToken();
        lastUpdateTime = block.timestamp;
        if (account != address(0)) {
            stakes[account].rewardDebt = earned(account);
        }
        _;
    }

    // Calculate reward per token
    function rewardPerToken() public view returns (uint256) {
        if (totalStaked == 0) {
            return rewardPerTokenStored;
        }
        uint256 timeElapsed = block.timestamp - lastUpdateTime;
        uint256 reward = (timeElapsed * APY * REWARD_PRECISION) / (SECONDS_IN_YEAR * 100);
        return rewardPerTokenStored + (reward * REWARD_PRECISION) / totalStaked;
    }

    // Calculate earned rewards for an account
    function earned(address account) public view returns (uint256) {
        Stake memory stake = stakes[account];
        uint256 currentRewardPerToken = rewardPerToken();
        return stake.amount * (currentRewardPerToken - stake.rewardDebt) / REWARD_PRECISION;
    }

    // Stake tokens
    function stake(uint256 amount) external nonReentrant updateReward(msg.sender) {
        require(amount > 0, "Cannot stake 0");
        
        stakes[msg.sender].amount += amount;
        stakes[msg.sender].rewardDebt = stakes[msg.sender].amount * rewardPerTokenStored / REWARD_PRECISION;
        totalStaked += amount;
        
        stakingToken.safeTransferFrom(msg.sender, address(this), amount);
        emit Staked(msg.sender, amount);
    }

    // Withdraw staked tokens and claim rewards
    function withdraw(uint256 amount) public nonReentrant updateReward(msg.sender) {
        require(amount > 0, "Cannot withdraw 0");
        require(stakes[msg.sender].amount >= amount, "Insufficient balance");
        
        _claimRewards();
        
        stakes[msg.sender].amount -= amount;
        stakes[msg.sender].rewardDebt = stakes[msg.sender].amount * rewardPerTokenStored / REWARD_PRECISION;
        totalStaked -= amount;
        
        stakingToken.safeTransfer(msg.sender, amount);
        emit Withdrawn(msg.sender, amount);
    }

    // Claim rewards without withdrawing staked tokens
    function claimRewards() public nonReentrant updateReward(msg.sender) {
        _claimRewards();
    }

    // Internal function to claim rewards
    function _claimRewards() internal {
        uint256 reward = earned(msg.sender);
        if (reward > 0) {
            stakes[msg.sender].rewardDebt = stakes[msg.sender].amount * rewardPerTokenStored / REWARD_PRECISION;
            stakingToken.safeTransfer(msg.sender, reward);
            emit RewardPaid(msg.sender, reward);
        }
    }

    // Emergency withdraw without claiming rewards
    function emergencyWithdraw() external nonReentrant {
        uint256 amount = stakes[msg.sender].amount;
        require(amount > 0, "Nothing to withdraw");
        
        totalStaked -= amount;
        stakes[msg.sender].amount = 0;
        stakes[msg.sender].rewardDebt = 0;
        
        stakingToken.safeTransfer(msg.sender, amount);
        emit EmergencyWithdraw(msg.sender, amount);
    }

    // Recover ERC20 tokens sent by mistake
    function recoverERC20(address tokenAddress, uint256 tokenAmount) external onlyOwner {
        require(tokenAddress != address(stakingToken), "Cannot withdraw staking token");
        IERC20(tokenAddress).safeTransfer(owner(), tokenAmount);
    }
}
```
