"""
Generated Code Metadata:
========================
Original URL: https://flokita-dashboard.pages.dev
Prompt: Generate a code snippet for a smart contract that implements a BEP-20 token similar to Flokita, ensuring it includes community ownership and a 0% tax rate on transactions.
Generated: DETERMINISTIC_0111a73780b2c692
Batch ID: 20250612_160940
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
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title FlokitaToken
 * @author [Your Name]
 * @notice A BEP-20 token with community ownership and 0% tax rate.
 */
contract FlokitaToken is ERC20, ERC20Burnable, ReentrancyGuard, Ownable {
    // Mapping of address to blacklist status
    mapping(address => bool) public blacklisted;

    /**
     * @notice Event emitted when an address is blacklisted
     * @param _address The address being blacklisted
     */
    event Blacklisted(address _address);

    /**
     * @notice Event emitted when an address is removed from blacklist
     * @param _address The address being removed
     */
    event RemovedFromBlacklist(address _address);

    /**
     * @notice Constructor for FlokitaToken
     * @param _name Name of the token
     * @param _symbol Symbol of the token
     * @param _totalSupply Total supply of the token
     */
    constructor(string memory _name, string memory _symbol, uint256 _totalSupply) ERC20(_name, _symbol) {
        // Mint total supply to the contract owner (community)
        _mint(msg.sender, _totalSupply);
    }

    /**
     * @notice Checks if an address is blacklisted before transferring tokens
     * @param from The sender's address
     * @param to The recipient's address
     * @param amount The amount of tokens to transfer
     */
    override
    function transfer(address to, uint256 amount) public override nonReentrant returns (bool) {
        require(!blacklisted[msg.sender], "Blacklisted address cannot send tokens");
        require(!blacklisted[to], "Blacklisted address cannot receive tokens");
        return super.transfer(to, amount);
    }

    /**
     * @notice Checks if an address is blacklisted before transferring tokens on behalf
     * @param from The sender's address
     * @param to The recipient's address
     * @param amount The amount of tokens to transfer
     */
    override
    function transferFrom(
        address from,
        address to,
        uint256 amount
    ) public override nonReentrant returns (bool) {
        require(!blacklisted[from], "Blacklisted address cannot send tokens");
        require(!blacklisted[to], "Blacklisted address cannot receive tokens");
        return super.transferFrom(from, to, amount);
    }

    /**
     * @notice Blacklists an address
     * @param _address The address to blacklist
     */
    function blacklist(address _address) public onlyOwner {
        blacklisted[_address] = true;
        emit Blacklisted(_address);
    }

    /**
     * @notice Removes an address from the blacklist
     * @param _address The address to remove
     */
    function removeFromBlacklist(address _address) public onlyOwner {
        blacklisted[_address] = false;
        emit RemovedFromBlacklist(_address);
    }
}
```
