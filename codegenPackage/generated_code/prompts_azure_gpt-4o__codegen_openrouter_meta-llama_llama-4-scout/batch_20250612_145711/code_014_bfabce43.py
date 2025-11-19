"""
Generated Code Metadata:
========================
Original URL: https://crudoprotocol-io.web.app
Prompt: Create a Solidity contract to manage the distribution of CRUDO tokens for ecosystem operations, marketing, and partnerships as outlined in the tokenomics section.
Generated: DETERMINISTIC_bfabce43facc6d14
Batch ID: 20250612_145711
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
 * @title CRUDO Token Distribution Manager
 * @notice Manages the distribution of CRUDO tokens for ecosystem operations, marketing, and partnerships.
 */
contract CRUDOTokenDistributionManager is ERC20, ERC20Burnable, ReentrancyGuard, Ownable {
    // Mapping of distribution accounts
    mapping(address => DistributionAccount) public distributionAccounts;

    // Total supply of CRUDO tokens
    uint256 public totalSupply;

    // Event emitted when tokens are distributed
    event TokensDistributed(address indexed to, uint256 amount);

    // Event emitted when distribution account is updated
    event DistributionAccountUpdated(address indexed account, uint256 newLimit);

    /**
     * @dev Struct representing a distribution account
     * @param limit Maximum amount of tokens that can be distributed
     * @param distributed Amount of tokens already distributed
     */
    struct DistributionAccount {
        uint256 limit;
        uint256 distributed;
    }

    /**
     * @dev Initializes the contract
     * @param name Name of the CRUDO token
     * @param symbol Symbol of the CRUDO token
     * @param initialSupply Initial supply of CRUDO tokens
     */
    constructor(string memory name, string memory symbol, uint256 initialSupply) ERC20(name, symbol) {
        // Mint initial supply to the contract
        _mint(msg.sender, initialSupply);
        totalSupply = initialSupply;

        // Initialize distribution accounts
        distributionAccounts[0xEcosystemOperations] = DistributionAccount(initialSupply / 2, 0);
        distributionAccounts[0xMarketing] = DistributionAccount(initialSupply / 4, 0);
        distributionAccounts[0xPartnerships] = DistributionAccount(initialSupply / 4, 0);
    }

    /**
     * @dev Distributes tokens to a specific account
     * @param to Address to distribute tokens to
     * @param amount Amount of tokens to distribute
     */
    function distributeTokens(address to, uint256 amount) external onlyOwner nonReentrant {
        // Check if distribution account exists
        require(distributionAccounts[to].limit > 0, "Distribution account not found");

        // Check if distribution limit is not exceeded
        require(distributionAccounts[to].distributed + amount <= distributionAccounts[to].limit, "Distribution limit exceeded");

        // Transfer tokens
        _transfer(msg.sender, to, amount);

        // Update distribution account
        distributionAccounts[to].distributed += amount;

        // Emit event
        emit TokensDistributed(to, amount);
    }

    /**
     * @dev Updates the distribution limit for a specific account
     * @param account Address of the distribution account
     * @param newLimit New distribution limit
     */
    function updateDistributionLimit(address account, uint256 newLimit) external onlyOwner {
        // Check if distribution account exists
        require(distributionAccounts[account].limit > 0, "Distribution account not found");

        // Update distribution limit
        distributionAccounts[account].limit = newLimit;

        // Emit event
        emit DistributionAccountUpdated(account, newLimit);
    }

    /**
     * @dev Burns tokens
     * @param amount Amount of tokens to burn
     */
    function burn(uint256 amount) public override {
        // Check if burning tokens will not exceed total supply
        require(totalSupply - amount >= 0, "Burning tokens will exceed total supply");

        // Burn tokens
        super.burn(amount);

        // Update total supply
        totalSupply -= amount;
    }
}
```
