"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://stakestoneclaim.pages.dev
Prompt: Design a cross-chain redemption system for STONE tokens using LayerZero, ensuring seamless asset and price transfers across blockchains.
Generated: DETERMINISTIC_39e2082599cd2ae2
Batch ID: 20250612_151057
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
import "@layerzerolabs/contracts/interfaces/ILayerZeroEndpoint.sol";
import "@layerzerolabs/contracts/interfaces/ILayerZeroReceiver.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title CrossChainSTONERedemption
 * @dev Contract for cross-chain redemption of STONE tokens using LayerZero protocol.
 */
contract CrossChainSTONERedemption is ILayerZeroReceiver, Ownable {
    // LayerZero endpoint for message communication
    ILayerZeroEndpoint public immutable layerZeroEndpoint;

    // Address of the STONE token contract
    IERC20 public immutable stoneToken;

    // Mapping to track trusted remote chains and their contract addresses
    mapping(uint16 => bytes) public trustedRemoteChains;

    // Event emitted on cross-chain redemption
    event Redeemed(
        address indexed user,
        uint256 amount,
        uint16 dstChainId,
        bytes dstAddress
    );

    // Event emitted on receiving cross-chain funds
    event ReceivedFunds(
        uint16 srcChainId,
        bytes srcAddress,
        address indexed user,
        uint256 amount
    );

    /**
     * @dev Constructor to initialize the contract.
     * @param _layerZeroEndpoint Address of the LayerZero endpoint.
     * @param _stoneToken Address of the STONE token contract.
     */
    constructor(address _layerZeroEndpoint, address _stoneToken) {
        require(_layerZeroEndpoint != address(0), "Invalid LayerZeroEndpoint");
        require(_stoneToken != address(0), "Invalid STONE token address");
        layerZeroEndpoint = ILayerZeroEndpoint(_layerZeroEndpoint);
        stoneToken = IERC20(_stoneToken);
    }

    /**
     * @dev Redeem STONE tokens to another chain.
     * @param amount Amount of STONE tokens to redeem.
     * @param dstChainId The LayerZero destination chain ID.
     * @param dstAddress The destination address on the remote chain.
     */
    function redeem(uint256 amount, uint16 dstChainId, bytes calldata dstAddress) external {
        require(amount > 0, "Amount must be greater than 0");
        require(trustedRemoteChains[dstChainId].length > 0, "Untrusted destination chain");

        // Transfer STONE tokens from user to this contract
        require(stoneToken.transferFrom(msg.sender, address(this), amount), "Token transfer failed");

        // Encode payload with user address and amount
        bytes memory payload = abi.encode(msg.sender, amount);

        // Send message to remote chain using LayerZero
        layerZeroEndpoint.send{value: msg.value}(
            dstChainId,              // Destination chain ID
            trustedRemoteChains[dstChainId], // Destination address
            payload,                 // Encoded payload
            payable(msg.sender),     // Refund address for excess gas
            address(0),              // Zero payment address
            bytes("")                // Adapter params
        );

        emit Redeemed(msg.sender, amount, dstChainId, dstAddress);
    }

    /**
     * @dev Receive cross-chain message from LayerZero.
     * @param srcChainId ID of the source chain.
     * @param srcAddress Address of the sender contract on the source chain.
     * @param payload Encoded data containing the user address and amount.
     */
    function lzReceive(uint16 srcChainId, bytes calldata srcAddress, uint64, bytes calldata payload) external override {
        require(msg.sender == address(layerZeroEndpoint), "Caller is not LayerZero endpoint");
        require(keccak256(srcAddress) == keccak256(trustedRemoteChains[srcChainId]), "Untrusted source address");

        // Decode payload
        (address user, uint256 amount) = abi.decode(payload, (address, uint256));

        // Transfer STONE tokens to user
        require(stoneToken.transfer(user, amount), "Token transfer failed");

        emit ReceivedFunds(srcChainId, srcAddress, user, amount);
    }

    /**
     * @dev Add or update a trusted remote chain.
     * @param chainId ID of the remote chain.
     * @param remoteAddress Address of the trusted contract on the remote chain.
     */
    function setTrustedRemoteChain(uint16 chainId, bytes calldata remoteAddress) external onlyOwner {
        trustedRemoteChains[chainId] = remoteAddress;
    }

    /**
     * @dev Withdraw native tokens accumulated in the contract (primarily for gas refunds).
     * @param to Address to send the withdrawn funds.
     */
    function withdrawNative(address payable to) external onlyOwner {
        require(to != address(0), "Invalid withdrawal address");
        to.transfer(address(this).balance);
    }

    /**
     * @dev Withdraw STONE tokens accumulated in the contract.
     * @param amount Amount of STONE tokens to withdraw.
     * @param to Address to send the withdrawn tokens.
     */
    function withdrawSTONE(uint256 amount, address to) external onlyOwner {
        require(to != address(0), "Invalid withdrawal address");
        require(stoneToken.transfer(to, amount), "Token transfer failed");
    }

    // Fallback function to receive native tokens
    receive() external payable {}
}
```
