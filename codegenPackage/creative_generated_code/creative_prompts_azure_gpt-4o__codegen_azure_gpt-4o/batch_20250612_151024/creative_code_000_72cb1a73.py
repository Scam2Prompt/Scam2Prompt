"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://grooveup.pages.dev
Prompt: Write a smart contract in Solidity for a decentralized "stream-to-earn" platform that rewards fans with tokens ($GROOVE) for streaming and reviewing music. Ensure the contract includes functionality for token distribution and artist NFT integration.
Generated: DETERMINISTIC_72cb1a733daf2f48
Batch ID: 20250612_151024
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
 * @title StreamToEarn
 * @dev A decentralized platform rewarding fans for streaming and reviewing music.
 * Fans earn $GROOVE tokens and artists can integrate NFTs for unique benefits.
 */
contract StreamToEarn {
    // Token-related variables
    address public owner;
    IERC20 public grooveToken;
    
    // Artist NFT contract
    IERC721 public artistNFT;

    // Struct to store artist information
    struct Artist {
        address artistAddress;
        uint256 tokenRewardRate; // Tokens rewarded per stream
        uint256 totalStreams;   // Total streams recorded
    }

    // Mapping to store artist details
    mapping(address => Artist) public artists;

    /**
     * @dev Modifier to restrict function access to the owner.
     */
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can call this function");
        _;
    }

    /**
     * @dev Modifier to ensure the sender is a registered artist.
     */
    modifier onlyArtist() {
        require(artists[msg.sender].artistAddress != address(0), "Only registered artists can call this function");
        _;
    }

    /**
     * @dev Event emitted when a stream is recorded.
     */
    event StreamRecorded(address indexed fan, address indexed artist, uint256 rewardAmount);

    /**
     * @dev Event emitted when a new artist is registered.
     */
    event ArtistRegistered(address indexed artist, uint256 tokenRewardRate);

    /**
     * @dev Constructor to initialize the contract with the token and NFT contract addresses.
     * @param _grooveToken Address of the $GROOVE token contract.
     * @param _artistNFT Address of the artist NFT contract.
     */
    constructor(address _grooveToken, address _artistNFT) {
        owner = msg.sender;
        grooveToken = IERC20(_grooveToken);
        artistNFT = IERC721(_artistNFT);
    }

    /**
     * @dev Function to register a new artist.
     * @param _artistAddress Address of the artist.
     * @param _tokenRewardRate Tokens to reward per stream.
     */
    function registerArtist(address _artistAddress, uint256 _tokenRewardRate) external onlyOwner {
        require(_artistAddress != address(0), "Invalid artist address");
        require(_tokenRewardRate > 0, "Reward rate must be greater than zero");

        artists[_artistAddress] = Artist({
            artistAddress: _artistAddress,
            tokenRewardRate: _tokenRewardRate,
            totalStreams: 0
        });

        emit ArtistRegistered(_artistAddress, _tokenRewardRate);
    }

    /**
     * @dev Function to record a stream and reward the fan.
     * @param _artistAddress Address of the artist whose music was streamed.
     */
    function recordStream(address _artistAddress) external {
        require(_artistAddress != address(0), "Invalid artist address");
        require(artists[_artistAddress].artistAddress != address(0), "Artist not registered");

        Artist storage artist = artists[_artistAddress];

        // Calculate reward amount and validate token availability
        uint256 rewardAmount = artist.tokenRewardRate;
        require(grooveToken.balanceOf(address(this)) >= rewardAmount, "Insufficient contract balance for rewards");

        // Transfer tokens to the fan
        grooveToken.transfer(msg.sender, rewardAmount);

        // Update stream count for the artist
        artist.totalStreams += 1;

        emit StreamRecorded(msg.sender, _artistAddress, rewardAmount);
    }

    /**
     * @dev Withdraw any remaining tokens in the contract (owner-only function).
     * @param _amount Amount of tokens to withdraw.
     */
    function withdrawTokens(uint256 _amount) external onlyOwner {
        require(_amount > 0, "Withdraw amount must be greater than zero");
        require(grooveToken.balanceOf(address(this)) >= _amount, "Insufficient contract balance");

        grooveToken.transfer(owner, _amount);
    }

    /**
     * @dev Check if a fan holds an artist's NFT for potential exclusive benefits.
     * @param _fan Address of the fan.
     * @param _artistNFTId ID of the artist NFT.
     * @return bool True if the fan holds the NFT, false otherwise.
     */
    function doesFanHoldArtistNFT(address _fan, uint256 _artistNFTId) external view returns (bool) {
        return artistNFT.ownerOf(_artistNFTId) == _fan;
    }
}

// Interface for ERC20 tokens
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}

// Interface for ERC721 tokens (NFTs)
interface IERC721 {
    function ownerOf(uint256 tokenId) external view returns (address);
}
```
