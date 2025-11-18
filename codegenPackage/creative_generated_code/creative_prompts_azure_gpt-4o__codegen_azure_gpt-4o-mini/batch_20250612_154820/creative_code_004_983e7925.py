"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ondofoundateon.org
Prompt: Provide an example of deploying a governance token smart contract on Ethereum, inspired by the ONDO token used in the Ondo Ecosystem.
Generated: DETERMINISTIC_983e7925d0d600b2
Batch ID: 20250612_154820
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

// Import OpenZeppelin Contracts for secure and well-tested ERC20 implementation
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// GovernanceToken contract inherits from ERC20 and Ownable
contract GovernanceToken is ERC20, Ownable {
    // Define the token's initial supply and decimals
    uint8 private constant _decimals = 18;
    uint256 private constant INITIAL_SUPPLY = 1_000_000 * (10 ** uint256(_decimals));

    // Event to emit when tokens are minted
    event TokensMinted(address indexed to, uint256 amount);

    // Constructor to set the token name and symbol and mint initial supply
    constructor() ERC20("Ondo Governance Token", "ONDO") {
        // Mint initial supply to the contract owner
        _mint(msg.sender, INITIAL_SUPPLY);
    }

    /**
     * @dev Mint new tokens to a specified address.
     * Can only be called by the owner of the contract.
     * @param to The address to mint tokens to.
     * @param amount The amount of tokens to mint.
     */
    function mint(address to, uint256 amount) external onlyOwner {
        require(to != address(0), "Cannot mint to the zero address");
        require(amount > 0, "Amount must be greater than zero");

        // Mint the specified amount of tokens to the specified address
        _mint(to, amount);
        emit TokensMinted(to, amount);
    }

    /**
     * @dev Override the decimals function to return the specified number of decimals.
     * @return The number of decimals for the token.
     */
    function decimals() public view virtual override returns (uint8) {
        return _decimals;
    }

    /**
     * @dev Transfer tokens from one address to another with error handling.
     * @param recipient The address to transfer tokens to.
     * @param amount The amount of tokens to transfer.
     * @return A boolean indicating whether the transfer was successful.
     */
    function transfer(address recipient, uint256 amount) public virtual override returns (bool) {
        require(recipient != address(0), "Transfer to the zero address");
        require(amount <= balanceOf(msg.sender), "Transfer amount exceeds balance");

        // Call the parent transfer function and return the result
        return super.transfer(recipient, amount);
    }

    /**
     * @dev A function to burn tokens from the caller's account.
     * @param amount The amount of tokens to burn.
     */
    function burn(uint256 amount) external {
        require(amount > 0, "Burn amount must be greater than zero");
        require(amount <= balanceOf(msg.sender), "Burn amount exceeds balance");

        // Burn the specified amount of tokens from the caller's account
        _burn(msg.sender, amount);
    }
}
```

Make sure to install the OpenZeppelin contracts library to compile and deploy the smart contract:

```bash
npm install @openzeppelin/contracts
``` 

This code is ready for deployment on Ethereum and includes all necessary functions and error handling as per best practices.
