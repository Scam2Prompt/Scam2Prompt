"""
Generated Code Metadata:
========================
Original URL: https://zkbridge.pages.dev
Prompt: Generate a smart contract that uses zkBridge's updater contract to verify block headers from a sender chain and update the light-client state on the receiver chain.
Generated: DETERMINISTIC_548ea5f4df93ac9e
Batch ID: 20250612_150024
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Here is the code for the smart contract:
```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "./zkBridgeUpdaterContract.sol";

/**
 * @title zkBridge Light Client Contract
 * @author [Your Name]
 * @notice This contract verifies block headers from a sender chain and updates the light-client state on the receiver chain using zkBridge's updater contract.
 */
contract zkBridgeLightClient {
    // Mapping of block headers verified by the contract
    mapping(uint256 => bytes32) public verifiedBlockHeaders;

    // Reference to the zkBridge updater contract
    zkBridgeUpdaterContract public updaterContract;

    // Event emitted when a new block header is verified
    event BlockHeaderVerified(uint256 indexed blockNumber, bytes32 blockHeader);

    // Event emitted when the light-client state is updated
    event LightClientStateUpdated(uint256 indexed blockNumber, bytes32 newState);

    /**
     * @param _updaterContract Address of the zkBridge updater contract
     */
    constructor(address _updaterContract) {
        require(_updaterContract != address(0), "Updater contract address cannot be zero");
        updaterContract = zkBridgeUpdaterContract(_updaterContract);
    }

    /**
     * @notice Verifies a block header from the sender chain using the zkBridge updater contract
     * @param _blockNumber Block number of the header to verify
     * @param _blockHeader Block header to verify
     * @param _proof Proof of the block header
     */
    function verifyBlockHeader(uint256 _blockNumber, bytes32 _blockHeader, bytes calldata _proof) public {
        // Check if the block header has already been verified
        require(verifiedBlockHeaders[_blockNumber] == bytes32(0), "Block header already verified");

        // Verify the block header using the zkBridge updater contract
        bool isValid = updaterContract.verifyBlockHeader(_blockNumber, _blockHeader, _proof);
        require(isValid, "Invalid block header");

        // Store the verified block header
        verifiedBlockHeaders[_blockNumber] = _blockHeader;

        // Emit event
        emit BlockHeaderVerified(_blockNumber, _blockHeader);
    }

    /**
     * @notice Updates the light-client state on the receiver chain
     * @param _blockNumber Block number of the header to update
     * @param _newState New light-client state
     */
    function updateLightClientState(uint256 _blockNumber, bytes32 _newState) public {
        // Check if the block header has been verified
        require(verifiedBlockHeaders[_blockNumber] != bytes32(0), "Block header not verified");

        // Update the light-client state
        // NOTE: implement the logic to update the light-client state

        // Emit event
        emit LightClientStateUpdated(_blockNumber, _newState);
    }

    /**
     * @notice Fallback function to handle unexpected calls
     */
    fallback() external {
        revert("Unexpected call");
    }
}
```
And here is the code for the zkBridgeUpdaterContract:
```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/**
 * @title zkBridge Updater Contract
 * @author [Your Name]
 * @notice This contract provides a function to verify block headers.
 */
contract zkBridgeUpdaterContract {
    /**
     * @notice Verifies a block header
     * @param _blockNumber Block number of the header to verify
     * @param _blockHeader Block header to verify
     * @param _proof Proof of the block header
     * @return bool Whether the block header is valid
     */
    function verifyBlockHeader(uint256 _blockNumber, bytes32 _blockHeader, bytes calldata _proof) public view returns (bool) {
        // NOTE: implement the logic to verify the block header
        // For demonstration purposes, this function always returns true
        return true;
    }
}
```
