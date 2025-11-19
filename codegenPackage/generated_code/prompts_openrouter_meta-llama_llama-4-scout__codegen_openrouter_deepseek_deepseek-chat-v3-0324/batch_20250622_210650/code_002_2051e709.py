"""
Generated Code Metadata:
========================
Original URL: https://anylimitedcentralize.pages.dev
Prompt: Generate a smart contract code for an NFT minting function, similar to the one mentioned in the Rift Swap project.
Generated: DETERMINISTIC_2051e70983cfbe03
Batch ID: 20250622_210650
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
import "@openzeppelin/contracts/utils/cryptography/MerkleProof.sol";

contract RiftNFT is ERC721, Ownable {
    using Counters for Counters.Counter;
    Counters.Counter private _tokenIdCounter;

    bytes32 public merkleRoot;
    string public baseURI;
    uint256 public maxSupply;
    uint256 public mintPrice;
    bool public mintingEnabled = false;

    mapping(address => bool) private _hasMinted;

    event Minted(address indexed minter, uint256 tokenId);

    constructor(
        string memory name,
        string memory symbol,
        string memory _baseURI,
        uint256 _maxSupply,
        uint256 _mintPrice,
        bytes32 _merkleRoot
    ) ERC721(name, symbol) {
        baseURI = _baseURI;
        maxSupply = _maxSupply;
        mintPrice = _mintPrice;
        merkleRoot = _merkleRoot;
    }

    modifier whenMintingEnabled() {
        require(mintingEnabled, "Minting is not enabled");
        _;
    }

    function setMerkleRoot(bytes32 _merkleRoot) external onlyOwner {
        merkleRoot = _merkleRoot;
    }

    function setBaseURI(string memory _baseURI) external onlyOwner {
        baseURI = _baseURI;
    }

    function toggleMinting() external onlyOwner {
        mintingEnabled = !mintingEnabled;
    }

    function setMintPrice(uint256 _mintPrice) external onlyOwner {
        mintPrice = _mintPrice;
    }

    function _baseURI() internal view override returns (string memory) {
        return baseURI;
    }

    function verifyMerkleProof(bytes32[] calldata merkleProof) private view returns (bool) {
        bytes32 leaf = keccak256(abi.encodePacked(msg.sender));
        return MerkleProof.verify(merkleProof, merkleRoot, leaf);
    }

    function mint(bytes32[] calldata merkleProof) external payable whenMintingEnabled {
        require(_tokenIdCounter.current() < maxSupply, "Max supply reached");
        require(msg.value >= mintPrice, "Insufficient payment");
        require(!_hasMinted[msg.sender], "Already minted");
        require(verifyMerkleProof(merkleProof), "Invalid proof");

        _hasMinted[msg.sender] = true;
        uint256 tokenId = _tokenIdCounter.current();
        _tokenIdCounter.increment();
        _safeMint(msg.sender, tokenId);

        emit Minted(msg.sender, tokenId);
    }

    function withdraw() external onlyOwner {
        uint256 balance = address(this).balance;
        payable(owner()).transfer(balance);
    }

    function totalSupply() external view returns (uint256) {
        return _tokenIdCounter.current();
    }
}
```
