"""
Generated Code Metadata:
========================
Original URL: https://validationdapp.pages.dev
Prompt: Design a smart contract that utilizes Multichain's zkRouter protocol for secure and private cross-chain transactions.
Generated: DETERMINISTIC_5d3e7913e7a75531
Batch ID: 20250622_204752
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/token/ERC20/SafeERC20.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";
import "@multichain/zkrouter/contracts/ZKRouter.sol";

/**
 * @title Multichain zkRouter Cross-Chain Bridge Contract
 * @author [Your Name]
 * @notice This contract enables secure and private cross-chain transactions using Multichain's zkRouter protocol.
 */
contract MultichainZKRouterBridge {
    using SafeMath for uint256;
    using SafeERC20 for IERC20;

    // Mapping of supported tokens and their corresponding addresses
    mapping(address => mapping(address => bool)) public supportedTokens;

    // Mapping of pending cross-chain transactions
    mapping(bytes32 => bool) public pendingTransactions;

    // Multichain zkRouter protocol instance
    ZKRouter public zkRouter;

    /**
     * @param _zkRouterAddress Address of the Multichain zkRouter protocol instance
     */
    constructor(address _zkRouterAddress) {
        zkRouter = ZKRouter(_zkRouterAddress);
    }

    /**
     * @dev Adds a token to the list of supported tokens
     * @param _tokenAddress Address of the token to add
     * @param _chainId Chain ID of the token
     */
    function addSupportedToken(address _tokenAddress, uint256 _chainId) public onlyOwner {
        supportedTokens[_tokenAddress][_chainId] = true;
    }

    /**
     * @dev Removes a token from the list of supported tokens
     * @param _tokenAddress Address of the token to remove
     * @param _chainId Chain ID of the token
     */
    function removeSupportedToken(address _tokenAddress, uint256 _chainId) public onlyOwner {
        supportedTokens[_tokenAddress][_chainId] = false;
    }

    /**
     * @dev Initiates a cross-chain transaction using the Multichain zkRouter protocol
     * @param _tokenAddress Address of the token to transfer
     * @param _amount Amount of tokens to transfer
     * @param _dstChainId Destination chain ID
     * @param _receiver Address of the receiver on the destination chain
     * @param _callData Additional call data for the transaction
     */
    function initiateCrossChainTransaction(
        address _tokenAddress,
        uint256 _amount,
        uint256 _dstChainId,
        address _receiver,
        bytes memory _callData
    ) public {
        // Check if token is supported
        require(supportedTokens[_tokenAddress][_dstChainId], "Token not supported");

        // Transfer tokens from sender to contract
        IERC20(_tokenAddress).safeTransferFrom(msg.sender, address(this), _amount);

        // Encode transaction data
        bytes memory encodedData = abi.encode(_tokenAddress, _amount, _receiver, _callData);

        // Generate transaction ID
        bytes32 transactionId = keccak256(encodedData);

        // Check if transaction is not already pending
        require(!pendingTransactions[transactionId], "Transaction already pending");

        // Mark transaction as pending
        pendingTransactions[transactionId] = true;

        // Execute cross-chain transaction using zkRouter
        zkRouter.executeTransaction(
            _dstChainId,
            _receiver,
            _tokenAddress,
            _amount,
            _callData,
            encodedData
        );
    }

    /**
     * @dev Completes a cross-chain transaction using the Multichain zkRouter protocol
     * @param _transactionId ID of the transaction to complete
     * @param _proof Proof of the transaction
     */
    function completeCrossChainTransaction(bytes32 _transactionId, bytes memory _proof) public {
        // Check if transaction is pending
        require(pendingTransactions[_transactionId], "Transaction not pending");

        // Verify transaction proof
        require(zkRouter.verifyProof(_transactionId, _proof), "Invalid proof");

        // Mark transaction as completed
        pendingTransactions[_transactionId] = false;

        // Decode transaction data
        bytes memory encodedData = zkRouter.getTransactionData(_transactionId);
        (address tokenAddress, uint256 amount, address receiver, bytes memory callData) = abi.decode(
            encodedData,
            (address, uint256, address, bytes)
        );

        // Transfer tokens to receiver
        IERC20(tokenAddress).safeTransfer(receiver, amount);

        // Execute additional call data
        if (callData.length > 0) {
            (bool success, ) = receiver.call(callData);
            require(success, "Call failed");
        }
    }

    modifier onlyOwner {
        require(msg.sender == owner, "Only owner");
        _;
    }

    address public owner;

    constructor() {
        owner = msg.sender;
    }
}
```
