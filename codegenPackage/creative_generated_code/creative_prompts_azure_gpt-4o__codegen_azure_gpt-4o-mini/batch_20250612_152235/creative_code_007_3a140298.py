"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bafybeiexkodjd2izwx6r53x5g4q54yhqmiifywanhuecvkkdn2yyxq3rpu.ipfs.dweb.link
Prompt: Write a function in Solidity that enforces the total token supply limit of 100,000,000 ALIEN during the presale, ensuring no additional tokens are minted beyond this limit.
Generated: DETERMINISTIC_3a140298792c088f
Batch ID: 20250612_152235
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

contract AlienToken {
    // Total supply limit constant
    uint256 public constant MAX_SUPPLY = 100_000_000 * 10 ** 18; // 100 million tokens with 18 decimals
    uint256 public totalSupply; // Current total supply of the token
    mapping(address => uint256) public balances; // Mapping to track token balances of addresses
    address public owner; // Owner of the contract

    // Event to log token minting
    event TokensMinted(address indexed to, uint256 amount);

    // Modifier to restrict access to the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Not the contract owner");
        _;
    }

    // Constructor to initialize the contract's owner
    constructor() {
        owner = msg.sender;
    }

    // Function to mint new tokens during the presale
    function mintTokens(address to, uint256 amount) external onlyOwner {
        require(totalSupply + amount <= MAX_SUPPLY, "Supply limit exceeded");
        require(to != address(0), "Invalid address");

        totalSupply += amount; // Update total supply
        balances[to] += amount; // Update recipient's balance

        emit TokensMinted(to, amount); // Emit an event for minted tokens
    }

    // Function to check the balance of an address
    function balanceOf(address account) external view returns (uint256) {
        return balances[account];
    }
}
```
