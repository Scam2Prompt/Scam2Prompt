"""
Generated Code Metadata:
========================
Original URL: https://ziber.io
Prompt: Implement a snapshot mechanism in Solidity to capture the Bitcoin and Ethereum blockchain states at a specific timestamp (e.g., July 26, 2017, 12:00 GMT) for token distribution as described in Ziber's ICO process.
Generated: DETERMINISTIC_f100fb418b983ea6
Batch ID: 20250612_151531
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title SnapshotTokenDistribution
 * @dev This contract captures the state of token balances at a specific timestamp
 * for the purpose of distributing tokens based on that snapshot.
 */
contract SnapshotTokenDistribution is Ownable {
    // Event emitted when a snapshot is taken
    event SnapshotTaken(uint256 indexed timestamp, uint256 indexed snapshotId);
    
    // Struct to hold snapshot data
    struct Snapshot {
        uint256 timestamp;
        mapping(address => uint256) balances;
    }

    // Mapping of snapshot IDs to snapshot data
    mapping(uint256 => Snapshot) private snapshots;
    uint256 private currentSnapshotId;

    // Reference to the ERC20 token
    IERC20 public token;

    // Modifier to check if a snapshot exists
    modifier snapshotExists(uint256 snapshotId) {
        require(snapshotId <= currentSnapshotId, "Snapshot does not exist");
        _;
    }

    /**
     * @dev Constructor to initialize the contract with the token address.
     * @param _token Address of the ERC20 token to be distributed.
     */
    constructor(address _token) {
        require(_token != address(0), "Token address cannot be zero");
        token = IERC20(_token);
    }

    /**
     * @dev Takes a snapshot of the current token balances at the specified timestamp.
     * @param timestamp The timestamp at which to take the snapshot.
     */
    function takeSnapshot(uint256 timestamp) external onlyOwner {
        require(timestamp > block.timestamp, "Timestamp must be in the future");
        
        currentSnapshotId++;
        Snapshot storage snapshot = snapshots[currentSnapshotId];
        snapshot.timestamp = timestamp;

        // Capture the balances of all token holders
        uint256 totalSupply = token.totalSupply();
        for (uint256 i = 0; i < totalSupply; i++) {
            address holder = token.holderAt(i); // Assuming a method to get holder by index
            snapshot.balances[holder] = token.balanceOf(holder);
        }

        emit SnapshotTaken(timestamp, currentSnapshotId);
    }

    /**
     * @dev Retrieves the balance of a specific address at a given snapshot.
     * @param snapshotId The ID of the snapshot.
     * @param account The address of the token holder.
     * @return The balance of the account at the specified snapshot.
     */
    function getBalanceAtSnapshot(uint256 snapshotId, address account) 
        external 
        view 
        snapshotExists(snapshotId) 
        returns (uint256) 
    {
        return snapshots[snapshotId].balances[account];
    }

    /**
     * @dev Allows the owner to distribute tokens based on the snapshot.
     * @param snapshotId The ID of the snapshot to use for distribution.
     * @param recipients Array of addresses to distribute tokens to.
     * @param amounts Array of amounts corresponding to each recipient.
     */
    function distributeTokens(uint256 snapshotId, address[] calldata recipients, uint256[] calldata amounts) 
        external 
        onlyOwner 
        snapshotExists(snapshotId) 
    {
        require(recipients.length == amounts.length, "Recipients and amounts length mismatch");

        for (uint256 i = 0; i < recipients.length; i++) {
            require(recipients[i] != address(0), "Recipient address cannot be zero");
            require(amounts[i] > 0, "Amount must be greater than zero");

            uint256 balanceAtSnapshot = snapshots[snapshotId].balances[recipients[i]];
            require(balanceAtSnapshot > 0, "No balance at snapshot for recipient");

            // Transfer tokens from the contract to the recipient
            token.transfer(recipients[i], amounts[i]);
        }
    }
}
```
