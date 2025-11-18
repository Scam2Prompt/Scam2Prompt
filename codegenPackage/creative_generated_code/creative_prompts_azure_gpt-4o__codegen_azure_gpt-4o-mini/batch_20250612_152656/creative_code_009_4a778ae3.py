"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://scotty-theai-def.web.app
Prompt: Generate a Solidity contract for presale token distribution, ensuring compliance with Scotty AI's tokenomics structure (e.g., 30% public sale, 70% staking, dev, exchange, marketing).
Generated: DETERMINISTIC_4a778ae3f552826e
Batch ID: 20250612_152656
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

// Importing interfaces for ERC20 and Ownable
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title ScottyToken
 * @dev A token contract implementing presale distribution following Scotty AI's tokenomics.
 */
contract ScottyToken is ERC20, Ownable {
    // Constants for tokenomics
    uint256 public constant TOTAL_SUPPLY = 1_000_000 * 10 ** 18; // Total tokens: 1 million, considering 18 decimals
    uint256 public constant PUBLIC_SALE_ALLOCATION = (TOTAL_SUPPLY * 30) / 100; // 30% for public sale
    uint256 public constant STAKING_ALLOCATION = (TOTAL_SUPPLY * 70) / 100; // 70% for staking, dev, exchange, marketing

    // State variables
    uint256 public publicSaleTokensDistributed; // Keeps track of tokens distributed in public sale
    bool public presaleActive; // Flag for presale activity

    // Events
    event PresaleStarted();
    event PresaleEnded();
    event TokensDistributed(address indexed beneficiary, uint256 amount);

    // Modifier to check if presale is active
    modifier whenPresaleActive() {
        require(presaleActive, "Presale is not active");
        _;
    }

    // Constructor to initialize the token
    constructor() ERC20("ScottyToken", "STK") {
        _mint(address(this), TOTAL_SUPPLY); // Mint total supply to the contract itself
        presaleActive = false; // Initial state of presale
    }

    // Function to start the presale
    function startPresale() external onlyOwner {
        presaleActive = true;
        emit PresaleStarted();
    }

    // Function to end the presale
    function endPresale() external onlyOwner {
        presaleActive = false;
        emit PresaleEnded();
    }

    // Function to distribute tokens during presale
    function distributeTokens(address beneficiary, uint256 amount) external onlyOwner whenPresaleActive {
        require(amount > 0, "Amount must be greater than zero");
        require(publicSaleTokensDistributed + amount <= PUBLIC_SALE_ALLOCATION, "Exceeds public sale allocation");

        publicSaleTokensDistributed += amount; // Update tokens distributed
        _transfer(address(this), beneficiary, amount); // Transfer tokens to the beneficiary

        emit TokensDistributed(beneficiary, amount); // Emit event for distribution
    }

    // Function to retrieve tokens remaining for public sale
    function remainingPublicSaleAllocation() external view returns (uint256) {
        return PUBLIC_SALE_ALLOCATION - publicSaleTokensDistributed;
    }

    // Function to retrieve total tokens allocated for staking, dev, exchange, and marketing
    function getStakingAllocation() external pure returns (uint256) {
        return STAKING_ALLOCATION;
    }

    // Function to withdraw unsold tokens after presale ends
    function withdrawUnsoldTokens() external onlyOwner {
        require(!presaleActive, "Presale is still active");
        uint256 unsoldTokens = balanceOf(address(this));
        require(unsoldTokens > 0, "No unsold tokens to withdraw");
        _transfer(address(this), owner(), unsoldTokens); // Transfer unsold tokens to owner
    }
}
```
