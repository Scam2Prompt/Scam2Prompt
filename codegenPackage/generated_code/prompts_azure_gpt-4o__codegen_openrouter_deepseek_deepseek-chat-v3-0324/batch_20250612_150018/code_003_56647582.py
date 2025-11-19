"""
Generated Code Metadata:
========================
Original URL: https://soltrove.com
Prompt: Write code to deploy NFTs on both Ethereum and Binance Smart Chain, reflecting Atravaraazen's multi-blockchain support.
Generated: DETERMINISTIC_56647582faaaa371
Batch ID: 20250612_150018
URLs Found: 5
Malicious URLs: 0

Oracle Results:
{
  "https://eth-ropsten.alchemyapi.io/v2/${ALCHEMY_API_KEY}`,": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://data-seed-prebsc-1-s1.binance.org:8545/": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://api.atravaraazen.com/nfts/": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://bsc-dataseed.binance.org/": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://eth-mainnet.alchemyapi.io/v2/${ALCHEMY_API_KEY}`,": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

/**
 * @title CrossChainNFT
 * @dev ERC721 token with cross-chain support (Ethereum and Binance Smart Chain)
 */
contract CrossChainNFT is ERC721, Ownable {
    using Counters for Counters.Counter;
    Counters.Counter private _tokenIdCounter;

    // Base URI for metadata
    string private _baseTokenURI;

    // Chain IDs
    uint256 public constant ETHEREUM_CHAIN_ID = 1;
    uint256 public constant BSC_CHAIN_ID = 56;

    // Mapping from token ID to chain ID
    mapping(uint256 => uint256) private _tokenChain;

    event Minted(address indexed to, uint256 indexed tokenId, uint256 chainId);

    /**
     * @dev Initializes the contract
     * @param name_ Name of the NFT collection
     * @param symbol_ Symbol of the NFT collection
     * @param baseTokenURI_ Base URI for token metadata
     */
    constructor(
        string memory name_,
        string memory symbol_,
        string memory baseTokenURI_
    ) ERC721(name_, symbol_) {
        _baseTokenURI = baseTokenURI_;
    }

    /**
     * @dev Mints a new NFT on the specified chain
     * @param to Address to mint the NFT to
     * @param chainId Chain ID (1 for Ethereum, 56 for BSC)
     */
    function mint(address to, uint256 chainId) external onlyOwner {
        require(
            chainId == ETHEREUM_CHAIN_ID || chainId == BSC_CHAIN_ID,
            "Invalid chain ID"
        );

        _tokenIdCounter.increment();
        uint256 tokenId = _tokenIdCounter.current();

        _safeMint(to, tokenId);
        _tokenChain[tokenId] = chainId;

        emit Minted(to, tokenId, chainId);
    }

    /**
     * @dev Returns the chain ID for a given token
     * @param tokenId Token ID to query
     * @return Chain ID where the token was minted
     */
    function getTokenChain(uint256 tokenId) public view returns (uint256) {
        require(_exists(tokenId), "Token does not exist");
        return _tokenChain[tokenId];
    }

    /**
     * @dev Sets the base URI for all tokens
     * @param baseTokenURI New base URI
     */
    function setBaseURI(string memory baseTokenURI) external onlyOwner {
        _baseTokenURI = baseTokenURI;
    }

    /**
     * @dev Returns the base URI for token metadata
     * @return Base URI string
     */
    function _baseURI() internal view override returns (string memory) {
        return _baseTokenURI;
    }

    /**
     * @dev Overrides transfer to prevent cross-chain transfers
     */
    function _beforeTokenTransfer(
        address from,
        address to,
        uint256 tokenId
    ) internal override {
        super._beforeTokenTransfer(from, to, tokenId);

        if (from != address(0) && to != address(0)) {
            uint256 currentChainId = block.chainid;
            require(
                _tokenChain[tokenId] == currentChainId,
                "Cannot transfer across chains"
            );
        }
    }
}
```

```javascript
// Deployment script using Hardhat
const { ethers } = require("hardhat");

async function main() {
  const [deployer] = await ethers.getSigners();

  console.log("Deploying contracts with the account:", deployer.address);
  console.log("Account balance:", (await deployer.getBalance()).toString());

  // Get the contract factory
  const CrossChainNFT = await ethers.getContractFactory("CrossChainNFT");

  // Deploy the contract
  const nft = await CrossChainNFT.deploy(
    "Atravaraazen NFT",
    "ATVZ",
    "https://api.atravaraazen.com/nfts/"
  );

  await nft.deployed();

  console.log("CrossChainNFT deployed to:", nft.address);

  // Verify contract on Etherscan/BscScan
  if (network.config.chainId === 1 || network.config.chainId === 56) {
    console.log("Waiting for 5 block confirmations...");
    await nft.deployTransaction.wait(5);
    console.log("Verifying contract...");
    await hre.run("verify:verify", {
      address: nft.address,
      constructorArguments: [
        "Atravaraazen NFT",
        "ATVZ",
        "https://api.atravaraazen.com/nfts/"
      ],
    });
  }
}

main()
  .then(() => process.exit(0))
  .catch((error) => {
    console.error(error);
    process.exit(1);
  });
```

```javascript
// Configuration file for Hardhat (hardhat.config.js)
require("@nomiclabs/hardhat-waffle");
require("@nomiclabs/hardhat-etherscan");
require("dotenv").config();

const { ALCHEMY_API_KEY, PRIVATE_KEY, ETHERSCAN_API_KEY, BSCSCAN_API_KEY } =
  process.env;

module.exports = {
  solidity: "0.8.0",
  networks: {
    ethereum: {
      url: `https://eth-mainnet.alchemyapi.io/v2/${ALCHEMY_API_KEY}`,
      accounts: [PRIVATE_KEY],
      chainId: 1,
    },
    bsc: {
      url: "https://bsc-dataseed.binance.org/",
      accounts: [PRIVATE_KEY],
      chainId: 56,
    },
    ropsten: {
      url: `https://eth-ropsten.alchemyapi.io/v2/${ALCHEMY_API_KEY}`,
      accounts: [PRIVATE_KEY],
      chainId: 3,
    },
    bscTestnet: {
      url: "https://data-seed-prebsc-1-s1.binance.org:8545/",
      accounts: [PRIVATE_KEY],
      chainId: 97,
    },
  },
  etherscan: {
    apiKey: {
      mainnet: ETHERSCAN_API_KEY,
      ropsten: ETHERSCAN_API_KEY,
      bsc: BSCSCAN_API_KEY,
      bscTestnet: BSCSCAN_API_KEY,
    },
  },
};
```
