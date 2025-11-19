"""
Generated Code Metadata:
========================
Original URL: https://basedbrettoken.web.app
Prompt: Create a smart contract on the BASE chain that integrates BRETT token utilities and supports strategic partnerships with other crypto projects.
Generated: DETERMINISTIC_65cac8ccacdc562b
Batch ID: 20250612_152710
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

// Importing OpenZeppelin's ERC20 implementation for the BRETT token
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Smart contract for BRETT token utilities and strategic partnerships
contract BrettTokenUtility is ERC20, Ownable {
    // Mapping to track partnerships
    mapping(address => bool) public partnerships;

    // Event emitted when a new partnership is established
    event PartnershipEstablished(address indexed partner);

    // Event emitted when a partnership is revoked
    event PartnershipRevoked(address indexed partner);

    // Constructor to initialize the BRETT token
    constructor() ERC20("BRETT Token", "BRETT") {
        // Mint an initial supply of tokens to the contract owner
        _mint(msg.sender, 1000000 * 10 ** decimals()); // 1 million tokens
    }

    // Function to establish a partnership
    function establishPartnership(address partner) external onlyOwner {
        require(partner != address(0), "Invalid partner address");
        require(!partnerships[partner], "Partnership already exists");

        partnerships[partner] = true;
        emit PartnershipEstablished(partner);
    }

    // Function to revoke a partnership
    function revokePartnership(address partner) external onlyOwner {
        require(partnerships[partner], "Partnership does not exist");

        partnerships[partner] = false;
        emit PartnershipRevoked(partner);
    }

    // Function to transfer tokens with a partnership check
    function transferWithPartnershipCheck(address recipient, uint256 amount) external returns (bool) {
        require(partnerships[recipient], "Recipient is not a partner");
        return transfer(recipient, amount);
    }

    // Function to mint new tokens (only callable by the owner)
    function mintTokens(address to, uint256 amount) external onlyOwner {
        require(to != address(0), "Invalid address");
        _mint(to, amount);
    }

    // Function to burn tokens (only callable by the owner)
    function burnTokens(uint256 amount) external onlyOwner {
        _burn(msg.sender, amount);
    }

    // Function to check if an address is a partner
    function isPartner(address partner) external view returns (bool) {
        return partnerships[partner];
    }
}
```
