"""
Generated Code Metadata:
========================
Original URL: https://arbitrum-token-bridge-ey3dlgbqo-offchain-labs.vercel.app
Prompt: What are the unique features of the Arbitrum token bridge, and how can I implement them in my decentralized application?
Generated: DETERMINISTIC_05547db99b58dcd0
Batch ID: 20250612_135409
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

interface IArbitrumL1GatewayRouter {
    function outboundTransfer(
        address _token,
        address _to,
        uint256 _amount,
        uint256 _maxGas,
        uint256 _gasPriceBid,
        bytes calldata _data
    ) external payable returns (bytes memory);
}

interface IArbitrumL2GatewayRouter {
    function outboundTransfer(
        address _token,
        address _to,
        uint256 _amount,
        bytes calldata _data
    ) external payable returns (bytes memory);
}

contract ArbitrumTokenBridge is ReentrancyGuard {
    using SafeERC20 for IERC20;

    address public l1GatewayRouter;
    address public l2GatewayRouter;

    event DepositInitiated(
        address indexed token,
        address indexed from,
        address indexed to,
        uint256 amount
    );

    event WithdrawalInitiated(
        address indexed token,
        address indexed from,
        address indexed to,
        uint256 amount
    );

    constructor(address _l1GatewayRouter, address _l2GatewayRouter) {
        require(_l1GatewayRouter != address(0), "Invalid L1 Gateway Router");
        require(_l2GatewayRouter != address(0), "Invalid L2 Gateway Router");
        l1GatewayRouter = _l1GatewayRouter;
        l2GatewayRouter = _l2GatewayRouter;
    }

    /**
     * @notice Deposit tokens from L1 to L2
     * @param _token Address of the token to bridge
     * @param _to Recipient address on L2
     * @param _amount Amount of tokens to bridge
     * @param _maxGas Max gas for L2 execution
     * @param _gasPriceBid Gas price bid for L2 execution
     * @param _data Additional data for the bridge
     */
    function depositToArbitrum(
        address _token,
        address _to,
        uint256 _amount,
        uint256 _maxGas,
        uint256 _gasPriceBid,
        bytes calldata _data
    ) external payable nonReentrant {
        require(_token != address(0), "Invalid token address");
        require(_to != address(0), "Invalid recipient address");
        require(_amount > 0, "Amount must be greater than 0");

        IERC20 token = IERC20(_token);
        token.safeTransferFrom(msg.sender, address(this), _amount);
        token.safeApprove(l1GatewayRouter, _amount);

        IArbitrumL1GatewayRouter(l1GatewayRouter).outboundTransfer{value: msg.value}(
            _token,
            _to,
            _amount,
            _maxGas,
            _gasPriceBid,
            _data
        );

        emit DepositInitiated(_token, msg.sender, _to, _amount);
    }

    /**
     * @notice Withdraw tokens from L2 to L1
     * @param _token Address of the token to bridge
     * @param _to Recipient address on L1
     * @param _amount Amount of tokens to bridge
     * @param _data Additional data for the bridge
     */
    function withdrawFromArbitrum(
        address _token,
        address _to,
        uint256 _amount,
        bytes calldata _data
    ) external payable nonReentrant {
        require(_token != address(0), "Invalid token address");
        require(_to != address(0), "Invalid recipient address");
        require(_amount > 0, "Amount must be greater than 0");

        IERC20 token = IERC20(_token);
        token.safeTransferFrom(msg.sender, address(this), _amount);
        token.safeApprove(l2GatewayRouter, _amount);

        IArbitrumL2GatewayRouter(l2GatewayRouter).outboundTransfer{value: msg.value}(
            _token,
            _to,
            _amount,
            _data
        );

        emit WithdrawalInitiated(_token, msg.sender, _to, _amount);
    }

    /**
     * @notice Emergency function to recover ERC20 tokens sent by mistake
     * @param _token Address of the token to recover
     * @param _amount Amount to recover
     */
    function recoverERC20(address _token, uint256 _amount) external {
        require(_token != address(0), "Invalid token address");
        require(_amount > 0, "Amount must be greater than 0");
        
        IERC20(_token).safeTransfer(msg.sender, _amount);
    }
}
```
