"""
Generated Code Metadata:
========================
Original URL: https://cornucopiasnfts.com
Prompt: Design a smart contract for a free minting event of NFTs, similar to the one offered by Cornucopias, using Solidity and OpenZeppelin libraries.
Generated: DETERMINISTIC_51cf30f1154924f9
Batch ID: 20250622_210718
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

contract FreeMintNFT is ERC721, Ownable {
    using Counters for Counters.Counter;
    Counters.Counter private _tokenIdCounter;

    uint256 public constant MAX_SUPPLY = 10000;
    uint256 public constant MAX_PER_WALLET = 1;
    uint256 public constant MINT_PRICE = 0 ether;
    
    bool public isMintingEnabled = false;
    bytes32 public merkleRoot;
    string public baseTokenURI;

    mapping(address => uint256) public mintedPerAddress;

    constructor(
        string memory name,
        string memory symbol,
        string memory _baseTokenURI,
        bytes32 _merkleRoot
    ) ERC721(name, symbol) {
        baseTokenURI = _baseTokenURI;
        merkleRoot = _merkleRoot;
    }

    function _baseURI() internal view override returns (string memory) {
        return baseTokenURI;
    }

    function setBaseURI(string memory _baseTokenURI) external onlyOwner {
        baseTokenURI = _baseTokenURI;
    }

    function setMerkleRoot(bytes32 _merkleRoot) external onlyOwner {
        merkleRoot = _merkleRoot;
    }

    function toggleMinting() external onlyOwner {
        isMintingEnabled = !isMintingEnabled;
    }

    function freeMint(bytes32[] calldata merkleProof) external {
        require(isMintingEnabled, "Minting is not enabled");
        require(_tokenIdCounter.current() < MAX_SUPPLY, "Max supply reached");
        require(mintedPerAddress[msg.sender] < MAX_PER_WALLET, "Max per wallet reached");
        require(msg.value == MINT_PRICE, "Incorrect ETH amount");

        // Verify Merkle Proof
        bytes32 leaf = keccak256(abi.encodePacked(msg.sender));
        require(MerkleProof.verify(merkleProof, merkleRoot, leaf), "Invalid proof");

        mintedPerAddress[msg.sender] += 1;
        _safeMint(msg.sender, _tokenIdCounter.current());
        _tokenIdCounter.increment();
    }

    function withdraw() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No funds to withdraw");
        payable(owner()).transfer(balance);
    }

    function totalSupply() external view returns (uint256) {
        return _tokenIdCounter.current();
    }
}
```
