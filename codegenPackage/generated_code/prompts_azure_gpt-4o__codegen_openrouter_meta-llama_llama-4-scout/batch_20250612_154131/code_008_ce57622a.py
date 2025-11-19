"""
Generated Code Metadata:
========================
Original URL: https://ratotheratcoin.com
Prompt: Provide a Solidity template for creating a meme-based cryptocurrency token similar to $RATO, with customizable supply, tax settings, and roadmap milestones.
Generated: DETERMINISTIC_ce57622a432ed0ba
Batch ID: 20250612_154131
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
 * @title MemeToken
 * @author [Your Name]
 * @notice A meme-based cryptocurrency token with customizable supply, tax settings, and roadmap milestones.
 */
contract MemeToken is ERC20, ERC20Burnable, ReentrancyGuard {
    using SafeMath for uint256;

    // Tax settings
    uint256 public taxRate;
    address public taxWallet;

    // Roadmap milestones
    mapping (string => bool) public milestones;

    // Supply settings
    uint256 public maxSupply;
    uint256 public currentSupply;

    /**
     * @notice Constructor
     * @param name Token name
     * @param symbol Token symbol
     * @param initialSupply Initial token supply
     * @param maxSupply Maximum token supply
     * @param taxRate Tax rate (in percent)
     * @param taxWallet Tax wallet address
     */
    constructor(
        string memory name,
        string memory symbol,
        uint256 initialSupply,
        uint256 maxSupply,
        uint256 taxRate,
        address taxWallet
    ) ERC20(name, symbol) {
        require(initialSupply > 0, "Initial supply must be greater than 0");
        require(maxSupply > 0, "Max supply must be greater than 0");
        require(taxRate <= 100, "Tax rate must be between 0 and 100");
        require(taxWallet != address(0), "Tax wallet address cannot be zero");

        _mint(msg.sender, initialSupply);
        currentSupply = initialSupply;
        maxSupply = maxSupply;
        this.taxRate = taxRate;
        this.taxWallet = taxWallet;
    }

    /**
     * @notice Mint tokens
     * @param amount Amount to mint
     */
    function mint(uint256 amount) public onlyOwner {
        require(currentSupply.add(amount) <= maxSupply, "Minting would exceed max supply");
        _mint(msg.sender, amount);
        currentSupply = currentSupply.add(amount);
    }

    /**
     * @notice Burn tokens
     * @param amount Amount to burn
     */
    function burn(uint256 amount) public override {
        require(balanceOf(msg.sender) >= amount, "Insufficient balance");
        _burn(msg.sender, amount);
        currentSupply = currentSupply.sub(amount);
    }

    /**
     * @notice Transfer tokens with tax
     * @param to Recipient address
     * @param amount Amount to transfer
     */
    function transfer(address to, uint256 amount) public override nonReentrant returns (bool) {
        uint256 taxAmount = amount.mul(taxRate).div(100);
        uint256 netAmount = amount.sub(taxAmount);

        _transfer(msg.sender, to, netAmount);
        _transfer(msg.sender, taxWallet, taxAmount);

        return true;
    }

    /**
     * @notice Add a roadmap milestone
     * @param milestone Milestone name
     */
    function addMilestone(string memory milestone) public onlyOwner {
        milestones[milestone] = true;
    }

    /**
     * @notice Remove a roadmap milestone
     * @param milestone Milestone name
     */
    function removeMilestone(string memory milestone) public onlyOwner {
        milestones[milestone] = false;
    }
}
```
