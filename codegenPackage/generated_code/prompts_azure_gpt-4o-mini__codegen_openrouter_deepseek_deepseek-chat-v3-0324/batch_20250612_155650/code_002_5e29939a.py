"""
Generated Code Metadata:
========================
Original URL: https://gifts-usualdao.com
Prompt: What are the best practices for integrating multichain functionality in a DeFi protocol like Usual, which aims to enhance user growth and TVL?
Generated: DETERMINISTIC_5e29939a94084c9d
Batch ID: 20250612_155650
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
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

interface ICrossChainRouter {
    function swap(
        uint256 amount,
        address token,
        uint256 targetChainId,
        address recipient
    ) external payable returns (bool);
}

contract UsualMultiChainDeFi is Ownable, ReentrancyGuard {
    using SafeMath for uint256;

    // Chain IDs for supported networks
    uint256 public constant ETHEREUM_MAINNET = 1;
    uint256 public constant BSC_MAINNET = 56;
    uint256 public constant POLYGON_MAINNET = 137;
    uint256 public constant ARBITRUM_MAINNET = 42161;

    // Supported tokens
    mapping(address => bool) public supportedTokens;
    
    // Cross-chain router contract
    ICrossChainRouter public crossChainRouter;
    
    // TVL tracking
    mapping(uint256 => uint256) public chainTVL;
    mapping(address => mapping(uint256 => uint256)) public userDeposits;

    // Events
    event TokenSupported(address indexed token, bool isSupported);
    event CrossChainDeposit(
        address indexed user,
        uint256 sourceChainId,
        uint256 targetChainId,
        address token,
        uint256 amount,
        uint256 timestamp
    );
    event CrossChainWithdrawal(
        address indexed user,
        uint256 sourceChainId,
        uint256 targetChainId,
        address token,
        uint256 amount,
        uint256 timestamp
    );

    constructor(address _crossChainRouter) {
        require(_crossChainRouter != address(0), "Invalid router address");
        crossChainRouter = ICrossChainRouter(_crossChainRouter);
    }

    /**
     * @dev Add or remove supported tokens
     * @param token Address of the token
     * @param isSupported Whether to support or not
     */
    function setSupportedToken(address token, bool isSupported) external onlyOwner {
        supportedTokens[token] = isSupported;
        emit TokenSupported(token, isSupported);
    }

    /**
     * @dev Deposit tokens from one chain to another
     * @param amount Amount to deposit
     * @param token Token address
     * @param targetChainId Destination chain ID
     */
    function depositToChain(
        uint256 amount,
        address token,
        uint256 targetChainId
    ) external payable nonReentrant {
        require(supportedTokens[token], "Token not supported");
        require(amount > 0, "Amount must be greater than 0");
        require(
            targetChainId == BSC_MAINNET ||
            targetChainId == POLYGON_MAINNET ||
            targetChainId == ARBITRUM_MAINNET,
            "Unsupported target chain"
        );

        IERC20(token).transferFrom(msg.sender, address(this), amount);
        
        // Update TVL and user deposits
        chainTVL[block.chainid] = chainTVL[block.chainid].add(amount);
        userDeposits[msg.sender][block.chainid] = userDeposits[msg.sender][block.chainid].add(amount);

        // Approve cross-chain router to spend tokens
        IERC20(token).approve(address(crossChainRouter), amount);
        
        // Execute cross-chain swap
        bool success = crossChainRouter.swap{value: msg.value}(
            amount,
            token,
            targetChainId,
            msg.sender
        );
        require(success, "Cross-chain transfer failed");

        emit CrossChainDeposit(
            msg.sender,
            block.chainid,
            targetChainId,
            token,
            amount,
            block.timestamp
        );
    }

    /**
     * @dev Withdraw tokens from another chain
     * @param amount Amount to withdraw
     * @param token Token address
     * @param sourceChainId Source chain ID
     */
    function withdrawFromChain(
        uint256 amount,
        address token,
        uint256 sourceChainId
    ) external payable nonReentrant {
        require(supportedTokens[token], "Token not supported");
        require(amount > 0, "Amount must be greater than 0");
        require(
            userDeposits[msg.sender][sourceChainId] >= amount,
            "Insufficient balance"
        );

        // Execute cross-chain swap back to original chain
        bool success = crossChainRouter.swap{value: msg.value}(
            amount,
            token,
            block.chainid,
            msg.sender
        );
        require(success, "Cross-chain transfer failed");

        // Update TVL and user deposits
        chainTVL[sourceChainId] = chainTVL[sourceChainId].sub(amount);
        userDeposits[msg.sender][sourceChainId] = userDeposits[msg.sender][sourceChainId].sub(amount);

        emit CrossChainWithdrawal(
            msg.sender,
            sourceChainId,
            block.chainid,
            token,
            amount,
            block.timestamp
        );
    }

    /**
     * @dev Update cross-chain router address
     * @param newRouter Address of the new router
     */
    function updateCrossChainRouter(address newRouter) external onlyOwner {
        require(newRouter != address(0), "Invalid router address");
        crossChainRouter = ICrossChainRouter(newRouter);
    }

    /**
     * @dev Emergency withdraw tokens (owner only)
     * @param token Address of the token to withdraw
     */
    function emergencyWithdraw(address token) external onlyOwner {
        uint256 balance = IERC20(token).balanceOf(address(this));
        IERC20(token).transfer(owner(), balance);
    }
}
```
