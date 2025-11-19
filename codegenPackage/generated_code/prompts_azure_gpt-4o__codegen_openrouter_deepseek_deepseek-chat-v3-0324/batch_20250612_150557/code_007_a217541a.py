"""
Generated Code Metadata:
========================
Original URL: https://eggdex.online
Prompt: Write a script to enable collateral sharing across multiple smart contracts for margin trading on DX25, ensuring exposure offsetting and portfolio risk management.
Generated: DETERMINISTIC_a217541af17ae066
Batch ID: 20250612_150557
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
 * @title CollateralManager
 * @dev Manages collateral sharing across multiple smart contracts for margin trading
 */
contract CollateralManager is Ownable, ReentrancyGuard {
    using SafeERC20 for IERC20;

    struct Position {
        address trader;
        address collateralToken;
        uint256 collateralAmount;
        uint256 leveragedAmount;
        bool isActive;
    }

    struct ContractInfo {
        address contractAddress;
        bool isWhitelisted;
    }

    // Mapping from position ID to Position
    mapping(bytes32 => Position) public positions;

    // Mapping from contract address to whitelist status
    mapping(address => bool) public whitelistedContracts;

    // Mapping from trader to total collateral value
    mapping(address => uint256) public totalCollateralValue;

    // Mapping from trader to total exposure
    mapping(address => uint256) public totalExposure;

    // Supported collateral tokens
    mapping(address => bool) public supportedCollateralTokens;

    // Events
    event PositionOpened(
        bytes32 positionId,
        address indexed trader,
        address indexed collateralToken,
        uint256 collateralAmount,
        uint256 leveragedAmount,
        address indexed contractAddress
    );

    event PositionClosed(
        bytes32 positionId,
        address indexed trader,
        address indexed collateralToken,
        uint256 collateralReturned,
        uint256 leveragedAmount,
        address indexed contractAddress
    );

    event CollateralDeposited(
        address indexed trader,
        address indexed token,
        uint256 amount
    );

    event CollateralWithdrawn(
        address indexed trader,
        address indexed token,
        uint256 amount
    );

    event ContractWhitelisted(address indexed contractAddress);
    event ContractBlacklisted(address indexed contractAddress);
    event CollateralTokenAdded(address indexed token);
    event CollateralTokenRemoved(address indexed token);

    /**
     * @dev Modifier to check if the caller is a whitelisted contract
     */
    modifier onlyWhitelisted() {
        require(
            whitelistedContracts[msg.sender],
            "CollateralManager: Caller not whitelisted"
        );
        _;
    }

    /**
     * @dev Initialize the contract with supported collateral tokens
     * @param _collateralTokens Array of supported collateral token addresses
     */
    constructor(address[] memory _collateralTokens) {
        for (uint256 i = 0; i < _collateralTokens.length; i++) {
            supportedCollateralTokens[_collateralTokens[i]] = true;
        }
    }

    /**
     * @dev Whitelist a contract address
     * @param _contractAddress Address of the contract to whitelist
     */
    function whitelistContract(address _contractAddress) external onlyOwner {
        require(
            !whitelistedContracts[_contractAddress],
            "CollateralManager: Contract already whitelisted"
        );
        whitelistedContracts[_contractAddress] = true;
        emit ContractWhitelisted(_contractAddress);
    }

    /**
     * @dev Blacklist a contract address
     * @param _contractAddress Address of the contract to blacklist
     */
    function blacklistContract(address _contractAddress) external onlyOwner {
        require(
            whitelistedContracts[_contractAddress],
            "CollateralManager: Contract not whitelisted"
        );
        whitelistedContracts[_contractAddress] = false;
        emit ContractBlacklisted(_contractAddress);
    }

    /**
     * @dev Add a supported collateral token
     * @param _token Address of the token to add
     */
    function addCollateralToken(address _token) external onlyOwner {
        require(
            !supportedCollateralTokens[_token],
            "CollateralManager: Token already supported"
        );
        supportedCollateralTokens[_token] = true;
        emit CollateralTokenAdded(_token);
    }

    /**
     * @dev Remove a supported collateral token
     * @param _token Address of the token to remove
     */
    function removeCollateralToken(address _token) external onlyOwner {
        require(
            supportedCollateralTokens[_token],
            "CollateralManager: Token not supported"
        );
        supportedCollateralTokens[_token] = false;
        emit CollateralTokenRemoved(_token);
    }

    /**
     * @dev Deposit collateral for margin trading
     * @param _token Address of the collateral token
     * @param _amount Amount of collateral to deposit
     */
    function depositCollateral(address _token, uint256 _amount)
        external
        nonReentrant
    {
        require(
            supportedCollateralTokens[_token],
            "CollateralManager: Token not supported"
        );
        require(_amount > 0, "CollateralManager: Amount must be greater than 0");

        IERC20(_token).safeTransferFrom(msg.sender, address(this), _amount);
        totalCollateralValue[msg.sender] += _amount;

        emit CollateralDeposited(msg.sender, _token, _amount);
    }

    /**
     * @dev Withdraw collateral from margin trading
     * @param _token Address of the collateral token
     * @param _amount Amount of collateral to withdraw
     */
    function withdrawCollateral(address _token, uint256 _amount)
        external
        nonReentrant
    {
        require(
            supportedCollateralTokens[_token],
            "CollateralManager: Token not supported"
        );
        require(_amount > 0, "CollateralManager: Amount must be greater than 0");
        require(
            totalCollateralValue[msg.sender] >= _amount,
            "CollateralManager: Insufficient collateral"
        );

        // Check if withdrawal would violate margin requirements
        require(
            (totalCollateralValue[msg.sender] - _amount) * 100 >=
                totalExposure[msg.sender] * 110,
            "CollateralManager: Withdrawal violates margin requirements"
        );

        totalCollateralValue[msg.sender] -= _amount;
        IERC20(_token).safeTransfer(msg.sender, _amount);

        emit CollateralWithdrawn(msg.sender, _token, _amount);
    }

    /**
     * @dev Open a new leveraged position (called by whitelisted contracts)
     * @param _trader Address of the trader
     * @param _collateralToken Address of the collateral token
     * @param _collateralAmount Amount of collateral used
     * @param _leveragedAmount Amount of leveraged position
     * @return positionId The ID of the new position
     */
    function openPosition(
        address _trader,
        address _collateralToken,
        uint256 _collateralAmount,
        uint256 _leveragedAmount
    ) external onlyWhitelisted nonReentrant returns (bytes32 positionId) {
        require(
            totalCollateralValue[_trader] >= _collateralAmount,
            "CollateralManager: Insufficient collateral"
        );

        positionId = keccak256(
            abi.encodePacked(
                _trader,
                _collateralToken,
                _collateralAmount,
                _leveragedAmount,
                block.timestamp
            )
        );

        positions[positionId] = Position({
            trader: _trader,
            collateralToken: _collateralToken,
            collateralAmount: _collateralAmount,
            leveragedAmount: _leveragedAmount,
            isActive: true
        });

        totalExposure[_trader] += _leveragedAmount;

        // Check margin requirements (110% of exposure)
        require(
            totalCollateralValue[_trader] * 100 >= totalExposure[_trader] * 110,
            "CollateralManager: Position violates margin requirements"
        );

        emit PositionOpened(
            positionId,
            _trader,
            _collateralToken,
            _collateralAmount,
            _leveragedAmount,
            msg.sender
        );

        return positionId;
    }

    /**
     * @dev Close an existing position (called by whitelisted contracts)
     * @param _positionId ID of the position to close
     * @param _collateralReturned Amount of collateral returned to trader
     * @param _profitOrLoss Profit or loss amount (positive for profit, negative for loss)
     */
    function closePosition(
        bytes32 _positionId,
        uint256 _collateralReturned,
        int256 _profitOrLoss
    ) external onlyWhitelisted nonReentrant {
        Position storage position = positions[_positionId];
        require(position.isActive, "CollateralManager: Position not active");

        position.isActive = false;
        totalExposure[position.trader] -= position.leveragedAmount;

        if (_profitOrLoss > 0) {
            totalCollateralValue[position.trader] += uint256(_profitOrLoss);
        } else if (_profitOrLoss < 0) {
            totalCollateralValue[position.trader] -= uint
