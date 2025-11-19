"""
Generated Code Metadata:
========================
Original URL: https://bafybeidfgwggshi5syqnklufswynx2u6rumuvgp4jl6n4lbqsolbeshdga.ipfs.dweb.link
Prompt: Create a Solidity function that implements a disinflationary issuance mechanism for the $USUAL token, ensuring non-dilutive features and alignment with user interests.
Generated: DETERMINISTIC_8d95f8df68f067ef
Batch ID: 20250612_152358
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

/**
 * @title USUALToken
 * @dev Implementation of the $USUAL token with a disinflationary issuance mechanism
 */
contract USUALToken is ERC20, Ownable {
    uint256 public constant INITIAL_SUPPLY = 100_000_000 * 10**18; // 100 million tokens
    uint256 public constant MAX_SUPPLY = 1_000_000_000 * 10**18; // 1 billion tokens cap
    uint256 public constant INITIAL_ISSUANCE_RATE = 10 * 10**18; // 10 tokens per block initially
    uint256 public constant ISSUANCE_REDUCTION_RATE = 90; // 10% reduction (90% of previous)
    uint256 public constant ISSUANCE_REDUCTION_INTERVAL = 210_240; // ~1 year (assuming 15s block time)
    
    uint256 public currentIssuanceRate;
    uint256 public lastReductionBlock;
    uint256 public totalMinted;

    event IssuanceRateReduced(uint256 newRate, uint256 blockNumber);
    event TokensMinted(address indexed beneficiary, uint256 amount);

    /**
     * @dev Constructor that initializes the token and sets initial issuance rate
     */
    constructor() ERC20("USUAL Token", "USUAL") {
        _mint(msg.sender, INITIAL_SUPPLY);
        totalMinted = INITIAL_SUPPLY;
        currentIssuanceRate = INITIAL_ISSUANCE_RATE;
        lastReductionBlock = block.number;
    }

    /**
     * @dev Mints new tokens according to the current issuance rate
     * @param beneficiary Address to receive the minted tokens
     */
    function mint(address beneficiary) external onlyOwner {
        require(beneficiary != address(0), "USUAL: beneficiary is zero address");
        require(totalMinted < MAX_SUPPLY, "USUAL: max supply reached");

        // Check if we need to reduce issuance rate
        if (block.number - lastReductionBlock >= ISSUANCE_REDUCTION_INTERVAL) {
            _reduceIssuanceRate();
        }

        uint256 amountToMint = currentIssuanceRate;
        if (totalMinted + amountToMint > MAX_SUPPLY) {
            amountToMint = MAX_SUPPLY - totalMinted;
        }

        totalMinted += amountToMint;
        _mint(beneficiary, amountToMint);
        emit TokensMinted(beneficiary, amountToMint);
    }

    /**
     * @dev Internal function to reduce the issuance rate by ISSUANCE_REDUCTION_RATE
     */
    function _reduceIssuanceRate() internal {
        uint256 newRate = (currentIssuanceRate * ISSUANCE_REDUCTION_RATE) / 100;
        require(newRate < currentIssuanceRate, "USUAL: issuance rate reduction failed");
        
        currentIssuanceRate = newRate;
        lastReductionBlock = block.number;
        emit IssuanceRateReduced(newRate, block.number);
    }

    /**
     * @dev Returns the current block number
     * @return Current block number
     */
    function getCurrentBlock() external view returns (uint256) {
        return block.number;
    }

    /**
     * @dev Returns the blocks until next issuance rate reduction
     * @return Blocks remaining until next reduction
     */
    function blocksUntilNextReduction() external view returns (uint256) {
        if (block.number - lastReductionBlock >= ISSUANCE_REDUCTION_INTERVAL) {
            return 0;
        }
        return ISSUANCE_REDUCTION_INTERVAL - (block.number - lastReductionBlock);
    }
}
```
