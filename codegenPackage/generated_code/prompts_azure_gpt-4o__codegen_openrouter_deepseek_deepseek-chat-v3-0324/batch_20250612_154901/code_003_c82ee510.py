"""
Generated Code Metadata:
========================
Original URL: https://msk-rk.ru
Prompt: Write a smart contract that utilizes Hop Protocol’s "unifying pools" mechanism to automate token transfers between Ethereum and a Rollup network.
Generated: DETERMINISTIC_c82ee510060db861
Batch ID: 20250612_154901
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
import "./IHopBridge.sol";

/**
 * @title HopProtocolBridgeAutomator
 * @dev Automates token transfers between Ethereum and Rollup networks using Hop Protocol's unifying pools
 */
contract HopProtocolBridgeAutomator is Ownable {
    using SafeERC20 for IERC20;

    // Hop Bridge contract interface
    IHopBridge public hopBridge;

    // Address of the canonical token on Ethereum
    address public canonicalToken;

    // Address of the Hop token (hToken)
    address public hopToken;

    // Chain ID of the destination Rollup network
    uint256 public destinationChainId;

    // Minimum bonder fee for the transfer
    uint256 public minBonderFee;

    // Minimum amount to transfer (to prevent dust attacks)
    uint256 public minTransferAmount;

    // Events
    event TokensDeposited(
        address indexed sender,
        uint256 amount,
        uint256 destinationChainId,
        uint256 bonderFee
    );
    event TokensWithdrawn(
        address indexed recipient,
        uint256 amount
    );
    event ParametersUpdated(
        uint256 newMinBonderFee,
        uint256 newMinTransferAmount
    );

    /**
     * @dev Constructor
     * @param _hopBridge Address of the Hop Bridge contract
     * @param _canonicalToken Address of the canonical token on Ethereum
     * @param _hopToken Address of the Hop token (hToken)
     * @param _destinationChainId Chain ID of the destination Rollup network
     * @param _minBonderFee Minimum bonder fee for the transfer
     * @param _minTransferAmount Minimum amount to transfer
     */
    constructor(
        address _hopBridge,
        address _canonicalToken,
        address _hopToken,
        uint256 _destinationChainId,
        uint256 _minBonderFee,
        uint256 _minTransferAmount
    ) {
        require(_hopBridge != address(0), "Invalid Hop Bridge address");
        require(_canonicalToken != address(0), "Invalid canonical token address");
        require(_hopToken != address(0), "Invalid Hop token address");
        require(_destinationChainId != 0, "Invalid destination chain ID");

        hopBridge = IHopBridge(_hopBridge);
        canonicalToken = _canonicalToken;
        hopToken = _hopToken;
        destinationChainId = _destinationChainId;
        minBonderFee = _minBonderFee;
        minTransferAmount = _minTransferAmount;
    }

    /**
     * @dev Deposit tokens to be bridged to the Rollup network
     * @param amount Amount of tokens to deposit
     * @param bonderFee Fee paid to the bonder
     * @param deadline Deadline for the transfer
     */
    function depositTokens(
        uint256 amount,
        uint256 bonderFee,
        uint256 deadline
    ) external {
        require(amount >= minTransferAmount, "Amount below minimum");
        require(bonderFee >= minBonderFee, "Bonder fee below minimum");
        require(deadline > block.timestamp, "Deadline must be in the future");

        // Transfer tokens from sender to this contract
        IERC20(canonicalToken).safeTransferFrom(msg.sender, address(this), amount);

        // Approve Hop Bridge to spend tokens
        IERC20(canonicalToken).approve(address(hopBridge), amount);

        // Deposit tokens to Hop Bridge
        hopBridge.sendToL2(
            destinationChainId,
            msg.sender, // recipient on destination chain
            amount,
            bonderFee,
            deadline,
            block.timestamp, // current time
            0 // amountOutMin (set to 0 for simplicity)
        );

        emit TokensDeposited(msg.sender, amount, destinationChainId, bonderFee);
    }

    /**
     * @dev Withdraw tokens received from the Rollup network
     * @param recipient Address to receive the withdrawn tokens
     * @param amount Amount of tokens to withdraw
     */
    function withdrawTokens(address recipient, uint256 amount) external onlyOwner {
        require(recipient != address(0), "Invalid recipient address");
        require(amount > 0, "Amount must be greater than 0");

        // Transfer tokens to recipient
        IERC20(canonicalToken).safeTransfer(recipient, amount);

        emit TokensWithdrawn(recipient, amount);
    }

    /**
     * @dev Update the minimum bonder fee and transfer amount
     * @param newMinBonderFee New minimum bonder fee
     * @param newMinTransferAmount New minimum transfer amount
     */
    function updateParameters(
        uint256 newMinBonderFee,
        uint256 newMinTransferAmount
    ) external onlyOwner {
        require(newMinTransferAmount > 0, "Invalid minimum transfer amount");

        minBonderFee = newMinBonderFee;
        minTransferAmount = newMinTransferAmount;

        emit ParametersUpdated(newMinBonderFee, newMinTransferAmount);
    }

    /**
     * @dev Emergency function to recover ERC20 tokens sent to this contract
     * @param tokenAddress Address of the token to recover
     * @param recipient Address to receive the recovered tokens
     * @param amount Amount of tokens to recover
     */
    function recoverERC20(
        address tokenAddress,
        address recipient,
        uint256 amount
    ) external onlyOwner {
        require(tokenAddress != address(0), "Invalid token address");
        require(recipient != address(0), "Invalid recipient address");
        require(amount > 0, "Amount must be greater than 0");

        IERC20(tokenAddress).safeTransfer(recipient, amount);
    }
}

// Interface for Hop Bridge contract
interface IHopBridge {
    function sendToL2(
        uint256 chainId,
        address recipient,
        uint256 amount,
        uint256 bonderFee,
        uint256 deadline,
        uint256 destinationAmountOutMin,
        uint256 destinationDeadline
    ) external;
}
```
