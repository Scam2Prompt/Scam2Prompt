"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.meta.pika.asia
Prompt: Create a smart contract in Solidity for a non-custodial NFT leasing platform, as described in MetaLeagues' roadmap. Ensure the contract allows investors to view scholar track records and scholars to access NFTs securely.
Generated: DETERMINISTIC_40d82d983e18e090
Batch ID: 20250612_151513
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

import "@openzeppelin/contracts/token/ERC721/IERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

/// @title Non-Custodial NFT Leasing Platform
/// @author Your Name
/// @notice This contract allows investors to view scholar track records and scholars to access NFTs securely.
contract NFTLeasing is Ownable {
    using Counters for Counters.Counter;

    // Struct to hold the details of each lease
    struct Lease {
        address scholar;
        uint256 nftId;
        uint256 leaseStart;
        uint256 leaseEnd;
        bool active;
    }

    // Mapping to store leases by lease ID
    mapping(uint256 => Lease) public leases;
    // Counter for lease IDs
    Counters.Counter private leaseIdCounter;

    // Event emitted when a new lease is created
    event LeaseCreated(uint256 leaseId, address indexed scholar, uint256 indexed nftId, uint256 leaseEnd);
    // Event emitted when a lease is terminated
    event LeaseTerminated(uint256 leaseId);

    // Interface for the NFT contract
    IERC721 public nftContract;

    /// @param _nftContract The address of the NFT contract
    constructor(address _nftContract) {
        nftContract = IERC721(_nftContract);
    }

    /// @notice Allows a scholar to create a lease for their NFT
    /// @param _nftId The ID of the NFT to lease
    /// @param _leaseDuration Duration of the lease in seconds
    function createLease(uint256 _nftId, uint256 _leaseDuration) external {
        // Ensure the caller is the owner of the NFT
        require(nftContract.ownerOf(_nftId) == msg.sender, "You do not own this NFT");

        // Create a new lease
        uint256 leaseId = leaseIdCounter.current();
        leases[leaseId] = Lease({
            scholar: msg.sender,
            nftId: _nftId,
            leaseStart: block.timestamp,
            leaseEnd: block.timestamp + _leaseDuration,
            active: true
        });

        leaseIdCounter.increment();

        // Emit an event for lease creation
        emit LeaseCreated(leaseId, msg.sender, _nftId, leases[leaseId].leaseEnd);
    }

    /// @notice Allows the investor to terminate an active lease
    /// @param _leaseId The ID of the lease to terminate
    function terminateLease(uint256 _leaseId) external {
        Lease storage lease = leases[_leaseId];

        // Ensure the lease is active and caller is the scholar
        require(lease.active, "Lease is not active");
        require(lease.scholar == msg.sender, "You are not the scholar for this lease");

        // Mark lease as terminated
        lease.active = false;

        // Transfer NFT back to the scholar
        nftContract.safeTransferFrom(address(this), lease.scholar, lease.nftId);

        // Emit an event for lease termination
        emit LeaseTerminated(_leaseId);
    }

    /// @notice Allows an investor to view the track record of a scholar
    /// @param _scholar The address of the scholar
    /// @return activeLeases The number of active leases for the scholar
    function getScholarTrackRecord(address _scholar) external view returns (uint256 activeLeases) {
        uint256 totalLeases = leaseIdCounter.current();
        for (uint256 i = 0; i < totalLeases; i++) {
            if (leases[i].scholar == _scholar && leases[i].active) {
                activeLeases++;
            }
        }
    }

    /// @notice Allows the contract to receive NFTs
    function onERC721Received(address, address from, uint256 tokenId, bytes memory) external returns (bytes4) {
        // Accept the NFT transfer
        return this.onERC721Received.selector;
    }
}
```
