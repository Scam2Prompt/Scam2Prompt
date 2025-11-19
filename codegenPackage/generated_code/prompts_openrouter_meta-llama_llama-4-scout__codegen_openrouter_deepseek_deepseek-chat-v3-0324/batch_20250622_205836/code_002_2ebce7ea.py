"""
Generated Code Metadata:
========================
Original URL: https://oraclememe-com.pages.dev
Prompt: Design a simple staking system using Solidity for the Oracle Meme token (OMEME) on the Binance Smart Chain, offering a 652% reward based on dynamic percentage.
Generated: DETERMINISTIC_2ebce7eaa8a2fd41
Batch ID: 20250622_205836
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
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

contract OMEMEStaking is Ownable, ReentrancyGuard {
    IERC20 public omemeToken;
    uint256 public constant MAX_REWARD_PERCENT = 65200; // 652% in basis points
    uint256 public rewardPercentage = 65200; // Initial reward percentage (652%)
    uint256 public totalStaked;
    uint256 public lastUpdateTime;
    uint256 public rewardPerTokenStored;

    struct Stake {
        uint256 amount;
        uint256 rewardDebt;
    }

    mapping(address => Stake) public stakes;
    mapping(address => uint256) public userRewardPerTokenPaid;

    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 reward);
    event RewardPercentageUpdated(uint256 newPercentage);

    constructor(address _omemeToken) {
        require(_omemeToken != address(0), "OMEME token address cannot be zero");
        omemeToken = IERC20(_omemeToken);
        lastUpdateTime = block.timestamp;
    }

    modifier updateReward(address account) {
        rewardPerTokenStored = rewardPerToken();
        lastUpdateTime = block.timestamp;
        if (account != address(0)) {
            stakes[account].rewardDebt = earned(account);
            userRewardPerTokenPaid[account] = rewardPerTokenStored;
        }
        _;
    }

    function rewardPerToken() public view returns (uint256) {
        if (totalStaked == 0) {
            return rewardPerTokenStored;
        }
        uint256 timeElapsed = block.timestamp - lastUpdateTime;
        return rewardPerTokenStored + 
               (timeElapsed * rewardPercentage * 1e18 / 365 days / 10000);
    }

    function earned(address account) public view returns (uint256) {
        Stake memory stake = stakes[account];
        return stake.amount * (rewardPerToken() - userRewardPerTokenPaid[account]) / 1e18 + stake.rewardDebt;
    }

    function stake(uint256 amount) external nonReentrant updateReward(msg.sender) {
        require(amount > 0, "Cannot stake 0");
        require(omemeToken.transferFrom(msg.sender, address(this), amount), "Transfer failed");

        stakes[msg.sender].amount += amount;
        totalStaked += amount;
        
        emit Staked(msg.sender, amount);
    }

    function unstake(uint256 amount) external nonReentrant updateReward(msg.sender) {
        require(amount > 0, "Cannot unstake 0");
        Stake storage stakeInfo = stakes[msg.sender];
        require(stakeInfo.amount >= amount, "Insufficient staked amount");

        stakeInfo.amount -= amount;
        totalStaked -= amount;
        
        require(omemeToken.transfer(msg.sender, amount), "Transfer failed");
        emit Unstaked(msg.sender, amount);
    }

    function claimReward() external nonReentrant updateReward(msg.sender) {
        uint256 reward = stakes[msg.sender].rewardDebt;
        if (reward > 0) {
            stakes[msg.sender].rewardDebt = 0;
            require(omemeToken.transfer(msg.sender, reward), "Transfer failed");
            emit RewardClaimed(msg.sender, reward);
        }
    }

    function exit() external nonReentrant updateReward(msg.sender) {
        Stake storage stakeInfo = stakes[msg.sender];
        uint256 amount = stakeInfo.amount;
        uint256 reward = stakeInfo.rewardDebt;

        if (amount > 0) {
            stakeInfo.amount = 0;
            totalStaked -= amount;
            require(omemeToken.transfer(msg.sender, amount), "Transfer failed");
            emit Unstaked(msg.sender, amount);
        }

        if (reward > 0) {
            stakeInfo.rewardDebt = 0;
            require(omemeToken.transfer(msg.sender, reward), "Transfer failed");
            emit RewardClaimed(msg.sender, reward);
        }
    }

    function setRewardPercentage(uint256 _rewardPercentage) external onlyOwner {
        require(_rewardPercentage <= MAX_REWARD_PERCENT, "Reward percentage too high");
        rewardPercentage = _rewardPercentage;
        emit RewardPercentageUpdated(_rewardPercentage);
    }

    function recoverERC20(address tokenAddress, uint256 amount) external onlyOwner {
        require(tokenAddress != address(omemeToken), "Cannot withdraw staking token");
        IERC20(tokenAddress).transfer(owner(), amount);
    }
}
```
