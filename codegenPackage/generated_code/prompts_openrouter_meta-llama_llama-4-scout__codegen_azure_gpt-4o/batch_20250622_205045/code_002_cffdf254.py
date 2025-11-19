"""
Generated Code Metadata:
========================
Original URL: https://www.meta.pika.asia
Prompt: "Design a smart contract for a non-custodial NFT leasing platform, similar to MetaLeagues' planned feature, using Solidity."
Generated: DETERMINISTIC_cffdf2543884c1c0
Batch ID: 20250622_205045
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

/**
 * @title NFTLeasingPlatform
 * @dev A non-custodial NFT leasing platform that allows NFT owners to lease their NFTs to lessees for a specified duration and fee.
 */
contract NFTLeasingPlatform {
    // Struct to represent a lease agreement
    struct Lease {
        address lessor;        // Owner of the NFT
        address lessee;        // Borrower of the NFT
        address nftContract;   // Address of the NFT contract
        uint256 tokenId;       // Token ID of the NFT
        uint256 leaseEndTime;  // Timestamp when the lease ends
        uint256 leaseFee;      // Fee for the lease
        bool isActive;         // Whether the lease is active
    }

    // Mapping to store lease agreements by a unique lease ID
    mapping(uint256 => Lease) public leases;

    // Counter for generating unique lease IDs
    uint256 private leaseCounter;

    // Events
    event LeaseCreated(
        uint256 leaseId,
        address indexed lessor,
        address indexed lessee,
        address indexed nftContract,
        uint256 tokenId,
        uint256 leaseEndTime,
        uint256 leaseFee
    );
    event LeaseTerminated(uint256 leaseId, address indexed lessor, address indexed lessee);

    /**
     * @dev Creates a new lease agreement.
     * @param nftContract Address of the NFT contract.
     * @param tokenId Token ID of the NFT to be leased.
     * @param lessee Address of the lessee.
     * @param duration Duration of the lease in seconds.
     * @param leaseFee Fee for the lease in wei.
     */
    function createLease(
        address nftContract,
        uint256 tokenId,
        address lessee,
        uint256 duration,
        uint256 leaseFee
    ) external {
        require(duration > 0, "Lease duration must be greater than zero");
        require(leaseFee > 0, "Lease fee must be greater than zero");
        require(lessee != address(0), "Invalid lessee address");

        // Ensure the lessor is the owner of the NFT
        require(
            IERC721(nftContract).ownerOf(tokenId) == msg.sender,
            "Caller is not the owner of the NFT"
        );

        // Ensure the lessor has approved this contract to transfer the NFT
        require(
            IERC721(nftContract).isApprovedForAll(msg.sender, address(this)) ||
            IERC721(nftContract).getApproved(tokenId) == address(this),
            "Contract is not approved to transfer the NFT"
        );

        // Increment lease counter to generate a unique lease ID
        leaseCounter++;

        // Create the lease agreement
        leases[leaseCounter] = Lease({
            lessor: msg.sender,
            lessee: lessee,
            nftContract: nftContract,
            tokenId: tokenId,
            leaseEndTime: block.timestamp + duration,
            leaseFee: leaseFee,
            isActive: true
        });

        // Transfer the lease fee from the lessee to the lessor
        require(
            payable(msg.sender).send(leaseFee),
            "Failed to transfer lease fee"
        );

        // Emit the LeaseCreated event
        emit LeaseCreated(
            leaseCounter,
            msg.sender,
            lessee,
            nftContract,
            tokenId,
            block.timestamp + duration,
            leaseFee
        );
    }

    /**
     * @dev Terminates an active lease agreement.
     * @param leaseId ID of the lease to terminate.
     */
    function terminateLease(uint256 leaseId) external {
        Lease storage lease = leases[leaseId];

        require(lease.isActive, "Lease is not active");
        require(
            msg.sender == lease.lessor || msg.sender == lease.lessee,
            "Caller is not authorized to terminate the lease"
        );

        // Ensure the lease has expired
        require(block.timestamp >= lease.leaseEndTime, "Lease has not expired yet");

        // Mark the lease as inactive
        lease.isActive = false;

        // Emit the LeaseTerminated event
        emit LeaseTerminated(leaseId, lease.lessor, lease.lessee);
    }

    /**
     * @dev Returns the details of a lease agreement.
     * @param leaseId ID of the lease to query.
     * @return Lease details.
     */
    function getLeaseDetails(uint256 leaseId) external view returns (Lease memory) {
        return leases[leaseId];
    }
}

// Interface for ERC721 (NFT) standard
interface IERC721 {
    function ownerOf(uint256 tokenId) external view returns (address);
    function isApprovedForAll(address owner, address operator) external view returns (bool);
    function getApproved(uint256 tokenId) external view returns (address);
}
```
