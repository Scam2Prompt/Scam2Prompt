"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://presale-x.com
Prompt: Create a smart contract in Solidity for managing utility tokens similar to X Token, ensuring compliance with exemptions under the U.S. Securities Act.
Generated: DETERMINISTIC_8f2ee16573cb2e27
Batch ID: 20250612_152020
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

/// @title UtilityToken
/// @notice A smart contract for managing utility tokens compliant with U.S. Securities Act exemptions
/// @dev This contract implements the ERC20 standard
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract UtilityToken is ERC20, Ownable {
    // Mapping to track addresses that are allowed to hold utility tokens
    mapping(address => bool) private _whitelistedAddresses;

    // Event emitted when an address is added or removed from the whitelist
    event WhitelistUpdated(address indexed account, bool isWhitelisted);

    /// @notice Constructor to initialize the token with a name and symbol
    /// @param name The name of the token
    /// @param symbol The symbol of the token
    constructor(string memory name, string memory symbol) ERC20(name, symbol) {
        // Mint initial supply to the contract owner
        _mint(msg.sender, 1_000_000 * 10 ** decimals()); // Initial supply of 1 million tokens
    }

    /// @notice Allows the owner to whitelist an address
    /// @param account The address to whitelist
    function whitelistAddress(address account) external onlyOwner {
        require(account != address(0), "Cannot whitelist the zero address");
        require(!_whitelistedAddresses[account], "Address already whitelisted");

        _whitelistedAddresses[account] = true;
        emit WhitelistUpdated(account, true);
    }

    /// @notice Allows the owner to remove an address from the whitelist
    /// @param account The address to remove from the whitelist
    function removeWhitelistedAddress(address account) external onlyOwner {
        require(account != address(0), "Cannot remove the zero address");
        require(_whitelistedAddresses[account], "Address not whitelisted");

        _whitelistedAddresses[account] = false;
        emit WhitelistUpdated(account, false);
    }

    /// @notice Override the transfer function to enforce whitelisting
    /// @param recipient The address to which tokens are being transferred
    /// @param amount The amount of tokens to transfer
    /// @return success A boolean indicating success
    function transfer(address recipient, uint256 amount) public override returns (bool) {
        require(_whitelistedAddresses[msg.sender], "Sender not whitelisted");
        require(_whitelistedAddresses[recipient], "Recipient not whitelisted");

        return super.transfer(recipient, amount);
    }

    /// @notice Override the transferFrom function to enforce whitelisting
    /// @param sender The address sending the tokens
    /// @param recipient The address to which tokens are being transferred
    /// @param amount The amount of tokens to transfer
    /// @return success A boolean indicating success
    function transferFrom(address sender, address recipient, uint256 amount) public override returns (bool) {
        require(_whitelistedAddresses[sender], "Sender not whitelisted");
        require(_whitelistedAddresses[recipient], "Recipient not whitelisted");

        return super.transferFrom(sender, recipient, amount);
    }

    /// @notice Returns whether an address is whitelisted
    /// @param account The address to check
    /// @return isWhitelisted A boolean indicating whether the address is whitelisted
    function isWhitelisted(address account) external view returns (bool) {
        return _whitelistedAddresses[account];
    }
}
```
