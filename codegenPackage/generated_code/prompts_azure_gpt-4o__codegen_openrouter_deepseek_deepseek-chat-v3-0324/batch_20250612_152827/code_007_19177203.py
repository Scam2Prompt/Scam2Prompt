"""
Generated Code Metadata:
========================
Original URL: https://bafybeifqb523rma32dtbtz2yeebyhpqrdvv7pt4basdjhn2uhdzoyvslai.ipfs.dweb.link
Prompt: Write a Solidity contract that allows users to lend $DAI, $USDC, or $WETH and earn yield, replicating the Vault functionality described in the Gains Network ecosystem.
Generated: DETERMINISTIC_1917720317c53e38
Batch ID: 20250612_152827
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

contract GainsVault is Ownable, ReentrancyGuard {
    using SafeERC20 for IERC20;

    struct Asset {
        IERC20 token;
        uint256 totalDeposits;
        uint256 totalShares;
        uint256 lastYieldTimestamp;
        uint256 yieldRate; // Annual yield rate in basis points (1% = 100)
    }

    mapping(address => Asset) public assets;
    mapping(address => mapping(address => uint256)) public userShares;

    event Deposit(address indexed user, address indexed asset, uint256 amount, uint256 shares);
    event Withdraw(address indexed user, address indexed asset, uint256 amount, uint256 shares);
    event YieldDistributed(address indexed asset, uint256 amount);
    event AssetAdded(address indexed asset, uint256 yieldRate);
    event YieldRateUpdated(address indexed asset, uint256 newYieldRate);

    constructor() {
        // Initialize with empty constructor
    }

    /**
     * @dev Add a new supported asset with its yield rate
     * @param _token Address of the ERC20 token
     * @param _yieldRate Annual yield rate in basis points (1% = 100)
     */
    function addAsset(address _token, uint256 _yieldRate) external onlyOwner {
        require(_token != address(0), "Invalid token address");
        require(assets[_token].token == IERC20(address(0)), "Asset already exists");
        require(_yieldRate > 0 && _yieldRate <= 10000, "Invalid yield rate");

        assets[_token] = Asset({
            token: IERC20(_token),
            totalDeposits: 0,
            totalShares: 0,
            lastYieldTimestamp: block.timestamp,
            yieldRate: _yieldRate
        });

        emit AssetAdded(_token, _yieldRate);
    }

    /**
     * @dev Update yield rate for an asset
     * @param _token Address of the ERC20 token
     * @param _newYieldRate New annual yield rate in basis points (1% = 100)
     */
    function updateYieldRate(address _token, uint256 _newYieldRate) external onlyOwner {
        require(assets[_token].token != IERC20(address(0)), "Asset does not exist");
        require(_newYieldRate > 0 && _newYieldRate <= 10000, "Invalid yield rate");

        _distributeYield(_token);
        assets[_token].yieldRate = _newYieldRate;

        emit YieldRateUpdated(_token, _newYieldRate);
    }

    /**
     * @dev Deposit tokens into the vault
     * @param _token Address of the ERC20 token to deposit
     * @param _amount Amount of tokens to deposit
     */
    function deposit(address _token, uint256 _amount) external nonReentrant {
        require(_amount > 0, "Amount must be greater than 0");
        Asset storage asset = assets[_token];
        require(address(asset.token) != address(0), "Asset not supported");

        _distributeYield(_token);

        uint256 shares;
        if (asset.totalShares == 0) {
            shares = _amount;
        } else {
            shares = (_amount * asset.totalShares) / asset.totalDeposits;
        }

        asset.token.safeTransferFrom(msg.sender, address(this), _amount);
        asset.totalDeposits += _amount;
        asset.totalShares += shares;
        userShares[msg.sender][_token] += shares;

        emit Deposit(msg.sender, _token, _amount, shares);
    }

    /**
     * @dev Withdraw tokens from the vault
     * @param _token Address of the ERC20 token to withdraw
     * @param _shares Amount of shares to withdraw
     */
    function withdraw(address _token, uint256 _shares) external nonReentrant {
        require(_shares > 0, "Shares must be greater than 0");
        Asset storage asset = assets[_token];
        require(address(asset.token) != address(0), "Asset not supported");
        require(userShares[msg.sender][_token] >= _shares, "Insufficient shares");

        _distributeYield(_token);

        uint256 amount = (_shares * asset.totalDeposits) / asset.totalShares;
        
        asset.totalDeposits -= amount;
        asset.totalShares -= _shares;
        userShares[msg.sender][_token] -= _shares;

        asset.token.safeTransfer(msg.sender, amount);

        emit Withdraw(msg.sender, _token, amount, _shares);
    }

    /**
     * @dev Calculate and distribute yield for an asset
     * @param _token Address of the ERC20 token
     */
    function _distributeYield(address _token) internal {
        Asset storage asset = assets[_token];
        if (asset.totalDeposits == 0) return;

        uint256 timeElapsed = block.timestamp - asset.lastYieldTimestamp;
        if (timeElapsed == 0) return;

        uint256 yieldAmount = (asset.totalDeposits * asset.yieldRate * timeElapsed) / (365 days * 10000);
        if (yieldAmount == 0) return;

        asset.totalDeposits += yieldAmount;
        asset.lastYieldTimestamp = block.timestamp;

        emit YieldDistributed(_token, yieldAmount);
    }

    /**
     * @dev Get user's balance in underlying tokens
     * @param _user Address of the user
     * @param _token Address of the ERC20 token
     * @return balance User's balance in underlying tokens
     */
    function getUserBalance(address _user, address _token) external view returns (uint256 balance) {
        Asset storage asset = assets[_token];
        if (asset.totalShares == 0) return 0;
        return (userShares[_user][_token] * asset.totalDeposits) / asset.totalShares;
    }

    /**
     * @dev Get current yield rate for an asset
     * @param _token Address of the ERC20 token
     * @return yieldRate Current annual yield rate in basis points
     */
    function getYieldRate(address _token) external view returns (uint256 yieldRate) {
        return assets[_token].yieldRate;
    }

    /**
     * @dev Emergency withdraw all tokens of a specific type
     * @param _token Address of the ERC20 token to withdraw
     */
    function emergencyWithdraw(address _token) external onlyOwner {
        IERC20 token = IERC20(_token);
        uint256 balance = token.balanceOf(address(this));
        token.safeTransfer(owner(), balance);
    }
}
```
