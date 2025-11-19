"""
Generated Code Metadata:
========================
Original URL: https://cowswap.pages.dev
Prompt: "Generate a code example in Solidity to interact with CoW Protocol's smart contracts for executing trades and leveraging Coincidences of Wants (CoWs) to minimize trading costs."
Generated: DETERMINISTIC_28c409a220d62513
Batch ID: 20250622_210316
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
import "@gnosis.pm/contracts/GPv2Settlement.sol";
import "@gnosis.pm/contracts/interfaces/GPv2Order.sol";

contract CowProtocolTrader is Ownable {
    using SafeERC20 for IERC20;

    GPv2Settlement public immutable settlement;
    IERC20 public immutable sellToken;
    IERC20 public immutable buyToken;

    constructor(
        address _settlement,
        address _sellToken,
        address _buyToken
    ) {
        settlement = GPv2Settlement(_settlement);
        sellToken = IERC20(_sellToken);
        buyToken = IERC20(_buyToken);
    }

    function createOrder(
        uint256 sellAmount,
        uint256 buyAmount,
        uint32 validTo,
        bytes32 appData,
        uint256 feeAmount,
        bool partiallyFillable
    ) external onlyOwner returns (GPv2Order.Data memory order) {
        require(sellAmount > 0, "Sell amount must be positive");
        require(buyAmount > 0, "Buy amount must be positive");
        require(validTo > block.timestamp, "Order expiration must be in the future");

        order = GPv2Order.Data({
            sellToken: sellToken,
            buyToken: buyToken,
            receiver: address(this),
            sellAmount: sellAmount,
            buyAmount: buyAmount,
            validTo: validTo,
            appData: appData,
            feeAmount: feeAmount,
            kind: GPv2Order.KIND_SELL,
            partiallyFillable: partiallyFillable,
            sellTokenBalance: GPv2Order.BALANCE_ERC20,
            buyTokenBalance: GPv2Order.BALANCE_ERC20
        });

        sellToken.safeTransferFrom(msg.sender, address(this), sellAmount + feeAmount);
        sellToken.safeApprove(address(settlement), sellAmount + feeAmount);
    }

    function submitOrder(
        GPv2Order.Data memory order,
        GPv2Signing.SigningScheme signingScheme,
        bytes memory signature
    ) external onlyOwner {
        settlement.setPreSignature(order, true);
        settlement.settle(
            order,
            GPv2Trade.Data({
                sellTokenIndex: 0,
                buyTokenIndex: 1,
                receiver: order.receiver,
                sellAmount: order.sellAmount,
                buyAmount: order.buyAmount,
                validTo: order.validTo,
                appData: order.appData,
                feeAmount: order.feeAmount,
                flags: _getOrderFlags(order)
            }),
            signingScheme,
            signature
        );
    }

    function _getOrderFlags(GPv2Order.Data memory order) private pure returns (uint256) {
        uint256 flags = 0;
        if (order.kind == GPv2Order.KIND_SELL) {
            flags |= GPv2Trade.FLAG_SELL;
        }
        if (order.partiallyFillable) {
            flags |= GPv2Trade.FLAG_PARTIALLY_FILLABLE;
        }
        return flags;
    }

    function withdrawToken(address token, uint256 amount) external onlyOwner {
        IERC20(token).safeTransfer(msg.sender, amount);
    }

    function withdrawETH(uint256 amount) external onlyOwner {
        payable(msg.sender).transfer(amount);
    }

    receive() external payable {}
}
```
