"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://moxie.news
Prompt: Develop a decentralized application (dApp) that utilizes the Moxie Protocol to reward referrals and product trials on Farcaster. Ensure the rewards are distributed according to the shared payout structure.
Generated: DETERMINISTIC_efc5975a59e29b97
Batch ID: 20250612_150715
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

// Import necessary interfaces and libraries
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

// Interface for the Moxie Protocol's reward distribution
interface IMoxieProtocol {
    function distributeRewards(address referrer, uint256 amount) external;
}

// Main contract for the decentralized application (dApp)
contract ReferralRewards is Ownable {
    // State variables
    IMoxieProtocol public moxieProtocol; // Instance of the Moxie Protocol
    IERC20 public rewardToken; // ERC20 token for rewards
    uint256 public rewardPercentage; // Percentage of rewards distributed

    // Mapping to track referrals
    mapping(address => address) public referrals; // Stores referrer for each user
    mapping(address => uint256) public referralCount; // Counts the number of referrals made by a user

    // Events
    event ReferralRegistered(address indexed user, address indexed referrer);
    event RewardsDistributed(address indexed referrer, uint256 amount);

    // Constructor to initialize state variables
    constructor(address _moxieProtocol, address _rewardToken, uint256 _rewardPercentage) {
        require(_moxieProtocol != address(0), "Invalid Moxie Protocol address");
        require(_rewardToken != address(0), "Invalid reward token address");
        require(_rewardPercentage > 0 && _rewardPercentage <= 100, "Percentage must be between 1 and 100");

        moxieProtocol = IMoxieProtocol(_moxieProtocol);
        rewardToken = IERC20(_rewardToken);
        rewardPercentage = _rewardPercentage;
    }

    // Function to register a referral
    function registerReferral(address referrer) external {
        require(referrer != msg.sender, "You cannot refer yourself");
        require(referrals[msg.sender] == address(0), "Referral already registered");

        referrals[msg.sender] = referrer;
        referralCount[referrer] += 1;

        emit ReferralRegistered(msg.sender, referrer);
    }

    // Function to distribute rewards to referrers
    function distributeRewards(address user) external onlyOwner {
        address referrer = referrals[user];
        require(referrer != address(0), "No referrer found for this user");

        // Calculate reward amount based on some conditions
        uint256 rewardAmount = calculateReward(user);
        
        // Transfer tokens to referrer
        require(rewardToken.balanceOf(address(this)) >= rewardAmount, "Insufficient contract balance");
        rewardToken.transfer(referrer, rewardAmount);
        
        // Call Moxie Protocol for distribution
        moxieProtocol.distributeRewards(referrer, rewardAmount);

        emit RewardsDistributed(referrer, rewardAmount);
    }

    // Internal function to calculate rewards based on the referrer and user
    function calculateReward(address user) internal view returns (uint256) {
        // Example logic for calculating reward (1 token per referral)
        return referralCount[user] * rewardPercentage / 100; // Example calculation
    }

    // Function to withdraw tokens from the contract (only owner can call this)
    function withdrawTokens(uint256 amount) external onlyOwner {
        require(amount > 0, "Withdrawal amount must be greater than 0");
        require(rewardToken.balanceOf(address(this)) >= amount, "Insufficient contract balance");

        rewardToken.transfer(owner(), amount);
    }
}
```
