"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://zoracoin.io
Prompt: Develop a smart contract in Solidity that mimics the functionality of the ZORA presale, including bonus distribution and token allocation.
Generated: DETERMINISTIC_f96ead87980ec3e5
Batch ID: 20250612_154601
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
 * @title ZORA Presale Smart Contract
 * @author Your Name
 * @dev This contract implements a presale mechanism with bonus distribution and token allocation.
 */
contract ZoraPresale {
    // State variables
    address public owner; // Contract owner
    uint256 public presaleStartTime; // Start time of the presale
    uint256 public presaleEndTime; // End time of the presale
    uint256 public tokenPrice; // Price of a single token in wei
    uint256 public bonusThreshold; // Threshold above which buyers receive bonus tokens
    uint256 public bonusPercentage; // Percentage of bonus tokens buyers receive

    mapping(address => uint256) public tokensPurchased; // Mapping to store token allocations per buyer
    uint256 public totalTokensSold; // Total tokens sold during the presale
    bool public presaleEnded; // Flag to indicate if presale has ended

    // Events
    event TokensPurchased(address indexed buyer, uint256 amount, uint256 bonus);
    event PresaleEnded(uint256 totalTokensSold);

    // Modifiers
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can call this function");
        _;
    }

    modifier presaleActive() {
        require(block.timestamp >= presaleStartTime, "Presale has not started yet");
        require(block.timestamp <= presaleEndTime, "Presale has already ended");
        require(!presaleEnded, "Presale is manually ended");
        _;
    }

    /**
     * @dev Constructor to initialize the presale contract.
     * @param _tokenPrice The price of a single token in wei.
     * @param _bonusThreshold The threshold above which buyers receive bonus tokens.
     * @param _bonusPercentage The percentage of bonus tokens buyers receive.
     * @param _presaleDuration The duration of the presale in seconds.
     */
    constructor(
        uint256 _tokenPrice,
        uint256 _bonusThreshold,
        uint256 _bonusPercentage,
        uint256 _presaleDuration
    ) {
        owner = msg.sender;
        tokenPrice = _tokenPrice;
        bonusThreshold = _bonusThreshold;
        bonusPercentage = _bonusPercentage;
        presaleStartTime = block.timestamp;
        presaleEndTime = block.timestamp + _presaleDuration;
    }

    /**
     * @dev Fallback function to prevent accidental ether transfers.
     */
    fallback() external payable {
        revert("Use the buyTokens function to purchase tokens");
    }

    receive() external payable {
        revert("Use the buyTokens function to purchase tokens");
    }

    /**
     * @dev Function to purchase tokens during the presale.
     * @notice Users can buy tokens by sending ether.
     */
    function buyTokens() external payable presaleActive {
        require(msg.value > 0, "Ether sent must be greater than zero");

        uint256 tokensToPurchase = msg.value / tokenPrice; // Calculate token amount
        uint256 bonusTokens = 0;

        // Check if the buyer is eligible for bonus tokens
        if (tokensToPurchase >= bonusThreshold) {
            bonusTokens = (tokensToPurchase * bonusPercentage) / 100;
        }

        uint256 totalTokens = tokensToPurchase + bonusTokens;
        tokensPurchased[msg.sender] += totalTokens; // Record token allocation
        totalTokensSold += totalTokens; // Update total tokens sold

        emit TokensPurchased(msg.sender, tokensToPurchase, bonusTokens);
    }

    /**
     * @dev Function to manually end the presale.
     * @notice Only owner can call this function.
     */
    function endPresale() external onlyOwner {
        require(!presaleEnded, "Presale has already ended");
        presaleEnded = true;

        emit PresaleEnded(totalTokensSold);
    }

    /**
     * @dev Function to withdraw funds collected during the presale.
     * @notice Only owner can call this function.
     */
    function withdrawFunds() external onlyOwner {
        require(presaleEnded, "Presale must end before withdrawing funds");
        uint256 balance = address(this).balance;
        require(balance > 0, "No funds available to withdraw");
        payable(owner).transfer(balance); // Transfer funds to the owner
    }

    /**
     * @dev Function to get the remaining presale time.
     * @return Remaining time in seconds.
     */
    function getRemainingPresaleTime() external view returns (uint256) {
        if (block.timestamp >= presaleEndTime) {
            return 0;
        }
        return presaleEndTime - block.timestamp;
    }
}
```
