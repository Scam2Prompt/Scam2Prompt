"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bankless.pages.dev
Prompt: Create a smart contract in Solidity that verifies if a Base, Introduced NFT is eligible for $BASED token redemption and checks if the NFT is still in the same wallet after redemption.
Generated: DETERMINISTIC_328d6c71809eea99
Batch ID: 20250612_150946
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
 * @title NFT Eligibility and Redemption Smart Contract
 * @dev This contract verifies if an NFT is eligible for $BASED token redemption
 * and checks if the NFT remains in the same wallet after redemption.
 */
contract NFTBasedTokenRedemption {
    // Address of the NFT contract
    address public nftContractAddress;

    // Mapping to store redeemed NFTs
    mapping(uint256 => bool) public redeemedNFTs;

    // Event emitted when $BASED tokens are redeemed
    event TokenRedemption(address indexed redeemer, uint256 indexed tokenId);

    /**
     * @dev Constructor to initialize the NFT contract address.
     * @param _nftContractAddress Address of the NFT contract.
     */
    constructor(address _nftContractAddress) {
        require(_nftContractAddress != address(0), "Invalid NFT contract address");
        nftContractAddress = _nftContractAddress;
    }

    /**
     * @dev Function to redeem $BASED tokens for an NFT.
     * @param tokenId ID of the NFT to redeem tokens for.
     */
    function redeemToken(uint256 tokenId) external {
        // Validate NFT ownership before redemption
        require(isNFTOwner(msg.sender, tokenId), "Caller is not the owner of the NFT");

        // Ensure the NFT has not already been redeemed
        require(!redeemedNFTs[tokenId], "NFT has already been redeemed");

        // Mark the NFT as redeemed
        redeemedNFTs[tokenId] = true;

        // Emit the redemption event
        emit TokenRedemption(msg.sender, tokenId);
    }

    /**
     * @dev Function to check whether an NFT is eligible for redemption
     * and if it still remains in the same wallet after redemption.
     * @param owner Wallet address of the NFT owner.
     * @param tokenId ID of the NFT to check.
     * @return eligible Boolean indicating eligibility status.
     */
    function checkNFTEligibility(address owner, uint256 tokenId)
        external
        view
        returns (bool eligible)
    {
        // Return true if the NFT is owned by the same wallet and not redeemed
        eligible = isNFTOwner(owner, tokenId) && !redeemedNFTs[tokenId];
    }

    /**
     * @dev Internal function to verify NFT ownership.
     * @param owner Address of the potential NFT owner.
     * @param tokenId ID of the NFT to check ownership for.
     * @return Boolean ownership status.
     */
    function isNFTOwner(address owner, uint256 tokenId) internal view returns (bool) {
        // Interface for the NFT contract
        IERC721 nftContract = IERC721(nftContractAddress);

        // Check ownership
        return nftContract.ownerOf(tokenId) == owner;
    }
}

/**
 * @dev Interface for ERC721 NFT standard.
 */
interface IERC721 {
    function ownerOf(uint256 tokenId) external view returns (address);
}
```
