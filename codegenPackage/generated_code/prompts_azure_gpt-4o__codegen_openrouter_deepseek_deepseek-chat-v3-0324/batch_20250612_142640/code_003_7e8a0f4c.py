"""
Generated Code Metadata:
========================
Original URL: https://para-swap.github.io
Prompt: Create a Solidity contract that uses ParaSwap to modularize core logic for a DeFi application while ensuring safe upgrades via ERC1967 proxy checks.
Generated: DETERMINISTIC_7e8a0f4c566b1718
Batch ID: 20250612_142640
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

import "@openzeppelin/contracts/proxy/ERC1967/ERC1967Proxy.sol";
import "@openzeppelin/contracts/proxy/ERC1967/ERC1967Upgrade.sol";
import "@openzeppelin/contracts/utils/Address.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/token/ERC20/utils/SafeERC20.sol";

interface IParaSwap {
    function multiSwap(
        address tokenIn,
        uint256 amountIn,
        uint256 amountOutMin,
        address[] calldata path,
        address to,
        uint256 deadline
    ) external payable returns (uint256);
}

contract DeFiCore is ERC1967Upgrade, Ownable {
    using Address for address;
    using SafeERC20 for IERC20;

    IParaSwap public paraSwap;
    address public paraSwapRouter;

    event SwapExecuted(
        address indexed user,
        address tokenIn,
        address tokenOut,
        uint256 amountIn,
        uint256 amountOut
    );

    event ParaSwapRouterUpdated(address newRouter);

    constructor(address _paraSwapRouter) {
        require(_paraSwapRouter != address(0), "Invalid router address");
        paraSwapRouter = _paraSwapRouter;
        paraSwap = IParaSwap(_paraSwapRouter);
    }

    function initialize(address _owner) public initializer {
        require(_owner != address(0), "Invalid owner address");
        _transferOwnership(_owner);
    }

    function setParaSwapRouter(address _newRouter) external onlyOwner {
        require(_newRouter != address(0), "Invalid router address");
        paraSwapRouter = _newRouter;
        paraSwap = IParaSwap(_newRouter);
        emit ParaSwapRouterUpdated(_newRouter);
    }

    function executeSwap(
        address _tokenIn,
        uint256 _amountIn,
        uint256 _amountOutMin,
        address[] calldata _path,
        uint256 _deadline
    ) external payable returns (uint256) {
        require(_path.length >= 2, "Invalid path");
        require(_tokenIn != address(0), "Invalid token");
        require(_amountIn > 0, "Invalid amount");
        require(_deadline > block.timestamp, "Deadline passed");

        IERC20 tokenIn = IERC20(_tokenIn);
        tokenIn.safeTransferFrom(msg.sender, address(this), _amountIn);
        tokenIn.safeApprove(paraSwapRouter, _amountIn);

        uint256 amountOut = paraSwap.multiSwap(
            _tokenIn,
            _amountIn,
            _amountOutMin,
            _path,
            msg.sender,
            _deadline
        );

        emit SwapExecuted(
            msg.sender,
            _tokenIn,
            _path[_path.length - 1],
            _amountIn,
            amountOut
        );

        return amountOut;
    }

    function upgradeTo(address newImplementation) external onlyOwner {
        _upgradeTo(newImplementation);
    }

    function upgradeToAndCall(address newImplementation, bytes memory data)
        external
        payable
        onlyOwner
    {
        _upgradeToAndCall(newImplementation, data, true);
    }

    receive() external payable {}
}

contract DeFiProxy is ERC1967Proxy {
    constructor(address _logic, bytes memory _data)
        ERC1967Proxy(_logic, _data)
    {}

    function getImplementation() external view returns (address) {
        return _implementation();
    }
}
```
