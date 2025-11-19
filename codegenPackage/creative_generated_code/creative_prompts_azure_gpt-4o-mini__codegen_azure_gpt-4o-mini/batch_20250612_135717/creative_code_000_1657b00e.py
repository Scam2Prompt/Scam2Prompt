"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://apedcoin.com
Prompt: Generate a smart contract for the APED token ($APED) with a total supply of 1,000,000,000 and the specified contract address.
Generated: DETERMINISTIC_1657b00ef46dea1b
Batch ID: 20250612_135717
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

// Importing OpenZeppelin's ERC20 implementation to leverage best practices
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title APEDToken
 * @dev Implementation of the ERC20 Token standard for the APED token.
 */
contract APEDToken is ERC20, Ownable {
    // Total supply of the token
    uint256 private constant _totalSupply = 1_000_000_000 * (10 ** uint256(decimals()));

    /**
     * @dev Constructor that gives msg.sender all of existing tokens.
     */
    constructor() ERC20("APED Token", "$APED") {
        // Mint the total supply to the contract owner (msg.sender)
        _mint(msg.sender, _totalSupply);
    }

    /**
     * @dev Function to burn tokens, reducing the total supply.
     * @param amount The amount of tokens to burn.
     */
    function burn(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        _burn(msg.sender, amount);
    }

    /**
     * @dev Function to retrieve the total supply of the token.
     * @return totalSupply The total supply of the token.
     */
    function totalSupply() public view override returns (uint256) {
        return _totalSupply;
    }
}
```

Note: Ensure you have the OpenZeppelin Contracts library installed in your development environment. You can install it using npm:

```bash
npm install @openzeppelin/contracts
```
