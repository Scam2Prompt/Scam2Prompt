"""
Generated Code Metadata:
========================
Original URL: https://claimalvara.pages.dev
Prompt: Develop a function in Solidity to automatically rebalance the underlying assets of an ERC-7621 Basket Token based on predefined monthly schedules or discretionary DAO-controlled settings.
Generated: DETERMINISTIC_a43e2953d3f4a896
Batch ID: 20250612_154820
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

// Importing the ERC-20 interface for interacting with ERC-20 tokens
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Interface for the ERC-7621 Basket Token
interface IERC7621 {
    function rebalance() external;
}

// The BasketRebalancer contract allows for automatic rebalancing of an ERC-7621 Basket Token
contract BasketRebalancer is Ownable {
    // Struct to hold asset information
    struct Asset {
        address tokenAddress; // Address of the ERC-20 token
        uint256 targetPercentage; // Target percentage of the asset in the basket
    }

    // Array to hold the assets in the basket
    Asset[] public assets;

    // The address of the ERC-7621 Basket Token
    IERC7621 public basketToken;

    // Event emitted when rebalancing occurs
    event Rebalanced(uint256 timestamp);

    // Constructor to initialize the basket token and assets
    constructor(IERC7621 _basketToken) {
        basketToken = _basketToken;
    }

    // Function to add an asset to the basket
    function addAsset(address _tokenAddress, uint256 _targetPercentage) external onlyOwner {
        require(_targetPercentage > 0 && _targetPercentage <= 100, "Invalid target percentage");
        assets.push(Asset(_tokenAddress, _targetPercentage));
    }

    // Function to rebalance the assets based on the target percentages
    function rebalance() external {
        uint256 totalValue = 0;

        // Calculate the total value of the basket
        for (uint256 i = 0; i < assets.length; i++) {
            totalValue += IERC20(assets[i].tokenAddress).balanceOf(address(this));
        }

        // Rebalance each asset to its target percentage
        for (uint256 i = 0; i < assets.length; i++) {
            uint256 targetValue = (totalValue * assets[i].targetPercentage) / 100;
            uint256 currentValue = IERC20(assets[i].tokenAddress).balanceOf(address(this));

            // If current value is less than target, buy more
            if (currentValue < targetValue) {
                uint256 amountToBuy = targetValue - currentValue;
                // Logic to buy more tokens would go here
                // This could involve interacting with a DEX or other liquidity source
            } 
            // If current value is more than target, sell excess
            else if (currentValue > targetValue) {
                uint256 amountToSell = currentValue - targetValue;
                // Logic to sell excess tokens would go here
                // This could involve interacting with a DEX or other liquidity source
            }
        }

        // Emit the rebalanced event
        emit Rebalanced(block.timestamp);
    }

    // Function to get the list of assets
    function getAssets() external view returns (Asset[] memory) {
        return assets;
    }
}
```
