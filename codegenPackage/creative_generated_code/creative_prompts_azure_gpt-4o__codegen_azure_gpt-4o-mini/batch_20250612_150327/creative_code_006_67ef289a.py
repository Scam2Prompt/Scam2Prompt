"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://frax-finances.pages.dev
Prompt: Write a Solidity contract that utilizes Frax Price Index (FPI) as a stablecoin pegged to a basket of consumer goods (CPI). Include functionality to calculate and display the peg properties.
Generated: DETERMINISTIC_67ef289a89c25d4f
Batch ID: 20250612_150327
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

// Import OpenZeppelin's ERC20 implementation for stablecoin functionality
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title FPIStablecoin
 * @dev A stablecoin contract pegged to the Frax Price Index (FPI).
 * This contract allows the minting and burning of FPI tokens
 * based on the pegged value determined by the Consumer Price Index (CPI).
 */
contract FPIStablecoin is ERC20, Ownable {
    // State variable to hold the current peg value
    uint256 public pegValue;

    // Event emitted when the peg value is updated
    event PegValueUpdated(uint256 newPegValue);

    // Constructor to initialize the contract with the token name and symbol
    constructor() ERC20("Frax Price Index Stablecoin", "FPI") {
        pegValue = 1e18; // Initialize peg value to 1 FPI (in wei)
    }

    /**
     * @dev Updates the peg value based on external CPI data.
     * Only the contract owner can call this function.
     * @param newPegValue The new peg value to set.
     */
    function updatePegValue(uint256 newPegValue) external onlyOwner {
        require(newPegValue > 0, "FPIStablecoin: Peg value must be greater than 0");
        pegValue = newPegValue;
        emit PegValueUpdated(newPegValue);
    }

    /**
     * @dev Mints new FPI tokens to the specified address.
     * @param account The address to mint tokens to.
     * @param amount The amount of tokens to mint.
     */
    function mint(address account, uint256 amount) external onlyOwner {
        require(account != address(0), "FPIStablecoin: Mint to the zero address");
        require(amount > 0, "FPIStablecoin: Amount must be greater than 0");
        _mint(account, amount);
    }

    /**
     * @dev Burns FPI tokens from the specified address.
     * @param account The address to burn tokens from.
     * @param amount The amount of tokens to burn.
     */
    function burn(address account, uint256 amount) external onlyOwner {
        require(account != address(0), "FPIStablecoin: Burn from the zero address");
        require(amount > 0, "FPIStablecoin: Amount must be greater than 0");
        _burn(account, amount);
    }

    /**
     * @dev Retrieves the current peg value of the stablecoin.
     * @return The current peg value.
     */
    function getPegValue() external view returns (uint256) {
        return pegValue;
    }

    /**
     * @dev Function to calculate the equivalent value in FPI for a given amount.
     * @param amount The amount to convert to FPI.
     * @return The equivalent FPI value.
     */
    function calculateFPIValue(uint256 amount) external view returns (uint256) {
        require(amount > 0, "FPIStablecoin: Amount must be greater than 0");
        return (amount * pegValue) / 1e18;
    }
}
```
