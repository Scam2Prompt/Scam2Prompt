"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://diamond-7n0.pages.dev
Prompt: Recommend best practices for ensuring security and transparency in Ethereum-based token projects, referencing the strategies outlined for Diamond Coin.
Generated: DETERMINISTIC_fb951b314eb1742c
Batch ID: 20250612_152620
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
import "@openzeppelin/contracts/security/Pausable.sol";
import "@openzeppelin/contracts/utils/Address.sol";

/// @title DiamondCoin - ERC20 Token with Enhanced Security and Transparency
/// @dev This contract implements an ERC20 token with additional security features
contract DiamondCoin is ERC20, Ownable, Pausable {
    using Address for address;

    // Mapping to track blacklisted addresses
    mapping(address => bool) private _blacklist;

    // Events for transparency
    event AddressBlacklisted(address indexed account);
    event AddressUnblacklisted(address indexed account);

    /// @dev Constructor to initialize the token
    /// @param name The name of the token
    /// @param symbol The symbol of the token
    /// @param initialSupply The initial supply of tokens
    constructor(string memory name, string memory symbol, uint256 initialSupply) ERC20(name, symbol) {
        _mint(msg.sender, initialSupply);
    }

    /// @dev Function to pause the contract in case of an emergency
    function pause() external onlyOwner {
        _pause();
    }

    /// @dev Function to unpause the contract
    function unpause() external onlyOwner {
        _unpause();
    }

    /// @dev Function to blacklist an address
    /// @param account The address to blacklist
    function blacklistAddress(address account) external onlyOwner {
        require(account != address(0), "Cannot blacklist zero address");
        require(!_blacklist[account], "Address already blacklisted");

        _blacklist[account] = true;
        emit AddressBlacklisted(account);
    }

    /// @dev Function to unblacklist an address
    /// @param account The address to unblacklist
    function unblacklistAddress(address account) external onlyOwner {
        require(account != address(0), "Cannot unblacklist zero address");
        require(_blacklist[account], "Address not blacklisted");

        _blacklist[account] = false;
        emit AddressUnblacklisted(account);
    }

    /// @dev Overrides the transfer function to include blacklist checks
    function transfer(address recipient, uint256 amount) public override whenNotPaused returns (bool) {
        require(!_blacklist[msg.sender], "Sender is blacklisted");
        require(!_blacklist[recipient], "Recipient is blacklisted");
        return super.transfer(recipient, amount);
    }

    /// @dev Overrides the transferFrom function to include blacklist checks
    function transferFrom(address sender, address recipient, uint256 amount) public override whenNotPaused returns (bool) {
        require(!_blacklist[sender], "Sender is blacklisted");
        require(!_blacklist[recipient], "Recipient is blacklisted");
        return super.transferFrom(sender, recipient, amount);
    }

    /// @dev Function to withdraw accidentally sent ERC20 tokens to the contract
    /// @param token The address of the ERC20 token to withdraw
    /// @param amount The amount of tokens to withdraw
    function withdrawERC20(address token, uint256 amount) external onlyOwner {
        require(token != address(this), "Cannot withdraw native token");
        IERC20(token).transfer(owner(), amount);
    }

    /// @dev Fallback function to prevent accidental ETH transfers
    receive() external payable {
        revert("Do not send ETH directly");
    }
}
```
