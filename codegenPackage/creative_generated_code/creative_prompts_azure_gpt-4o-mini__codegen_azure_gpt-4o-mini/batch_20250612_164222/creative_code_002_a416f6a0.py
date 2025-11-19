"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.meta.pika.asia
Prompt: Create a Solidity smart contract that facilitates NFT leasing for scholars within the MetaLeagues ecosystem.
Generated: DETERMINISTIC_a416f6a022dcc4b0
Batch ID: 20250612_164222
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
import "@openzeppelin/contracts/token/ERC721/extensions/IERC721Metadata.sol";
import "@openzeppelin/contracts/utils/Counters.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/// @title NFT Leasing Contract for Scholars in the MetaLeagues Ecosystem
/// @dev This contract allows users to lease their NFTs to scholars for a specified duration.
contract NFTLeasing is Ownable {
    using Counters for Counters.Counter;

    // Struct to hold lease details
    struct Lease {
        address lessor;             // Address of the NFT owner
        address lessee;             // Address of the scholar leasing the NFT
        uint256 tokenId;            // ID of the NFT being leased
        uint256 leaseStart;         // Start time of the lease
        uint256 leaseEnd;           // End time of the lease
        bool isActive;              // Lease status
    }

    // Mapping from lease ID to Lease struct
    mapping(uint256 => Lease) public leases;
    Counters.Counter private leaseIdCounter; // Counter for lease IDs

    // Event emitted when a lease is created
    event LeaseCreated(uint256 indexed leaseId, address indexed lessor, address indexed lessee, uint256 tokenId, uint256 leaseEnd);
    
    // Event emitted when a lease is terminated
    event LeaseTerminated(uint256 indexed leaseId);

    // Modifier to check if the caller is the lessee
    modifier onlyLessee(uint256 leaseId) {
        require(msg.sender == leases[leaseId].lessee, "Caller is not the lessee");
        _;
    }

    // Modifier to check if the lease is active
    modifier leaseIsActive(uint256 leaseId) {
        require(leases[leaseId].isActive, "Lease is not active");
        require(block.timestamp < leases[leaseId].leaseEnd, "Lease has expired");
        _;
    }

    /// @notice Creates a new lease for an NFT
    /// @param _nftContract Address of the NFT contract
    /// @param _tokenId ID of the NFT to lease
    /// @param _lessee Address of the scholar leasing the NFT
    /// @param _duration Duration of the lease in seconds
    function createLease(
        address _nftContract,
        uint256 _tokenId,
        address _lessee,
        uint256 _duration
    ) external {
        require(IERC721(_nftContract).ownerOf(_tokenId) == msg.sender, "Caller is not the NFT owner");
        require(_lessee != address(0), "Invalid lessee address");
        require(_duration > 0, "Duration must be greater than zero");

        // Transfer NFT to lessee
        IERC721(_nftContract).transferFrom(msg.sender, _lessee, _tokenId);

        // Create a new lease
        uint256 leaseId = leaseIdCounter.current();
        leaseIdCounter.increment();

        leases[leaseId] = Lease({
            lessor: msg.sender,
            lessee: _lessee,
            tokenId: _tokenId,
            leaseStart: block.timestamp,
            leaseEnd: block.timestamp + _duration,
            isActive: true
        });

        emit LeaseCreated(leaseId, msg.sender, _lessee, _tokenId, block.timestamp + _duration);
    }

    /// @notice Terminates an existing lease
    /// @param leaseId ID of the lease to terminate
    function terminateLease(uint256 leaseId) external onlyLessee(leaseId) leaseIsActive(leaseId) {
        // Mark lease as inactive
        leases[leaseId].isActive = false;

        // Transfer NFT back to lessor
        IERC721(leases[leaseId].lessor).transferFrom(msg.sender, leases[leaseId].lessor, leases[leaseId].tokenId);

        emit LeaseTerminated(leaseId);
    }

    /// @notice Retrieves the details of a lease
    /// @param leaseId ID of the lease to retrieve
    /// @return Lessor, Lessee, TokenId, LeaseStart, LeaseEnd, IsActive
    function getLeaseDetails(uint256 leaseId) external view returns (address, address, uint256, uint256, uint256, bool) {
        Lease memory lease = leases[leaseId];
        return (lease.lessor, lease.lessee, lease.tokenId, lease.leaseStart, lease.leaseEnd, lease.isActive);
    }
}
```
