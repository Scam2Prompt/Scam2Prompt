"""
Generated Code Metadata:
========================
Original URL: https://bafybeidbzihyinyo7izo2bw76p5ghzvavjsr3c5oqgowyshfuo5g6gfmti.ipfs.dweb.link
Prompt: How can I implement cross-chain swaps using the XSwap protocol and Chainlink CCIP for secure token transfers?
Generated: DETERMINISTIC_b8fdf65a346a6e45
Batch ID: 20250612_160940
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.19;

import "@chainlink/contracts/src/v0.8/ccip/interfaces/IRouterClient.sol";
import "@chainlink/contracts/src/v0.8/ccip/applications/CCIPReceiver.sol";
import "@chainlink/contracts/src/v0.8/ccip/libraries/Client.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/token/ERC20/utils/SafeERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract XSwap is CCIPReceiver, Ownable {
    using SafeERC20 for IERC20;

    // Chainlink CCIP Router
    IRouterClient public immutable router;

    // Supported chains and their corresponding Chainlink chain selectors
    mapping(uint64 => bool) public supportedChains;
    mapping(bytes32 => bool) public processedMessages;

    // Swap details
    struct SwapRequest {
        address sender;
        address tokenIn;
        address tokenOut;
        uint256 amountIn;
        uint256 minAmountOut;
        uint64 destinationChain;
    }

    event SwapInitiated(
        bytes32 indexed messageId,
        address indexed sender,
        address tokenIn,
        address tokenOut,
        uint256 amountIn,
        uint256 minAmountOut,
        uint64 destinationChain
    );

    event SwapCompleted(
        bytes32 indexed messageId,
        address indexed sender,
        address tokenOut,
        uint256 amountOut
    );

    constructor(address _router) CCIPReceiver(_router) {
        router = IRouterClient(_router);
    }

    // Add supported chain
    function addSupportedChain(uint64 _chainSelector) external onlyOwner {
        supportedChains[_chainSelector] = true;
    }

    // Remove supported chain
    function removeSupportedChain(uint64 _chainSelector) external onlyOwner {
        supportedChains[_chainSelector] = false;
    }

    // Initiate cross-chain swap
    function initiateSwap(
        address _tokenIn,
        address _tokenOut,
        uint256 _amountIn,
        uint256 _minAmountOut,
        uint64 _destinationChain
    ) external payable {
        require(supportedChains[_destinationChain], "Unsupported destination chain");
        require(_amountIn > 0, "Amount must be greater than 0");

        IERC20 tokenIn = IERC20(_tokenIn);
        require(tokenIn.balanceOf(msg.sender) >= _amountIn, "Insufficient balance");

        // Transfer tokens from sender to this contract
        tokenIn.safeTransferFrom(msg.sender, address(this), _amountIn);

        // Build CCIP message
        SwapRequest memory request = SwapRequest({
            sender: msg.sender,
            tokenIn: _tokenIn,
            tokenOut: _tokenOut,
            amountIn: _amountIn,
            minAmountOut: _minAmountOut,
            destinationChain: _destinationChain
        });

        bytes memory data = abi.encode(request);
        Client.EVM2AnyMessage memory message = Client.EVM2AnyMessage({
            receiver: abi.encode(address(this)),
            data: data,
            tokenAmounts: new Client.EVMTokenAmount[](0),
            extraArgs: "",
            feeToken: address(0)
        });

        // Send CCIP message
        uint256 fee = router.getFee(_destinationChain, message);
        require(msg.value >= fee, "Insufficient fee");

        bytes32 messageId = router.ccipSend{value: fee}(_destinationChain, message);
        
        emit SwapInitiated(
            messageId,
            msg.sender,
            _tokenIn,
            _tokenOut,
            _amountIn,
            _minAmountOut,
            _destinationChain
        );
    }

    // Handle incoming CCIP message
    function _ccipReceive(
        Client.Any2EVMMessage memory message
    ) internal override {
        bytes32 messageId = message.messageId;
        require(!processedMessages[messageId], "Message already processed");

        SwapRequest memory request = abi.decode(message.data, (SwapRequest));
        require(supportedChains[message.sourceChainSelector], "Unsupported source chain");

        // Process swap (simplified - in production would use oracle for price feed)
        IERC20 tokenOut = IERC20(request.tokenOut);
        uint256 amountOut = request.amountIn; // Simplified - should use price oracle
        
        require(amountOut >= request.minAmountOut, "Insufficient output amount");
        require(tokenOut.balanceOf(address(this)) >= amountOut, "Insufficient liquidity");

        // Transfer tokens to recipient
        tokenOut.safeTransfer(request.sender, amountOut);

        processedMessages[messageId] = true;
        
        emit SwapCompleted(
            messageId,
            request.sender,
            request.tokenOut,
            amountOut
        );
    }

    // Withdraw tokens (emergency use)
    function withdrawToken(address _token, uint256 _amount) external onlyOwner {
        IERC20(_token).safeTransfer(owner(), _amount);
    }

    // Withdraw native currency (emergency use)
    function withdrawNative(uint256 _amount) external onlyOwner {
        payable(owner()).transfer(_amount);
    }

    // Receive fallback
    receive() external payable {}
}
```
