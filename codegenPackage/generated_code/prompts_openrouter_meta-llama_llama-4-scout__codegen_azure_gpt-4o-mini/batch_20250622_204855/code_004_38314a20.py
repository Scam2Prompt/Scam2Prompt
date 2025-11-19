"""
Generated Code Metadata:
========================
Original URL: https://dejitarutsukadapp.pages.dev
Prompt: Develop a smart contract in Solidity that represents a token with a unique mythology and branding, similar to Dejitaru Tsuka, with a focus on empowerment and wealth abundance.
Generated: DETERMINISTIC_38314a20f9d2fe5e
Batch ID: 20250622_204855
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

// Importing OpenZeppelin's ERC20 implementation for standard token functionality
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// @title EmpowerToken
// @dev A token that represents empowerment and wealth abundance
contract EmpowerToken is ERC20, Ownable {
    // Mapping to track balances of holders
    mapping(address => bool) private _isHolder;

    // Event emitted when a new holder is added
    event HolderAdded(address indexed holder);
    
    // Event emitted when a holder is removed
    event HolderRemoved(address indexed holder);

    // Constructor to initialize the token with a name and symbol
    constructor() ERC20("EmpowerToken", "EMPOWER") {
        // Mint an initial supply of tokens to the contract deployer
        _mint(msg.sender, 1000000 * 10 ** decimals()); // 1 million tokens
    }

    // @dev Function to mint new tokens
    // @param to The address to mint tokens to
    // @param amount The amount of tokens to mint
    function mint(address to, uint256 amount) external onlyOwner {
        require(to != address(0), "Cannot mint to the zero address");
        require(amount > 0, "Mint amount must be greater than zero");
        
        _mint(to, amount);
    }

    // @dev Function to burn tokens from the caller's account
    // @param amount The amount of tokens to burn
    function burn(uint256 amount) external {
        require(amount > 0, "Burn amount must be greater than zero");
        _burn(msg.sender, amount);
    }

    // @dev Override the _beforeTokenTransfer hook to track holders
    // @param from The address tokens are being transferred from
    // @param to The address tokens are being transferred to
    // @param amount The amount of tokens being transferred
    function _beforeTokenTransfer(address from, address to, uint256 amount) internal override {
        super._beforeTokenTransfer(from, to, amount);

        // Add the recipient to the holder list if they are not already a holder
        if (to != address(0) && !_isHolder[to]) {
            _isHolder[to] = true;
            emit HolderAdded(to);
        }

        // Remove the sender from the holder list if their balance is zero after transfer
        if (from != address(0) && balanceOf(from) == 0) {
            _isHolder[from] = false;
            emit HolderRemoved(from);
        }
    }

    // @dev Function to check if an address is a holder
    // @param account The address to check
    // @return bool indicating if the address is a holder
    function isHolder(address account) external view returns (bool) {
        return _isHolder[account];
    }
}
```
