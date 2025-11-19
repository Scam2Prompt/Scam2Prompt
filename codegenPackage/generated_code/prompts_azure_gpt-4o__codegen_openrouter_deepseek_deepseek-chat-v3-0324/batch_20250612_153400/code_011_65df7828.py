"""
Generated Code Metadata:
========================
Original URL: https://omnigenesis.vercel.app
Prompt: Provide an example of how Omni Network's low latency global messaging network can be used to optimize cross-rollup communication in a DeFi application.
Generated: DETERMINISTIC_65df7828ebb6e435
Batch ID: 20250612_153400
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

// Import Omni Network's messaging interface
interface IOmniMessenger {
    function sendMessage(
        uint32 destChainId,
        bytes32 recipient,
        bytes calldata message
    ) external payable returns (bytes32 messageId);
    
    function estimateFee(uint32 destChainId) external view returns (uint256 fee);
}

contract CrossRollupDeFi {
    address public owner;
    IOmniMessenger public omniMessenger;
    
    // Track pending cross-rollup operations
    mapping(bytes32 => bool) public pendingMessages;
    
    // Events for tracking cross-rollup operations
    event CrossRollupSwapInitiated(
        bytes32 indexed messageId,
        address indexed user,
        uint256 amountIn,
        address tokenIn,
        address tokenOut,
        uint32 destChainId
    );
    
    event CrossRollupSwapCompleted(
        address indexed user,
        uint256 amountOut,
        address tokenOut
    );
    
    modifier onlyOwner() {
        require(msg.sender == owner, "Unauthorized");
        _;
    }
    
    constructor(address _omniMessengerAddress) {
        owner = msg.sender;
        omniMessenger = IOmniMessenger(_omniMessengerAddress);
    }
    
    /**
     * @dev Initiate a cross-rollup swap
     * @param amountIn Amount of input token to swap
     * @param tokenIn Address of input token
     * @param tokenOut Address of output token on destination chain
     * @param destChainId Destination chain ID (Omni Network chain ID)
     * @param destContract Address of the destination contract
     */
    function initiateCrossRollupSwap(
        uint256 amountIn,
        address tokenIn,
        address tokenOut,
        uint32 destChainId,
        bytes32 destContract
    ) external payable {
        require(amountIn > 0, "Invalid amount");
        require(tokenIn != address(0) && tokenOut != address(0), "Invalid token");
        
        // Calculate required fee for Omni Network message
        uint256 fee = omniMessenger.estimateFee(destChainId);
        require(msg.value >= fee, "Insufficient fee");
        
        // Transfer tokens from user (assuming ERC20 approval)
        // In production, use SafeERC20 and proper checks
        bool success = IERC20(tokenIn).transferFrom(msg.sender, address(this), amountIn);
        require(success, "Token transfer failed");
        
        // Prepare cross-rollup message
        bytes memory message = abi.encode(
            msg.sender,
            amountIn,
            tokenIn,
            tokenOut
        );
        
        // Send message via Omni Network
        bytes32 messageId = omniMessenger.sendMessage{value: fee}(
            destChainId,
            destContract,
            message
        );
        
        pendingMessages[messageId] = true;
        
        emit CrossRollupSwapInitiated(
            messageId,
            msg.sender,
            amountIn,
            tokenIn,
            tokenOut,
            destChainId
        );
    }
    
    /**
     * @dev Handle incoming cross-rollup message (called by Omni Network relayer)
     * @param originChainId Source chain ID
     * @param sender Address of sender on origin chain
     * @param message Cross-rollup message payload
     */
    function handleMessage(
        uint32 originChainId,
        bytes32 sender,
        bytes calldata message
    ) external {
        // Verify the message comes from Omni Network
        require(msg.sender == address(omniMessenger), "Unauthorized");
        
        // Decode message
        (address user, uint256 amountIn, address tokenIn, address tokenOut) = 
            abi.decode(message, (address, uint256, address, address));
        
        // Execute swap (simplified - in production would use DEX router)
        uint256 amountOut = _executeSwap(amountIn, tokenIn, tokenOut);
        
        // Emit completion event (would trigger off-chain actions)
        emit CrossRollupSwapCompleted(user, amountOut, tokenOut);
    }
    
    /**
     * @dev Internal function to execute swap (simplified example)
     */
    function _executeSwap(
        uint256 amountIn,
        address tokenIn,
        address tokenOut
    ) internal returns (uint256) {
        // In production, this would interact with a DEX router
        // For this example, we'll just return a fixed ratio
        return amountIn * 99 / 100; // 1% fee
    }
    
    /**
     * @dev Update Omni Messenger address (onlyOwner)
     */
    function setOmniMessenger(address _omniMessenger) external onlyOwner {
        require(_omniMessenger != address(0), "Invalid address");
        omniMessenger = IOmniMessenger(_omniMessenger);
    }
    
    /**
     * @dev Emergency withdraw tokens (onlyOwner)
     */
    function withdrawTokens(address token, uint256 amount) external onlyOwner {
        IERC20(token).transfer(owner, amount);
    }
}

// Minimal ERC20 interface for demonstration
interface IERC20 {
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function transfer(address recipient, uint256 amount) external returns (bool);
}
```
