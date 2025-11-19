"""
Generated Code Metadata:
========================
Original URL: https://pythbtc.com
Prompt: Demonstrate how to configure a smart contract to use Pyth price feed oracles for decentralized finance (DeFi) applications.
Generated: DETERMINISTIC_1fc6c012431fa2a4
Batch ID: 20250612_155015
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@pythnetwork/pyth-contracts/src/Pyth.sol";
import "@pythnetwork/pyth-contracts/src/interfaces/IPyth.sol";

/**
 * @title PythOracleExample
 * @author [Your Name]
 * @notice Example contract demonstrating how to use Pyth price feed oracles for DeFi applications.
 */
contract PythOracleExample {
    // Pyth oracle instance
    IPyth public pyth;

    // Mapping of asset feeds to their corresponding prices
    mapping(bytes32 => Pyth.Price) public prices;

    /**
     * @param _pyth Pyth oracle address
     */
    constructor(address _pyth) {
        pyth = IPyth(_pyth);
    }

    /**
     * @dev Updates the price of an asset feed
     * @param _feedId Asset feed ID (e.g., 0x... for ETH/USD)
     */
    function updatePrice(bytes32 _feedId) public {
        // Get the latest price update
        Pyth.Price memory price = pyth.getPrice(_feedId);

        // Validate the price update
        require(price.price > 0, "Invalid price");

        // Store the updated price
        prices[_feedId] = price;
    }

    /**
     * @dev Gets the current price of an asset feed
     * @param _feedId Asset feed ID (e.g., 0x... for ETH/USD)
     * @return Current price of the asset feed
     */
    function getPrice(bytes32 _feedId) public view returns (int64) {
        // Retrieve the stored price
        Pyth.Price memory price = prices[_feedId];

        // Return the current price
        return price.price;
    }

    /**
     * @dev Example usage: Swap tokens using Pyth oracle prices
     * @param _tokenIn Token to swap from (e.g., ERC20)
     * @param _tokenOut Token to swap to (e.g., ERC20)
     * @param _amountIn Amount of tokens to swap
     * @param _feedIdIn Asset feed ID for tokenIn (e.g., 0x... for ETH/USD)
     * @param _feedIdOut Asset feed ID for tokenOut (e.g., 0x... for ETH/USD)
     */
    function swapTokens(
        IERC20 _tokenIn,
        IERC20 _tokenOut,
        uint256 _amountIn,
        bytes32 _feedIdIn,
        bytes32 _feedIdOut
    ) public {
        // Get the current prices
        int64 priceIn = getPrice(_feedIdIn);
        int64 priceOut = getPrice(_feedIdOut);

        // Calculate the swap amount
        uint256 amountOut = (_amountIn * uint256(priceOut)) / uint256(priceIn);

        // Perform the token swap
        _tokenIn.transferFrom(msg.sender, address(this), _amountIn);
        _tokenOut.transfer(msg.sender, amountOut);
    }
}
```

```python
# Example usage with Brownie
from brownie import accounts, network, PythOracleExample, Contract

def deploy_pyth_oracle():
    # Set up Pyth oracle address (testnet/mainnet)
    pyth_address = "0x..."

    # Deploy the contract
    accounts.add("0x...")
    contract = PythOracleExample.deploy(pyth_address, {"from": accounts[0]})

    return contract

def main():
    network.connect("mainnet")
    contract = deploy_pyth_oracle()

    # Update and get prices
    feed_id = "0x..."
    contract.updatePrice(feed_id)
    price = contract.getPrice(feed_id)

    print(f"Current price: {price}")

if __name__ == "__main__":
    main()
```
