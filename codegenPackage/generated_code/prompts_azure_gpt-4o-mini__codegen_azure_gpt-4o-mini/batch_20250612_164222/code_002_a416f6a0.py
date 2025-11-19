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

// Importing the ERC721 interface and Ownable contract from OpenZeppelin
import "@openzeppelin/contracts/token/ERC721/IERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Interface for the NFT leasing contract
interface INFTLeasing {
    function leaseNFT(uint256 tokenId, address lessee, uint256 duration) external;
    function returnNFT(uint256 tokenId) external;
}

// NFTLeasing contract for leasing NFTs
contract NFTLeasing is INFTLeasing, Ownable {
    // Struct to hold lease information
    struct Lease {
        address lessee;
        uint256 startTime;
        uint256 duration;
    }

    // Mapping from token ID to lease information
    mapping(uint256 => Lease) public leases;

    // Event emitted when an NFT is leased
    event NFTLeased(uint256 indexed tokenId, address indexed lessee, uint256 duration);

    // Event emitted when an NFT lease is returned
    event NFTReturned(uint256 indexed tokenId);

    // Modifier to check if the caller is the lessee
    modifier onlyLessee(uint256 tokenId) {
        require(leases[tokenId].lessee == msg.sender, "Not the lessee");
        _;
    }

    // Function to lease an NFT
    function leaseNFT(uint256 tokenId, address lessee, uint256 duration) external override onlyOwner {
        require(lessee != address(0), "Invalid lessee address");
        require(duration > 0, "Duration must be greater than zero");
        require(leases[tokenId].lessee == address(0), "NFT already leased");

        // Set lease information
        leases[tokenId] = Lease({
            lessee: lessee,
            startTime: block.timestamp,
            duration: duration
        });

        emit NFTLeased(tokenId, lessee, duration);
    }

    // Function to return an NFT
    function returnNFT(uint256 tokenId) external override onlyLessee(tokenId) {
        require(block.timestamp <= leases[tokenId].startTime + leases[tokenId].duration, "Lease period has expired");

        // Clear lease information
        delete leases[tokenId];

        emit NFTReturned(tokenId);
    }

    // Function to check if an NFT is currently leased
    function isNFTLeased(uint256 tokenId) external view returns (bool) {
        return leases[tokenId].lessee != address(0);
    }

    // Function to get lease details
    function getLeaseDetails(uint256 tokenId) external view returns (address lessee, uint256 startTime, uint256 duration) {
        Lease memory lease = leases[tokenId];
        return (lease.lessee, lease.startTime, lease.duration);
    }
}
```
