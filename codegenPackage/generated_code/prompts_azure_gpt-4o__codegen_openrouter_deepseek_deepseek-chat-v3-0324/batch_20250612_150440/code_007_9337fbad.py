"""
Generated Code Metadata:
========================
Original URL: https://arbitrum-token-bridge-ey3dlgbqo-offchain-labs.vercel.app
Prompt: Suggest an approach for integrating the Arbitrum Token Bridge into a decentralized finance (DeFi) application.
Generated: DETERMINISTIC_9337fbadf98d1db9
Batch ID: 20250612_150440
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
import "@arbitrum/nitro-contracts/src/bridge/IInbox.sol";
import "@arbitrum/nitro-contracts/src/bridge/IOutbox.sol";

contract ArbitrumBridgeIntegration {
    using SafeERC20 for IERC20;

    // Arbitrum contracts
    address public immutable inboxAddress;
    address public immutable l1TokenAddress;
    address public immutable l2TokenAddress;

    // Events
    event TokensDeposited(address indexed user, uint256 amount, uint256 maxSubmissionCost);
    event TokensWithdrawn(address indexed user, uint256 amount);

    /**
     * @param _inboxAddress Address of Arbitrum's Inbox contract on L1
     * @param _l1TokenAddress Address of ERC20 token on L1
     * @param _l2TokenAddress Address of corresponding ERC20 token on L2
     */
    constructor(
        address _inboxAddress,
        address _l1TokenAddress,
        address _l2TokenAddress
    ) {
        require(_inboxAddress != address(0), "Invalid inbox address");
        require(_l1TokenAddress != address(0), "Invalid L1 token address");
        require(_l2TokenAddress != address(0), "Invalid L2 token address");

        inboxAddress = _inboxAddress;
        l1TokenAddress = _l1TokenAddress;
        l2TokenAddress = _l2TokenAddress;
    }

    /**
     * @notice Deposit tokens from L1 to L2
     * @param amount Amount of tokens to deposit
     * @param maxGas Max gas for L2 execution
     * @param gasPriceBid Gas price bid for L2 execution
     * @param maxSubmissionCost Max submission cost for retryable ticket
     */
    function depositTokens(
        uint256 amount,
        uint256 maxGas,
        uint256 gasPriceBid,
        uint256 maxSubmissionCost
    ) external payable {
        require(amount > 0, "Amount must be greater than 0");
        require(msg.value >= maxSubmissionCost + (maxGas * gasPriceBid), "Insufficient ETH for fees");

        // Transfer tokens from user to this contract
        IERC20(l1TokenAddress).safeTransferFrom(msg.sender, address(this), amount);

        // Approve token transfer to bridge
        IERC20(l1TokenAddress).approve(inboxAddress, amount);

        // Create retryable ticket to deposit tokens
        bytes memory data = abi.encodeWithSignature(
            "depositERC20To(address,address,address,uint256,uint256,uint256,uint256)",
            l1TokenAddress,
            l2TokenAddress,
            msg.sender,
            amount,
            maxGas,
            gasPriceBid,
            maxSubmissionCost
        );

        IInbox(inboxAddress).createRetryableTicket{value: msg.value}(
            inboxAddress, // target
            0, // arbTxCallValue
            maxSubmissionCost,
            msg.sender, // refundAddress
            msg.sender, // beneficiary
            maxGas,
            gasPriceBid,
            data
        );

        emit TokensDeposited(msg.sender, amount, maxSubmissionCost);
    }

    /**
     * @notice Withdraw tokens from L2 to L1 (initiate withdrawal)
     * @dev This function should be called on L2
     * @param amount Amount of tokens to withdraw
     */
    function withdrawTokens(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");

        // Transfer tokens from user to this contract
        IERC20(l2TokenAddress).safeTransferFrom(msg.sender, address(this), amount);

        // Approve token transfer to bridge
        IERC20(l2TokenAddress).approve(inboxAddress, amount);

        // Initiate withdrawal
        IOutbox(outboxAddress).initiateWithdrawal(
            l2TokenAddress,
            msg.sender,
            amount
        );

        emit TokensWithdrawn(msg.sender, amount);
    }

    /**
     * @notice Complete withdrawal from L2 to L1
     * @dev This function should be called on L1 after the challenge period
     * @param proof Merkle proof of withdrawal
     * @param index Index of withdrawal in Merkle tree
     * @param l2Sender Address that initiated withdrawal on L2
     * @param to Address to receive tokens on L1
     * @param l2Block L2 block number of withdrawal
     * @param l1Block L1 block number of withdrawal
     * @param l2Timestamp L2 timestamp of withdrawal
     * @param amount Amount of tokens to withdraw
     * @param data Additional data
     */
    function completeWithdrawal(
        bytes32[] calldata proof,
        uint256 index,
        address l2Sender,
        address to,
        uint256 l2Block,
        uint256 l1Block,
        uint256 l2Timestamp,
        uint256 amount,
        bytes calldata data
    ) external {
        IOutbox(outboxAddress).executeTransaction(
            proof,
            index,
            l2Sender,
            to,
            l2Block,
            l1Block,
            l2Timestamp,
            amount,
            data
        );

        // Transfer tokens to recipient
        IERC20(l1TokenAddress).safeTransfer(to, amount);
    }
}
```
