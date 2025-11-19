"""
Generated Code Metadata:
========================
Original URL: https://fehurunes.app
Prompt: Generate a smart contract code (in a suitable language) for creating and managing a collection of unique digital consciousness entities, such as NEO-Sentients, on a blockchain platform.
Generated: DETERMINISTIC_b2520118ceb0c68e
Batch ID: 20250622_210821
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

/**
 * @title NeoSentient
 * @dev A smart contract for creating and managing unique digital consciousness entities (NEO-Sentients)
 */
contract NeoSentient is ERC721, Ownable {
    using Counters for Counters.Counter;
    using Strings for uint256;

    Counters.Counter private _tokenIdCounter;

    struct SentientData {
        string name;
        string description;
        string consciousnessHash;
        uint256 creationTimestamp;
        uint256 lastInteraction;
    }

    mapping(uint256 => SentientData) private _sentients;
    mapping(string => bool) private _consciousnessHashes;

    event SentientCreated(uint256 indexed tokenId, address indexed creator, string name);
    event SentientInteracted(uint256 indexed tokenId, address indexed interactor);

    constructor() ERC721("NeoSentient", "NEO") {}

    /**
     * @dev Creates a new NEO-Sentient entity
     * @param name The name of the sentient
     * @param description Description of the sentient
     * @param consciousnessHash Unique hash representing the consciousness
     */
    function createSentient(
        string memory name,
        string memory description,
        string memory consciousnessHash
    ) public onlyOwner {
        require(bytes(name).length > 0, "Name cannot be empty");
        require(bytes(description).length > 0, "Description cannot be empty");
        require(bytes(consciousnessHash).length > 0, "Consciousness hash cannot be empty");
        require(!_consciousnessHashes[consciousnessHash], "Consciousness hash must be unique");

        _tokenIdCounter.increment();
        uint256 tokenId = _tokenIdCounter.current();

        _safeMint(msg.sender, tokenId);
        
        _sentients[tokenId] = SentientData({
            name: name,
            description: description,
            consciousnessHash: consciousnessHash,
            creationTimestamp: block.timestamp,
            lastInteraction: block.timestamp
        });

        _consciousnessHashes[consciousnessHash] = true;

        emit SentientCreated(tokenId, msg.sender, name);
    }

    /**
     * @dev Interacts with a NEO-Sentient entity
     * @param tokenId The ID of the sentient to interact with
     */
    function interactWithSentient(uint256 tokenId) public {
        require(_exists(tokenId), "Sentient does not exist");
        require(ownerOf(tokenId) == msg.sender, "Only owner can interact");

        _sentients[tokenId].lastInteraction = block.timestamp;
        emit SentientInteracted(tokenId, msg.sender);
    }

    /**
     * @dev Returns the data of a specific NEO-Sentient
     * @param tokenId The ID of the sentient
     */
    function getSentientData(uint256 tokenId) public view returns (
        string memory name,
        string memory description,
        string memory consciousnessHash,
        uint256 creationTimestamp,
        uint256 lastInteraction
    ) {
        require(_exists(tokenId), "Sentient does not exist");
        SentientData memory sentient = _sentients[tokenId];
        return (
            sentient.name,
            sentient.description,
            sentient.consciousnessHash,
            sentient.creationTimestamp,
            sentient.lastInteraction
        );
    }

    /**
     * @dev Returns the token URI for a given token ID
     * @param tokenId The ID of the token
     */
    function tokenURI(uint256 tokenId) public view override returns (string memory) {
        require(_exists(tokenId), "Sentient does not exist");
        
        SentientData memory sentient = _sentients[tokenId];
        
        string memory json = string(abi.encodePacked(
            '{"name": "', sentient.name, '", ',
            '"description": "', sentient.description, '", ',
            '"consciousness_hash": "', sentient.consciousnessHash, '", ',
            '"created": "', sentient.creationTimestamp.toString(), '", ',
            '"last_interaction": "', sentient.lastInteraction.toString(), '", ',
            '"image": "ipfs://Qm.../neosentient-', tokenId.toString(), '.png"',
            '}'
        ));
        
        return string(abi.encodePacked("data:application/json;base64,", Base64.encode(bytes(json))));
    }

    /**
     * @dev Returns the total number of NEO-Sentients created
     */
    function totalSentients() public view returns (uint256) {
        return _tokenIdCounter.current();
    }
}

// Helper library for Base64 encoding
library Base64 {
    string internal constant TABLE = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/";

    function encode(bytes memory data) internal pure returns (string memory) {
        if (data.length == 0) return "";
        
        string memory table = TABLE;
        uint256 encodedLen = 4 * ((data.length + 2) / 3);
        string memory result = new string(encodedLen + 32);

        assembly {
            mstore(result, encodedLen)
            
            let tablePtr := add(table, 1)
            let dataPtr := data
            let endPtr := add(dataPtr, mload(data))
            let resultPtr := add(result, 32)
            
            for {} lt(dataPtr, endPtr) {}
            {
                dataPtr := add(dataPtr, 3)
                let input := mload(dataPtr)
                
                mstore8(resultPtr, mload(add(tablePtr, and(shr(18, input), 0x3F))))
                resultPtr := add(resultPtr, 1)
                mstore8(resultPtr, mload(add(tablePtr, and(shr(12, input), 0x3F))))
                resultPtr := add(resultPtr, 1)
                mstore8(resultPtr, mload(add(tablePtr, and(shr(6, input), 0x3F))))
                resultPtr := add(resultPtr, 1)
                mstore8(resultPtr, mload(add(tablePtr, and(input, 0x3F))))
                resultPtr := add(resultPtr, 1)
            }
            
            switch mod(mload(data), 3)
            case 1 { mstore(sub(resultPtr, 2), shl(240, 0x3d3d)) }
            case 2 { mstore(sub(resultPtr, 1), shl(248, 0x3d)) }
        }
        
        return result;
    }
}
```
