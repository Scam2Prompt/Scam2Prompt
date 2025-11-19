"""
Generated Code Metadata:
========================
Original URL: https://bafybeifn4q7vghs7f3xwilosxa4dyllaadejgevezprlqf5cgs5mgpvmr4.ipfs.dweb.link
Prompt: "Create a simple smart contract on Arbitrum that utilizes Vertex's API for perpetuals trading."
Generated: DETERMINISTIC_a9b5a7e09d08cc9e
Batch ID: 20250622_205111
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

// Interface for Vertex's Perpetuals API
interface IVertexPerpetuals {
    function submitOrder(
        address sender,
        address baseToken,
        address quoteToken,
        uint256 amount,
        uint256 price,
        bool isBuy
    ) external returns (bytes32 orderId);
    
    function cancelOrder(bytes32 orderId) external returns (bool);
    
    function getOrderStatus(bytes32 orderId) external view returns (
        address baseToken,
        address quoteToken,
        uint256 amount,
        uint256 price,
        bool isBuy,
        bool isFilled,
        bool isCancelled
    );
}

contract VertexPerpetualTrader {
    address public owner;
    IVertexPerpetuals public vertexPerpetuals;
    
    // Events
    event OrderSubmitted(bytes32 indexed orderId, address indexed trader);
    event OrderCancelled(bytes32 indexed orderId);
    event OwnershipTransferred(address indexed previousOwner, address indexed newOwner);
    
    // Modifiers
    modifier onlyOwner() {
        require(msg.sender == owner, "VertexPerpetualTrader: caller is not the owner");
        _;
    }
    
    constructor(address _vertexPerpetualsAddress) {
        require(_vertexPerpetualsAddress != address(0), "VertexPerpetualTrader: invalid address");
        owner = msg.sender;
        vertexPerpetuals = IVertexPerpetuals(_vertexPerpetualsAddress);
    }
    
    /**
     * @dev Submit an order to Vertex Perpetuals
     * @param baseToken Address of the base token
     * @param quoteToken Address of the quote token
     * @param amount Amount of the order
     * @param price Price of the order
     * @param isBuy Whether the order is a buy order
     */
    function submitOrder(
        address baseToken,
        address quoteToken,
        uint256 amount,
        uint256 price,
        bool isBuy
    ) external onlyOwner returns (bytes32 orderId) {
        require(baseToken != address(0), "VertexPerpetualTrader: invalid base token");
        require(quoteToken != address(0), "VertexPerpetualTrader: invalid quote token");
        require(amount > 0, "VertexPerpetualTrader: amount must be > 0");
        require(price > 0, "VertexPerpetualTrader: price must be > 0");
        
        orderId = vertexPerpetuals.submitOrder(
            address(this),
            baseToken,
            quoteToken,
            amount,
            price,
            isBuy
        );
        
        emit OrderSubmitted(orderId, msg.sender);
        return orderId;
    }
    
    /**
     * @dev Cancel an existing order
     * @param orderId ID of the order to cancel
     */
    function cancelOrder(bytes32 orderId) external onlyOwner returns (bool) {
        bool success = vertexPerpetuals.cancelOrder(orderId);
        require(success, "VertexPerpetualTrader: order cancellation failed");
        
        emit OrderCancelled(orderId);
        return success;
    }
    
    /**
     * @dev Get order status
     * @param orderId ID of the order to check
     */
    function getOrderStatus(bytes32 orderId) external view returns (
        address baseToken,
        address quoteToken,
        uint256 amount,
        uint256 price,
        bool isBuy,
        bool isFilled,
        bool isCancelled
    ) {
        return vertexPerpetuals.getOrderStatus(orderId);
    }
    
    /**
     * @dev Transfer ownership of the contract
     * @param newOwner Address of the new owner
     */
    function transferOwnership(address newOwner) external onlyOwner {
        require(newOwner != address(0), "VertexPerpetualTrader: new owner is the zero address");
        emit OwnershipTransferred(owner, newOwner);
        owner = newOwner;
    }
}
```
