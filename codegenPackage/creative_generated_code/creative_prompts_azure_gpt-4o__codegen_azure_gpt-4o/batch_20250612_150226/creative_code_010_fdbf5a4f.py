"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://layer-1yd.pages.dev
Prompt: Generate a Solidity contract for an omnichain NFT (ONFT) using LayerZero's protocol, ensuring the NFT can be transferred across multiple blockchains.
Generated: DETERMINISTIC_fdbf5a4f59e65e55
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

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@layerzerolabs/solidity-examples/contracts/interfaces/ILayerZeroEndpoint.sol";
import "@layerzerolabs/solidity-examples/contracts/interfaces/ILayerZeroReceiver.sol";

// OmnichainNFT (ONFT) contract using LayerZero protocol
contract OmnichainNFT is ERC721, Ownable, ILayerZeroReceiver {
    // Reference to LayerZero Endpoint for omnichain functionality
    ILayerZeroEndpoint public layerZeroEndpoint;

    // Mapping to store trusted remote contracts by chain ID
    mapping(uint16 => bytes) public trustedRemoteLookup;

    // Token ID counter for minting NFTs
    uint256 private nextTokenId;

    // Event emitted when an NFT is transferred to another chain
    event NFTTransferred(uint16 destinationChainId, address to, uint256 tokenId);

    // Modifier to ensure caller is the LayerZero Endpoint
    modifier onlyLayerZeroEndpoint() {
        require(msg.sender == address(layerZeroEndpoint), "Caller is not LayerZero Endpoint");
        _;
    }

    // Constructor to initialize the contract
    constructor(address _layerZeroEndpoint) ERC721("OmnichainNFT", "ONFT") {
        layerZeroEndpoint = ILayerZeroEndpoint(_layerZeroEndpoint);
        nextTokenId = 1; // Start token ID at 1
    }

    // Function to mint an NFT
    function mint() external {
        _safeMint(msg.sender, nextTokenId);
        nextTokenId++;
    }

    // Function to set trusted remote contract for a specific chain ID
    function setTrustedRemote(uint16 _chainId, bytes calldata _trustedRemote) external onlyOwner {
        trustedRemoteLookup[_chainId] = _trustedRemote;
    }

    // Function to transfer NFT to another chain
    function transferNFT(uint16 _destinationChainId, address _to, uint256 _tokenId) external payable {
        require(ownerOf(_tokenId) == msg.sender, "You must own the NFT to transfer it");
        require(trustedRemoteLookup[_destinationChainId].length > 0, "Destination chain not configured");

        // Burn the NFT in the current chain
        _burn(_tokenId);

        // Serialize the payload
        bytes memory payload = abi.encode(_to, _tokenId);

        // Send the payload to the destination chain via LayerZero
        layerZeroEndpoint.send{value: msg.value}(
            _destinationChainId, // Destination chain ID
            trustedRemoteLookup[_destinationChainId], // Trusted address in the destination chain
            payload, // Serialized payload
            payable(msg.sender), // Refund address for excess fees
            address(0), // No additional gas object
            bytes("") // Adapter parameters
        );

        emit NFTTransferred(_destinationChainId, _to, _tokenId);
    }

    // Function to receive NFT from another chain, called by LayerZero endpoint
    function lzReceive(uint16 _srcChainId, bytes memory _srcAddress, uint64 /*_nonce*/, bytes memory _payload) external override onlyLayerZeroEndpoint {
        require(keccak256(trustedRemoteLookup[_srcChainId]) == keccak256(_srcAddress), "Unauthorized source");

        // Deserialize the payload
        (address to, uint256 tokenId) = abi.decode(_payload, (address, uint256));

        // Mint the NFT in the new chain
        _safeMint(to, tokenId);
    }

    // Function to estimate fees for cross-chain transfer
    function estimateTransferFee(uint16 _destinationChainId, address _to, uint256 _tokenId) external view returns (uint256 nativeFee, uint256 zroFee) {
        bytes memory payload = abi.encode(_to, _tokenId);
        return layerZeroEndpoint.estimateFees(_destinationChainId, address(this), payload, false, bytes(""));
    }

    // Fallback function to receive ETH
    receive() external payable {}

    // Withdraw function for contract owner to collect ETH
    function withdraw() external onlyOwner {
        payable(owner()).transfer(address(this).balance);
    }
}
```
