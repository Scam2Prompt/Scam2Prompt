"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pythim.com
Prompt: Write a Solidity smart contract that incorporates Pythim's price feed oracles to calculate the value of a portfolio in real-time.
Generated: DETERMINISTIC_e109e08e456ec348
Batch ID: 20250612_155048
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

// Import the Pyth interface
import "@pythnetwork/pyth-sdk-solidity/IPyth.sol";

contract PortfolioValueCalculator {
    // State variables
    address public owner;
    IPyth public pythInstance;

    struct Asset {
        string assetId;       // Unique asset identifier (e.g., symbol or product ID)
        uint256 amount;       // Amount of the asset
        bool exists;          // Ensure asset is tracked in the portfolio
    }

    mapping(string => Asset) public portfolioAssets; // Mapping assetId => Asset

    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    event PortfolioUpdated(string assetId, uint256 amount);
    event AssetRemoved(string assetId);

    constructor(address _pythInstanceAddress) {
        require(_pythInstanceAddress != address(0), "Invalid Pyth instance address");
        owner = msg.sender;
        pythInstance = IPyth(_pythInstanceAddress);
    }

    /**
     * @dev Add or update an asset in the portfolio.
     * @param assetId The unique identifier of the asset (e.g., symbol).
     * @param amount The amount of the asset in the portfolio.
     */
    function updateAsset(string memory assetId, uint256 amount) public onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        portfolioAssets[assetId] = Asset(assetId, amount, true);
        emit PortfolioUpdated(assetId, amount);
    }

    /**
     * @dev Remove an asset from the portfolio.
     * @param assetId The unique identifier of the asset to remove.
     */
    function removeAsset(string memory assetId) public onlyOwner {
        require(portfolioAssets[assetId].exists, "Asset does not exist");
        delete portfolioAssets[assetId];
        emit AssetRemoved(assetId);
    }

    /**
     * @dev Fetch the real-time value of the portfolio using Pyth price feed oracles.
     * @param priceIds List of Pyth price IDs corresponding to the assets in the portfolio.
     * @return portfolioValue The total value of the portfolio in USD (or another base currency).
     */
    function getPortfolioValue(bytes32[] memory priceIds) public view returns (uint256 portfolioValue) {
        portfolioValue = 0;

        for (uint256 i = 0; i < priceIds.length; i++) {
            bytes32 priceId = priceIds[i];
            string memory assetId = abi.decode(abi.encodePacked(priceId), (string));
            
            // Skip if the asset is not in the portfolio
            if (!portfolioAssets[assetId].exists) {
                continue;
            }

            // Get the price data from Pyth oracle
            IPyth.Price memory priceData = pythInstance.getPriceUnsafe(priceId);

            // Ensure the price data is valid
            require(priceData.price > 0, "Invalid price data");
            require(priceData.expo <= 0, "Invalid price exponent");

            // Calculate the asset value based on its price and amount
            uint256 assetValue = (portfolioAssets[assetId].amount * uint256(priceData.price)) / (10 ** uint256(-priceData.expo));
            portfolioValue += assetValue;
        }

        return portfolioValue;
    }
}
```
