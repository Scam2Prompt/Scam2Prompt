"""
Generated Code Metadata:
========================
Original URL: https://op-enocean.github.io
Prompt: Design a smart contract architecture that leverages Open Ocean for secure cross-contract interactions, including multiple use cases.
Generated: DETERMINISTIC_1f40884594f4cb32
Batch ID: 20250622_210821
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
import "@openzeppelin/contracts/token/ERC20/utils/SafeERC20.sol";

/**
 * @title OpenOceanIntegration
 * @dev Smart contract for secure cross-contract interactions using OpenOcean
 */
contract OpenOceanIntegration is Ownable, ReentrancyGuard {
    using SafeERC20 for IERC20;

    // OpenOcean router address
    address public openOceanRouter;

    // Mapping of approved contracts for interaction
    mapping(address => bool) public approvedContracts;

    // Events
    event OpenOceanSwap(
        address indexed user,
        address indexed tokenIn,
        address indexed tokenOut,
        uint256 amountIn,
        uint256 amountOut
    );
    event ContractApproved(address indexed contractAddress);
    event ContractRevoked(address indexed contractAddress);

    /**
     * @dev Constructor
     * @param _openOceanRouter Address of OpenOcean router contract
     */
    constructor(address _openOceanRouter) {
        require(_openOceanRouter != address(0), "Invalid router address");
        openOceanRouter = _openOceanRouter;
    }

    /**
     * @dev Approve a contract for interaction
     * @param _contract Address of the contract to approve
     */
    function approveContract(address _contract) external onlyOwner {
        require(_contract != address(0), "Invalid contract address");
        approvedContracts[_contract] = true;
        emit ContractApproved(_contract);
    }

    /**
     * @dev Revoke approval for a contract
     * @param _contract Address of the contract to revoke
     */
    function revokeContract(address _contract) external onlyOwner {
        require(approvedContracts[_contract], "Contract not approved");
        approvedContracts[_contract] = false;
        emit ContractRevoked(_contract);
    }

    /**
     * @dev Execute a swap through OpenOcean
     * @param _tokenIn Address of input token
     * @param _tokenOut Address of output token
     * @param _amountIn Amount of input token
     * @param _minAmountOut Minimum amount of output token expected
     * @param _data Additional swap data for OpenOcean
     */
    function executeSwap(
        address _tokenIn,
        address _tokenOut,
        uint256 _amountIn,
        uint256 _minAmountOut,
        bytes calldata _data
    ) external nonReentrant {
        require(_amountIn > 0, "Amount must be greater than 0");
        require(_tokenIn != address(0) && _tokenOut != address(0), "Invalid token address");

        IERC20 tokenIn = IERC20(_tokenIn);
        tokenIn.safeTransferFrom(msg.sender, address(this), _amountIn);
        tokenIn.safeApprove(openOceanRouter, _amountIn);

        (bool success, bytes memory result) = openOceanRouter.call(_data);
        require(success, "Swap failed");

        uint256 amountOut = IERC20(_tokenOut).balanceOf(address(this));
        require(amountOut >= _minAmountOut, "Insufficient output amount");

        IERC20(_tokenOut).safeTransfer(msg.sender, amountOut);

        emit OpenOceanSwap(msg.sender, _tokenIn, _tokenOut, _amountIn, amountOut);
    }

    /**
     * @dev Execute a cross-contract call
     * @param _target Address of target contract
     * @param _value Amount of ETH to send
     * @param _data Call data
     */
    function executeCall(
        address _target,
        uint256 _value,
        bytes calldata _data
    ) external nonReentrant {
        require(approvedContracts[_target], "Contract not approved");
        (bool success, ) = _target.call{value: _value}(_data);
        require(success, "Call failed");
    }

    /**
     * @dev Withdraw tokens from the contract
     * @param _token Address of token to withdraw
     * @param _amount Amount to withdraw
     */
    function withdrawTokens(address _token, uint256 _amount) external onlyOwner {
        require(_amount > 0, "Amount must be greater than 0");
        IERC20(_token).safeTransfer(msg.sender, _amount);
    }

    /**
     * @dev Withdraw ETH from the contract
     * @param _amount Amount to withdraw
     */
    function withdrawETH(uint256 _amount) external onlyOwner {
        require(_amount > 0, "Amount must be greater than 0");
        payable(msg.sender).transfer(_amount);
    }

    // Receive ETH
    receive() external payable {}
}

/**
 * @title LendingPlatform
 * @dev Example use case: Lending platform integration
 */
contract LendingPlatform is Ownable, ReentrancyGuard {
    using SafeERC20 for IERC20;

    // OpenOcean integration contract
    OpenOceanIntegration public openOceanIntegration;

    // Events
    event Deposit(address indexed user, address indexed token, uint256 amount);
    event Withdraw(address indexed user, address indexed token, uint256 amount);
    event Borrow(address indexed user, address indexed token, uint256 amount);
    event Repay(address indexed user, address indexed token, uint256 amount);

    /**
     * @dev Constructor
     * @param _openOceanIntegration Address of OpenOcean integration contract
     */
    constructor(address _openOceanIntegration) {
        openOceanIntegration = OpenOceanIntegration(_openOceanIntegration);
    }

    /**
     * @dev Deposit tokens into the lending platform
     * @param _token Address of token to deposit
     * @param _amount Amount to deposit
     */
    function deposit(address _token, uint256 _amount) external nonReentrant {
        require(_amount > 0, "Amount must be greater than 0");
        IERC20(_token).safeTransferFrom(msg.sender, address(this), _amount);
        emit Deposit(msg.sender, _token, _amount);
    }

    /**
     * @dev Withdraw tokens from the lending platform
     * @param _token Address of token to withdraw
     * @param _amount Amount to withdraw
     */
    function withdraw(address _token, uint256 _amount) external nonReentrant {
        require(_amount > 0, "Amount must be greater than 0");
        IERC20(_token).safeTransfer(msg.sender, _amount);
        emit Withdraw(msg.sender, _token, _amount);
    }

    /**
     * @dev Borrow tokens using OpenOcean swap
     * @param _collateralToken Address of collateral token
     * @param _borrowToken Address of token to borrow
     * @param _collateralAmount Amount of collateral
     * @param _minBorrowAmount Minimum amount to borrow
     * @param _swapData OpenOcean swap data
     */
    function borrow(
        address _collateralToken,
        address _borrowToken,
        uint256 _collateralAmount,
        uint256 _minBorrowAmount,
        bytes calldata _swapData
    ) external nonReentrant {
        require(_collateralAmount > 0, "Amount must be greater than 0");
        
        IERC20(_collateralToken).safeTransferFrom(msg.sender, address(this), _collateralAmount);
        IERC20(_collateralToken).safeApprove(address(openOceanIntegration), _collateralAmount);

        openOceanIntegration.executeSwap(
            _collateralToken,
            _borrowToken,
            _collateralAmount,
            _minBorrowAmount,
            _swapData
        );

        uint256 borrowAmount = IERC20(_borrowToken).balanceOf(address(this));
        IERC20(_borrowToken).safeTransfer(msg.sender, borrowAmount);

        emit Borrow(msg.sender, _borrowToken, borrowAmount);
    }

    /**
     * @dev Repay borrowed tokens
     * @param _token Address of token to repay
     * @param _amount Amount to repay
     */
    function repay(address _token, uint256 _amount) external nonReentrant {
        require(_amount > 0, "Amount must be greater than 0");
        IERC20(_token).safeTransferFrom(msg.sender, address(this), _amount);
        emit Repay(msg.sender, _token, _amount);
    }
}

/**
 * @title YieldAggregator
 * @dev Example use case: Yield aggregation
 */
contract YieldAggregator is Ownable, ReentrancyGuard {
    using SafeERC20 for IERC20;

    // OpenOcean integration contract
    OpenOceanIntegration public openOceanIntegration;

    // Events
    event Invest(address indexed user, address indexed token, uint256 amount);
    event WithdrawYield(address indexed user, address indexed token, uint256 amount);

    /**
     * @dev Constructor
     * @param _openOceanIntegration Address of OpenOcean integration contract
     */
    constructor(address _openOceanIntegration) {
        openOceanIntegration = OpenOceanIntegration(_openOceanIntegration);
