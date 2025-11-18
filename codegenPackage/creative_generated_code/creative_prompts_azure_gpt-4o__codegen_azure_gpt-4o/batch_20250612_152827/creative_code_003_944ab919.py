"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bitcoindogsclub-en.pages.dev
Prompt: Create a smart contract in Solidity to manage the tokenomics of $0DOG, including the 90% token distribution and automatic removal of unsold tokens after 30 days.
Generated: DETERMINISTIC_944ab91939db00a3
Batch ID: 20250612_152827
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
 * @title $0DOG Tokenomics Smart Contract
 * @dev This contract manages the tokenomics of $0DOG, including distribution and removal of unsold tokens.
 */
contract ZeroDogToken {
    // Token details
    string public constant name = "$0DOG";
    string public constant symbol = "0DOG";
    uint8 public constant decimals = 18;

    // Total supply
    uint256 public constant totalSupply = 1000000 * (10 ** uint256(decimals)); // 1 million tokens

    // Address of the owner
    address public owner;

    // Time for unsold tokens removal
    uint256 public immutable tokenSaleEndTime;
    uint256 public constant DISTRIBUTION_PERCENTAGE = 90; // 90% distribution

    // Balances mapping
    mapping(address => uint256) public balances;

    // Events
    event Transfer(address indexed from, address indexed to, uint256 value);
    event TokensBurned(uint256 amount);

    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    /**
     * @dev Constructor sets the owner and distribution logic.
     */
    constructor() {
        owner = msg.sender;
        tokenSaleEndTime = block.timestamp + 30 days;

        // Allocate 90% of tokens to the owner
        uint256 distributionAmount = (totalSupply * DISTRIBUTION_PERCENTAGE) / 100;
        balances[owner] = distributionAmount;

        // Allocate the remaining 10% to the contract itself (unsold tokens)
        balances[address(this)] = totalSupply - distributionAmount;
    }

    /**
     * @dev Transfer tokens to a specific address.
     * @param to Address to transfer the tokens to.
     * @param amount Amount of tokens to transfer.
     */
    function transfer(address to, uint256 amount) external {
        require(to != address(0), "Cannot transfer to the zero address");
        require(balances[msg.sender] >= amount, "Insufficient balance");

        // Update balances
        balances[msg.sender] -= amount;
        balances[to] += amount;

        emit Transfer(msg.sender, to, amount);
    }

    /**
     * @dev Burns unsold tokens after token sale ends.
     */
    function burnUnsoldTokens() external onlyOwner {
        require(block.timestamp > tokenSaleEndTime, "Token sale is still ongoing");

        uint256 unsoldTokens = balances[address(this)];
        require(unsoldTokens > 0, "No unsold tokens to burn");

        // Burn unsold tokens
        balances[address(this)] = 0;

        emit TokensBurned(unsoldTokens);
    }

    /**
     * @dev Fallback function to prevent accidental ETH transfers.
     */
    receive() external payable {
        revert("Contract does not accept ETH");
    }
}
```
