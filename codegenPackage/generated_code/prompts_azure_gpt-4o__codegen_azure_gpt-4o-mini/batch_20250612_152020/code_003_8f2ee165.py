"""
Generated Code Metadata:
========================
Original URL: https://presale-x.com
Prompt: Create a smart contract in Solidity for managing utility tokens similar to X Token, ensuring compliance with exemptions under the U.S. Securities Act.
Generated: DETERMINISTIC_8f2ee16573cb2e27
Batch ID: 20250612_152020
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
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title UtilityToken
 * @dev A smart contract for managing utility tokens compliant with U.S. Securities Act exemptions.
 */
contract UtilityToken is ERC20, Ownable {
    using SafeMath for uint256;

    // Mapping to track whitelisted addresses
    mapping(address => bool) private _whitelisted;

    // Event emitted when an address is whitelisted
    event AddressWhitelisted(address indexed account);
    
    // Event emitted when an address is removed from the whitelist
    event AddressRemovedFromWhitelist(address indexed account);

    // Modifier to check if the caller is whitelisted
    modifier onlyWhitelisted() {
        require(_whitelisted[msg.sender], "UtilityToken: caller is not whitelisted");
        _;
    }

    /**
     * @dev Constructor that gives the deployer all initial tokens.
     * @param initialSupply The initial supply of tokens.
     */
    constructor(uint256 initialSupply) ERC20("UtilityToken", "UTK") {
        require(initialSupply > 0, "UtilityToken: initial supply must be greater than 0");
        _mint(msg.sender, initialSupply);
    }

    /**
     * @dev Function to whitelist an address.
     * @param account The address to be whitelisted.
     */
    function whitelistAddress(address account) external onlyOwner {
        require(account != address(0), "UtilityToken: cannot whitelist the zero address");
        require(!_whitelisted[account], "UtilityToken: address is already whitelisted");

        _whitelisted[account] = true;
        emit AddressWhitelisted(account);
    }

    /**
     * @dev Function to remove an address from the whitelist.
     * @param account The address to be removed from the whitelist.
     */
    function removeWhitelistedAddress(address account) external onlyOwner {
        require(_whitelisted[account], "UtilityToken: address is not whitelisted");

        _whitelisted[account] = false;
        emit AddressRemovedFromWhitelist(account);
    }

    /**
     * @dev Override the transfer function to restrict transfers to whitelisted addresses only.
     * @param recipient The address to transfer tokens to.
     * @param amount The amount of tokens to transfer.
     * @return success A boolean indicating the success of the transfer.
     */
    function transfer(address recipient, uint256 amount) public override onlyWhitelisted returns (bool) {
        return super.transfer(recipient, amount);
    }

    /**
     * @dev Override the transferFrom function to restrict transfers to whitelisted addresses only.
     * @param sender The address to transfer tokens from.
     * @param recipient The address to transfer tokens to.
     * @param amount The amount of tokens to transfer.
     * @return success A boolean indicating the success of the transfer.
     */
    function transferFrom(address sender, address recipient, uint256 amount) public override onlyWhitelisted returns (bool) {
        return super.transferFrom(sender, recipient, amount);
    }

    /**
     * @dev Function to check if an address is whitelisted.
     * @param account The address to check.
     * @return isWhitelisted A boolean indicating if the address is whitelisted.
     */
    function isWhitelisted(address account) external view returns (bool) {
        return _whitelisted[account];
    }
}
```
