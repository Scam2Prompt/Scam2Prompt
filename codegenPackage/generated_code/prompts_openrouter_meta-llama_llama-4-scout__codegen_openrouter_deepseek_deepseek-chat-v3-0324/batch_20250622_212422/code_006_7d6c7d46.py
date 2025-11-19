"""
Generated Code Metadata:
========================
Original URL: https://portalbridge.dev
Prompt: Generate a code example for a smart contract that utilizes the Portal Token Bridge to transfer tokens between two chains, ensuring maximum security and minimal transaction costs.
Generated: DETERMINISTIC_7d6c7d4624086da6
Batch ID: 20250622_212422
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

interface IPortalBridge {
    function transferTokens(
        address token,
        uint256 amount,
        uint16 recipientChain,
        bytes32 recipient,
        uint256 arbiterFee,
        uint32 nonce
    ) external returns (uint64 sequence);
}

contract CrossChainTokenBridge is Ownable, ReentrancyGuard {
    using SafeERC20 for IERC20;

    IPortalBridge public portalBridge;
    uint16 public immutable targetChainId;
    address public immutable targetContract;

    event TokensDeposited(
        address indexed sender,
        address indexed token,
        uint256 amount,
        uint64 sequence
    );
    event TokensWithdrawn(
        address indexed recipient,
        address indexed token,
        uint256 amount
    );

    constructor(
        address _portalBridge,
        uint16 _targetChainId,
        address _targetContract
    ) {
        require(_portalBridge != address(0), "Invalid portal bridge address");
        require(_targetContract != address(0), "Invalid target contract address");
        
        portalBridge = IPortalBridge(_portalBridge);
        targetChainId = _targetChainId;
        targetContract = _targetContract;
    }

    function depositTokens(
        address token,
        uint256 amount,
        uint256 arbiterFee,
        uint32 nonce
    ) external nonReentrant returns (uint64 sequence) {
        require(token != address(0), "Invalid token address");
        require(amount > 0, "Amount must be greater than 0");

        IERC20(token).safeTransferFrom(msg.sender, address(this), amount);
        IERC20(token).safeApprove(address(portalBridge), amount);

        bytes32 recipient = addressToBytes32(targetContract);
        sequence = portalBridge.transferTokens(
            token,
            amount,
            targetChainId,
            recipient,
            arbiterFee,
            nonce
        );

        emit TokensDeposited(msg.sender, token, amount, sequence);
        return sequence;
    }

    function withdrawTokens(
        address token,
        address recipient,
        uint256 amount
    ) external onlyOwner nonReentrant {
        require(token != address(0), "Invalid token address");
        require(recipient != address(0), "Invalid recipient address");
        require(amount > 0, "Amount must be greater than 0");

        IERC20(token).safeTransfer(recipient, amount);
        emit TokensWithdrawn(recipient, token, amount);
    }

    function updatePortalBridge(address _portalBridge) external onlyOwner {
        require(_portalBridge != address(0), "Invalid portal bridge address");
        portalBridge = IPortalBridge(_portalBridge);
    }

    function addressToBytes32(address addr) internal pure returns (bytes32) {
        return bytes32(uint256(uint160(addr)));
    }

    function recoverERC20(address token, uint256 amount) external onlyOwner {
        require(token != address(0), "Invalid token address");
        IERC20(token).safeTransfer(owner(), amount);
    }
}
```
