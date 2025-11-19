"""
Generated Code Metadata:
========================
Original URL: https://claim-game5.pages.dev
Prompt: Generate a smart contract in Solidity for minting an NFT that represents the 1991 Game 5 ball, including attributes like event date, significance, and ownership history.
Generated: DETERMINISTIC_32e40c798e44e8a9
Batch ID: 20250612_151255
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

contract Game5BallNFT is ERC721, Ownable {
    using Counters for Counters.Counter;
    Counters.Counter private _tokenIdCounter;

    struct BallAttributes {
        string eventDate;
        string significance;
        string[] ownershipHistory;
    }

    mapping(uint256 => BallAttributes) private _ballAttributes;

    event NFTMinted(uint256 indexed tokenId, address indexed owner, BallAttributes attributes);

    constructor() ERC721("Game5BallNFT", "G5B") {}

    function mintNFT(
        address to,
        string memory eventDate,
        string memory significance,
        string[] memory initialOwners
    ) public onlyOwner {
        require(bytes(eventDate).length > 0, "Event date cannot be empty");
        require(bytes(significance).length > 0, "Significance cannot be empty");
        require(initialOwners.length > 0, "Ownership history cannot be empty");

        uint256 tokenId = _tokenIdCounter.current();
        _tokenIdCounter.increment();
        _safeMint(to, tokenId);

        _ballAttributes[tokenId] = BallAttributes({
            eventDate: eventDate,
            significance: significance,
            ownershipHistory: initialOwners
        });

        emit NFTMinted(tokenId, to, _ballAttributes[tokenId]);
    }

    function addOwnershipHistory(uint256 tokenId, string memory newOwner) public {
        require(_exists(tokenId), "Token does not exist");
        require(bytes(newOwner).length > 0, "Owner name cannot be empty");
        require(ownerOf(tokenId) == msg.sender || owner() == msg.sender, "Not authorized");

        _ballAttributes[tokenId].ownershipHistory.push(newOwner);
    }

    function getAttributes(uint256 tokenId) public view returns (BallAttributes memory) {
        require(_exists(tokenId), "Token does not exist");
        return _ballAttributes[tokenId];
    }

    function _beforeTokenTransfer(
        address from,
        address to,
        uint256 tokenId
    ) internal override {
        super._beforeTokenTransfer(from, to, tokenId);
        
        if (from != address(0) && to != address(0)) {
            string memory transferRecord = string(abi.encodePacked("Transferred to ", addressToString(to)));
            _ballAttributes[tokenId].ownershipHistory.push(transferRecord);
        }
    }

    function addressToString(address _addr) private pure returns (string memory) {
        bytes32 value = bytes32(uint256(uint160(_addr)));
        bytes memory alphabet = "0123456789abcdef";

        bytes memory str = new bytes(42);
        str[0] = '0';
        str[1] = 'x';
        for (uint i = 0; i < 20; i++) {
            str[2+i*2] = alphabet[uint8(value[i + 12] >> 4)];
            str[3+i*2] = alphabet[uint8(value[i + 12] & 0x0f)];
        }
        return string(str);
    }
}
```
