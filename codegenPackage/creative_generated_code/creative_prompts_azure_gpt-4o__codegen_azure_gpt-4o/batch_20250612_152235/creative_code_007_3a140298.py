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

/**
 * @title AlienTokenPresale
 * @dev Contract for managing the presale of ALIEN tokens with a strict supply cap.
 */
contract AlienTokenPresale {
    // Total supply limit for ALIEN tokens during presale
    uint256 public constant TOTAL_SUPPLY_LIMIT = 100_000_000 * 10**18; // 100 million ALIEN tokens (assuming 18 decimals)

    // Current total minted tokens during presale
    uint256 public totalMinted;

    // Address of the token owner
    address public owner;

    // Event emitted when tokens are minted
    event TokensMinted(address indexed to, uint256 amount);

    // Modifier to restrict access to the contract owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    /**
     * @dev Sets the deployer as the initial owner of the contract.
     */
    constructor() {
        owner = msg.sender;
    }

    /**
     * @dev Mint tokens during the presale. Ensures that the total supply limit is not exceeded.
     * @param to The address to receive the minted tokens.
     * @param amount The number of tokens to mint (in wei, including decimals).
     */
    function mint(address to, uint256 amount) external onlyOwner {
        require(to != address(0), "Cannot mint to the zero address");
        require(amount > 0, "Mint amount should be greater than zero");
        require(totalMinted + amount <= TOTAL_SUPPLY_LIMIT, "Minting exceeds total supply limit");

        // Update total minted
        totalMinted += amount;

        // Emit event
        emit TokensMinted(to, amount);

        // Logic for transferring tokens can be implemented here
        // In a real-world scenario, you'd call the token contract directly (e.g., ERC20's _mint function).
    }

    /**
     * @dev Allows the contract owner to update ownership to a new address.
     * @param newOwner The address of the new owner.
     */
    function transferOwnership(address newOwner) external onlyOwner {
        require(newOwner != address(0), "New owner cannot be the zero address");
        owner = newOwner;
    }
}
```
