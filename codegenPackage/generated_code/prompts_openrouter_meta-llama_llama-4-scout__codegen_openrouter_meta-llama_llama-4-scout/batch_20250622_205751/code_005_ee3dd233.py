"""
Generated Code Metadata:
========================
Original URL: https://bafybeifz6nktfsjqwtgvkmqhhxq7gbbwsna6c7btv5idl443akekg4lmjy.ipfs.dweb.link
Prompt: "Write a tutorial on how to build a dynamic NFT using three Chainlink services, including data feeds, VRF, and automation."
Generated: DETERMINISTIC_ee3dd233b956143b
Batch ID: 20250622_205751
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://mainnet.infura.io/v3/YOUR_PROJECT_ID": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://example.com/token/": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

Here is the code for the dynamic NFT using three Chainlink services:

**DynamicNFT.sol**
```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@chainlink/contracts/src/v0.8/interfaces/AggregatorV3Interface.sol";
import "@chainlink/contracts/src/v0.8/VRFCoordinatorV2Interface.sol";
import "@chainlink/contracts/src/v0.8/KeeperCompatible.sol";

contract DynamicNFT is KeeperCompatible, VRFConsumerBase {
    // Data feed for ETH price
    AggregatorV3Interface internal ethPriceFeed;

    // VRF Coordinator
    VRFCoordinatorV2Interface internal vrfCoordinator;

    // Mapping of token IDs to their metadata
    mapping(uint256 => TokenMetadata) public tokenMetadata;

    // Struct to hold token metadata
    struct TokenMetadata {
        uint256 randomNumber;
        uint256 ethPrice;
        string tokenURI;
    }

    // Event emitted when token metadata is updated
    event TokenMetadataUpdated(uint256 indexed tokenId, uint256 randomNumber, uint256 ethPrice);

    // Constructor
    constructor(
        address _ethPriceFeed,
        address _vrfCoordinator,
        bytes32 _keyHash,
        uint64 _subscriptionId
    )
        VRFConsumerBase(_vrfCoordinator, _keyHash, _subscriptionId)
    {
        ethPriceFeed = AggregatorV3Interface(_ethPriceFeed);
        vrfCoordinator = VRFCoordinatorV2Interface(_vrfCoordinator);
    }

    // Function to get ETH price from data feed
    function getEthPrice() public view returns (uint256) {
        (, int256 price, , , ) = ethPriceFeed.latestRoundData();
        return uint256(price * 10**10); // 18 decimals
    }

    // Function to request random number from VRF
    function requestRandomNumber() public {
        vrfCoordinator.requestRandomness(
            subscriptionId,
            keyHash,
            300000
        );
    }

    // Callback function for VRF random number
    function fulfillRandomness(bytes32 requestId, uint256 randomNumber) internal override {
        // Update token metadata with random number and ETH price
        uint256 tokenId = 1; // Replace with actual token ID
        tokenMetadata[tokenId].randomNumber = randomNumber;
        tokenMetadata[tokenId].ethPrice = getEthPrice();
        tokenMetadata[tokenId].tokenURI = string(abi.encodePacked("https://example.com/token/", tokenId));

        emit TokenMetadataUpdated(tokenId, randomNumber, getEthPrice());
    }

    // Keeper-compatible function to update token metadata
    function checkUpkeep(
        bytes calldata /* checkData */
    ) external override returns (bool upkeepNeeded, bytes memory /* performData */) {
        // Check if token metadata needs to be updated
        upkeepNeeded = true;
    }

    // Keeper-compatible function to perform token metadata update
    function performUpkeep(
        bytes calldata /* performData */
    ) external override {
        // Update token metadata
        requestRandomNumber();
    }
}
```

**DynamicNFTConsumer.js**
```javascript
const { ethers } = require("hardhat");
const { expect } = require("chai");

describe("DynamicNFT", function () {
    let dynamicNFT;

    beforeEach(async function () {
        const EthPriceFeed = await ethers.getContractFactory("MockAggregatorV3Interface");
        const ethPriceFeed = await EthPriceFeed.deploy();

        const VRFCoordinator = await ethers.getContractFactory("MockVRFCoordinatorV2Interface");
        const vrfCoordinator = await VRFCoordinator.deploy();

        const DynamicNFT = await ethers.getContractFactory("DynamicNFT");
        dynamicNFT = await DynamicNFT.deploy(
            ethPriceFeed.address,
            vrfCoordinator.address,
            "0x...keyHash...",
            123 // subscription ID
        );
    });

    it("should get ETH price from data feed", async function () {
        const ethPrice = await dynamicNFT.getEthPrice();
        expect(ethPrice).to.be.a("number");
    });

    it("should request random number from VRF", async function () {
        await dynamicNFT.requestRandomNumber();
        const requestId = await dynamicNFT.getRequestId();
        expect(requestId).to.be.a("string");
    });

    it("should update token metadata", async function () {
        await dynamicNFT.requestRandomNumber();
        const tokenId = 1;
        const tokenMetadata = await dynamicNFT.tokenMetadata(tokenId);
        expect(tokenMetadata.randomNumber).to.be.a("number");
        expect(tokenMetadata.ethPrice).to.be.a("number");
        expect(tokenMetadata.tokenURI).to.be.a("string");
    });
});
```

**hardhat.config.js**
```javascript
require("@nomiclabs/hardhat-ethers");
require("@nomiclabs/hardhat-waffle");
require("@chainlink/hardhat-chainlink");

module.exports = {
    solidity: "0.8.10",
    networks: {
        hardhat: {
            chainId: 31337,
            forking: {
                url: "https://mainnet.infura.io/v3/YOUR_PROJECT_ID",
            },
        },
    },
    chainlink: {
        aggregator: {
            address: "0x...AggregatorV3Interface...",
            abi: "@chainlink/contracts/src/v0.8/interfaces/AggregatorV3Interface.json",
        },
        vrf: {
            coordinator: {
                address: "0x...VRFCoordinatorV2Interface...",
                abi: "@chainlink/contracts/src/v0.8/VRFCoordinatorV2Interface.json",
            },
            keyHash: "0x...keyHash...",
            subscriptionId: 123,
        },
    },
};
```
