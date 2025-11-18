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

/**
 * @title Non-Custodial NFT Leasing Platform
 * @author MetaLeagues
 * @notice This contract enables investors to lease NFTs to scholars securely
 *         and view scholar track records. Scholars can use leased NFTs without
 *         transferring ownership.
 */
contract NFTLeasingPlatform {
    // Events
    event NFTLeased(address indexed investor, address indexed scholar, uint256 indexed tokenId, uint256 leaseDuration);
    event LeaseEnded(address indexed investor, address indexed scholar, uint256 indexed tokenId);
    event ScholarPerformanceUpdated(address indexed scholar, uint256 performanceScore);

    // Data structures
    struct Lease {
        address investor;
        address scholar;
        uint256 tokenId;
        uint256 leaseStart;
        uint256 leaseDuration; // in seconds
    }

    struct Scholar {
        uint256 totalPerformanceScore;
        uint256 numberOfLeases;
    }

    // Storage
    mapping(uint256 => Lease) public activeLeases; // tokenId => Lease
    mapping(address => Scholar) public scholarRecords; // scholar address => Scholar
    mapping(address => mapping(uint256 => bool)) public investorApprovals; // investor => tokenId => approval

    // External contracts
    IERC721 public nftContract;

    // Constructor
    constructor(address _nftContract) {
        require(_nftContract != address(0), "Invalid NFT contract address");
        nftContract = IERC721(_nftContract);
    }

    // Modifiers
    modifier onlyInvestor(uint256 tokenId) {
        require(nftContract.ownerOf(tokenId) == msg.sender, "Caller is not the NFT owner");
        _;
    }

    modifier onlyScholar(uint256 tokenId) {
        require(activeLeases[tokenId].scholar == msg.sender, "Caller is not the NFT scholar");
        _;
    }

    modifier leaseExists(uint256 tokenId) {
        require(activeLeases[tokenId].investor != address(0), "Lease does not exist");
        _;
    }

    // Functions

    /**
     * @notice Approve a scholar to use an NFT
     * @param scholar The address of the scholar
     * @param tokenId The ID of the NFT
     */
    function approveScholar(address scholar, uint256 tokenId) external onlyInvestor(tokenId) {
        require(scholar != address(0), "Invalid scholar address");
        investorApprovals[msg.sender][tokenId] = true;
    }

    /**
     * @notice Lease an NFT to a scholar
     * @param tokenId The ID of the NFT
     * @param leaseDuration The lease duration in seconds
     */
    function leaseNFT(uint256 tokenId, uint256 leaseDuration) external {
        // Verify conditions
        require(investorApprovals[nftContract.ownerOf(tokenId)][tokenId], "Scholar not approved by investor");
        require(leaseDuration > 0, "Lease duration must be greater than zero");

        // Create lease
        address investor = nftContract.ownerOf(tokenId);
        activeLeases[tokenId] = Lease({
            investor: investor,
            scholar: msg.sender,
            tokenId: tokenId,
            leaseStart: block.timestamp,
            leaseDuration: leaseDuration
        });

        emit NFTLeased(investor, msg.sender, tokenId, leaseDuration);
    }

    /**
     * @notice End a lease manually or automatically after duration expires
     * @param tokenId The ID of the NFT
     */
    function endLease(uint256 tokenId) external leaseExists(tokenId) {
        // Verify conditions
        Lease memory lease = activeLeases[tokenId];
        require(
            msg.sender == lease.investor || 
            msg.sender == lease.scholar || 
            block.timestamp >= lease.leaseStart + lease.leaseDuration,
            "Unauthorized to end lease"
        );

        // Clean up lease
        delete activeLeases[tokenId];
        investorApprovals[lease.investor][tokenId] = false;

        emit LeaseEnded(lease.investor, lease.scholar, tokenId);
    }

    /**
     * @notice Update scholar's performance score
     * @param scholar The address of the scholar
     * @param score The performance score to add
     */
    function updateScholarPerformance(address scholar, uint256 score) external {
        require(score > 0, "Invalid performance score");
        scholarRecords[scholar].totalPerformanceScore += score;
        scholarRecords[scholar].numberOfLeases += 1;

        emit ScholarPerformanceUpdated(scholar, scholarRecords[scholar].totalPerformanceScore);
    }

    /**
     * @notice Get scholar's performance record
     * @param scholar The address of the scholar
     * @return totalPerformanceScore Total performance score of the scholar
     * @return numberOfLeases Number of leases completed by the scholar
     */
    function getScholarRecord(address scholar) external view returns (uint256 totalPerformanceScore, uint256 numberOfLeases) {
        Scholar memory record = scholarRecords[scholar];
        return (record.totalPerformanceScore, record.numberOfLeases);
    }
}

/**
 * @dev Interface for ERC-721 standard
 */
interface IERC721 {
    function ownerOf(uint256 tokenId) external view returns (address);
}
```
