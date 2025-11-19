"""
Generated Code Metadata:
========================
Original URL: https://floki-reward.com
Prompt: Generate Solidity code for creating a staking contract that rewards users with Floki's sister token, TOKEN, when they stake $FLOKI tokens.
Generated: DETERMINISTIC_b899b318d9c5ee0c
Batch ID: 20250612_151624
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
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title Floki Staking Contract
 * @author [Your Name]
 * @notice This contract allows users to stake $FLOKI tokens and earn TOKEN rewards.
 */
contract FlokiStakingContract is ReentrancyGuard {
    using SafeMath for uint256;
    using SafeERC20 for IERC20;

    // Mapping of user staking balances
    mapping(address => uint256) public stakingBalances;

    // Mapping of user reward debt
    mapping(address => uint256) public rewardDebt;

    // Total staking balance
    uint256 public totalStakingBalance;

    // Accrued reward per share
    uint256 public accRewardPerShare;

    // Reward rate per block
    uint256 public rewardRate;

    // TOKEN reward contract
    IERC20 public tokenReward;

    // $FLOKI token contract
    IERC20 public flokiToken;

    // Flag to check if contract is initialized
    bool public initialized;

    /**
     * @dev Emitted when a user stakes $FLOKI tokens
     * @param user User address
     * @param amount Staked amount
     */
    event Staked(address indexed user, uint256 amount);

    /**
     * @dev Emitted when a user unstakes $FLOKI tokens
     * @param user User address
     * @param amount Unstaked amount
     */
    event Unstaked(address indexed user, uint256 amount);

    /**
     * @dev Emitted when rewards are claimed
     * @param user User address
     * @param amount Claimed amount
     */
    event RewardsClaimed(address indexed user, uint256 amount);

    /**
     * @dev Initializes the contract
     * @param _flokiToken $FLOKI token contract address
     * @param _tokenReward TOKEN reward contract address
     * @param _rewardRate Reward rate per block
     */
    function initialize(
        address _flokiToken,
        address _tokenReward,
        uint256 _rewardRate
    ) public {
        require(!initialized, "Contract already initialized");
        require(_flokiToken != address(0), "Invalid $FLOKI token address");
        require(_tokenReward != address(0), "Invalid TOKEN reward address");
        require(_rewardRate > 0, "Reward rate must be greater than 0");

        flokiToken = IERC20(_flokiToken);
        tokenReward = IERC20(_tokenReward);
        rewardRate = _rewardRate;

        initialized = true;
    }

    /**
     * @dev Stakes $FLOKI tokens
     * @param amount Staked amount
     */
    function stake(uint256 amount) public nonReentrant {
        require(amount > 0, "Staked amount must be greater than 0");
        require(flokiToken.balanceOf(msg.sender) >= amount, "Insufficient $FLOKI token balance");

        flokiToken.safeTransferFrom(msg.sender, address(this), amount);

        stakingBalances[msg.sender] = stakingBalances[msg.sender].add(amount);
        totalStakingBalance = totalStakingBalance.add(amount);

        updateRewardDebt(msg.sender);

        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Unstakes $FLOKI tokens
     * @param amount Unstaked amount
     */
    function unstake(uint256 amount) public nonReentrant {
        require(amount > 0, "Unstaked amount must be greater than 0");
        require(stakingBalances[msg.sender] >= amount, "Insufficient staked balance");

        stakingBalances[msg.sender] = stakingBalances[msg.sender].sub(amount);
        totalStakingBalance = totalStakingBalance.sub(amount);

        flokiToken.safeTransfer(msg.sender, amount);

        updateRewardDebt(msg.sender);

        emit Unstaked(msg.sender, amount);
    }

    /**
     * @dev Claims TOKEN rewards
     */
    function claimRewards() public nonReentrant {
        uint256 rewards = getRewardAmount(msg.sender);

        if (rewards > 0) {
            rewardDebt[msg.sender] = 0;
            tokenReward.safeTransfer(msg.sender, rewards);

            emit RewardsClaimed(msg.sender, rewards);
        }
    }

    /**
     * @dev Updates reward debt for a user
     * @param user User address
     */
    function updateRewardDebt(address user) internal {
        if (totalStakingBalance == 0) return;

        uint256 pendingReward = getPendingReward();
        accRewardPerShare = accRewardPerShare.add(pendingReward.mul(1e18).div(totalStakingBalance));

        rewardDebt[user] = stakingBalances[user].mul(accRewardPerShare).div(1e18);
    }

    /**
     * @dev Gets pending reward
     * @return Pending reward amount
     */
    function getPendingReward() internal view returns (uint256) {
        return rewardRate;
    }

    /**
     * @dev Gets reward amount for a user
     * @param user User address
     * @return Reward amount
     */
    function getRewardAmount(address user) public view returns (uint256) {
        uint256 userRewardDebt = rewardDebt[user];
        uint256 userStakingBalance = stakingBalances[user];

        if (userStakingBalance == 0) return 0;

        uint256 currentRewardPerShare = accRewardPerShare;
        uint256 pendingReward = getPendingReward();
        currentRewardPerShare = currentRewardPerShare.add(pendingReward.mul(1e18).div(totalStakingBalance));

        uint256 userReward = userStakingBalance.mul(currentRewardPerShare).div(1e18).sub(userRewardDebt);

        return userReward;
    }
}
```
