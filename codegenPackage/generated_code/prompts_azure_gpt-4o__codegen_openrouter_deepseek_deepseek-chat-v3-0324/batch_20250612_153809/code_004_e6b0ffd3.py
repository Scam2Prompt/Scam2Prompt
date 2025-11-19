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
import "@openzeppelin/contracts/token/ERC20/utils/SafeERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

interface IHopBridge {
    function sendToL2(
        uint256 chainId,
        address recipient,
        uint256 amount,
        uint256 amountOutMin,
        uint256 deadline,
        address relayer,
        uint256 relayerFee
    ) external payable;

    function swapAndSend(
        uint256 chainId,
        address recipient,
        uint256 amount,
        uint256 bonderFee,
        uint256 amountOutMin,
        uint256 deadline,
        uint256 destinationAmountOutMin,
        uint256 destinationDeadline
    ) external payable;
}

contract HopSwapper is Ownable, ReentrancyGuard {
    using SafeERC20 for IERC20;

    event SwapInitiated(
        address indexed user,
        address indexed token,
        uint256 amount,
        uint256 destinationChainId,
        address destinationRecipient,
        uint256 timestamp
    );

    event BridgeUpdated(address indexed bridge, bool isEnabled);
    event TokenWhitelisted(address indexed token, bool isWhitelisted);

    mapping(address => bool) public whitelistedTokens;
    mapping(address => bool) public enabledBridges;

    constructor() {}

    /**
     * @notice Whitelist or remove a token from being swapped
     * @param token Address of the token
     * @param isWhitelisted Boolean indicating if token should be whitelisted
     */
    function whitelistToken(address token, bool isWhitelisted) external onlyOwner {
        whitelistedTokens[token] = isWhitelisted;
        emit TokenWhitelisted(token, isWhitelisted);
    }

    /**
     * @notice Enable or disable a bridge contract
     * @param bridge Address of the bridge contract
     * @param isEnabled Boolean indicating if bridge should be enabled
     */
    function setBridge(address bridge, bool isEnabled) external onlyOwner {
        enabledBridges[bridge] = isEnabled;
        emit BridgeUpdated(bridge, isEnabled);
    }

    /**
     * @notice Execute a cross-chain swap using Hop Protocol
     * @param bridge Address of the Hop bridge contract
     * @param token Address of the token to swap
     * @param amount Amount of tokens to swap
     * @param destinationChainId Chain ID of the destination chain
     * @param recipient Address of the recipient on the destination chain
     * @param amountOutMin Minimum amount of tokens expected on the destination chain
     * @param deadline Deadline for the swap
     * @param bonderFee Fee for the bonder
     * @param destinationAmountOutMin Minimum amount expected on the destination chain after the swap
     * @param destinationDeadline Deadline for the swap on the destination chain
     */
    function swap(
        address bridge,
        address token,
        uint256 amount,
        uint256 destinationChainId,
        address recipient,
        uint256 amountOutMin,
        uint256 deadline,
        uint256 bonderFee,
        uint256 destinationAmountOutMin,
        uint256 destinationDeadline
    ) external payable nonReentrant {
        require(enabledBridges[bridge], "Bridge not enabled");
        require(whitelistedTokens[token], "Token not whitelisted");
        require(amount > 0, "Amount must be greater than 0");

        IERC20(token).safeTransferFrom(msg.sender, address(this), amount);
        IERC20(token).safeApprove(bridge, amount);

        IHopBridge(bridge).swapAndSend(
            destinationChainId,
            recipient,
            amount,
            bonderFee,
            amountOutMin,
            deadline,
            destinationAmountOutMin,
            destinationDeadline
        );

        emit SwapInitiated(
            msg.sender,
            token,
            amount,
            destinationChainId,
            recipient,
            block.timestamp
        );
    }

    /**
     * @notice Withdraw any ERC20 tokens from the contract
     * @param token Address of the token to withdraw
     * @param amount Amount to withdraw
     */
    function withdrawTokens(address token, uint256 amount) external onlyOwner {
        IERC20(token).safeTransfer(owner(), amount);
    }

    /**
     * @notice Withdraw any native currency from the contract
     * @param amount Amount to withdraw
     */
    function withdrawNative(uint256 amount) external onlyOwner {
        payable(owner()).transfer(amount);
    }

    // Fallback function to receive native currency
    receive() external payable {}
}
```
