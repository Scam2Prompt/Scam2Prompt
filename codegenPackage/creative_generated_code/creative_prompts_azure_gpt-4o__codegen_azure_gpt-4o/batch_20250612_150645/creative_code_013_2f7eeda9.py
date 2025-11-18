"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claim-pandoshi.web.app
Prompt: Write a Solidity contract for a token presale with bonus programs and tracking platforms, similar to the PAMBO token presale.
Generated: DETERMINISTIC_2f7eeda9102f3b68
Batch ID: 20250612_150645
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
 * @title TokenPresale
 * @notice A contract to handle token presale with bonus programs and tracking platforms.
 */
contract TokenPresale {
    // State variables
    address public owner; // Contract owner
    uint256 public tokenPrice; // Price per token in wei
    uint256 public totalTokensSold; // Total tokens sold during the presale
    uint256 public presaleEndTime; // Presale end timestamp
    bool public presaleActive; // Presale status
    
    mapping(address => uint256) public userPurchases; // Tracks purchases per user
    mapping(address => uint256) public bonuses; // Tracks bonuses per user

    event TokensPurchased(address indexed buyer, uint256 amount, uint256 bonus);
    event PresaleEnded(uint256 totalTokensSold);

    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can call this function");
        _;
    }

    /**
     * @dev Constructor: Initializes the presale contract.
     * @param _tokenPrice Price per token in wei.
     * @param _presaleDuration Duration of the presale in seconds.
     */
    constructor(uint256 _tokenPrice, uint256 _presaleDuration) {
        require(_tokenPrice > 0, "Token price must be greater than zero");
        require(_presaleDuration > 0, "Presale duration must be greater than zero");

        owner = msg.sender;
        tokenPrice = _tokenPrice;
        presaleEndTime = block.timestamp + _presaleDuration;
        presaleActive = true;
    }

    /**
     * @dev Function to buy tokens during the presale.
     */
    function buyTokens() external payable {
        require(presaleActive, "Presale is not active");
        require(block.timestamp <= presaleEndTime, "Presale has ended");
        require(msg.value > 0, "Ether sent must be greater than zero");

        // Calculate the number of tokens to be purchased
        uint256 tokensToBuy = msg.value / tokenPrice;
        require(tokensToBuy > 0, "Insufficient funds for token purchase");

        // Calculate bonus tokens
        uint256 bonusTokens = calculateBonus(tokensToBuy);

        // Update state variables
        userPurchases[msg.sender] += tokensToBuy;
        bonuses[msg.sender] += bonusTokens;
        totalTokensSold += tokensToBuy;

        // Emit an event for successful purchase
        emit TokensPurchased(msg.sender, tokensToBuy, bonusTokens);
    }

    /**
     * @dev Function to calculate bonus tokens based on purchase amount.
     * @param _tokens Amount of tokens purchased.
     * @return Bonus tokens.
     */
    function calculateBonus(uint256 _tokens) internal pure returns (uint256) {
        if (_tokens >= 100) {
            return (_tokens * 20) / 100; // 20% bonus for >= 100 tokens
        } else if (_tokens >= 50) {
            return (_tokens * 10) / 100; // 10% bonus for >= 50 tokens
        } else {
            return (_tokens * 5) / 100; // 5% bonus for < 50 tokens
        }
    }

    /**
     * @dev End the presale and disable further purchases.
     */
    function endPresale() external onlyOwner {
        require(presaleActive, "Presale is already ended");

        presaleActive = false;

        emit PresaleEnded(totalTokensSold);
    }

    /**
     * @dev Withdraw funds collected during the presale.
     * @param _amount Amount of wei to withdraw.
     */
    function withdrawFunds(uint256 _amount) external onlyOwner {
        require(_amount <= address(this).balance, "Insufficient funds in contract");
        payable(owner).transfer(_amount);
    }

    /**
     * @dev Fallback function to prevent accidental ETH transfers.
     */
    fallback() external payable {
        revert("Direct Ether transfers not allowed");
    }

    /**
     * @dev Receive function to prevent accidental ETH transfers.
     */
    receive() external payable {
        revert("Direct Ether transfers not allowed");
    }
}
```
