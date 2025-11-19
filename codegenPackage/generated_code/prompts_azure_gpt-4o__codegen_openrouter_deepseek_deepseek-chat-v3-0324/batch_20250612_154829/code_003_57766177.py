"""
Generated Code Metadata:
========================
Original URL: https://predelin.ru
Prompt: Write a Solidity smart contract to interact with Beethoven X's liquidity pools, enabling users to deposit and withdraw assets securely.
Generated: DETERMINISTIC_577661778558df45
Batch ID: 20250612_154829
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

interface IBeethovenVault {
    enum SwapKind { GIVEN_IN, GIVEN_OUT }
    
    struct FundManagement {
        address sender;
        bool fromInternalBalance;
        address payable recipient;
        bool toInternalBalance;
    }

    struct SingleSwap {
        bytes32 poolId;
        SwapKind kind;
        address assetIn;
        address assetOut;
        uint256 amount;
        bytes userData;
    }

    function swap(
        SingleSwap memory singleSwap,
        FundManagement memory funds,
        uint256 limit,
        uint256 deadline
    ) external payable returns (uint256);

    function joinPool(
        bytes32 poolId,
        address sender,
        address recipient,
        JoinPoolRequest memory request
    ) external payable;

    function exitPool(
        bytes32 poolId,
        address sender,
        address recipient,
        ExitPoolRequest memory request
    ) external payable;

    struct JoinPoolRequest {
        address[] assets;
        uint256[] maxAmountsIn;
        bytes userData;
        bool fromInternalBalance;
    }

    struct ExitPoolRequest {
        address[] assets;
        uint256[] minAmountsOut;
        bytes userData;
        bool toInternalBalance;
    }
}

contract BeethovenXPoolManager is Ownable, ReentrancyGuard {
    using SafeERC20 for IERC20;

    IBeethovenVault public immutable beethovenVault;

    constructor(address _beethovenVault) {
        require(_beethovenVault != address(0), "Invalid vault address");
        beethovenVault = IBeethovenVault(_beethovenVault);
    }

    /**
     * @dev Deposit assets into a Beethoven X liquidity pool
     * @param poolId The ID of the pool to join
     * @param assets Array of tokens in the pool
     * @param maxAmountsIn Max amounts of tokens to deposit
     * @param userData Encoded data for the join operation
     */
    function depositToPool(
        bytes32 poolId,
        address[] calldata assets,
        uint256[] calldata maxAmountsIn,
        bytes calldata userData
    ) external nonReentrant {
        require(assets.length == maxAmountsIn.length, "Array length mismatch");

        // Approve tokens to be spent by the vault
        for (uint256 i = 0; i < assets.length; i++) {
            if (maxAmountsIn[i] > 0) {
                IERC20(assets[i]).safeTransferFrom(msg.sender, address(this), maxAmountsIn[i]);
                IERC20(assets[i]).safeApprove(address(beethovenVault), maxAmountsIn[i]);
            }
        }

        IBeethovenVault.JoinPoolRequest memory request = IBeethovenVault.JoinPoolRequest({
            assets: assets,
            maxAmountsIn: maxAmountsIn,
            userData: userData,
            fromInternalBalance: false
        });

        beethovenVault.joinPool(poolId, address(this), msg.sender, request);
    }

    /**
     * @dev Withdraw assets from a Beethoven X liquidity pool
     * @param poolId The ID of the pool to exit
     * @param assets Array of tokens in the pool
     * @param minAmountsOut Minimum amounts of tokens to receive
     * @param userData Encoded data for the exit operation
     */
    function withdrawFromPool(
        bytes32 poolId,
        address[] calldata assets,
        uint256[] calldata minAmountsOut,
        bytes calldata userData
    ) external nonReentrant {
        require(assets.length == minAmountsOut.length, "Array length mismatch");

        IBeethovenVault.ExitPoolRequest memory request = IBeethovenVault.ExitPoolRequest({
            assets: assets,
            minAmountsOut: minAmountsOut,
            userData: userData,
            toInternalBalance: false
        });

        beethovenVault.exitPool(poolId, address(this), msg.sender, request);
    }

    /**
     * @dev Perform a swap through Beethoven X
     * @param poolId The ID of the pool to swap through
     * @param kind Swap type (GIVEN_IN or GIVEN_OUT)
     * @param assetIn Token to swap from
     * @param assetOut Token to swap to
     * @param amount Amount to swap
     * @param limit Minimum or maximum amount to receive (depending on swap kind)
     * @param deadline Deadline for the swap
     * @param userData Additional swap data
     */
    function swapTokens(
        bytes32 poolId,
        IBeethovenVault.SwapKind kind,
        address assetIn,
        address assetOut,
        uint256 amount,
        uint256 limit,
        uint256 deadline,
        bytes calldata userData
    ) external nonReentrant returns (uint256) {
        IERC20(assetIn).safeTransferFrom(msg.sender, address(this), amount);
        IERC20(assetIn).safeApprove(address(beethovenVault), amount);

        IBeethovenVault.SingleSwap memory singleSwap = IBeethovenVault.SingleSwap({
            poolId: poolId,
            kind: kind,
            assetIn: assetIn,
            assetOut: assetOut,
            amount: amount,
            userData: userData
        });

        IBeethovenVault.FundManagement memory funds = IBeethovenVault.FundManagement({
            sender: address(this),
            fromInternalBalance: false,
            recipient: payable(msg.sender),
            toInternalBalance: false
        });

        return beethovenVault.swap(singleSwap, funds, limit, deadline);
    }

    /**
     * @dev Emergency function to recover ERC20 tokens sent to the contract by mistake
     * @param tokenAddress Address of the token to recover
     * @param amount Amount to recover
     */
    function recoverERC20(address tokenAddress, uint256 amount) external onlyOwner {
        IERC20(tokenAddress).safeTransfer(owner(), amount);
    }
}
```
