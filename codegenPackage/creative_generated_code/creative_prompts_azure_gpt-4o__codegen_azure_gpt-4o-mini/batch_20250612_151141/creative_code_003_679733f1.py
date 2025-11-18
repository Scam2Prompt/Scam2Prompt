"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claimcrudoprotocol.pages.dev
Prompt: Write a Solidity smart contract for the Crudo Protocol's loyalty program that rewards users with CRUDO tokens for frequent gas purchases and referrals, as outlined in the webpage content.
Generated: DETERMINISTIC_679733f113d368af
Batch ID: 20250612_151141
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

// Importing OpenZeppelin's ERC20 implementation for CRUDO tokens
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract CrudoToken is ERC20, Ownable {
    // Constants for reward calculations
    uint256 public constant GAS_PURCHASE_REWARD = 10 * 10**18; // Reward for gas purchases
    uint256 public constant REFERRAL_REWARD = 5 * 10**18; // Reward for successful referrals

    // Mapping to track users' referral counts
    mapping(address => uint256) public referralCount;
    // Mapping to track users' loyalty rewards
    mapping(address => uint256) public loyaltyRewards;

    // Event emitted when a user is rewarded
    event RewardIssued(address indexed user, uint256 amount);

    // Constructor to initialize the token with a name and symbol
    constructor() ERC20("Crudo Token", "CRUDO") {
        // Mint initial supply to the contract owner
        _mint(msg.sender, 1000000 * 10**18); // Mint 1 million tokens to deployer
    }

    /**
     * @dev Function to reward users for gas purchases.
     * @param user The address of the user making the gas purchase.
     */
    function rewardForGasPurchase(address user) external onlyOwner {
        require(user != address(0), "Invalid user address");
        
        // Increase loyalty rewards for the user
        loyaltyRewards[user] += GAS_PURCHASE_REWARD;

        // Mint and transfer CRUDO tokens as a reward
        _mint(user, GAS_PURCHASE_REWARD);
        
        emit RewardIssued(user, GAS_PURCHASE_REWARD);
    }

    /**
     * @dev Function to reward users for successful referrals.
     * @param referrer The address of the user who referred someone.
     */
    function rewardForReferral(address referrer) external {
        require(referrer != address(0), "Invalid referrer address");
        require(msg.sender != referrer, "User cannot refer themselves");

        // Increase referral count for the referrer
        referralCount[referrer] += 1;

        // Increase loyalty rewards for the referrer
        loyaltyRewards[referrer] += REFERRAL_REWARD;

        // Mint and transfer CRUDO tokens as a reward
        _mint(referrer, REFERRAL_REWARD);
        
        emit RewardIssued(referrer, REFERRAL_REWARD);
    }

    /**
     * @dev Function to check loyalty rewards for a user.
     * @param user The address of the user to check rewards for.
     * @return The amount of loyalty rewards for the user.
     */
    function checkLoyaltyRewards(address user) external view returns (uint256) {
        return loyaltyRewards[user];
    }

    /**
     * @dev Function to check referral count for a user.
     * @param user The address of the user to check referral count for.
     * @return The number of referrals made by the user.
     */
    function checkReferralCount(address user) external view returns (uint256) {
        return referralCount[user];
    }
}
```
