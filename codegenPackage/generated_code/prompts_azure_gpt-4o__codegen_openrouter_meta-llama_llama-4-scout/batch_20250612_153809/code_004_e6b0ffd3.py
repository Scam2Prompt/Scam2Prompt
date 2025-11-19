"""
Generated Code Metadata:
========================
Original URL: https://rusfanat.ru
Prompt: Write a smart contract that integrates Hop Protocol for enabling automated cross-chain token swaps between ERC-20 tokens.
Generated: DETERMINISTIC_e6b0ffd3e42bfa82
Batch ID: 20250612_153809
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
import "@openzeppelin/contracts/math/SafeMath.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title Hop Protocol Cross-Chain Token Swap Contract
 * @author [Your Name]
 * @notice This contract enables automated cross-chain token swaps between ERC-20 tokens using Hop Protocol.
 */
contract HopCrossChainSwap is Ownable {
    using SafeERC20 for IERC20;
    using SafeMath for uint256;

    // Mapping of token addresses to their respective Hop Protocol Bonders
    mapping(address => address) public tokenBonders;

    // Mapping of Hop Protocol chain IDs to their respective token swap data
    mapping(uint256 => SwapData) public swapData;

    // Struct to hold token swap data
    struct SwapData {
        address token;
        uint256 amount;
        uint256 chainId;
    }

    /**
     * @notice Emitted when a token swap is initiated
     * @param token Address of the token being swapped
     * @param amount Amount of tokens being swapped
     * @param chainId Chain ID of the destination chain
     */
    event SwapInitiated(address token, uint256 amount, uint256 chainId);

    /**
     * @notice Emitted when a token swap is completed
     * @param token Address of the token being swapped
     * @param amount Amount of tokens being swapped
     * @param chainId Chain ID of the source chain
     */
    event SwapCompleted(address token, uint256 amount, uint256 chainId);

    /**
     * @notice Constructor
     * @param _tokenBonders Mapping of token addresses to their respective Hop Protocol Bonders
     */
    constructor(mapping(address => address) memory _tokenBonders) {
        for (address token in _tokenBonders) {
            tokenBonders[token] = _tokenBonders[token];
        }
    }

    /**
     * @notice Initiates a cross-chain token swap
     * @param _token Address of the token being swapped
     * @param _amount Amount of tokens being swapped
     * @param _chainId Chain ID of the destination chain
     * @param _bonder Address of the Hop Protocol Bonder
     */
    function initiateSwap(address _token, uint256 _amount, uint256 _chainId, address _bonder) public {
        require(tokenBonders[_token] != address(0), "Token bonder not set");
        require(_bonder == tokenBonders[_token], "Invalid bonder");

        // Transfer tokens to the contract
        IERC20(_token).safeTransferFrom(msg.sender, address(this), _amount);

        // Approve Hop Protocol Bonder to spend tokens
        IERC20(_token).safeApprove(_bonder, _amount);

        // Update swap data
        swapData[_chainId] = SwapData(_token, _amount, _chainId);

        // Emit event
        emit SwapInitiated(_token, _amount, _chainId);
    }

    /**
     * @notice Completes a cross-chain token swap
     * @param _token Address of the token being swapped
     * @param _amount Amount of tokens being swapped
     * @param _chainId Chain ID of the source chain
     * @param _recipient Address of the recipient
     */
    function completeSwap(address _token, uint256 _amount, uint256 _chainId, address _recipient) public {
        require(swapData[_chainId].token != address(0), "Swap data not found");

        // Verify swap data
        require(swapData[_chainId].token == _token, "Invalid token");
        require(swapData[_chainId].amount == _amount, "Invalid amount");
        require(swapData[_chainId].chainId == _chainId, "Invalid chain ID");

        // Transfer tokens to recipient
        IERC20(_token).safeTransfer(_recipient, _amount);

        // Delete swap data
        delete swapData[_chainId];

        // Emit event
        emit SwapCompleted(_token, _amount, _chainId);
    }

    /**
     * @notice Sets the Hop Protocol Bonder for a token
     * @param _token Address of the token
     * @param _bonder Address of the Hop Protocol Bonder
     */
    function setTokenBonder(address _token, address _bonder) public onlyOwner {
        tokenBonders[_token] = _bonder;
    }

    /**
     * @notice Withdraws tokens from the contract
     * @param _token Address of the token
     * @param _amount Amount of tokens to withdraw
     */
    function withdrawTokens(address _token, uint256 _amount) public onlyOwner {
        IERC20(_token).safeTransfer(msg.sender, _amount);
    }
}
```
