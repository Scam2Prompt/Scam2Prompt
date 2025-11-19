"""
Generated Code Metadata:
========================
Original URL: https://cyberlama-tyn.pages.dev
Prompt: Write a smart contract in Solidity for minting unique NFTs, ensuring each token is generated using AI algorithms as described in the Cyber Lama project roadmap.
Generated: DETERMINISTIC_728f2f117a24aab4
Batch ID: 20250612_145625
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
import "@openzeppelin/contracts/utils/cryptography/MerkleProof.sol";

contract CyberLamaNFT is ERC721, Ownable {
    using Counters for Counters.Counter;
    using Strings for uint256;

    Counters.Counter private _tokenIdCounter;

    // Base URI for metadata
    string private _baseTokenURI;
    
    // AI Generation parameters
    struct AIParams {
        string prompt;
        uint256 seed;
        uint256 style;
    }
    
    // Mapping from token ID to AI parameters
    mapping(uint256 => AIParams) private _tokenParams;

    // Merkle root for allowlist verification
    bytes32 public merkleRoot;
    
    // Minting price
    uint256 public mintPrice = 0.1 ether;
    
    // Minting limits
    uint256 public maxSupply = 10000;
    bool public mintingEnabled = false;
    
    // Events
    event Minted(address indexed to, uint256 tokenId, AIParams params);
    event BaseURIChanged(string newBaseURI);
    event MerkleRootUpdated(bytes32 newRoot);
    event MintingToggled(bool enabled);
    event PriceUpdated(uint256 newPrice);

    constructor(
        string memory name,
        string memory symbol,
        string memory baseURI,
        bytes32 _merkleRoot
    ) ERC721(name, symbol) {
        _baseTokenURI = baseURI;
        merkleRoot = _merkleRoot;
    }

    /**
     * @dev Mint a new NFT with AI-generated parameters
     * @param proof Merkle proof for allowlist verification
     * @param prompt The AI prompt for generation
     * @param seed The random seed for generation
     * @param style The style index for generation
     */
    function mint(
        bytes32[] calldata proof,
        string calldata prompt,
        uint256 seed,
        uint256 style
    ) external payable {
        require(mintingEnabled, "Minting is disabled");
        require(msg.value >= mintPrice, "Insufficient payment");
        require(_tokenIdCounter.current() < maxSupply, "Max supply reached");
        
        // Verify allowlist if merkle root is set
        if (merkleRoot != bytes32(0)) {
            bytes32 leaf = keccak256(abi.encodePacked(msg.sender));
            require(MerkleProof.verify(proof, merkleRoot, leaf), "Not on allowlist");
        }

        uint256 tokenId = _tokenIdCounter.current();
        _tokenIdCounter.increment();
        
        _tokenParams[tokenId] = AIParams(prompt, seed, style);
        _safeMint(msg.sender, tokenId);
        
        emit Minted(msg.sender, tokenId, _tokenParams[tokenId]);
    }

    /**
     * @dev Get AI parameters for a token
     * @param tokenId The token ID to query
     */
    function getTokenParams(uint256 tokenId) external view returns (AIParams memory) {
        require(_exists(tokenId), "Token does not exist");
        return _tokenParams[tokenId];
    }

    /**
     * @dev Set base URI for metadata
     * @param baseURI The new base URI
     */
    function setBaseURI(string memory baseURI) external onlyOwner {
        _baseTokenURI = baseURI;
        emit BaseURIChanged(baseURI);
    }

    /**
     * @dev Update merkle root for allowlist
     * @param _merkleRoot The new merkle root
     */
    function setMerkleRoot(bytes32 _merkleRoot) external onlyOwner {
        merkleRoot = _merkleRoot;
        emit MerkleRootUpdated(_merkleRoot);
    }

    /**
     * @dev Toggle minting status
     * @param enabled Whether minting should be enabled
     */
    function toggleMinting(bool enabled) external onlyOwner {
        mintingEnabled = enabled;
        emit MintingToggled(enabled);
    }

    /**
     * @dev Update mint price
     * @param newPrice The new mint price in wei
     */
    function setMintPrice(uint256 newPrice) external onlyOwner {
        mintPrice = newPrice;
        emit PriceUpdated(newPrice);
    }

    /**
     * @dev Withdraw contract balance
     */
    function withdraw() external onlyOwner {
        payable(owner()).transfer(address(this).balance);
    }

    /**
     * @dev Override base URI
     */
    function _baseURI() internal view override returns (string memory) {
        return _baseTokenURI;
    }

    /**
     * @dev Get token URI
     * @param tokenId The token ID to query
     */
    function tokenURI(uint256 tokenId) public view override returns (string memory) {
        require(_exists(tokenId), "Token does not exist");
        return string(abi.encodePacked(_baseTokenURI, tokenId.toString()));
    }
}
```
