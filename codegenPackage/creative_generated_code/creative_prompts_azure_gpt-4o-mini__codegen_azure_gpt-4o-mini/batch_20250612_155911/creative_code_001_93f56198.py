"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://eth-coin-creator.pages.dev
Prompt: Write a Solidity code snippet for creating a token on the BNB Smart Chain with 100% ownership and a $1 creation fee.
Generated: DETERMINISTIC_93f56198862511d1
Batch ID: 20250612_155911
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

// Importing OpenZeppelin's ERC20 contract and Ownable contract for standard token functionality and ownership control
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract MyToken is ERC20, Ownable {
    // Setting the creation fee in wei (1 BNB = 10^18 wei; hence $1 is represented here in wei)
    uint256 public constant CREATION_FEE = 1 ether / 1000; // Adjust according to current BNB price

    // Mapping to track if an address has already created a token
    mapping(address => bool) public hasCreatedToken;

    // Event to log token creation
    event TokenCreated(address indexed creator, uint256 amount);

    // Constructor to initialize the token with a name and symbol
    constructor() ERC20("MyToken", "MTK") {
        // Minting initial supply to the contract owner
        _mint(msg.sender, 1000000 * 10 ** decimals()); // Minting 1,000,000 tokens
    }

    // Function to create tokens, requires a fee to be paid
    function createTokens(uint256 amount) external payable {
        // Check if the sender has already created a token
        require(!hasCreatedToken[msg.sender], "Token already created by this address.");
        // Check if the correct creation fee is sent
        require(msg.value >= CREATION_FEE, "Insufficient fee sent.");

        // Mint the specified amount of tokens to the creator
        _mint(msg.sender, amount * 10 ** decimals());
        hasCreatedToken[msg.sender] = true;

        // Emit the token creation event
        emit TokenCreated(msg.sender, amount);
    }

    // Function to withdraw the collected fees to the owner
    function withdrawFees() external onlyOwner {
        // Transfer the contract's balance to the owner
        payable(owner()).transfer(address(this).balance);
    }

    // Fallback function to receive ether
    receive() external payable {}

    // Function to allow the owner to destroy the contract if needed
    function destroy() external onlyOwner {
        selfdestruct(payable(owner()));
    }
}
```
