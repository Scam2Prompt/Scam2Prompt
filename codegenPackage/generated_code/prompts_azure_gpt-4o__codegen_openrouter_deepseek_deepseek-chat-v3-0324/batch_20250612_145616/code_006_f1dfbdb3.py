"""
Generated Code Metadata:
========================
Original URL: https://moonhop.pages.dev
Prompt: Create a Solidity smart contract that implements a referral program similar to MOONHOP's, allowing users to generate referral codes and track rewards.
Generated: DETERMINISTIC_f1dfbdb3fc332712
Batch ID: 20250612_145616
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

/**
 * @title MoonHopReferral
 * @dev A referral program contract that allows users to generate referral codes and earn rewards
 */
contract MoonHopReferral {
    // Struct to store referral information
    struct ReferralInfo {
        address referrer;
        uint256 totalReferrals;
        uint256 totalRewards;
        mapping(address => bool) referredUsers;
    }

    // Contract owner
    address public owner;

    // Referral reward percentage (in basis points, e.g., 500 = 5%)
    uint256 public rewardPercentage;

    // Mapping from referral code to referrer address
    mapping(string => address) public referralCodes;

    // Mapping from referrer address to referral info
    mapping(address => ReferralInfo) public referrers;

    // Mapping from user address to their referrer
    mapping(address => address) public userReferrers;

    // Events
    event ReferralCodeGenerated(address indexed referrer, string code);
    event ReferralRegistered(address indexed referrer, address indexed user);
    event RewardDistributed(address indexed referrer, address indexed user, uint256 amount);
    event OwnershipTransferred(address indexed previousOwner, address indexed newOwner);
    event RewardPercentageUpdated(uint256 newPercentage);

    // Modifier to restrict function access to owner only
    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can call this function");
        _;
    }

    /**
     * @dev Constructor sets the initial owner and reward percentage
     * @param _rewardPercentage Initial reward percentage in basis points
     */
    constructor(uint256 _rewardPercentage) {
        owner = msg.sender;
        rewardPercentage = _rewardPercentage;
    }

    /**
     * @dev Generate a new referral code
     * @param code The referral code to register
     */
    function generateReferralCode(string memory code) external {
        require(bytes(code).length > 0, "Referral code cannot be empty");
        require(referralCodes[code] == address(0), "Referral code already exists");
        
        referralCodes[code] = msg.sender;
        emit ReferralCodeGenerated(msg.sender, code);
    }

    /**
     * @dev Register a referral using a referral code
     * @param code The referral code to use
     */
    function registerReferral(string memory code) external {
        require(bytes(code).length > 0, "Referral code cannot be empty");
        require(userReferrers[msg.sender] == address(0), "User already has a referrer");
        
        address referrer = referralCodes[code];
        require(referrer != address(0), "Invalid referral code");
        require(referrer != msg.sender, "Cannot refer yourself");

        ReferralInfo storage refInfo = referrers[referrer];
        require(!refInfo.referredUsers[msg.sender], "User already referred by this address");

        userReferrers[msg.sender] = referrer;
        refInfo.referredUsers[msg.sender] = true;
        refInfo.totalReferrals += 1;

        emit ReferralRegistered(referrer, msg.sender);
    }

    /**
     * @dev Distribute rewards to referrer based on transaction amount
     * @param user The user who made the transaction
     * @param amount The transaction amount
     * @return rewardAmount The calculated reward amount
     */
    function distributeRewards(address user, uint256 amount) external returns (uint256 rewardAmount) {
        address referrer = userReferrers[user];
        if (referrer == address(0)) {
            return 0;
        }

        rewardAmount = (amount * rewardPercentage) / 10000;
        if (rewardAmount > 0) {
            ReferralInfo storage refInfo = referrers[referrer];
            refInfo.totalRewards += rewardAmount;
            
            emit RewardDistributed(referrer, user, rewardAmount);
        }
        return rewardAmount;
    }

    /**
     * @dev Check if a user was referred by a specific referrer
     * @param referrer The referrer address
     * @param user The user address
     * @return True if the user was referred by the referrer
     */
    function isReferredBy(address referrer, address user) external view returns (bool) {
        return referrers[referrer].referredUsers[user];
    }

    /**
     * @dev Update the reward percentage (owner only)
     * @param newPercentage New reward percentage in basis points
     */
    function updateRewardPercentage(uint256 newPercentage) external onlyOwner {
        require(newPercentage <= 10000, "Percentage cannot exceed 100%");
        rewardPercentage = newPercentage;
        emit RewardPercentageUpdated(newPercentage);
    }

    /**
     * @dev Transfer ownership of the contract (owner only)
     * @param newOwner Address of the new owner
     */
    function transferOwnership(address newOwner) external onlyOwner {
        require(newOwner != address(0), "New owner cannot be zero address");
        emit OwnershipTransferred(owner, newOwner);
        owner = newOwner;
    }
}
```
