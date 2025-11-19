"""
Generated Code Metadata:
========================
Original URL: https://deploy-cow-amm.bleu.fi
Prompt: "Generate code to integrate CoW AMM with Safe for secure trades, using Solidity and OpenZeppelin libraries."
Generated: DETERMINISTIC_0c348a9b2de23eac
Batch ID: 20250622_211951
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
import "@gnosis.pm/safe-contracts/contracts/GnosisSafe.sol";
import "@gnosis.pm/safe-contracts/contracts/proxies/GnosisSafeProxyFactory.sol";

interface ICoWAMM {
    function swap(
        IERC20 sellToken,
        IERC20 buyToken,
        uint256 sellAmount,
        uint256 buyAmount,
        uint256 validTo,
        bytes32 feeDiscount
    ) external returns (uint256 boughtAmount);
}

contract CoWAMMSafeIntegration is Ownable {
    using SafeERC20 for IERC20;

    GnosisSafeProxyFactory public immutable safeProxyFactory;
    ICoWAMM public immutable cowAMM;

    event TradeExecuted(
        address indexed safeAddress,
        address sellToken,
        address buyToken,
        uint256 sellAmount,
        uint256 buyAmount
    );

    constructor(GnosisSafeProxyFactory _safeProxyFactory, ICoWAMM _cowAMM) {
        require(address(_safeProxyFactory) != address(0), "Invalid Safe Factory");
        require(address(_cowAMM) != address(0), "Invalid CoW AMM");

        safeProxyFactory = _safeProxyFactory;
        cowAMM = _cowAMM;
    }

    /**
     * @dev Executes a trade via CoW AMM from a Gnosis Safe
     * @param safeAddress Address of the Gnosis Safe
     * @param sellToken Token to sell
     * @param buyToken Token to buy
     * @param sellAmount Amount of sellToken to swap
     * @param buyAmount Minimum amount of buyToken to receive
     * @param validTo Deadline for the trade
     * @param feeDiscount Fee discount data
     * @param signatures Signatures from Safe owners
     */
    function executeTrade(
        address safeAddress,
        IERC20 sellToken,
        IERC20 buyToken,
        uint256 sellAmount,
        uint256 buyAmount,
        uint256 validTo,
        bytes32 feeDiscount,
        bytes memory signatures
    ) external onlyOwner {
        require(safeAddress != address(0), "Invalid Safe address");
        require(address(sellToken) != address(0), "Invalid sell token");
        require(address(buyToken) != address(0), "Invalid buy token");
        require(sellAmount > 0, "Invalid sell amount");
        require(buyAmount > 0, "Invalid buy amount");
        require(validTo > block.timestamp, "Expired deadline");

        GnosisSafe safe = GnosisSafe(payable(safeAddress));

        // Transfer tokens from Safe to this contract
        bytes memory transferCallData = abi.encodeWithSelector(
            IERC20.transferFrom.selector,
            safeAddress,
            address(this),
            sellAmount
        );

        safe.execTransaction(
            address(sellToken),
            0,
            transferCallData,
            Enum.Operation.Call,
            0,
            0,
            0,
            address(0),
            payable(0),
            signatures
        );

        // Approve CoW AMM to spend sellToken
        sellToken.safeApprove(address(cowAMM), sellAmount);

        // Execute swap
        uint256 boughtAmount = cowAMM.swap(
            sellToken,
            buyToken,
            sellAmount,
            buyAmount,
            validTo,
            feeDiscount
        );

        require(boughtAmount >= buyAmount, "Insufficient buy amount");

        // Transfer bought tokens back to Safe
        buyToken.safeTransfer(safeAddress, boughtAmount);

        emit TradeExecuted(
            safeAddress,
            address(sellToken),
            address(buyToken),
            sellAmount,
            boughtAmount
        );
    }

    /**
     * @dev Emergency function to recover ERC20 tokens sent by mistake
     * @param token Address of the token to recover
     * @param amount Amount to recover
     */
    function recoverERC20(IERC20 token, uint256 amount) external onlyOwner {
        require(address(token) != address(0), "Invalid token");
        token.safeTransfer(owner(), amount);
    }
}
```
