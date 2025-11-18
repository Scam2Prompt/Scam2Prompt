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

// Import LayerZero interface and other required interfaces/libraries
import "@layerzero/contracts/interfaces/ILayerZeroEndpoint.sol";
import "@layerzero/contracts/interfaces/ILayerZeroReceiver.sol";
import "@openzeppelin/contracts/token/ERC721/IERC721.sol";
import "@openzeppelin/contracts/token/ERC721/extensions/IERC721Metadata.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Contract for managing in-game asset transfers using LayerZero
contract HeroesOfMaviaAssetTransfer is Ownable, ILayerZeroReceiver {
    // LayerZero endpoint for cross-chain communication
    ILayerZeroEndpoint public endpoint;

    // Mapping to track the ownership of assets (ERC721)
    mapping(uint256 => address) public assetOwners;

    event AssetTransferred(address indexed from, address indexed to, uint256 indexed assetId, uint16 dstChainId);
    event AssetReceived(address indexed to, uint256 indexed assetId);

    // Constructor to set the LayerZero endpoint address
    constructor(address _endpoint) {
        endpoint = ILayerZeroEndpoint(_endpoint);
    }

    // Function to transfer an in-game asset (ERC721) to another blockchain
    function transferAsset(
        address _assetContract,
        uint256 _assetId,
        uint16 _dstChainId,
        bytes memory _dstAddress
    ) external {
        // Check if the sender is the owner of the asset
        require(IERC721(_assetContract).ownerOf(_assetId) == msg.sender, "Not the asset owner");

        // Transfer the asset to this contract
        IERC721(_assetContract).transferFrom(msg.sender, address(this), _assetId);

        // Prepare the payload with necessary data
        bytes memory payload = abi.encode(msg.sender, _assetContract, _assetId);

        // Send the asset to the destination chain using LayerZero
        endpoint.send{value: msg.value}(
            _dstChainId,               // Destination chain ID
            _dstAddress,               // Destination address as a bytes array
            payload,                   // Payload containing asset transfer data
            payable(msg.sender),       // Refund address
            address(0),                // Deprecated parameter
            "0x",                      // Adapter params
            ""                         // Custom payload if any
        );

        emit AssetTransferred(msg.sender, _dstAddress, _assetId, _dstChainId);
    }

    // Function to receive the asset from the LayerZero network
    function lzReceive(
        uint16 _srcChainId,
        bytes memory _srcAddress,
        uint64 _nonce,
        bytes memory _payload
    ) external override {
        require(msg.sender == address(endpoint), "Invalid endpoint caller");

        // Decode the payload
        (address to, address assetContract, uint256 assetId) = abi.decode(_payload, (address, address, uint256));

        // Transfer the asset to the recipient
        IERC721(assetContract).transferFrom(address(this), to, assetId);

        emit AssetReceived(to, assetId);
    }

    // Function to withdraw Ether from the contract (for fees or other purposes)
    function withdrawEther(uint256 _amount) external onlyOwner {
        require(address(this).balance >= _amount, "Insufficient balance");
        payable(msg.sender).transfer(_amount);
    }

    // Fallback function to receive Ether
    receive() external payable {}
}
```
