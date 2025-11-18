"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://planetserfi.pages.dev
Prompt: Write a smart contract in Solidity to tokenize Real-World Assets (RWA) on a blockchain platform, ensuring compliance with sustainable development goals (SDGs) as outlined by Planet ReFi.
Generated: DETERMINISTIC_572d97ce2c420ff6
Batch ID: 20250612_152739
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
 * @title RealWorldAssetToken
 * @dev A smart contract to tokenize Real-World Assets (RWA) ensuring compliance with SDGs.
 * This contract uses ERC-20 standards and includes mechanisms to enforce compliance with sustainable practices.
 */
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract RealWorldAssetToken is ERC20, Ownable {
    // Mapping to track compliance status of token holders
    mapping(address => bool) public complianceStatus;

    // Event emitted when a user's compliance status is updated
    event ComplianceStatusUpdated(address indexed user, bool status);

    /**
     * @dev Constructor that initializes the token name and symbol.
     * @param name_ The name of the token.
     * @param symbol_ The symbol of the token.
     */
    constructor(string memory name_, string memory symbol_) ERC20(name_, symbol_) {}

    /**
     * @dev Modifier to check compliance before transferring tokens.
     */
    modifier onlyCompliant(address account) {
        require(complianceStatus[account], "Account is not compliant with SDGs.");
        _;
    }

    /**
     * @dev Function to update compliance status for an account.
     * @param account The address of the user.
     * @param status Boolean value representing compliance (true for compliant, false otherwise).
     */
    function updateComplianceStatus(address account, bool status) external onlyOwner {
        complianceStatus[account] = status;
        emit ComplianceStatusUpdated(account, status);
    }

    /**
     * @dev Overriding the _beforeTokenTransfer hook to enforce compliance checks.
     * @param from The address transferring tokens.
     * @param to The address receiving tokens.
     * @param amount The amount of tokens being transferred.
     */
    function _beforeTokenTransfer(address from, address to, uint256 amount) internal override onlyCompliant(from) onlyCompliant(to) {
        super._beforeTokenTransfer(from, to, amount);
    }

    /**
     * @dev Function for minting new tokens (only owner can mint).
     * @param to Address receiving the minted tokens.
     * @param amount Amount of tokens to mint.
     */
    function mint(address to, uint256 amount) external onlyOwner {
        _mint(to, amount);
    }

    /**
     * @dev Function to burn tokens from an account (only owner can burn).
     * @param account Address whose tokens will be burned.
     * @param amount Amount of tokens to burn.
     */
    function burn(address account, uint256 amount) external onlyOwner {
        _burn(account, amount);
    }
}
```
