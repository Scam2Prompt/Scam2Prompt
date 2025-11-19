"""
Generated Code Metadata:
========================
Original URL: https://kama-exx.pages.dev
Prompt: Generate a smart contract code in Solidity for a token similar to $KAMA, including functions for minting, freezing, and burning tokens.
Generated: DETERMINISTIC_7fdfb32265c8c8af
Batch ID: 20250622_204615
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

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/Pausable.sol";

/**
 * @title KAMAToken
 * @dev ERC20 Token with minting, freezing, and burning capabilities
 */
contract KAMAToken is ERC20, Ownable, Pausable {
    // Mapping to track frozen accounts
    mapping(address => bool) private _frozenAccounts;

    // Event emitted when tokens are minted
    event Mint(address indexed to, uint256 amount);
    
    // Event emitted when an account is frozen
    event Frozen(address indexed account);
    
    // Event emitted when an account is unfrozen
    event Unfrozen(address indexed account);
    
    // Event emitted when tokens are burned
    event Burn(address indexed from, uint256 amount);

    /**
     * @dev Constructor that gives msg.sender all of existing tokens.
     */
    constructor(uint256 initialSupply) ERC20("KAMAToken", "KAMA") {
        _mint(msg.sender, initialSupply);
    }

    /**
     * @dev Mint new tokens to a specified address.
     * @param to The address to mint tokens to.
     * @param amount The amount of tokens to mint.
     */
    function mint(address to, uint256 amount) external onlyOwner whenNotPaused {
        require(to != address(0), "Cannot mint to the zero address");
        _mint(to, amount);
        emit Mint(to, amount);
    }

    /**
     * @dev Freeze an account, preventing it from transferring tokens.
     * @param account The address to freeze.
     */
    function freezeAccount(address account) external onlyOwner {
        require(account != address(0), "Cannot freeze the zero address");
        require(!_frozenAccounts[account], "Account is already frozen");
        
        _frozenAccounts[account] = true;
        emit Frozen(account);
    }

    /**
     * @dev Unfreeze a previously frozen account.
     * @param account The address to unfreeze.
     */
    function unfreezeAccount(address account) external onlyOwner {
        require(account != address(0), "Cannot unfreeze the zero address");
        require(_frozenAccounts[account], "Account is not frozen");
        
        _frozenAccounts[account] = false;
        emit Unfrozen(account);
    }

    /**
     * @dev Override the transfer function to prevent transfers from frozen accounts.
     */
    function _beforeTokenTransfer(address from, address to, uint256 amount) internal override {
        super._beforeTokenTransfer(from, to, amount);
        require(!_frozenAccounts[from], "Transfer from frozen account");
    }

    /**
     * @dev Burn tokens from the caller's account.
     * @param amount The amount of tokens to burn.
     */
    function burn(uint256 amount) external whenNotPaused {
        _burn(msg.sender, amount);
        emit Burn(msg.sender, amount);
    }

    /**
     * @dev Pause all token transfers.
     */
    function pause() external onlyOwner {
        _pause();
    }

    /**
     * @dev Unpause all token transfers.
     */
    function unpause() external onlyOwner {
        _unpause();
    }
}
```
