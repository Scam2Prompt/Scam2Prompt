"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tokenscreatorpro2025.pages.dev
Prompt: Generate code to create a token on the Ethereum network with 100% ownership and a $1 creation fee, as described on Tokens Creator Pro 2025.
Generated: DETERMINISTIC_854095cb3d3db51b
Batch ID: 20250612_145916
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

// Importing the OpenZeppelin ERC20 contract for the token implementation
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Contract that creates a new ERC20 token with 100% ownership by the deployer
contract TokenCreator is ERC20, Ownable {
    // Constant for the creation fee
    uint256 public constant CREATION_FEE = 0.01 ether; // $1 in Wei (1 ether = 10^18 Wei)

    // Event emitted when a new token is created
    event TokenCreated(address indexed creator, string name, string symbol);

    // Constructor to initialize the token with a name and symbol
    constructor(string memory name, string memory symbol) ERC20(name, symbol) payable {
        // Require the creation fee to be paid
        require(msg.value == CREATION_FEE, "Incorrect creation fee sent");
        // The deployer has 100% ownership
        _mint(msg.sender, 1000000 * 10 ** decimals()); // Minting 1 million tokens
        emit TokenCreated(msg.sender, name, symbol);
    }

    // Function to withdraw the creation fee to the contract owner
    function withdrawFees() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No funds to withdraw");
        payable(owner()).transfer(balance);
    }

    // Fallback function to receive Ether
    receive() external payable {
        revert("Direct Ether transfers are not allowed.");
    }
}
```

### Notes:
- This code uses OpenZeppelin's ERC20 implementation to manage the token functionality and ownership.
- The contract requires a creation fee of $1 (in Ether) to be sent when deploying the contract.
- It includes error handling for fee validation and withdrawal.
- The `withdrawFees` function allows the contract owner to withdraw any fees collected.
- A fallback function is implemented to prevent direct Ether transfers to the contract.
