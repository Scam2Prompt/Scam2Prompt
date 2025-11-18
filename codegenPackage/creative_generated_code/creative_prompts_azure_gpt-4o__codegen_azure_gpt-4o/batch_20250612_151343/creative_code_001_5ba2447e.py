"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://basedonpepe.pages.dev
Prompt: Generate Solidity code for a smart contract that interacts with the Based $PEPE token on the BASE chain, specifically using the contract address `0x52b492a33E447Cdb854c7FC19F1e57E8BfA1777D` to verify token balances.
Generated: DETERMINISTIC_5ba2447ef53ed741
Batch ID: 20250612_151343
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
 * @title BasedPEPEBalanceChecker
 * @dev A smart contract to interact with the Based $PEPE token contract on the BASE chain
 *      and retrieve token balances for specific addresses.
 */
contract BasedPEPEBalanceChecker {
    // Address of the Based $PEPE token contract on the BASE chain
    address public constant BASED_PEPE_TOKEN_ADDRESS = 0x52b492a33E447Cdb854c7FC19F1e57E8BfA1777D;

    /**
     * @dev ERC-20 interface for balanceOf function
     */
    interface IERC20 {
        function balanceOf(address account) external view returns (uint256);
    }

    /**
     * @dev Fetches the Based $PEPE token balance of a given address
     * @param account The address whose balance will be checked
     * @return The token balance of the given address
     */
    function getTokenBalance(address account) external view returns (uint256) {
        // Input validation to ensure a valid address
        require(account != address(0), "Invalid account address");

        // Interacting with the Based $PEPE token contract to get the balance
        return IERC20(BASED_PEPE_TOKEN_ADDRESS).balanceOf(account);
    }
}
```
