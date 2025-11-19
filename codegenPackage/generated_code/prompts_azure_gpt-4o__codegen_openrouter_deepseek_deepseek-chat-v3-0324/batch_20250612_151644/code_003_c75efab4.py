"""
Generated Code Metadata:
========================
Original URL: https://shibuya-git-website-redesign-landing-page-pleasrdevs.vercel.app
Prompt: Provide an example of a smart contract written in Solidity for managing NFT claims tied to user participation in interactive media series.
Generated: DETERMINISTIC_c75efab42fe480b4
Batch ID: 20250612_151644
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

contract InteractiveMediaNFT is ERC721, Ownable {
    using Counters for Counters.Counter;
    Counters.Counter private _tokenIdCounter;

    // Struct to store episode participation data
    struct EpisodeParticipation {
        uint256 episodeId;
        uint256 participationThreshold;
        mapping(address => uint256) userParticipation;
        mapping(address => bool) hasClaimed;
    }

    // Mapping from episode ID to participation data
    mapping(uint256 => EpisodeParticipation) public episodes;

    // Base URI for NFT metadata
    string private _baseTokenURI;

    // Event emitted when a user claims an NFT
    event NFTClaimed(address indexed user, uint256 episodeId, uint256 tokenId);

    constructor(string memory name, string memory symbol, string memory baseURI) ERC721(name, symbol) {
        _baseTokenURI = baseURI;
    }

    /**
     * @dev Sets the participation threshold for an episode
     * @param episodeId The ID of the episode
     * @param threshold The minimum participation required to claim NFT
     */
    function setEpisodeThreshold(uint256 episodeId, uint256 threshold) external onlyOwner {
        episodes[episodeId].episodeId = episodeId;
        episodes[episodeId].participationThreshold = threshold;
    }

    /**
     * @dev Records user participation for an episode
     * @param episodeId The ID of the episode
     * @param user The address of the participating user
     * @param amount The amount of participation to add
     */
    function recordParticipation(uint256 episodeId, address user, uint256 amount) external onlyOwner {
        EpisodeParticipation storage episode = episodes[episodeId];
        require(episode.episodeId == episodeId, "Episode not initialized");
        episode.userParticipation[user] += amount;
    }

    /**
     * @dev Claims NFT if participation threshold is met
     * @param episodeId The ID of the episode to claim for
     */
    function claimNFT(uint256 episodeId) external {
        EpisodeParticipation storage episode = episodes[episodeId];
        require(episode.episodeId == episodeId, "Episode not initialized");
        require(!episode.hasClaimed[msg.sender], "NFT already claimed for this episode");
        require(
            episode.userParticipation[msg.sender] >= episode.participationThreshold,
            "Participation threshold not met"
        );

        uint256 tokenId = _tokenIdCounter.current();
        _tokenIdCounter.increment();
        _safeMint(msg.sender, tokenId);
        episode.hasClaimed[msg.sender] = true;

        emit NFTClaimed(msg.sender, episodeId, tokenId);
    }

    /**
     * @dev Updates the base URI for NFT metadata
     * @param baseURI The new base URI
     */
    function setBaseURI(string memory baseURI) external onlyOwner {
        _baseTokenURI = baseURI;
    }

    /**
     * @dev Returns the base URI for NFT metadata
     */
    function _baseURI() internal view virtual override returns (string memory) {
        return _baseTokenURI;
    }

    /**
     * @dev Checks if a user can claim NFT for an episode
     * @param episodeId The ID of the episode
     * @param user The address of the user to check
     * @return canClaim Whether the user can claim
     * @return hasClaimed Whether the user has already claimed
     */
    function canClaimNFT(uint256 episodeId, address user) external view returns (bool canClaim, bool hasClaimed) {
        EpisodeParticipation storage episode = episodes[episodeId];
        hasClaimed = episode.hasClaimed[user];
        canClaim = !hasClaimed && 
                  episode.episodeId == episodeId && 
                  episode.userParticipation[user] >= episode.participationThreshold;
    }
}
```
