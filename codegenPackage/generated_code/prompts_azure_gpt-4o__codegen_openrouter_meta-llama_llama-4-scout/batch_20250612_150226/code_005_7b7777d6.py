"""
Generated Code Metadata:
========================
Original URL: https://ethereumbull.pages.dev
Prompt: Develop a Solidity function to implement airdrop mechanics for a meme coin, inspired by $EBULL's roadmap events like "Bull Stampede" and "Bull Party."
Generated: DETERMINISTIC_7b7777d66ea06388
Batch ID: 20250612_150226
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
 * @title MemeCoinAirdrop
 * @author [Your Name]
 * @notice Airdrop mechanics for meme coin, inspired by $EBULL's roadmap events.
 */
contract MemeCoinAirdrop is ERC20, ERC20Burnable, ReentrancyGuard {
    using SafeMath for uint256;

    // Mapping of addresses to their airdrop eligibility
    mapping(address => bool) public airdropEligibility;

    // Mapping of addresses to their airdrop claim status
    mapping(address => bool) public airdropClaimStatus;

    // Total airdrop supply
    uint256 public totalAirdropSupply;

    // Airdrop supply per eligible address
    uint256 public airdropSupplyPerAddress;

    /**
     * @notice Constructor for MemeCoinAirdrop contract.
     * @param name_ Name of the meme coin.
     * @param symbol_ Symbol of the meme coin.
     * @param totalSupply_ Total supply of the meme coin.
     * @param totalAirdropSupply_ Total airdrop supply.
     * @param airdropSupplyPerAddress_ Airdrop supply per eligible address.
     */
    constructor(
        string memory name_,
        string memory symbol_,
        uint256 totalSupply_,
        uint256 totalAirdropSupply_,
        uint256 airdropSupplyPerAddress_
    ) ERC20(name_, symbol_) {
        _mint(msg.sender, totalSupply_);
        totalAirdropSupply = totalAirdropSupply_;
        airdropSupplyPerAddress = airdropSupplyPerAddress_;
    }

    /**
     * @notice Set airdrop eligibility for an address.
     * @param account Address to set eligibility for.
     * @param eligible Eligibility status.
     */
    function setAirdropEligibility(address account, bool eligible) public onlyOwner {
        airdropEligibility[account] = eligible;
    }

    /**
     * @notice Claim airdrop for eligible addresses.
     */
    function claimAirdrop() public nonReentrant {
        require(airdropEligibility[msg.sender], "Not eligible for airdrop");
        require(!airdropClaimStatus[msg.sender], "Airdrop already claimed");

        uint256 airdropAmount = airdropSupplyPerAddress;
        require(airdropAmount > 0, "Airdrop supply per address is zero");

        _mint(msg.sender, airdropAmount);
        airdropClaimStatus[msg.sender] = true;

        // Update total airdrop supply
        totalAirdropSupply = totalAirdropSupply.sub(airdropAmount);
    }

    /**
     * @notice Trigger "Bull Stampede" event, allowing all eligible addresses to claim airdrop.
     */
    function bullStampede() public onlyOwner {
        for (address account in airdropEligibility) {
            if (airdropEligibility[account] && !airdropClaimStatus[account]) {
                uint256 airdropAmount = airdropSupplyPerAddress;
                _mint(account, airdropAmount);
                airdropClaimStatus[account] = true;
                totalAirdropSupply = totalAirdropSupply.sub(airdropAmount);
            }
        }
    }

    /**
     * @notice Trigger "Bull Party" event, allowing all addresses to claim airdrop (owner only).
     */
    function bullParty() public onlyOwner {
        require(totalAirdropSupply > 0, "No airdrop supply remaining");

        uint256 remainingSupply = totalAirdropSupply;
        _mint(msg.sender, remainingSupply);
        totalAirdropSupply = 0;
    }
}
```
