"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://flokidongerapp.com
Prompt: Generate a Solidity-based token sale contract for FLOKIDONGER with parameters like presale price (0.0006 USD), launch price (0.0015 USD), and maximum entries (50 billion tokens).
Generated: DETERMINISTIC_aea77dfb4bdd0ea7
Batch ID: 20250612_145423
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
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

contract FlokidongerTokenSale is Ownable {
    using SafeMath for uint256;

    // Token being sold
    IERC20 public token;

    // Sale parameters
    uint256 public presalePrice; // Price in wei for presale
    uint256 public launchPrice;   // Price in wei for launch
    uint256 public maxEntries;    // Maximum tokens available for sale
    uint256 public totalSold;      // Tokens sold so far

    // Sale state
    bool public presaleActive;
    bool public launchActive;

    // Events
    event TokensPurchased(address indexed buyer, uint256 amount, uint256 totalCost);
    event SaleStateChanged(bool presaleActive, bool launchActive);

    // Constructor to set the token and prices
    constructor(IERC20 _token, uint256 _presalePrice, uint256 _launchPrice, uint256 _maxEntries) {
        token = _token;
        presalePrice = _presalePrice;
        launchPrice = _launchPrice;
        maxEntries = _maxEntries;
        totalSold = 0;
        presaleActive = false;
        launchActive = false;
    }

    // Modifier to check if the presale is active
    modifier onlyDuringPresale() {
        require(presaleActive, "Presale is not active");
        _;
    }

    // Modifier to check if the launch is active
    modifier onlyDuringLaunch() {
        require(launchActive, "Launch is not active");
        _;
    }

    // Function to start presale
    function startPresale() external onlyOwner {
        presaleActive = true;
        launchActive = false;
        emit SaleStateChanged(presaleActive, launchActive);
    }

    // Function to start launch
    function startLaunch() external onlyOwner {
        require(totalSold >= maxEntries, "Presale must be completed before launch");
        launchActive = true;
        presaleActive = false;
        emit SaleStateChanged(presaleActive, launchActive);
    }

    // Function to purchase tokens during presale
    function buyTokensPresale(uint256 _amount) external payable onlyDuringPresale {
        require(_amount > 0, "Amount must be greater than zero");
        require(totalSold.add(_amount) <= maxEntries, "Exceeds maximum entries");

        uint256 totalCost = presalePrice.mul(_amount);
        require(msg.value >= totalCost, "Insufficient Ether sent");

        totalSold = totalSold.add(_amount);
        token.transfer(msg.sender, _amount);

        // Refund excess Ether
        if (msg.value > totalCost) {
            payable(msg.sender).transfer(msg.value.sub(totalCost));
        }

        emit TokensPurchased(msg.sender, _amount, totalCost);
    }

    // Function to purchase tokens during launch
    function buyTokensLaunch(uint256 _amount) external payable onlyDuringLaunch {
        require(_amount > 0, "Amount must be greater than zero");
        require(totalSold.add(_amount) <= maxEntries, "Exceeds maximum entries");

        uint256 totalCost = launchPrice.mul(_amount);
        require(msg.value >= totalCost, "Insufficient Ether sent");

        totalSold = totalSold.add(_amount);
        token.transfer(msg.sender, _amount);

        // Refund excess Ether
        if (msg.value > totalCost) {
            payable(msg.sender).transfer(msg.value.sub(totalCost));
        }

        emit TokensPurchased(msg.sender, _amount, totalCost);
    }

    // Function to withdraw funds raised from the sale
    function withdrawFunds() external onlyOwner {
        payable(owner()).transfer(address(this).balance);
    }

    // Function to withdraw unsold tokens
    function withdrawUnsoldTokens() external onlyOwner {
        require(!presaleActive && !launchActive, "Cannot withdraw tokens while sale is active");
        uint256 unsoldTokens = token.balanceOf(address(this));
        token.transfer(owner(), unsoldTokens);
    }

    // Function to check the contract's balance
    function contractBalance() external view returns (uint256) {
        return address(this).balance;
    }
}
```
