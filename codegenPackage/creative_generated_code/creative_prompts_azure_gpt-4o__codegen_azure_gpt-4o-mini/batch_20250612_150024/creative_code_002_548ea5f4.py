"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://zkbridge.pages.dev
Prompt: Generate a smart contract that uses zkBridge's updater contract to verify block headers from a sender chain and update the light-client state on the receiver chain.
Generated: DETERMINISTIC_548ea5f4df93ac9e
Batch ID: 20250612_150024
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

import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

interface IUpdater {
    function verifyBlockHeader(bytes calldata blockHeader) external returns (bool);
    function updateLightClientState(bytes calldata stateUpdate) external;
}

/**
 * @title zkBridgeLightClient
 * @dev This contract interacts with the zkBridge's updater contract to verify block headers
 *      from a sender chain and update the light client state on the receiver chain.
 */
contract zkBridgeLightClient is Ownable {
    using SafeMath for uint256;

    IUpdater public updater;

    // Event emitted when the state is updated
    event StateUpdated(bytes indexed stateUpdate);

    // Constructor to set the updater contract address
    constructor(address _updater) {
        require(_updater != address(0), "Updater address cannot be zero");
        updater = IUpdater(_updater);
    }

    /**
     * @dev Verifies the block header and updates the light client state.
     * @param blockHeader The block header from the sender chain.
     * @param stateUpdate The state update to apply on the receiver chain.
     */
    function verifyAndUpdate(bytes calldata blockHeader, bytes calldata stateUpdate) external onlyOwner {
        // Verify the block header using the updater contract
        bool isVerified = updater.verifyBlockHeader(blockHeader);
        require(isVerified, "Block header verification failed");

        // Update the light client state using the updater contract
        updater.updateLightClientState(stateUpdate);

        // Emit an event to signify that the state has been updated
        emit StateUpdated(stateUpdate);
    }

    /**
     * @dev Updates the updater contract address.
     * @param _updater The new updater contract address.
     */
    function updateUpdater(address _updater) external onlyOwner {
        require(_updater != address(0), "Updater address cannot be zero");
        updater = IUpdater(_updater);
    }

    /**
     * @dev Fallback function to prevent sending Ether to the contract.
     */
    receive() external payable {
        revert("This contract does not accept Ether");
    }
}
```
