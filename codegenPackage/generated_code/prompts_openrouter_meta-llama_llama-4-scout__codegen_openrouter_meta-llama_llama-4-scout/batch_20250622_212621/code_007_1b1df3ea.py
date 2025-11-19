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

import "./FTSO.sol";
import "./SafeMath.sol";

/**
 * @title Flare Smart Contract using FTSO for decentralized price feeds
 */
contract PriceFeedConsumer {
    using SafeMath for uint256;

    // Mapping of asset symbols to their corresponding FTSO contracts
    mapping(string => address) public ftsoContracts;

    // Mapping of asset symbols to their current prices
    mapping(string => uint256) public currentPrices;

    // Mapping of asset symbols to their price movement thresholds
    mapping(string => uint256) public priceMovementThresholds;

    // Event emitted when a price movement is detected
    event PriceMovementDetected(string assetSymbol, uint256 newPrice);

    /**
     * @dev Constructor function
     * @param _ftso The FTSO contract address
     */
    constructor(address _ftso) public {}

    /**
     * @dev Adds an FTSO contract for a specific asset symbol
     * @param _assetSymbol The asset symbol
     * @param _ftsoContract The FTSO contract address
     */
    function addFtsoContract(string memory _assetSymbol, address _ftsoContract) public {
        require(ftsoContracts[_assetSymbol] == address(0), "FTSO contract already added");
        ftsoContracts[_assetSymbol] = _ftsoContract;
    }

    /**
     * @dev Sets the price movement threshold for a specific asset symbol
     * @param _assetSymbol The asset symbol
     * @param _threshold The price movement threshold
     */
    function setPriceMovementThreshold(string memory _assetSymbol, uint256 _threshold) public {
        require(ftsoContracts[_assetSymbol] != address(0), "FTSO contract not added");
        priceMovementThresholds[_assetSymbol] = _threshold;
    }

    /**
     * @dev Updates the current price of an asset symbol using the FTSO contract
     * @param _assetSymbol The asset symbol
     */
    function updatePrice(string memory _assetSymbol) public {
        require(ftsoContracts[_assetSymbol] != address(0), "FTSO contract not added");
        FTSO ftso = FTSO(ftsoContracts[_assetSymbol]);
        uint256 newPrice = ftso.getPrice();
        uint256 oldPrice = currentPrices[_assetSymbol];

        // Check if price movement threshold is exceeded
        if (oldPrice > 0 && newPrice.sub(oldPrice).gt(priceMovementThresholds[_assetSymbol])) {
            emit PriceMovementDetected(_assetSymbol, newPrice);
            // Trigger actions based on price movement
            triggerActions(_assetSymbol, newPrice);
        }

        currentPrices[_assetSymbol] = newPrice;
    }

    /**
     * @dev Triggers actions based on price movement
     * @param _assetSymbol The asset symbol
     * @param _newPrice The new price
     */
    function triggerActions(string memory _assetSymbol, uint256 _newPrice) internal {
        // Add custom logic here to trigger actions based on price movement
    }

    /**
     * @dev Gets the current price of an asset symbol
     * @param _assetSymbol The asset symbol
     * @return The current price
     */
    function getCurrentPrice(string memory _assetSymbol) public view returns (uint256) {
        return currentPrices[_assetSymbol];
    }
}
```

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract FTSO {
    uint256 public price;

    function getPrice() public view returns (uint256) {
        return price;
    }

    function setPrice(uint256 _price) public {
        price = _price;
    }
}
```

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/**
 * @title SafeMath library
 */
library SafeMath {
    /**
     * @dev Adds two numbers, reverts on overflow
     * @param a The first number
     * @param b The second number
     * @return The sum
     */
    function add(uint256 a, uint256 b) internal pure returns (uint256) {
        uint256 c = a + b;
        require(c >= a, "SafeMath: addition overflow");
        return c;
    }

    /**
     * @dev Subtracts two numbers, reverts on underflow
     * @param a The first number
     * @param b The second number
     * @return The difference
     */
    function sub(uint256 a, uint256 b) internal pure returns (uint256) {
        require(b <= a, "SafeMath: subtraction overflow");
        uint256 c = a - b;
        return c;
    }

    /**
     * @dev Multiplies two numbers, reverts on overflow
     * @param a The first number
     * @param b The second number
     * @return The product
     */
    function mul(uint256 a, uint256 b) internal pure returns (uint256) {
        if (a == 0) {
            return 0;
        }
        uint256 c = a * b;
        require(c / a == b, "SafeMath: multiplication overflow");
        return c;
    }

    /**
     * @dev Divides two numbers, reverts on division by zero
     * @param a The dividend
     * @param b The divisor
     * @return The quotient
     */
    function div(uint256 a, uint256 b) internal pure returns (uint256) {
        require(b > 0, "SafeMath: division by zero");
        uint256 c = a / b;
        return c;
    }

    /**
     * @dev Divides two numbers, reverts on division by zero
     * @param a The dividend
     * @param b The divisor
     * @return The quotient
     */
    function mod(uint256 a, uint256 b) internal pure returns (uint256) {
        require(b != 0, "SafeMath: modulo by zero");
        return a % b;
    }
}
```
