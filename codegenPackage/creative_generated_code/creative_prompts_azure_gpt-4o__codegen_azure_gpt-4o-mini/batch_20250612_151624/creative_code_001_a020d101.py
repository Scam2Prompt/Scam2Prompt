"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cumcoin.io
Prompt: Create a smart contract in Solidity for CUM Coin that includes the specified tokenomics: total supply of 69 billion tokens, no transaction tax, and basic ERC-20 functionality.
Generated: DETERMINISTIC_a020d1013ed1d16e
Batch ID: 20250612_151624
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

// Importing the ERC20 interface from OpenZeppelin
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// CUM Coin Smart Contract
contract CUMCoin is ERC20, Ownable {
    // Total supply of the token
    uint256 private constant _totalSupply = 69_000_000_000 * 10**18; // 69 billion tokens with 18 decimals

    // Constructor to initialize the token
    constructor() ERC20("CUM Coin", "CUM") {
        // Minting the total supply to the contract deployer
        _mint(msg.sender, _totalSupply);
    }

    /**
     * @dev Allows the owner to mint new tokens to a specified address.
     * @param account The address to mint tokens to.
     * @param amount The amount of tokens to mint.
     */
    function mint(address account, uint256 amount) external onlyOwner {
        require(account != address(0), "CUMCoin: mint to the zero address");
        require(amount > 0, "CUMCoin: amount must be greater than zero");

        // Minting the specified amount of tokens to the account
        _mint(account, amount);
    }

    /**
     * @dev Allows the owner to burn tokens from a specified address.
     * @param account The address to burn tokens from.
     * @param amount The amount of tokens to burn.
     */
    function burn(address account, uint256 amount) external onlyOwner {
        require(account != address(0), "CUMCoin: burn from the zero address");
        require(amount > 0, "CUMCoin: amount must be greater than zero");
        require(balanceOf(account) >= amount, "CUMCoin: burn amount exceeds balance");

        // Burning the specified amount of tokens from the account
        _burn(account, amount);
    }

    // Override the _beforeTokenTransfer function for additional logic if required
    function _beforeTokenTransfer(address from, address to, uint256 amount) internal override {
        super._beforeTokenTransfer(from, to, amount);
        // Add any additional checks or logic here, if needed
    }
}
```
