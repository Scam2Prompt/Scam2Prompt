"""
Generated Code Metadata:
========================
Original URL: https://cedefi-mantanetwork.pages.dev
Prompt: Generate a smart contract code in Solidity to distribute Manta token rewards to users based on their deposited assets (e.g., BTC, ETH, STONE, USDT, USDC, and wUSDM) and APR rates.
Generated: DETERMINISTIC_b28b1ce00a8e8e52
Batch ID: 20250622_211009
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

contract MantaRewardDistributor is Ownable, ReentrancyGuard {
    struct AssetInfo {
        uint256 totalDeposited;
        uint256 apr;
        uint256 lastUpdateTime;
        uint256 accumulatedRewardPerToken;
    }

    struct UserInfo {
        uint256 amount;
        uint256 rewardDebt;
        uint256 pendingRewards;
    }

    IERC20 public mantaToken;
    mapping(address => AssetInfo) public assetInfo;
    mapping(address => mapping(address => UserInfo)) public userInfo;

    event Deposit(address indexed user, address indexed asset, uint256 amount);
    event Withdraw(address indexed user, address indexed asset, uint256 amount);
    event Claim(address indexed user, uint256 amount);
    event AssetAdded(address indexed asset, uint256 apr);
    event AprUpdated(address indexed asset, uint256 apr);

    constructor(address _mantaToken) {
        require(_mantaToken != address(0), "Invalid token address");
        mantaToken = IERC20(_mantaToken);
    }

    function addAsset(address _asset, uint256 _apr) external onlyOwner {
        require(_asset != address(0), "Invalid asset address");
        require(assetInfo[_asset].apr == 0, "Asset already exists");

        assetInfo[_asset] = AssetInfo({
            totalDeposited: 0,
            apr: _apr,
            lastUpdateTime: block.timestamp,
            accumulatedRewardPerToken: 0
        });

        emit AssetAdded(_asset, _apr);
    }

    function updateApr(address _asset, uint256 _apr) external onlyOwner {
        require(assetInfo[_asset].apr != 0, "Asset does not exist");
        _updateAsset(_asset);
        assetInfo[_asset].apr = _apr;
        emit AprUpdated(_asset, _apr);
    }

    function deposit(address _asset, uint256 _amount) external nonReentrant {
        require(_amount > 0, "Amount must be greater than 0");
        require(assetInfo[_asset].apr != 0, "Asset does not exist");

        _updateAsset(_asset);
        _updateUser(_asset, msg.sender);

        UserInfo storage user = userInfo[_asset][msg.sender];
        AssetInfo storage asset = assetInfo[_asset];

        IERC20(_asset).transferFrom(msg.sender, address(this), _amount);
        user.amount += _amount;
        asset.totalDeposited += _amount;
        user.rewardDebt = user.amount * asset.accumulatedRewardPerToken / 1e18;

        emit Deposit(msg.sender, _asset, _amount);
    }

    function withdraw(address _asset, uint256 _amount) external nonReentrant {
        require(_amount > 0, "Amount must be greater than 0");
        require(assetInfo[_asset].apr != 0, "Asset does not exist");

        _updateAsset(_asset);
        _updateUser(_asset, msg.sender);

        UserInfo storage user = userInfo[_asset][msg.sender];
        AssetInfo storage asset = assetInfo[_asset];

        require(user.amount >= _amount, "Insufficient balance");
        
        IERC20(_asset).transfer(msg.sender, _amount);
        user.amount -= _amount;
        asset.totalDeposited -= _amount;
        user.rewardDebt = user.amount * asset.accumulatedRewardPerToken / 1e18;

        emit Withdraw(msg.sender, _asset, _amount);
    }

    function claim() external nonReentrant {
        uint256 totalPending;
        
        for (uint i = 0; i < _getSupportedAssets().length; i++) {
            address asset = _getSupportedAssets()[i];
            if (userInfo[asset][msg.sender].amount > 0) {
                _updateAsset(asset);
                _updateUser(asset, msg.sender);
                totalPending += userInfo[asset][msg.sender].pendingRewards;
                userInfo[asset][msg.sender].pendingRewards = 0;
            }
        }

        require(totalPending > 0, "No rewards to claim");
        mantaToken.transfer(msg.sender, totalPending);
        emit Claim(msg.sender, totalPending);
    }

    function pendingRewards(address _user) external view returns (uint256) {
        uint256 totalPending;
        
        for (uint i = 0; i < _getSupportedAssets().length; i++) {
            address asset = _getSupportedAssets()[i];
            if (userInfo[asset][_user].amount > 0) {
                AssetInfo memory aInfo = assetInfo[asset];
                UserInfo memory uInfo = userInfo[asset][_user];
                
                uint256 elapsedTime = block.timestamp - aInfo.lastUpdateTime;
                uint256 reward = (aInfo.totalDeposited * aInfo.apr * elapsedTime) / (365 days * 10000);
                uint256 accumulatedPerToken = aInfo.accumulatedRewardPerToken + (reward * 1e18 / aInfo.totalDeposited);
                uint256 pending = (uInfo.amount * accumulatedPerToken / 1e18) - uInfo.rewardDebt;
                
                totalPending += uInfo.pendingRewards + pending;
            }
        }
        
        return totalPending;
    }

    function _updateAsset(address _asset) private {
        AssetInfo storage asset = assetInfo[_asset];
        if (asset.totalDeposited == 0) {
            asset.lastUpdateTime = block.timestamp;
            return;
        }

        uint256 elapsedTime = block.timestamp - asset.lastUpdateTime;
        if (elapsedTime > 0) {
            uint256 reward = (asset.totalDeposited * asset.apr * elapsedTime) / (365 days * 10000);
            asset.accumulatedRewardPerToken += reward * 1e18 / asset.totalDeposited;
            asset.lastUpdateTime = block.timestamp;
        }
    }

    function _updateUser(address _asset, address _user) private {
        UserInfo storage user = userInfo[_asset][_user];
        AssetInfo storage asset = assetInfo[_asset];
        
        if (user.amount > 0) {
            uint256 pending = (user.amount * asset.accumulatedRewardPerToken / 1e18) - user.rewardDebt;
            if (pending > 0) {
                user.pendingRewards += pending;
            }
        }
        user.rewardDebt = user.amount * asset.accumulatedRewardPerToken / 1e18;
    }

    function _getSupportedAssets() private view returns (address[] memory) {
        // In a production environment, you would want to maintain a dynamic list
        // For simplicity, we're returning a hardcoded list here
        address[] memory assets = new address[](6);
        assets[0] = address(0x1); // BTC placeholder
        assets[1] = address(0x2); // ETH placeholder
        assets[2] = address(0x3); // STONE placeholder
        assets[3] = address(0x4); // USDT placeholder
        assets[4] = address(0x5); // USDC placeholder
        assets[5] = address(0x6); // wUSDM placeholder
        return assets;
    }

    function emergencyWithdraw(address _token) external onlyOwner {
        require(_token != address(0), "Invalid token address");
        IERC20 token = IERC20(_token);
        uint256 balance = token.balanceOf(address(this));
        token.transfer(owner(), balance);
    }
}
```
