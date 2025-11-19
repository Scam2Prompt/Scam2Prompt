"""
Generated Code Metadata:
========================
Original URL: https://mintlama.pages.dev
Prompt: Generate code for testing and securing smart contracts for an NFT collection, ensuring compliance with the Cyber Lama roadmap's Phase 2 requirements.
Generated: DETERMINISTIC_3bcfd97360c5224c
Batch ID: 20250612_152235
URLs Found: 3
Malicious URLs: 0

Oracle Results:
{
  "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/math/SafeMath.sol": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://example.com/nft/": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/token/ERC721/SafeERC721.sol": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```javascript
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/token/ERC721/SafeERC721.sol";
import "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/math/SafeMath.sol";

/**
 * @title CyberLamaNFT
 * @author [Your Name]
 * @notice NFT contract for Cyber Lama collection
 */
contract CyberLamaNFT {
    using SafeMath for uint256;
    using SafeERC721 for mapping(address => uint256);

    // Mapping of NFT owners
    mapping(address => uint256) private _balances;

    // Mapping of NFT token IDs to owners
    mapping(uint256 => address) private _owners;

    // Mapping of NFT token IDs to URIs
    mapping(uint256 => string) private _tokenURIs;

    // Total supply of NFTs
    uint256 private _totalSupply;

    // Cyber Lama roadmap Phase 2 requirements
    // 1. Max supply: 1000
    // 2. Max mint per tx: 5
    // 3. Minting fee: 0.1 ETH

    uint256 public constant MAX_SUPPLY = 1000;
    uint256 public constant MAX_MINT_PER_TX = 5;
    uint256 public constant MINTING_FEE = 0.1 ether;

    /**
     * @dev Initializes the contract
     */
    constructor() public {
        _totalSupply = 0;
    }

    /**
     * @dev Mints new NFTs
     * @param _amount Number of NFTs to mint
     */
    function mint(uint256 _amount) public payable {
        require(_amount > 0, "Invalid mint amount");
        require(_amount <= MAX_MINT_PER_TX, "Exceeds max mint per tx");
        require(_totalSupply.add(_amount) <= MAX_SUPPLY, "Exceeds max supply");
        require(msg.value >= MINTING_FEE.mul(_amount), "Insufficient minting fee");

        for (uint256 i = 0; i < _amount; i++) {
            _totalSupply = _totalSupply.add(1);
            uint256 tokenId = _totalSupply;
            _owners[tokenId] = msg.sender;
            _balances[msg.sender] = _balances[msg.sender].add(1);
            _tokenURIs[tokenId] = string(abi.encodePacked("https://example.com/nft/", tokenId));
        }
    }

    /**
     * @dev Transfers NFT ownership
     * @param _to New owner address
     * @param _tokenId Token ID to transfer
     */
    function transfer(address _to, uint256 _tokenId) public {
        require(_owners[_tokenId] == msg.sender, "Only owner can transfer");
        require(_to != address(0), "Invalid recipient");

        _balances[msg.sender] = _balances[msg.sender].sub(1);
        _balances[_to] = _balances[_to].add(1);
        _owners[_tokenId] = _to;
    }

    /**
     * @dev Gets NFT owner
     * @param _tokenId Token ID
     * @return Owner address
     */
    function ownerOf(uint256 _tokenId) public view returns (address) {
        return _owners[_tokenId];
    }

    /**
     * @dev Gets NFT URI
     * @param _tokenId Token ID
     * @return URI string
     */
    function tokenURI(uint256 _tokenId) public view returns (string memory) {
        return _tokenURIs[_tokenId];
    }

    /**
     * @dev Gets NFT balance
     * @param _owner Owner address
     * @return Balance
     */
    function balanceOf(address _owner) public view returns (uint256) {
        return _balances[_owner];
    }
}

// Testing contract
contract CyberLamaNFTTest {
    CyberLamaNFT public nft;

    constructor() public {
        nft = new CyberLamaNFT();
    }

    function testMint() public {
        uint256 amount = 5;
        uint256 fee = CyberLamaNFT(nft).MINTING_FEE().mul(amount);
        (bool sent, ) = address(nft).call{value: fee}("");
        require(sent, "Failed to send ether");
        nft.mint(amount);
        assert(nft.balanceOf(address(this)) == amount);
    }

    function testTransfer() public {
        uint256 amount = 1;
        uint256 fee = CyberLamaNFT(nft).MINTING_FEE().mul(amount);
        (bool sent, ) = address(nft).call{value: fee}("");
        require(sent, "Failed to send ether");
        nft.mint(amount);
        address recipient = address(0x123);
        nft.transfer(recipient, 1);
        assert(nft.ownerOf(1) == recipient);
    }
}
```
