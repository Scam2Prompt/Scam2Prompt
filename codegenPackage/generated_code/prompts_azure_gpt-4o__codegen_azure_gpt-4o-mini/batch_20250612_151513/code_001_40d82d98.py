"""
Generated Code Metadata:
========================
Original URL: https://www.meta.pika.asia
Prompt: Create a smart contract in Solidity for a non-custodial NFT leasing platform, as described in MetaLeagues' roadmap. Ensure the contract allows investors to view scholar track records and scholars to access NFTs securely.
Generated: DETERMINISTIC_40d82d983e18e090
Batch ID: 20250612_151513
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

import "@openzeppelin/contracts/token/ERC721/IERC721.sol";
import "@openzeppelin/contracts/token/ERC721/utils/ERC721Holder.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

// Interface for the NFT contract
interface INFT is IERC721 {
    function getTrackRecord(address scholar) external view returns (string memory);
}

// Smart contract for the non-custodial NFT leasing platform
contract NFTLeasingPlatform is Ownable, ERC721Holder {
    using Counters for Counters.Counter;

    // Struct to hold lease information
    struct Lease {
        address scholar;
        address investor;
        uint256 tokenId;
        uint256 leaseStart;
        uint256 leaseEnd;
        bool isActive;
    }

    // Mapping to store leases by their ID
    mapping(uint256 => Lease) public leases;
    Counters.Counter private leaseIdCounter;

    // Event emitted when a lease is created
    event LeaseCreated(uint256 leaseId, address indexed scholar, address indexed investor, uint256 tokenId, uint256 leaseStart, uint256 leaseEnd);
    
    // Event emitted when a lease is terminated
    event LeaseTerminated(uint256 leaseId);

    // Reference to the NFT contract
    INFT public nftContract;

    // Constructor to set the NFT contract address
    constructor(address _nftContract) {
        require(_nftContract != address(0), "Invalid NFT contract address");
        nftContract = INFT(_nftContract);
    }

    // Function to create a lease for an NFT
    function createLease(address scholar, uint256 tokenId, uint256 leaseDuration) external {
        require(nftContract.ownerOf(tokenId) == msg.sender, "Only the owner can lease the NFT");
        require(leaseDuration > 0, "Lease duration must be greater than zero");

        // Transfer the NFT to the contract
        nftContract.safeTransferFrom(msg.sender, address(this), tokenId);

        // Create a new lease
        leaseIdCounter.increment();
        uint256 leaseId = leaseIdCounter.current();
        leases[leaseId] = Lease({
            scholar: scholar,
            investor: msg.sender,
            tokenId: tokenId,
            leaseStart: block.timestamp,
            leaseEnd: block.timestamp + leaseDuration,
            isActive: true
        });

        emit LeaseCreated(leaseId, scholar, msg.sender, tokenId, block.timestamp, block.timestamp + leaseDuration);
    }

    // Function to terminate a lease
    function terminateLease(uint256 leaseId) external {
        Lease storage lease = leases[leaseId];
        require(lease.isActive, "Lease is not active");
        require(msg.sender == lease.investor || msg.sender == owner(), "Only the investor or owner can terminate the lease");

        // Transfer the NFT back to the investor
        nftContract.safeTransferFrom(address(this), lease.investor, lease.tokenId);

        // Mark the lease as inactive
        lease.isActive = false;

        emit LeaseTerminated(leaseId);
    }

    // Function for scholars to view their track record
    function viewTrackRecord(address scholar) external view returns (string memory) {
        return nftContract.getTrackRecord(scholar);
    }

    // Function to retrieve lease details
    function getLeaseDetails(uint256 leaseId) external view returns (Lease memory) {
        return leases[leaseId];
    }
}
```
