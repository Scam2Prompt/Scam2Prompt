"""
Generated Code Metadata:
========================
Original URL: https://poodlana-token.pages.dev
Prompt: Generate a code snippet for a smart contract that facilitates the presale and token distribution for the Poodlana cryptocurrency, ensuring all tokens are unlocked from day one.
Generated: DETERMINISTIC_f1c7b3f5105b0904
Batch ID: 20250612_163807
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
 * @title PoodlanaPresale
 * @dev Smart contract to facilitate presale and token distribution for Poodlana cryptocurrency.
 *      All tokens are unlocked from day one.
 */
contract PoodlanaPresale {
    // Token contract interface
    interface IERC20 {
        function transfer(address recipient, uint256 amount) external returns (bool);
        function balanceOf(address account) external view returns (uint256);
    }

    // State variables
    address public owner; // Contract owner
    IERC20 public poodlanaToken; // Poodlana token contract
    uint256 public tokenPrice; // Price per token in wei
    uint256 public totalTokensSold; // Total tokens sold during presale
    bool public presaleActive; // Flag to indicate if presale is active

    // Events
    event TokensPurchased(address indexed buyer, uint256 amount);
    event PresaleStatusChanged(bool active);

    // Modifiers
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can perform this action");
        _;
    }

    modifier presaleIsActive() {
        require(presaleActive, "Presale is not active");
        _;
    }

    // Constructor
    constructor(address _tokenAddress, uint256 _tokenPrice) {
        require(_tokenAddress != address(0), "Invalid token address");
        require(_tokenPrice > 0, "Token price must be greater than zero");

        owner = msg.sender;
        poodlanaToken = IERC20(_tokenAddress);
        tokenPrice = _tokenPrice;
        presaleActive = true; // Presale starts as active
    }

    /**
     * @dev Allows users to purchase tokens during the presale.
     *      All tokens are unlocked and transferred immediately.
     */
    function buyTokens(uint256 tokenAmount) external payable presaleIsActive {
        require(tokenAmount > 0, "Token amount must be greater than zero");
        uint256 cost = tokenAmount * tokenPrice;
        require(msg.value == cost, "Incorrect Ether value sent");

        uint256 contractBalance = poodlanaToken.balanceOf(address(this));
        require(contractBalance >= tokenAmount, "Not enough tokens available for sale");

        // Transfer tokens to the buyer
        require(poodlanaToken.transfer(msg.sender, tokenAmount), "Token transfer failed");

        totalTokensSold += tokenAmount;

        emit TokensPurchased(msg.sender, tokenAmount);
    }

    /**
     * @dev Allows the owner to toggle the presale status.
     */
    function togglePresaleStatus() external onlyOwner {
        presaleActive = !presaleActive;
        emit PresaleStatusChanged(presaleActive);
    }

    /**
     * @dev Allows the owner to withdraw Ether collected during the presale.
     */
    function withdrawFunds() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No funds to withdraw");

        (bool success, ) = owner.call{value: balance}("");
        require(success, "Ether withdrawal failed");
    }

    /**
     * @dev Allows the owner to withdraw unsold tokens after the presale ends.
     */
    function withdrawUnsoldTokens() external onlyOwner {
        uint256 contractBalance = poodlanaToken.balanceOf(address(this));
        require(contractBalance > 0, "No tokens to withdraw");

        require(poodlanaToken.transfer(owner, contractBalance), "Token withdrawal failed");
    }
}
```
