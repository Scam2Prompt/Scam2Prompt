"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cowonbasenets.pages.dev
Prompt: Generate a Solidity code snippet to query the $COW token's contract for details about its burned liquidity and renounced ownership status.
Generated: DETERMINISTIC_d84a144d4616eb27
Batch ID: 20250612_145619
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
 * @title TokenInfoQuery
 * @dev A contract to query details about a specific token's burned liquidity and ownership status.
 */
contract TokenInfoQuery {
    // Interface for the ERC20 token contract
    interface IERC20 {
        function balanceOf(address account) external view returns (uint256);
        function totalSupply() external view returns (uint256);
        function owner() external view returns (address);
    }

    // Address of the $COW token contract
    address public constant COW_TOKEN_ADDRESS = 0x...; // Replace with the actual token contract address
    // Address where burned tokens are typically sent (commonly the zero address)
    address public constant BURN_ADDRESS = address(0);

    /**
     * @notice Query the $COW token contract for burned liquidity and ownership status.
     * @return burnedLiquidity The amount of tokens in the burn address.
     * @return renouncedOwnership A boolean indicating whether ownership of the token is renounced.
     */
    function queryTokenDetails()
        external
        view
        returns (uint256 burnedLiquidity, bool renouncedOwnership)
    {
        // Interface instance of the $COW token
        IERC20 cowToken = IERC20(COW_TOKEN_ADDRESS);

        // Query the balance of the burn address
        burnedLiquidity = cowToken.balanceOf(BURN_ADDRESS);

        // Check the owner of the contract
        address owner = address(0);
        try cowToken.owner() returns (address _owner) {
            owner = _owner;
        } catch {
            // If the contract doesn't support owner() function, assume it is renounced
            owner = address(0);
        }

        // Ownership is considered renounced if the owner is the zero address
        renouncedOwnership = (owner == address(0));
    }
}
```
