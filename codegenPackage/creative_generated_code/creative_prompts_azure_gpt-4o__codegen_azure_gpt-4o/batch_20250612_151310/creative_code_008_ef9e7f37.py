"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kelexocrypto.pages.dev
Prompt: Provide example code to implement a token burn event for a cryptocurrency project, similar to the burn event mentioned in the KoalaKash roadmap.
Generated: DETERMINISTIC_ef9e7f37112f1de3
Batch ID: 20250612_151310
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
 * @title TokenBurnable
 * @dev Implements a token burn feature for a cryptocurrency project.
 */
contract TokenBurnable {
    // Token name and symbol
    string public name = "KoalaKash";
    string public symbol = "KKASH";

    // Total supply of the token
    uint256 public totalSupply;

    // Mapping to track balances of each address
    mapping(address => uint256) public balances;

    // Address of the contract owner
    address public owner;

    // Event emitted when tokens are burned
    event TokensBurned(address indexed burner, uint256 amount);

    // Modifier to restrict actions to the contract owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    // Constructor to initialize the contract
    constructor(uint256 initialSupply) {
        owner = msg.sender;         // Set the contract owner
        totalSupply = initialSupply; // Set the total supply
        balances[owner] = totalSupply; // Assign all tokens to the owner initially
    }

    /**
     * @dev Burn tokens from the sender's balance.
     * @param amount The number of tokens to burn.
     */
    function burn(uint256 amount) external {
        require(amount > 0, "Burn amount must be greater than zero");
        require(balances[msg.sender] >= amount, "Insufficient balance to burn");

        // Reduce the sender's balance and the total supply
        balances[msg.sender] -= amount;
        totalSupply -= amount;

        // Emit the TokensBurned event
        emit TokensBurned(msg.sender, amount);
    }

    /**
     * @dev Get the balance of a specific address.
     * @param account The address to query the balance.
     * @return The balance of the specified address.
     */
    function balanceOf(address account) external view returns (uint256) {
        return balances[account];
    }

    /**
     * @dev Mint new tokens and add to the owner's balance.
     * Note: Only the owner can mint tokens.
     * @param amount The number of tokens to mint.
     */
    function mint(uint256 amount) external onlyOwner {
        require(amount > 0, "Mint amount must be greater than zero");

        // Increase the total supply and the owner's balance
        totalSupply += amount;
        balances[owner] += amount;
    }
}
```
