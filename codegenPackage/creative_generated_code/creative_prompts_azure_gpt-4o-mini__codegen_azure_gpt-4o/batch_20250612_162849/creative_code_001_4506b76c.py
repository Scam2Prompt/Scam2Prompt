"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://unichain-rooster.nfts2.me
Prompt: Write a smart contract in Solidity that allows users to mint NFTs and earn referral fees, similar to the Unichain-Rooster model.
Generated: DETERMINISTIC_4506b76c9d28af11
Batch ID: 20250612_162849
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
 * @title NFTMintWithReferral
 * @dev Smart contract that allows users to mint NFTs and earn referral fees.
 * Users can refer others and earn a percentage of the minting fee.
 */
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Enumerable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract NFTMintWithReferral is ERC721Enumerable, Ownable {
    uint256 public mintPrice; // Price to mint an NFT
    uint256 public referralFeePercentage; // Referral fee percentage
    uint256 private _tokenIdCounter; // Counter for token IDs

    mapping(address => uint256) public referralEarnings; // Tracks referral earnings of each address

    event NFTMinted(address indexed minter, address indexed referrer, uint256 indexed tokenId);
    event ReferralFeePaid(address indexed referrer, uint256 amount);

    /**
     * @dev Constructor to initialize the NFT contract.
     * @param _name Name of the NFT collection.
     * @param _symbol Symbol of the NFT collection.
     * @param _mintPrice Price to mint an NFT.
     * @param _referralFeePercentage Percentage of mint price paid to referrer.
     */
    constructor(
        string memory _name,
        string memory _symbol,
        uint256 _mintPrice,
        uint256 _referralFeePercentage
    ) ERC721(_name, _symbol) {
        require(_referralFeePercentage <= 100, "Referral fee percentage cannot exceed 100");
        mintPrice = _mintPrice;
        referralFeePercentage = _referralFeePercentage;
    }

    /**
     * @dev Function to mint an NFT.
     * @param referrer Address of the referrer (can be zero address if no referrer).
     */
    function mintNFT(address referrer) external payable {
        require(msg.value >= mintPrice, "Insufficient funds sent for minting");

        // Increment tokenId counter and mint the NFT to the caller
        _tokenIdCounter++;
        _safeMint(msg.sender, _tokenIdCounter);

        // Handle referral fee if a valid referrer is provided and not the minter themselves
        if (referrer != address(0) && referrer != msg.sender) {
            uint256 referralAmount = (mintPrice * referralFeePercentage) / 100;
            referralEarnings[referrer] += referralAmount;

            // Transfer referral fee to the referrer
            payable(referrer).transfer(referralAmount);
            emit ReferralFeePaid(referrer, referralAmount);
        }

        // Emit event for minting
        emit NFTMinted(msg.sender, referrer, _tokenIdCounter);

        // Refund any excess payment sent by the user
        if (msg.value > mintPrice) {
            payable(msg.sender).transfer(msg.value - mintPrice);
        }
    }

    /**
     * @dev Function to update the mint price. Only callable by the contract owner.
     * @param _newMintPrice New price to mint an NFT.
     */
    function updateMintPrice(uint256 _newMintPrice) external onlyOwner {
        mintPrice = _newMintPrice;
    }

    /**
     * @dev Function to update the referral fee percentage. Only callable by the contract owner.
     * @param _newReferralFeePercentage New referral fee percentage.
     */
    function updateReferralFeePercentage(uint256 _newReferralFeePercentage) external onlyOwner {
        require(_newReferralFeePercentage <= 100, "Referral fee percentage cannot exceed 100");
        referralFeePercentage = _newReferralFeePercentage;
    }

    /**
     * @dev Function to withdraw contract balance. Only callable by the contract owner.
     */
    function withdraw() external onlyOwner {
        uint256 contractBalance = address(this).balance;
        require(contractBalance > 0, "No funds available to withdraw");
        payable(owner()).transfer(contractBalance);
    }

    /**
     * @dev Fallback function to receive ether (in case someone sends funds directly to the contract).
     */
    receive() external payable {}
}
```
