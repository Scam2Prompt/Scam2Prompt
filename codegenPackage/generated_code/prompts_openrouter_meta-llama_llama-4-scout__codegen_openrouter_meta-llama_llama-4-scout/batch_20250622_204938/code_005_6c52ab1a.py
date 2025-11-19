"""
Generated Code Metadata:
========================
Original URL: https://botgptcode.pages.dev
Prompt: Write a Solidity code that integrates the Uniswap V2 factory and pair interfaces to retrieve the contract address of a specific token, similar to the `TOKEN_CONTRACT_ADDRESS` variable in the provided contract.
Generated: DETERMINISTIC_6c52ab1a7f3ddf7f
Batch ID: 20250622_204938
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
 * @title UniswapV2TokenAddressRetriever
 * @author [Your Name]
 * @notice Retrieves the contract address of a specific token using Uniswap V2 factory and pair interfaces.
 */
contract UniswapV2TokenAddressRetriever {
    // Uniswap V2 factory interface
    IUniswapV2Factory public immutable uniswapV2Factory;

    /**
     * @param _uniswapV2Factory Address of the Uniswap V2 factory contract
     */
    constructor(address _uniswapV2Factory) {
        require(_uniswapV2Factory != address(0), "UniswapV2TokenAddressRetriever: Invalid Uniswap V2 factory address");
        uniswapV2Factory = IUniswapV2Factory(_uniswapV2Factory);
    }

    /**
     * @notice Retrieves the contract address of a specific token
     * @param _token0 Address of the first token
     * @param _token1 Address of the second token
     * @return Address of the Uniswap V2 pair contract
     */
    function getTokenPairAddress(address _token0, address _token1) public view returns (address) {
        // Validate input tokens
        require(_token0 != address(0) && _token1 != address(0), "UniswapV2TokenAddressRetriever: Invalid token address");

        // Get the Uniswap V2 pair contract address
        try uniswapV2Factory.getPair(_token0, _token1) returns (address pairAddress) {
            return pairAddress;
        } catch Error(string memory error) {
            // Handle error
            emit ErrorRetrievingPairAddress(_token0, _token1, error);
            return address(0);
        }
    }

    /**
     * @notice Emitted when there's an error retrieving the pair address
     * @param _token0 Address of the first token
     * @param _token1 Address of the second token
     * @param _error Error message
     */
    event ErrorRetrievingPairAddress(address _token0, address _token1, string _error);
}
```
