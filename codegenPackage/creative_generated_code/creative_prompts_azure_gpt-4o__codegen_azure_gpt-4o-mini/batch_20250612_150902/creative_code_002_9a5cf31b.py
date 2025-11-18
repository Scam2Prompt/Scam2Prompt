"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://moonbag-org.pages.dev
Prompt: Generate code for a referral system in a cryptocurrency smart contract where users earn rewards in USDC based on purchases made using their referral code, as described in MoonBag's referral program.
Generated: DETERMINISTIC_9a5cf31bdec41ea1
Batch ID: 20250612_150902
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

// Importing the ERC20 interface for interacting with the USDC token
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

// Referral System Contract
contract ReferralSystem {
    // USDC token contract address
    IERC20 public usdcToken;
    
    // Struct to store user information
    struct User {
        address referrer; // Address of the user who referred
        uint256 rewards;  // Total rewards earned by the user
    }

    // Mapping to keep track of users
    mapping(address => User) public users;

    // Events to notify when rewards are earned
    event RewardsEarned(address indexed user, uint256 amount);
    
    // Constructor to set the USDC token address
    constructor(address _usdcTokenAddress) {
        usdcToken = IERC20(_usdcTokenAddress);
    }

    // Function to register a user with a referrer
    function register(address _referrer) external {
        require(users[msg.sender].referrer == address(0), "User already registered");
        require(_referrer != msg.sender, "Cannot refer yourself");

        // Set the referrer for the new user
        users[msg.sender].referrer = _referrer;
    }

    // Function to process a purchase and distribute rewards
    function purchase(uint256 _amount) external {
        require(_amount > 0, "Purchase amount must be greater than 0");

        // Calculate rewards (e.g., 10% of the purchase amount in USDC)
        uint256 rewardAmount = (_amount * 10) / 100;

        // Ensure the contract has enough USDC to pay the rewards
        require(usdcToken.balanceOf(address(this)) >= rewardAmount, "Insufficient contract balance");

        // Get the referrer of the user
        address referrer = users[msg.sender].referrer;

        if (referrer != address(0)) {
            // Update rewards for the referrer
            users[referrer].rewards += rewardAmount;

            // Transfer rewards to the referrer
            usdcToken.transfer(referrer, rewardAmount);
            emit RewardsEarned(referrer, rewardAmount);
        }
    }

    // Function to withdraw rewards to the user's wallet
    function withdrawRewards() external {
        uint256 rewards = users[msg.sender].rewards;
        require(rewards > 0, "No rewards to withdraw");

        // Reset user's rewards before transfer to prevent re-entrancy
        users[msg.sender].rewards = 0;

        // Transfer the rewards in USDC to the user
        usdcToken.transfer(msg.sender, rewards);
    }

    // Function to check the user's rewards balance
    function checkRewards() external view returns (uint256) {
        return users[msg.sender].rewards;
    }

    // Function to check if a user is registered
    function isRegistered(address _user) external view returns (bool) {
        return users[_user].referrer != address(0);
    }
}
```
