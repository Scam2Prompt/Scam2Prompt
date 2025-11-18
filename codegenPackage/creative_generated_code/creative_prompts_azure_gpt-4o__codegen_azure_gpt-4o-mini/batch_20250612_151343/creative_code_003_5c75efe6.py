"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claimyoureasyneiro.pages.dev
Prompt: Write a Solidity smart contract that could be used to distribute $NEIRO tokens as part of a referral program. Include functions for claiming tokens and tracking referrals.
Generated: DETERMINISTIC_5c75efe60080c80c
Batch ID: 20250612_151343
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

// Importing the ERC20 interface for the $NEIRO token
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title ReferralProgram
 * @dev This contract allows users to claim $NEIRO tokens based on referrals.
 */
contract ReferralProgram is Ownable {
    // Token contract instance
    IERC20 public neiroToken;

    // Mapping to track referrals and claimed tokens
    mapping(address => address) public referrals; // User => Referrer
    mapping(address => uint256) public claimedTokens; // User => Claimed Amount

    // Token distribution amount for each successful referral
    uint256 public constant REFERRAL_REWARD = 100 * 10**18; // Example: 100 NEIRO tokens

    // Event emitted when a user claims tokens
    event TokensClaimed(address indexed user, uint256 amount);
    // Event emitted when a referral is made
    event ReferralMade(address indexed user, address indexed referrer);

    /**
     * @dev Constructor to set the $NEIRO token address.
     * @param _neiroToken Address of the $NEIRO token contract
     */
    constructor(address _neiroToken) {
        require(_neiroToken != address(0), "Invalid token address");
        neiroToken = IERC20(_neiroToken);
    }

    /**
     * @dev Function to register a referral.
     * @param referrer Address of the referrer
     */
    function registerReferral(address referrer) external {
        require(referrer != msg.sender, "You cannot refer yourself");
        require(referrals[msg.sender] == address(0), "Referral already registered");

        referrals[msg.sender] = referrer;
        emit ReferralMade(msg.sender, referrer);
    }

    /**
     * @dev Function for users to claim their referral tokens.
     */
    function claimTokens() external {
        // Check if the user has a registered referrer
        require(referrals[msg.sender] != address(0), "No referral registered");

        // Ensure the user has not already claimed tokens
        require(claimedTokens[msg.sender] == 0, "Tokens already claimed");

        // Transfer tokens from the contract to the user
        claimedTokens[msg.sender] = REFERRAL_REWARD;
        require(neiroToken.transfer(msg.sender, REFERRAL_REWARD), "Token transfer failed");

        emit TokensClaimed(msg.sender, REFERRAL_REWARD);
    }

    /**
     * @dev Owner function to withdraw tokens from the contract.
     * @param amount Amount of tokens to withdraw
     */
    function withdrawTokens(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        require(neiroToken.balanceOf(address(this)) >= amount, "Insufficient balance");

        bool success = neiroToken.transfer(owner(), amount);
        require(success, "Token withdrawal failed");
    }

    /**
     * @dev Function to check the referral of a user.
     * @param user Address of the user
     * @return address of the referrer
     */
    function getReferrer(address user) external view returns (address) {
        return referrals[user];
    }

    /**
     * @dev Function to check the claimed tokens of a user.
     * @param user Address of the user
     * @return Amount of tokens claimed by the user
     */
    function getClaimedTokens(address user) external view returns (uint256) {
        return claimedTokens[user];
    }
}
```
