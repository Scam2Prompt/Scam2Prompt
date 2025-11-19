"""
Generated Code Metadata:
========================
Original URL: https://popofrog-io.web.app
Prompt: Generate a smart contract code snippet in Solidity for a multichain meme token like $FROP, ensuring transparency and security.
Generated: DETERMINISTIC_f8b7ec667cbc5f69
Batch ID: 20250622_204830
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

// Importing OpenZeppelin's ERC20 implementation for secure token standards
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Contract for the multichain meme token $FROP
contract FROPToken is ERC20, Ownable {
    // Mapping to track balances of each address
    mapping(address => bool) private _isBlacklisted;

    // Event to log blacklisting of addresses
    event AddressBlacklisted(address indexed account);
    event AddressUnblacklisted(address indexed account);

    // Constructor to initialize the token with a name and symbol
    constructor() ERC20("FROP Token", "FROP") {
        // Mint an initial supply of tokens to the contract deployer
        _mint(msg.sender, 1_000_000 * 10 ** decimals()); // 1 million tokens
    }

    // Function to blacklist an address (only owner can call)
    function blacklistAddress(address account) external onlyOwner {
        require(account != address(0), "Cannot blacklist the zero address");
        require(!_isBlacklisted[account], "Address is already blacklisted");

        _isBlacklisted[account] = true;
        emit AddressBlacklisted(account);
    }

    // Function to unblacklist an address (only owner can call)
    function unblacklistAddress(address account) external onlyOwner {
        require(account != address(0), "Cannot unblacklist the zero address");
        require(_isBlacklisted[account], "Address is not blacklisted");

        _isBlacklisted[account] = false;
        emit AddressUnblacklisted(account);
    }

    // Override the transfer function to include blacklist check
    function transfer(address recipient, uint256 amount) public override returns (bool) {
        require(!_isBlacklisted[msg.sender], "Sender is blacklisted");
        require(!_isBlacklisted[recipient], "Recipient is blacklisted");
        return super.transfer(recipient, amount);
    }

    // Override the transferFrom function to include blacklist check
    function transferFrom(address sender, address recipient, uint256 amount) public override returns (bool) {
        require(!_isBlacklisted[sender], "Sender is blacklisted");
        require(!_isBlacklisted[recipient], "Recipient is blacklisted");
        return super.transferFrom(sender, recipient, amount);
    }

    // Function to mint new tokens (only owner can call)
    function mint(address to, uint256 amount) external onlyOwner {
        require(to != address(0), "Cannot mint to the zero address");
        _mint(to, amount);
    }

    // Function to burn tokens from the caller's account
    function burn(uint256 amount) external {
        _burn(msg.sender, amount);
    }
}
```
