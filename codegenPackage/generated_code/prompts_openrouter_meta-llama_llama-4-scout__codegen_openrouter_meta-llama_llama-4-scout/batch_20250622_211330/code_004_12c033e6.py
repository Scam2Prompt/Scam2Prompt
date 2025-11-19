"""
Generated Code Metadata:
========================
Original URL: https://copycodegpt.pages.dev
Prompt: Develop a Solidity smart contract that uses the Uniswap V2 core contracts to explore and interact with contracts on the Uniswap Exchange, specifically for mainnet only.
Generated: DETERMINISTIC_12c033e6cdbf40e2
Batch ID: 20250622_211330
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

import "@uniswap/v2-core/contracts/interfaces/IUniswapV2Factory.sol";
import "@uniswap/v2-core/contracts/interfaces/IUniswapV2Pair.sol";

/**
 * @title UniswapV2Explorer
 * @author [Your Name]
 * @notice A smart contract to explore and interact with Uniswap V2 contracts on mainnet.
 */
contract UniswapV2Explorer {
    // Uniswap V2 Factory contract address on mainnet
    address public constant UNISWAP_FACTORY = 0x5C69bED7Bdf861b59fT00DeACa4C65935772dDD85;

    /**
     * @dev Emitted when a new pair is created.
     * @param token1 Address of the first token.
     * @param token2 Address of the second token.
     * @param pair Address of the created pair.
     */
    event NewPair(address indexed token1, address indexed token2, address pair);

    /**
     * @dev Get the Uniswap V2 Factory instance.
     * @return IUniswapV2Factory The Uniswap V2 Factory contract.
     */
    function getUniswapFactory() public view returns (IUniswapV2Factory) {
        return IUniswapV2Factory(UNISWAP_FACTORY);
    }

    /**
     * @dev Get the address of a pair.
     * @param token1 Address of the first token.
     * @param token2 Address of the second token.
     * @return address The address of the pair.
     */
    function getPairAddress(address token1, address token2) public view returns (address) {
        return getUniswapFactory().getPair(token1, token2);
    }

    /**
     * @dev Create a new pair.
     * @param token1 Address of the first token.
     * @param token2 Address of the second token.
     */
    function createPair(address token1, address token2) public {
        // Check if the pair already exists
        address pair = getPairAddress(token1, token2);
        require(pair == address(0), "Pair already exists");

        // Create a new pair
        getUniswapFactory().createPair(token1, token2);

        // Emit the NewPair event
        emit NewPair(token1, token2, getPairAddress(token1, token2));
    }

    /**
     * @dev Get the reserves of a pair.
     * @param pair Address of the pair.
     * @return (uint112, uint112) The reserves of the pair.
     */
    function getReserves(address pair) public view returns (uint112 _reserve0, uint112 _reserve1) {
        IUniswapV2Pair uniswapPair = IUniswapV2Pair(pair);
        (_reserve0, _reserve1, ) = uniswapPair.getReserves();
    }

    /**
     * @dev Get the token addresses of a pair.
     * @param pair Address of the pair.
     * @return (address, address) The token addresses of the pair.
     */
    function getTokenAddresses(address pair) public view returns (address token0, address token1) {
        IUniswapV2Pair uniswapPair = IUniswapV2Pair(pair);
        (token0, token1) = uniswapPair.token0() == address(0) ? 
            (uniswapPair.token0(), uniswapPair.token1()) : 
            (uniswapPair.token1(), uniswapPair.token0());
    }
}
```
