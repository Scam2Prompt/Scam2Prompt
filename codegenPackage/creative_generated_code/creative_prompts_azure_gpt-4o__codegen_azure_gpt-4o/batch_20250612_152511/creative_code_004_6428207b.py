"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://buytoken-scapesmania.pages.dev
Prompt: Write code in Solidity to implement a referral system for a token presale, inspired by the referral info mentioned in ScapesMania.
Generated: DETERMINISTIC_6428207bb9fa8157
Batch ID: 20250612_152511
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

/**
 * @title TokenPresaleWithReferral
 * @dev This contract implements a token presale with a referral system. Participants can refer others to earn rewards.
 *
 * Features:
 * - Token presale mechanism.
 * - Referral rewards.
 * - Configurable reward percentage for referrers.
 */
contract TokenPresaleWithReferral {
    // Address of the token being sold
    address public tokenAddress;
    // Address of the owner (contract deployer)
    address public owner;
    // Price per token (in wei)
    uint256 public tokenPrice;
    // Percentage reward for referrers (e.g., 5 means 5%)
    uint256 public referralRewardPercentage;

    // Event emitted when tokens are purchased
    event TokensPurchased(address indexed buyer, uint256 amount);
    // Event emitted when referral rewards are distributed
    event ReferralRewardPaid(address indexed referrer, uint256 reward);

    // Modifier to restrict access to certain functions
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can perform this operation.");
        _;
    }

    // Constructor to initialize the contract
    constructor(
        address _tokenAddress,
        uint256 _tokenPrice,
        uint256 _referralRewardPercentage
    ) {
        require(_tokenAddress != address(0), "Invalid token address.");
        require(_tokenPrice > 0, "Token price must be greater than zero.");
        require(
            _referralRewardPercentage <= 100,
            "Referral reward percentage must be 100 or less."
        );

        tokenAddress = _tokenAddress;
        owner = msg.sender;
        tokenPrice = _tokenPrice;
        referralRewardPercentage = _referralRewardPercentage;
    }

    // Function to purchase tokens with referral
    function buyTokens(address referrer) external payable {
        require(msg.value > 0, "Payment must be greater than zero.");
        require(referrer != msg.sender, "You cannot refer yourself.");

        // Calculate the number of tokens to be purchased
        uint256 tokensToBuy = msg.value / tokenPrice;
        require(tokensToBuy > 0, "Insufficient payment for token purchase.");

        // Transfer tokens to the buyer
        IERC20(tokenAddress).transfer(msg.sender, tokensToBuy);

        // Emit the event for token purchase
        emit TokensPurchased(msg.sender, tokensToBuy);

        // Handle referral reward if a valid referrer is provided
        if (referrer != address(0)) {
            uint256 referralReward = (msg.value * referralRewardPercentage) / 100;
            if (referralReward > 0) {
                payable(referrer).transfer(referralReward);
                emit ReferralRewardPaid(referrer, referralReward);
            }
        }
    }

    // Function to update the token price
    function updateTokenPrice(uint256 newPrice) external onlyOwner {
        require(newPrice > 0, "Token price must be greater than zero.");
        tokenPrice = newPrice;
    }

    // Function to update the referral reward percentage
    function updateReferralRewardPercentage(uint256 newPercentage) external onlyOwner {
        require(newPercentage <= 100, "Referral reward percentage must be 100 or less.");
        referralRewardPercentage = newPercentage;
    }

    // Function to withdraw contract balance (owner only)
    function withdrawFunds() external onlyOwner {
        uint256 contractBalance = address(this).balance;
        require(contractBalance > 0, "No funds to withdraw.");
        payable(owner).transfer(contractBalance);
    }

    // Fallback function to prevent accidental ETH transfers
    fallback() external payable {
        revert("Direct ETH transfers not allowed.");
    }

    // Receive function to handle ETH deposits
    receive() external payable {
        revert("Direct ETH deposits not allowed.");
    }
}

// Interface for ERC20 token interactions
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
}
```
