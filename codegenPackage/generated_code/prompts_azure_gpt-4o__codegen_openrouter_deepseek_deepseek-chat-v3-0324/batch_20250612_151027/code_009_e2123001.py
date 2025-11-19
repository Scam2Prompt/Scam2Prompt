"""
Generated Code Metadata:
========================
Original URL: https://nyanheroes-d2u.pages.dev
Prompt: Write a Solidity contract for managing token rewards and referrals, inspired by the Nyan Heroes platform.
Generated: DETERMINISTIC_e21230011e2b56be
Batch ID: 20250612_151027
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

contract RewardReferralSystem is Ownable, ReentrancyGuard {
    IERC20 public rewardToken;

    // Reward configuration
    uint256 public rewardAmount = 100 * (10 ** 18); // Default reward amount
    uint256 public referralRewardPercentage = 10; // 10% of rewardAmount
    uint256 public claimCooldown = 7 days;

    // User data
    struct UserInfo {
        address referrer;
        uint256 lastClaimTime;
        uint256 totalEarned;
        uint256 totalReferrals;
        uint256 referralEarnings;
        bool isRegistered;
    }

    mapping(address => UserInfo) public users;
    mapping(address => bool) public operators;

    // Events
    event Registered(address indexed user, address indexed referrer);
    event RewardClaimed(address indexed user, uint256 amount);
    event ReferralReward(address indexed referrer, address indexed referee, uint256 amount);
    event RewardAmountUpdated(uint256 newAmount);
    event ReferralPercentageUpdated(uint256 newPercentage);
    event OperatorUpdated(address indexed operator, bool status);

    modifier onlyOperator() {
        require(operators[msg.sender] || msg.sender == owner(), "Not authorized");
        _;
    }

    constructor(IERC20 _rewardToken) {
        rewardToken = _rewardToken;
        operators[msg.sender] = true;
    }

    /**
     * @dev Register a user with an optional referrer
     * @param referrer Address of the referrer (can be zero address)
     */
    function register(address referrer) external {
        require(!users[msg.sender].isRegistered, "Already registered");
        
        if (referrer != address(0) && referrer != msg.sender) {
            require(users[referrer].isRegistered, "Referrer not registered");
            users[msg.sender].referrer = referrer;
            users[referrer].totalReferrals += 1;
        }

        users[msg.sender].isRegistered = true;
        emit Registered(msg.sender, referrer);
    }

    /**
     * @dev Claim rewards for the caller
     */
    function claimRewards() external nonReentrant {
        UserInfo storage user = users[msg.sender];
        require(user.isRegistered, "Not registered");
        require(block.timestamp >= user.lastClaimTime + claimCooldown, "Claim cooldown active");

        uint256 amount = rewardAmount;
        require(rewardToken.balanceOf(address(this)) >= amount, "Insufficient contract balance");

        user.lastClaimTime = block.timestamp;
        user.totalEarned += amount;

        // Transfer reward to user
        rewardToken.transfer(msg.sender, amount);
        emit RewardClaimed(msg.sender, amount);

        // Handle referral reward if applicable
        if (user.referrer != address(0)) {
            uint256 referralAmount = (amount * referralRewardPercentage) / 100;
            if (rewardToken.balanceOf(address(this)) >= referralAmount) {
                users[user.referrer].referralEarnings += referralAmount;
                rewardToken.transfer(user.referrer, referralAmount);
                emit ReferralReward(user.referrer, msg.sender, referralAmount);
            }
        }
    }

    /**
     * @dev Admin function to update reward amount
     * @param newAmount New reward amount in token units
     */
    function setRewardAmount(uint256 newAmount) external onlyOwner {
        rewardAmount = newAmount;
        emit RewardAmountUpdated(newAmount);
    }

    /**
     * @dev Admin function to update referral percentage
     * @param newPercentage New referral percentage (0-100)
     */
    function setReferralPercentage(uint256 newPercentage) external onlyOwner {
        require(newPercentage <= 100, "Invalid percentage");
        referralRewardPercentage = newPercentage;
        emit ReferralPercentageUpdated(newPercentage);
    }

    /**
     * @dev Admin function to update claim cooldown
     * @param newCooldown New cooldown in seconds
     */
    function setClaimCooldown(uint256 newCooldown) external onlyOwner {
        claimCooldown = newCooldown;
    }

    /**
     * @dev Admin function to add/remove operators
     * @param operator Address to update
     * @param status New operator status
     */
    function setOperator(address operator, bool status) external onlyOwner {
        operators[operator] = status;
        emit OperatorUpdated(operator, status);
    }

    /**
     * @dev Admin function to withdraw tokens from contract
     * @param amount Amount to withdraw
     */
    function withdrawTokens(uint256 amount) external onlyOwner {
        require(rewardToken.balanceOf(address(this)) >= amount, "Insufficient balance");
        rewardToken.transfer(owner(), amount);
    }

    /**
     * @dev Operator function to manually reward a user
     * @param user Address to reward
     * @param amount Amount to reward
     */
    function manualReward(address user, uint256 amount) external onlyOperator {
        require(users[user].isRegistered, "User not registered");
        require(rewardToken.balanceOf(address(this)) >= amount, "Insufficient contract balance");

        rewardToken.transfer(user, amount);
        users[user].totalEarned += amount;
        emit RewardClaimed(user, amount);
    }
}
```
