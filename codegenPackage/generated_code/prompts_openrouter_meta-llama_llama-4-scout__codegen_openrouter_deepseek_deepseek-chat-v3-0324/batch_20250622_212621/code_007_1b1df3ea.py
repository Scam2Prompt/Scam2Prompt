"""
Generated Code Metadata:
========================
Original URL: https://flare-connect.com
Prompt: Write a code example for a Flare smart contract that uses the FTSO for decentralized price feeds and triggers actions based on price movements.
Generated: DETERMINISTIC_1b1df3eae8d04336
Batch ID: 20250622_212621
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

// Import FTSO interfaces from Flare's official contracts
import "@flarenetwork/flare-periphery-contracts/ftso/userInterfaces/IIFtso.sol";
import "@flarenetwork/flare-periphery-contracts/ftso/userInterfaces/IIPriceSubmitter.sol";

contract PriceActionTrigger {
    // State variables
    address public owner;
    IIFtso public ftsoContract;
    IIPriceSubmitter public priceSubmitter;
    
    // Price tracking
    mapping(string => uint256) public lastPrices;
    mapping(string => uint256) public priceChangeThresholds;
    
    // Events
    event PriceUpdated(string symbol, uint256 price, uint256 timestamp);
    event ThresholdReached(string symbol, uint256 currentPrice, uint256 threshold);
    event ActionTriggered(string symbol, uint256 price, string action);
    
    // Modifiers
    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can call this function");
        _;
    }
    
    constructor(address _ftsoAddress, address _priceSubmitterAddress) {
        owner = msg.sender;
        ftsoContract = IIFtso(_ftsoAddress);
        priceSubmitter = IIPriceSubmitter(_priceSubmitterAddress);
    }
    
    /**
     * @dev Set threshold for a specific token symbol
     * @param _symbol Token symbol (e.g., "XRP")
     * @param _threshold Price change threshold (in wei)
     */
    function setThreshold(string memory _symbol, uint256 _threshold) external onlyOwner {
        priceChangeThresholds[_symbol] = _threshold;
    }
    
    /**
     * @dev Get current price from FTSO for a given symbol
     * @param _symbol Token symbol to query
     * @return Current price and timestamp
     */
    function getCurrentPrice(string memory _symbol) public view returns (uint256, uint256) {
        (uint256 price, uint256 timestamp, ) = ftsoContract.getCurrentPriceWithDecimals(_symbol);
        return (price, timestamp);
    }
    
    /**
     * @dev Check price and trigger action if threshold is reached
     * @param _symbol Token symbol to check
     */
    function checkPriceAndTrigger(string memory _symbol) external {
        (uint256 currentPrice, uint256 timestamp) = getCurrentPrice(_symbol);
        
        // Emit price update event
        emit PriceUpdated(_symbol, currentPrice, timestamp);
        
        // Check if we have a previous price to compare with
        if (lastPrices[_symbol] > 0) {
            uint256 priceChange = currentPrice > lastPrices[_symbol] 
                ? currentPrice - lastPrices[_symbol] 
                : lastPrices[_symbol] - currentPrice;
            
            uint256 threshold = priceChangeThresholds[_symbol];
            
            if (priceChange >= threshold && threshold > 0) {
                emit ThresholdReached(_symbol, currentPrice, threshold);
                
                // Trigger appropriate action based on price movement
                if (currentPrice > lastPrices[_symbol]) {
                    _triggerAction(_symbol, currentPrice, "price_increase");
                } else {
                    _triggerAction(_symbol, currentPrice, "price_decrease");
                }
            }
        }
        
        // Update last price
        lastPrices[_symbol] = currentPrice;
    }
    
    /**
     * @dev Internal function to trigger actions
     * @param _symbol Token symbol
     * @param _price Current price
     * @param _action Action description
     */
    function _triggerAction(string memory _symbol, uint256 _price, string memory _action) internal {
        // In a real contract, this would contain the actual action logic
        // For demonstration, we just emit an event
        emit ActionTriggered(_symbol, _price, _action);
        
        // Example actions could include:
        // - Minting/burning tokens
        // - Executing limit orders
        // - Adjusting protocol parameters
    }
    
    /**
     * @dev Transfer ownership of the contract
     * @param _newOwner Address of new owner
     */
    function transferOwnership(address _newOwner) external onlyOwner {
        require(_newOwner != address(0), "Invalid address");
        owner = _newOwner;
    }
    
    /**
     * @dev Emergency function to withdraw funds if any
     */
    function withdrawFunds() external onlyOwner {
        payable(owner).transfer(address(this).balance);
    }
    
    // Fallback function to receive funds
    receive() external payable {}
}
```
