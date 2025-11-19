"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://layer-1yd.pages.dev
Prompt: Write a Solidity contract that utilizes LayerZero's OFT standard to transfer fungible tokens across multiple blockchains without using liquidity pools.
Generated: DETERMINISTIC_c9820f8c3f8ead29
Batch ID: 20250612_164304
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

// Import LayerZero's OFT (Omnichain Fungible Token) contract
import "@layerzerolabs/oft/contracts/FullOFT.sol";

/**
 * @title CrossChainToken
 * @dev A fungible token contract that utilizes LayerZero's OFT standard for seamless token transfers across chains.
 */
contract CrossChainToken is FullOFT {
    // Event emitted when an admin changes the trusted address for LayerZero communication
    event TrustedRemoteUpdated(uint16 indexed dstChainId, bytes remoteAddress);

    // Mapping to store trusted remote LayerZero addresses for cross-chain communication
    mapping(uint16 => bytes) public trustedRemoteLookup;

    /**
     * @dev Constructor initializes the token with name, symbol, and LayerZero endpoint.
     * @param _name Name of the token.
     * @param _symbol Symbol of the token.
     * @param _endpoint LayerZero endpoint address.
     */
    constructor(string memory _name, string memory _symbol, address _endpoint)
        FullOFT(_name, _symbol, _endpoint)
    {}

    /**
     * @dev Updates the trusted remote address for a specific chain ID.
     * Callable only by the contract owner.
     * @param _chainId Destination chain ID.
     * @param _remoteAddress Address of the trusted contract on the destination chain.
     */
    function setTrustedRemote(uint16 _chainId, bytes calldata _remoteAddress) external onlyOwner {
        trustedRemoteLookup[_chainId] = _remoteAddress;
        emit TrustedRemoteUpdated(_chainId, _remoteAddress);
    }

    /**
     * @dev Overrides the LayerZero _creditTo method to validate trusted remote addresses.
     * Ensures only valid source addresses interact with this contract.
     * @param _chainId Source chain ID.
     * @param _sender Address of the sender from the source chain.
     */
    function _creditTo(uint16 _chainId, address _sender, uint _amount) internal override {
        require(keccak256(trustedRemoteLookup[_chainId]) == keccak256(abi.encodePacked(_sender)), "Invalid remote sender");
        super._creditTo(_chainId, _sender, _amount);
    }

    /**
     * @dev Sends tokens to a recipient on a different chain.
     * @param _dstChainId Destination chain ID.
     * @param _recipient Recipient address on the destination chain.
     * @param _amount Amount of tokens to send.
     * @param _refundAddress Address to refund excess gas fees.
     * @param _adapterParams Parameters for LayerZero adapter (e.g., gas limit).
     */
    function sendTokensToChain(
        uint16 _dstChainId,
        bytes calldata _recipient,
        uint _amount,
        address payable _refundAddress,
        bytes calldata _adapterParams
    ) external payable {
        // Transfer tokens from the sender to this contract for sending
        _transfer(msg.sender, address(this), _amount);

        // Call LayerZero's send functionality
        _send(
            _dstChainId,
            _recipient,
            _amount,
            _refundAddress,
            msg.sender,
            _adapterParams
        );
    }

    /**
     * @dev Ensures the recipient receives the tokens after a cross-chain transfer.
     * Overrides the LayerZero _debitFrom method.
     * @param _from Address initiating the transfer.
     * @param _chainId Destination chain ID.
     * @param _amount Amount of tokens being transferred.
     */
    function _debitFrom(address _from, uint16 _chainId, uint _amount) internal override {
        require(balanceOf(_from) >= _amount, "Insufficient balance");
        super._debitFrom(_from, _chainId, _amount);
    }
}
```
