"""
Generated Code Metadata:
========================
Original URL: https://connectflrlines.com
Prompt: Write a smart contract that utilizes the Flare Time Series Oracle to fetch decentralized price feeds for a DeFi application.
Generated: DETERMINISTIC_8b9d06bc47e7599b
Batch ID: 20250612_161005
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

// Import Flare's FTSO interfaces
import "@flarenetwork/flare-smart-contracts/contracts/ftso/interface/IFtso.sol";
import "@flarenetwork/flare-smart-contracts/contracts/ftso/interface/IFtsoRegistry.sol";
import "@flarenetwork/flare-smart-contracts/contracts/ftso/interface/IWNat.sol";

/**
 * @title PriceFeedConsumer
 * @dev A smart contract that fetches decentralized price feeds from Flare's FTSO
 */
contract PriceFeedConsumer {
    IFtsoRegistry public ftsoRegistry;
    IWNat public wNat;

    // Mapping to store the symbol to FTSO index
    mapping(string => uint256) public symbolToFtsoIndex;

    // Events
    event PriceUpdated(string indexed symbol, uint256 price, uint256 timestamp);
    event FtsoIndexSet(string indexed symbol, uint256 index);

    /**
     * @dev Constructor initializes the FTSO Registry and WNat contracts
     * @param _ftsoRegistry Address of the FTSO Registry contract
     * @param _wNat Address of the Wrapped Native token contract
     */
    constructor(address _ftsoRegistry, address _wNat) {
        require(_ftsoRegistry != address(0), "Invalid FTSO Registry address");
        require(_wNat != address(0), "Invalid WNat address");
        
        ftsoRegistry = IFtsoRegistry(_ftsoRegistry);
        wNat = IWNat(_wNat);
    }

    /**
     * @dev Sets the FTSO index for a given symbol
     * @param _symbol The symbol/asset identifier (e.g., "XRP", "BTC")
     * @param _index The index of the FTSO in the registry
     */
    function setFtsoIndex(string memory _symbol, uint256 _index) external {
        require(bytes(_symbol).length > 0, "Symbol cannot be empty");
        require(_index < ftsoRegistry.getSupportedIndicesLength(), "Invalid FTSO index");

        symbolToFtsoIndex[_symbol] = _index;
        emit FtsoIndexSet(_symbol, _index);
    }

    /**
     * @dev Fetches the current price for a given symbol
     * @param _symbol The symbol/asset identifier
     * @return price The current price
     * @return timestamp The timestamp of the price update
     */
    function getCurrentPrice(string memory _symbol) 
        external 
        view 
        returns (uint256 price, uint256 timestamp) 
    {
        require(bytes(_symbol).length > 0, "Symbol cannot be empty");
        uint256 index = symbolToFtsoIndex[_symbol];
        require(index != 0 || keccak256(bytes(_symbol)) == keccak256(bytes("FLR")), "FTSO index not set");

        IFtso ftso = ftsoRegistry.getFtso(index);
        (price, timestamp) = ftso.getCurrentPrice();
    }

    /**
     * @dev Fetches the price at a specific epoch for a given symbol
     * @param _symbol The symbol/asset identifier
     * @param _epochId The epoch ID to query
     * @return price The price at the specified epoch
     * @return timestamp The timestamp of the price update
     */
    function getPriceAtEpoch(string memory _symbol, uint256 _epochId) 
        external 
        view 
        returns (uint256 price, uint256 timestamp) 
    {
        require(bytes(_symbol).length > 0, "Symbol cannot be empty");
        uint256 index = symbolToFtsoIndex[_symbol];
        require(index != 0 || keccak256(bytes(_symbol)) == keccak256(bytes("FLR")), "FTSO index not set");

        IFtso ftso = ftsoRegistry.getFtso(index);
        (price, timestamp) = ftso.getEpochPrice(_epochId);
    }

    /**
     * @dev Fetches the price and updates the contract state
     * @param _symbol The symbol/asset identifier
     * @return price The current price
     * @return timestamp The timestamp of the price update
     */
    function updatePrice(string memory _symbol) 
        external 
        returns (uint256 price, uint256 timestamp) 
    {
        require(bytes(_symbol).length > 0, "Symbol cannot be empty");
        uint256 index = symbolToFtsoIndex[_symbol];
        require(index != 0 || keccak256(bytes(_symbol)) == keccak256(bytes("FLR")), "FTSO index not set");

        IFtso ftso = ftsoRegistry.getFtso(index);
        (price, timestamp) = ftso.getCurrentPrice();

        emit PriceUpdated(_symbol, price, timestamp);
    }

    /**
     * @dev Delegates votes to a price provider for better accuracy
     * @param _to The address to delegate to
     */
    function delegateVotes(address _to) external {
        require(_to != address(0), "Cannot delegate to zero address");
        wNat.delegate(_to);
    }
}
```
