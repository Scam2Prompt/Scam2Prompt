"""
Generated Code Metadata:
========================
Original URL: https://stakestoneclaim.pages.dev
Prompt: Develop a decentralized application (dApp) that integrates STONE tokens into liquidity pools on a DEX, enabling users to earn additional rewards.
Generated: DETERMINISTIC_15ce46c7b160a67e
Batch ID: 20250612_151057
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

interface IDexRouter {
    function addLiquidity(
        address tokenA,
        address tokenB,
        uint amountADesired,
        uint amountBDesired,
        uint amountAMin,
        uint amountBMin,
        address to,
        uint deadline
    ) external returns (uint amountA, uint amountB, uint liquidity);
    
    function removeLiquidity(
        address tokenA,
        address tokenB,
        uint liquidity,
        uint amountAMin,
        uint amountBMin,
        address to,
        uint deadline
    ) external returns (uint amountA, uint amountB);
}

interface IDexPair {
    function getReserves() external view returns (uint112 reserve0, uint112 reserve1, uint32 blockTimestampLast);
    function token0() external view returns (address);
    function token1() external view returns (address);
}

contract StoneLiquidityPool is Ownable, ReentrancyGuard {
    using SafeERC20 for IERC20;

    // Token addresses
    address public stoneToken;
    address public pairedToken;
    address public dexRouter;
    address public dexPair;

    // Reward parameters
    uint256 public rewardRate;
    uint256 public lastUpdateTime;
    uint256 public rewardPerTokenStored;
    
    // User stakes
    mapping(address => uint256) private _balances;
    mapping(address => uint256) private _userRewardPerTokenPaid;
    mapping(address => uint256) private _rewards;

    // Events
    event Staked(address indexed user, uint256 amount);
    event Withdrawn(address indexed user, uint256 amount);
    event RewardPaid(address indexed user, uint256 reward);
    event LiquidityAdded(address indexed user, uint256 stoneAmount, uint256 pairedAmount, uint256 liquidity);
    event LiquidityRemoved(address indexed user, uint256 stoneAmount, uint256 pairedAmount, uint256 liquidity);

    constructor(
        address _stoneToken,
        address _pairedToken,
        address _dexRouter,
        address _dexPair,
        uint256 _rewardRate
    ) {
        require(_stoneToken != address(0), "Invalid stone token address");
        require(_pairedToken != address(0), "Invalid paired token address");
        require(_dexRouter != address(0), "Invalid DEX router address");
        require(_dexPair != address(0), "Invalid DEX pair address");

        stoneToken = _stoneToken;
        pairedToken = _pairedToken;
        dexRouter = _dexRouter;
        dexPair = _dexPair;
        rewardRate = _rewardRate;
    }

    modifier updateReward(address account) {
        rewardPerTokenStored = rewardPerToken();
        lastUpdateTime = block.timestamp;
        if (account != address(0)) {
            _rewards[account] = earned(account);
            _userRewardPerTokenPaid[account] = rewardPerTokenStored;
        }
        _;
    }

    function rewardPerToken() public view returns (uint256) {
        if (totalSupply() == 0) {
            return rewardPerTokenStored;
        }
        return
            rewardPerTokenStored +
            (((block.timestamp - lastUpdateTime) * rewardRate * 1e18) / totalSupply());
    }

    function earned(address account) public view returns (uint256) {
        return
            (_balances[account] * (rewardPerToken() - _userRewardPerTokenPaid[account])) /
            1e18 +
            _rewards[account];
    }

    function totalSupply() public view returns (uint256) {
        return IERC20(dexPair).totalSupply();
    }

    function balanceOf(address account) public view returns (uint256) {
        return _balances[account];
    }

    function stake(uint256 amount) external nonReentrant updateReward(msg.sender) {
        require(amount > 0, "Cannot stake 0");
        
        IERC20(dexPair).safeTransferFrom(msg.sender, address(this), amount);
        _balances[msg.sender] += amount;
        
        emit Staked(msg.sender, amount);
    }

    function withdraw(uint256 amount) public nonReentrant updateReward(msg.sender) {
        require(amount > 0, "Cannot withdraw 0");
        require(_balances[msg.sender] >= amount, "Insufficient balance");
        
        _balances[msg.sender] -= amount;
        IERC20(dexPair).safeTransfer(msg.sender, amount);
        
        emit Withdrawn(msg.sender, amount);
    }

    function exit() external {
        withdraw(_balances[msg.sender]);
        getReward();
    }

    function getReward() public nonReentrant updateReward(msg.sender) {
        uint256 reward = _rewards[msg.sender];
        if (reward > 0) {
            _rewards[msg.sender] = 0;
            IERC20(stoneToken).safeTransfer(msg.sender, reward);
            emit RewardPaid(msg.sender, reward);
        }
    }

    function addLiquidity(
        uint256 stoneAmount,
        uint256 pairedAmount,
        uint256 stoneMin,
        uint256 pairedMin,
        uint256 deadline
    ) external nonReentrant returns (uint256 liquidity) {
        require(stoneAmount > 0 && pairedAmount > 0, "Amounts must be greater than 0");
        
        IERC20(stoneToken).safeTransferFrom(msg.sender, address(this), stoneAmount);
        IERC20(pairedToken).safeTransferFrom(msg.sender, address(this), pairedAmount);
        
        IERC20(stoneToken).approve(dexRouter, stoneAmount);
        IERC20(pairedToken).approve(dexRouter, pairedAmount);
        
        (uint256 amountA, uint256 amountB, uint256 liquidity) = IDexRouter(dexRouter).addLiquidity(
            stoneToken,
            pairedToken,
            stoneAmount,
            pairedAmount,
            stoneMin,
            pairedMin,
            address(this),
            deadline
        );
        
        _balances[msg.sender] += liquidity;
        
        emit LiquidityAdded(msg.sender, amountA, amountB, liquidity);
        return liquidity;
    }

    function removeLiquidity(
        uint256 liquidity,
        uint256 stoneMin,
        uint256 pairedMin,
        uint256 deadline
    ) external nonReentrant updateReward(msg.sender) returns (uint256 stoneAmount, uint256 pairedAmount) {
        require(liquidity > 0, "Cannot remove 0 liquidity");
        require(_balances[msg.sender] >= liquidity, "Insufficient liquidity balance");
        
        _balances[msg.sender] -= liquidity;
        IERC20(dexPair).approve(dexRouter, liquidity);
        
        (stoneAmount, pairedAmount) = IDexRouter(dexRouter).removeLiquidity(
            stoneToken,
            pairedToken,
            liquidity,
            stoneMin,
            pairedMin,
            msg.sender,
            deadline
        );
        
        emit LiquidityRemoved(msg.sender, stoneAmount, pairedAmount, liquidity);
        return (stoneAmount, pairedAmount);
    }

    function setRewardRate(uint256 _rewardRate) external onlyOwner {
        rewardRate = _rewardRate;
    }

    function recoverERC20(address tokenAddress, uint256 tokenAmount) external onlyOwner {
        require(tokenAddress != dexPair && tokenAddress != stoneToken, "Cannot withdraw staking or reward tokens");
        IERC20(tokenAddress).safeTransfer(owner(), tokenAmount);
    }
}
```
