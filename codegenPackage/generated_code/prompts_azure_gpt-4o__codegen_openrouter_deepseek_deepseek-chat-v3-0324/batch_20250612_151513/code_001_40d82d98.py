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
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract NFTLeasingPlatform is ReentrancyGuard, Ownable {
    // Struct to store lease details
    struct Lease {
        address scholar;
        uint256 tokenId;
        uint256 startTime;
        uint256 endTime;
        uint256 leaseAmount;
        bool isActive;
    }

    // Struct to store scholar performance metrics
    struct ScholarRecord {
        uint256 totalLeases;
        uint256 successfulLeases;
        uint256 totalEarnings;
        uint256 lastLeaseTimestamp;
    }

    // Mapping from NFT contract address to tokenId to Lease
    mapping(address => mapping(uint256 => Lease)) public leases;

    // Mapping from scholar address to their performance record
    mapping(address => ScholarRecord) public scholarRecords;

    // Mapping from NFT contract address to whether it's approved
    mapping(address => bool) public approvedNFTContracts;

    // Events
    event NFTContractApproved(address indexed nftContract);
    event NFTContractRevoked(address indexed nftContract);
    event Leased(
        address indexed nftContract,
        uint256 indexed tokenId,
        address indexed scholar,
        uint256 startTime,
        uint256 endTime,
        uint256 leaseAmount
    );
    event LeaseEnded(
        address indexed nftContract,
        uint256 indexed tokenId,
        address indexed scholar,
        uint256 leaseAmount
    );
    event LeaseExtended(
        address indexed nftContract,
        uint256 indexed tokenId,
        uint256 newEndTime,
        uint256 additionalAmount
    );

    // Modifier to check if NFT contract is approved
    modifier onlyApprovedNFT(address _nftContract) {
        require(approvedNFTContracts[_nftContract], "NFT contract not approved");
        _;
    }

    // Modifier to check if caller is NFT owner
    modifier onlyNFTOwner(address _nftContract, uint256 _tokenId) {
        require(
            IERC721(_nftContract).ownerOf(_tokenId) == msg.sender,
            "Caller is not NFT owner"
        );
        _;
    }

    // Modifier to check if lease is active
    modifier onlyActiveLease(address _nftContract, uint256 _tokenId) {
        require(
            leases[_nftContract][_tokenId].isActive,
            "Lease is not active"
        );
        _;
    }

    // Approve an NFT contract for leasing
    function approveNFTContract(address _nftContract) external onlyOwner {
        approvedNFTContracts[_nftContract] = true;
        emit NFTContractApproved(_nftContract);
    }

    // Revoke approval for an NFT contract
    function revokeNFTContract(address _nftContract) external onlyOwner {
        approvedNFTContracts[_nftContract] = false;
        emit NFTContractRevoked(_nftContract);
    }

    // Lease an NFT to a scholar
    function leaseNFT(
        address _nftContract,
        uint256 _tokenId,
        address _scholar,
        uint256 _duration,
        uint256 _leaseAmount
    ) external onlyApprovedNFT(_nftContract) onlyNFTOwner(_nftContract, _tokenId) nonReentrant {
        require(_duration > 0, "Duration must be positive");
        require(_leaseAmount > 0, "Lease amount must be positive");
        require(!leases[_nftContract][_tokenId].isActive, "NFT is already leased");

        // Transfer NFT to contract (custodial)
        IERC721(_nftContract).transferFrom(msg.sender, address(this), _tokenId);

        // Create lease
        leases[_nftContract][_tokenId] = Lease({
            scholar: _scholar,
            tokenId: _tokenId,
            startTime: block.timestamp,
            endTime: block.timestamp + _duration,
            leaseAmount: _leaseAmount,
            isActive: true
        });

        // Update scholar record
        scholarRecords[_scholar].totalLeases += 1;
        scholarRecords[_scholar].lastLeaseTimestamp = block.timestamp;

        emit Leased(
            _nftContract,
            _tokenId,
            _scholar,
            block.timestamp,
            block.timestamp + _duration,
            _leaseAmount
        );
    }

    // End a lease and return NFT to owner
    function endLease(address _nftContract, uint256 _tokenId)
        external
        onlyApprovedNFT(_nftContract)
        onlyActiveLease(_nftContract, _tokenId)
        nonReentrant
    {
        Lease storage lease = leases[_nftContract][_tokenId];
        require(
            msg.sender == lease.scholar || msg.sender == IERC721(_nftContract).ownerOf(_tokenId),
            "Only scholar or owner can end lease"
        );

        // Transfer NFT back to owner
        address owner = IERC721(_nftContract).ownerOf(_tokenId);
        IERC721(_nftContract).transferFrom(address(this), owner, _tokenId);

        // Update lease status
        lease.isActive = false;

        // Update scholar record if lease completed successfully
        if (block.timestamp <= lease.endTime) {
            scholarRecords[lease.scholar].successfulLeases += 1;
            scholarRecords[lease.scholar].totalEarnings += lease.leaseAmount;
        }

        emit LeaseEnded(_nftContract, _tokenId, lease.scholar, lease.leaseAmount);
    }

    // Extend a lease
    function extendLease(
        address _nftContract,
        uint256 _tokenId,
        uint256 _additionalDuration,
        uint256 _additionalAmount
    )
        external
        payable
        onlyApprovedNFT(_nftContract)
        onlyActiveLease(_nftContract, _tokenId)
        nonReentrant
    {
        require(_additionalDuration > 0, "Additional duration must be positive");
        require(_additionalAmount > 0, "Additional amount must be positive");
        require(msg.value >= _additionalAmount, "Insufficient payment");

        Lease storage lease = leases[_nftContract][_tokenId];
        require(msg.sender == lease.scholar, "Only scholar can extend lease");

        lease.endTime += _additionalDuration;
        lease.leaseAmount += _additionalAmount;

        emit LeaseExtended(_nftContract, _tokenId, lease.endTime, _additionalAmount);
    }

    // Get scholar performance record
    function getScholarRecord(address _scholar) external view returns (ScholarRecord memory) {
        return scholarRecords[_scholar];
    }

    // Get lease details
    function getLeaseDetails(address _nftContract, uint256 _tokenId)
        external
        view
        returns (Lease memory)
    {
        return leases[_nftContract][_tokenId];
    }

    // Withdraw funds from contract (only owner)
    function withdraw() external onlyOwner nonReentrant {
        payable(owner()).transfer(address(this).balance);
    }
}
```
