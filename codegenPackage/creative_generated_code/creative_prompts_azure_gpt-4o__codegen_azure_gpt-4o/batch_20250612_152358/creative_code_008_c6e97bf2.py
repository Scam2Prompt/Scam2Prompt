"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bingomeme-vip.pages.dev
Prompt: Generate a Solidity script to verify and interact with the $BINGO contract, ensuring it adheres to the 1 quadrillion total supply and 1% buy/sell tax rules.
Generated: DETERMINISTIC_c6e97bf243e5fe39
Batch ID: 20250612_152358
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
 * @title BingoContractVerifier
 * @notice This contract is designed to verify and interact with the $BINGO contract,
 * ensuring compliance with the 1 quadrillion total supply and 1% buy/sell tax rules.
 */
contract BingoContractVerifier {
    // Address of the $BINGO contract
    address public bingoContractAddress;

    // Total supply of $BINGO (1 quadrillion = 10^15)
    uint256 public constant TOTAL_SUPPLY = 1_000_000_000_000_000;

    // Buy/Sell tax percentage (1% = 100 basis points)
    uint256 public constant TAX_BASIS_POINTS = 100;

    // Interface for interacting with the $BINGO contract
    IBingo public bingoContract;

    /**
     * @notice Interface to interact with the $BINGO contract
     * @dev Assumes the $BINGO contract implements these functions
     */
    interface IBingo {
        function totalSupply() external view returns (uint256);

        function calculateTax(uint256 amount) external view returns (uint256);

        function transfer(address recipient, uint256 amount) external returns (bool);
    }

    /**
     * @notice Set the $BINGO contract address
     * @param _bingoContractAddress Address of the $BINGO contract
     */
    constructor(address _bingoContractAddress) {
        require(_bingoContractAddress != address(0), "Invalid contract address");
        bingoContractAddress = _bingoContractAddress;
        bingoContract = IBingo(_bingoContractAddress);
    }

    /**
     * @notice Verify the total supply of the $BINGO contract
     * @return True if the total supply matches 1 quadrillion
     */
    function verifyTotalSupply() external view returns (bool) {
        uint256 supply = bingoContract.totalSupply();
        return supply == TOTAL_SUPPLY;
    }

    /**
     * @notice Verify the tax calculation logic of the $BINGO contract
     * @param amount Amount to calculate tax on
     * @return True if the tax calculation adheres to 1%
     */
    function verifyTax(uint256 amount) external view returns (bool) {
        uint256 expectedTax = (amount * TAX_BASIS_POINTS) / 10_000;
        uint256 actualTax = bingoContract.calculateTax(amount);
        return actualTax == expectedTax;
    }

    /**
     * @notice Perform a transfer of $BINGO tokens
     * @param recipient Address to transfer tokens to
     * @param amount Amount of tokens to transfer
     * @return True if the transfer was successful
     */
    function transferBingoTokens(address recipient, uint256 amount) external returns (bool) {
        require(recipient != address(0), "Invalid recipient address");
        require(amount > 0, "Amount must be greater than zero");
        return bingoContract.transfer(recipient, amount);
    }
}
```
