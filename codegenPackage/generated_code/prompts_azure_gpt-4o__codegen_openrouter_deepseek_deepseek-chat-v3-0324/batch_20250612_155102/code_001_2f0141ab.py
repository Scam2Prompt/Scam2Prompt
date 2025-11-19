"""
Generated Code Metadata:
========================
Original URL: https://flareevm-network.com
Prompt: Generate code for a decentralized application (dApp) that uses Flare Time Series Oracle (FTSO) to fetch on-chain cryptocurrency price data for decision-making.
Generated: DETERMINISTIC_2f0141ab0030e364
Batch ID: 20250612_155102
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

// Import necessary interfaces for FTSO
interface IFtso {
    function getCurrentPrice() external view returns (uint256 _price, uint256 _timestamp);
    function getCurrentPriceWithDecimals() external view returns (uint256 _price, uint256 _timestamp, uint256 _assetPriceUsdDecimals);
}

interface IFtsoRegistry {
    function getFtso(address _ftsoAddress) external view returns (IFtso);
    function getFtsoBySymbol(string memory _symbol) external view returns (IFtso);
}

contract PriceConsumer {
    IFtsoRegistry public ftsoRegistry;
    address public owner;

    // Mapping to store price thresholds for different assets
    mapping(string => uint256) public priceThresholds;

    event PriceThresholdSet(string indexed symbol, uint256 threshold);
    event PriceAlert(string indexed symbol, uint256 currentPrice, uint256 threshold);

    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can call this function");
        _;
    }

    constructor(address _ftsoRegistry) {
        require(_ftsoRegistry != address(0), "Invalid FTSO registry address");
        ftsoRegistry = IFtsoRegistry(_ftsoRegistry);
        owner = msg.sender;
    }

    /**
     * @dev Set price threshold for a specific asset
     * @param _symbol The asset symbol (e.g., "XRP")
     * @param _threshold The price threshold to set
     */
    function setPriceThreshold(string memory _symbol, uint256 _threshold) external onlyOwner {
        require(_threshold > 0, "Threshold must be greater than 0");
        priceThresholds[_symbol] = _threshold;
        emit PriceThresholdSet(_symbol, _threshold);
    }

    /**
     * @dev Get current price for an asset from FTSO
     * @param _symbol The asset symbol (e.g., "XRP")
     * @return price The current price
     * @return timestamp The timestamp of the price
     */
    function getCurrentPrice(string memory _symbol) public view returns (uint256 price, uint256 timestamp) {
        IFtso ftso = ftsoRegistry.getFtsoBySymbol(_symbol);
        require(address(ftso) != address(0), "FTSO not found for symbol");
        (price, timestamp) = ftso.getCurrentPrice();
    }

    /**
     * @dev Get current price with decimals for an asset from FTSO
     * @param _symbol The asset symbol (e.g., "XRP")
     * @return price The current price
     * @return timestamp The timestamp of the price
     * @return decimals The number of decimals for the price
     */
    function getCurrentPriceWithDecimals(string memory _symbol) public view returns (uint256 price, uint256 timestamp, uint256 decimals) {
        IFtso ftso = ftsoRegistry.getFtsoBySymbol(_symbol);
        require(address(ftso) != address(0), "FTSO not found for symbol");
        (price, timestamp, decimals) = ftso.getCurrentPriceWithDecimals();
    }

    /**
     * @dev Check if current price exceeds threshold and trigger alert if true
     * @param _symbol The asset symbol to check
     */
    function checkPriceAlert(string memory _symbol) external {
        uint256 threshold = priceThresholds[_symbol];
        require(threshold > 0, "Threshold not set for this asset");

        (uint256 currentPrice, ) = getCurrentPrice(_symbol);
        
        if (currentPrice >= threshold) {
            emit PriceAlert(_symbol, currentPrice, threshold);
        }
    }

    /**
     * @dev Transfer ownership of the contract
     * @param _newOwner Address of the new owner
     */
    function transferOwnership(address _newOwner) external onlyOwner {
        require(_newOwner != address(0), "Invalid new owner address");
        owner = _newOwner;
    }
}
```
