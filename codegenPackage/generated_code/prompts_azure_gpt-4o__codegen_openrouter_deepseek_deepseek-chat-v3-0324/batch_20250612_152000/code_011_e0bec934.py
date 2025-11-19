"""
Generated Code Metadata:
========================
Original URL: https://y45y45y54.pages.dev
Prompt: Write a smart contract that uses Pyth price feeds to calculate expiry prices for options contracts in a DeFi application on Ethereum.
Generated: DETERMINISTIC_e0bec934e5846536
Batch ID: 20250612_152000
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

import "@pythnetwork/pyth-sdk-solidity/IPyth.sol";
import "@pythnetwork/pyth-sdk-solidity/PythStructs.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

contract OptionsExpiryPricing is Ownable {
    using SafeMath for uint256;

    IPyth public pyth;
    bytes32 public priceFeedId;
    uint256 public expiryTimestamp;
    uint256 public expiryPrice;
    bool public priceSet;

    event ExpiryPriceSet(uint256 price, uint256 timestamp);

    constructor(
        address _pythContract,
        bytes32 _priceFeedId,
        uint256 _expiryTimestamp
    ) {
        require(_pythContract != address(0), "Invalid Pyth contract address");
        require(_priceFeedId != bytes32(0), "Invalid price feed ID");
        require(
            _expiryTimestamp > block.timestamp,
            "Expiry must be in the future"
        );

        pyth = IPyth(_pythContract);
        priceFeedId = _priceFeedId;
        expiryTimestamp = _expiryTimestamp;
    }

    function setExpiryPrice(bytes[] calldata priceUpdateData)
        external
        payable
        onlyOwner
    {
        require(!priceSet, "Price already set");
        require(
            block.timestamp >= expiryTimestamp,
            "Cannot set price before expiry"
        );

        uint256 fee = pyth.getUpdateFee(priceUpdateData);
        require(msg.value >= fee, "Insufficient fee");

        pyth.updatePriceFeeds{value: fee}(priceUpdateData);

        PythStructs.Price memory price = pyth.getPrice(priceFeedId);
        expiryPrice = convertPriceToUint(price);
        priceSet = true;

        emit ExpiryPriceSet(expiryPrice, block.timestamp);

        // Refund any excess payment
        if (msg.value > fee) {
            payable(msg.sender).transfer(msg.value - fee);
        }
    }

    function getExpiryPrice() external view returns (uint256) {
        require(priceSet, "Price not yet set");
        return expiryPrice;
    }

    function convertPriceToUint(PythStructs.Price memory price)
        internal
        pure
        returns (uint256)
    {
        require(price.expo <= 0, "Negative exponent expected");

        uint256 priceInUint = uint256(uint64(price.price));
        uint256 decimals = uint256(uint32(-price.expo));

        // Scale price to 18 decimals
        if (decimals < 18) {
            priceInUint = priceInUint.mul(10**(18 - decimals));
        } else if (decimals > 18) {
            priceInUint = priceInUint.div(10**(decimals - 18));
        }

        return priceInUint;
    }

    function updateExpiryTimestamp(uint256 newExpiryTimestamp)
        external
        onlyOwner
    {
        require(!priceSet, "Price already set");
        require(
            newExpiryTimestamp > block.timestamp,
            "New expiry must be in the future"
        );
        expiryTimestamp = newExpiryTimestamp;
    }

    function withdraw() external onlyOwner {
        payable(owner()).transfer(address(this).balance);
    }

    receive() external payable {}
}
```
