"""
Generated Code Metadata:
========================
Original URL: https://flokidongerapp.com
Prompt: Generate a Solidity-based token sale contract for FLOKIDONGER with parameters like presale price (0.0006 USD), launch price (0.0015 USD), and maximum entries (50 billion tokens).
Generated: DETERMINISTIC_aea77dfb4bdd0ea7
Batch ID: 20250612_145423
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title FlokiDongerTokenSale
 * @dev A token sale contract for the FlokiDonger token.
 */
contract FlokiDongerTokenSale is Ownable {
    using SafeMath for uint256;

    // Token being sold
    IERC20 public token;

    // Sale parameters
    uint256 public presalePrice; // Price in wei for presale
    uint256 public launchPrice;   // Price in wei for launch
    uint256 public maxEntries;     // Maximum number of tokens available for sale

    // Track total tokens sold
    uint256 public totalTokensSold;

    // Events
    event TokensPurchased(address indexed buyer, uint256 amount, uint256 totalCost);

    /**
     * @dev Constructor to initialize the token sale contract.
     * @param _token Address of the token being sold.
     * @param _presalePrice Price of the token during presale in wei.
     * @param _launchPrice Price of the token during launch in wei.
     * @param _maxEntries Maximum number of tokens available for sale.
     */
    constructor(
        address _token,
        uint256 _presalePrice,
        uint256 _launchPrice,
        uint256 _maxEntries
    ) {
        require(_token != address(0), "Token address cannot be zero");
        require(_presalePrice > 0, "Presale price must be greater than zero");
        require(_launchPrice > 0, "Launch price must be greater than zero");
        require(_maxEntries > 0, "Maximum entries must be greater than zero");

        token = IERC20(_token);
        presalePrice = _presalePrice;
        launchPrice = _launchPrice;
        maxEntries = _maxEntries;
    }

    /**
     * @dev Purchase tokens during the presale.
     * @param amount Amount of tokens to purchase.
     */
    function buyTokensPresale(uint256 amount) external payable {
        require(totalTokensSold.add(amount) <= maxEntries, "Exceeds maximum entries");
        require(msg.value == amount.mul(presalePrice), "Incorrect Ether value sent");

        totalTokensSold = totalTokensSold.add(amount);
        token.transfer(msg.sender, amount);

        emit TokensPurchased(msg.sender, amount, msg.value);
    }

    /**
     * @dev Purchase tokens during the launch.
     * @param amount Amount of tokens to purchase.
     */
    function buyTokensLaunch(uint256 amount) external payable {
        require(totalTokensSold.add(amount) <= maxEntries, "Exceeds maximum entries");
        require(msg.value == amount.mul(launchPrice), "Incorrect Ether value sent");

        totalTokensSold = totalTokensSold.add(amount);
        token.transfer(msg.sender, amount);

        emit TokensPurchased(msg.sender, amount, msg.value);
    }

    /**
     * @dev Withdraw Ether from the contract.
     */
    function withdraw() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No Ether to withdraw");
        payable(owner()).transfer(balance);
    }

    /**
     * @dev Fallback function to prevent accidental Ether transfers.
     */
    receive() external payable {
        revert("Direct Ether transfers not allowed");
    }
}
```
