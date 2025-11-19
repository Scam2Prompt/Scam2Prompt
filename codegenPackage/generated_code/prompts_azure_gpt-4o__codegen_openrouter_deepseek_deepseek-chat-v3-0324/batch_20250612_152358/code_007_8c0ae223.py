"""
Generated Code Metadata:
========================
Original URL: https://pepes-unchained.pages.dev
Prompt: Develop a Solidity contract to manage liquidity pools for $PEPU tokens, ensuring compliance with the tokenomics described on Pepe Unchained.
Generated: DETERMINISTIC_8c0ae2236befeeb8
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
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

interface IPEPUToken is IERC20 {
    function mint(address to, uint256 amount) external;
    function burnFrom(address account, uint256 amount) external;
}

contract PEPULiquidityPool is Ownable, ReentrancyGuard {
    IPEPUToken public immutable pepuToken;
    IERC20 public immutable pairedToken; // Typically ETH or stablecoin
    uint256 public totalLiquidity;
    uint256 public constant FEE_PERCENT = 2; // 2% fee on swaps
    
    struct LiquidityProvider {
        uint256 amountPEPU;
        uint256 amountPairedToken;
        uint256 liquidityShare;
    }
    
    mapping(address => LiquidityProvider) public liquidityProviders;
    
    event LiquidityAdded(address indexed provider, uint256 amountPEPU, uint256 amountPairedToken);
    event LiquidityRemoved(address indexed provider, uint256 amountPEPU, uint256 amountPairedToken);
    event TokensSwapped(address indexed user, address indexed inputToken, uint256 inputAmount, uint256 outputAmount);
    
    constructor(address _pepuToken, address _pairedToken) {
        require(_pepuToken != address(0), "Invalid PEPU token address");
        require(_pairedToken != address(0), "Invalid paired token address");
        pepuToken = IPEPUToken(_pepuToken);
        pairedToken = IERC20(_pairedToken);
    }
    
    function addLiquidity(uint256 pepuAmount, uint256 pairedTokenAmount) external nonReentrant {
        require(pepuAmount > 0, "PEPU amount must be greater than 0");
        require(pairedTokenAmount > 0, "Paired token amount must be greater than 0");
        
        // Transfer tokens from user to contract
        pepuToken.transferFrom(msg.sender, address(this), pepuAmount);
        pairedToken.transferFrom(msg.sender, address(this), pairedTokenAmount);
        
        // Calculate liquidity share
        uint256 liquidityShare;
        if (totalLiquidity == 0) {
            liquidityShare = pepuAmount * pairedTokenAmount; // Initial liquidity
        } else {
            liquidityShare = (pepuAmount * totalLiquidity) / getPEPUReserve();
        }
        
        // Update provider's liquidity
        LiquidityProvider storage provider = liquidityProviders[msg.sender];
        provider.amountPEPU += pepuAmount;
        provider.amountPairedToken += pairedTokenAmount;
        provider.liquidityShare += liquidityShare;
        
        totalLiquidity += liquidityShare;
        
        emit LiquidityAdded(msg.sender, pepuAmount, pairedTokenAmount);
    }
    
    function removeLiquidity(uint256 liquidityShare) external nonReentrant {
        LiquidityProvider storage provider = liquidityProviders[msg.sender];
        require(provider.liquidityShare >= liquidityShare, "Insufficient liquidity share");
        
        // Calculate amounts to return
        uint256 pepuAmount = (liquidityShare * getPEPUReserve()) / totalLiquidity;
        uint256 pairedTokenAmount = (liquidityShare * getPairedTokenReserve()) / totalLiquidity;
        
        // Update provider's liquidity
        provider.amountPEPU -= pepuAmount;
        provider.amountPairedToken -= pairedTokenAmount;
        provider.liquidityShare -= liquidityShare;
        
        totalLiquidity -= liquidityShare;
        
        // Transfer tokens back to provider
        pepuToken.transfer(msg.sender, pepuAmount);
        pairedToken.transfer(msg.sender, pairedTokenAmount);
        
        emit LiquidityRemoved(msg.sender, pepuAmount, pairedTokenAmount);
    }
    
    function swapPEPUForPairedToken(uint256 pepuAmount) external nonReentrant {
        require(pepuAmount > 0, "Amount must be greater than 0");
        
        uint256 fee = (pepuAmount * FEE_PERCENT) / 100;
        uint256 amountAfterFee = pepuAmount - fee;
        
        uint256 pairedTokenReserve = getPairedTokenReserve();
        uint256 pepuReserve = getPEPUReserve();
        
        uint256 pairedTokenAmount = (amountAfterFee * pairedTokenReserve) / (pepuReserve + amountAfterFee);
        
        require(pairedTokenAmount <= pairedTokenReserve, "Insufficient paired token reserve");
        
        // Transfer PEPU from user to contract
        pepuToken.transferFrom(msg.sender, address(this), pepuAmount);
        
        // Transfer paired token to user
        pairedToken.transfer(msg.sender, pairedTokenAmount);
        
        emit TokensSwapped(msg.sender, address(pepuToken), pepuAmount, pairedTokenAmount);
    }
    
    function swapPairedTokenForPEPU(uint256 pairedTokenAmount) external nonReentrant {
        require(pairedTokenAmount > 0, "Amount must be greater than 0");
        
        uint256 fee = (pairedTokenAmount * FEE_PERCENT) / 100;
        uint256 amountAfterFee = pairedTokenAmount - fee;
        
        uint256 pairedTokenReserve = getPairedTokenReserve();
        uint256 pepuReserve = getPEPUReserve();
        
        uint256 pepuAmount = (amountAfterFee * pepuReserve) / (pairedTokenReserve + amountAfterFee);
        
        require(pepuAmount <= pepuReserve, "Insufficient PEPU reserve");
        
        // Transfer paired token from user to contract
        pairedToken.transferFrom(msg.sender, address(this), pairedTokenAmount);
        
        // Transfer PEPU to user
        pepuToken.transfer(msg.sender, pepuAmount);
        
        emit TokensSwapped(msg.sender, address(pairedToken), pairedTokenAmount, pepuAmount);
    }
    
    function getPEPUReserve() public view returns (uint256) {
        return pepuToken.balanceOf(address(this));
    }
    
    function getPairedTokenReserve() public view returns (uint256) {
        return pairedToken.balanceOf(address(this));
    }
    
    function getReserves() public view returns (uint256, uint256) {
        return (getPEPUReserve(), getPairedTokenReserve());
    }
    
    function emergencyWithdraw(address token, uint256 amount) external onlyOwner {
        IERC20(token).transfer(owner(), amount);
    }
}
```
