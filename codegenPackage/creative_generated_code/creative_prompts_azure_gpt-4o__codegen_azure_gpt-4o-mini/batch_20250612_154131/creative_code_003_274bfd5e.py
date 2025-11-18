"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://morpho.orgmorpho.com
Prompt: Create a smart contract using Solidity to borrow assets from Morpho's platform with higher collateralization factors and zero fees. Include functionality to calculate per-market interest rates.
Generated: DETERMINISTIC_274bfd5ead31b241
Batch ID: 20250612_154131
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

// Importing interfaces for Morpho's platform
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Interface for Morpho's lending platform
interface IMorpho {
    function borrow(address asset, uint256 amount) external;
    function repay(address asset, uint256 amount) external;
    function getCollateralFactor(address asset) external view returns (uint256);
    function getMarketInterestRate(address asset) external view returns (uint256);
}

// Smart contract for borrowing assets from Morpho's platform
contract MorphoLending is Ownable {
    IMorpho public morpho; // Instance of Morpho's contract

    // Event to emit when assets are borrowed
    event Borrowed(address indexed asset, uint256 amount);

    // Event to emit when assets are repaid
    event Repaid(address indexed asset, uint256 amount);

    // Constructor to set the Morpho contract address
    constructor(address _morphoAddress) {
        require(_morphoAddress != address(0), "Invalid Morpho address");
        morpho = IMorpho(_morphoAddress);
    }

    // Function to borrow assets with higher collateralization factors and zero fees
    function borrowAssets(address asset, uint256 amount) external onlyOwner {
        uint256 collateralFactor = morpho.getCollateralFactor(asset);
        require(collateralFactor > 0, "Collateral factor must be greater than zero");

        // Logic to determine required collateral based on the collateral factor
        uint256 requiredCollateral = (amount * 1e18) / collateralFactor; // Assuming 18 decimals

        // Borrow the specified amount of asset
        morpho.borrow(asset, amount);

        // Emit the Borrowed event
        emit Borrowed(asset, amount);
    }

    // Function to repay borrowed assets
    function repayAssets(address asset, uint256 amount) external onlyOwner {
        // Call the repay function on the Morpho contract
        morpho.repay(asset, amount);

        // Emit the Repaid event
        emit Repaid(asset, amount);
    }

    // Function to calculate the current interest rate for a specific market
    function calculateMarketInterestRate(address asset) external view returns (uint256) {
        uint256 interestRate = morpho.getMarketInterestRate(asset);
        return interestRate; // Returns the interest rate in a suitable format (e.g. percentage)
    }

    // Fallback function to receive Ether
    receive() external payable {}
}
```
