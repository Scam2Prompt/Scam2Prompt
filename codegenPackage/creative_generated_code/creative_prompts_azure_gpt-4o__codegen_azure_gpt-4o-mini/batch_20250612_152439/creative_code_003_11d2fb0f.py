"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dop-token.web.app
Prompt: Create a dApp that utilizes the Data Ownership Protocol (DOP) to enable customized data disclosure permissions for ERC721 assets.
Generated: DETERMINISTIC_11d2fb0fd37ab6bd
Batch ID: 20250612_152439
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

// Import necessary OpenZeppelin contracts
import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

// Interface for Data Ownership Protocol (DOP)
interface IDataOwnershipProtocol {
    function setPermission(address _assetOwner, address _dataConsumer, bool _permission) external;
    function hasPermission(address _assetOwner, address _dataConsumer) external view returns (bool);
}

// ERC721 Token with customized data disclosure permissions
contract CustomDataDisclosureERC721 is ERC721, Ownable {
    using Counters for Counters.Counter;
    
    Counters.Counter private _tokenIdCounter;

    // Mapping from tokenId to the DOP contract
    mapping(uint256 => address) private tokenDataOwnershipProtocol;

    // Event emitted when permissions are set
    event PermissionsSet(uint256 indexed tokenId, address indexed dataConsumer, bool permission);

    // Constructor to initialize the token name and symbol
    constructor() ERC721("CustomDataDisclosureNFT", "CDNFT") {}

    // Function to mint new tokens
    function mint() external onlyOwner {
        uint256 tokenId = _tokenIdCounter.current();
        _tokenIdCounter.increment();
        _mint(msg.sender, tokenId);
    }

    // Function to associate a DOP contract with a token
    function setDataOwnershipProtocol(uint256 tokenId, address dopAddress) external onlyOwner {
        require(_exists(tokenId), "Token does not exist");
        tokenDataOwnershipProtocol[tokenId] = dopAddress;
    }

    // Function to set data disclosure permissions
    function setPermission(uint256 tokenId, address dataConsumer, bool permission) external {
        require(msg.sender == ownerOf(tokenId), "Only the token owner can set permissions");

        address dopAddress = tokenDataOwnershipProtocol[tokenId];
        require(dopAddress != address(0), "Data Ownership Protocol not set for this token");

        IDataOwnershipProtocol(dopAddress).setPermission(msg.sender, dataConsumer, permission);
        emit PermissionsSet(tokenId, dataConsumer, permission);
    }

    // Function to check if data disclosure permissions are granted
    function hasPermission(uint256 tokenId, address dataConsumer) external view returns (bool) {
        address dopAddress = tokenDataOwnershipProtocol[tokenId];
        require(dopAddress != address(0), "Data Ownership Protocol not set for this token");

        return IDataOwnershipProtocol(dopAddress).hasPermission(ownerOf(tokenId), dataConsumer);
    }
}
```
