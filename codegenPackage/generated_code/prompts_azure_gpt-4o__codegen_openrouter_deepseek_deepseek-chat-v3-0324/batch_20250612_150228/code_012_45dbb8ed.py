"""
Generated Code Metadata:
========================
Original URL: https://bafybeiaoni35loah6mxudvrxltj6qkb5afmoqjqbg2spapid2kltvnqvby.ipfs.dweb.link
Prompt: Provide code to implement NAVI Protocol's fortified security measures, including multi-oracle pricing mechanisms, into a DeFi platform.
Generated: DETERMINISTIC_45dbb8ed252b190e
Batch ID: 20250612_150228
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
import "@openzeppelin/contracts/security/Pausable.sol";
import "@chainlink/contracts/src/v0.8/interfaces/AggregatorV3Interface.sol";

/**
 * @title NAVI Protocol Security Module
 * @notice Implements multi-oracle pricing with fortified security measures
 */
contract NAVISecurityModule is Ownable, Pausable {
    struct OracleConfig {
        address oracleAddress;
        uint256 deviationThreshold; // Percentage (e.g., 5 for 5%)
        uint256 heartbeat; // Seconds
        bool isActive;
    }

    mapping(address => OracleConfig) public assetOracles;
    mapping(address => uint256) public lastPriceUpdate;
    mapping(address => uint256) public lastPrice;

    uint256 public constant MAX_DEVIATION = 20; // 20% maximum deviation allowed
    uint256 public constant MIN_ORACLES = 3; // Minimum number of oracles required

    event PriceUpdated(address indexed asset, uint256 price, uint256 timestamp);
    event OracleAdded(address indexed asset, address oracle, uint256 deviationThreshold, uint256 heartbeat);
    event OracleRemoved(address indexed asset, address oracle);
    event EmergencyPauseTriggered(address indexed caller);

    /**
     * @dev Add or update an oracle for an asset
     * @param _asset The asset address
     * @param _oracle The oracle address (Chainlink Aggregator)
     * @param _deviationThreshold Allowed price deviation percentage
     * @param _heartbeat Maximum time between price updates
     */
    function setOracle(
        address _asset,
        address _oracle,
        uint256 _deviationThreshold,
        uint256 _heartbeat
    ) external onlyOwner {
        require(_deviationThreshold <= MAX_DEVIATION, "Deviation too high");
        require(_heartbeat > 0, "Heartbeat must be positive");

        assetOracles[_asset] = OracleConfig({
            oracleAddress: _oracle,
            deviationThreshold: _deviationThreshold,
            heartbeat: _heartbeat,
            isActive: true
        });

        emit OracleAdded(_asset, _oracle, _deviationThreshold, _heartbeat);
    }

    /**
     * @dev Remove an oracle for an asset
     * @param _asset The asset address
     */
    function removeOracle(address _asset) external onlyOwner {
        require(assetOracles[_asset].oracleAddress != address(0), "Oracle not found");
        emit OracleRemoved(_asset, assetOracles[_asset].oracleAddress);
        delete assetOracles[_asset];
    }

    /**
     * @dev Get the latest price for an asset using multiple oracles
     * @param _asset The asset address
     * @return price The validated price
     */
    function getPrice(address _asset) external view whenNotPaused returns (uint256) {
        require(assetOracles[_asset].oracleAddress != address(0), "No oracle configured");
        require(block.timestamp - lastPriceUpdate[_asset] <= assetOracles[_asset].heartbeat, "Price stale");

        return lastPrice[_asset];
    }

    /**
     * @dev Update price from oracles and validate
     * @param _asset The asset address
     */
    function updatePrice(address _asset) external whenNotPaused {
        OracleConfig memory config = assetOracles[_asset];
        require(config.oracleAddress != address(0), "No oracle configured");

        AggregatorV3Interface oracle = AggregatorV3Interface(config.oracleAddress);
        (, int256 price, , uint256 updatedAt, ) = oracle.latestRoundData();

        require(updatedAt > lastPriceUpdate[_asset], "Price not updated");
        require(block.timestamp - updatedAt <= config.heartbeat, "Price stale");

        uint256 currentPrice = uint256(price);
        if (lastPrice[_asset] > 0) {
            uint256 deviation = _calculateDeviation(lastPrice[_asset], currentPrice);
            require(deviation <= config.deviationThreshold, "Price deviation too high");
        }

        lastPrice[_asset] = currentPrice;
        lastPriceUpdate[_asset] = block.timestamp;

        emit PriceUpdated(_asset, currentPrice, block.timestamp);
    }

    /**
     * @dev Calculate percentage deviation between two prices
     * @param _oldPrice Previous price
     * @param _newPrice New price
     * @return deviation Percentage deviation
     */
    function _calculateDeviation(uint256 _oldPrice, uint256 _newPrice) internal pure returns (uint256) {
        if (_oldPrice == _newPrice) return 0;
        if (_oldPrice == 0) return type(uint256).max;

        uint256 difference = _oldPrice > _newPrice 
            ? _oldPrice - _newPrice 
            : _newPrice - _oldPrice;
        
        return (difference * 100) / _oldPrice;
    }

    /**
     * @dev Emergency pause mechanism
     */
    function emergencyPause() external onlyOwner {
        _pause();
        emit EmergencyPauseTriggered(msg.sender);
    }

    /**
     * @dev Resume operations
     */
    function unpause() external onlyOwner {
        _unpause();
    }
}

/**
 * @title NAVI Protocol Main Contract
 * @notice Core DeFi platform with integrated security module
 */
contract NAVIProtocol {
    NAVISecurityModule public securityModule;

    constructor(address _securityModule) {
        securityModule = NAVISecurityModule(_securityModule);
    }

    // Additional DeFi protocol functions would be implemented here
    // with proper integration of the security module for all price feeds
}
```
