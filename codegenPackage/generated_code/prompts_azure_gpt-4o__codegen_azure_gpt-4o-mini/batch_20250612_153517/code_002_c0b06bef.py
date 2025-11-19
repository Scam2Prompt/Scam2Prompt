"""
Generated Code Metadata:
========================
Original URL: https://oldioen.pages.dev
Prompt: Generate Solidity code for an Ethereum smart contract that supports IOEN token transactions and includes auditing features similar to those mentioned in the DeusSec certification.
Generated: DETERMINISTIC_c0b06bef578668e2
Batch ID: 20250612_153517
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
import "@openzeppelin/contracts/utils/Context.sol";

/**
 * @title IOEN Token Contract
 * @dev This contract implements an ERC20 token with auditing features.
 */
contract IOENToken is Context, ERC20, Ownable {
    // Mapping to track the audit status of addresses
    mapping(address => bool) private _auditedAddresses;

    // Event emitted when an address is audited
    event AddressAudited(address indexed account, bool status);

    /**
     * @dev Constructor that gives msg.sender all of existing tokens.
     */
    constructor(uint256 initialSupply) ERC20("IOEN Token", "IOEN") {
        require(initialSupply > 0, "Initial supply must be greater than zero");
        _mint(msg.sender, initialSupply);
    }

    /**
     * @dev Function to audit an address.
     * @param account The address to be audited.
     * @param status The audit status to set.
     */
    function auditAddress(address account, bool status) external onlyOwner {
        require(account != address(0), "Cannot audit the zero address");
        _auditedAddresses[account] = status;
        emit AddressAudited(account, status);
    }

    /**
     * @dev Function to check if an address is audited.
     * @param account The address to check.
     * @return bool indicating if the address is audited.
     */
    function isAudited(address account) external view returns (bool) {
        return _auditedAddresses[account];
    }

    /**
     * @dev Override the transfer function to include auditing checks.
     * @param recipient The address to transfer tokens to.
     * @param amount The amount of tokens to transfer.
     * @return bool indicating success of the transfer.
     */
    function transfer(address recipient, uint256 amount) public override returns (bool) {
        require(_auditedAddresses[_msgSender()] || _auditedAddresses[recipient], "Transfer not allowed: both addresses are not audited");
        return super.transfer(recipient, amount);
    }

    /**
     * @dev Override the transferFrom function to include auditing checks.
     * @param sender The address to transfer tokens from.
     * @param recipient The address to transfer tokens to.
     * @param amount The amount of tokens to transfer.
     * @return bool indicating success of the transfer.
     */
    function transferFrom(address sender, address recipient, uint256 amount) public override returns (bool) {
        require(_auditedAddresses[sender] || _auditedAddresses[recipient], "Transfer not allowed: both addresses are not audited");
        return super.transferFrom(sender, recipient, amount);
    }

    /**
     * @dev Function to mint new tokens.
     * @param account The address to mint tokens to.
     * @param amount The amount of tokens to mint.
     */
    function mint(address account, uint256 amount) external onlyOwner {
        require(account != address(0), "Cannot mint to the zero address");
        _mint(account, amount);
    }

    /**
     * @dev Function to burn tokens from an account.
     * @param amount The amount of tokens to burn.
     */
    function burn(uint256 amount) external {
        _burn(_msgSender(), amount);
    }
}
```
