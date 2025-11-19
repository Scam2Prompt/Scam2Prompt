"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rangersprotocol.gitbook.io
Prompt: What is the process for creating and managing sub-chains on the Rangers Protocol? Include a code example for issuing RAP20 tokens.
Generated: DETERMINISTIC_479ab47fbd873674
Batch ID: 20250612_135144
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
 * @title RAP20 Token Contract Example
 * @dev Rangers Protocol supports creating sub-chains and issuing RAP20 tokens.
 * This contract demonstrates issuing RAP20 tokens on a Rangers Protocol sub-chain.
 * Ensure to deploy this contract on a sub-chain of Rangers Protocol.
 */

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract RAP20Token is ERC20, Ownable {
    /**
     * @dev Constructor to initialize the RAP20 token with a name and symbol.
     * @param name Name of the token.
     * @param symbol Symbol representing the token.
     * @param initialSupply Initial token supply (in smallest units) to mint to the deployer's address.
     */
    constructor(
        string memory name,
        string memory symbol,
        uint256 initialSupply
    ) ERC20(name, symbol) {
        // Mint the initial supply of tokens to the owner (deployer's address)
        _mint(msg.sender, initialSupply);
    }

    /**
     * @notice Mint new tokens to a specified address.
     * @param to Address to receive the new tokens.
     * @param amount Number of tokens to mint (in smallest units).
     * Only the contract owner can call this function.
     */
    function mint(address to, uint256 amount) external onlyOwner {
        _mint(to, amount);
    }

    /**
     * @notice Burn tokens from the caller's balance.
     * @param amount Number of tokens to burn (in smallest units).
     */
    function burn(uint256 amount) external {
        _burn(msg.sender, amount);
    }
}
```

### Steps for Sub-chain Management and RAP20 Token Deployment:
1. **Sub-chain Creation:** Set up a sub-chain using Rangers Protocol, following their documentation to configure nodes and parameters.
2. **Deploy RAP20 Token Contract:** Use the above contract to issue RAP20 tokens on the sub-chain. Replace `name`, `symbol`, and `initialSupply` in the constructor with your desired values.
3. **Interact with the Contract:**
   - Mint tokens using the `mint` function (restricted to the owner).
   - Burn tokens using the `burn` function.

To deploy and interact with this contract, use a deployment tool like Hardhat, Truffle, or Remix, and connect to your Rangers Protocol sub-chain.
