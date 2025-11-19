"""
Generated Code Metadata:
========================
Original URL: https://bafybeif5xdzxzkk6hpdngckqqt4qfejabreu6fkzi4rwsnuk733woz2spu.ipfs.dweb.link
Prompt: "Generate code for a liquidity provider interface that allows users to claim bonus interest shares on their positions, up to 4%, as described in the Silo Finance documentation."
Generated: DETERMINISTIC_80ba5815300eed60
Batch ID: 20250622_205111
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

interface ISilo {
    function balanceOf(address account) external view returns (uint256);
    function totalSupply() external view returns (uint256);
    function asset() external view returns (address);
}

contract LiquidityProviderBonus is Ownable, ReentrancyGuard {
    IERC20 public rewardToken;
    ISilo public silo;
    uint256 public constant MAX_BONUS = 400; // 4% in basis points
    uint256 public bonusRate; // in basis points (1% = 100)
    uint256 public lastUpdateTime;
    uint256 public rewardPerTokenStored;
    uint256 public totalRewardsDistributed;

    mapping(address => uint256) public userRewardPerTokenPaid;
    mapping(address => uint256) public rewards;

    event BonusRateUpdated(uint256 newRate);
    event RewardPaid(address indexed user, uint256 reward);
    event RewardsAdded(uint256 amount);

    constructor(address _silo, address _rewardToken, uint256 _initialBonusRate) {
        require(_silo != address(0), "Invalid silo address");
        require(_rewardToken != address(0), "Invalid reward token address");
        require(_initialBonusRate <= MAX_BONUS, "Bonus rate too high");

        silo = ISilo(_silo);
        rewardToken = IERC20(_rewardToken);
        bonusRate = _initialBonusRate;
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
        if (silo.totalSupply() == 0) {
            return rewardPerTokenStored;
        }
        return rewardPerTokenStored + (
            (block.timestamp - lastUpdateTime) * bonusRate * 1e18 / 10000 / 365 days
        );
    }

    function earned(address account) public view returns (uint256) {
        return (silo.balanceOf(account) * 
               (rewardPerToken() - userRewardPerTokenPaid[account]) / 1e18) + 
               rewards[account];
    }

    function claimReward() external nonReentrant updateReward(msg.sender) {
        uint256 reward = rewards[msg.sender];
        if (reward > 0) {
            rewards[msg.sender] = 0;
            totalRewardsDistributed += reward;
            require(rewardToken.transfer(msg.sender, reward), "Transfer failed");
            emit RewardPaid(msg.sender, reward);
        }
    }

    function setBonusRate(uint256 newRate) external onlyOwner {
        require(newRate <= MAX_BONUS, "Bonus rate too high");
        bonusRate = newRate;
        emit BonusRateUpdated(newRate);
    }

    function addRewards(uint256 amount) external onlyOwner {
        require(amount > 0, "Cannot add 0 rewards");
        require(rewardToken.transferFrom(msg.sender, address(this), amount), "Transfer failed");
        rewardPerTokenStored = rewardPerToken();
        lastUpdateTime = block.timestamp;
        emit RewardsAdded(amount);
    }

    function recoverERC20(address tokenAddress, uint256 amount) external onlyOwner {
        require(tokenAddress != address(rewardToken), "Cannot withdraw reward token");
        IERC20(tokenAddress).transfer(owner(), amount);
    }
}
```
