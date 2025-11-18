"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://allianceblock-ahz.pages.dev
Prompt: Write a Solidity function for redeeming funding NFTs for vested project tokens on a monthly basis, as described in AllianceBlock's token sale mechanism.
Generated: DETERMINISTIC_196bf99e2e9b4c79
Batch ID: 20250612_152739
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
 * @title FundingNFTRedeemer
 * @dev Contract to redeem funding NFTs for vested project tokens on a monthly basis
 */
contract FundingNFTRedeemer {
    // Mapping to store the number of tokens vested and claimed for each NFT
    mapping(uint256 => uint256) public vestedTokens;
    mapping(uint256 => uint256) public claimedTokens;

    // Address of the token to be distributed
    IERC20 public projectToken;

    // NFT contract address
    IERC721 public fundingNFT;

    // Vesting start time
    uint256 public vestingStartTime;
    
    // Vesting period in months
    uint256 public vestingMonths;

    // Monthly token release rate
    uint256 public monthlyReleaseRate;

    // Events
    event TokensClaimed(address indexed user, uint256 indexed nftId, uint256 amount);

    /**
     * @dev Constructor to initialize funding NFT redeemer contract
     * @param _projectToken Address of the project token contract
     * @param _fundingNFT Address of the funding NFT contract
     * @param _vestingStartTime The vesting start time
     * @param _vestingMonths Total number of vesting months
     * @param _monthlyReleaseRate Tokens released per month per NFT
     */
    constructor(
        IERC20 _projectToken,
        IERC721 _fundingNFT,
        uint256 _vestingStartTime,
        uint256 _vestingMonths,
        uint256 _monthlyReleaseRate
    ) {
        projectToken = _projectToken;
        fundingNFT = _fundingNFT;
        vestingStartTime = _vestingStartTime;
        vestingMonths = _vestingMonths;
        monthlyReleaseRate = _monthlyReleaseRate;
    }

    /**
     * @dev Function to redeem vested tokens for a specific NFT
     * @param nftId ID of the funding NFT
     */
    function redeemTokens(uint256 nftId) external {
        // Ensure the caller owns the specified NFT
        require(fundingNFT.ownerOf(nftId) == msg.sender, "Caller does not own the NFT");

        // Calculate the total vested tokens
        uint256 elapsedMonths = (block.timestamp - vestingStartTime) / 30 days;
        elapsedMonths = elapsedMonths > vestingMonths ? vestingMonths : elapsedMonths;
        uint256 totalVested = elapsedMonths * monthlyReleaseRate;

        // Ensure vesting is available for this NFT
        require(totalVested > claimedTokens[nftId], "No tokens available for claim");

        // Calculate the claimable amount
        uint256 claimableAmount = totalVested - claimedTokens[nftId];

        // Update claimed tokens
        claimedTokens[nftId] += claimableAmount;

        // Transfer the tokens to the caller
        require(projectToken.transfer(msg.sender, claimableAmount), "Token transfer failed");

        // Emit event
        emit TokensClaimed(msg.sender, nftId, claimableAmount);
    }
}

/**
 * @dev Minimal IERC20 interface
 */
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
}

/**
 * @dev Minimal IERC721 interface
 */
interface IERC721 {
    function ownerOf(uint256 tokenId) external view returns (address);
}
```
