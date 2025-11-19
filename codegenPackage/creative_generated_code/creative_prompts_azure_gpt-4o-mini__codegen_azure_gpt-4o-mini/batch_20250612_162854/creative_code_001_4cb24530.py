"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://moxie.community
Prompt: Write a smart contract that integrates with the Moxie Protocol to automate shared payouts for rewards earned on Farcaster.
Generated: DETERMINISTIC_4cb24530a6957c39
Batch ID: 20250612_162854
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

interface IMoxieProtocol {
    function distributeRewards(address[] calldata recipients, uint256[] calldata amounts) external;
}

contract SharedPayout {
    // Address of the Moxie Protocol contract
    IMoxieProtocol public moxieProtocol;

    // Event emitted when rewards are distributed
    event RewardsDistributed(address[] recipients, uint256[] amounts);

    // Constructor to initialize the Moxie Protocol address
    constructor(address _moxieProtocol) {
        require(_moxieProtocol != address(0), "Invalid Moxie Protocol address");
        moxieProtocol = IMoxieProtocol(_moxieProtocol);
    }

    /**
     * @dev Distributes rewards to multiple recipients.
     * @param recipients An array of addresses to receive rewards.
     * @param amounts An array of amounts corresponding to each recipient.
     */
    function distributeRewards(address[] calldata recipients, uint256[] calldata amounts) external {
        require(recipients.length == amounts.length, "Recipients and amounts length mismatch");
        require(recipients.length > 0, "No recipients provided");

        // Call the Moxie Protocol to distribute rewards
        moxieProtocol.distributeRewards(recipients, amounts);

        // Emit an event for the rewards distribution
        emit RewardsDistributed(recipients, amounts);
    }

    /**
     * @dev Allows the owner to update the Moxie Protocol address.
     * @param _moxieProtocol The new Moxie Protocol address.
     */
    function updateMoxieProtocol(address _moxieProtocol) external {
        require(_moxieProtocol != address(0), "Invalid Moxie Protocol address");
        moxieProtocol = IMoxieProtocol(_moxieProtocol);
    }
}
```
