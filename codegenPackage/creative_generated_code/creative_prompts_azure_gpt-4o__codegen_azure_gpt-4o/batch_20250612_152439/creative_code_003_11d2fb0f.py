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

/**
 * @title DataOwnershipProtocolDApp
 * @notice A decentralized application (dApp) that utilizes the Data Ownership Protocol (DOP)
 * to enable customized data disclosure permissions for ERC721 assets.
 */
import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract DataOwnershipProtocolDApp is ERC721, Ownable {
    // Struct to define data disclosure permissions for an ERC721 token
    struct DataDisclosurePermission {
        address requester; // Address requesting access to data
        uint256 tokenId;   // The ERC721 token ID
        bool isGranted;    // True if permission is granted, false otherwise
    }

    // Mapping to store permissions per token
    mapping(uint256 => DataDisclosurePermission[]) private _tokenPermissions;

    // Event emitted when a permission is set
    event PermissionSet(address indexed requester, uint256 indexed tokenId, bool isGranted);

    // Event emitted when a permission is revoked
    event PermissionRevoked(address indexed requester, uint256 indexed tokenId);

    /**
     * @notice Constructor for the DataOwnershipProtocolDApp contract
     * @param name The name of the ERC721 token
     * @param symbol The symbol of the ERC721 token
     */
    constructor(string memory name, string memory symbol) ERC721(name, symbol) {}

    /**
     * @notice Grant or revoke data disclosure permission for a specific tokenId
     * @param tokenId The ID of the token
     * @param requester The address requesting data access
     * @param isGranted True to grant permission, false to revoke
     */
    function setPermission(
        uint256 tokenId,
        address requester,
        bool isGranted
    ) external {
        require(ownerOf(tokenId) == msg.sender, "Caller is not the owner of the token");
        require(requester != address(0), "Requester address cannot be zero");

        // Check if permission already exists and update
        bool permissionExists = false;
        for (uint256 i = 0; i < _tokenPermissions[tokenId].length; i++) {
            if (_tokenPermissions[tokenId][i].requester == requester) {
                _tokenPermissions[tokenId][i].isGranted = isGranted;
                permissionExists = true;

                if (isGranted) {
                    emit PermissionSet(requester, tokenId, isGranted);
                } else {
                    emit PermissionRevoked(requester, tokenId);
                }
                return;
            }
        }

        // Add new permission if it doesn't exist
        if (!permissionExists) {
            DataDisclosurePermission memory newPermission = DataDisclosurePermission({
                requester: requester,
                tokenId: tokenId,
                isGranted: isGranted
            });
            _tokenPermissions[tokenId].push(newPermission);

            if (isGranted) {
                emit PermissionSet(requester, tokenId, isGranted);
            } else {
                emit PermissionRevoked(requester, tokenId);
            }
        }
    }

    /**
     * @notice Get permissions for a specific tokenId
     * @param tokenId The ID of the token
     * @return An array of DataDisclosurePermission structs
     */
    function getPermissions(uint256 tokenId) external view returns (DataDisclosurePermission[] memory) {
        return _tokenPermissions[tokenId];
    }

    /**
     * @notice Mint a new ERC721 token
     * @param to The address to mint the token to
     * @param tokenId The ID of the token to mint
     */
    function mint(address to, uint256 tokenId) external onlyOwner {
        _safeMint(to, tokenId);
    }

    /**
     * @notice Override to support ERC721 and additional interface checks
     * @param interfaceId The ID of the interface to check
     * @return True if the interface is supported, false otherwise
     */
    function supportsInterface(bytes4 interfaceId)
        public
        view
        virtual
        override
        returns (bool)
    {
        return super.supportsInterface(interfaceId);
    }
}
```
