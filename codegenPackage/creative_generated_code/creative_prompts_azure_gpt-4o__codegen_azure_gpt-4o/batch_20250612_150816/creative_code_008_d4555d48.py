"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bonemv.com
Prompt: Generate a Solidity contract that tracks reward claims and prevents duplicate claims, inspired by the REWARD Portal v2 functionality.
Generated: DETERMINISTIC_d4555d4882323eae
Batch ID: 20250612_150816
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.18;

/**
 * @title RewardTracker
 * @dev A smart contract to track reward claims and prevent duplicate claims.
 */
contract RewardTracker {
    // Owner of the contract
    address private owner;

    // Mapping to track whether an address has claimed its reward
    mapping(address => bool) private hasClaimedReward;

    // Event emitted when a reward is successfully claimed
    event RewardClaimed(address indexed claimant);

    // Modifier to restrict certain functions to the contract owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Access restricted to contract owner");
        _;
    }

    /**
     * @dev Constructor to set the contract's owner to the deployer.
     */
    constructor() {
        owner = msg.sender;
    }

    /**
     * @dev Allows the address to claim their reward if they haven't already.
     */
    function claimReward() external {
        // Revert if the address has already claimed its reward
        require(!hasClaimedReward[msg.sender], "Reward already claimed");

        // Mark the reward as claimed for the sender
        hasClaimedReward[msg.sender] = true;

        // Emit the RewardClaimed event
        emit RewardClaimed(msg.sender);
    }

    /**
     * @dev Checks if an address has already claimed a reward.
     * @param claimant The address to check.
     * @return True if the address has claimed a reward, false otherwise.
     */
    function hasClaimed(address claimant) external view returns (bool) {
        return hasClaimedReward[claimant];
    }

    /**
     * @dev Allows the owner to reset reward claims for a specific address.
     * @param claimant The address whose claim status will be reset.
     */
    function resetClaim(address claimant) external onlyOwner {
        // Reset the claim status for the specified address
        hasClaimedReward[claimant] = false;
    }

    /**
     * @dev Allows the owner to transfer ownership of the contract to a new address.
     * @param newOwner The address of the new owner.
     */
    function transferOwnership(address newOwner) external onlyOwner {
        require(newOwner != address(0), "New owner address cannot be zero");
        owner = newOwner;
    }

    /**
     * @dev Allows the contract owner to self-destruct the contract, removing it from the blockchain.
     */
    function destroyContract() external onlyOwner {
        selfdestruct(payable(owner));
    }
}
```
