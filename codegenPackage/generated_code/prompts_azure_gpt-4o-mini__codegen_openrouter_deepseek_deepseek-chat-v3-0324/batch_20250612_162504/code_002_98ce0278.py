"""
Generated Code Metadata:
========================
Original URL: https://sportnode.nl
Prompt: Write a dApp that allows athletes to interact with fans, incorporating the development strategies mentioned on Sportnode's website.
Generated: DETERMINISTIC_98ce02789fa74f4b
Batch ID: 20250612_162504
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
import "@openzeppelin/contracts/utils/Strings.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

/**
 * @title SportNodeAthleteToken
 * @dev A dApp that allows athletes to interact with fans through NFTs
 */
contract SportNodeAthleteToken is ERC721, Ownable, ReentrancyGuard {
    using Counters for Counters.Counter;
    using Strings for uint256;

    // Token counter
    Counters.Counter private _tokenIdCounter;

    // Base URI for metadata
    string private _baseTokenURI;

    // Athlete information
    struct Athlete {
        address walletAddress;
        string name;
        string sport;
        bool isVerified;
    }

    // Fan interaction types
    enum InteractionType {
        Message,
        VideoCall,
        MeetAndGreet
    }

    // Interaction details
    struct Interaction {
        uint256 tokenId;
        InteractionType interactionType;
        uint256 price;
        bool isActive;
    }

    // Mapping from token ID to athlete
    mapping(uint256 => Athlete) private _athletes;

    // Mapping from token ID to interactions
    mapping(uint256 => Interaction[]) private _interactions;

    // Mapping from token ID to owner
    mapping(uint256 => address) private _tokenOwners;

    // Events
    event AthleteRegistered(uint256 indexed tokenId, address indexed athleteWallet, string name, string sport);
    event InteractionCreated(uint256 indexed tokenId, InteractionType interactionType, uint256 price);
    event InteractionPurchased(uint256 indexed tokenId, address indexed fanAddress, InteractionType interactionType);

    /**
     * @dev Constructor
     * @param name_ Name of the token
     * @param symbol_ Symbol of the token
     * @param baseTokenURI_ Base URI for metadata
     */
    constructor(
        string memory name_,
        string memory symbol_,
        string memory baseTokenURI_
    ) ERC721(name_, symbol_) {
        _baseTokenURI = baseTokenURI_;
    }

    /**
     * @dev Register a new athlete
     * @param name Athlete's name
     * @param sport Athlete's sport
     */
    function registerAthlete(string memory name, string memory sport) external {
        require(bytes(name).length > 0, "Name cannot be empty");
        require(bytes(sport).length > 0, "Sport cannot be empty");

        _tokenIdCounter.increment();
        uint256 tokenId = _tokenIdCounter.current();

        _mint(msg.sender, tokenId);
        
        _athletes[tokenId] = Athlete({
            walletAddress: msg.sender,
            name: name,
            sport: sport,
            isVerified: false
        });

        _tokenOwners[tokenId] = msg.sender;

        emit AthleteRegistered(tokenId, msg.sender, name, sport);
    }

    /**
     * @dev Verify an athlete (only owner)
     * @param tokenId Token ID of the athlete
     */
    function verifyAthlete(uint256 tokenId) external onlyOwner {
        require(_exists(tokenId), "Athlete does not exist");
        _athletes[tokenId].isVerified = true;
    }

    /**
     * @dev Create a new interaction for fans
     * @param tokenId Token ID of the athlete
     * @param interactionType Type of interaction
     * @param price Price for the interaction
     */
    function createInteraction(
        uint256 tokenId,
        InteractionType interactionType,
        uint256 price
    ) external {
        require(_exists(tokenId), "Athlete does not exist");
        require(_tokenOwners[tokenId] == msg.sender, "Only athlete can create interactions");
        require(price > 0, "Price must be greater than 0");

        _interactions[tokenId].push(Interaction({
            tokenId: tokenId,
            interactionType: interactionType,
            price: price,
            isActive: true
        }));

        emit InteractionCreated(tokenId, interactionType, price);
    }

    /**
     * @dev Purchase an interaction
     * @param tokenId Token ID of the athlete
     * @param interactionIndex Index of the interaction
     */
    function purchaseInteraction(uint256 tokenId, uint256 interactionIndex) external payable nonReentrant {
        require(_exists(tokenId), "Athlete does not exist");
        require(interactionIndex < _interactions[tokenId].length, "Invalid interaction index");
        
        Interaction storage interaction = _interactions[tokenId][interactionIndex];
        require(interaction.isActive, "Interaction is not active");
        require(msg.value >= interaction.price, "Insufficient payment");

        address athleteAddress = _tokenOwners[tokenId];
        payable(athleteAddress).transfer(msg.value);

        emit InteractionPurchased(tokenId, msg.sender, interaction.interactionType);
    }

    /**
     * @dev Get athlete information
     * @param tokenId Token ID of the athlete
     */
    function getAthlete(uint256 tokenId) external view returns (Athlete memory) {
        require(_exists(tokenId), "Athlete does not exist");
        return _athletes[tokenId];
    }

    /**
     * @dev Get interactions for an athlete
     * @param tokenId Token ID of the athlete
     */
    function getInteractions(uint256 tokenId) external view returns (Interaction[] memory) {
        require(_exists(tokenId), "Athlete does not exist");
        return _interactions[tokenId];
    }

    /**
     * @dev Set base URI for metadata
     * @param baseURI New base URI
     */
    function setBaseURI(string memory baseURI) external onlyOwner {
        _baseTokenURI = baseURI;
    }

    /**
     * @dev Get base URI
     */
    function _baseURI() internal view override returns (string memory) {
        return _baseTokenURI;
    }

    /**
     * @dev Check if token exists
     * @param tokenId Token ID to check
     */
    function _exists(uint256 tokenId) internal view returns (bool) {
        return _tokenOwners[tokenId] != address(0);
    }
}
```
