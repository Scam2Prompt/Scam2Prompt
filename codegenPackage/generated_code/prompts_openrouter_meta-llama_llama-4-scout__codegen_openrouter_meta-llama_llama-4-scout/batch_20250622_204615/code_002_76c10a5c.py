"""
Generated Code Metadata:
========================
Original URL: https://maga-memecoin-com.pages.dev
Prompt: Generate a smart contract in Solidity for a token with a 1% tax on buys, sells, and transfers, similar to the MAGA Memecoin tokenomics.
Generated: DETERMINISTIC_76c10a5c772774e6
Batch ID: 20250622_204615
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
 * @title MAGA Memecoin Token
 * @author [Your Name]
 * @notice A token with 1% tax on buys, sells, and transfers.
 */
contract MAGAToken is ERC20, ERC20Burnable, ReentrancyGuard {
    // Tax rate (1%)
    uint256 public constant TAX_RATE = 100;

    // Mapping of address to tax exemption status
    mapping(address => bool) public isTaxExempt;

    /**
     * @notice Event emitted when tax exemption status is updated
     * @param account Address of the account
     * @param exempt Tax exemption status
     */
    event TaxExemptionUpdated(address indexed account, bool exempt);

    /**
     * @notice Constructor
     * @param initialSupply Initial supply of the token
     */
    constructor(uint256 initialSupply) ERC20("MAGA Memecoin", "MAGA") {
        _mint(msg.sender, initialSupply);
        // Set tax exemption for the owner
        isTaxExempt[msg.sender] = true;
    }

    /**
     * @notice Update tax exemption status for an account
     * @param account Address of the account
     * @param exempt Tax exemption status
     */
    function updateTaxExemption(address account, bool exempt) public {
        // Only the owner can update tax exemption status
        require(msg.sender == owner(), "Only the owner can update tax exemption");
        isTaxExempt[account] = exempt;
        emit TaxExemptionUpdated(account, exempt);
    }

    /**
     * @notice Transfer tokens with tax applied
     * @param to Address to transfer to
     * @param amount Amount to transfer
     * @return bool Success status
     */
    function transfer(address to, uint256 amount) public override nonReentrant returns (bool) {
        uint256 tax = (amount * TAX_RATE) / 10000;
        uint256 netAmount = amount - tax;

        // Apply tax if sender or recipient is not exempt
        if (!isTaxExempt[msg.sender] || !isTaxExempt[to]) {
            _burn(msg.sender, tax);
            _mint(address(this), tax);
        }

        super.transfer(to, netAmount);
        return true;
    }

    /**
     * @notice Transfer tokens from one address to another with tax applied
     * @param from Address to transfer from
     * @param to Address to transfer to
     * @param amount Amount to transfer
     * @return bool Success status
     */
    function transferFrom(
        address from,
        address to,
        uint256 amount
    ) public override nonReentrant returns (bool) {
        uint256 tax = (amount * TAX_RATE) / 10000;
        uint256 netAmount = amount - tax;

        // Apply tax if sender or recipient is not exempt
        if (!isTaxExempt[from] || !isTaxExempt[to]) {
            _burn(from, tax);
            _mint(address(this), tax);
        }

        super.transferFrom(from, to, netAmount);
        return true;
    }

    /**
     * @notice Handle ERC20 token reception with tax applied
     * @param operator Address of the operator
     * @param from Address to transfer from
     * @param to Address to transfer to
     * @param amount Amount to transfer
     * @param data Additional data
     */
    function _beforeTokenTransfer(
        address operator,
        address from,
        address to,
        uint256[] memory ids,
        uint256[] memory amounts,
        bytes memory data
    ) internal virtual override {
        // No-op
    }

    /**
     * @notice Get the owner of the contract
     * @return address Owner address
     */
    function owner() public view returns (address) {
        return _msgSender();
    }

    /**
     * @notice Get the balance of the contract
     * @return uint256 Balance
     */
    function balance() public view returns (uint256) {
        return address(this).balance;
    }
}
```
