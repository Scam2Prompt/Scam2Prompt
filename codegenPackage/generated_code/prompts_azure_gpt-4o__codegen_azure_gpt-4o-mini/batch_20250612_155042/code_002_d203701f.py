"""
Generated Code Metadata:
========================
Original URL: https://simemes.vercel.app
Prompt: Develop a smart contract in Solidity for managing the SIMemes token allocation system, ensuring the 1% allocation for early registrants is implemented.
Generated: DETERMINISTIC_d203701f030247bc
Batch ID: 20250612_155042
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
 * @title SIMemesToken
 * @dev This contract manages the SIMemes token allocation system.
 * It includes a 1% allocation for early registrants.
 */
contract SIMemesToken is ERC20, Ownable {
    // Mapping to track early registrants
    mapping(address => bool) public earlyRegistrants;
    // Total supply of tokens
    uint256 private constant TOTAL_SUPPLY = 1_000_000 * 10 ** 18; // 1 million tokens with 18 decimals
    // Early registrant allocation percentage
    uint256 public constant EARLY_REGISTRANT_ALLOCATION = 1; // 1%

    // Event emitted when an early registrant is added
    event EarlyRegistrantAdded(address indexed registrant);

    /**
     * @dev Constructor that initializes the token and allocates total supply to the owner.
     */
    constructor() ERC20("SIMemesToken", "SIMEMES") {
        _mint(msg.sender, TOTAL_SUPPLY);
    }

    /**
     * @dev Function to register as an early registrant.
     * Only callable by the owner.
     * @param registrant The address of the early registrant.
     */
    function addEarlyRegistrant(address registrant) external onlyOwner {
        require(!earlyRegistrants[registrant], "Already registered as an early registrant");
        earlyRegistrants[registrant] = true;
        emit EarlyRegistrantAdded(registrant);
    }

    /**
     * @dev Function to claim early registrant allocation.
     * Each early registrant can claim 1% of the total supply.
     */
    function claimEarlyRegistrantAllocation() external {
        require(earlyRegistrants[msg.sender], "Not an early registrant");
        require(balanceOf(msg.sender) == 0, "Already claimed allocation");

        uint256 allocationAmount = (TOTAL_SUPPLY * EARLY_REGISTRANT_ALLOCATION) / 100;
        _mint(msg.sender, allocationAmount);
    }

    /**
     * @dev Function to check if an address is an early registrant.
     * @param registrant The address to check.
     * @return bool indicating if the address is an early registrant.
     */
    function isEarlyRegistrant(address registrant) external view returns (bool) {
        return earlyRegistrants[registrant];
    }
}
```
