"""
Generated Code Metadata:
========================
Original URL: https://claims-catcoin.pages.dev
Prompt: Design a community-driven ecosystem for $CAT token, including integrations with other cryptocurrencies and decentralized applications.
Generated: DETERMINISTIC_ede87e0ffb8736e4
Batch ID: 20250622_210231
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

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/token/ERC20/extensions/ERC20Burnable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/Pausable.sol";
import "@openzeppelin/contracts/token/ERC20/utils/SafeERC20.sol";

interface IDEXRouter {
    function factory() external pure returns (address);
    function WETH() external pure returns (address);
    function addLiquidityETH(
        address token,
        uint amountTokenDesired,
        uint amountTokenMin,
        uint amountETHMin,
        address to,
        uint deadline
    ) external payable returns (uint amountToken, uint amountETH, uint liquidity);
    function swapExactTokensForETHSupportingFeeOnTransferTokens(
        uint amountIn,
        uint amountOutMin,
        address[] calldata path,
        address to,
        uint deadline
    ) external;
}

contract CATToken is ERC20, ERC20Burnable, Ownable, Pausable {
    using SafeERC20 for IERC20;

    uint256 public constant MAX_SUPPLY = 1_000_000_000 * 10**18; // 1B tokens
    uint256 public constant COMMUNITY_REWARD_PERCENT = 10; // 10% for community rewards
    uint256 public constant LIQUIDITY_POOL_PERCENT = 5; // 5% for liquidity pool
    uint256 public constant TEAM_PERCENT = 5; // 5% for team
    
    address public dexRouterAddress;
    address public liquidityPoolAddress;
    address public communityRewardAddress;
    address public teamAddress;
    
    mapping(address => bool) public whitelistedDApps;
    mapping(address => bool) public whitelistedTokens;
    
    event DAppWhitelisted(address indexed dapp, bool whitelisted);
    event TokenWhitelisted(address indexed token, bool whitelisted);
    event LiquidityAdded(uint256 tokenAmount, uint256 ethAmount);
    event CommunityRewardDistributed(address indexed recipient, uint256 amount);
    event CrossChainSwap(address indexed from, address indexed toToken, uint256 amount);

    constructor(
        address _dexRouterAddress,
        address _liquidityPoolAddress,
        address _communityRewardAddress,
        address _teamAddress
    ) ERC20("Community CAT Token", "CAT") {
        require(_dexRouterAddress != address(0), "Invalid DEX router address");
        require(_liquidityPoolAddress != address(0), "Invalid liquidity pool address");
        require(_communityRewardAddress != address(0), "Invalid community reward address");
        require(_teamAddress != address(0), "Invalid team address");
        
        dexRouterAddress = _dexRouterAddress;
        liquidityPoolAddress = _liquidityPoolAddress;
        communityRewardAddress = _communityRewardAddress;
        teamAddress = _teamAddress;
        
        // Initial distribution
        uint256 communityReward = (MAX_SUPPLY * COMMUNITY_REWARD_PERCENT) / 100;
        uint256 liquidityPool = (MAX_SUPPLY * LIQUIDITY_POOL_PERCENT) / 100;
        uint256 teamAllocation = (MAX_SUPPLY * TEAM_PERCENT) / 100;
        
        _mint(communityRewardAddress, communityReward);
        _mint(liquidityPoolAddress, liquidityPool);
        _mint(teamAddress, teamAllocation);
        _mint(msg.sender, MAX_SUPPLY - communityReward - liquidityPool - teamAllocation);
    }

    function pause() public onlyOwner {
        _pause();
    }

    function unpause() public onlyOwner {
        _unpause();
    }

    function whitelistDApp(address _dapp, bool _whitelisted) external onlyOwner {
        whitelistedDApps[_dapp] = _whitelisted;
        emit DAppWhitelisted(_dapp, _whitelisted);
    }

    function whitelistToken(address _token, bool _whitelisted) external onlyOwner {
        whitelistedTokens[_token] = _whitelisted;
        emit TokenWhitelisted(_token, _whitelisted);
    }

    function addLiquidity(uint256 tokenAmount) external payable onlyOwner {
        require(tokenAmount > 0, "Amount must be greater than 0");
        require(balanceOf(msg.sender) >= tokenAmount, "Insufficient balance");
        
        _approve(msg.sender, address(this), tokenAmount);
        IERC20(address(this)).safeTransferFrom(msg.sender, address(this), tokenAmount);
        
        _approve(address(this), dexRouterAddress, tokenAmount);
        
        IDEXRouter router = IDEXRouter(dexRouterAddress);
        router.addLiquidityETH{value: msg.value}(
            address(this),
            tokenAmount,
            0,
            0,
            liquidityPoolAddress,
            block.timestamp + 300
        );
        
        emit LiquidityAdded(tokenAmount, msg.value);
    }

    function distributeCommunityRewards(address[] calldata recipients, uint256[] calldata amounts) external {
        require(msg.sender == communityRewardAddress, "Only community reward address can distribute");
        require(recipients.length == amounts.length, "Arrays length mismatch");
        
        for (uint256 i = 0; i < recipients.length; i++) {
            _transfer(communityRewardAddress, recipients[i], amounts[i]);
            emit CommunityRewardDistributed(recipients[i], amounts[i]);
        }
    }

    function crossChainSwap(address toToken, uint256 amount) external {
        require(whitelistedTokens[toToken], "Token not whitelisted");
        require(balanceOf(msg.sender) >= amount, "Insufficient balance");
        
        _burn(msg.sender, amount);
        emit CrossChainSwap(msg.sender, toToken, amount);
    }

    function _beforeTokenTransfer(address from, address to, uint256 amount) internal override whenNotPaused {
        super._beforeTokenTransfer(from, to, amount);
    }
}

interface IBridge {
    function swap(address fromToken, address toToken, uint256 amount) external;
}

contract CATBridge is Ownable {
    using SafeERC20 for IERC20;
    
    mapping(address => bool) public supportedTokens;
    mapping(address => uint256) public fees; // Fee in basis points (1 = 0.01%)
    
    event TokenSupported(address indexed token, bool supported);
    event FeeUpdated(address indexed token, uint256 fee);
    event BridgeSwap(address indexed user, address fromToken, address toToken, uint256 amount, uint256 fee);

    constructor() {
        // Initialize with default fees (0.1%)
        fees[address(0)] = 10; // ETH/BNB/etc
    }

    function supportToken(address token, bool supported) external onlyOwner {
        supportedTokens[token] = supported;
        emit TokenSupported(token, supported);
    }

    function setFee(address token, uint256 feeBasisPoints) external onlyOwner {
        fees[token] = feeBasisPoints;
        emit FeeUpdated(token, feeBasisPoints);
    }

    function swap(address fromToken, address toToken, uint256 amount) external payable {
        require(supportedTokens[fromToken] && supportedTokens[toToken], "Tokens not supported");
        
        uint256 fee = (amount * (fees[fromToken] > 0 ? fees[fromToken] : fees[address(0)])) / 10000;
        uint256 amountAfterFee = amount - fee;
        
        if (fromToken == address(0)) {
            require(msg.value == amount, "Incorrect ETH amount");
            // Transfer fee to owner
            payable(owner()).transfer(fee);
        } else {
            IERC20(fromToken).safeTransferFrom(msg.sender, address(this), amount);
            // Transfer fee to owner
            IERC20(fromToken).safeTransfer(owner(), fee);
        }
        
        emit BridgeSwap(msg.sender, fromToken, toToken, amountAfterFee, fee);
    }
}

contract CATStaking is Ownable {
    using SafeERC20 for IERC20;
    
    struct Stake {
        uint256 amount;
        uint256 stakedAt;
        uint256 lastClaimed;
    }
    
    IERC20 public catToken;
    uint256 public rewardRate = 10; // 10% APY
    uint256 public minStakeDuration = 30 days;
    
    mapping(address => Stake) public stakes;
    
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 amount);

    constructor(address _catToken) {
        catToken = IERC20(_catToken);
    }

    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        
        Stake storage userStake = stakes[msg.sender];
        if (userStake.amount >
