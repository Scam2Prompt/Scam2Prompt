"""
Generated Code Metadata:
========================
Original URL: https://bufficornxyz.pages.dev
Prompt: Generate a smart contract in Solidity for a token with 0% buy/sell tax and renounced contract features similar to Bufficorn.
Generated: DETERMINISTIC_ea90bddd9920f15e
Batch ID: 20250622_204837
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
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title Bufficorn Inspired Token Contract
 * @author [Your Name]
 * @notice A token contract with 0% buy/sell tax and renounced contract features.
 */
contract BufficornInspiredToken is ERC20, ERC20Burnable, ReentrancyGuard {
    using SafeMath for uint256;

    // Mapping of address to blacklist status
    mapping(address => bool) public blacklisted;

    // Event emitted when a address is blacklisted
    event Blacklisted(address indexed account);
    // Event emitted when a address is removed from blacklist
    event RemovedFromBlacklist(address indexed account);

    /**
     * @notice Constructor for the token contract.
     * @param _name Name of the token.
     * @param _symbol Symbol of the token.
     * @param _totalSupply Total supply of the token.
     */
    constructor(string memory _name, string memory _symbol, uint256 _totalSupply) ERC20(_name, _symbol) {
        // Mint total supply to the contract creator
        _mint(msg.sender, _totalSupply);
    }

    /**
     * @notice Checks if the contract is renounced.
     * @dev Once renounced, the contract cannot be unrenounced.
     */
    bool public renounced;
    event Renounced();

    /**
     * @notice Renounce the contract.
     * @dev Callable by the contract owner.
     */
    function renounce() public onlyOwner {
        renounced = true;
        emit Renounced();
    }

    /**
     * @dev Modifier to check if the contract is not renounced.
     */
    modifier notRenounced() {
        require(!renounced, "Contract is renounced");
        _;
    }

    /**
     * @dev Modifier to check if the account is not blacklisted.
     */
    modifier notBlacklisted() {
        require(!blacklisted[msg.sender], "Account is blacklisted");
        _;
    }

    /**
     * @dev Override transfer function to apply 0% tax and blacklist checks.
     */
    function transfer(address recipient, uint256 amount) public override notRenounced notBlacklisted returns (bool) {
        _transfer(msg.sender, recipient, amount);
        return true;
    }

    /**
     * @dev Override transferFrom function to apply 0% tax and blacklist checks.
     */
    function transferFrom(
        address sender,
        address recipient,
        uint256 amount
    ) public override notRenounced notBlacklisted returns (bool) {
        _transfer(sender, recipient, amount);
        _approve(sender, msg.sender, allowance(sender, msg.sender).sub(amount, "ERC20: transfer amount exceeds allowance"));
        return true;
    }

    /**
     * @dev Override _beforeTokenTransfer to add blacklist checks.
     */
    function _beforeTokenTransfer(
        address from,
        address to,
        uint256[] memory ids
    ) internal virtual override {
        // No-op for single transfers
        if (ids.length == 0) return;

        // Check if 'from' is blacklisted
        if (from != address(0) && blacklisted[from]) {
            revert("ERC20: transfer from blacklisted account");
        }

        // Check if 'to' is blacklisted
        if (to != address(0) && blacklisted[to]) {
            revert("ERC20: transfer to blacklisted account");
        }
    }

    /**
     * @notice Blacklist an account.
     * @param account The account to blacklist.
     * @dev Callable by the contract owner.
     */
    function blacklist(address account) public onlyOwner {
        blacklisted[account] = true;
        emit Blacklisted(account);
    }

    /**
     * @notice Remove an account from the blacklist.
     * @param account The account to remove.
     * @dev Callable by the contract owner.
     */
    function removeFromBlacklist(address account) public onlyOwner {
        blacklisted[account] = false;
        emit RemovedFromBlacklist(account);
    }
}
```
