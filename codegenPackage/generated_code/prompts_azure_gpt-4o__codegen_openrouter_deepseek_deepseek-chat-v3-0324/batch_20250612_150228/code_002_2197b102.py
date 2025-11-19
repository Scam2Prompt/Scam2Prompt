"""
Generated Code Metadata:
========================
Original URL: https://bafybeifck3tvl2afu34735yd3ul2g5ifecjinp2c7na6kdjx3q2no76q5i.ipfs.dweb.link
Prompt: Provide a step-by-step guide in Solidity to create a smart contract that bridges tokens between Avalanche and Arbitrum networks, referencing the "How to Bridge?" section of the Joe exchange.
Generated: DETERMINISTIC_2197b102522bb92e
Batch ID: 20250612_150228
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
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title CrossChainTokenBridge
 * @dev A smart contract for bridging ERC20 tokens between Avalanche and Arbitrum networks
 * @notice This contract implements the bridging functionality similar to Joe Exchange's "How to Bridge?" section
 */
contract CrossChainTokenBridge is ReentrancyGuard, Ownable {
    using SafeERC20 for IERC20;

    // Struct to store bridge request details
    struct BridgeRequest {
        address requester;
        address token;
        uint256 amount;
        uint256 targetChainId;
        uint256 nonce;
        bool isProcessed;
    }

    // Mapping to store bridge requests
    mapping(bytes32 => BridgeRequest) public bridgeRequests;

    // Mapping to store supported tokens and their bridge fees
    mapping(address => uint256) public bridgeFees;

    // Mapping to store supported chain IDs
    mapping(uint256 => bool) public supportedChains;

    // Event emitted when a new bridge request is created
    event BridgeRequestCreated(
        bytes32 requestId,
        address indexed requester,
        address indexed token,
        uint256 amount,
        uint256 targetChainId,
        uint256 nonce
    );

    // Event emitted when a bridge request is processed
    event BridgeRequestProcessed(
        bytes32 requestId,
        address indexed requester,
        address indexed token,
        uint256 amount,
        uint256 targetChainId
    );

    // Event emitted when bridge fees are updated
    event BridgeFeeUpdated(address indexed token, uint256 newFee);

    // Event emitted when a new chain is supported
    event ChainSupportUpdated(uint256 chainId, bool isSupported);

    /**
     * @dev Constructor to initialize the contract
     * @param _initialOwner The initial owner of the contract
     */
    constructor(address _initialOwner) Ownable(_initialOwner) {
        // Initialize with default supported chains (Avalanche and Arbitrum)
        supportedChains[43114] = true; // Avalanche Mainnet C-Chain
        supportedChains[42161] = true; // Arbitrum One
    }

    /**
     * @dev Function to create a bridge request
     * @param _token The address of the token to bridge
     * @param _amount The amount of tokens to bridge
     * @param _targetChainId The chain ID of the target network
     */
    function createBridgeRequest(
        address _token,
        uint256 _amount,
        uint256 _targetChainId
    ) external payable nonReentrant {
        require(_amount > 0, "Amount must be greater than zero");
        require(supportedChains[_targetChainId], "Target chain not supported");
        require(bridgeFees[_token] <= msg.value, "Insufficient bridge fee");

        IERC20 token = IERC20(_token);
        uint256 balanceBefore = token.balanceOf(address(this));
        token.safeTransferFrom(msg.sender, address(this), _amount);
        uint256 balanceAfter = token.balanceOf(address(this));
        require(balanceAfter - balanceBefore == _amount, "Token transfer failed");

        uint256 nonce = uint256(keccak256(abi.encodePacked(block.timestamp, msg.sender, _amount)));
        bytes32 requestId = keccak256(abi.encodePacked(msg.sender, _token, _amount, _targetChainId, nonce));

        bridgeRequests[requestId] = BridgeRequest({
            requester: msg.sender,
            token: _token,
            amount: _amount,
            targetChainId: _targetChainId,
            nonce: nonce,
            isProcessed: false
        });

        emit BridgeRequestCreated(requestId, msg.sender, _token, _amount, _targetChainId, nonce);
    }

    /**
     * @dev Function to process a bridge request (only callable by owner)
     * @param _requestId The ID of the bridge request to process
     */
    function processBridgeRequest(bytes32 _requestId) external onlyOwner {
        BridgeRequest storage request = bridgeRequests[_requestId];
        require(!request.isProcessed, "Request already processed");
        require(request.requester != address(0), "Invalid request ID");

        request.isProcessed = true;
        IERC20(request.token).safeTransfer(request.requester, request.amount);

        emit BridgeRequestProcessed(
            _requestId,
            request.requester,
            request.token,
            request.amount,
            request.targetChainId
        );
    }

    /**
     * @dev Function to update bridge fee for a token (only callable by owner)
     * @param _token The address of the token
     * @param _fee The new bridge fee
     */
    function updateBridgeFee(address _token, uint256 _fee) external onlyOwner {
        bridgeFees[_token] = _fee;
        emit BridgeFeeUpdated(_token, _fee);
    }

    /**
     * @dev Function to update chain support (only callable by owner)
     * @param _chainId The chain ID to update
     * @param _isSupported Whether the chain is supported or not
     */
    function updateChainSupport(uint256 _chainId, bool _isSupported) external onlyOwner {
        supportedChains[_chainId] = _isSupported;
        emit ChainSupportUpdated(_chainId, _isSupported);
    }

    /**
     * @dev Function to withdraw collected fees (only callable by owner)
     * @param _amount The amount to withdraw
     */
    function withdrawFees(uint256 _amount) external onlyOwner {
        require(_amount <= address(this).balance, "Insufficient balance");
        payable(owner()).transfer(_amount);
    }

    /**
     * @dev Function to withdraw ERC20 tokens (only callable by owner)
     * @param _token The address of the token to withdraw
     * @param _amount The amount to withdraw
     */
    function withdrawERC20(address _token, uint256 _amount) external onlyOwner {
        IERC20(_token).safeTransfer(owner(), _amount);
    }
}
```
