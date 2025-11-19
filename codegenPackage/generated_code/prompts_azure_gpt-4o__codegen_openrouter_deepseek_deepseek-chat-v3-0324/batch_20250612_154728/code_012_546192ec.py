"""
Generated Code Metadata:
========================
Original URL: https://zkswapfinance.gitbook.io
Prompt: Generate code for implementing zkSwap Finance's Swap2Earn mechanism in a decentralized application, ensuring rewards are distributed to both traders and liquidity providers.
Generated: DETERMINISTIC_546192eca5af4d8e
Batch ID: 20250612_154728
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
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

contract zkSwapFinance is Ownable, ReentrancyGuard {
    using SafeMath for uint256;

    // Token contract addresses
    IERC20 public rewardToken;
    IERC20 public tokenA;
    IERC20 public tokenB;

    // Reward distribution parameters
    uint256 public traderRewardPercentage = 50; // 50% to traders
    uint256 public lpRewardPercentage = 50;    // 50% to LPs
    uint256 public totalRewardsDistributed;

    // Swap tracking
    struct SwapInfo {
        address trader;
        uint256 amountIn;
        uint256 amountOut;
        uint256 timestamp;
    }

    // Liquidity provider tracking
    struct LPInfo {
        address provider;
        uint256 liquidityAmount;
        uint256 lastUpdate;
    }

    // Mappings
    mapping(address => uint256) public traderRewards;
    mapping(address => uint256) public lpRewards;
    mapping(address => LPInfo) public liquidityProviders;
    SwapInfo[] public swapHistory;

    // Events
    event Swapped(
        address indexed trader,
        uint256 amountIn,
        uint256 amountOut,
        uint256 timestamp
    );
    event LiquidityAdded(
        address indexed provider,
        uint256 amount,
        uint256 timestamp
    );
    event LiquidityRemoved(
        address indexed provider,
        uint256 amount,
        uint256 timestamp
    );
    event RewardsDistributed(
        address indexed recipient,
        uint256 amount,
        bool isTrader
    );

    constructor(
        address _rewardToken,
        address _tokenA,
        address _tokenB
    ) {
        require(_rewardToken != address(0), "Invalid reward token address");
        require(_tokenA != address(0), "Invalid token A address");
        require(_tokenB != address(0), "Invalid token B address");

        rewardToken = IERC20(_rewardToken);
        tokenA = IERC20(_tokenA);
        tokenB = IERC20(_tokenB);
    }

    /**
     * @dev Execute a token swap
     * @param _amountIn Amount of input token
     * @param _amountOutMin Minimum amount of output token expected
     * @param _isTokenAtoB Direction of swap (true: A to B, false: B to A)
     */
    function swap(
        uint256 _amountIn,
        uint256 _amountOutMin,
        bool _isTokenAtoB
    ) external nonReentrant {
        require(_amountIn > 0, "Amount must be greater than 0");

        IERC20 inputToken = _isTokenAtoB ? tokenA : tokenB;
        IERC20 outputToken = _isTokenAtoB ? tokenB : tokenA;

        // Transfer input tokens from user
        require(
            inputToken.transferFrom(msg.sender, address(this), _amountIn),
            "Transfer failed"
        );

        // Calculate output amount (simplified for example)
        uint256 amountOut = calculateOutputAmount(_amountIn, _isTokenAtoB);
        require(amountOut >= _amountOutMin, "Insufficient output amount");

        // Transfer output tokens to user
        require(
            outputToken.transfer(msg.sender, amountOut),
            "Transfer failed"
        );

        // Record swap
        swapHistory.push(
            SwapInfo({
                trader: msg.sender,
                amountIn: _amountIn,
                amountOut: amountOut,
                timestamp: block.timestamp
            })
        );

        // Distribute rewards
        distributeRewards(msg.sender, _amountIn);

        emit Swapped(msg.sender, _amountIn, amountOut, block.timestamp);
    }

    /**
     * @dev Add liquidity to the pool
     * @param _amountA Amount of token A to add
     * @param _amountB Amount of token B to add
     */
    function addLiquidity(
        uint256 _amountA,
        uint256 _amountB
    ) external nonReentrant {
        require(_amountA > 0 && _amountB > 0, "Amounts must be greater than 0");

        // Transfer tokens from user
        require(
            tokenA.transferFrom(msg.sender, address(this), _amountA),
            "Token A transfer failed"
        );
        require(
            tokenB.transferFrom(msg.sender, address(this), _amountB),
            "Token B transfer failed"
        );

        // Update LP info
        if (liquidityProviders[msg.sender].provider == address(0)) {
            liquidityProviders[msg.sender] = LPInfo({
                provider: msg.sender,
                liquidityAmount: _amountA.add(_amountB),
                lastUpdate: block.timestamp
            });
        } else {
            liquidityProviders[msg.sender].liquidityAmount = liquidityProviders[
                msg.sender
            ].liquidityAmount.add(_amountA.add(_amountB));
            liquidityProviders[msg.sender].lastUpdate = block.timestamp;
        }

        emit LiquidityAdded(
            msg.sender,
            _amountA.add(_amountB),
            block.timestamp
        );
    }

    /**
     * @dev Remove liquidity from the pool
     * @param _amount Amount of liquidity to remove
     */
    function removeLiquidity(uint256 _amount) external nonReentrant {
        require(_amount > 0, "Amount must be greater than 0");
        LPInfo storage lpInfo = liquidityProviders[msg.sender];
        require(lpInfo.liquidityAmount >= _amount, "Insufficient liquidity");

        // Calculate proportional amounts of tokenA and tokenB
        uint256 totalLiquidity = tokenA.balanceOf(address(this)).add(
            tokenB.balanceOf(address(this))
        );
        uint256 amountA = _amount.mul(tokenA.balanceOf(address(this))).div(
            totalLiquidity
        );
        uint256 amountB = _amount.mul(tokenB.balanceOf(address(this))).div(
            totalLiquidity
        );

        // Transfer tokens back to user
        require(tokenA.transfer(msg.sender, amountA), "Token A transfer failed");
        require(tokenB.transfer(msg.sender, amountB), "Token B transfer failed");

        // Update LP info
        lpInfo.liquidityAmount = lpInfo.liquidityAmount.sub(_amount);
        lpInfo.lastUpdate = block.timestamp;

        emit LiquidityRemoved(msg.sender, _amount, block.timestamp);
    }

    /**
     * @dev Claim trader rewards
     */
    function claimTraderRewards() external nonReentrant {
        uint256 rewardAmount = traderRewards[msg.sender];
        require(rewardAmount > 0, "No rewards to claim");

        traderRewards[msg.sender] = 0;
        require(
            rewardToken.transfer(msg.sender, rewardAmount),
            "Reward transfer failed"
        );

        emit RewardsDistributed(msg.sender, rewardAmount, true);
    }

    /**
     * @dev Claim LP rewards
     */
    function claimLPRewards() external nonReentrant {
        uint256 rewardAmount = lpRewards[msg.sender];
        require(rewardAmount > 0, "No rewards to claim");

        lpRewards[msg.sender] = 0;
        require(
            rewardToken.transfer(msg.sender, rewardAmount),
            "Reward transfer failed"
        );

        emit RewardsDistributed(msg.sender, rewardAmount, false);
    }

    /**
     * @dev Distribute rewards to trader and LPs
     * @param _trader Address of the trader
     * @param _swapAmount Amount swapped
     */
    function distributeRewards(address _trader, uint256 _swapAmount) internal {
        // Calculate total rewards (simplified for example)
        uint256 totalReward = _swapAmount.div(100); // 1% of swap amount

        // Distribute to trader
        uint256 traderReward = totalReward.mul(traderRewardPercentage).div(100);
        traderRewards[_trader] = traderRewards[_trader].add(traderReward);

        // Distribute to LPs (proportional to their liquidity)
        uint256 lpReward = totalReward.mul(lpRewardPercentage).div(100);
        uint256 totalLiquidity = tokenA.balanceOf(address(this)).add(
            tokenB.balanceOf(address(this))
        );

        if (totalLiquidity > 0) {
            for (uint256 i = 0; i < swapHistory.length; i++) {
                address provider = swapHistory[i].trader;
                if (liquidityProviders[provider].liquidityAmount > 0) {
                    uint256 providerShare = liquidityProviders[provider]
                        .l
