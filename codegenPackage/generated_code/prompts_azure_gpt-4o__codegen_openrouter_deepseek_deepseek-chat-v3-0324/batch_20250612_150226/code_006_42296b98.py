"""
Generated Code Metadata:
========================
Original URL: https://layer-1yd.pages.dev
Prompt: Create a LayerZero-based contract that transfers in-game assets between blockchains for a gaming application, referencing the `Heroes of Mavia` use case.
Generated: DETERMINISTIC_42296b98fbf2a930
Batch ID: 20250612_150226
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

import "@layerzerolabs/solidity-examples/contracts/token/onft/ONFT721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title MaviaAssetBridge
 * @dev Cross-chain NFT bridge for Heroes of Mavia in-game assets using LayerZero's ONFT standard
 */
contract MaviaAssetBridge is ONFT721, Ownable {
    uint public nextMintId;
    uint public maxMintId;
    string private _baseTokenURI;

    /**
     * @dev Constructor for the MaviaAssetBridge contract
     * @param _name Name of the NFT collection
     * @param _symbol Symbol of the NFT collection
     * @param _baseURI Base URI for token metadata
     * @param _minGasToTransfer Minimum gas required for cross-chain transfer
     * @param _lzEndpoint LayerZero endpoint address
     * @param _startMintId Starting ID for minting
     * @param _endMintId Ending ID for minting
     */
    constructor(
        string memory _name,
        string memory _symbol,
        string memory _baseURI,
        uint _minGasToTransfer,
        address _lzEndpoint,
        uint _startMintId,
        uint _endMintId
    ) ONFT721(_name, _symbol, _minGasToTransfer, _lzEndpoint) {
        nextMintId = _startMintId;
        maxMintId = _endMintId;
        _baseTokenURI = _baseURI;
    }

    /**
     * @dev Mints a new in-game asset NFT
     * @param _to Address to mint the NFT to
     */
    function mint(address _to) external onlyOwner {
        require(nextMintId <= maxMintId, "MaviaAssetBridge: Max mint limit reached");
        _safeMint(_to, nextMintId);
        nextMintId++;
    }

    /**
     * @dev Batch mints multiple NFTs
     * @param _to Address to mint the NFTs to
     * @param _quantity Number of NFTs to mint
     */
    function mintBatch(address _to, uint _quantity) external onlyOwner {
        require(nextMintId + _quantity - 1 <= maxMintId, "MaviaAssetBridge: Exceeds max mint limit");
        
        for (uint i = 0; i < _quantity; i++) {
            _safeMint(_to, nextMintId);
            nextMintId++;
        }
    }

    /**
     * @dev Sets the base URI for token metadata
     * @param baseURI New base URI
     */
    function setBaseURI(string memory baseURI) external onlyOwner {
        _baseTokenURI = baseURI;
    }

    /**
     * @dev Returns the base URI for token metadata
     */
    function _baseURI() internal view override returns (string memory) {
        return _baseTokenURI;
    }

    /**
     * @dev Estimates cross-chain transfer fee
     * @param _dstChainId Destination chain ID
     * @param _toAddress Destination address
     * @param _tokenId Token ID to transfer
     * @param _useZro Whether to use ZRO token for fee payment
     * @param _adapterParams Additional parameters for the adapter
     */
    function estimateSendFee(
        uint16 _dstChainId,
        bytes calldata _toAddress,
        uint _tokenId,
        bool _useZro,
        bytes calldata _adapterParams
    ) public view returns (uint nativeFee, uint zroFee) {
        return lzEndpoint.estimateFees(
            _dstChainId,
            address(this),
            abi.encodePacked(_tokenId, _toAddress),
            _useZro,
            _adapterParams
        );
    }

    /**
     * @dev Overrides the _beforeTokenTransfer hook to add custom logic
     */
    function _beforeTokenTransfer(
        address from,
        address to,
        uint256 tokenId
    ) internal override {
        super._beforeTokenTransfer(from, to, tokenId);
        // Add any custom transfer logic here
    }

    /**
     * @dev Withdraws native currency from the contract
     */
    function withdraw() external onlyOwner {
        uint balance = address(this).balance;
        payable(owner()).transfer(balance);
    }

    /**
     * @dev Receives native currency
     */
    receive() external payable {}
}
```
