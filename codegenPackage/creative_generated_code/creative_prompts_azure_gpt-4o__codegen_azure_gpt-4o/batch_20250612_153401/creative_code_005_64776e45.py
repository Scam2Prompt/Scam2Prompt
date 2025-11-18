"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://register-jessecoin.pages.dev
Prompt: Develop a Solidity contract that includes a function to mint JESSE tokens at the specified rate (0.1 BASE = 99,500 JESSE) and ensures the total supply does not exceed 100,000,000 tokens.
Generated: DETERMINISTIC_64776e4514cb15fa
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

/**
 * @title JESSE Token Contract
 * @dev This contract implements a minting mechanism for JESSE tokens,
 * ensuring the total supply does not exceed 100,000,000 tokens.
 */
contract JesseToken {
    // Token details
    string public name = "JESSE Token";
    string public symbol = "JESSE";
    uint8 public decimals = 18;

    // Total supply cap
    uint256 public constant MAX_SUPPLY = 100_000_000 * (10 ** uint256(decimals));

    // Rate of minting: 0.1 BASE = 99,500 JESSE
    uint256 public constant MINT_RATE = 99500 * (10 ** uint256(decimals - 1)); // Adjusting for 0.1 BASE

    // Current total supply of the token
    uint256 public totalSupply;

    // Balances mapping
    mapping(address => uint256) public balanceOf;

    // Owner of the contract
    address public owner;

    // Events
    event Transfer(address indexed from, address indexed to, uint256 value);
    event Mint(address indexed to, uint256 value);

    // Modifier to restrict access to owner-only functions
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    /**
     * @dev Constructor that sets the deployer as the owner.
     */
    constructor() {
        owner = msg.sender;
    }

    /**
     * @dev Function to mint JESSE tokens, ensuring total supply does not exceed the max cap.
     * @param to The address to which tokens will be minted.
     * @param baseAmount The amount of BASE tokens being spent.
     */
    function mint(address to, uint256 baseAmount) external onlyOwner {
        // Calculate the amount of JESSE tokens to mint based on the specified rate
        uint256 jesseAmount = (baseAmount * MINT_RATE) / (10 ** uint256(decimals));

        // Ensure the total supply does not exceed the maximum cap
        require(totalSupply + jesseAmount <= MAX_SUPPLY, "Minting exceeds max supply");

        // Update balances and total supply
        balanceOf[to] += jesseAmount;
        totalSupply += jesseAmount;

        // Emit the mint and transfer events
        emit Mint(to, jesseAmount);
        emit Transfer(address(0), to, jesseAmount);
    }

    /**
     * @dev Function to check the remaining mintable tokens.
     * @return The number of tokens that can still be minted.
     */
    function remainingSupply() external view returns (uint256) {
        return MAX_SUPPLY - totalSupply;
    }
}
```
