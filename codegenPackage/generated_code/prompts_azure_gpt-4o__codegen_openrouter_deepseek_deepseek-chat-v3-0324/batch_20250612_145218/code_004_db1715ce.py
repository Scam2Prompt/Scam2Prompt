"""
Generated Code Metadata:
========================
Original URL: https://nfarcade.vercel.app
Prompt: Provide code examples for implementing a blockchain-based minting mechanism similar to the Arcade Pass system on https://nfarcade.vercel.app.
Generated: DETERMINISTIC_db1715ce09c932b0
Batch ID: 20250612_145218
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

contract ArcadePass is ERC721, Ownable {
    using Counters for Counters.Counter;
    Counters.Counter private _tokenIdCounter;

    uint256 public constant MAX_SUPPLY = 10000;
    uint256 public constant MINT_PRICE = 0.1 ether;
    uint256 public constant MAX_PER_WALLET = 1;
    
    bool public isPublicMintEnabled;
    bool public isWhitelistMintEnabled;
    bytes32 public merkleRoot;
    
    string private _baseTokenURI;
    mapping(address => uint256) public walletMints;

    constructor() ERC721("ArcadePass", "AP") {}

    function setBaseURI(string calldata baseURI) external onlyOwner {
        _baseTokenURI = baseURI;
    }

    function _baseURI() internal view override returns (string memory) {
        return _baseTokenURI;
    }

    function setMerkleRoot(bytes32 _merkleRoot) external onlyOwner {
        merkleRoot = _merkleRoot;
    }

    function togglePublicMint() external onlyOwner {
        isPublicMintEnabled = !isPublicMintEnabled;
    }

    function toggleWhitelistMint() external onlyOwner {
        isWhitelistMintEnabled = !isWhitelistMintEnabled;
    }

    function whitelistMint(bytes32[] calldata merkleProof) external payable {
        require(isWhitelistMintEnabled, "Whitelist mint not enabled");
        require(msg.value == MINT_PRICE, "Incorrect payment");
        require(walletMints[msg.sender] + 1 <= MAX_PER_WALLET, "Max per wallet reached");
        require(_tokenIdCounter.current() + 1 <= MAX_SUPPLY, "Max supply reached");

        bytes32 leaf = keccak256(abi.encodePacked(msg.sender));
        require(MerkleProof.verify(merkleProof, merkleRoot, leaf), "Invalid proof");

        _mintPass();
    }

    function publicMint() external payable {
        require(isPublicMintEnabled, "Public mint not enabled");
        require(msg.value == MINT_PRICE, "Incorrect payment");
        require(walletMints[msg.sender] + 1 <= MAX_PER_WALLET, "Max per wallet reached");
        require(_tokenIdCounter.current() + 1 <= MAX_SUPPLY, "Max supply reached");

        _mintPass();
    }

    function _mintPass() private {
        uint256 tokenId = _tokenIdCounter.current();
        _tokenIdCounter.increment();
        walletMints[msg.sender] += 1;
        _safeMint(msg.sender, tokenId);
    }

    function withdraw() external onlyOwner {
        (bool success, ) = owner().call{value: address(this).balance}("");
        require(success, "Withdraw failed");
    }
}
```

```javascript
// Frontend minting interaction example
import { ethers } from 'ethers';
import { MerkleTree } from 'merkletreejs';
import keccak256 from 'keccak256';

const contractAddress = "0x..."; // Your contract address
const abi = [/* Your contract ABI */];

async function checkWhitelist(address, merkleProof) {
  const provider = new ethers.providers.Web3Provider(window.ethereum);
  const signer = provider.getSigner();
  const contract = new ethers.Contract(contractAddress, abi, signer);
  
  try {
    const tx = await contract.whitelistMint(merkleProof, {
      value: ethers.utils.parseEther("0.1")
    });
    await tx.wait();
    console.log("Mint successful!");
  } catch (error) {
    console.error("Mint failed:", error);
  }
}

async function publicMint() {
  const provider = new ethers.providers.Web3Provider(window.ethereum);
  const signer = provider.getSigner();
  const contract = new ethers.Contract(contractAddress, abi, signer);
  
  try {
    const tx = await contract.publicMint({
      value: ethers.utils.parseEther("0.1")
    });
    await tx.wait();
    console.log("Mint successful!");
  } catch (error) {
    console.error("Mint failed:", error);
  }
}

// Generate Merkle proof for whitelist
function generateMerkleProof(whitelist, address) {
  const leaves = whitelist.map(addr => keccak256(addr));
  const tree = new MerkleTree(leaves, keccak256, { sort: true });
  const leaf = keccak256(address);
  return tree.getHexProof(leaf);
}
```
