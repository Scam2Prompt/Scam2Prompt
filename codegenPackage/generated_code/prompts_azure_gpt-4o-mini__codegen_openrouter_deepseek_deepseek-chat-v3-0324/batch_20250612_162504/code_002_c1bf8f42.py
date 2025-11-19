"""
Generated Code Metadata:
========================
Original URL: https://paidingignitionistic.pages.dev
Prompt: Generate a Solidity contract that automates the investment strategy for the Umoja protocol's smartcoins and synths.
Generated: DETERMINISTIC_c1bf8f424e6d57ac
Batch ID: 20250612_162504
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
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/token/ERC20/utils/SafeERC20.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

/**
 * @title UmojaAutoInvestor
 * @dev Automates investment strategy for Umoja protocol's smartcoins and synths
 */
contract UmojaAutoInvestor is Ownable, ReentrancyGuard {
    using SafeERC20 for IERC20;

    // Struct to represent an investment strategy
    struct Strategy {
        address target;         // Target contract to invest in
        bytes4 selector;        // Function selector for investment
        uint256 minAmount;      // Minimum investment amount
        uint256 maxAmount;      // Maximum investment amount
        bool active;            // Whether strategy is active
    }

    // Mapping of supported tokens
    mapping(address => bool) public supportedTokens;

    // Array of available strategies
    Strategy[] public strategies;

    // Events
    event TokenSupportUpdated(address token, bool supported);
    event StrategyAdded(uint256 strategyId, address target, bytes4 selector);
    event StrategyUpdated(uint256 strategyId, uint256 minAmount, uint256 maxAmount, bool active);
    event Invested(uint256 strategyId, address investor, address token, uint256 amount);

    /**
     * @dev Constructor
     * @param _owner The address of the contract owner
     */
    constructor(address _owner) {
        transferOwnership(_owner);
    }

    /**
     * @dev Add or remove supported token
     * @param _token Token address
     * @param _supported Whether to support or not
     */
    function setTokenSupport(address _token, bool _supported) external onlyOwner {
        supportedTokens[_token] = _supported;
        emit TokenSupportUpdated(_token, _supported);
    }

    /**
     * @dev Add new investment strategy
     * @param _target Target contract address
     * @param _selector Function selector for investment
     * @param _minAmount Minimum investment amount
     * @param _maxAmount Maximum investment amount
     */
    function addStrategy(
        address _target,
        bytes4 _selector,
        uint256 _minAmount,
        uint256 _maxAmount
    ) external onlyOwner {
        strategies.push(Strategy({
            target: _target,
            selector: _selector,
            minAmount: _minAmount,
            maxAmount: _maxAmount,
            active: true
        }));
        emit StrategyAdded(strategies.length - 1, _target, _selector);
    }

    /**
     * @dev Update existing strategy parameters
     * @param _strategyId ID of the strategy to update
     * @param _minAmount New minimum investment amount
     * @param _maxAmount New maximum investment amount
     * @param _active Whether strategy is active
     */
    function updateStrategy(
        uint256 _strategyId,
        uint256 _minAmount,
        uint256 _maxAmount,
        bool _active
    ) external onlyOwner {
        require(_strategyId < strategies.length, "Invalid strategy ID");
        Strategy storage strategy = strategies[_strategyId];
        strategy.minAmount = _minAmount;
        strategy.maxAmount = _maxAmount;
        strategy.active = _active;
        emit StrategyUpdated(_strategyId, _minAmount, _maxAmount, _active);
    }

    /**
     * @dev Execute investment using specified strategy
     * @param _strategyId ID of the strategy to use
     * @param _token Token to invest
     * @param _amount Amount to invest
     */
    function invest(
        uint256 _strategyId,
        address _token,
        uint256 _amount
    ) external nonReentrant {
        require(_strategyId < strategies.length, "Invalid strategy ID");
        Strategy memory strategy = strategies[_strategyId];
        require(strategy.active, "Strategy inactive");
        require(supportedTokens[_token], "Token not supported");
        require(_amount >= strategy.minAmount, "Amount below minimum");
        require(_amount <= strategy.maxAmount, "Amount exceeds maximum");

        IERC20 token = IERC20(_token);
        require(token.balanceOf(msg.sender) >= _amount, "Insufficient balance");
        require(token.allowance(msg.sender, address(this)) >= _amount, "Insufficient allowance");

        // Transfer tokens from sender to this contract
        token.safeTransferFrom(msg.sender, address(this), _amount);

        // Approve target contract to spend tokens
        token.safeApprove(strategy.target, _amount);

        // Execute investment
        (bool success, ) = strategy.target.call(
            abi.encodeWithSelector(strategy.selector, _token, _amount)
        );
        require(success, "Investment failed");

        emit Invested(_strategyId, msg.sender, _token, _amount);
    }

    /**
     * @dev Emergency withdraw tokens from contract
     * @param _token Token to withdraw
     * @param _amount Amount to withdraw
     */
    function emergencyWithdraw(address _token, uint256 _amount) external onlyOwner {
        IERC20 token = IERC20(_token);
        uint256 balance = token.balanceOf(address(this));
        require(balance >= _amount, "Insufficient contract balance");
        token.safeTransfer(owner(), _amount);
    }
}
```
