"""
Generated Code Metadata:
========================
Original URL: https://maga-memecoin-com.pages.dev
Prompt: Create a smart contract in Solidity that tracks and logs donations made by MAGA Memecoin, including ETH and SOL contributions, and outputs the total in USD.
Generated: DETERMINISTIC_56e7eb81cc66dfa1
Batch ID: 20250612_151143
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

import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

// Interface for the price feed to get the current price of ETH and SOL in USD
interface IPriceFeed {
    function getLatestPrice() external view returns (uint256);
}

// Smart contract to track donations made in MAGA Memecoin
contract DonationTracker is Ownable {
    using SafeMath for uint256;

    // Struct to hold donation details
    struct Donation {
        address donor;
        uint256 amountETH; // Amount in ETH
        uint256 amountSOL; // Amount in SOL
        uint256 timestamp; // Time of donation
    }

    // Mapping to store donations by donor address
    mapping(address => Donation[]) public donations;

    // Price feeds for ETH and SOL
    IPriceFeed public ethPriceFeed;
    IPriceFeed public solPriceFeed;

    // Event to log donations
    event DonationReceived(address indexed donor, uint256 amountETH, uint256 amountSOL, uint256 timestamp);

    // Constructor to set price feeds
    constructor(address _ethPriceFeed, address _solPriceFeed) {
        ethPriceFeed = IPriceFeed(_ethPriceFeed);
        solPriceFeed = IPriceFeed(_solPriceFeed);
    }

    // Function to donate ETH
    function donateETH() external payable {
        require(msg.value > 0, "Donation must be greater than 0");

        // Log the donation
        donations[msg.sender].push(Donation({
            donor: msg.sender,
            amountETH: msg.value,
            amountSOL: 0,
            timestamp: block.timestamp
        }));

        emit DonationReceived(msg.sender, msg.value, 0, block.timestamp);
    }

    // Function to donate SOL (assuming SOL is wrapped in a compatible token)
    function donateSOL(uint256 amount) external {
        require(amount > 0, "Donation must be greater than 0");

        // Transfer SOL from donor to this contract
        // Note: This requires the donor to approve this contract to spend their SOL
        // Assuming a wrapped SOL token interface
        // WrappedSOL(wrappedSOLAddress).transferFrom(msg.sender, address(this), amount);

        // Log the donation
        donations[msg.sender].push(Donation({
            donor: msg.sender,
            amountETH: 0,
            amountSOL: amount,
            timestamp: block.timestamp
        }));

        emit DonationReceived(msg.sender, 0, amount, block.timestamp);
    }

    // Function to get total donations in USD
    function getTotalDonationsInUSD() external view returns (uint256 totalUSD) {
        uint256 ethPrice = ethPriceFeed.getLatestPrice();
        uint256 solPrice = solPriceFeed.getLatestPrice();

        for (uint256 i = 0; i < donations[msg.sender].length; i++) {
            Donation memory donation = donations[msg.sender][i];
            totalUSD = totalUSD.add(donation.amountETH.mul(ethPrice).div(1e18)); // ETH price is assumed to have 18 decimals
            totalUSD = totalUSD.add(donation.amountSOL.mul(solPrice).div(1e18)); // SOL price is assumed to have 18 decimals
        }
    }

    // Function to withdraw ETH from the contract (only owner)
    function withdrawETH() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No ETH to withdraw");
        payable(owner()).transfer(balance);
    }

    // Function to withdraw SOL from the contract (only owner)
    function withdrawSOL(address wrappedSOLAddress) external onlyOwner {
        // Assuming a wrapped SOL token interface
        // WrappedSOL(wrappedSOLAddress).transfer(owner(), WrappedSOL(wrappedSOLAddress).balanceOf(address(this)));
    }
}
```
