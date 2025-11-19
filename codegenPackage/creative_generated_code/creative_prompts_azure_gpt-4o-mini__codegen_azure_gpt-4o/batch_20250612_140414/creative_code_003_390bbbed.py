"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://arbitrum.nfts2.me
Prompt: Can you provide an example of how to track referral earnings for mints made through a referral link in an Arbitrum-based NFT project?
Generated: DETERMINISTIC_390bbbed7bab317f
Batch ID: 20250612_140414
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
 * @title Arbitrum NFT Referral Earnings Tracker
 * @notice Smart contract to track referral earnings for mints made through referral links
 */
contract NFTReferralTracker {
    // Struct for Referral Data
    struct Referral {
        uint256 totalEarnings; // Total earnings of the referrer
        uint256 totalMints;    // Total mints attributed to the referrer
    }

    // Mapping to store referral data by referrer address
    mapping(address => Referral) public referrals;

    // Mapping to store mint prices by token ID
    mapping(uint256 => uint256) public tokenMintPrices;

    // NFT owners (for demonstrating ownership tracking)
    mapping(uint256 => address) public tokenOwners;

    // Event emitted on successful NFT mint through referral
    event NFTMinted(
        address indexed minter,
        address indexed referrer,
        uint256 indexed tokenId,
        uint256 mintPrice,
        uint256 referralEarnings
    );

    // Owner address (contract deployer)
    address public owner;

    // Referral percentage (e.g., 10% -> 1000 basis points)
    uint256 public referralPercentage; // In basis points (1% = 100)

    /**
     * @notice Modifier to restrict access to contract owner
     */
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the contract owner can perform this action.");
        _;
    }

    /**
     * @notice Constructor to initialize contract parameters
     * @param _referralPercentage Referral percentage in basis points
     */
    constructor(uint256 _referralPercentage) {
        require(
            _referralPercentage <= 10000,
            "Referral percentage cannot exceed 10000 basis points (100%)."
        );
        owner = msg.sender;
        referralPercentage = _referralPercentage;
    }

    /**
     * @notice Function to mint an NFT with a referral link
     * @param tokenId ID of the token to mint
     * @param referrer Address of the referrer
     */
    function mintNFT(uint256 tokenId, address referrer) external payable {
        // Check if token is already minted
        require(tokenOwners[tokenId] == address(0), "Token already minted.");

        // Validate mint price
        uint256 mintPrice = tokenMintPrices[tokenId];
        require(mintPrice > 0, "Mint price not set for this token.");
        require(msg.value == mintPrice, "Incorrect ETH sent for minting.");

        // Mint the token to the sender
        tokenOwners[tokenId] = msg.sender;

        // Calculate referral earnings
        uint256 referralEarnings = (mintPrice * referralPercentage) / 10000;

        // Update referral data
        if (referrer != address(0) && referrer != msg.sender) {
            referrals[referrer].totalEarnings += referralEarnings;
            referrals[referrer].totalMints += 1;

            // Send referral earnings to referrer
            (bool success, ) = referrer.call{value: referralEarnings}("");
            require(success, "Failed to transfer referral earnings.");
        }

        // Emit the NFTMinted event
        emit NFTMinted(msg.sender, referrer, tokenId, mintPrice, referralEarnings);

        // Send remaining funds to contract owner
        uint256 remainingFunds = mintPrice - referralEarnings;
        (bool ownerTransferSuccess, ) = owner.call{value: remainingFunds}("");
        require(ownerTransferSuccess, "Failed to transfer funds to the owner.");
    }

    /**
     * @notice Function to set the mint price for a token
     * @param tokenId ID of the token
     * @param price Mint price in wei
     */
    function setMintPrice(uint256 tokenId, uint256 price) external onlyOwner {
        require(price > 0, "Mint price must be greater than zero.");
        tokenMintPrices[tokenId] = price;
    }

    /**
     * @notice Function to withdraw ETH from the contract
     */
    function withdraw() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No funds available to withdraw.");
        (bool success, ) = owner.call{value: balance}("");
        require(success, "Failed to withdraw funds.");
    }

    /**
     * @notice Fallback function to handle ETH sent directly to the contract
     */
    receive() external payable {}

    /**
     * @notice Function to get the referral data for a specific referrer
     * @param referrer Address of the referrer
     * @return totalEarnings Total earnings of the referrer
     * @return totalMints Total mints attributed to the referrer
     */
    function getReferralData(address referrer)
        external
        view
        returns (uint256 totalEarnings, uint256 totalMints)
    {
        Referral memory referral = referrals[referrer];
        return (referral.totalEarnings, referral.totalMints);
    }
}
```
