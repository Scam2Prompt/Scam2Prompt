"""
Generated Code Metadata:
========================
Original URL: https://bafybeifz6nktfsjqwtgvkmqhhxq7gbbwsna6c7btv5idl443akekg4lmjy.ipfs.dweb.link
Prompt: "Write a tutorial on how to build a dynamic NFT using three Chainlink services, including data feeds, VRF, and automation."
Generated: DETERMINISTIC_ee3dd233b956143b
Batch ID: 20250622_205751
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

// Importing necessary Chainlink contracts
import "@chainlink/contracts/src/v0.8/VRFConsumerBase.sol";
import "@chainlink/contracts/src/v0.8/interfaces/AggregatorV3Interface.sol";
import "@chainlink/contracts/src/v0.8/AutomationCompatible.sol";

contract DynamicNFT is VRFConsumerBase, AutomationCompatible {
    // State variables
    uint256 public tokenId;
    string public baseURI;
    AggregatorV3Interface internal priceFeed;
    bytes32 internal keyHash;
    uint256 internal fee;
    uint256 public randomResult;

    // Event to emit when a new NFT is minted
    event NFTMinted(uint256 indexed tokenId, string tokenURI);

    // Constructor to initialize the contract
    constructor(
        address _vrfCoordinator,
        address _link,
        address _priceFeed,
        bytes32 _keyHash,
        uint256 _fee,
        string memory _baseURI
    ) 
        VRFConsumerBase(_vrfCoordinator, _link) 
    {
        priceFeed = AggregatorV3Interface(_priceFeed);
        keyHash = _keyHash;
        fee = _fee;
        baseURI = _baseURI;
    }

    // Function to mint a new NFT
    function mintNFT() external returns (uint256) {
        require(LINK.balanceOf(address(this)) >= fee, "Not enough LINK to pay fee");
        // Request a random number from Chainlink VRF
        requestRandomness(keyHash, fee);
        return tokenId;
    }

    // Callback function used by VRF Coordinator
    function fulfillRandomness(bytes32 requestId, uint256 randomness) internal override {
        randomResult = randomness;
        // Create a new NFT with the random result
        string memory tokenURI = string(abi.encodePacked(baseURI, uint2str(randomResult)));
        emit NFTMinted(tokenId, tokenURI);
        tokenId++;
    }

    // Function to convert uint to string
    function uint2str(uint256 _i) internal pure returns (string memory str) {
        if (_i == 0) {
            return "0";
        }
        uint256 j = _i;
        uint256 len;
        while (j != 0) {
            len++;
            j /= 10;
        }
        bytes memory bstr = new bytes(len);
        uint256 k = len;
        while (_i != 0) {
            bstr[--k] = bytes1(uint8(48 + _i % 10));
            _i /= 10;
        }
        return string(bstr);
    }

    // Function to check if the NFT can be updated based on price feed
    function checkUpkeep(bytes calldata /* checkData */) external view override returns (bool upkeepNeeded, bytes memory /* performData */) {
        // Example condition: upkeep needed if price changes significantly
        (, int price, , ,) = priceFeed.latestRoundData();
        upkeepNeeded = (uint256(price) % 10) == 0; // Example condition
    }

    // Function to perform upkeep
    function performUpkeep(bytes calldata /* performData */) external override {
        // Logic to update NFT based on price feed
        // This could involve changing metadata or triggering a new mint
    }
}
```
