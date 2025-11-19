"""
Generated Code Metadata:
========================
Original URL: https://remixethereum.pages.dev
Prompt: Create a basic ERC20 token smart contract using Remix's project templates and Solidity compiler, and describe how to customize and deploy it.
Generated: DETERMINISTIC_d7bf3e4381891594
Batch ID: 20250622_204901
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";

/**
 * @title MyToken
 * @dev Very simple ERC20 Token example, where all tokens are pre-assigned to the creator.
 * Note they can later distribute these tokens as they wish using `transfer` and other
 * ERC20 functions.
 */
contract MyToken is ERC20 {
    /**
     * @dev Constructor that gives msg.sender all of existing tokens.
     * @param initialSupply The initial supply of tokens.
     * @param tokenName The name of the token.
     * @param tokenSymbol The symbol of the token.
     */
    constructor(
        uint256 initialSupply,
        string memory tokenName,
        string memory tokenSymbol
    ) ERC20(tokenName, tokenSymbol) {
        _mint(msg.sender, initialSupply);
    }
}
```

To customize and deploy:
1. Open Remix IDE
2. Create new file (e.g., MyToken.sol)
3. Paste this code
4. Install OpenZeppelin contracts via Remix's "File Explorer" -> "Dependencies"
5. Compile with Solidity compiler (0.8.0+)
6. Deploy via "Deploy & Run Transactions" tab:
   - Enter initialSupply (in wei)
   - Enter tokenName (string)
   - Enter tokenSymbol (string)
7. Click "Deploy"
