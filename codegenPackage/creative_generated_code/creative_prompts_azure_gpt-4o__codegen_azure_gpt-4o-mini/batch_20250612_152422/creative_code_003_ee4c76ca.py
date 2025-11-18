"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://funkybunnies.pages.dev
Prompt: Write a smart contract in Solidity for a token called "Funky Bunnies" that supports minting and burning functionalities.
Generated: DETERMINISTIC_ee4c76caa175a5a1
Batch ID: 20250612_152422
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

// Import the ERC20 interface from OpenZeppelin
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title FunkyBunniesToken
 * @dev This contract implements an ERC20 token called "Funky Bunnies" 
 * with minting and burning functionalities.
 */
contract FunkyBunniesToken is ERC20, Ownable {
    
    // Mapping to track whether an address is allowed to mint/burn
    mapping(address => bool) private _minters;

    /**
     * @dev Constructor to set the token name and symbol.
     */
    constructor() ERC20("Funky Bunnies", "FBUNNY") {
        // Grant the deployer the ability to mint
        _minters[msg.sender] = true;
    }

    /**
     * @dev Modifier to check if the caller is a minter.
     */
    modifier onlyMinter() {
        require(_minters[msg.sender], "Caller is not a minter");
        _;
    }

    /**
     * @dev Function to mint new tokens.
     * @param to The address to receive the minted tokens.
     * @param amount The amount of tokens to mint.
     */
    function mint(address to, uint256 amount) external onlyMinter {
        require(to != address(0), "Cannot mint to the zero address");
        require(amount > 0, "Mint amount must be greater than zero");
        
        _mint(to, amount);
    }

    /**
     * @dev Function to burn a specific amount of tokens
     * from the caller's account.
     * @param amount The amount of tokens to burn.
     */
    function burn(uint256 amount) external {
        require(amount > 0, "Burn amount must be greater than zero");
        
        _burn(msg.sender, amount);
    }

    /**
     * @dev Function to add a new minter.
     * @param account The address to add as a minter.
     */
    function addMinter(address account) external onlyOwner {
        require(account != address(0), "Cannot add the zero address as a minter");
        _minters[account] = true;
    }

    /**
     * @dev Function to remove an existing minter.
     * @param account The address to remove from minters.
     */
    function removeMinter(address account) external onlyOwner {
        require(account != address(0), "Cannot remove the zero address from minters");
        _minters[account] = false;
    }

    /**
     * @dev Function to check if an address is a minter.
     * @param account The address to check.
     * @return bool True if the account is a minter, otherwise false.
     */
    function isMinter(address account) external view returns (bool) {
        return _minters[account];
    }
}
```
