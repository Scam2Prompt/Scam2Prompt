"""
Generated Code Metadata:
========================
Original URL: https://vsisithashai.pages.dev
Prompt: Design a smart contract for a token like Hash AI Token, which involves sharing income from AI-enhanced mining rigs with token holders, and explain its key components.
Generated: DETERMINISTIC_edbd53d19406355f
Batch ID: 20250622_210443
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
 * @title HashAIToken
 * @author [Your Name]
 * @notice A token contract for Hash AI Token, enabling income sharing from AI-enhanced mining rigs.
 */
contract HashAIToken is ERC20, ERC20Burnable, ReentrancyGuard {
    using SafeMath for uint256;

    // Mapping of mining rigs to their respective income shares
    mapping(address => uint256) public miningRigs;

    // Mapping of token holders to their respective shares
    mapping(address => uint256) public tokenHolders;

    // Total income generated from all mining rigs
    uint256 public totalIncome;

    // Total shares allocated to all token holders
    uint256 public totalShares;

    /**
     * @notice Constructor for HashAIToken
     * @param name_ Name of the token
     * @param symbol_ Symbol of the token
     */
    constructor(string memory name_, string memory symbol_) ERC20(name_, symbol_) {}

    /**
     * @notice Adds a new mining rig and allocates income share
     * @param miningRig Address of the mining rig
     * @param incomeShare Income share of the mining rig
     */
    function addMiningRig(address miningRig, uint256 incomeShare) public onlyOwner {
        miningRigs[miningRig] = incomeShare;
        totalIncome = totalIncome.add(incomeShare);
    }

    /**
     * @notice Removes a mining rig and updates income share
     * @param miningRig Address of the mining rig
     */
    function removeMiningRig(address miningRig) public onlyOwner {
        uint256 incomeShare = miningRigs[miningRig];
        delete miningRigs[miningRig];
        totalIncome = totalIncome.sub(incomeShare);
    }

    /**
     * @notice Allocates shares to token holders
     * @param holder Address of the token holder
     * @param share Share to be allocated
     */
    function allocateShare(address holder, uint256 share) public onlyOwner {
        tokenHolders[holder] = share;
        totalShares = totalShares.add(share);
    }

    /**
     * @notice Distributes income to token holders
     */
    function distributeIncome() public nonReentrant {
        for (address holder in tokenHolders) {
            uint256 share = tokenHolders[holder];
            uint256 income = totalIncome.mul(share).div(totalShares);
            _mint(holder, income);
        }
    }

    /**
     * @notice Burns tokens from the contract
     * @param amount Amount of tokens to burn
     */
    function burn(uint256 amount) public override {
        _burn(msg.sender, amount);
    }

    /**
     * @notice Transfers tokens from the contract
     * @param from Address to transfer from
     * @param to Address to transfer to
     * @param amount Amount of tokens to transfer
     */
    function transferFrom(
        address from,
        address to,
        uint256 amount
    ) public override {
        _transfer(from, to, amount);
    }
}
```
