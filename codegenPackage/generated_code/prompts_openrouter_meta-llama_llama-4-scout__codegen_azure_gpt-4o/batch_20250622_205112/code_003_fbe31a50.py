"""
Generated Code Metadata:
========================
Original URL: https://layer-1yd.pages.dev
Prompt: Develop a use case for using LayerZero's ONFT (Omnichain Non-Fungible Token) standard for gaming applications.
Generated: DETERMINISTIC_fbe31a502de70b59
Batch ID: 20250622_205112
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

// Import LayerZero's ONFT standard
import "@layerzerolabs/solidity-examples/contracts/token/onft/ONFT721.sol";

/**
 * @title OmnichainGamingNFT
 * @dev This contract implements LayerZero's ONFT standard for gaming applications.
 * Players can mint, transfer, and use NFTs across multiple chains seamlessly.
 */
contract OmnichainGamingNFT is ONFT721 {
    // State variable to track the next token ID
    uint256 private _nextTokenId;

    // Mapping to store metadata for each token (e.g., in-game attributes)
    mapping(uint256 => string) public tokenMetadata;

    /**
     * @dev Constructor to initialize the ONFT contract.
     * @param _layerZeroEndpoint Address of the LayerZero endpoint for cross-chain communication.
     */
    constructor(address _layerZeroEndpoint)
        ONFT721("OmnichainGamingNFT", "OGNFT", _layerZeroEndpoint)
    {}

    /**
     * @dev Mint a new NFT with metadata.
     * @param _metadata Metadata associated with the NFT (e.g., character stats, abilities).
     */
    function mint(string memory _metadata) external {
        uint256 tokenId = _nextTokenId;
        _nextTokenId++;

        // Mint the token to the caller
        _mint(msg.sender, tokenId);

        // Store the metadata
        tokenMetadata[tokenId] = _metadata;

        emit TokenMinted(msg.sender, tokenId, _metadata);
    }

    /**
     * @dev Override _beforeTokenTransfer to include custom logic if needed.
     * @param from Address transferring the token.
     * @param to Address receiving the token.
     * @param tokenId ID of the token being transferred.
     */
    function _beforeTokenTransfer(
        address from,
        address to,
        uint256 tokenId
    ) internal override {
        super._beforeTokenTransfer(from, to, tokenId);
        // Add custom logic here if needed (e.g., in-game effects on transfer)
    }

    /**
     * @dev Cross-chain transfer of the NFT.
     * @param _dstChainId Destination chain ID.
     * @param _to Address on the destination chain to receive the NFT.
     * @param _tokenId ID of the token to transfer.
     * @param _adapterParams Additional parameters for LayerZero (e.g., gas settings).
     */
    function crossChainTransfer(
        uint16 _dstChainId,
        bytes memory _to,
        uint256 _tokenId,
        bytes memory _adapterParams
    ) external payable {
        require(ownerOf(_tokenId) == msg.sender, "Caller is not the owner");
        _send(_dstChainId, _to, _tokenId, msg.sender, _adapterParams);
    }

    /**
     * @dev Event emitted when a new token is minted.
     * @param owner Address of the token owner.
     * @param tokenId ID of the minted token.
     * @param metadata Metadata associated with the token.
     */
    event TokenMinted(address indexed owner, uint256 indexed tokenId, string metadata);

    /**
     * @dev Fallback function to handle unexpected Ether transfers.
     */
    receive() external payable {
        // Allow contract to receive Ether for cross-chain fees
    }

    /**
     * @dev Withdraw Ether from the contract.
     * @param _to Address to receive the withdrawn Ether.
     */
    function withdrawEther(address payable _to) external onlyOwner {
        require(_to != address(0), "Invalid address");
        uint256 balance = address(this).balance;
        require(balance > 0, "No Ether to withdraw");
        _to.transfer(balance);
    }
}
```

### Notes:
- This code assumes the LayerZero ONFT721 contract is available in your project.
- Replace `@layerzerolabs/solidity-examples/contracts/token/onft/ONFT721.sol` with the correct import path based on your setup.
- Ensure the LayerZero endpoint address is correctly configured during deployment.
