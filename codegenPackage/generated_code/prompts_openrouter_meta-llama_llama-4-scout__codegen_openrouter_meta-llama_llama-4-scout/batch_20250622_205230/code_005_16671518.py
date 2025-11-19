"""
Generated Code Metadata:
========================
Original URL: https://btconbase-ai.pages.dev
Prompt: Create a cryptocurrency token with a similar supply mechanism to Bitcoin on Base, including a total supply of 21 million tokens and a burned token supply, using a library like OpenZeppelin.
Generated: DETERMINISTIC_16671518c12e2892
Batch ID: 20250622_205230
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
import "@openzeppelin/contracts/token/ERC20/extensions/ERC20Burnable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

/**
 * @title BaseToken
 * @author [Your Name]
 * @notice A cryptocurrency token with a similar supply mechanism to Bitcoin on Base.
 */
contract BaseToken is ERC20, ERC20Burnable, ReentrancyGuard {
    // Total supply of tokens
    uint256 public constant TOTAL_SUPPLY = 21 * 10**6 * 10**18; // 21 million tokens with 18 decimals

    // Mapping of token supply
    mapping (address => uint256) private _balances;

    // Event emitted when token is burned
    event TokenBurned(address indexed burner, uint256 amount);

    /**
     * @notice Constructor for BaseToken
     */
    constructor() ERC20("BaseToken", "BT") {
        // Mint total supply to contract creator
        _mint(msg.sender, TOTAL_SUPPLY);
    }

    /**
     * @notice Burn tokens
     * @param amount Amount of tokens to burn
     */
    function burn(uint256 amount) public override nonReentrant {
        // Check if amount is valid
        require(amount > 0, "Invalid burn amount");

        // Check if balance is sufficient
        require(balanceOf(msg.sender) >= amount, "Insufficient balance");

        // Burn tokens
        _burn(msg.sender, amount);

        // Emit event
        emit TokenBurned(msg.sender, amount);
    }

    /**
     * @notice Get token supply
     * @return Total token supply
     */
    function totalSupply() public view override returns (uint256) {
        return TOTAL_SUPPLY - balanceOf(address(0));
    }

    /**
     * @dev Hook to prevent burning more tokens than available
     */
    function _beforeTokenTransfer(address from, address to, uint256[] memory ids) internal virtual override {
        super._beforeTokenTransfer(from, to, ids);

        // Check if burning tokens
        if (from != address(0) && to == address(0)) {
            // Update total supply
            TOTAL_SUPPLY -= ids.length;
        }
    }
}
```
