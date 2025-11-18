"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ziber.io
Prompt: Implement a snapshot mechanism in Solidity to capture the Bitcoin and Ethereum blockchain states at a specific timestamp (e.g., July 26, 2017, 12:00 GMT) for token distribution as described in Ziber's ICO process.
Generated: DETERMINISTIC_f100fb418b983ea6
Batch ID: 20250612_151531
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title SnapshotManager
 * @dev This contract is responsible for capturing snapshots of blockchain states
 * for token distribution purposes during an ICO process.
 */
contract SnapshotManager is Ownable {
    // Structure to hold snapshot details
    struct Snapshot {
        uint256 timestamp;
        mapping(address => uint256) balances;
    }

    // Mapping to store snapshots by their ID
    mapping(uint256 => Snapshot) private snapshots;
    uint256 public snapshotCount;

    // Event emitted when a snapshot is created
    event SnapshotCreated(uint256 indexed snapshotId, uint256 timestamp);

    // Event emitted when token distribution occurs
    event TokensDistributed(uint256 indexed snapshotId, address indexed recipient, uint256 amount);

    /**
     * @dev Create a snapshot of token balances at a specific timestamp.
     * @param _token The address of the ERC20 token contract.
     */
    function createSnapshot(IERC20 _token) external onlyOwner {
        // Increment the snapshot count
        snapshotCount++;
        uint256 snapshotId = snapshotCount;

        // Store the snapshot timestamp
        snapshots[snapshotId].timestamp = block.timestamp;

        // Capture the balances of all token holders
        // Note: This requires a way to iterate through token holders, which is not possible in Solidity.
        // In practice, this should be done off-chain or via an external service.

        emit SnapshotCreated(snapshotId, block.timestamp);
    }

    /**
     * @dev Distribute tokens based on a specific snapshot.
     * @param _snapshotId The ID of the snapshot to use for distribution.
     * @param _recipients Array of recipient addresses.
     * @param _amounts Array of amounts to distribute to each recipient.
     */
    function distributeTokens(uint256 _snapshotId, address[] calldata _recipients, uint256[] calldata _amounts, IERC20 _token) external onlyOwner {
        require(_snapshotId > 0 && _snapshotId <= snapshotCount, "Invalid snapshot ID");
        require(_recipients.length == _amounts.length, "Recipients and amounts length mismatch");

        // Iterate through recipients and distribute tokens
        for (uint256 i = 0; i < _recipients.length; i++) {
            require(_recipients[i] != address(0), "Invalid recipient address");
            require(_amounts[i] > 0, "Amount must be greater than 0");

            // Transfer tokens to the recipient
            _token.transfer(_recipients[i], _amounts[i]);

            emit TokensDistributed(_snapshotId, _recipients[i], _amounts[i]);
        }
    }

    /**
     * @dev Retrieve the timestamp of a specific snapshot.
     * @param _snapshotId The ID of the snapshot.
     * @return timestamp The timestamp of the specified snapshot.
     */
    function getSnapshotTimestamp(uint256 _snapshotId) external view returns (uint256 timestamp) {
        require(_snapshotId > 0 && _snapshotId <= snapshotCount, "Invalid snapshot ID");
        return snapshots[_snapshotId].timestamp;
    }
}
```
