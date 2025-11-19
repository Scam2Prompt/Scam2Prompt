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

/**
 * @title NFTLeaseContract
 * @dev A smart contract to facilitate NFT leasing for scholars within the MetaLeagues ecosystem.
 *      The contract allows owners to lease their NFTs to scholars for a specified duration and fee.
 */
contract NFTLeaseContract {
    // Struct to store lease details
    struct Lease {
        address nftAddress;      // Address of the NFT contract
        uint256 tokenId;         // Token ID of the NFT
        address owner;           // Owner of the NFT
        address scholar;         // Scholar who is leasing the NFT
        uint256 leaseStart;      // Start timestamp of the lease
        uint256 leaseEnd;        // End timestamp of the lease
        uint256 leaseFee;        // Lease fee in wei
    }

    // Mapping to store active leases
    mapping(uint256 => Lease) public leases;

    // Counter to track lease IDs
    uint256 private leaseIdCounter;

    // Events
    event LeaseCreated(
        uint256 indexed leaseId,
        address indexed nftAddress,
        uint256 tokenId,
        address indexed scholar,
        uint256 leaseStart,
        uint256 leaseEnd,
        uint256 leaseFee
    );
    event LeaseTerminated(uint256 indexed leaseId);

    // Modifiers
    modifier onlyOwner(uint256 leaseId) {
        require(
            leases[leaseId].owner == msg.sender,
            "Only the owner of the NFT can call this function"
        );
        _;
    }

    modifier leaseExists(uint256 leaseId) {
        require(leases[leaseId].owner != address(0), "Lease does not exist");
        _;
    }

    /**
     * @dev Creates a lease for an NFT.
     * @param nftAddress Address of the NFT contract.
     * @param tokenId Token ID of the NFT.
     * @param scholar Address of the scholar leasing the NFT.
     * @param leaseDuration Duration of the lease in seconds.
     * @param leaseFee Fee for the lease in wei.
     */
    function createLease(
        address nftAddress,
        uint256 tokenId,
        address scholar,
        uint256 leaseDuration,
        uint256 leaseFee
    ) external {
        require(scholar != address(0), "Scholar address cannot be zero");
        require(leaseDuration > 0, "Lease duration must be greater than zero");
        require(leaseFee > 0, "Lease fee must be greater than zero");

        // Increment lease ID counter
        leaseIdCounter++;

        // Create the lease
        leases[leaseIdCounter] = Lease({
            nftAddress: nftAddress,
            tokenId: tokenId,
            owner: msg.sender,
            scholar: scholar,
            leaseStart: block.timestamp,
            leaseEnd: block.timestamp + leaseDuration,
            leaseFee: leaseFee
        });

        // Emit the LeaseCreated event
        emit LeaseCreated(
            leaseIdCounter,
            nftAddress,
            tokenId,
            scholar,
            block.timestamp,
            block.timestamp + leaseDuration,
            leaseFee
        );
    }

    /**
     * @dev Terminates a lease and returns the NFT to the owner.
     * @param leaseId ID of the lease to terminate.
     */
    function terminateLease(uint256 leaseId)
        external
        leaseExists(leaseId)
        onlyOwner(leaseId)
    {
        // Delete the lease
        delete leases[leaseId];

        // Emit the LeaseTerminated event
        emit LeaseTerminated(leaseId);
    }

    /**
     * @dev Allows the scholar to pay the lease fee.
     * @param leaseId ID of the lease.
     */
    function payLeaseFee(uint256 leaseId) external payable leaseExists(leaseId) {
        Lease memory lease = leases[leaseId];

        require(
            msg.sender == lease.scholar,
            "Only the scholar can pay the lease fee"
        );
        require(
            block.timestamp >= lease.leaseStart &&
                block.timestamp <= lease.leaseEnd,
            "Lease is not active"
        );
        require(msg.value == lease.leaseFee, "Incorrect lease fee amount");

        // Transfer the lease fee to the owner
        payable(lease.owner).transfer(msg.value);
    }

    /**
     * @dev Gets lease details by ID.
     * @param leaseId ID of the lease.
     * @return The lease details.
     */
    function getLease(uint256 leaseId)
        external
        view
        leaseExists(leaseId)
        returns (Lease memory)
    {
        return leases[leaseId];
    }
}
```
