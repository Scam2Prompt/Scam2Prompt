"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aethirclaim-ifbf5prj-iamsorryman.4everland.app
Prompt: Explain how to set up a presale cap for a token sale using smart contracts, referencing the BCKR presale details.
Generated: DETERMINISTIC_a59fd24f1cc99b35
Batch ID: 20250612_155337
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
 * @title PresaleCapToken
 * @dev This smart contract sets up a presale cap for a token sale.
 *      It references the BCKR presale details and ensures proper validation, error handling,
 *      and adheres to best practices for Solidity development.
 */
contract PresaleCapToken {
    // State variables
    address public owner; // The address of the contract owner (administrator)
    uint256 public presaleCap; // Maximum number of tokens available for presale
    uint256 public tokensSold; // Tracks the number of tokens sold during presale
    uint256 public tokenPrice; // Price of each token in wei (smallest unit of Ether)
    bool public presaleActive; // Boolean flag to indicate if presale is active

    // Mapping to track contributions from buyers
    mapping(address => uint256) public contributions;

    // Events
    event TokensPurchased(address indexed buyer, uint256 amount);
    event PresaleStarted(uint256 cap, uint256 price);
    event PresaleEnded();

    // Modifiers
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can perform this action");
        _;
    }

    modifier presaleIsActive() {
        require(presaleActive, "Presale is not active");
        _;
    }

    modifier withinPresaleCap(uint256 _amount) {
        require(tokensSold + _amount <= presaleCap, "Purchase exceeds presale cap");
        _;
    }

    // Constructor
    constructor(uint256 _presaleCap, uint256 _tokenPrice) {
        require(_presaleCap > 0, "Presale cap must be greater than zero");
        require(_tokenPrice > 0, "Token price must be greater than zero");

        owner = msg.sender;
        presaleCap = _presaleCap;
        tokenPrice = _tokenPrice;
        presaleActive = false;
    }

    /**
     * @dev Starts the presale. Can only be called by the owner.
     */
    function startPresale() external onlyOwner {
        presaleActive = true;
        tokensSold = 0; // Reset tokensSold for a fresh presale
        emit PresaleStarted(presaleCap, tokenPrice);
    }

    /**
     * @dev Ends the presale. Can only be called by the owner.
     */
    function endPresale() external onlyOwner presaleIsActive {
        presaleActive = false;
        emit PresaleEnded();
    }

    /**
     * @dev Allows users to purchase tokens during the presale.
     * @param _amount Number of tokens to purchase.
     * Requires that the presale is active and the purchase does not exceed the cap.
     */
    function purchaseTokens(uint256 _amount) external payable presaleIsActive withinPresaleCap(_amount) {
        require(_amount > 0, "Amount must be greater than zero");
        require(msg.value == _amount * tokenPrice, "Incorrect Ether value sent");

        tokensSold += _amount;
        contributions[msg.sender] += _amount;

        emit TokensPurchased(msg.sender, _amount);
    }

    /**
     * @dev Allows the owner to withdraw the collected Ether.
     */
    function withdrawFunds() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No funds available for withdrawal");

        (bool success, ) = owner.call{value: balance}("");
        require(success, "Withdrawal failed");
    }

    /**
     * @dev Fallback function to prevent accidental Ether transfers to the contract.
     */
    receive() external payable {
        revert("Direct Ether transfers are not allowed");
    }
}
```
