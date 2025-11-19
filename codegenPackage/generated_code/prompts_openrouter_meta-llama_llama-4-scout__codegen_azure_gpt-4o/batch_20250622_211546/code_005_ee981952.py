"""
Generated Code Metadata:
========================
Original URL: https://dancingtriangle.website
Prompt: Write a Solidity smart contract code to burn a specific percentage of $triangle cryptocurrency supply, similar to the 6.9% market-bought and burned tokens mentioned on the webpage.
Generated: DETERMINISTIC_ee981952d0fc22f3
Batch ID: 20250622_211546
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

/**
 * @title TriangleTokenBurner
 * @dev A smart contract to burn a specific percentage of $triangle cryptocurrency supply.
 */
contract TriangleTokenBurner {
    // Address of the $triangle token contract
    address public triangleTokenAddress;

    // Percentage to burn (e.g., 6.9%)
    uint256 public burnPercentage;

    // Event emitted when tokens are burned
    event TokensBurned(uint256 amountBurned);

    /**
     * @dev Constructor to initialize the contract with the token address and burn percentage.
     * @param _triangleTokenAddress Address of the $triangle token contract.
     * @param _burnPercentage Percentage of tokens to burn (e.g., 6.9 for 6.9%).
     */
    constructor(address _triangleTokenAddress, uint256 _burnPercentage) {
        require(_triangleTokenAddress != address(0), "Invalid token address");
        require(_burnPercentage > 0 && _burnPercentage <= 100, "Burn percentage must be between 0 and 100");

        triangleTokenAddress = _triangleTokenAddress;
        burnPercentage = _burnPercentage;
    }

    /**
     * @dev Function to burn a specific percentage of the token supply.
     * Requires the contract to hold the tokens to be burned.
     */
    function burnTokens() external {
        // Interface for the ERC20 token
        IERC20 triangleToken = IERC20(triangleTokenAddress);

        // Get the balance of tokens held by this contract
        uint256 contractBalance = triangleToken.balanceOf(address(this));
        require(contractBalance > 0, "No tokens to burn");

        // Calculate the amount to burn based on the burn percentage
        uint256 amountToBurn = (contractBalance * burnPercentage) / 100;

        // Burn the tokens
        require(triangleToken.transfer(address(0), amountToBurn), "Token burn failed");

        // Emit the burn event
        emit TokensBurned(amountToBurn);
    }
}

/**
 * @dev Interface for ERC20 token standard.
 */
interface IERC20 {
    function balanceOf(address account) external view returns (uint256);
    function transfer(address recipient, uint256 amount) external returns (bool);
}
```
