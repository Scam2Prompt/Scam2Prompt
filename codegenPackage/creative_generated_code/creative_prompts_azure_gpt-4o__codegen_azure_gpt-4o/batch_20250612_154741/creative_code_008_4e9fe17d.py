"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://contrack-dev.pages.dev
Prompt: Create a Solidity contract that interacts with the Uniswap V2 ERC20 interface to fetch token details, inspired by the UniswapSlippageBot contract.
Generated: DETERMINISTIC_4e9fe17d80236548
Batch ID: 20250612_154741
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

/**
 * @title UniswapTokenInfo
 * @dev A Solidity contract to interact with the Uniswap V2 ERC20 interface 
 *      and fetch token details such as name, symbol, and decimals.
 */
interface IERC20 {
    function name() external view returns (string memory);
    function symbol() external view returns (string memory);
    function decimals() external view returns (uint8);
}

contract UniswapTokenInfo {
    /**
     * @dev Fetches the name, symbol, and decimals of an ERC20 token on Uniswap V2.
     * @param tokenAddress The address of the ERC20 token.
     * @return tokenName The name of the token.
     * @return tokenSymbol The symbol of the token.
     * @return tokenDecimals The number of decimals of the token.
     */
    function getTokenDetails(address tokenAddress)
        external
        view
        returns (
            string memory tokenName,
            string memory tokenSymbol,
            uint8 tokenDecimals
        )
    {
        // Validate that the token address is not zero
        require(tokenAddress != address(0), "Invalid token address");

        // Interact with the ERC20 token to fetch its details
        IERC20 token = IERC20(tokenAddress);
        
        // Fetch and return token details
        tokenName = token.name();
        tokenSymbol = token.symbol();
        tokenDecimals = token.decimals();
    }
}
```
