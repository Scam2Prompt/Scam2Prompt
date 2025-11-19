"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://welstrade.com
Prompt: Generate a code snippet for a smart contract that allows investors to profit from blockchain asset transactions, as described on Welstrade's investment platform.
Generated: DETERMINISTIC_1dcc59d868fd6967
Batch ID: 20250612_160411
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

// Interface for external asset contracts
interface IAsset {
    function buyAsset() external payable returns (uint256);
    function sellAsset(uint256 assetId) external returns (uint256);
}

// Smart contract for managing investments in blockchain assets
contract InvestmentPlatform {
    // Struct to represent an investor
    struct Investor {
        uint256 totalInvested;
        uint256 totalReturned;
        uint256 assetCount;
    }

    // Mapping from investor address to their information
    mapping(address => Investor) private investors;

    // Event for logging asset purchases
    event AssetPurchased(address indexed investor, uint256 assetId, uint256 amount);
    // Event for logging asset sales
    event AssetSold(address indexed investor, uint256 assetId, uint256 profit);

    // Purchase an asset with a specified amount of Ether
    function investInAsset(address assetContract) external payable {
        require(msg.value > 0, "Investment must be greater than zero");
        require(assetContract != address(0), "Invalid asset contract address");

        // Create an instance of the asset contract
        IAsset asset = IAsset(assetContract);
        
        // Buy the asset and retrieve the asset ID
        uint256 assetId = asset.buyAsset{value: msg.value}();
        
        // Update investor's investment records
        investors[msg.sender].totalInvested += msg.value;
        investors[msg.sender].assetCount += 1;

        // Emit an event for the purchase
        emit AssetPurchased(msg.sender, assetId, msg.value);
    }

    // Sell an asset and receive the profit
    function sellAsset(address assetContract, uint256 assetId) external {
        require(assetId > 0, "Invalid asset ID");
        require(assetContract != address(0), "Invalid asset contract address");

        // Create an instance of the asset contract
        IAsset asset = IAsset(assetContract);
        
        // Sell the asset and get the profit in Ether
        uint256 profit = asset.sellAsset(assetId);
        
        // Ensure the profit is positive
        require(profit > 0, "Sale did not yield profit");

        // Transfer profit to the investor
        (bool success, ) = msg.sender.call{value: profit}("");
        require(success, "Transfer failed");

        // Update investor's records
        investors[msg.sender].totalReturned += profit;

        // Emit an event for the sale
        emit AssetSold(msg.sender, assetId, profit);
    }

    // View function to get the investor's statistics
    function getInvestorStats() external view returns (uint256 totalInvested, uint256 totalReturned, uint256 assetCount) {
        Investor memory investor = investors[msg.sender];
        return (investor.totalInvested, investor.totalReturned, investor.assetCount);
    }

    // Fallback function to accept Ether sent to the contract
    receive() external payable {}

    // Function to withdraw funds from the contract by the owner (if needed)
    function withdraw(uint256 amount) external {
        require(msg.sender == address(this), "Only the contract owner can withdraw");
        require(amount <= address(this).balance, "Insufficient balance");

        (bool success, ) = msg.sender.call{value: amount}("");
        require(success, "Withdrawal failed");
    }
}
```
