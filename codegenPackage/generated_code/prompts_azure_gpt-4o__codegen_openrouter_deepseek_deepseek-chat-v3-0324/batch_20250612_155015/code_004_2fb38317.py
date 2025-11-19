"""
Generated Code Metadata:
========================
Original URL: https://pythop.com
Prompt: Provide an example of a smart contract that integrates Pythop's market data API to trigger specific actions based on price thresholds.
Generated: DETERMINISTIC_2fb38317e674c838
Batch ID: 20250612_155015
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

// Import Pyth Oracle interface
interface IPyth {
    struct Price {
        int64 price;
        uint64 conf;
        int32 expo;
        uint publishTime;
    }

    function getPriceUnsafe(bytes32 id) external view returns (Price memory price);
    function getPrice(bytes32 id) external view returns (Price memory price);
    function getPriceNoOlderThan(bytes32 id, uint age) external view returns (Price memory price);
    function updatePriceFeeds(bytes[] calldata updateData) external payable;
}

contract PriceThresholdTrigger {
    IPyth public pyth;
    bytes32 public priceFeedId;
    address public owner;
    
    // Price threshold in USD scaled to 8 decimals (e.g., 100000000 = $1.00)
    int64 public upperThreshold;
    int64 public lowerThreshold;
    
    // Events
    event ThresholdReached(bytes32 indexed priceFeedId, int64 price, string direction);
    event ThresholdsUpdated(int64 newUpperThreshold, int64 newLowerThreshold);
    event OwnershipTransferred(address indexed previousOwner, address indexed newOwner);

    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can call this function");
        _;
    }

    constructor(
        address _pythAddress,
        bytes32 _priceFeedId,
        int64 _upperThreshold,
        int64 _lowerThreshold
    ) {
        require(_pythAddress != address(0), "Invalid Pyth address");
        require(_upperThreshold > _lowerThreshold, "Upper threshold must be greater than lower");
        
        pyth = IPyth(_pythAddress);
        priceFeedId = _priceFeedId;
        upperThreshold = _upperThreshold;
        lowerThreshold = _lowerThreshold;
        owner = msg.sender;
    }

    function checkPrice() public returns (int64) {
        IPyth.Price memory priceData = pyth.getPrice(priceFeedId);
        int64 currentPrice = priceData.price;
        
        if (currentPrice >= upperThreshold) {
            emit ThresholdReached(priceFeedId, currentPrice, "above");
        } else if (currentPrice <= lowerThreshold) {
            emit ThresholdReached(priceFeedId, currentPrice, "below");
        }
        
        return currentPrice;
    }

    function updateThresholds(int64 _newUpperThreshold, int64 _newLowerThreshold) external onlyOwner {
        require(_newUpperThreshold > _newLowerThreshold, "Upper threshold must be greater than lower");
        
        upperThreshold = _newUpperThreshold;
        lowerThreshold = _newLowerThreshold;
        
        emit ThresholdsUpdated(_newUpperThreshold, _newLowerThreshold);
    }

    function transferOwnership(address newOwner) external onlyOwner {
        require(newOwner != address(0), "New owner cannot be zero address");
        emit OwnershipTransferred(owner, newOwner);
        owner = newOwner;
    }

    // Helper function to convert price to human-readable format
    function getNormalizedPrice() external view returns (int256) {
        IPyth.Price memory priceData = pyth.getPrice(priceFeedId);
        return int256(priceData.price) * (10 ** (18 + priceData.expo));
    }

    // Allow contract to receive ETH for Pyth update fees
    receive() external payable {}
}
```
