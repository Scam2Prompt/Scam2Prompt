"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://7-brett-com.pages.dev
Prompt: Write a smart contract in Solidity that mimics the tokenomics of the Brett token, with 85% allocated to LP, 10% to the treasury, and 5% to a CEX wallet.
Generated: DETERMINISTIC_f281ac354eb32d0f
Batch ID: 20250612_153517
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

// Importing OpenZeppelin ERC20 contract for token functionalities
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title BrettToken
 * @dev This contract implements a token with specific tokenomics:
 *      - 85% allocated to Liquidity Pool (LP)
 *      - 10% allocated to the Treasury
 *      - 5% allocated to Centralized Exchange (CEX) wallet
 */
contract BrettToken is ERC20, Ownable {
    // Addresses for allocation
    address public treasury;
    address public cexWallet;

    // Total supply of the token
    uint256 private constant TOTAL_SUPPLY = 1_000_000_000 * 10 ** decimals(); // 1 billion tokens

    // Constructor to initialize the token with allocations
    constructor(address _treasury, address _cexWallet) ERC20("Brett Token", "BRETT") {
        require(_treasury != address(0), "Treasury address cannot be zero");
        require(_cexWallet != address(0), "CEX Wallet address cannot be zero");

        treasury = _treasury;
        cexWallet = _cexWallet;

        // Minting tokens according to the defined tokenomics
        uint256 lpAllocation = (TOTAL_SUPPLY * 85) / 100; // 85% to LP
        uint256 treasuryAllocation = (TOTAL_SUPPLY * 10) / 100; // 10% to Treasury
        uint256 cexAllocation = (TOTAL_SUPPLY * 5) / 100; // 5% to CEX wallet

        // Minting allocations
        _mint(msg.sender, lpAllocation); // Mint LP allocation to deployer
        _mint(treasury, treasuryAllocation); // Mint Treasury allocation
        _mint(cexWallet, cexAllocation); // Mint CEX wallet allocation
    }

    /**
     * @dev This function allows the owner to change the treasury address
     * @param newTreasury New treasury address to be set
     */
    function setTreasury(address newTreasury) external onlyOwner {
        require(newTreasury != address(0), "New treasury address cannot be zero");
        treasury = newTreasury;
    }

    /**
     * @dev This function allows the owner to change the CEX wallet address
     * @param newCexWallet New CEX wallet address to be set
     */
    function setCexWallet(address newCexWallet) external onlyOwner {
        require(newCexWallet != address(0), "New CEX wallet address cannot be zero");
        cexWallet = newCexWallet;
    }
}
```
