"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tgcasino-app.pages.dev
Prompt: Generate a Solidity contract to implement TG.Casino's NFT-based High Roller rewards system, including staking bonuses and rakeback percentages.
Generated: DETERMINISTIC_fba084acdc676fc0
Batch ID: 20250612_153517
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

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

contract HighRollerRewards is ERC721, Ownable {
    using SafeMath for uint256;

    // Struct to store NFT metadata related to rewards
    struct NFTRewards {
        uint256 stakingBonus;    // Bonus percentage for staking
        uint256 rakebackPercent; // Rakeback percentage
    }

    // Mapping from tokenId to NFT rewards metadata
    mapping(uint256 => NFTRewards) public nftRewards;

    // Mapping from staker address to the staked tokenId
    mapping(address => uint256) public stakedNFT;

    // Event declarations for logging
    event NFTMinted(address indexed owner, uint256 tokenId, uint256 stakingBonus, uint256 rakebackPercent);
    event NFTStaked(address indexed staker, uint256 tokenId);
    event NFTUnstaked(address indexed staker, uint256 tokenId);

    // Constructor to set the NFT name and symbol
    constructor() ERC721("HighRollerNFT", "HRNFT") {}

    /**
     * @dev Mint a new NFT with rewards metadata.
     * @param recipient Address of the NFT recipient.
     * @param stakingBonus Staking bonus percentage.
     * @param rakebackPercent Rakeback percentage.
     */
    function mintNFT(
        address recipient,
        uint256 stakingBonus,
        uint256 rakebackPercent
    ) external onlyOwner {
        require(recipient != address(0), "Invalid recipient address");
        require(stakingBonus > 0 && stakingBonus <= 100, "Staking bonus must be between 1% and 100%");
        require(rakebackPercent > 0 && rakebackPercent <= 100, "Rakeback percentage must be between 1% and 100%");

        // Generate a new tokenId, incrementing total supply
        uint256 tokenId = totalSupply() + 1;

        // Mint the NFT
        _safeMint(recipient, tokenId);

        // Assign rewards metadata to the NFT
        nftRewards[tokenId] = NFTRewards(stakingBonus, rakebackPercent);

        emit NFTMinted(recipient, tokenId, stakingBonus, rakebackPercent);
    }

    /**
     * @dev Stake an NFT for High Roller rewards. The caller must own the NFT.
     * @param tokenId ID of the NFT to stake.
     */
    function stakeNFT(uint256 tokenId) external {
        require(ownerOf(tokenId) == msg.sender, "Caller is not the owner of the NFT");
        require(stakedNFT[msg.sender] == 0, "Already staking another NFT");

        // Transfer the NFT to the contract for staking
        safeTransferFrom(msg.sender, address(this), tokenId);

        // Record the staking
        stakedNFT[msg.sender] = tokenId;

        emit NFTStaked(msg.sender, tokenId);
    }

    /**
     * @dev Unstake an NFT and transfer it back to the owner.
     */
    function unstakeNFT() external {
        uint256 tokenId = stakedNFT[msg.sender];
        require(tokenId != 0, "No NFT is currently staked");

        // Transfer the NFT back to the owner
        safeTransferFrom(address(this), msg.sender, tokenId);

        // Clear staking record
        stakedNFT[msg.sender] = 0;

        emit NFTUnstaked(msg.sender, tokenId);
    }

    /**
     * @dev Get rewards metadata of a specific NFT.
     * @param tokenId ID of the NFT.
     * @return stakingBonus Staking bonus percentage.
     * @return rakebackPercent Rakeback percentage.
     */
    function getNFTRewards(uint256 tokenId) external view returns (uint256 stakingBonus, uint256 rakebackPercent) {
        require(_exists(tokenId), "NFT does not exist");

        NFTRewards memory rewards = nftRewards[tokenId];
        return (rewards.stakingBonus, rewards.rakebackPercent);
    }

    /**
     * @dev Override totalSupply function, since OpenZeppelin's ERC721 does not implement it.
     * @return Total NFT supply.
     */
    function totalSupply() public view returns (uint256) {
        return _owners.length; // _owners is a private variable in ERC721 tracking token ownership
    }
}
```
