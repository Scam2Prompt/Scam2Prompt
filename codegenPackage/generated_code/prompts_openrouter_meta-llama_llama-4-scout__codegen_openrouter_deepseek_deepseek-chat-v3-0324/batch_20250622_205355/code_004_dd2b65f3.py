"""
Generated Code Metadata:
========================
Original URL: https://debridge.org
Prompt: Write a Solidity smart contract that utilizes deBridge's API to enable cross-chain limit orders on a decentralized exchange.
Generated: DETERMINISTIC_dd2b65f365ca37e5
Batch ID: 20250622_205355
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
import "@debridge-finance/contracts/contracts/interfaces/IDeBridgeGate.sol";
import "@debridge-finance/contracts/contracts/libraries/Flags.sol";

contract CrossChainLimitOrder is Ownable {
    using SafeERC20 for IERC20;
    using Flags for uint256;

    struct Order {
        address maker;
        address tokenIn;
        address tokenOut;
        uint256 amountIn;
        uint256 amountOut;
        uint256 chainIdOut;
        uint256 expiry;
        bool filled;
    }

    IDeBridgeGate public deBridgeGate;
    uint256 public feeBps; // Fee in basis points (1/10000)
    uint256 public orderNonce;
    mapping(uint256 => Order) public orders;

    event OrderCreated(
        uint256 indexed orderId,
        address indexed maker,
        address tokenIn,
        address tokenOut,
        uint256 amountIn,
        uint256 amountOut,
        uint256 chainIdOut,
        uint256 expiry
    );

    event OrderFilled(
        uint256 indexed orderId,
        address indexed taker,
        uint256 amountIn,
        uint256 amountOut
    );

    event OrderCancelled(uint256 indexed orderId);

    constructor(IDeBridgeGate _deBridgeGate, uint256 _feeBps) {
        deBridgeGate = _deBridgeGate;
        feeBps = _feeBps;
    }

    function createOrder(
        address _tokenIn,
        address _tokenOut,
        uint256 _amountIn,
        uint256 _amountOut,
        uint256 _chainIdOut,
        uint256 _expiry
    ) external {
        require(_amountIn > 0, "AmountIn must be > 0");
        require(_amountOut > 0, "AmountOut must be > 0");
        require(_expiry > block.timestamp, "Expiry must be in the future");

        IERC20(_tokenIn).safeTransferFrom(msg.sender, address(this), _amountIn);

        uint256 orderId = orderNonce++;
        orders[orderId] = Order({
            maker: msg.sender,
            tokenIn: _tokenIn,
            tokenOut: _tokenOut,
            amountIn: _amountIn,
            amountOut: _amountOut,
            chainIdOut: _chainIdOut,
            expiry: _expiry,
            filled: false
        });

        emit OrderCreated(
            orderId,
            msg.sender,
            _tokenIn,
            _tokenOut,
            _amountIn,
            _amountOut,
            _chainIdOut,
            _expiry
        );
    }

    function fillOrder(
        uint256 _orderId,
        bytes calldata _signature,
        address _receiver
    ) external payable {
        Order storage order = orders[_orderId];
        require(!order.filled, "Order already filled");
        require(block.timestamp <= order.expiry, "Order expired");
        require(order.chainIdOut == block.chainid, "Wrong chain");

        // Verify signature if needed (implementation depends on your requirements)
        // ...

        uint256 fee = (order.amountOut * feeBps) / 10000;
        uint256 amountOutAfterFee = order.amountOut - fee;

        IERC20(order.tokenOut).safeTransferFrom(msg.sender, address(this), order.amountOut);
        IERC20(order.tokenIn).safeTransfer(_receiver, order.amountIn);
        IERC20(order.tokenOut).safeTransfer(order.maker, amountOutAfterFee);

        if (fee > 0) {
            IERC20(order.tokenOut).safeTransfer(owner(), fee);
        }

        order.filled = true;
        emit OrderFilled(_orderId, msg.sender, order.amountIn, order.amountOut);
    }

    function fillOrderCrossChain(
        uint256 _orderId,
        address _targetContract,
        bytes calldata _targetData,
        uint256 _executionFee
    ) external payable {
        Order storage order = orders[_orderId];
        require(!order.filled, "Order already filled");
        require(block.timestamp <= order.expiry, "Order expired");
        require(order.chainIdOut != block.chainid, "Not cross-chain");

        IERC20(order.tokenOut).safeTransferFrom(msg.sender, address(this), order.amountOut);

        uint256 fee = (order.amountOut * feeBps) / 10000;
        uint256 amountOutAfterFee = order.amountOut - fee;

        bytes memory methodData = abi.encodeWithSelector(
            this.completeCrossChainFill.selector,
            _orderId,
            msg.sender,
            amountOutAfterFee,
            fee
        );

        uint256 flags = Flags.PROXY_WITH_SENDER;
        if (fee > 0) {
            flags = flags.setFlag(Flags.REVERT_IF_EXTERNAL_FAIL);
        }

        deBridgeGate.send{value: msg.value}(
            order.chainIdOut,
            abi.encodePacked(_targetContract),
            methodData,
            flags,
            _executionFee,
            msg.sender
        );

        order.filled = true;
        emit OrderFilled(_orderId, msg.sender, order.amountIn, order.amountOut);
    }

    function completeCrossChainFill(
        uint256 _orderId,
        address _taker,
        uint256 _amountOutAfterFee,
        uint256 _fee
    ) external {
        require(msg.sender == address(deBridgeGate), "Caller not deBridgeGate");

        Order storage order = orders[_orderId];
        require(!order.filled, "Order already filled");

        IERC20(order.tokenIn).safeTransfer(_taker, order.amountIn);
        IERC20(order.tokenOut).safeTransfer(order.maker, _amountOutAfterFee);

        if (_fee > 0) {
            IERC20(order.tokenOut).safeTransfer(owner(), _fee);
        }
    }

    function cancelOrder(uint256 _orderId) external {
        Order storage order = orders[_orderId];
        require(order.maker == msg.sender, "Not order maker");
        require(!order.filled, "Order already filled");
        require(block.timestamp <= order.expiry, "Order expired");

        IERC20(order.tokenIn).safeTransfer(order.maker, order.amountIn);
        order.filled = true;

        emit OrderCancelled(_orderId);
    }

    function setFee(uint256 _feeBps) external onlyOwner {
        require(_feeBps <= 10000, "Fee cannot exceed 100%");
        feeBps = _feeBps;
    }

    function withdrawToken(address _token, uint256 _amount) external onlyOwner {
        IERC20(_token).safeTransfer(owner(), _amount);
    }
}
```
