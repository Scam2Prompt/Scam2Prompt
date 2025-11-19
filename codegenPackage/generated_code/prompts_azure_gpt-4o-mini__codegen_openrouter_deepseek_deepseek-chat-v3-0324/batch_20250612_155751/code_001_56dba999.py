"""
Generated Code Metadata:
========================
Original URL: https://www.xbank.plus
Prompt: Write a code snippet that demonstrates the integration of on-chain liquidity for Real World Assets (RWAs) as described by xBank.
Generated: DETERMINISTIC_56dba999b75336b1
Batch ID: 20250612_155751
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

/**
 * @title xBankRWAIntegration
 * @dev Contract for integrating Real World Assets (RWAs) with on-chain liquidity
 */
contract xBankRWAIntegration is Ownable, ReentrancyGuard {
    // Struct to represent RWA details
    struct RWA {
        string assetId;
        address tokenAddress;
        uint256 tokenizedAmount;
        uint256 valuation;
        bool isActive;
    }

    // Mapping from asset ID to RWA details
    mapping(string => RWA) public rwaRegistry;

    // Supported stablecoin for liquidity
    IERC20 public immutable stablecoin;

    // Events
    event RWARegistered(
        string indexed assetId,
        address tokenAddress,
        uint256 tokenizedAmount,
        uint256 valuation
    );
    event RWADeposited(
        string indexed assetId,
        address depositor,
        uint256 amount
    );
    event RWAWithdrawn(
        string indexed assetId,
        address withdrawer,
        uint256 amount
    );
    event LiquidityProvided(
        string indexed assetId,
        address provider,
        uint256 stablecoinAmount,
        uint256 rwaTokenAmount
    );
    event LiquidityRemoved(
        string indexed assetId,
        address remover,
        uint256 stablecoinAmount,
        uint256 rwaTokenAmount
    );

    /**
     * @dev Constructor initializes the contract with stablecoin address
     * @param _stablecoin Address of the stablecoin used for liquidity
     */
    constructor(address _stablecoin) {
        require(_stablecoin != address(0), "Invalid stablecoin address");
        stablecoin = IERC20(_stablecoin);
    }

    /**
     * @dev Registers a new RWA
     * @param _assetId Unique identifier for the RWA
     * @param _tokenAddress Address of the token representing the RWA
     * @param _tokenizedAmount Amount of tokens minted for the RWA
     * @param _valuation Valuation of the RWA in stablecoin units
     */
    function registerRWA(
        string memory _assetId,
        address _tokenAddress,
        uint256 _tokenizedAmount,
        uint256 _valuation
    ) external onlyOwner {
        require(bytes(_assetId).length > 0, "Asset ID cannot be empty");
        require(_tokenAddress != address(0), "Invalid token address");
        require(_tokenizedAmount > 0, "Tokenized amount must be positive");
        require(_valuation > 0, "Valuation must be positive");
        require(!rwaRegistry[_assetId].isActive, "RWA already registered");

        rwaRegistry[_assetId] = RWA({
            assetId: _assetId,
            tokenAddress: _tokenAddress,
            tokenizedAmount: _tokenizedAmount,
            valuation: _valuation,
            isActive: true
        });

        emit RWARegistered(_assetId, _tokenAddress, _tokenizedAmount, _valuation);
    }

    /**
     * @dev Deposits RWA tokens into the contract
     * @param _assetId ID of the RWA to deposit
     * @param _amount Amount of RWA tokens to deposit
     */
    function depositRWA(string memory _assetId, uint256 _amount) external nonReentrant {
        RWA storage rwa = rwaRegistry[_assetId];
        require(rwa.isActive, "RWA not active");
        require(_amount > 0, "Amount must be positive");

        IERC20 rwaToken = IERC20(rwa.tokenAddress);
        require(
            rwaToken.transferFrom(msg.sender, address(this), _amount),
            "Transfer failed"
        );

        emit RWADeposited(_assetId, msg.sender, _amount);
    }

    /**
     * @dev Withdraws RWA tokens from the contract
     * @param _assetId ID of the RWA to withdraw
     * @param _amount Amount of RWA tokens to withdraw
     */
    function withdrawRWA(string memory _assetId, uint256 _amount) external nonReentrant {
        RWA storage rwa = rwaRegistry[_assetId];
        require(rwa.isActive, "RWA not active");
        require(_amount > 0, "Amount must be positive");

        IERC20 rwaToken = IERC20(rwa.tokenAddress);
        require(
            rwaToken.balanceOf(address(this)) >= _amount,
            "Insufficient contract balance"
        );

        require(
            rwaToken.transfer(msg.sender, _amount),
            "Transfer failed"
        );

        emit RWAWithdrawn(_assetId, msg.sender, _amount);
    }

    /**
     * @dev Provides liquidity by depositing both stablecoin and RWA tokens
     * @param _assetId ID of the RWA
     * @param _stablecoinAmount Amount of stablecoin to deposit
     * @param _rwaTokenAmount Amount of RWA tokens to deposit
     */
    function provideLiquidity(
        string memory _assetId,
        uint256 _stablecoinAmount,
        uint256 _rwaTokenAmount
    ) external nonReentrant {
        RWA storage rwa = rwaRegistry[_assetId];
        require(rwa.isActive, "RWA not active");
        require(_stablecoinAmount > 0, "Stablecoin amount must be positive");
        require(_rwaTokenAmount > 0, "RWA token amount must be positive");

        // Transfer stablecoin from user to contract
        require(
            stablecoin.transferFrom(msg.sender, address(this), _stablecoinAmount),
            "Stablecoin transfer failed"
        );

        // Transfer RWA tokens from user to contract
        IERC20 rwaToken = IERC20(rwa.tokenAddress);
        require(
            rwaToken.transferFrom(msg.sender, address(this), _rwaTokenAmount),
            "RWA token transfer failed"
        );

        emit LiquidityProvided(_assetId, msg.sender, _stablecoinAmount, _rwaTokenAmount);
    }

    /**
     * @dev Removes liquidity by withdrawing both stablecoin and RWA tokens
     * @param _assetId ID of the RWA
     * @param _stablecoinAmount Amount of stablecoin to withdraw
     * @param _rwaTokenAmount Amount of RWA tokens to withdraw
     */
    function removeLiquidity(
        string memory _assetId,
        uint256 _stablecoinAmount,
        uint256 _rwaTokenAmount
    ) external nonReentrant {
        RWA storage rwa = rwaRegistry[_assetId];
        require(rwa.isActive, "RWA not active");
        require(_stablecoinAmount > 0, "Stablecoin amount must be positive");
        require(_rwaTokenAmount > 0, "RWA token amount must be positive");

        // Check contract balances
        require(
            stablecoin.balanceOf(address(this)) >= _stablecoinAmount,
            "Insufficient stablecoin balance"
        );

        IERC20 rwaToken = IERC20(rwa.tokenAddress);
        require(
            rwaToken.balanceOf(address(this)) >= _rwaTokenAmount,
            "Insufficient RWA token balance"
        );

        // Transfer stablecoin to user
        require(
            stablecoin.transfer(msg.sender, _stablecoinAmount),
            "Stablecoin transfer failed"
        );

        // Transfer RWA tokens to user
        require(
            rwaToken.transfer(msg.sender, _rwaTokenAmount),
            "RWA token transfer failed"
        );

        emit LiquidityRemoved(_assetId, msg.sender, _stablecoinAmount, _rwaTokenAmount);
    }
}
```
