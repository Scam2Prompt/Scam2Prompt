"""
Generated Code Metadata:
========================
Original URL: https://www.zkfinance.org
Prompt: Develop a decentralized application (dApp) that connects to zkFinance's lending markets for prime assets, ensuring low fees and high security using zkSync.
Generated: DETERMINISTIC_e3537479a8819be7
Batch ID: 20250612_153547
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

import "@matterlabs/zksync-contracts/l2/contracts/interfaces/IZkSync.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title zkFinanceLending
 * @dev A decentralized lending application for prime assets on zkSync
 */
contract zkFinanceLending is ReentrancyGuard {
    using SafeMath for uint256;

    // zkSync contract interface
    IZkSync public immutable zkSync;

    // Supported assets
    struct Asset {
        bool isSupported;
        uint256 totalSupplied;
        uint256 totalBorrowed;
        uint256 interestRate;
    }

    // User balances
    struct UserBalance {
        uint256 supplied;
        uint256 borrowed;
    }

    // Mapping of supported assets
    mapping(address => Asset) public supportedAssets;
    
    // Mapping of user balances per asset
    mapping(address => mapping(address => UserBalance)) public userBalances;

    // Events
    event AssetAdded(address indexed asset, uint256 interestRate);
    event AssetSupplied(address indexed user, address indexed asset, uint256 amount);
    event AssetBorrowed(address indexed user, address indexed asset, uint256 amount);
    event AssetRepaid(address indexed user, address indexed asset, uint256 amount);
    event AssetWithdrawn(address indexed user, address indexed asset, uint256 amount);

    /**
     * @dev Constructor
     * @param _zkSyncAddress Address of the zkSync contract
     */
    constructor(address _zkSyncAddress) {
        require(_zkSyncAddress != address(0), "Invalid zkSync address");
        zkSync = IZkSync(_zkSyncAddress);
    }

    /**
     * @dev Add a new supported asset
     * @param _asset Address of the ERC20 token
     * @param _interestRate Initial interest rate (APY in basis points)
     */
    function addSupportedAsset(address _asset, uint256 _interestRate) external {
        require(_asset != address(0), "Invalid asset address");
        require(!supportedAssets[_asset].isSupported, "Asset already supported");
        require(_interestRate > 0, "Interest rate must be positive");

        supportedAssets[_asset] = Asset({
            isSupported: true,
            totalSupplied: 0,
            totalBorrowed: 0,
            interestRate: _interestRate
        });

        emit AssetAdded(_asset, _interestRate);
    }

    /**
     * @dev Supply assets to the lending pool
     * @param _asset Address of the ERC20 token
     * @param _amount Amount to supply
     */
    function supply(address _asset, uint256 _amount) external nonReentrant {
        require(supportedAssets[_asset].isSupported, "Asset not supported");
        require(_amount > 0, "Amount must be positive");

        // Transfer tokens from user to contract
        IERC20(_asset).transferFrom(msg.sender, address(this), _amount);

        // Update balances
        userBalances[msg.sender][_asset].supplied = userBalances[msg.sender][_asset].supplied.add(_amount);
        supportedAssets[_asset].totalSupplied = supportedAssets[_asset].totalSupplied.add(_amount);

        emit AssetSupplied(msg.sender, _asset, _amount);
    }

    /**
     * @dev Borrow assets from the lending pool
     * @param _asset Address of the ERC20 token
     * @param _amount Amount to borrow
     */
    function borrow(address _asset, uint256 _amount) external nonReentrant {
        require(supportedAssets[_asset].isSupported, "Asset not supported");
        require(_amount > 0, "Amount must be positive");
        require(
            _amount <= getAvailableLiquidity(_asset),
            "Insufficient liquidity"
        );

        // Update balances
        userBalances[msg.sender][_asset].borrowed = userBalances[msg.sender][_asset].borrowed.add(_amount);
        supportedAssets[_asset].totalBorrowed = supportedAssets[_asset].totalBorrowed.add(_amount);

        // Transfer tokens to user
        IERC20(_asset).transfer(msg.sender, _amount);

        emit AssetBorrowed(msg.sender, _asset, _amount);
    }

    /**
     * @dev Repay borrowed assets
     * @param _asset Address of the ERC20 token
     * @param _amount Amount to repay
     */
    function repay(address _asset, uint256 _amount) external nonReentrant {
        require(supportedAssets[_asset].isSupported, "Asset not supported");
        require(_amount > 0, "Amount must be positive");
        require(
            userBalances[msg.sender][_asset].borrowed >= _amount,
            "Repay amount exceeds borrowed amount"
        );

        // Transfer tokens from user to contract
        IERC20(_asset).transferFrom(msg.sender, address(this), _amount);

        // Update balances
        userBalances[msg.sender][_asset].borrowed = userBalances[msg.sender][_asset].borrowed.sub(_amount);
        supportedAssets[_asset].totalBorrowed = supportedAssets[_asset].totalBorrowed.sub(_amount);

        emit AssetRepaid(msg.sender, _asset, _amount);
    }

    /**
     * @dev Withdraw supplied assets
     * @param _asset Address of the ERC20 token
     * @param _amount Amount to withdraw
     */
    function withdraw(address _asset, uint256 _amount) external nonReentrant {
        require(supportedAssets[_asset].isSupported, "Asset not supported");
        require(_amount > 0, "Amount must be positive");
        require(
            userBalances[msg.sender][_asset].supplied >= _amount,
            "Withdraw amount exceeds supplied amount"
        );
        require(
            _amount <= getAvailableLiquidity(_asset),
            "Insufficient liquidity"
        );

        // Update balances
        userBalances[msg.sender][_asset].supplied = userBalances[msg.sender][_asset].supplied.sub(_amount);
        supportedAssets[_asset].totalSupplied = supportedAssets[_asset].totalSupplied.sub(_amount);

        // Transfer tokens to user
        IERC20(_asset).transfer(msg.sender, _amount);

        emit AssetWithdrawn(msg.sender, _asset, _amount);
    }

    /**
     * @dev Get available liquidity for an asset
     * @param _asset Address of the ERC20 token
     * @return Available liquidity
     */
    function getAvailableLiquidity(address _asset) public view returns (uint256) {
        return supportedAssets[_asset].totalSupplied.sub(supportedAssets[_asset].totalBorrowed);
    }

    /**
     * @dev Get user's supply balance for an asset
     * @param _user User address
     * @param _asset Address of the ERC20 token
     * @return Supply balance
     */
    function getUserSupplyBalance(address _user, address _asset) external view returns (uint256) {
        return userBalances[_user][_asset].supplied;
    }

    /**
     * @dev Get user's borrow balance for an asset
     * @param _user User address
     * @param _asset Address of the ERC20 token
     * @return Borrow balance
     */
    function getUserBorrowBalance(address _user, address _asset) external view returns (uint256) {
        return userBalances[_user][_asset].borrowed;
    }
}
```
