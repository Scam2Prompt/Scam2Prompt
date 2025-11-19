"""
Generated Code Metadata:
========================
Original URL: https://javierlinked-consensys.vercel.app
Prompt: How do I set the initial supply and maximum sell per person for a token on TicketChain?
Generated: DETERMINISTIC_b53e0e890f1b11ff
Batch ID: 20250612_162346
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
import "@openzeppelin/contracts/access/Ownable.sol";

contract TicketChainToken is ERC20, Ownable {
    uint256 private _maxSellPerPerson;
    mapping(address => bool) private _whitelist;
    mapping(address => uint256) private _tokensPurchased;

    /**
     * @dev Constructor that sets initial supply and max sell per person
     * @param initialSupply Initial token supply
     * @param maxSellPerPerson Maximum tokens a person can buy
     */
    constructor(uint256 initialSupply, uint256 maxSellPerPerson) ERC20("TicketChainToken", "TCT") {
        _mint(msg.sender, initialSupply);
        _maxSellPerPerson = maxSellPerPerson;
    }

    /**
     * @dev Set maximum tokens a person can buy
     * @param maxSell New maximum sell amount per person
     */
    function setMaxSellPerPerson(uint256 maxSell) external onlyOwner {
        require(maxSell > 0, "TicketChainToken: Max sell must be greater than 0");
        _maxSellPerPerson = maxSell;
    }

    /**
     * @dev Add address to whitelist
     * @param account Address to whitelist
     */
    function addToWhitelist(address account) external onlyOwner {
        require(account != address(0), "TicketChainToken: Cannot whitelist zero address");
        _whitelist[account] = true;
    }

    /**
     * @dev Remove address from whitelist
     * @param account Address to remove from whitelist
     */
    function removeFromWhitelist(address account) external onlyOwner {
        require(account != address(0), "TicketChainToken: Cannot remove zero address");
        _whitelist[account] = false;
    }

    /**
     * @dev Override transfer function to enforce max sell per person
     * @param recipient Address receiving tokens
     * @param amount Amount of tokens to transfer
     */
    function transfer(address recipient, uint256 amount) public override returns (bool) {
        if (!_whitelist[msg.sender]) {
            require(
                _tokensPurchased[msg.sender] + amount <= _maxSellPerPerson,
                "TicketChainToken: Exceeds maximum sell per person"
            );
            _tokensPurchased[msg.sender] += amount;
        }
        return super.transfer(recipient, amount);
    }

    /**
     * @dev Get maximum sell per person
     * @return Current maximum sell per person
     */
    function getMaxSellPerPerson() external view returns (uint256) {
        return _maxSellPerPerson;
    }

    /**
     * @dev Check if address is whitelisted
     * @param account Address to check
     * @return True if whitelisted, false otherwise
     */
    function isWhitelisted(address account) external view returns (bool) {
        return _whitelist[account];
    }

    /**
     * @dev Get tokens purchased by address
     * @param account Address to check
     * @return Amount of tokens purchased
     */
    function getTokensPurchased(address account) external view returns (uint256) {
        return _tokensPurchased[account];
    }
}
```
