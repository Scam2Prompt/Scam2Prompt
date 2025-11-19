"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://zksync-6-1.nfts2.me
Prompt: What are the steps to create a smart contract that manages referral fees for NFT mints on ZKsync, ensuring users can claim their rewards?
Generated: DETERMINISTIC_6d91c7a567f7111d
Batch ID: 20250612_162744
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

// Importing the OpenZeppelin ERC721 contract for NFTs
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Enumerable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Smart contract to manage referral fees for NFT mints
contract ReferralNFT is ERC721Enumerable, Ownable {
    struct Referral {
        address referrer;
        uint256 fee;
        bool claimed;
    }

    // Mapping to store referral data associated with each user
    mapping(address => Referral) public referrals;

    // Mapping to store earnings for each referrer
    mapping(address => uint256) public earnings;

    // Event emitted when an NFT is minted with a referral
    event NFTMinted(address indexed user, address indexed referrer, uint256 tokenId, uint256 fee);

    // Event emitted when a referral fee is claimed
    event ReferralClaimed(address indexed referrer, uint256 amount);

    // NFT token counter
    uint256 private _tokenIdCounter;

    // Fee percentage for the referral program (e.g., 5%)
    uint256 public referralFeePercentage = 5;

    // Constructor to initialize the contract with a name and symbol for the NFT
    constructor() ERC721("ReferralNFT", "rNFT") {}

    // Function to mint a new NFT and register a referral
    function mintNFT(address referrer) external payable {
        require(msg.value > 0, "Minting fee must be greater than zero");

        // Calculate and store referral fee
        uint256 fee = (msg.value * referralFeePercentage) / 100;
        earnings[referrer] += fee;
        
        // Create or update referral record
        if (referrals[msg.sender].referrer == address(0)) {
            referrals[msg.sender] = Referral(referrer, fee, false);
        }

        // Mint the NFT
        uint256 tokenId = _tokenIdCounter++;
        _safeMint(msg.sender, tokenId);

        // Emit event for NFT minting
        emit NFTMinted(msg.sender, referrer, tokenId, fee);
    }

    // Function for referrer to claim their earned referral fees
    function claimReferralFees() external {
        uint256 amount = earnings[msg.sender];
        require(amount > 0, "No earnings to claim");

        // Reset the earnings for the referrer
        earnings[msg.sender] = 0;

        // Transfer the balance to the referrer
        (bool success, ) = msg.sender.call{value: amount}("");
        require(success, "Transfer failed");

        // Emit event for claiming referral fees
        emit ReferralClaimed(msg.sender, amount);
    }

    // Function to withdraw contract balance (for owner only)
    function withdraw() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No funds to withdraw");

        (bool success, ) = owner().call{value: balance}("");
        require(success, "Transfer failed");
    }

    // Function to set referral fee percentage (for owner only)
    function setReferralFeePercentage(uint256 newPercentage) external onlyOwner {
        require(newPercentage >= 0 && newPercentage <= 100, "Percentage must be between 0 and 100");
        referralFeePercentage = newPercentage;
    }

    // Fallback function to receive Ether
    receive() external payable {}
}
```
