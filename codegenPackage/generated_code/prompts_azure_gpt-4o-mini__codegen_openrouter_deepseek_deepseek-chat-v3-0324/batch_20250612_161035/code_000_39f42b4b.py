"""
Generated Code Metadata:
========================
Original URL: https://zeek.social
Prompt: Generate code to integrate a referral system in a Web3 SocialFi Dapp similar to Zeek Network.
Generated: DETERMINISTIC_39f42b4b0e608479
Batch ID: 20250612_161035
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
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

contract ReferralSystem is Ownable, ReentrancyGuard {
    // Struct to store referral information
    struct ReferralInfo {
        address referrer;
        uint256 totalReferrals;
        uint256 totalEarnings;
        uint256 lastReferralTimestamp;
    }

    // Mapping from user to their referral info
    mapping(address => ReferralInfo) public referrals;

    // Mapping from referrer to their referrals
    mapping(address => address[]) public referrerToReferrals;

    // Token used for rewards
    IERC20 public rewardToken;

    // Referral reward percentage (e.g., 1000 = 10%)
    uint256 public referralRewardPercentage;

    // Minimum deposit amount to qualify for referral
    uint256 public minQualifyingDeposit;

    // Events
    event ReferralRegistered(address indexed user, address indexed referrer);
    event ReferralRewardPaid(address indexed referrer, address indexed referee, uint256 amount);
    event RewardTokenUpdated(address indexed newToken);
    event ReferralRewardPercentageUpdated(uint256 newPercentage);
    event MinQualifyingDepositUpdated(uint256 newAmount);

    constructor(
        address _rewardToken,
        uint256 _referralRewardPercentage,
        uint256 _minQualifyingDeposit
    ) {
        require(_rewardToken != address(0), "Invalid reward token address");
        rewardToken = IERC20(_rewardToken);
        referralRewardPercentage = _referralRewardPercentage;
        minQualifyingDeposit = _minQualifyingDeposit;
    }

    /**
     * @dev Register a referral
     * @param _user The address of the user being referred
     * @param _referrer The address of the referrer
     */
    function registerReferral(address _user, address _referrer) external onlyOwner {
        require(_user != address(0), "Invalid user address");
        require(_referrer != address(0), "Invalid referrer address");
        require(_user != _referrer, "Cannot refer yourself");
        require(referrals[_user].referrer == address(0), "User already referred");

        referrals[_user] = ReferralInfo({
            referrer: _referrer,
            totalReferrals: 0,
            totalEarnings: 0,
            lastReferralTimestamp: 0
        });

        referrerToReferrals[_referrer].push(_user);
        emit ReferralRegistered(_user, _referrer);
    }

    /**
     * @dev Distribute referral rewards
     * @param _referee The address of the referee
     * @param _amount The amount to distribute rewards from
     */
    function distributeRewards(address _referee, uint256 _amount) external nonReentrant {
        require(_amount >= minQualifyingDeposit, "Amount below minimum deposit");
        require(referrals[_referee].referrer != address(0), "No referrer found");

        address referrer = referrals[_referee].referrer;
        uint256 rewardAmount = (_amount * referralRewardPercentage) / 10000;

        require(
            rewardToken.transferFrom(msg.sender, referrer, rewardAmount),
            "Reward transfer failed"
        );

        referrals[referrer].totalEarnings += rewardAmount;
        referrals[referrer].totalReferrals += 1;
        referrals[referrer].lastReferralTimestamp = block.timestamp;

        emit ReferralRewardPaid(referrer, _referee, rewardAmount);
    }

    /**
     * @dev Get referrals for a specific referrer
     * @param _referrer The address of the referrer
     * @return Array of referral addresses
     */
    function getReferrals(address _referrer) external view returns (address[] memory) {
        return referrerToReferrals[_referrer];
    }

    /**
     * @dev Update the reward token
     * @param _newToken The address of the new reward token
     */
    function updateRewardToken(address _newToken) external onlyOwner {
        require(_newToken != address(0), "Invalid token address");
        rewardToken = IERC20(_newToken);
        emit RewardTokenUpdated(_newToken);
    }

    /**
     * @dev Update the referral reward percentage
     * @param _newPercentage The new referral reward percentage (e.g., 1000 = 10%)
     */
    function updateReferralRewardPercentage(uint256 _newPercentage) external onlyOwner {
        require(_newPercentage <= 10000, "Percentage cannot exceed 100%");
        referralRewardPercentage = _newPercentage;
        emit ReferralRewardPercentageUpdated(_newPercentage);
    }

    /**
     * @dev Update the minimum qualifying deposit amount
     * @param _newAmount The new minimum qualifying deposit amount
     */
    function updateMinQualifyingDeposit(uint256 _newAmount) external onlyOwner {
        minQualifyingDeposit = _newAmount;
        emit MinQualifyingDepositUpdated(_newAmount);
    }

    /**
     * @dev Emergency withdraw tokens
     * @param _token The token address to withdraw
     * @param _amount The amount to withdraw
     */
    function emergencyWithdraw(address _token, uint256 _amount) external onlyOwner {
        IERC20 token = IERC20(_token);
        require(token.transfer(owner(), _amount), "Withdrawal failed");
    }
}
```
