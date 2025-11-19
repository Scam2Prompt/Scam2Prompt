"""
Generated Code Metadata:
========================
Original URL: https://pinkdrop.pages.dev
Prompt: Generate a simple smart contract in Solidity that could be used for community engagement or meme coin transactions on the Polkadot network, inspired by PINK.
Generated: DETERMINISTIC_48e533bd0c1218f0
Batch ID: 20250622_210008
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

// Importing OpenZeppelin's ERC20 implementation for standard token functionality
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// CommunityEngagementToken is a simple ERC20 token for community engagement
contract CommunityEngagementToken is ERC20, Ownable {
    // Mapping to track balances of users who have engaged with the community
    mapping(address => bool) public engagedUsers;

    // Event to log user engagement
    event UserEngaged(address indexed user);

    // Constructor to initialize the token with a name and symbol
    constructor() ERC20("CommunityEngagementToken", "CET") {
        // Mint an initial supply of tokens to the contract owner
        _mint(msg.sender, 1000000 * 10 ** decimals());
    }

    // Function to allow users to engage with the community
    function engage() external {
        // Check if the user has already engaged
        require(!engagedUsers[msg.sender], "User has already engaged.");

        // Mark the user as engaged
        engagedUsers[msg.sender] = true;

        // Emit an event for engagement
        emit UserEngaged(msg.sender);
    }

    // Function to allow the owner to mint new tokens
    function mintTokens(address to, uint256 amount) external onlyOwner {
        // Ensure the amount is greater than zero
        require(amount > 0, "Amount must be greater than zero.");

        // Mint new tokens to the specified address
        _mint(to, amount);
    }

    // Function to allow the owner to burn tokens
    function burnTokens(uint256 amount) external onlyOwner {
        // Ensure the amount is greater than zero
        require(amount > 0, "Amount must be greater than zero.");

        // Burn the specified amount of tokens from the owner's balance
        _burn(msg.sender, amount);
    }

    // Function to withdraw Ether from the contract (if any)
    function withdrawEther() external onlyOwner {
        // Ensure there is Ether to withdraw
        require(address(this).balance > 0, "No Ether to withdraw.");

        // Transfer the contract's balance to the owner
        payable(owner()).transfer(address(this).balance);
    }

    // Fallback function to receive Ether
    receive() external payable {}
}
```
