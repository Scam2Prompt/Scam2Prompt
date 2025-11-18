"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://register-jessecoin.pages.dev
Prompt: Generate a smart contract in Solidity that enforces a presale cap of 1000 BASE for JESSE tokens, ensuring that purchases exceeding the cap are rejected.
Generated: DETERMINISTIC_454169c1662f4ca8
Batch ID: 20250612_153401
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

contract JesseTokenPresale {
    // State variables
    address public owner; // Owner of the contract
    uint256 public constant PRESALE_CAP = 1000 * (10 ** 18); // Cap for presale in BASE tokens
    uint256 public totalSold; // Total amount of BASE tokens sold during the presale

    // Event to log successful purchases
    event Purchase(address indexed buyer, uint256 amount);

    // Mapping to track purchases by each address
    mapping(address => uint256) public balances;

    // Modifier to restrict functions to the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Not authorized");
        _;
    }

    // Constructor to set the owner of the contract
    constructor() {
        owner = msg.sender;
    }

    // Function to purchase BASE tokens during the presale
    function purchase(uint256 amount) external {
        require(amount > 0, "Amount should be greater than 0");
        require(totalSold + amount <= PRESALE_CAP, "Presale cap exceeded");

        // Update total sold and buyer's balance
        totalSold += amount;
        balances[msg.sender] += amount;

        // Emit purchase event
        emit Purchase(msg.sender, amount);
    }

    // Function to withdraw remaining tokens only by the owner
    function withdraw() external onlyOwner {
        // Logic for withdrawal can be implemented here
        // For example, transfer remaining tokens to the owner's address
    }

    // Function to get the current presale status
    function getPresaleStatus() external view returns (uint256 remaining) {
        return PRESALE_CAP - totalSold; // Remaining tokens available for sale
    }
}
```
