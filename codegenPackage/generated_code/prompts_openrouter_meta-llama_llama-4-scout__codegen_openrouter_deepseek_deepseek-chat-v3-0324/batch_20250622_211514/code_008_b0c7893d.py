"""
Generated Code Metadata:
========================
Original URL: https://mike-token-web-olj7orfr7-percenal-miketoken.vercel.app
Prompt: Write a smart contract function to manage NFT launches and artist collaborations on the Mike Token platform, as mentioned in the Q3 2023 roadmap.
Generated: DETERMINISTIC_b0c7893dca28f29a
Batch ID: 20250622_211514
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
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

contract MikeTokenNFTLaunch is ERC721, Ownable, ReentrancyGuard {
    using Counters for Counters.Counter;
    
    // Struct to store artist collaboration details
    struct Collaboration {
        address artistAddress;
        uint256 royaltyPercentage;
        bool isActive;
    }

    // NFT launch details
    struct NFTLaunch {
        uint256 launchId;
        string metadataURI;
        uint256 maxSupply;
        uint256 mintPrice;
        uint256 totalMinted;
        bool isActive;
        address[] collaborators;
    }

    // State variables
    Counters.Counter private _launchIdCounter;
    mapping(uint256 => NFTLaunch) public launches;
    mapping(uint256 => mapping(address => Collaboration)) public collaborations;
    mapping(uint256 => mapping(address => bool)) private _hasMinted;

    // Events
    event LaunchCreated(
        uint256 indexed launchId,
        string metadataURI,
        uint256 maxSupply,
        uint256 mintPrice,
        address[] collaborators
    );
    event NFTPurchased(
        uint256 indexed launchId,
        address indexed buyer,
        uint256 tokenId
    );
    event CollaborationAdded(
        uint256 indexed launchId,
        address indexed artist,
        uint256 royaltyPercentage
    );
    event CollaborationRemoved(
        uint256 indexed launchId,
        address indexed artist
    );

    // Constructor
    constructor() ERC721("MikeTokenNFT", "MTN") {}

    /**
     * @dev Creates a new NFT launch
     * @param metadataURI The URI pointing to the NFT metadata
     * @param maxSupply Maximum number of NFTs that can be minted
     * @param mintPrice Price per NFT in wei
     * @param collaborators Array of artist addresses to collaborate with
     * @param royaltyPercentages Array of royalty percentages for collaborators
     */
    function createLaunch(
        string memory metadataURI,
        uint256 maxSupply,
        uint256 mintPrice,
        address[] memory collaborators,
        uint256[] memory royaltyPercentages
    ) external onlyOwner {
        require(collaborators.length == royaltyPercentages.length, "Arrays length mismatch");
        require(maxSupply > 0, "Max supply must be greater than 0");

        uint256 launchId = _launchIdCounter.current();
        _launchIdCounter.increment();

        launches[launchId] = NFTLaunch({
            launchId: launchId,
            metadataURI: metadataURI,
            maxSupply: maxSupply,
            mintPrice: mintPrice,
            totalMinted: 0,
            isActive: true,
            collaborators: collaborators
        });

        for (uint256 i = 0; i < collaborators.length; i++) {
            collaborations[launchId][collaborators[i]] = Collaboration({
                artistAddress: collaborators[i],
                royaltyPercentage: royaltyPercentages[i],
                isActive: true
            });
        }

        emit LaunchCreated(launchId, metadataURI, maxSupply, mintPrice, collaborators);
    }

    /**
     * @dev Mints an NFT from a specific launch
     * @param launchId The ID of the launch to mint from
     */
    function mintNFT(uint256 launchId) external payable nonReentrant {
        NFTLaunch storage launch = launches[launchId];
        require(launch.isActive, "Launch is not active");
        require(msg.value == launch.mintPrice, "Incorrect ETH amount");
        require(launch.totalMinted < launch.maxSupply, "Max supply reached");
        require(!_hasMinted[launchId][msg.sender], "Already minted");

        uint256 tokenId = launch.totalMinted + 1;
        _safeMint(msg.sender, tokenId);
        launch.totalMinted++;

        _hasMinted[launchId][msg.sender] = true;

        // Distribute royalties to collaborators
        _distributeRoyalties(launchId);

        emit NFTPurchased(launchId, msg.sender, tokenId);
    }

    /**
     * @dev Internal function to distribute royalties to collaborators
     * @param launchId The ID of the launch
     */
    function _distributeRoyalties(uint256 launchId) internal {
        NFTLaunch storage launch = launches[launchId];
        uint256 totalRoyalty = msg.value;
        uint256 remaining = msg.value;

        for (uint256 i = 0; i < launch.collaborators.length; i++) {
            address collaborator = launch.collaborators[i];
            Collaboration storage collab = collaborations[launchId][collaborator];
            
            if (collab.isActive) {
                uint256 share = (totalRoyalty * collab.royaltyPercentage) / 100;
                payable(collaborator).transfer(share);
                remaining -= share;
            }
        }

        // Send remaining to contract owner
        if (remaining > 0) {
            payable(owner()).transfer(remaining);
        }
    }

    /**
     * @dev Adds a new collaborator to a launch
     * @param launchId The ID of the launch
     * @param artist The address of the artist to add
     * @param royaltyPercentage The royalty percentage for the artist
     */
    function addCollaborator(
        uint256 launchId,
        address artist,
        uint256 royaltyPercentage
    ) external onlyOwner {
        require(launches[launchId].isActive, "Launch is not active");
        require(
            collaborations[launchId][artist].artistAddress == address(0),
            "Collaborator already exists"
        );

        collaborations[launchId][artist] = Collaboration({
            artistAddress: artist,
            royaltyPercentage: royaltyPercentage,
            isActive: true
        });

        launches[launchId].collaborators.push(artist);

        emit CollaborationAdded(launchId, artist, royaltyPercentage);
    }

    /**
     * @dev Removes a collaborator from a launch
     * @param launchId The ID of the launch
     * @param artist The address of the artist to remove
     */
    function removeCollaborator(uint256 launchId, address artist) external onlyOwner {
        require(launches[launchId].isActive, "Launch is not active");
        require(
            collaborations[launchId][artist].artistAddress != address(0),
            "Collaborator does not exist"
        );

        collaborations[launchId][artist].isActive = false;

        emit CollaborationRemoved(launchId, artist);
    }

    /**
     * @dev Toggles the active status of a launch
     * @param launchId The ID of the launch
     */
    function toggleLaunchStatus(uint256 launchId) external onlyOwner {
        launches[launchId].isActive = !launches[launchId].isActive;
    }

    /**
     * @dev Returns the token URI for a given token ID
     * @param tokenId The ID of the token
     * @return The token URI
     */
    function tokenURI(uint256 tokenId) public view override returns (string memory) {
        require(_exists(tokenId), "Token does not exist");
        
        // All tokens in a launch share the same metadata
        // You might want to modify this for per-token metadata
        for (uint256 i = 0; i < _launchIdCounter.current(); i++) {
            if (tokenId <= launches[i].totalMinted) {
                return launches[i].metadataURI;
            }
        }
        
        revert("Token not found in any launch");
    }
}
```
