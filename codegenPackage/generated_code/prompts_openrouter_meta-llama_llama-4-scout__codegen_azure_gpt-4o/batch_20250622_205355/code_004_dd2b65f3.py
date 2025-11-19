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

/**
 * @title CrossChainLimitOrder
 * @dev A smart contract to enable cross-chain limit orders using deBridge's API.
 *      This contract interacts with deBridge to facilitate cross-chain communication.
 */
interface IDeBridgeGate {
    function send(
        address _tokenAddress,
        uint256 _amount,
        uint256 _chainIdTo,
        bytes memory _receiverAddress,
        bytes memory _data,
        bool _useAssetFee,
        uint256 _referralCode
    ) external payable;
}

contract CrossChainLimitOrder {
    // Address of the deBridgeGate contract
    address public deBridgeGateAddress;

    // Struct to store limit order details
    struct LimitOrder {
        address user;
        address tokenAddress;
        uint256 amount;
        uint256 targetChainId;
        bytes targetAddress;
        uint256 price; // Price at which the order should execute
        bool fulfilled;
    }

    // Mapping to store limit orders
    mapping(uint256 => LimitOrder) public limitOrders;
    uint256 public orderCount;

    // Events
    event LimitOrderCreated(
        uint256 indexed orderId,
        address indexed user,
        address tokenAddress,
        uint256 amount,
        uint256 targetChainId,
        bytes targetAddress,
        uint256 price
    );
    event LimitOrderFulfilled(uint256 indexed orderId);

    /**
     * @dev Constructor to initialize the deBridgeGate address.
     * @param _deBridgeGateAddress Address of the deBridgeGate contract.
     */
    constructor(address _deBridgeGateAddress) {
        require(_deBridgeGateAddress != address(0), "Invalid deBridgeGate address");
        deBridgeGateAddress = _deBridgeGateAddress;
    }

    /**
     * @dev Create a new limit order.
     * @param _tokenAddress Address of the token to be sent.
     * @param _amount Amount of tokens to be sent.
     * @param _targetChainId ID of the target chain.
     * @param _targetAddress Address of the receiver on the target chain.
     * @param _price Price at which the order should execute.
     */
    function createLimitOrder(
        address _tokenAddress,
        uint256 _amount,
        uint256 _targetChainId,
        bytes memory _targetAddress,
        uint256 _price
    ) external payable {
        require(_tokenAddress != address(0), "Invalid token address");
        require(_amount > 0, "Amount must be greater than zero");
        require(_targetChainId > 0, "Invalid target chain ID");
        require(_targetAddress.length > 0, "Invalid target address");
        require(_price > 0, "Price must be greater than zero");

        // Increment order count
        orderCount++;

        // Create a new limit order
        limitOrders[orderCount] = LimitOrder({
            user: msg.sender,
            tokenAddress: _tokenAddress,
            amount: _amount,
            targetChainId: _targetChainId,
            targetAddress: _targetAddress,
            price: _price,
            fulfilled: false
        });

        emit LimitOrderCreated(orderCount, msg.sender, _tokenAddress, _amount, _targetChainId, _targetAddress, _price);
    }

    /**
     * @dev Fulfill a limit order by sending tokens cross-chain using deBridge.
     * @param _orderId ID of the limit order to fulfill.
     */
    function fulfillLimitOrder(uint256 _orderId) external payable {
        LimitOrder storage order = limitOrders[_orderId];
        require(order.user != address(0), "Order does not exist");
        require(!order.fulfilled, "Order already fulfilled");

        // Interact with deBridgeGate to send tokens cross-chain
        IDeBridgeGate(deBridgeGateAddress).send{value: msg.value}(
            order.tokenAddress,
            order.amount,
            order.targetChainId,
            order.targetAddress,
            "",
            false,
            0
        );

        // Mark the order as fulfilled
        order.fulfilled = true;

        emit LimitOrderFulfilled(_orderId);
    }

    /**
     * @dev Fallback function to receive Ether.
     */
    receive() external payable {}

    /**
     * @dev Withdraw Ether from the contract.
     * @param _to Address to send the Ether to.
     * @param _amount Amount of Ether to withdraw.
     */
    function withdrawEther(address payable _to, uint256 _amount) external {
        require(_to != address(0), "Invalid address");
        require(_amount <= address(this).balance, "Insufficient balance");

        _to.transfer(_amount);
    }
}
```
