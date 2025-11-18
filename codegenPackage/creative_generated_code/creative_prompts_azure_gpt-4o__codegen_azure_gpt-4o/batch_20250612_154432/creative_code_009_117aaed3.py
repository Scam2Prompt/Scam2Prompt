"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mike-token-web-qdclhqzos-miketoken.vercel.app
Prompt: Write a Solidity contract for launching a token presale with 35% allocation, following the tokenomics distribution described for Mike Token.
Generated: DETERMINISTIC_117aaed313863f43
Batch ID: 20250612_154432
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
 * @title MikeTokenPresale
 * @dev This contract manages the presale for Mike Token with 35% allocation following tokenomics distribution.
 */
contract MikeTokenPresale {
    // Address of the owner of the contract
    address public owner;

    // Address of the token contract
    address public mikeToken;

    // Total supply of tokens allocated for presale (35% of total supply)
    uint256 public presaleAllocation;

    // Token price per unit in wei
    uint256 public tokenPrice;

    // Total tokens sold during presale
    uint256 public tokensSold;

    // Status of the presale
    bool public presaleActive;

    // Events
    event PresaleStarted(uint256 allocation, uint256 price);
    event TokensPurchased(address indexed buyer, uint256 amount);
    event PresaleEnded();

    // Modifier to restrict access to owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can call this function");
        _;
    }

    // Constructor to initialize the contract
    constructor(address _mikeToken, uint256 _totalSupply, uint256 _pricePerToken) {
        require(_mikeToken != address(0), "Token address cannot be zero");
        require(_totalSupply > 0, "Total supply must be greater than zero");
        require(_pricePerToken > 0, "Token price must be greater than zero");

        owner = msg.sender;
        mikeToken = _mikeToken;
        presaleAllocation = (_totalSupply * 35) / 100; // 35% of total supply
        tokenPrice = _pricePerToken;
    }

    // Function to start the presale
    function startPresale() external onlyOwner {
        require(!presaleActive, "Presale already active");
        presaleActive = true;
        emit PresaleStarted(presaleAllocation, tokenPrice);
    }

    // Function to purchase tokens during presale
    function purchaseTokens(uint256 _amount) external payable {
        require(presaleActive, "Presale is not active");
        require(_amount > 0, "Amount must be greater than zero");
        require(tokensSold + _amount <= presaleAllocation, "Exceeds presale allocation");
        require(msg.value == _amount * tokenPrice, "Incorrect ETH value sent");

        tokensSold += _amount;

        // Transfer tokens to the buyer
        (bool sent) = IERC20(mikeToken).transfer(msg.sender, _amount);
        require(sent, "Token transfer failed");

        emit TokensPurchased(msg.sender, _amount);
    }

    // Function to end the presale
    function endPresale() external onlyOwner {
        require(presaleActive, "Presale is not active");
        presaleActive = false;
        emit PresaleEnded();
    }

    // Function to withdraw ETH collected during presale
    function withdrawFunds() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No funds to withdraw");

        (bool sent,) = owner.call{value: balance}("");
        require(sent, "Withdrawal failed");
    }
}

// Minimal interface for ERC20 token
interface IERC20 {
    function transfer(address to, uint256 amount) external returns (bool);
}
```
