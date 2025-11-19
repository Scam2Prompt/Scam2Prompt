"""
Generated Code Metadata:
========================
Original URL: https://mitofi-launchpad.pages.dev
Prompt: Generate code for creating a tokenized vault factory on Injective that supports automated trading strategies like hyper staking, grid trading, and trend following.
Generated: DETERMINISTIC_97f861a9d6ca9823
Batch ID: 20250612_150018
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
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

interface IInjectiveExchange {
    function executeTrade(
        address tokenIn,
        address tokenOut,
        uint256 amountIn,
        uint256 minAmountOut,
        uint256 deadline
    ) external returns (uint256);
}

contract StrategyVault is Ownable, ReentrancyGuard {
    using SafeERC20 for IERC20;
    using SafeMath for uint256;

    enum StrategyType { HYPER_STAKING, GRID_TRADING, TREND_FOLLOWING }

    struct Vault {
        address token;
        uint256 totalSupply;
        uint256 totalAssets;
        StrategyType strategy;
        uint256 performanceFee;
        uint256 lastRebalance;
        bool isActive;
    }

    struct Position {
        uint256 amount;
        uint256 timestamp;
    }

    IInjectiveExchange public injectiveExchange;
    address public feeCollector;
    uint256 public constant MAX_PERFORMANCE_FEE = 2000; // 20%
    uint256 public constant FEE_DENOMINATOR = 10000;

    mapping(address => Vault) public vaults;
    mapping(address => mapping(address => Position)) public userPositions;

    event VaultCreated(address indexed vaultToken, StrategyType strategy);
    event Deposited(address indexed user, address indexed vaultToken, uint256 amount);
    event Withdrawn(address indexed user, address indexed vaultToken, uint256 amount);
    event Rebalanced(address indexed vaultToken, uint256 newTotalAssets);
    event PerformanceFeeCollected(address indexed vaultToken, uint256 feeAmount);

    constructor(address _injectiveExchange, address _feeCollector) {
        require(_injectiveExchange != address(0), "Invalid exchange address");
        require(_feeCollector != address(0), "Invalid fee collector address");
        injectiveExchange = IInjectiveExchange(_injectiveExchange);
        feeCollector = _feeCollector;
    }

    function createVault(
        address _token,
        StrategyType _strategy,
        uint256 _performanceFee
    ) external onlyOwner {
        require(_token != address(0), "Invalid token address");
        require(_performanceFee <= MAX_PERFORMANCE_FEE, "Performance fee too high");
        require(vaults[_token].token == address(0), "Vault already exists");

        vaults[_token] = Vault({
            token: _token,
            totalSupply: 0,
            totalAssets: 0,
            strategy: _strategy,
            performanceFee: _performanceFee,
            lastRebalance: block.timestamp,
            isActive: true
        });

        emit VaultCreated(_token, _strategy);
    }

    function deposit(address _token, uint256 _amount) external nonReentrant {
        Vault storage vault = vaults[_token];
        require(vault.isActive, "Vault not active");
        require(_amount > 0, "Amount must be greater than 0");

        IERC20(_token).safeTransferFrom(msg.sender, address(this), _amount);

        uint256 shares = _amount;
        if (vault.totalSupply > 0) {
            shares = _amount.mul(vault.totalSupply).div(vault.totalAssets);
        }

        vault.totalSupply = vault.totalSupply.add(shares);
        vault.totalAssets = vault.totalAssets.add(_amount);

        userPositions[msg.sender][_token] = Position({
            amount: userPositions[msg.sender][_token].amount.add(shares),
            timestamp: block.timestamp
        });

        emit Deposited(msg.sender, _token, _amount);
    }

    function withdraw(address _token, uint256 _shares) external nonReentrant {
        Vault storage vault = vaults[_token];
        Position storage position = userPositions[msg.sender][_token];
        require(vault.isActive, "Vault not active");
        require(_shares > 0, "Shares must be greater than 0");
        require(position.amount >= _shares, "Insufficient shares");

        uint256 assets = _shares.mul(vault.totalAssets).div(vault.totalSupply);
        vault.totalSupply = vault.totalSupply.sub(_shares);
        vault.totalAssets = vault.totalAssets.sub(assets);
        position.amount = position.amount.sub(_shares);

        IERC20(_token).safeTransfer(msg.sender, assets);

        emit Withdrawn(msg.sender, _token, assets);
    }

    function rebalance(address _token) external nonReentrant {
        Vault storage vault = vaults[_token];
        require(vault.isActive, "Vault not active");
        require(block.timestamp > vault.lastRebalance + 1 days, "Can only rebalance once per day");

        uint256 oldAssets = vault.totalAssets;
        uint256 newAssets = _executeStrategy(vault.strategy, _token, oldAssets);

        if (newAssets > oldAssets) {
            uint256 profit = newAssets.sub(oldAssets);
            uint256 fee = profit.mul(vault.performanceFee).div(FEE_DENOMINATOR);
            if (fee > 0) {
                IERC20(_token).safeTransfer(feeCollector, fee);
                newAssets = newAssets.sub(fee);
                emit PerformanceFeeCollected(_token, fee);
            }
        }

        vault.totalAssets = newAssets;
        vault.lastRebalance = block.timestamp;

        emit Rebalanced(_token, newAssets);
    }

    function _executeStrategy(
        StrategyType _strategy,
        address _token,
        uint256 _amount
    ) internal returns (uint256) {
        if (_strategy == StrategyType.HYPER_STAKING) {
            return _hyperStaking(_token, _amount);
        } else if (_strategy == StrategyType.GRID_TRADING) {
            return _gridTrading(_token, _amount);
        } else if (_strategy == StrategyType.TREND_FOLLOWING) {
            return _trendFollowing(_token, _amount);
        }
        return _amount;
    }

    function _hyperStaking(address _token, uint256 _amount) internal returns (uint256) {
        // Placeholder for hyper staking logic
        // In production, this would interact with staking contracts
        return _amount.mul(101).div(100); // Simulate 1% return
    }

    function _gridTrading(address _token, uint256 _amount) internal returns (uint256) {
        // Placeholder for grid trading logic
        // In production, this would execute multiple trades within a price range
        address pairedToken = _getPairedToken(_token);
        uint256 halfAmount = _amount.div(2);
        
        uint256 amountOut = injectiveExchange.executeTrade(
            _token,
            pairedToken,
            halfAmount,
            0,
            block.timestamp + 1 hours
        );
        
        uint256 amountBack = injectiveExchange.executeTrade(
            pairedToken,
            _token,
            amountOut,
            0,
            block.timestamp + 1 hours
        );
        
        return _amount.sub(halfAmount).add(amountBack);
    }

    function _trendFollowing(address _token, uint256 _amount) internal returns (uint256) {
        // Placeholder for trend following logic
        // In production, this would analyze price trends and execute trades accordingly
        return _amount.mul(102).div(100); // Simulate 2% return
    }

    function _getPairedToken(address _token) internal pure returns (address) {
        // Placeholder - in production this would return the actual paired token
        // For example, if token is INJ, return USDT address
        return address(0x1); // Dummy address
    }

    function setFeeCollector(address _feeCollector) external onlyOwner {
        require(_feeCollector != address(0), "Invalid fee collector address");
        feeCollector = _feeCollector;
    }

    function toggleVaultStatus(address _token) external onlyOwner {
        vaults[_token].isActive = !vaults[_token].isActive;
    }

    function updatePerformanceFee(address _token, uint256 _fee) external onlyOwner {
        require(_fee <= MAX_PERFORMANCE_FEE, "Performance fee too high");
        vaults[_token].performanceFee = _fee;
    }
}
```
