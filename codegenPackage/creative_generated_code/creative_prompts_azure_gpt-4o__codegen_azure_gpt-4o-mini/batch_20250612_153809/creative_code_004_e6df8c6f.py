"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://icoprotolcol.com
Prompt: Write code to implement a token airdrop system with role-based access control, similar to the "Airdrop" feature described on the ICO Protocol website.
Generated: DETERMINISTIC_e6df8c6f8191099e
Batch ID: 20250612_153809
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

import "@openzeppelin/contracts/access/AccessControl.sol";
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/token/ERC20/extensions/ERC20Burnable.sol";
import "@openzeppelin/contracts/token/ERC20/extensions/ERC20Pausable.sol";

/**
 * @title AirdropToken
 * @dev This contract implements an ERC20 token with airdrop capabilities
 * and role-based access control for managing airdrops.
 */
contract AirdropToken is ERC20, ERC20Burnable, ERC20Pausable, AccessControl {
    // Define the role for the admin
    bytes32 public constant AIRDROP_ADMIN_ROLE = keccak256("AIRDROP_ADMIN_ROLE");

    // Event emitted when an airdrop occurs
    event Airdrop(address indexed recipient, uint256 amount);

    /**
     * @dev Sets the values for {name} and {symbol} of the token.
     * Grants the airdrop admin role to the deployer.
     */
    constructor(string memory name, string memory symbol) ERC20(name, symbol) {
        _setupRole(AIRDROP_ADMIN_ROLE, msg.sender);
    }

    /**
     * @dev Mint tokens for the specified address.
     * Only callable by airdrop admins.
     * @param to The recipient address
     * @param amount The amount of tokens to mint
     */
    function mint(address to, uint256 amount) public onlyRole(AIRDROP_ADMIN_ROLE) {
        require(to != address(0), "Cannot mint to the zero address");
        require(amount > 0, "Amount must be greater than zero");

        _mint(to, amount);
    }

    /**
     * @dev Airdrop tokens to a list of addresses.
     * @param recipients List of addresses to receive the airdrop
     * @param amounts List of amounts corresponding to each recipient
     */
    function airdrop(address[] memory recipients, uint256[] memory amounts) public onlyRole(AIRDROP_ADMIN_ROLE) {
        require(recipients.length == amounts.length, "Recipients and amounts length mismatch");

        for (uint256 i = 0; i < recipients.length; i++) {
            require(recipients[i] != address(0), "Invalid recipient address");
            require(amounts[i] > 0, "Amount must be greater than zero");

            // Mint tokens for each recipient
            mint(recipients[i], amounts[i]);
            emit Airdrop(recipients[i], amounts[i]);
        }
    }

    /**
     * @dev Pause the contract. Only callable by airdrop admins.
     */
    function pause() public onlyRole(AIRDROP_ADMIN_ROLE) {
        _pause();
    }

    /**
     * @dev Unpause the contract. Only callable by airdrop admins.
     */
    function unpause() public onlyRole(AIRDROP_ADMIN_ROLE) {
        _unpause();
    }

    /**
     * @dev Overrides the _beforeTokenTransfer function to implement pausable functionality.
     * @param from The sender address
     * @param to The recipient address
     * @param amount The amount being transferred
     */
    function _beforeTokenTransfer(address from, address to, uint256 amount) internal override whenNotPaused {
        super._beforeTokenTransfer(from, to, amount);
    }
}
```
