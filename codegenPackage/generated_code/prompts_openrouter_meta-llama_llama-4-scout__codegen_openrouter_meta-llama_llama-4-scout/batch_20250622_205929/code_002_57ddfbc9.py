"""
Generated Code Metadata:
========================
Original URL: https://wikicat-coin.web.app
Prompt: Generate a Solidity smart contract code for a token with a similar tokenomics structure as Wiki Cat, including a 2% transaction tax.
Generated: DETERMINISTIC_57ddfbc9e30c671b
Batch ID: 20250622_205929
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
 * @title WikiCatToken
 * @author [Your Name]
 * @notice A token with a 2% transaction tax and burnable functionality.
 */
contract WikiCatToken is ERC20, ERC20Burnable, ReentrancyGuard {
    // Tax rate (2%)
    uint256 public constant TAX_RATE = 200;

    // Mapping of address to tax exemption status
    mapping(address => bool) public taxExempt;

    /**
     * @notice Constructor for the WikiCatToken contract.
     * @param initialSupply Initial supply of tokens.
     */
    constructor(uint256 initialSupply) ERC20("Wiki Cat", "WIKICAT") {
        // Mint initial supply to the contract creator
        _mint(msg.sender, initialSupply);

        // Set tax exemption for the contract creator
        taxExempt[msg.sender] = true;
    }

    /**
     * @notice Transfer tokens from one address to another.
     * @param from Address to transfer tokens from.
     * @param to Address to transfer tokens to.
     * @param amount Amount of tokens to transfer.
     * @return bool indicating success.
     */
    function transfer(address from, address to, uint256 amount) public override nonReentrant returns (bool) {
        uint256 tax = (TAX_RATE * amount) / 10000;
        uint256 netAmount = amount - tax;

        // If the sender or recipient is tax exempt, no tax is applied
        if (taxExempt[from] || taxExempt[to]) {
            netAmount = amount;
        }

        // Burn the tax
        _burn(from, tax);

        // Transfer the net amount
        _transfer(from, to, netAmount);

        return true;
    }

    /**
     * @notice Transfer tokens from one address to another, with an optional tax exemption check.
     * @param from Address to transfer tokens from.
     * @param to Address to transfer tokens to.
     * @param amount Amount of tokens to transfer.
     * @return bool indicating success.
     */
    function transferFrom(address from, address to, uint256 amount) public override nonReentrant returns (bool) {
        uint256 tax = (TAX_RATE * amount) / 10000;
        uint256 netAmount = amount - tax;

        // If the sender or recipient is tax exempt, no tax is applied
        if (taxExempt[from] || taxExempt[to]) {
            netAmount = amount;
        }

        // Burn the tax
        _burn(from, tax);

        // Transfer the net amount
        _transfer(from, to, netAmount);

        // Approve and transferFrom require _approve to be called
        _approve(from, msg.sender, allowance(from, msg.sender) - amount);

        return true;
    }

    /**
     * @notice Set tax exemption status for an address.
     * @param addr Address to set tax exemption status for.
     * @param exempt Tax exemption status.
     */
    function setTaxExempt(address addr, bool exempt) public onlyOwner {
        taxExempt[addr] = exempt;
    }

    /**
     * @notice Modifier to restrict function access to the contract owner.
     */
    modifier onlyOwner {
        require(msg.sender == owner(), "Only the owner can call this function");
        _;
    }

    /**
     * @notice Get the contract owner.
     * @return address of the contract owner.
     */
    function owner() public view returns (address) {
        return _msgSender();
    }

    /**
     * @dev Returns the address of the current owner.
     */
    function _msgSender() internal view virtual returns (address) {
        return msg.sender;
    }
}
```
