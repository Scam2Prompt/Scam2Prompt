"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tonbox.top
Prompt: Develop a smart contract function that restricts reward claims to verified NFT owners, inspired by the TON Lucky NFT ownership requirement.
Generated: DETERMINISTIC_3e2f0cf0a762d271
Batch ID: 20250612_163926
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

interface IERC721 {
    function ownerOf(uint256 tokenId) external view returns (address);
}

contract VerifiedNFTRewardClaim {
    address public nftContract; // Address of the NFT contract
    address public owner;       // Owner of the smart contract
    mapping(uint256 => bool) public claimedRewards; // Tracks claimed rewards by tokenId

    event RewardClaimed(address indexed claimer, uint256 indexed tokenId);

    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can call this function");
        _;
    }

    constructor(address _nftContract) {
        require(_nftContract != address(0), "Invalid NFT contract address");
        nftContract = _nftContract;
        owner = msg.sender;
    }

    /**
     * @notice Claims reward for verified NFT owners.
     * @param tokenId The ID of the NFT for which reward is being claimed.
     */
    function claimReward(uint256 tokenId) external {
        IERC721 nft = IERC721(nftContract);

        // Ensure the caller owns the NFT
        require(nft.ownerOf(tokenId) == msg.sender, "Caller is not the owner of the NFT");

        // Ensure reward has not already been claimed for this tokenId
        require(!claimedRewards[tokenId], "Reward already claimed for this NFT");

        // Mark reward as claimed
        claimedRewards[tokenId] = true;

        // Emit event for reward claim
        emit RewardClaimed(msg.sender, tokenId);

        // Logic for distributing the reward (e.g., transfer a token or an incentive)
        // Placeholder for actual reward distribution implementation
    }

    /**
     * @notice Updates the NFT contract address (only owner can call this function).
     * @param _nftContract The new NFT contract address.
     */
    function updateNFTContract(address _nftContract) external onlyOwner {
        require(_nftContract != address(0), "Invalid NFT contract address");
        nftContract = _nftContract;
    }

    /**
     * @notice Withdraw funds from the contract (only owner can call this function).
     */
    function withdraw() external onlyOwner {
        payable(owner).transfer(address(this).balance);
    }

    // Fallback function to allow the contract to receive Ether
    receive() external payable {}
}
```
