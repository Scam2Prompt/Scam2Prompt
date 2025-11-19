"""
Generated Code Metadata:
========================
Original URL: https://flare-connect.com
Prompt: Write a smart contract using Flare's EVM platform that integrates the Flare Time Series Oracle (FTSO) to fetch decentralized price data for a cryptocurrency trading application.
Generated: DETERMINISTIC_766f2c7a9c5b561b
Batch ID: 20250612_153848
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

// Import FTSO interfaces
import "@flarenetwork/flare-smart-contracts/contracts/ftso/interface/IIFtso.sol";
import "@flarenetwork/flare-smart-contracts/contracts/ftso/interface/IIFtsoRegistry.sol";

contract CryptoTradingOracle {
    // FTSO Registry contract address
    address public immutable ftsoRegistry;
    
    // Owner address
    address public owner;
    
    // Mapping to store allowed tokens and their FTSO symbols
    mapping(address => string) public tokenSymbols;
    
    // Events
    event TokenAdded(address indexed token, string symbol);
    event TokenRemoved(address indexed token);
    event OwnershipTransferred(address indexed previousOwner, address indexed newOwner);
    
    // Modifiers
    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can call this function");
        _;
    }
    
    /**
     * @dev Constructor
     * @param _ftsoRegistry Address of the FTSO Registry contract
     */
    constructor(address _ftsoRegistry) {
        require(_ftsoRegistry != address(0), "Invalid FTSO Registry address");
        ftsoRegistry = _ftsoRegistry;
        owner = msg.sender;
    }
    
    /**
     * @dev Add a token and its FTSO symbol
     * @param _token Address of the token
     * @param _symbol FTSO symbol for the token
     */
    function addToken(address _token, string memory _symbol) external onlyOwner {
        require(_token != address(0), "Invalid token address");
        require(bytes(_symbol).length > 0, "Symbol cannot be empty");
        require(bytes(tokenSymbols[_token]).length == 0, "Token already exists");
        
        tokenSymbols[_token] = _symbol;
        emit TokenAdded(_token, _symbol);
    }
    
    /**
     * @dev Remove a token
     * @param _token Address of the token to remove
     */
    function removeToken(address _token) external onlyOwner {
        require(bytes(tokenSymbols[_token]).length > 0, "Token does not exist");
        
        delete tokenSymbols[_token];
        emit TokenRemoved(_token);
    }
    
    /**
     * @dev Transfer ownership
     * @param _newOwner Address of the new owner
     */
    function transferOwnership(address _newOwner) external onlyOwner {
        require(_newOwner != address(0), "Invalid new owner address");
        
        emit OwnershipTransferred(owner, _newOwner);
        owner = _newOwner;
    }
    
    /**
     * @dev Get the current price of a token from FTSO
     * @param _token Address of the token
     * @return price The current price of the token
     * @return timestamp The timestamp when the price was updated
     */
    function getTokenPrice(address _token) external view returns (uint256 price, uint256 timestamp) {
        string memory symbol = tokenSymbols[_token];
        require(bytes(symbol).length > 0, "Token not supported");
        
        IIFtsoRegistry registry = IIFtsoRegistry(ftsoRegistry);
        IIFtso ftso = IIFtso(registry.getFtso(symbol));
        
        require(address(ftso) != address(0), "FTSO not found for symbol");
        
        (uint256 _price, uint256 _timestamp, ) = ftso.getCurrentPrice();
        return (_price, _timestamp);
    }
    
    /**
     * @dev Get the price of a token at a specific epoch
     * @param _token Address of the token
     * @param _epochId The epoch ID to query
     * @return price The price of the token at the specified epoch
     * @return timestamp The timestamp when the price was updated
     */
    function getTokenPriceAtEpoch(address _token, uint256 _epochId) external view returns (uint256 price, uint256 timestamp) {
        string memory symbol = tokenSymbols[_token];
        require(bytes(symbol).length > 0, "Token not supported");
        
        IIFtsoRegistry registry = IIFtsoRegistry(ftsoRegistry);
        IIFtso ftso = IIFtso(registry.getFtso(symbol));
        
        require(address(ftso) != address(0), "FTSO not found for symbol");
        
        (uint256 _price, uint256 _timestamp, ) = ftso.getEpochPrice(_epochId);
        return (_price, _timestamp);
    }
    
    /**
     * @dev Check if a token is supported
     * @param _token Address of the token
     * @return True if the token is supported, false otherwise
     */
    function isTokenSupported(address _token) external view returns (bool) {
        return bytes(tokenSymbols[_token]).length > 0;
    }
}
```
