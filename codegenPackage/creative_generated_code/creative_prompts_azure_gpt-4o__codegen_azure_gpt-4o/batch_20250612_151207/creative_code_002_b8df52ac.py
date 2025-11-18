"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://neiroethe.pages.dev
Prompt: "Using the Ethereum blockchain, write a script in Solidity to verify the circulating supply of $NEIRO tokens and display the token's contract address, symbol, and decimal information."
Generated: DETERMINISTIC_b8df52ac6611cabf
Batch ID: 20250612_151207
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
 * @title TokenInfo
 * @notice This contract retrieves information about a given ERC-20 token.
 * It provides the circulating supply, contract address, symbol, and decimals.
 */
contract TokenInfo {
    // Address of the ERC-20 token contract
    address public tokenAddress;

    // Constructor to initialize the token address
    constructor(address _tokenAddress) {
        require(_tokenAddress != address(0), "Invalid token address");
        tokenAddress = _tokenAddress;
    }

    /**
     * @notice Interface for interacting with ERC-20 contracts
     * @dev This defines the functions we need to interact with the token contract.
     */
    interface IERC20 {
        function totalSupply() external view returns (uint256);
        function symbol() external view returns (string memory);
        function decimals() external view returns (uint8);
    }

    /**
     * @notice Get the circulating supply of the token
     * @return The total supply as defined in the ERC-20 contract
     */
    function getCirculatingSupply() public view returns (uint256) {
        IERC20 token = IERC20(tokenAddress);
        return token.totalSupply();
    }

    /**
     * @notice Get the symbol of the token
     * @return The token's symbol as defined in the ERC-20 contract
     */
    function getTokenSymbol() public view returns (string memory) {
        IERC20 token = IERC20(tokenAddress);
        return token.symbol();
    }

    /**
     * @notice Get the decimals of the token
     * @return The number of decimals used by the token as defined in the ERC-20 contract
     */
    function getTokenDecimals() public view returns (uint8) {
        IERC20 token = IERC20(tokenAddress);
        return token.decimals();
    }

    /**
     * @notice Get the full token information: contract address, symbol, and decimals
     * @return tokenAddress, symbol, and decimals
     */
    function getTokenInfo()
        external
        view
        returns (
            address,
            string memory,
            uint8
        )
    {
        IERC20 token = IERC20(tokenAddress);
        return (tokenAddress, token.symbol(), token.decimals());
    }
}
```
