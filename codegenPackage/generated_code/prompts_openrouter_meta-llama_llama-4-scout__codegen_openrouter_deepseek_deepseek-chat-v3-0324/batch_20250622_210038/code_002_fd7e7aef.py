"""
Generated Code Metadata:
========================
Original URL: https://synthr-verify.pages.dev
Prompt: Generate a smart contract code for creating a cross-chain perpetuals trading platform using SYNTHR's omnichain synthetic assets.
Generated: DETERMINISTIC_fd7e7aefc729ed52
Batch ID: 20250622_210038
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
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

interface ISynthrBridge {
    function sendDepositCollateral(address _account, bytes32 _collateralKey, uint256 _amount) external;
    function sendWithdrawCollateral(address _account, bytes32 _collateralKey, uint256 _amount) external;
    function sendOpenPosition(
        address _account,
        bytes32 _synthKey,
        uint256 _amount,
        uint256 _leverage,
        bool _isLong
    ) external;
    function sendClosePosition(
        address _account,
        bytes32 _synthKey,
        uint256 _amount
    ) external;
}

contract PerpetualsPlatform is ReentrancyGuard, Ownable {
    using SafeMath for uint256;

    struct Position {
        bytes32 synthKey;
        uint256 amount;
        uint256 leverage;
        bool isLong;
        uint256 entryPrice;
        uint256 timestamp;
    }

    mapping(address => mapping(bytes32 => uint256)) public collateralBalances;
    mapping(address => Position[]) public positions;
    mapping(bytes32 => uint256) public synthPrices;

    ISynthrBridge public synthrBridge;
    address public feeCollector;
    uint256 public feeRate = 30; // 0.3% in basis points (10000 = 100%)

    event CollateralDeposited(address indexed account, bytes32 indexed collateralKey, uint256 amount);
    event CollateralWithdrawn(address indexed account, bytes32 indexed collateralKey, uint256 amount);
    event PositionOpened(address indexed account, bytes32 indexed synthKey, uint256 amount, uint256 leverage, bool isLong);
    event PositionClosed(address indexed account, bytes32 indexed synthKey, uint256 amount, uint256 pnl);
    event FeeCollected(address indexed account, uint256 amount);

    constructor(address _synthrBridge, address _feeCollector) {
        synthrBridge = ISynthrBridge(_synthrBridge);
        feeCollector = _feeCollector;
    }

    function depositCollateral(bytes32 _collateralKey, uint256 _amount) external nonReentrant {
        require(_amount > 0, "Amount must be greater than 0");
        
        IERC20 collateralToken = IERC20(address(uint160(uint256(_collateralKey))));
        require(collateralToken.transferFrom(msg.sender, address(this), _amount), "Transfer failed");

        collateralBalances[msg.sender][_collateralKey] = collateralBalances[msg.sender][_collateralKey].add(_amount);
        synthrBridge.sendDepositCollateral(msg.sender, _collateralKey, _amount);

        emit CollateralDeposited(msg.sender, _collateralKey, _amount);
    }

    function withdrawCollateral(bytes32 _collateralKey, uint256 _amount) external nonReentrant {
        require(_amount > 0, "Amount must be greater than 0");
        require(collateralBalances[msg.sender][_collateralKey] >= _amount, "Insufficient collateral");

        collateralBalances[msg.sender][_collateralKey] = collateralBalances[msg.sender][_collateralKey].sub(_amount);
        synthrBridge.sendWithdrawCollateral(msg.sender, _collateralKey, _amount);

        IERC20 collateralToken = IERC20(address(uint160(uint256(_collateralKey))));
        require(collateralToken.transfer(msg.sender, _amount), "Transfer failed");

        emit CollateralWithdrawn(msg.sender, _collateralKey, _amount);
    }

    function openPosition(
        bytes32 _synthKey,
        uint256 _amount,
        uint256 _leverage,
        bool _isLong
    ) external nonReentrant {
        require(_amount > 0, "Amount must be greater than 0");
        require(_leverage > 0, "Leverage must be greater than 0");
        require(synthPrices[_synthKey] > 0, "Invalid synth price");

        uint256 collateralNeeded = _amount.mul(_leverage).div(synthPrices[_synthKey]);
        require(collateralBalances[msg.sender][_synthKey] >= collateralNeeded, "Insufficient collateral");

        uint256 fee = _amount.mul(feeRate).div(10000);
        uint256 amountAfterFee = _amount.sub(fee);

        collateralBalances[msg.sender][_synthKey] = collateralBalances[msg.sender][_synthKey].sub(collateralNeeded);
        
        positions[msg.sender].push(Position({
            synthKey: _synthKey,
            amount: amountAfterFee,
            leverage: _leverage,
            isLong: _isLong,
            entryPrice: synthPrices[_synthKey],
            timestamp: block.timestamp
        }));

        synthrBridge.sendOpenPosition(msg.sender, _synthKey, amountAfterFee, _leverage, _isLong);

        if (fee > 0) {
            IERC20 synthToken = IERC20(address(uint160(uint256(_synthKey))));
            require(synthToken.transfer(feeCollector, fee), "Fee transfer failed");
            emit FeeCollected(msg.sender, fee);
        }

        emit PositionOpened(msg.sender, _synthKey, amountAfterFee, _leverage, _isLong);
    }

    function closePosition(uint256 _positionIndex) external nonReentrant {
        require(_positionIndex < positions[msg.sender].length, "Invalid position index");
        Position memory position = positions[msg.sender][_positionIndex];

        uint256 currentPrice = synthPrices[position.synthKey];
        uint256 pnl = calculatePnl(position.amount, position.entryPrice, currentPrice, position.leverage, position.isLong);

        uint256 collateralToReturn = position.amount.mul(position.leverage).div(position.entryPrice);
        collateralBalances[msg.sender][position.synthKey] = collateralBalances[msg.sender][position.synthKey].add(collateralToReturn.add(pnl));

        synthrBridge.sendClosePosition(msg.sender, position.synthKey, position.amount);

        // Remove the position
        positions[msg.sender][_positionIndex] = positions[msg.sender][positions[msg.sender].length - 1];
        positions[msg.sender].pop();

        emit PositionClosed(msg.sender, position.synthKey, position.amount, pnl);
    }

    function calculatePnl(
        uint256 _amount,
        uint256 _entryPrice,
        uint256 _currentPrice,
        uint256 _leverage,
        bool _isLong
    ) public pure returns (uint256) {
        if (_isLong) {
            return _amount.mul(_leverage).mul(_currentPrice.sub(_entryPrice)).div(_entryPrice);
        } else {
            return _amount.mul(_leverage).mul(_entryPrice.sub(_currentPrice)).div(_entryPrice);
        }
    }

    function updateSynthPrice(bytes32 _synthKey, uint256 _price) external onlyOwner {
        require(_price > 0, "Price must be greater than 0");
        synthPrices[_synthKey] = _price;
    }

    function setFeeRate(uint256 _newFeeRate) external onlyOwner {
        require(_newFeeRate <= 1000, "Fee rate too high"); // Max 10%
        feeRate = _newFeeRate;
    }

    function setFeeCollector(address _newFeeCollector) external onlyOwner {
        require(_newFeeCollector != address(0), "Invalid address");
        feeCollector = _newFeeCollector;
    }

    function getPositions(address _account) external view returns (Position[] memory) {
        return positions[_account];
    }

    function getCollateralBalance(address _account, bytes32 _collateralKey) external view returns (uint256) {
        return collateralBalances[_account][_collateralKey];
    }
}
```
