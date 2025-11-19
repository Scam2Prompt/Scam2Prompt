"""
Generated Code Metadata:
========================
Original URL: https://bafybeibasskry2ovpgydqzwiw46ea2lmyxe4fqb6jekaixqidxb6cvjn3m.ipfs.dweb.link
Prompt: Provide an example of how to integrate EigenLayer for achieving interoperability with Ethereum Layer 2 chains using Polymer.
Generated: DETERMINISTIC_50d6c4005ba88423
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
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

interface IEigenLayer {
    function depositIntoStrategy(address strategy, IERC20 token, uint256 amount) external;
    function withdrawFromStrategy(address strategy, IERC20 token, uint256 amount) external;
    function getStrategyShares(address user, address strategy) external view returns (uint256);
}

interface IPolymer {
    function bridgeToL2(
        address token,
        uint256 amount,
        uint256 chainId,
        address recipient
    ) external payable;
}

contract EigenLayerPolymerBridge is Ownable, ReentrancyGuard {
    IEigenLayer public immutable eigenLayer;
    IPolymer public immutable polymer;
    address public strategy;
    
    mapping(address => bool) public supportedTokens;
    mapping(uint256 => bool) public supportedChainIds;

    event TokenDeposited(address indexed user, address indexed token, uint256 amount);
    event TokenBridged(address indexed user, address indexed token, uint256 amount, uint256 chainId);
    event TokenWithdrawn(address indexed user, address indexed token, uint256 amount);
    event StrategyUpdated(address newStrategy);
    event TokenSupportUpdated(address token, bool isSupported);
    event ChainSupportUpdated(uint256 chainId, bool isSupported);

    constructor(
        address _eigenLayer,
        address _polymer,
        address _initialStrategy
    ) {
        require(_eigenLayer != address(0), "Invalid EigenLayer address");
        require(_polymer != address(0), "Invalid Polymer address");
        require(_initialStrategy != address(0), "Invalid strategy address");
        
        eigenLayer = IEigenLayer(_eigenLayer);
        polymer = IPolymer(_polymer);
        strategy = _initialStrategy;
    }

    function depositToEigenLayer(
        IERC20 token,
        uint256 amount
    ) external nonReentrant {
        require(supportedTokens[address(token)], "Token not supported");
        require(amount > 0, "Amount must be greater than 0");
        
        token.transferFrom(msg.sender, address(this), amount);
        token.approve(address(eigenLayer), amount);
        eigenLayer.depositIntoStrategy(strategy, token, amount);
        
        emit TokenDeposited(msg.sender, address(token), amount);
    }

    function bridgeToL2(
        IERC20 token,
        uint256 amount,
        uint256 chainId,
        address recipient
    ) external payable nonReentrant {
        require(supportedTokens[address(token)], "Token not supported");
        require(supportedChainIds[chainId], "Chain ID not supported");
        require(amount > 0, "Amount must be greater than 0");
        
        uint256 shares = eigenLayer.getStrategyShares(address(this), strategy);
        require(shares >= amount, "Insufficient shares");
        
        eigenLayer.withdrawFromStrategy(strategy, token, amount);
        token.approve(address(polymer), amount);
        polymer.bridgeToL2{value: msg.value}(address(token), amount, chainId, recipient);
        
        emit TokenBridged(msg.sender, address(token), amount, chainId);
    }

    function withdrawFromEigenLayer(
        IERC20 token,
        uint256 amount
    ) external nonReentrant onlyOwner {
        require(amount > 0, "Amount must be greater than 0");
        
        eigenLayer.withdrawFromStrategy(strategy, token, amount);
        token.transfer(owner(), amount);
        
        emit TokenWithdrawn(owner(), address(token), amount);
    }

    function updateStrategy(address newStrategy) external onlyOwner {
        require(newStrategy != address(0), "Invalid strategy address");
        strategy = newStrategy;
        emit StrategyUpdated(newStrategy);
    }

    function setTokenSupport(address token, bool isSupported) external onlyOwner {
        supportedTokens[token] = isSupported;
        emit TokenSupportUpdated(token, isSupported);
    }

    function setChainSupport(uint256 chainId, bool isSupported) external onlyOwner {
        supportedChainIds[chainId] = isSupported;
        emit ChainSupportUpdated(chainId, isSupported);
    }

    function emergencyWithdraw(
        IERC20 token,
        uint256 amount
    ) external nonReentrant onlyOwner {
        token.transfer(owner(), amount);
    }
}
```
