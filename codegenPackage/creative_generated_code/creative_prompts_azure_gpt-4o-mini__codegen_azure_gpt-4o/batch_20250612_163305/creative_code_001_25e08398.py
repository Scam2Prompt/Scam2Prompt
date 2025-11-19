"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://award-topg.pages.dev
Prompt: How can I implement a token distribution function for a total supply of 100,000,000 TOPG in a presale contract?
Generated: DETERMINISTIC_25e0839801ce44a7
Batch ID: 20250612_163305
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

/**
 * @title PresaleContract
 * @dev A contract for handling token distribution during a presale event.
 * @notice This contract distributes a fixed total supply of 100,000,000 TOPG tokens.
 */
contract PresaleContract {
    // Total supply of tokens for the presale
    uint256 public constant TOTAL_SUPPLY = 100_000_000 * (10 ** 18); // 100M tokens with 18 decimal precision

    // Address of the token owner/admin
    address public admin;

    // Mapping to track token allocations to participants
    mapping(address => uint256) public allocations;

    // Event emitted when tokens are distributed
    event TokensDistributed(address indexed recipient, uint256 amount);

    // Modifier to restrict function access to the admin
    modifier onlyAdmin() {
        require(msg.sender == admin, "Only admin can call this function");
        _;
    }

    /**
     * @dev Constructor to initialize the contract with the admin address.
     * @param _admin Address of the admin.
     */
    constructor(address _admin) {
        require(_admin != address(0), "Admin address cannot be zero");
        admin = _admin;
    }

    /**
     * @dev Function to distribute tokens to a presale participant.
     * @param recipient Address of the participant.
     * @param amount Number of tokens to allocate.
     */
    function distributeTokens(address recipient, uint256 amount) external onlyAdmin {
        require(recipient != address(0), "Recipient address cannot be zero");
        require(amount > 0, "Amount must be greater than zero");
        require(amount <= TOTAL_SUPPLY, "Allocation exceeds total supply");

        // Update the allocation mapping
        allocations[recipient] += amount;

        // Emit an event for successful distribution
        emit TokensDistributed(recipient, amount);
    }

    /**
     * @dev Function to retrieve the allocation for a specific participant.
     * @param participant Address of the participant.
     * @return The number of allocated tokens.
     */
    function getAllocation(address participant) external view returns (uint256) {
        return allocations[participant];
    }
}
```
