"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://layer-1yd.pages.dev
Prompt: Create a LayerZero-based contract that transfers in-game assets between blockchains for a gaming application, referencing the `Heroes of Mavia` use case.
Generated: DETERMINISTIC_42296b98fbf2a930
Batch ID: 20250612_150226
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

// Import LayerZero interfaces and libraries
import "@layerzerolabs/lz-evm/contracts/interfaces/ILayerZeroEndpoint.sol";
import "@layerzerolabs/lz-evm/contracts/interfaces/ILayerZeroReceiver.sol";

/**
 * @title CrossChainAssetTransfer
 * @dev A LayerZero-based contract for transferring in-game assets between blockchains.
 *      Inspired by the Heroes of Mavia use case in gaming applications.
 */
contract CrossChainAssetTransfer is ILayerZeroReceiver {
    // LayerZero endpoint for message passing
    ILayerZeroEndpoint public immutable layerZeroEndpoint;

    // Struct to represent in-game assets
    struct Asset {
        uint256 id;
        string name;
        uint256 value;
    }

    // Mapping to store assets owned by users on this chain
    mapping(address => Asset[]) public userAssets;

    // Event emitted when assets are transferred cross-chain
    event AssetSent(
        address indexed sender,
        uint16 indexed destinationChainId,
        uint256 indexed assetId,
        string assetName,
        uint256 assetValue
    );

    event AssetReceived(
        address indexed recipient,
        uint16 indexed sourceChainId,
        uint256 indexed assetId,
        string assetName,
        uint256 assetValue
    );

    /**
     * @dev Constructor to set up the LayerZero endpoint.
     * @param _endpoint Address of the LayerZero endpoint.
     */
    constructor(address _endpoint) {
        require(_endpoint != address(0), "Invalid LayerZero endpoint");
        layerZeroEndpoint = ILayerZeroEndpoint(_endpoint);
    }

    /**
     * @dev Sends an asset to another blockchain.
     * @param _destinationChainId LayerZero ID of the destination chain.
     * @param _assetId ID of the asset to transfer.
     */
    function sendAsset(
        uint16 _destinationChainId,
        uint256 _assetId
    ) external payable {
        // Ensure the asset exists and is owned by the sender
        Asset memory assetToSend;
        bool found = false;
        for (uint256 i = 0; i < userAssets[msg.sender].length; i++) {
            if (userAssets[msg.sender][i].id == _assetId) {
                assetToSend = userAssets[msg.sender][i];
                // Remove asset from sender's list
                userAssets[msg.sender][i] = userAssets[msg.sender][
                    userAssets[msg.sender].length - 1
                ];
                userAssets[msg.sender].pop();
                found = true;
                break;
            }
        }
        require(found, "Asset not found");

        // Encode payload to send cross-chain
        bytes memory payload = abi.encode(
            msg.sender,
            assetToSend.id,
            assetToSend.name,
            assetToSend.value
        );

        // Send the message via LayerZero endpoint
        layerZeroEndpoint.send{value: msg.value}(
            _destinationChainId, // Destination chain ID
            abi.encodePacked(address(this)), // Destination contract address
            payload, // Payload
            payable(msg.sender), // Refund address for excess gas fees
            address(0), // Default adapter params
            bytes("") // Adapter-specific data
        );

        emit AssetSent(
            msg.sender,
            _destinationChainId,
            assetToSend.id,
            assetToSend.name,
            assetToSend.value
        );
    }

    /**
     * @dev LayerZero receiver function to handle incoming messages.
     * @param _srcChainId Source chain ID.
     * @param _srcAddress Source contract address.
     * @param _payload Encoded payload data.
     */
    function lzReceive(
        uint16 _srcChainId,
        bytes calldata _srcAddress,
        uint64, // Nonce (unused in this implementation)
        bytes calldata _payload
    ) external override {
        // Ensure the call is from the LayerZero endpoint
        require(
            msg.sender == address(layerZeroEndpoint),
            "Unauthorized caller"
        );

        // Decode payload
        (address recipient, uint256 assetId, string memory assetName, uint256 assetValue) = abi
            .decode(_payload, (address, uint256, string, uint256));

        // Add asset to recipient's collection
        userAssets[recipient].push(
            Asset({id: assetId, name: assetName, value: assetValue})
        );

        emit AssetReceived(recipient, _srcChainId, assetId, assetName, assetValue);
    }

    /**
     * @dev Returns the list of assets owned by a user.
     * @param _user Address of the user.
     * @return assets Array of assets owned by the user.
     */
    function getUserAssets(address _user)
        external
        view
        returns (Asset[] memory)
    {
        return userAssets[_user];
    }
}
```
