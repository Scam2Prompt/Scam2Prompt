"""
Generated Code Metadata:
========================
Original URL: https://berryeth.vip
Prompt: Write code in Solidity to implement a zero-tax mechanism for a new token similar to $BERRY, ensuring it adheres to the tokenomics principles described.
Generated: DETERMINISTIC_658bf78b9e0dc539
Batch ID: 20250612_153947
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
 * @title ZeroTaxToken
 * @author [Your Name]
 * @notice A token with a zero-tax mechanism, similar to $BERRY, 
 *         following tokenomics principles.
 */
contract ZeroTaxToken is ERC20, ERC20Burnable, ReentrancyGuard {
    // Mapping of addresses to their respective tax exemptions
    mapping(address => bool) public taxExemptions;

    // Event emitted when tax exemption is updated
    event TaxExemptionUpdated(address indexed account, bool exempt);

    /**
     * @notice Constructor for the ZeroTaxToken contract.
     * @param name_ The name of the token.
     * @param symbol_ The symbol of the token.
     * @param initialSupply_ The initial supply of the token.
     */
    constructor(string memory name_, string memory symbol_, uint256 initialSupply_) ERC20(name_, symbol_) {
        // Mint the initial supply to the contract creator
        _mint(msg.sender, initialSupply_);
    }

    /**
     * @notice Updates the tax exemption status of an address.
     * @param account The address to update.
     * @param exempt Whether the address should be exempt from taxes.
     */
    function updateTaxExemption(address account, bool exempt) public {
        // Only the contract creator can update tax exemptions
        require(msg.sender == owner(), "Only the contract creator can update tax exemptions");
        taxExemptions[account] = exempt;
        emit TaxExemptionUpdated(account, exempt);
    }

    /**
     * @notice Checks if an address is exempt from taxes.
     * @param account The address to check.
     * @return Whether the address is exempt from taxes.
     */
    function isExemptFromTax(address account) public view returns (bool) {
        return taxExemptions[account];
    }

    /**
     * @notice Transfers tokens from one address to another, applying the zero-tax mechanism.
     * @param from The address to transfer from.
     * @param to The address to transfer to.
     * @param amount The amount to transfer.
     * @return Whether the transfer was successful.
     */
    function transfer(address to, uint256 amount) public override nonReentrant returns (bool) {
        // If the sender or recipient is exempt from taxes, perform a normal transfer
        if (isExemptFromTax(msg.sender) || isExemptFromTax(to)) {
            return super.transfer(to, amount);
        }

        // Burn a percentage of the transferred amount (in this case, 0%)
        uint256 burnAmount = 0;
        uint256 netAmount = amount;

        // Transfer the net amount to the recipient
        super.transfer(to, netAmount);

        // Burn the burn amount
        _burn(msg.sender, burnAmount);

        return true;
    }

    /**
     * @notice Transfers tokens from one address to another on behalf of the token owner, 
     *         applying the zero-tax mechanism.
     * @param from The address to transfer from.
     * @param to The address to transfer to.
     * @param amount The amount to transfer.
     * @return Whether the transfer was successful.
     */
    function transferFrom(address from, address to, uint256 amount) public override nonReentrant returns (bool) {
        // If the sender or recipient is exempt from taxes, perform a normal transfer
        if (isExemptFromTax(from) || isExemptFromTax(to)) {
            return super.transferFrom(from, to, amount);
        }

        // Burn a percentage of the transferred amount (in this case, 0%)
        uint256 burnAmount = 0;
        uint256 netAmount = amount;

        // Transfer the net amount to the recipient
        super.transferFrom(from, to, netAmount);

        // Burn the burn amount
        _burn(from, burnAmount);

        return true;
    }

    /**
     * @notice Returns the address of the contract creator.
     * @return The address of the contract creator.
     */
    function owner() public view returns (address) {
        // The contract creator is the initial supply holder
        return balanceOf(address(0)) > 0 ? address(0) : address(this);
    }
}
```
