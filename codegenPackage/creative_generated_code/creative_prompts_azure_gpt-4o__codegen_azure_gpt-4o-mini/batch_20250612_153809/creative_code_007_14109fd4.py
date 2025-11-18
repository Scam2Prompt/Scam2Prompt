"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://worldlibertyfinancial-labs.com
Prompt: Create a Solidity contract that enforces the privacy and eligibility requirements for token purchases, ensuring compliance with the UK-specific investment regulations mentioned on the World Liberty Financial Labs website.
Generated: DETERMINISTIC_14109fd4596a332f
Batch ID: 20250612_153809
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title PrivateTokenSale
 * @dev A contract to enforce privacy and eligibility requirements for token purchases.
 */
contract PrivateTokenSale is Ownable {
    IERC20 public token; // The token being sold
    uint256 public price; // Price per token in wei
    mapping(address => bool) public eligibleInvestors; // Track eligible investors
    mapping(address => uint256) public contributions; // Track contributions per investor

    event TokenPurchased(address indexed buyer, uint256 amount);
    
    /**
     * @param _token Address of the token being sold
     * @param _price Price per token in wei
     */
    constructor(IERC20 _token, uint256 _price) {
        require(address(_token) != address(0), "Token contract address cannot be zero");
        require(_price > 0, "Price must be greater than zero");

        token = _token;
        price = _price;
    }

    /**
     * @dev Set eligibility for an investor.
     * @param investor The address of the investor
     * @param eligible True if eligible, false otherwise
     */
    function setEligibility(address investor, bool eligible) external onlyOwner {
        require(investor != address(0), "Investor address cannot be zero");
        eligibleInvestors[investor] = eligible;
    }

    /**
     * @dev Purchase tokens. Only eligible investors can buy tokens.
     * @param amount Amount of tokens to buy
     */
    function buyTokens(uint256 amount) external payable {
        require(eligibleInvestors[msg.sender], "Investor is not eligible");
        require(amount > 0, "Purchase amount must be greater than zero");
        require(msg.value == amount * price, "Incorrect Ether value sent");

        contributions[msg.sender] += amount;

        // Transfer tokens to the buyer
        token.transfer(msg.sender, amount);

        emit TokenPurchased(msg.sender, amount);
    }

    /**
     * @dev Withdraw Ether from the contract.
     */
    function withdraw() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No Ether to withdraw");
        
        // Transfer the balance to the owner
        payable(owner()).transfer(balance);
    }

    /**
     * @dev Fallback function to prevent accidental Ether deposits.
     */
    receive() external payable {
        revert("Direct Ether transfers are not allowed");
    }
}
```
