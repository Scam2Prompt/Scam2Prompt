"""
Generated Code Metadata:
========================
Original URL: https://spacem-world.vercel.app
Prompt: Design a simple smart contract in Solidity for distributing SpaceM Tokens as rewards in a cryptocurrency campaign.
Generated: DETERMINISTIC_3661143b68e5d314
Batch ID: 20250622_211721
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

// Importing OpenZeppelin's ERC20 implementation for token standards
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// SpaceM Token contract inheriting from ERC20 and Ownable
contract SpaceMToken is ERC20, Ownable {
    // Event to log the distribution of tokens
    event TokensDistributed(address indexed recipient, uint256 amount);

    // Constructor to initialize the token with a name and symbol
    constructor() ERC20("SpaceM Token", "SPM") {
        // Mint initial supply to the contract owner
        _mint(msg.sender, 1000000 * 10 ** decimals()); // 1 million tokens
    }

    // Function to distribute tokens to a list of recipients
    // Only the owner can call this function
    function distributeTokens(address[] calldata recipients, uint256 amount) external onlyOwner {
        require(recipients.length > 0, "No recipients provided");
        require(amount > 0, "Amount must be greater than zero");
        require(balanceOf(msg.sender) >= amount * recipients.length, "Insufficient balance for distribution");

        for (uint256 i = 0; i < recipients.length; i++) {
            require(recipients[i] != address(0), "Invalid recipient address");
            _transfer(msg.sender, recipients[i], amount);
            emit TokensDistributed(recipients[i], amount);
        }
    }

    // Function to withdraw tokens from the contract (only owner)
    function withdrawTokens(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        require(balanceOf(address(this)) >= amount, "Insufficient contract balance");

        _transfer(address(this), msg.sender, amount);
    }
}
```
