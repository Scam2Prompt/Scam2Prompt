"""
Generated Code Metadata:
========================
Original URL: https://opensea.io
Prompt: Write a function in Solidity to interact with OpenSea's smart contract and perform a basic operation such as buying an NFT.
Generated: DETERMINISTIC_83e062b7eca3f303
Batch ID: 20250622_205139
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

import "@openzeppelin/contracts/token/ERC721/IERC721.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/utils/Address.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

interface IOpenSeaExchange {
    function atomicMatch_(
        address[14] memory addrs,
        uint256[18] memory uints,
        uint8[8] memory feeMethodsSidesKindsHowToCalls,
        bytes memory calldataBuy,
        bytes memory calldataSell,
        bytes memory replacementPatternBuy,
        bytes memory replacementPatternSell,
        bytes memory staticExtradataBuy,
        bytes memory staticExtradataSell,
        uint8[2] memory vs,
        bytes32[5] memory rssMetadata
    ) external payable;
}

contract OpenSeaNFTPurchaser is ReentrancyGuard {
    using Address for address payable;

    address public constant OPENSEA_EXCHANGE = 0x7f268357A8c2552623316e2562D90e642bB538E5;
    address public constant WETH = 0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2;

    /**
     * @notice Buy an NFT from OpenSea
     * @param addrs [0] = registry address
     *              [1] = maker address
     *              [2] = static target address
     *              [3] = payment token address (WETH)
     *              [4] = collection address
     *              [5] = token recipient
     * @param uints [0] = maker relayer fee
     *              [1] = taker relayer fee
     *              [2] = maker protocol fee
     *              [3] = taker protocol fee
     *              [4] = base price
     *              [5] = extra price
     *              [6] = listing time
     *              [7] = expiration time
     *              [8] = salt
     * @param feeMethodsSidesKindsHowToCalls Fee method, side, kind, and how to call
     * @param calldataBuy Calldata for buy order
     * @param calldataSell Calldata for sell order
     * @param replacementPatternBuy Replacement pattern for buy order
     * @param replacementPatternSell Replacement pattern for sell order
     * @param staticExtradataBuy Static extradata for buy order
     * @param staticExtradataSell Static extradata for sell order
     * @param vs Signature v values
     * @param rssMetadata Signature r and s values
     */
    function buyNFT(
        address[14] memory addrs,
        uint256[18] memory uints,
        uint8[8] memory feeMethodsSidesKindsHowToCalls,
        bytes memory calldataBuy,
        bytes memory calldataSell,
        bytes memory replacementPatternBuy,
        bytes memory replacementPatternSell,
        bytes memory staticExtradataBuy,
        bytes memory staticExtradataSell,
        uint8[2] memory vs,
        bytes32[5] memory rssMetadata
    ) external payable nonReentrant {
        require(addrs[3] == WETH, "Only WETH payments supported");
        require(msg.value >= uints[4], "Insufficient payment");

        // Approve WETH if needed
        if (IERC20(WETH).allowance(address(this), OPENSEA_EXCHANGE) < uints[4]) {
            IERC20(WETH).approve(OPENSEA_EXCHANGE, type(uint256).max);
        }

        // Convert ETH to WETH if needed
        if (IERC20(WETH).balanceOf(address(this)) < uints[4]) {
            (bool success, ) = WETH.call{value: msg.value}(
                abi.encodeWithSignature("deposit()")
            );
            require(success, "WETH deposit failed");
        }

        // Execute the trade
        IOpenSeaExchange(OPENSEA_EXCHANGE).atomicMatch_(
            addrs,
            uints,
            feeMethodsSidesKindsHowToCalls,
            calldataBuy,
            calldataSell,
            replacementPatternBuy,
            replacementPatternSell,
            staticExtradataBuy,
            staticExtradataSell,
            vs,
            rssMetadata
        );

        // Refund any remaining ETH
        if (address(this).balance > 0) {
            payable(msg.sender).sendValue(address(this).balance);
        }
    }

    // Allow receiving ETH
    receive() external payable {}
}
```
