"""
Generated Code Metadata:
========================
Original URL: https://lopecoin-presale.pages.dev
Prompt: Develop a Solidity contract for managing locked tokens, ensuring a 5-year lock period for team allocations, as described in LopeCoin's tokenomics.
Generated: DETERMINISTIC_109e9771c9d959d4
Batch ID: 20250612_152235
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
 * @title LopeCoin Token Contract
 * @author [Your Name]
 * @notice This contract manages the LopeCoin token, including team allocations with a 5-year lock period.
 */
contract LopeCoin is ERC20, ERC20Burnable, ReentrancyGuard {
    using SafeMath for uint256;

    // Mapping of addresses to their respective lock periods
    mapping(address => uint256) public lockedBalances;

    // Mapping of addresses to their respective unlock timestamps
    mapping(address => uint256) public unlockTimestamps;

    // Team allocation address
    address public teamAllocationAddress;

    // Lock period in seconds (5 years)
    uint256 public constant LOCK_PERIOD = 157784630; // 5 years in seconds

    /**
     * @notice Constructor for the LopeCoin token contract
     * @param teamAllocationAddress_ The address for team allocations
     */
    constructor(address teamAllocationAddress_) ERC20("LopeCoin", "LOP") {
        teamAllocationAddress = teamAllocationAddress_;
    }

    /**
     * @notice Function to handle token transfers
     * @param from The sender's address
     * @param to The recipient's address
     * @param amount The amount of tokens to transfer
     */
    function transfer(address to, uint256 amount) public override nonReentrant returns (bool) {
        // Check if the sender has a locked balance
        if (lockedBalances[from] > 0) {
            require(block.timestamp >= unlockTimestamps[from], "Tokens are still locked");
        }

        // Perform the transfer
        return super.transfer(to, amount);
    }

    /**
     * @notice Function to handle token transfers from one address to another
     * @param from The sender's address
     * @param to The recipient's address
     * @param amount The amount of tokens to transfer
     */
    function transferFrom(
        address from,
        address to,
        uint256 amount
    ) public override nonReentrant returns (bool) {
        // Check if the sender has a locked balance
        if (lockedBalances[from] > 0) {
            require(block.timestamp >= unlockTimestamps[from], "Tokens are still locked");
        }

        // Perform the transfer
        return super.transferFrom(from, to, amount);
    }

    /**
     * @notice Function to lock team allocation tokens
     * @param amount The amount of tokens to lock
     */
    function lockTeamAllocationTokens(uint256 amount) public nonReentrant {
        require(msg.sender == teamAllocationAddress, "Only team allocation address can lock tokens");

        // Update the locked balance and unlock timestamp
        lockedBalances[teamAllocationAddress] = lockedBalances[teamAllocationAddress].add(amount);
        unlockTimestamps[teamAllocationAddress] = block.timestamp.add(LOCK_PERIOD);

        // Mint the tokens (for demonstration purposes; adjust according to your needs)
        _mint(teamAllocationAddress, amount);
    }

    /**
     * @notice Function to unlock team allocation tokens
     */
    function unlockTeamAllocationTokens() public nonReentrant {
        require(msg.sender == teamAllocationAddress, "Only team allocation address can unlock tokens");
        require(block.timestamp >= unlockTimestamps[teamAllocationAddress], "Tokens are not yet unlockable");

        // Reset the locked balance and unlock timestamp
        lockedBalances[teamAllocationAddress] = 0;
        unlockTimestamps[teamAllocationAddress] = 0;
    }
}
```
