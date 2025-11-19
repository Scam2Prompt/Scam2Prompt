"""
Generated Code Metadata:
========================
Original URL: https://bac-games.vercel.app
Prompt: Design a basic blockchain-based gaming ecosystem with a token listing process, including measures for providing liquidity and relinquishing control rights, inspired by BAC's approach.
Generated: DETERMINISTIC_220ddfd0d378bf4e
Batch ID: 20250622_204829
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";
import "@uniswap/v2-core/contracts/interfaces/IUniswapV2Factory.sol";
import "@uniswap/v2-periphery/contracts/interfaces/IUniswapV2Router02.sol";

contract GameToken is ERC20, Ownable {
    using SafeMath for uint256;
    
    IUniswapV2Router02 public uniswapV2Router;
    address public uniswapV2Pair;
    
    uint256 public constant TOTAL_SUPPLY = 1_000_000_000 * 10**18; // 1B tokens
    uint256 public constant LIQUIDITY_PERCENT = 50; // 50% of total supply for liquidity
    uint256 public constant TEAM_TOKENS_PERCENT = 20; // 20% for team (vested)
    uint256 public constant COMMUNITY_POOL_PERCENT = 30; // 30% for community rewards
    
    bool public liquidityAdded = false;
    uint256 public liquidityLockTime;
    uint256 public constant LOCK_TIME = 365 days; // 1 year lock
    
    mapping(address => bool) public whitelisted;
    mapping(address => uint256) public vestingSchedule;
    mapping(address => uint256) public claimedTokens;
    
    event LiquidityAdded(uint256 tokenAmount, uint256 ethAmount);
    event TokensClaimed(address indexed recipient, uint256 amount);
    event WhitelistUpdated(address indexed account, bool status);
    
    constructor() ERC20("GameToken", "GAME") {
        _mint(address(this), TOTAL_SUPPLY);
        
        // Initialize Uniswap V2 Router
        IUniswapV2Router02 _uniswapV2Router = IUniswapV2Router02(
            0x7a250d5630B4cF539739dF2C5dAcb4c659F2488D
        );
        uniswapV2Router = _uniswapV2Router;
        
        // Whitelist deployer initially
        whitelisted[msg.sender] = true;
    }
    
    function addLiquidity() external payable onlyOwner {
        require(!liquidityAdded, "Liquidity already added");
        require(msg.value > 0, "ETH amount must be greater than 0");
        
        uint256 liquidityAmount = TOTAL_SUPPLY.mul(LIQUIDITY_PERCENT).div(100);
        
        // Approve token transfer
        _approve(address(this), address(uniswapV2Router), liquidityAmount);
        
        // Add liquidity
        (uint256 tokenAmount, uint256 ethAmount, ) = uniswapV2Router.addLiquidityETH{value: msg.value}(
            address(this),
            liquidityAmount,
            0,
            0,
            address(this),
            block.timestamp + 15 minutes
        );
        
        // Create pair
        uniswapV2Pair = IUniswapV2Factory(uniswapV2Router.factory()).getPair(
            address(this),
            uniswapV2Router.WETH()
        );
        
        liquidityAdded = true;
        liquidityLockTime = block.timestamp + LOCK_TIME;
        
        emit LiquidityAdded(tokenAmount, ethAmount);
    }
    
    function distributeInitialTokens() external onlyOwner {
        require(liquidityAdded, "Liquidity must be added first");
        
        // Team tokens (vested)
        uint256 teamTokens = TOTAL_SUPPLY.mul(TEAM_TOKENS_PERCENT).div(100);
        vestingSchedule[owner()] = teamTokens;
        
        // Community pool
        uint256 communityTokens = TOTAL_SUPPLY.mul(COMMUNITY_POOL_PERCENT).div(100);
        _transfer(address(this), owner(), communityTokens);
    }
    
    function claimVestedTokens() external {
        require(vestingSchedule[msg.sender] > 0, "No tokens to claim");
        require(block.timestamp >= liquidityLockTime, "Tokens are still locked");
        
        uint256 claimable = vestingSchedule[msg.sender].sub(claimedTokens[msg.sender]);
        require(claimable > 0, "No tokens left to claim");
        
        claimedTokens[msg.sender] = claimedTokens[msg.sender].add(claimable);
        _transfer(address(this), msg.sender, claimable);
        
        emit TokensClaimed(msg.sender, claimable);
    }
    
    function updateWhitelist(address account, bool status) external onlyOwner {
        whitelisted[account] = status;
        emit WhitelistUpdated(account, status);
    }
    
    function renounceOwnership() public override onlyOwner {
        require(block.timestamp >= liquidityLockTime, "Cannot renounce before lock period ends");
        super.renounceOwnership();
    }
    
    function transfer(address recipient, uint256 amount) public override returns (bool) {
        // Only allow transfers after liquidity is added
        require(liquidityAdded || whitelisted[msg.sender], "Transfers not enabled yet");
        return super.transfer(recipient, amount);
    }
    
    function transferFrom(address sender, address recipient, uint256 amount) public override returns (bool) {
        // Only allow transfers after liquidity is added
        require(liquidityAdded || whitelisted[sender], "Transfers not enabled yet");
        return super.transferFrom(sender, recipient, amount);
    }
    
    // Emergency functions
    function emergencyWithdrawETH() external onlyOwner {
        require(block.timestamp < liquidityLockTime, "Lock period ended");
        payable(owner()).transfer(address(this).balance);
    }
    
    function emergencyWithdrawTokens(address tokenAddress) external onlyOwner {
        require(block.timestamp < liquidityLockTime, "Lock period ended");
        IERC20 token = IERC20(tokenAddress);
        token.transfer(owner(), token.balanceOf(address(this)));
    }
}
```
