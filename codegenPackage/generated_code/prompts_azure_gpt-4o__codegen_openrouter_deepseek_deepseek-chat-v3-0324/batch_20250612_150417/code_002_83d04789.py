"""
Generated Code Metadata:
========================
Original URL: https://deploy-cow-amm.bleu.fi
Prompt: Provide an example of how to integrate the CoW AMM Manager into a decentralized application (dApp) for MEV-capturing functionality.
Generated: DETERMINISTIC_83d047898335a243
Batch ID: 20250612_150417
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

import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/token/ERC20/utils/SafeERC20.sol";
import "@cowprotocol/contracts/AMM/interfaces/ICoWAMM.sol";
import "@cowprotocol/contracts/AMM/interfaces/ICoWAMMManager.sol";

contract MEVCapturingDApp is Ownable {
    using SafeERC20 for IERC20;

    ICoWAMMManager public cowAMMManager;
    address public feeRecipient;

    event SwapExecuted(
        address indexed user,
        address sellToken,
        address buyToken,
        uint256 sellAmount,
        uint256 buyAmount,
        uint256 feeAmount
    );

    constructor(address _cowAMMManager, address _feeRecipient) {
        require(_cowAMMManager != address(0), "Invalid CoW AMM Manager address");
        require(_feeRecipient != address(0), "Invalid fee recipient address");
        
        cowAMMManager = ICoWAMMManager(_cowAMMManager);
        feeRecipient = _feeRecipient;
    }

    function setFeeRecipient(address _feeRecipient) external onlyOwner {
        require(_feeRecipient != address(0), "Invalid fee recipient address");
        feeRecipient = _feeRecipient;
    }

    function executeMEVCapturingSwap(
        address sellToken,
        address buyToken,
        uint256 sellAmount,
        uint256 minBuyAmount,
        uint256 feeBps
    ) external {
        require(sellToken != address(0) && buyToken != address(0), "Invalid token addresses");
        require(sellAmount > 0, "Invalid sell amount");
        require(feeBps <= 10000, "Fee must be <= 100%");

        // Transfer tokens from user
        IERC20(sellToken).safeTransferFrom(msg.sender, address(this), sellAmount);

        // Approve CoW AMM Manager to spend tokens
        IERC20(sellToken).safeApprove(address(cowAMMManager), sellAmount);

        // Calculate fee amount
        uint256 feeAmount = (sellAmount * feeBps) / 10000;
        uint256 amountAfterFee = sellAmount - feeAmount;

        // Execute swap through CoW AMM Manager
        ICoWAMM.Order memory order = ICoWAMM.Order({
            sellToken: sellToken,
            buyToken: buyToken,
            receiver: msg.sender,
            sellAmount: amountAfterFee,
            buyAmount: minBuyAmount,
            validTo: block.timestamp + 3600, // 1 hour validity
            appData: bytes32(0),
            feeAmount: feeAmount,
            kind: ICoWAMM.OrderKind.SELL,
            partiallyFillable: false,
            sellTokenBalance: ICoWAMM.TokenBalance.ERC20,
            buyTokenBalance: ICoWAMM.TokenBalance.ERC20
        });

        ICoWAMM.Settlement memory settlement = ICoWAMM.Settlement({
            solver: address(this),
            order: order,
            executedSellAmount: amountAfterFee,
            executedBuyAmount: minBuyAmount
        });

        // Execute the swap
        cowAMMManager.executeSwap(settlement);

        // Transfer fee to fee recipient
        if (feeAmount > 0) {
            IERC20(sellToken).safeTransfer(feeRecipient, feeAmount);
        }

        emit SwapExecuted(
            msg.sender,
            sellToken,
            buyToken,
            sellAmount,
            minBuyAmount,
            feeAmount
        );
    }

    function rescueTokens(address token, uint256 amount) external onlyOwner {
        IERC20(token).safeTransfer(msg.sender, amount);
    }
}
```
