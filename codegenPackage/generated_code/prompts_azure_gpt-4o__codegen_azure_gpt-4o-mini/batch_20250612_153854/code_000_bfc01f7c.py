"""
Generated Code Metadata:
========================
Original URL: https://zora-air-spring.nfts2.me
Prompt: Write a smart contract in Solidity that generates a referral link for a wallet address and tracks referral fees for minting NFTs, similar to the functionality described on the Zora Air Spring platform.
Generated: DETERMINISTIC_bfc01f7cec7c19fc
Batch ID: 20250612_153854
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

/// @title ReferralNFT
/// @notice A smart contract for minting NFTs with referral tracking
contract ReferralNFT is ERC721, Ownable {
    using Counters for Counters.Counter;

    // Counter for tracking token IDs
    Counters.Counter private _tokenIdCounter;

    // Mapping from wallet address to referral link
    mapping(address => string) public referralLinks;

    // Mapping from wallet address to referral earnings
    mapping(address => uint256) public referralEarnings;

    // Event emitted when a new NFT is minted
    event NFTMinted(address indexed owner, uint256 tokenId, address indexed referrer);

    // Event emitted when a referral link is created
    event ReferralLinkCreated(address indexed user, string referralLink);

    // Base fee for minting an NFT
    uint256 public mintingFee = 0.01 ether;

    // Referral fee percentage (in basis points, e.g., 500 = 5%)
    uint256 public referralFeePercentage = 500;

    /// @dev Constructor to initialize the contract with a name and symbol
    constructor() ERC721("ReferralNFT", "rNFT") {}

    /// @notice Create a referral link for the sender
    /// @param _link The referral link to be created
    function createReferralLink(string memory _link) external {
        require(bytes(referralLinks[msg.sender]).length == 0, "Referral link already exists");
        referralLinks[msg.sender] = _link;
        emit ReferralLinkCreated(msg.sender, _link);
    }

    /// @notice Mint a new NFT with an optional referrer
    /// @param referrer The address of the referrer (optional)
    function mintNFT(address referrer) external payable {
        require(msg.value >= mintingFee, "Insufficient funds to mint NFT");

        // Increment the token ID counter and get the new token ID
        uint256 tokenId = _tokenIdCounter.current();
        _tokenIdCounter.increment();

        // Mint the NFT to the sender
        _mint(msg.sender, tokenId);

        // Handle referral fees if a valid referrer is provided
        if (referrer != address(0) && referrer != msg.sender) {
            uint256 referralFee = (msg.value * referralFeePercentage) / 10000;
            referralEarnings[referrer] += referralFee;
            payable(referrer).transfer(referralFee);
        }

        // Emit the NFTMinted event
        emit NFTMinted(msg.sender, tokenId, referrer);
    }

    /// @notice Withdraw accumulated referral earnings for the owner
    function withdrawEarnings() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No earnings to withdraw");
        payable(owner()).transfer(balance);
    }

    /// @notice Set a new minting fee
    /// @param newFee The new minting fee in wei
    function setMintingFee(uint256 newFee) external onlyOwner {
        mintingFee = newFee;
    }

    /// @notice Set a new referral fee percentage
    /// @param newPercentage The new referral fee percentage in basis points
    function setReferralFeePercentage(uint256 newPercentage) external onlyOwner {
        require(newPercentage <= 10000, "Percentage cannot exceed 100%");
        referralFeePercentage = newPercentage;
    }
}
```
