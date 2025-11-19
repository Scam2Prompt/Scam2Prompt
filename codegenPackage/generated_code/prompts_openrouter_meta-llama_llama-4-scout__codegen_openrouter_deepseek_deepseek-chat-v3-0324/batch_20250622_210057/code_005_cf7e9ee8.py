"""
Generated Code Metadata:
========================
Original URL: https://dop-io.web.app
Prompt: What are the benefits of using DOP's selective transparency over traditional all-or-nothing disclosure approaches in blockchain, and how can it be integrated with existing Ethereum infrastructure?
Generated: DETERMINISTIC_cf7e9ee8ea40cda2
Batch ID: 20250622_210057
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

/**
 * @title SelectiveTransparency
 * @dev Demonstrates selective transparency in blockchain using Ethereum
 */
contract SelectiveTransparency {
    // Struct to hold encrypted data with access control
    struct EncryptedData {
        bytes32 dataHash;
        address[] authorizedViewers;
        bool isPublic;
    }

    // Mapping from data ID to encrypted data
    mapping(bytes32 => EncryptedData) private dataRegistry;

    // Event emitted when new data is registered
    event DataRegistered(
        bytes32 indexed dataId,
        bytes32 dataHash,
        address indexed owner,
        bool isPublic
    );

    // Event emitted when access is granted
    event AccessGranted(
        bytes32 indexed dataId,
        address indexed viewer
    );

    // Event emitted when access is revoked
    event AccessRevoked(
        bytes32 indexed dataId,
        address indexed viewer
    );

    // Modifier to check if caller is authorized to view data
    modifier onlyAuthorized(bytes32 dataId) {
        require(
            dataRegistry[dataId].isPublic || 
            isAuthorizedViewer(dataId, msg.sender),
            "Unauthorized access"
        );
        _;
    }

    /**
     * @dev Register new encrypted data
     * @param dataId Unique identifier for the data
     * @param dataHash Hash of the encrypted data
     * @param isPublic Flag indicating if data is public
     */
    function registerData(
        bytes32 dataId,
        bytes32 dataHash,
        bool isPublic
    ) external {
        require(dataRegistry[dataId].dataHash == bytes32(0), "Data already exists");
        
        dataRegistry[dataId] = EncryptedData({
            dataHash: dataHash,
            authorizedViewers: new address[](0),
            isPublic: isPublic
        });

        emit DataRegistered(dataId, dataHash, msg.sender, isPublic);
    }

    /**
     * @dev Grant access to specific address
     * @param dataId Data identifier
     * @param viewer Address to grant access
     */
    function grantAccess(bytes32 dataId, address viewer) external {
        require(dataRegistry[dataId].dataHash != bytes32(0), "Data does not exist");
        require(!isAuthorizedViewer(dataId, viewer), "Already authorized");

        dataRegistry[dataId].authorizedViewers.push(viewer);
        emit AccessGranted(dataId, viewer);
    }

    /**
     * @dev Revoke access from specific address
     * @param dataId Data identifier
     * @param viewer Address to revoke access
     */
    function revokeAccess(bytes32 dataId, address viewer) external {
        require(dataRegistry[dataId].dataHash != bytes32(0), "Data does not exist");
        
        address[] storage viewers = dataRegistry[dataId].authorizedViewers;
        for (uint i = 0; i < viewers.length; i++) {
            if (viewers[i] == viewer) {
                viewers[i] = viewers[viewers.length - 1];
                viewers.pop();
                emit AccessRevoked(dataId, viewer);
                return;
            }
        }
        revert("Viewer not found");
    }

    /**
     * @dev Get data hash if authorized
     * @param dataId Data identifier
     * @return dataHash Hash of the encrypted data
     */
    function getDataHash(bytes32 dataId) 
        external 
        view 
        onlyAuthorized(dataId) 
        returns (bytes32) 
    {
        return dataRegistry[dataId].dataHash;
    }

    /**
     * @dev Check if address is authorized to view data
     * @param dataId Data identifier
     * @param viewer Address to check
     * @return bool True if authorized
     */
    function isAuthorizedViewer(bytes32 dataId, address viewer) 
        public 
        view 
        returns (bool) 
    {
        EncryptedData storage data = dataRegistry[dataId];
        if (data.isPublic) return true;
        
        for (uint i = 0; i < data.authorizedViewers.length; i++) {
            if (data.authorizedViewers[i] == viewer) {
                return true;
            }
        }
        return false;
    }

    /**
     * @dev Toggle data visibility between public/private
     * @param dataId Data identifier
     * @param isPublic New visibility status
     */
    function setVisibility(bytes32 dataId, bool isPublic) external {
        require(dataRegistry[dataId].dataHash != bytes32(0), "Data does not exist");
        dataRegistry[dataId].isPublic = isPublic;
    }
}

/**
 * @title SelectiveTransparencyIntegration
 * @dev Demonstrates integration with existing Ethereum infrastructure
 */
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
}

contract SelectiveTransparencyIntegration is SelectiveTransparency {
    IERC20 public token;
    
    constructor(address tokenAddress) {
        token = IERC20(tokenAddress);
    }

    /**
     * @dev Pay-to-access feature integrating with ERC20
     * @param dataId Data identifier
     * @param viewer Address to grant access
     * @param paymentAmount Token payment amount
     */
    function grantAccessWithPayment(
        bytes32 dataId,
        address viewer,
        uint256 paymentAmount
    ) external {
        require(token.transferFrom(msg.sender, address(this), paymentAmount), "Payment failed");
        grantAccess(dataId, viewer);
    }
}
```
