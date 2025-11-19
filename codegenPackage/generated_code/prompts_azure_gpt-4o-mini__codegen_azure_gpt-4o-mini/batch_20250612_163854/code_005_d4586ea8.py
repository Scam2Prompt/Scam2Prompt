"""
Generated Code Metadata:
========================
Original URL: https://popofrog-io.pages.dev
Prompt: Develop a smart contract for the $FROP token that includes features for transparency and security, as highlighted in the Popo The Frog documentation.
Generated: DETERMINISTIC_d4586ea85c1d6813
Batch ID: 20250612_163854
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
import "@openzeppelin/contracts/utils/Context.sol";

// Smart contract for the $FROP token
contract FROPToken is ERC20, Ownable {
    // Mapping to track balances of holders
    mapping(address => bool) private _isBlacklisted;

    // Event emitted when an address is blacklisted
    event Blacklisted(address indexed account);
    
    // Event emitted when an address is removed from the blacklist
    event Unblacklisted(address indexed account);

    // Constructor to initialize the token with a name and symbol
    constructor() ERC20("FROP Token", "$FROP") {
        // Mint initial supply to the contract deployer
        _mint(msg.sender, 1000000 * 10 ** decimals()); // 1 million tokens
    }

    // Function to blacklist an address
    function blacklistAddress(address account) external onlyOwner {
        require(account != address(0), "Cannot blacklist the zero address");
        require(!_isBlacklisted[account], "Address is already blacklisted");

        _isBlacklisted[account] = true;
        emit Blacklisted(account);
    }

    // Function to remove an address from the blacklist
    function unblacklistAddress(address account) external onlyOwner {
        require(account != address(0), "Cannot unblacklist the zero address");
        require(_isBlacklisted[account], "Address is not blacklisted");

        _isBlacklisted[account] = false;
        emit Unblacklisted(account);
    }

    // Override the transfer function to include blacklist check
    function _transfer(address sender, address recipient, uint256 amount) internal override {
        require(!_isBlacklisted[sender], "Sender is blacklisted");
        require(!_isBlacklisted[recipient], "Recipient is blacklisted");
        super._transfer(sender, recipient, amount);
    }

    // Function to check if an address is blacklisted
    function isBlacklisted(address account) external view returns (bool) {
        return _isBlacklisted[account];
    }
}
```
