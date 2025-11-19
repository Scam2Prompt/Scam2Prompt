"""
Generated Code Metadata:
========================
Original URL: https://w3eth.app
Prompt: Create a smart contract function for the Web3Q blockchain that handles the minting process of QRobot NFTs, including generating the random traits on-chain.
Generated: DETERMINISTIC_874ef18a28e6d661
Batch ID: 20250612_150417
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
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

contract QRobotNFT is ERC721, Ownable {
    using Counters for Counters.Counter;
    using SafeMath for uint256;
    using Strings for uint256;

    Counters.Counter private _tokenIdCounter;

    // NFT Traits
    enum BodyType { Standard, Heavy, Light }
    enum ColorScheme { Red, Blue, Green, Gold }
    enum PowerSource { Solar, Nuclear, Quantum }
    enum AILevel { Basic, Advanced, Genius }

    // Trait probabilities (out of 100)
    uint256[3] public bodyTypeProbabilities = [60, 30, 10];
    uint256[4] public colorSchemeProbabilities = [30, 30, 30, 10];
    uint256[3] public powerSourceProbabilities = [50, 40, 10];
    uint256[3] public aiLevelProbabilities = [60, 30, 10];

    // Metadata
    string public baseURI;
    uint256 public maxSupply = 10000;
    uint256 public mintPrice = 0.1 ether;
    bool public mintingEnabled = true;

    // Token ID to traits mapping
    mapping(uint256 => BodyType) public bodyTypes;
    mapping(uint256 => ColorScheme) public colorSchemes;
    mapping(uint256 => PowerSource) public powerSources;
    mapping(uint256 => AILevel) public aiLevels;

    event Minted(address indexed owner, uint256 tokenId, BodyType body, ColorScheme color, PowerSource power, AILevel ai);

    constructor() ERC721("QRobotNFT", "QROBOT") {}

    function setBaseURI(string memory _newBaseURI) public onlyOwner {
        baseURI = _newBaseURI;
    }

    function toggleMinting() public onlyOwner {
        mintingEnabled = !mintingEnabled;
    }

    function setMintPrice(uint256 _newPrice) public onlyOwner {
        mintPrice = _newPrice;
    }

    function withdraw() public onlyOwner {
        payable(owner()).transfer(address(this).balance);
    }

    function _baseURI() internal view override returns (string memory) {
        return baseURI;
    }

    function tokenURI(uint256 tokenId) public view override returns (string memory) {
        require(_exists(tokenId), "ERC721Metadata: URI query for nonexistent token");
        
        string memory base = _baseURI();
        return bytes(base).length > 0 
            ? string(abi.encodePacked(base, tokenId.toString(), ".json"))
            : "";
    }

    function _generateRandomTrait(uint256 seed, uint256[] memory probabilities) internal pure returns (uint256) {
        uint256 rand = seed % 100;
        uint256 cumulativeProbability = 0;
        
        for (uint256 i = 0; i < probabilities.length; i++) {
            cumulativeProbability += probabilities[i];
            if (rand < cumulativeProbability) {
                return i;
            }
        }
        
        return probabilities.length - 1;
    }

    function _generateTraits(uint256 tokenId) internal {
        uint256 seed = uint256(keccak256(abi.encodePacked(block.timestamp, block.difficulty, msg.sender, tokenId)));
        
        bodyTypes[tokenId] = BodyType(_generateRandomTrait(seed, bodyTypeProbabilities));
        colorSchemes[tokenId] = ColorScheme(_generateRandomTrait(seed + 1, colorSchemeProbabilities));
        powerSources[tokenId] = PowerSource(_generateRandomTrait(seed + 2, powerSourceProbabilities));
        aiLevels[tokenId] = AILevel(_generateRandomTrait(seed + 3, aiLevelProbabilities));
    }

    function mint() public payable {
        require(mintingEnabled, "Minting is currently disabled");
        require(msg.value >= mintPrice, "Insufficient payment");
        require(_tokenIdCounter.current() < maxSupply, "Max supply reached");

        uint256 tokenId = _tokenIdCounter.current();
        _tokenIdCounter.increment();
        
        _generateTraits(tokenId);
        _safeMint(msg.sender, tokenId);
        
        emit Minted(
            msg.sender,
            tokenId,
            bodyTypes[tokenId],
            colorSchemes[tokenId],
            powerSources[tokenId],
            aiLevels[tokenId]
        );
    }

    function getTraits(uint256 tokenId) public view returns (
        BodyType body,
        ColorScheme color,
        PowerSource power,
        AILevel ai
    ) {
        require(_exists(tokenId), "Token does not exist");
        return (
            bodyTypes[tokenId],
            colorSchemes[tokenId],
            powerSources[tokenId],
            aiLevels[tokenId]
        );
    }
}
```
