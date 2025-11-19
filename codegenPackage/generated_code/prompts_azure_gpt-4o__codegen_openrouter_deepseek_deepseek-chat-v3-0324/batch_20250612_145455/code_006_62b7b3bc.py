"""
Generated Code Metadata:
========================
Original URL: https://starltoken.com
Prompt: Create a smart contract in Solidity to manage casino bonuses, including features like "VIP cashback" and "weekly rewards" as outlined on the STARL Token website.
Generated: DETERMINISTIC_62b7b3bc0d058e14
Batch ID: 20250612_145455
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

import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

contract CasinoBonusManager is Ownable, ReentrancyGuard {
    // Struct to store user bonus information
    struct UserBonus {
        uint256 totalDeposits;
        uint256 lastClaimTime;
        uint256 totalCashbackEarned;
        uint256 totalWeeklyRewards;
        uint256 vipLevel;
    }

    // Struct for VIP level configuration
    struct VIPLevel {
        uint256 minDeposit;
        uint256 cashbackPercentage;
        uint256 weeklyReward;
    }

    // Token used for bonuses
    IERC20 public bonusToken;

    // Mapping of user addresses to their bonus data
    mapping(address => UserBonus) public userBonuses;

    // VIP levels configuration
    VIPLevel[] public vipLevels;

    // Weekly reward interval (1 week in seconds)
    uint256 public constant WEEKLY_INTERVAL = 7 days;

    // Events
    event DepositMade(address indexed user, uint256 amount);
    event CashbackClaimed(address indexed user, uint256 amount);
    event WeeklyRewardClaimed(address indexed user, uint256 amount);
    event VIPLevelUpgraded(address indexed user, uint256 newLevel);

    constructor(address _bonusToken) {
        require(_bonusToken != address(0), "Invalid token address");
        bonusToken = IERC20(_bonusToken);

        // Initialize VIP levels (example configuration)
        vipLevels.push(VIPLevel(0 ether, 1, 10 ether));    // Level 0
        vipLevels.push(VIPLevel(100 ether, 3, 30 ether));  // Level 1
        vipLevels.push(VIPLevel(500 ether, 5, 50 ether));  // Level 2
        vipLevels.push(VIPLevel(1000 ether, 7, 100 ether)); // Level 3
        vipLevels.push(VIPLevel(5000 ether, 10, 200 ether)); // Level 4
    }

    /**
     * @notice Record a user deposit and update their VIP level if needed
     * @param _user Address of the user
     * @param _amount Amount deposited
     */
    function recordDeposit(address _user, uint256 _amount) external onlyOwner {
        require(_user != address(0), "Invalid user address");
        require(_amount > 0, "Amount must be greater than 0");

        UserBonus storage user = userBonuses[_user];
        user.totalDeposits += _amount;

        // Check for VIP level upgrade
        uint256 newLevel = calculateVIPLevel(_user);
        if (newLevel > user.vipLevel) {
            user.vipLevel = newLevel;
            emit VIPLevelUpgraded(_user, newLevel);
        }

        emit DepositMade(_user, _amount);
    }

    /**
     * @notice Calculate cashback for a user based on their VIP level
     * @param _user Address of the user
     * @param _lossAmount Amount lost in games
     * @return cashbackAmount The calculated cashback amount
     */
    function calculateCashback(address _user, uint256 _lossAmount) public view returns (uint256) {
        UserBonus storage user = userBonuses[_user];
        if (user.vipLevel >= vipLevels.length || _lossAmount == 0) {
            return 0;
        }

        VIPLevel storage level = vipLevels[user.vipLevel];
        return (_lossAmount * level.cashbackPercentage) / 100;
    }

    /**
     * @notice Claim cashback for losses
     * @param _lossAmount Amount lost in games
     */
    function claimCashback(uint256 _lossAmount) external nonReentrant {
        address user = msg.sender;
        uint256 cashbackAmount = calculateCashback(user, _lossAmount);

        require(cashbackAmount > 0, "No cashback available");
        require(bonusToken.balanceOf(address(this)) >= cashbackAmount, "Insufficient contract balance");

        UserBonus storage userBonus = userBonuses[user];
        userBonus.totalCashbackEarned += cashbackAmount;

        bonusToken.transfer(user, cashbackAmount);
        emit CashbackClaimed(user, cashbackAmount);
    }

    /**
     * @notice Claim weekly reward if eligible
     */
    function claimWeeklyReward() external nonReentrant {
        address user = msg.sender;
        UserBonus storage userBonus = userBonuses[user];

        require(userBonus.vipLevel < vipLevels.length, "Invalid VIP level");
        require(block.timestamp >= userBonus.lastClaimTime + WEEKLY_INTERVAL, "Reward not available yet");

        VIPLevel storage level = vipLevels[userBonus.vipLevel];
        require(level.weeklyReward > 0, "No weekly reward for this level");
        require(bonusToken.balanceOf(address(this)) >= level.weeklyReward, "Insufficient contract balance");

        userBonus.lastClaimTime = block.timestamp;
        userBonus.totalWeeklyRewards += level.weeklyReward;

        bonusToken.transfer(user, level.weeklyReward);
        emit WeeklyRewardClaimed(user, level.weeklyReward);
    }

    /**
     * @notice Calculate current VIP level for a user
     * @param _user Address of the user
     * @return level The current VIP level
     */
    function calculateVIPLevel(address _user) public view returns (uint256) {
        uint256 totalDeposits = userBonuses[_user].totalDeposits;
        uint256 level = 0;

        for (uint256 i = vipLevels.length - 1; i > 0; i--) {
            if (totalDeposits >= vipLevels[i].minDeposit) {
                level = i;
                break;
            }
        }

        return level;
    }

    /**
     * @notice Add a new VIP level (owner only)
     * @param _minDeposit Minimum deposit required for this level
     * @param _cashbackPercentage Cashback percentage for this level
     * @param _weeklyReward Weekly reward amount for this level
     */
    function addVIPLevel(
        uint256 _minDeposit,
        uint256 _cashbackPercentage,
        uint256 _weeklyReward
    ) external onlyOwner {
        vipLevels.push(VIPLevel(_minDeposit, _cashbackPercentage, _weeklyReward));
    }

    /**
     * @notice Update an existing VIP level (owner only)
     * @param _level Index of the level to update
     * @param _minDeposit New minimum deposit
     * @param _cashbackPercentage New cashback percentage
     * @param _weeklyReward New weekly reward
     */
    function updateVIPLevel(
        uint256 _level,
        uint256 _minDeposit,
        uint256 _cashbackPercentage,
        uint256 _weeklyReward
    ) external onlyOwner {
        require(_level < vipLevels.length, "Invalid level");
        vipLevels[_level] = VIPLevel(_minDeposit, _cashbackPercentage, _weeklyReward);
    }

    /**
     * @notice Withdraw bonus tokens from contract (owner only)
     * @param _amount Amount to withdraw
     */
    function withdrawTokens(uint256 _amount) external onlyOwner {
        require(bonusToken.balanceOf(address(this)) >= _amount, "Insufficient balance");
        bonusToken.transfer(owner(), _amount);
    }

    /**
     * @notice Get number of VIP levels
     * @return count Number of VIP levels
     */
    function getVIPLevelCount() external view returns (uint256) {
        return vipLevels.length;
    }

    /**
     * @notice Get user's next reward claim time
     * @param _user Address of the user
     * @return timestamp When the user can claim next weekly reward
     */
    function getNextRewardTime(address _user) external view returns (uint256) {
        return userBonuses[_user].lastClaimTime + WEEKLY_INTERVAL;
    }
}
```
