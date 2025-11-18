"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://1inch-docs.vercel.app
Prompt: Provide an example of using the 1inch Spot Price Aggregator smart contract to extract the current price of USDT from decentralized exchanges (DEXes).
Generated: DETERMINISTIC_2278784aa455945f
Batch ID: 20250612_155028
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title PriceAggregator
 * @dev A contract to interact with the 1inch Spot Price Aggregator to get the price of USDT
 */
contract PriceAggregator is Ownable {
    using SafeMath for uint256;

    // 1inch Spot Price Aggregator contract address (Mainnet)
    address constant ONE_INCH_AGGREGATOR = 0x1111111254fb6c44bac0bed2854e76f906e5b50; // Replace with actual address

    // Event to emit the fetched price
    event PriceFetched(uint256 price);

    /**
     * @dev Fetches the current price of USDT in terms of ETH using the 1inch Spot Price Aggregator.
     * @param usdtAddress The address of the USDT token contract.
     * @return price The current price of USDT in terms of ETH.
     */
    function getUSDTPrice(address usdtAddress) external view returns (uint256 price) {
        require(usdtAddress != address(0), "Invalid USDT address");
        
        // Call the Spot Price Aggregator and get the price
        // The call assumes that the 1inch aggregator has a method to fetch the price
        // Replace the following with the correct method to call the aggregator
        (bool success, bytes memory data) = ONE_INCH_AGGREGATOR.staticcall(
            abi.encodeWithSignature("getRate(address,address)", usdtAddress, address(0))
        );
        
        // Handle potential failure of the call
        require(success, "Failed to fetch price from 1inch aggregator");
        
        // Decode the returned data to get the price
        price = abi.decode(data, (uint256));
        
        // Emit event with the fetched price
        emit PriceFetched(price);
    }
}
```

### Notes:
- Ensure to replace the placeholder address with the actual address of the 1inch Spot Price Aggregator.
- Make sure the method used to fetch the price is correct as per 1inch's latest interface, as the code snippet assumes a specific method signature. Adjust it as necessary based on the actual contract interface on the blockchain.
- Additional safety checks and validations can be added based on the specific requirements of the context in which this contract will be deployed.
