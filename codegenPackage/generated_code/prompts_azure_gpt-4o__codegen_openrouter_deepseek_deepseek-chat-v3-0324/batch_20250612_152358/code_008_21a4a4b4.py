"""
Generated Code Metadata:
========================
Original URL: https://bafybeidfgwggshi5syqnklufswynx2u6rumuvgp4jl6n4lbqsolbeshdga.ipfs.dweb.link
Prompt: Write a Solidity function that allows users to deposit institutional-grade collateral to mint USD0, ensuring compliance with the protocol's risk policies.
Generated: DETERMINISTIC_21a4a4b453452746
Batch ID: 20250612_152358
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
import "@openzeppelin/contracts/security/Pausable.sol";

contract USD0Minter is Ownable, Pausable {
    IERC20 public immutable usd0Token;
    IERC20 public immutable collateralToken;
    
    uint256 public collateralRatio; // 1e18 = 100%
    uint256 public minCollateralAmount;
    uint256 public maxCollateralAmount;
    uint256 public totalCollateralDeposited;
    
    mapping(address => uint256) public userCollateral;
    mapping(address => bool) public whitelistedAssets;
    mapping(address => bool) public whitelistedUsers;
    
    event CollateralDeposited(address indexed user, uint256 amount);
    event USD0Minted(address indexed user, uint256 amount);
    event CollateralWithdrawn(address indexed user, uint256 amount);
    event USD0Burned(address indexed user, uint256 amount);
    event AssetWhitelisted(address indexed asset);
    event AssetDelisted(address indexed asset);
    event UserWhitelisted(address indexed user);
    event UserDelisted(address indexed user);
    
    constructor(
        address _usd0Token,
        address _collateralToken,
        uint256 _collateralRatio,
        uint256 _minCollateralAmount,
        uint256 _maxCollateralAmount
    ) {
        require(_usd0Token != address(0), "Invalid USD0 token address");
        require(_collateralToken != address(0), "Invalid collateral token address");
        require(_collateralRatio > 0, "Collateral ratio must be positive");
        
        usd0Token = IERC20(_usd0Token);
        collateralToken = IERC20(_collateralToken);
        collateralRatio = _collateralRatio;
        minCollateralAmount = _minCollateralAmount;
        maxCollateralAmount = _maxCollateralAmount;
        
        whitelistedAssets[_collateralToken] = true;
    }
    
    modifier onlyWhitelistedUser() {
        require(whitelistedUsers[msg.sender], "User not whitelisted");
        _;
    }
    
    modifier onlyWhitelistedAsset(address asset) {
        require(whitelistedAssets[asset], "Asset not whitelisted");
        _;
    }
    
    function depositAndMint(uint256 collateralAmount) external whenNotPaused onlyWhitelistedUser {
        require(collateralAmount >= minCollateralAmount, "Below minimum collateral");
        require(collateralAmount <= maxCollateralAmount, "Above maximum collateral");
        
        uint256 usd0ToMint = (collateralAmount * 1e18) / collateralRatio;
        require(usd0Token.balanceOf(address(this)) >= usd0ToMint, "Insufficient USD0 liquidity");
        
        // Transfer collateral from user
        require(
            collateralToken.transferFrom(msg.sender, address(this), collateralAmount),
            "Collateral transfer failed"
        );
        
        // Update state
        userCollateral[msg.sender] += collateralAmount;
        totalCollateralDeposited += collateralAmount;
        
        // Mint USD0 to user
        require(
            usd0Token.transfer(msg.sender, usd0ToMint),
            "USD0 transfer failed"
        );
        
        emit CollateralDeposited(msg.sender, collateralAmount);
        emit USD0Minted(msg.sender, usd0ToMint);
    }
    
    function burnAndWithdraw(uint256 usd0Amount) external whenNotPaused onlyWhitelistedUser {
        uint256 collateralToWithdraw = (usd0Amount * collateralRatio) / 1e18;
        
        require(
            userCollateral[msg.sender] >= collateralToWithdraw,
            "Insufficient collateral balance"
        );
        
        // Burn USD0 from user
        require(
            usd0Token.transferFrom(msg.sender, address(this), usd0Amount),
            "USD0 transfer failed"
        );
        
        // Transfer collateral back to user
        require(
            collateralToken.transfer(msg.sender, collateralToWithdraw),
            "Collateral transfer failed"
        );
        
        // Update state
        userCollateral[msg.sender] -= collateralToWithdraw;
        totalCollateralDeposited -= collateralToWithdraw;
        
        emit USD0Burned(msg.sender, usd0Amount);
        emit CollateralWithdrawn(msg.sender, collateralToWithdraw);
    }
    
    // Admin functions
    function whitelistAsset(address asset) external onlyOwner {
        whitelistedAssets[asset] = true;
        emit AssetWhitelisted(asset);
    }
    
    function delistAsset(address asset) external onlyOwner {
        whitelistedAssets[asset] = false;
        emit AssetDelisted(asset);
    }
    
    function whitelistUser(address user) external onlyOwner {
        whitelistedUsers[user] = true;
        emit UserWhitelisted(user);
    }
    
    function delistUser(address user) external onlyOwner {
        whitelistedUsers[user] = false;
        emit UserDelisted(user);
    }
    
    function setCollateralRatio(uint256 newRatio) external onlyOwner {
        require(newRatio > 0, "Collateral ratio must be positive");
        collateralRatio = newRatio;
    }
    
    function setMinCollateralAmount(uint256 newMin) external onlyOwner {
        minCollateralAmount = newMin;
    }
    
    function setMaxCollateralAmount(uint256 newMax) external onlyOwner {
        maxCollateralAmount = newMax;
    }
    
    function pause() external onlyOwner {
        _pause();
    }
    
    function unpause() external onlyOwner {
        _unpause();
    }
    
    function emergencyWithdraw(address token, uint256 amount) external onlyOwner {
        require(
            IERC20(token).transfer(owner(), amount),
            "Emergency withdrawal failed"
        );
    }
}
```
