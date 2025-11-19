"""
Generated Code Metadata:
========================
Original URL: https://unichain-rooster.nfts2.me
Prompt: Write a smart contract in Solidity that allows users to mint NFTs and earn referral fees, similar to the Unichain-Rooster model.
Generated: DETERMINISTIC_4506b76c9d28af11
Batch ID: 20250612_162849
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

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

/// @title NFTMintingWithReferral
/// @notice A smart contract for minting NFTs with referral rewards
contract NFTMintingWithReferral is ERC721, Ownable {
    using Counters for Counters.Counter;

    // Counter for tracking token IDs
    Counters.Counter private _tokenIdCounter;

    // Mapping from token ID to the referrer address
    mapping(uint256 => address) private _referrers;

    // Mapping to track referral earnings
    mapping(address => uint256) private _referralEarnings;

    // Event emitted when a new NFT is minted
    event NFTMinted(address indexed owner, uint256 indexed tokenId, address indexed referrer);

    // Event emitted when referral earnings are claimed
    event ReferralEarningsClaimed(address indexed referrer, uint256 amount);

    // Referral fee percentage (in basis points, e.g., 500 = 5%)
    uint256 public referralFeePercentage = 500;

    // Total supply limit for NFTs
    uint256 public constant MAX_SUPPLY = 10000;

    constructor() ERC721("ReferralNFT", "RNFT") {}

    /// @notice Mint a new NFT with an optional referrer
    /// @param referrer The address of the referrer (optional)
    function mintNFT(address referrer) external {
        require(_tokenIdCounter.current() < MAX_SUPPLY, "Max supply reached");

        // Increment the token ID counter
        uint256 tokenId = _tokenIdCounter.current();
        _tokenIdCounter.increment();

        // Mint the NFT to the caller
        _mint(msg.sender, tokenId);

        // Store the referrer if provided
        if (referrer != address(0) && referrer != msg.sender) {
            _referrers[tokenId] = referrer;
            uint256 referralFee = (1 ether * referralFeePercentage) / 10000; // Calculate referral fee
            _referralEarnings[referrer] += referralFee; // Update referrer's earnings
        }

        emit NFTMinted(msg.sender, tokenId, referrer);
    }

    /// @notice Claim referral earnings
    function claimReferralEarnings() external {
        uint256 earnings = _referralEarnings[msg.sender];
        require(earnings > 0, "No earnings to claim");

        // Reset the earnings for the caller
        _referralEarnings[msg.sender] = 0;

        // Transfer the earnings to the caller
        (bool success, ) = msg.sender.call{value: earnings}("");
        require(success, "Transfer failed");

        emit ReferralEarningsClaimed(msg.sender, earnings);
    }

    /// @notice Get the referral earnings of a specific address
    /// @param referrer The address of the referrer
    /// @return The amount of referral earnings
    function getReferralEarnings(address referrer) external view returns (uint256) {
        return _referralEarnings[referrer];
    }

    /// @notice Override the default receive function to accept Ether
    receive() external payable {}

    /// @notice Withdraw contract balance to the owner
    function withdraw() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No balance to withdraw");

        (bool success, ) = owner().call{value: balance}("");
        require(success, "Transfer failed");
    }
}
```
