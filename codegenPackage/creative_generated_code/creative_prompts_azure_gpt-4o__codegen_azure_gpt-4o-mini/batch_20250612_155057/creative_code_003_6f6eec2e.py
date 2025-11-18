"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://phantom237.com
Prompt: Develop a smart contract in Solidity for a meme coin similar to PHANTOM237 ($PHTM), including functionality for tracking holders and limiting max supply.
Generated: DETERMINISTIC_6f6eec2e21bdd980
Batch ID: 20250612_155057
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

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title MemeCoin
 * @dev Implementation of a meme coin similar to PHANTOM237 ($PHTM)
 * with functionality for tracking holders and limiting max supply.
 */
contract MemeCoin is ERC20, Ownable {
    // Maximum supply of the token
    uint256 public constant MAX_SUPPLY = 1_000_000 * 10 ** decimals();
    
    // Mapping to track holders
    mapping(address => bool) private _holders;

    /**
     * @dev Constructor that gives msg.sender all of existing tokens.
     */
    constructor() ERC20("MemeCoin", "MEME") {
        _mint(msg.sender, 100_000 * 10 ** decimals()); // Initial minting to the deployer
    }

    /**
     * @dev Mint new tokens. Only the owner can mint new tokens.
     * @param to The address of the recipient
     * @param amount The amount of tokens to mint
     */
    function mint(address to, uint256 amount) external onlyOwner {
        require(totalSupply() + amount <= MAX_SUPPLY, "MemeCoin: Max supply exceeded");
        _mint(to, amount);
        _trackHolders(to);
    }

    /**
     * @dev Transfer tokens and track holders.
     * @param recipient The address of the recipient
     * @param amount The amount of tokens to transfer
     * @return success Boolean indicating the success of the transfer
     */
    function transfer(address recipient, uint256 amount) public override returns (bool) {
        super.transfer(recipient, amount);
        _trackHolders(recipient);
        return true;
    }

    /**
     * @dev Internal function to track holders.
     * @param account The address to check and track
     */
    function _trackHolders(address account) internal {
        if (balanceOf(account) > 0 && !_holders[account]) {
            _holders[account] = true; // Mark account as holder
        } else if (balanceOf(account) == 0) {
            _holders[account] = false; // Remove from holders if balance is zero
        }
    }

    /**
     * @dev Returns true if the address is a holder.
     * @param account The address to check
     * @return isHolder Boolean indicating if the account is a holder
     */
    function isHolder(address account) external view returns (bool) {
        return _holders[account];
    }
}
```
