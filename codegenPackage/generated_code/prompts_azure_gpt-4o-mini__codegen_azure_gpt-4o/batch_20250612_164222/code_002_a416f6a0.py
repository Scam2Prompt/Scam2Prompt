"""
Generated Code Metadata:
========================
Original URL: https://www.meta.pika.asia
Prompt: Create a Solidity smart contract that facilitates NFT leasing for scholars within the MetaLeagues ecosystem.
Generated: DETERMINISTIC_a416f6a022dcc4b0
Batch ID: 20250612_164222
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
 * @title NFT Leasing Contract for MetaLeagues Ecosystem
 * @dev This contract allows NFT owners to lease their NFTs to scholars for a specified duration and fee.
 */
contract NFTLeasing {
    // Struct to store lease details
    struct Lease {
        address owner;         // Address of the NFT owner
        address scholar;       // Address of the scholar leasing the NFT
        uint256 tokenId;       // ID of the NFT being leased
        uint256 leaseStart;    // Start time of the lease (timestamp)
        uint256 leaseEnd;      // End time of the lease (timestamp)
        uint256 leaseFee;      // Fee for the lease (in wei)
        bool isActive;         // Whether the lease is currently active
    }

    // Mapping to store leases by lease ID
    mapping(uint256 => Lease) public leases;

    // Counter for lease IDs
    uint256 public leaseCounter;

    // ERC721 interface for interacting with NFTs
    IERC721 public nftContract;

    // Events
    event LeaseCreated(uint256 leaseId, address indexed owner, address indexed scholar, uint256 tokenId, uint256 leaseStart, uint256 leaseEnd, uint256 leaseFee);
    event LeaseTerminated(uint256 leaseId, address indexed owner, address indexed scholar, uint256 tokenId);

    /**
     * @dev Constructor to initialize the NFT contract address.
     * @param _nftContract Address of the ERC721 NFT contract.
     */
    constructor(address _nftContract) {
        require(_nftContract != address(0), "Invalid NFT contract address");
        nftContract = IERC721(_nftContract);
    }

    /**
     * @dev Create a new lease for an NFT.
     * @param _tokenId ID of the NFT to be leased.
     * @param _scholar Address of the scholar leasing the NFT.
     * @param _leaseDuration Duration of the lease in seconds.
     * @param _leaseFee Fee for the lease (in wei).
     */
    function createLease(uint256 _tokenId, address _scholar, uint256 _leaseDuration, uint256 _leaseFee) external {
        require(_scholar != address(0), "Invalid scholar address");
        require(_leaseDuration > 0, "Lease duration must be greater than zero");
        require(_leaseFee > 0, "Lease fee must be greater than zero");

        // Ensure the caller owns the NFT
        require(nftContract.ownerOf(_tokenId) == msg.sender, "Caller is not the owner of the NFT");

        // Transfer the NFT to the contract for the lease duration
        nftContract.transferFrom(msg.sender, address(this), _tokenId);

        // Create the lease
        leaseCounter++;
        leases[leaseCounter] = Lease({
            owner: msg.sender,
            scholar: _scholar,
            tokenId: _tokenId,
            leaseStart: block.timestamp,
            leaseEnd: block.timestamp + _leaseDuration,
            leaseFee: _leaseFee,
            isActive: true
        });

        emit LeaseCreated(leaseCounter, msg.sender, _scholar, _tokenId, block.timestamp, block.timestamp + _leaseDuration, _leaseFee);
    }

    /**
     * @dev Terminate an active lease and return the NFT to the owner.
     * @param _leaseId ID of the lease to terminate.
     */
    function terminateLease(uint256 _leaseId) external {
        Lease storage lease = leases[_leaseId];

        require(lease.isActive, "Lease is not active");
        require(lease.owner == msg.sender, "Caller is not the owner of the lease");

        // Return the NFT to the owner
        nftContract.transferFrom(address(this), lease.owner, lease.tokenId);

        // Mark the lease as inactive
        lease.isActive = false;

        emit LeaseTerminated(_leaseId, lease.owner, lease.scholar, lease.tokenId);
    }

    /**
     * @dev Scholar pays the lease fee to activate the lease.
     * @param _leaseId ID of the lease to activate.
     */
    function payLeaseFee(uint256 _leaseId) external payable {
        Lease storage lease = leases[_leaseId];

        require(lease.isActive, "Lease is not active");
        require(lease.scholar == msg.sender, "Caller is not the scholar of the lease");
        require(msg.value == lease.leaseFee, "Incorrect lease fee");

        // Transfer the lease fee to the owner
        payable(lease.owner).transfer(msg.value);
    }

    /**
     * @dev Check if a lease is active.
     * @param _leaseId ID of the lease to check.
     * @return True if the lease is active, false otherwise.
     */
    function isLeaseActive(uint256 _leaseId) external view returns (bool) {
        Lease storage lease = leases[_leaseId];
        return lease.isActive && block.timestamp < lease.leaseEnd;
    }
}

// Minimal ERC721 interface
interface IERC721 {
    function ownerOf(uint256 tokenId) external view returns (address);
    function transferFrom(address from, address to, uint256 tokenId) external;
}
```
