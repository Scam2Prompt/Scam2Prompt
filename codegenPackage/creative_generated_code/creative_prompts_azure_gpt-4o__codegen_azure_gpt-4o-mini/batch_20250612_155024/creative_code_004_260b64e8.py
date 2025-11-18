"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pythgame.com
Prompt: Write code to validate and update market data in a smart contract using Pyth Network's oracle services.
Generated: DETERMINISTIC_260b64e895135bf5
Batch ID: 20250612_155024
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

// Interface for the Pyth Network's Price Feed
interface IPyth {
    function getPrice(string memory symbol) external view returns (int256 price, uint256 publishTime);
}

/**
 * @title Market Data Validator
 * @dev This contract updates market data using Pyth Network's oracle services.
 */
contract MarketDataValidator {
    IPyth public pyth; // Pyth Network price feed contract
    address public owner; // Owner of the contract
    string public symbol; // Symbol for the market data

    // Event emitted when market data is updated
    event MarketDataUpdated(int256 price, uint256 timestamp);

    /**
     * @dev Constructor to initialize the contract with Pyth contract address and market symbol.
     * @param _pyth Address of the Pyth Network's Price Feed contract
     * @param _symbol The market symbol to track
     */
    constructor(address _pyth, string memory _symbol) {
        require(_pyth != address(0), "Pyth address cannot be zero");
        pyth = IPyth(_pyth);
        owner = msg.sender;
        symbol = _symbol;
    }

    /**
     * @dev Update market data from the Pyth Network.
     * Emits a MarketDataUpdated event on success.
     */
    function updateMarketData() external {
        (int256 price, uint256 publishTime) = pyth.getPrice(symbol);
        
        // Check if the price is valid
        require(price > 0, "Invalid price received");

        emit MarketDataUpdated(price, publishTime);
    }

    /**
     * @dev Modifier to restrict function access to the owner.
     */
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    /**
     * @dev Function to update the Pyth contract address.
     * @param _newPyth The new Pyth Network's Price Feed contract address
     */
    function updatePythAddress(address _newPyth) external onlyOwner {
        require(_newPyth != address(0), "New Pyth address cannot be zero");
        pyth = IPyth(_newPyth);
    }

    /**
     * @dev Function to change the symbol being tracked.
     * @param _newSymbol The new market symbol to track
     */
    function updateSymbol(string memory _newSymbol) external onlyOwner {
        symbol = _newSymbol;
    }
}
```
