"""
Generated Code Metadata:
========================
Original URL: https://studio-git-scott-dashboard-update-metaplex.vercel.app
Prompt: Write a script using the Truffle API to mint an NFT titled "Golden Pig" with metadata and cost optimization features.
Generated: DETERMINISTIC_1c6958cfc3acca28
Batch ID: 20250612_152358
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721URIStorage.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

contract GoldenPigNFT is ERC721, ERC721URIStorage, Ownable {
    using Counters for Counters.Counter;
    Counters.Counter private _tokenIdCounter;

    // Cost optimization: Packed variables
    struct MintConfig {
        uint256 maxSupply;
        uint256 mintPrice;
        bool mintingEnabled;
    }
    MintConfig public config;

    event NFTMinted(address indexed recipient, uint256 tokenId, string tokenURI);

    constructor(
        string memory _name,
        string memory _symbol,
        uint256 _maxSupply,
        uint256 _mintPrice
    ) ERC721(_name, _symbol) {
        config = MintConfig({
            maxSupply: _maxSupply,
            mintPrice: _mintPrice,
            mintingEnabled: true
        });
    }

    function safeMint(address to, string memory uri) public payable {
        require(config.mintingEnabled, "Minting is disabled");
        require(msg.value >= config.mintPrice, "Insufficient payment");
        require(_tokenIdCounter.current() < config.maxSupply, "Max supply reached");

        uint256 tokenId = _tokenIdCounter.current();
        _tokenIdCounter.increment();
        _safeMint(to, tokenId);
        _setTokenURI(tokenId, uri);

        emit NFTMinted(to, tokenId, uri);
    }

    // Cost optimization: Batch token URI updates
    function batchSetTokenURI(
        uint256[] memory tokenIds,
        string[] memory uris
    ) public onlyOwner {
        require(tokenIds.length == uris.length, "Arrays length mismatch");
        for (uint256 i = 0; i < tokenIds.length; i++) {
            _setTokenURI(tokenIds[i], uris[i]);
        }
    }

    function toggleMinting() public onlyOwner {
        config.mintingEnabled = !config.mintingEnabled;
    }

    function updateMintPrice(uint256 newPrice) public onlyOwner {
        config.mintPrice = newPrice;
    }

    function withdraw() public onlyOwner {
        payable(owner()).transfer(address(this).balance);
    }

    // The following functions are overrides required by Solidity.
    function _burn(uint256 tokenId) internal override(ERC721, ERC721URIStorage) {
        super._burn(tokenId);
    }

    function tokenURI(uint256 tokenId)
        public
        view
        override(ERC721, ERC721URIStorage)
        returns (string memory)
    {
        return super.tokenURI(tokenId);
    }

    function supportsInterface(bytes4 interfaceId)
        public
        view
        override(ERC721, ERC721URIStorage)
        returns (bool)
    {
        return super.supportsInterface(interfaceId);
    }
}
```

```javascript
// truffle-config.js
module.exports = {
  networks: {
    development: {
      host: "127.0.0.1",
      port: 7545,
      network_id: "*",
    },
  },
  compilers: {
    solc: {
      version: "0.8.0",
      settings: {
        optimizer: {
          enabled: true,
          runs: 200,
        },
      },
    },
  },
};
```

```javascript
// scripts/mint.js
const GoldenPigNFT = artifacts.require("GoldenPigNFT");

module.exports = async function (deployer, network, accounts) {
  // Deploy contract
  await deployer.deploy(
    GoldenPigNFT,
    "Golden Pig NFT",
    "GPNFT",
    1000, // max supply
    web3.utils.toWei("0.01", "ether") // mint price
  );

  const instance = await GoldenPigNFT.deployed();
  const owner = accounts[0];
  const recipient = accounts[1];

  // Mint NFT with metadata
  const metadataURI = "ipfs://QmXJZx.../golden-pig.json";
  await instance.safeMint(recipient, metadataURI, {
    from: recipient,
    value: web3.utils.toWei("0.01", "ether"),
  });

  console.log(`NFT minted to ${recipient} with URI: ${metadataURI}`);
};
```
