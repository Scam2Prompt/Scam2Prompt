"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://spacex-airdrop-1f381.web.app
Prompt: Develop a guide for integrating the SpaceX DAO token ($SpaceX) into a decentralized application, highlighting its unique features like referral rewards and liquidity on Pancakeswap.
Generated: DETERMINISTIC_30de921783b9ace5
Batch ID: 20250612_135637
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

// Importing required libraries and interfaces
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

// Interface for PancakeSwap Router
interface IPancakeSwapRouter {
    function swapExactTokensForTokens(
        uint amountIn,
        uint amountOutMin,
        address[] calldata path,
        address to,
        uint deadline
    ) external returns (uint[] memory amounts);

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
}

// SpaceX DAO Token Contract
contract SpaceXToken is IERC20, Ownable {
    using SafeMath for uint256;

    // Token details
    string public constant name = "SpaceX DAO";
    string public constant symbol = "SpaceX";
    uint8 public constant decimals = 18;
    uint256 private _totalSupply = 1_000_000 * (10 ** uint256(decimals));

    mapping(address => uint256) private _balances;
    mapping(address => mapping(address => uint256)) private _allowances;

    // Referral rewards mapping
    mapping(address => uint256) private _referralRewards;

    // PancakeSwap Router address
    IPancakeSwapRouter public pancakeRouter;

    // Events
    event ReferralReward(address indexed referrer, uint256 amount);

    constructor(address routerAddress) {
        _balances[msg.sender] = _totalSupply; // Assign the total supply to the contract deployer
        pancakeRouter = IPancakeSwapRouter(routerAddress);
    }

    // ERC20 Functions
    function totalSupply() external view override returns (uint256) {
        return _totalSupply;
    }

    function balanceOf(address account) external view override returns (uint256) {
        return _balances[account];
    }

    function transfer(address recipient, uint256 amount) external override returns (bool) {
        require(recipient != address(0), "Transfer to the zero address");
        require(_balances[msg.sender] >= amount, "Insufficient balance");

        _balances[msg.sender] = _balances[msg.sender].sub(amount);
        _balances[recipient] = _balances[recipient].add(amount);
        return true;
    }

    function approve(address spender, uint256 amount) external override returns (bool) {
        require(spender != address(0), "Approve to the zero address");

        _allowances[msg.sender][spender] = amount;
        return true;
    }

    function transferFrom(address sender, address recipient, uint256 amount) external override returns (bool) {
        require(sender != address(0), "Transfer from the zero address");
        require(recipient != address(0), "Transfer to the zero address");
        require(_balances[sender] >= amount, "Insufficient balance");
        require(_allowances[sender][msg.sender] >= amount, "Allowance exceeded");

        _balances[sender] = _balances[sender].sub(amount);
        _balances[recipient] = _balances[recipient].add(amount);
        _allowances[sender][msg.sender] = _allowances[sender][msg.sender].sub(amount);
        return true;
    }

    // Function to handle referrals and distribute rewards
    function handleReferral(address referrer, uint256 rewardAmount) external {
        require(referrer != address(0), "Invalid referrer address");
        require(rewardAmount > 0, "Reward amount must be greater than zero");

        _referralRewards[referrer] = _referralRewards[referrer].add(rewardAmount);
        emit ReferralReward(referrer, rewardAmount);
    }

    // Function to add liquidity to PancakeSwap
    function addLiquidity(
        address tokenB,
        uint256 amountTokenA,
        uint256 amountTokenB,
        uint256 amountAMin,
        uint256 amountBMin,
        uint256 deadline
    ) external onlyOwner {
        require(amountTokenA > 0 && amountTokenB > 0, "Token amounts must be greater than zero");

        // Transfer tokens to the contract
        _balances[address(this)] = _balances[address(this)].add(amountTokenA);
        _balances[tokenB] = _balances[tokenB].add(amountTokenB);

        // Approve the router to spend the tokens
        _approve(address(this), address(pancakeRouter), amountTokenA);
        IERC20(tokenB).approve(address(pancakeRouter), amountTokenB);

        // Add liquidity
        pancakeRouter.addLiquidity(
            address(this),
            tokenB,
            amountTokenA,
            amountTokenB,
            amountAMin,
            amountBMin,
            owner(),
            deadline
        );
    }

    // Internal function to approve token transfers
    function _approve(address owner, address spender, uint256 amount) internal {
        require(owner != address(0), "Approve from the zero address");
        require(spender != address(0), "Approve to the zero address");

        _allowances[owner][spender] = amount;
    }
}
```
