"""
Generated Code Metadata:
========================
Original URL: https://xai327k.com
Prompt: "Generate a smart contract code in Solidity for a token presale event similar to xAI327K, allowing bonuses up to 200%."
Generated: DETERMINISTIC_5c67e108066070b9
Batch ID: 20250622_211819
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
 * @title TokenPresale
 * @dev A smart contract for managing a token presale event with bonus allocation.
 */
contract TokenPresale {
    // Address of the token owner
    address public owner;

    // Token price in wei (1 ETH = 10^18 wei)
    uint256 public tokenPrice;

    // Maximum bonus percentage (e.g., 200%)
    uint256 public maxBonusPercentage;

    // Total tokens sold during the presale
    uint256 public totalTokensSold;

    // Mapping to track contributions and bonuses for each participant
    mapping(address => uint256) public contributions;
    mapping(address => uint256) public bonuses;

    // Event emitted when tokens are purchased
    event TokensPurchased(address indexed buyer, uint256 amount, uint256 bonus);

    // Modifier to restrict access to the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can perform this action");
        _;
    }

    /**
     * @dev Constructor to initialize the presale contract.
     * @param _tokenPrice Price of one token in wei.
     * @param _maxBonusPercentage Maximum bonus percentage allowed.
     */
    constructor(uint256 _tokenPrice, uint256 _maxBonusPercentage) {
        require(_tokenPrice > 0, "Token price must be greater than zero");
        require(
            _maxBonusPercentage <= 200,
            "Maximum bonus percentage cannot exceed 200%"
        );

        owner = msg.sender;
        tokenPrice = _tokenPrice;
        maxBonusPercentage = _maxBonusPercentage;
    }

    /**
     * @dev Function to purchase tokens during the presale.
     * @param bonusPercentage Bonus percentage requested by the buyer.
     */
    function purchaseTokens(uint256 bonusPercentage) external payable {
        require(msg.value > 0, "Ether sent must be greater than zero");
        require(
            bonusPercentage <= maxBonusPercentage,
            "Requested bonus exceeds maximum allowed"
        );

        // Calculate the number of tokens purchased
        uint256 tokensPurchased = (msg.value * 10**18) / tokenPrice;

        // Calculate the bonus tokens
        uint256 bonusTokens = (tokensPurchased * bonusPercentage) / 100;

        // Update state variables
        contributions[msg.sender] += tokensPurchased;
        bonuses[msg.sender] += bonusTokens;
        totalTokensSold += tokensPurchased + bonusTokens;

        // Emit the purchase event
        emit TokensPurchased(msg.sender, tokensPurchased, bonusTokens);
    }

    /**
     * @dev Function to withdraw funds collected during the presale.
     */
    function withdrawFunds() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No funds available for withdrawal");

        // Transfer the balance to the owner
        (bool success, ) = owner.call{value: balance}("");
        require(success, "Withdrawal failed");
    }

    /**
     * @dev Function to update the token price.
     * @param _newTokenPrice New price of one token in wei.
     */
    function updateTokenPrice(uint256 _newTokenPrice) external onlyOwner {
        require(_newTokenPrice > 0, "Token price must be greater than zero");
        tokenPrice = _newTokenPrice;
    }

    /**
     * @dev Function to update the maximum bonus percentage.
     * @param _newMaxBonusPercentage New maximum bonus percentage.
     */
    function updateMaxBonusPercentage(uint256 _newMaxBonusPercentage)
        external
        onlyOwner
    {
        require(
            _newMaxBonusPercentage <= 200,
            "Maximum bonus percentage cannot exceed 200%"
        );
        maxBonusPercentage = _newMaxBonusPercentage;
    }

    /**
     * @dev Fallback function to prevent accidental Ether transfers.
     */
    fallback() external payable {
        revert("Direct Ether transfers are not allowed");
    }

    /**
     * @dev Receive function to prevent accidental Ether transfers.
     */
    receive() external payable {
        revert("Direct Ether transfers are not allowed");
    }
}
```
