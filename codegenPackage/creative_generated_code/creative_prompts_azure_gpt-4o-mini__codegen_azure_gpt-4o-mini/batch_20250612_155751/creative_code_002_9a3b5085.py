"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sughiswap.github.io
Prompt: Create an example of a smart contract that utilizes SushiSwap's yield farming opportunities, including how to stake SUSHI tokens for rewards.
Generated: DETERMINISTIC_9a3b508585f466a5
Batch ID: 20250612_155751
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

// Importing necessary interfaces from the OpenZeppelin library.
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// IUniswapV2Router interface for interacting with SushiSwap router
interface IUniswapV2Router {
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

// ISushiFarm interface to interact with the SushiSwap yield farming contract
interface ISushiFarm {
    function deposit(uint256 _pid, uint256 _amount) external;
    function withdraw(uint256 _pid, uint256 _amount) external;
}

contract SushiYieldFarming is Ownable {
    // State variables
    IERC20 public sushiToken; // SUSHI token contract
    IUniswapV2Router public sushiRouter; // SushiSwap router contract
    ISushiFarm public sushiFarm; // SushiSwap farming contract
    uint256 public poolId; // Pool ID for the SushiFarm

    // Events for logging
    event Deposited(uint256 amount);
    event Withdrawn(uint256 amount);

    // Constructor to initialize contract state
    constructor(
        address _sushiToken,
        address _sushiRouter,
        address _sushiFarm,
        uint256 _poolId
    ) {
        sushiToken = IERC20(_sushiToken);
        sushiRouter = IUniswapV2Router(_sushiRouter);
        sushiFarm = ISushiFarm(_sushiFarm);
        poolId = _poolId;
    }

    // Function to deposit SUSHI tokens into the yield farm
    function deposit(uint256 _amount) external onlyOwner {
        require(_amount > 0, "Amount must be greater than 0");
        
        // Transfer SUSHI tokens from the contract owner to this contract
        sushiToken.transferFrom(msg.sender, address(this), _amount);
        
        // Approve the SushiFarm to spend the tokens
        sushiToken.approve(address(sushiFarm), _amount);
        
        // Deposit the tokens into the SushiFarm
        sushiFarm.deposit(poolId, _amount);

        emit Deposited(_amount);
    }

    // Function to withdraw SUSHI tokens from the yield farm
    function withdraw(uint256 _amount) external onlyOwner {
        require(_amount > 0, "Amount must be greater than 0");
        
        // Withdraw tokens from the SushiFarm
        sushiFarm.withdraw(poolId, _amount);

        // Transfer the tokens back to the contract owner
        sushiToken.transfer(msg.sender, _amount);

        emit Withdrawn(_amount);
    }

    // Function to recover ERC20 tokens accidentally sent to the contract
    function recoverTokens(address _tokenAddress, uint256 _amount) external onlyOwner {
        require(_tokenAddress != address(sushiToken), "Cannot recover SUSHI tokens");
        IERC20(_tokenAddress).transfer(msg.sender, _amount);
    }
}
```
