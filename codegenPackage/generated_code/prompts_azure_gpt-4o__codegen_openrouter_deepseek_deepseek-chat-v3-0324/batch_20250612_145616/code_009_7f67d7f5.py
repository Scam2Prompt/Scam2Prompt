"""
Generated Code Metadata:
========================
Original URL: https://arbitrum.gmx-oracle.io
Prompt: Provide an example of using GMX oracle data to trigger automated smart contract functions based on price thresholds on Arbitrum.
Generated: DETERMINISTIC_7f67d7f57739eb64
Batch ID: 20250612_145616
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

// Interface for Chainlink Price Feed
interface AggregatorV3Interface {
    function decimals() external view returns (uint8);
    function description() external view returns (string memory);
    function version() external view returns (uint256);
    function getRoundData(uint80 _roundId)
        external
        view
        returns (
            uint80 roundId,
            int256 answer,
            uint256 startedAt,
            uint256 updatedAt,
            uint80 answeredInRound
        );
    function latestRoundData()
        external
        view
        returns (
            uint80 roundId,
            int256 answer,
            uint256 startedAt,
            uint256 updatedAt,
            uint80 answeredInRound
        );
}

contract PriceThresholdTrigger {
    AggregatorV3Interface internal priceFeed;
    address public owner;
    uint256 public thresholdPrice;
    bool public thresholdReached;
    
    // GMX uses Chainlink oracles on Arbitrum
    // Example: ETH/USD price feed on Arbitrum - 0x639Fe6ab55C921f74e7fac1ee960C0B6293ba612
    constructor(address _priceFeedAddress, uint256 _thresholdPrice) {
        priceFeed = AggregatorV3Interface(_priceFeedAddress);
        thresholdPrice = _thresholdPrice;
        owner = msg.sender;
        thresholdReached = false;
    }
    
    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can call this function");
        _;
    }
    
    function checkPriceThreshold() public returns (bool) {
        (
            /*uint80 roundID*/,
            int price,
            /*uint startedAt*/,
            /*uint timeStamp*/,
            /*uint80 answeredInRound*/
        ) = priceFeed.latestRoundData();
        
        uint256 currentPrice = uint256(price) / (10 ** priceFeed.decimals());
        
        if (currentPrice >= thresholdPrice && !thresholdReached) {
            thresholdReached = true;
            emit ThresholdReached(currentPrice);
            return true;
        }
        return false;
    }
    
    function executeAction() external {
        require(checkPriceThreshold(), "Price threshold not reached");
        // Custom logic to execute when threshold is reached
        performCustomAction();
    }
    
    function performCustomAction() internal {
        // Implement your custom smart contract logic here
        // Example: liquidate positions, trigger trades, etc.
    }
    
    function updateThreshold(uint256 _newThreshold) external onlyOwner {
        thresholdPrice = _newThreshold;
        thresholdReached = false;
    }
    
    function transferOwnership(address newOwner) external onlyOwner {
        require(newOwner != address(0), "Invalid address");
        owner = newOwner;
    }
    
    event ThresholdReached(uint256 currentPrice);
}
```
