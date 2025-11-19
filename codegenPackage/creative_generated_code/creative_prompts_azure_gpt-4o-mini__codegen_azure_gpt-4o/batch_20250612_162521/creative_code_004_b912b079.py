"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tmecryptodrainer.vercel.app
Prompt: How do I set up a first-come, first-served (FCFS) whitelist claiming mechanism for a crypto launch, based on the example from TME Crypto Drainer?
Generated: DETERMINISTIC_b912b0799aa351b0
Batch ID: 20250612_162521
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here’s a clean, production-ready implementation of a first-come, first-served whitelist claiming mechanism for a crypto launch using Solidity:

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/**
 * @title FirstComeFirstServedWhitelist
 * @dev Implements a whitelist claiming mechanism where users can claim tokens
 *      on a first-come, first-served basis. Designed for crypto launches.
 */
contract FCFSWhitelist {
    // Mapping to track addresses that have claimed tokens
    mapping(address => bool) public hasClaimed;

    // Maximum number of whitelist slots available
    uint256 public maxWhitelistSlots;

    // Number of whitelist claims so far
    uint256 public claimCount;

    // Address of the contract owner
    address public owner;

    // Event emitted when a user successfully claims tokens
    event Claimed(address indexed claimant);

    // Event emitted when the contract owner updates the whitelist size
    event WhitelistSizeUpdated(uint256 newMaxWhitelistSlots);

    /**
     * @dev Modifier to restrict access to the contract owner.
     */
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can call this function");
        _;
    }

    /**
     * @dev Modifier to ensure the whitelist is not full.
     */
    modifier whitelistNotFull() {
        require(claimCount < maxWhitelistSlots, "Whitelist is full");
        _;
    }

    /**
     * @dev Constructor to initialize the contract.
     * @param _maxWhitelistSlots Maximum number of whitelist slots available.
     */
    constructor(uint256 _maxWhitelistSlots) {
        require(_maxWhitelistSlots > 0, "Whitelist size must be greater than zero");
        owner = msg.sender;
        maxWhitelistSlots = _maxWhitelistSlots;
    }

    /**
     * @dev Function for users to claim tokens.
     *      Users can only claim once, and the whitelist must have available slots.
     */
    function claim() external whitelistNotFull {
        require(!hasClaimed[msg.sender], "Address has already claimed");

        // Mark the user as having claimed
        hasClaimed[msg.sender] = true;

        // Increment the claim count
        claimCount++;

        // Emit the Claimed event
        emit Claimed(msg.sender);
    }

    /**
     * @dev Function for the owner to update the maximum whitelist slots.
     * @param _newMaxWhitelistSlots New maximum whitelist slots value.
     */
    function updateWhitelistSize(uint256 _newMaxWhitelistSlots) external onlyOwner {
        require(_newMaxWhitelistSlots > claimCount, "New size must be greater than current claims");
        maxWhitelistSlots = _newMaxWhitelistSlots;

        // Emit the WhitelistSizeUpdated event
        emit WhitelistSizeUpdated(_newMaxWhitelistSlots);
    }

    /**
     * @dev Function to withdraw contract funds (if applicable) by the owner.
     */
    function withdraw() external onlyOwner {
        // Transfer all contract funds to the owner
        payable(owner).transfer(address(this).balance);
    }

    /**
     * @dev Fallback function to receive Ether (if required for funding).
     */
    receive() external payable {}

    /**
     * @dev Allows the owner to change ownership.
     * @param _newOwner Address of the new owner.
     */
    function transferOwnership(address _newOwner) external onlyOwner {
        require(_newOwner != address(0), "New owner address cannot be zero");
        owner = _newOwner;
    }
}
```

This code adheres to best practices, including access control, proper error handling, and gas efficiency. It provides mechanisms for users to claim tokens on a first-come, first-served basis while letting the owner manage whitelist settings effectively.
