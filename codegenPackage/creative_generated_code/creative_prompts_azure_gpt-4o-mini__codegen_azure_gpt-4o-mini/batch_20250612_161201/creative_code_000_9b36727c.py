"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://flash-stake.pages.dev
Prompt: How can I implement a no-liquidation leverage strategy using Flashstake to lock GLP and earn a fixed APR?
Generated: DETERMINISTIC_9b36727c9b7300db
Batch ID: 20250612_161201
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

interface IFlashstake {
    function stake(uint256 amount, address receiver) external;
    function withdraw(uint256 amount) external;
}

contract NoLiquidationLeverageStrategy {
    using SafeMath for uint256;

    // Address of the Flashstake contract
    IFlashstake public flashstake;
    // Address of the GLP token
    IERC20 public glpToken;
    // User's staked balance
    mapping(address => uint256) public stakedBalances;
    
    // Event to emit when GLP is staked
    event Staked(address indexed user, uint256 amount);
    // Event to emit when GLP is withdrawn
    event Withdrawn(address indexed user, uint256 amount);

    /**
     * @dev Constructor to initialize the contract with Flashstake and GLP token addresses.
     * @param _flashstake Address of the Flashstake contract.
     * @param _glpToken Address of the GLP token.
     */
    constructor(address _flashstake, address _glpToken) {
        flashstake = IFlashstake(_flashstake);
        glpToken = IERC20(_glpToken);
    }

    /**
     * @dev Stake GLP tokens in Flashstake to earn fixed APR.
     * @param amount Amount of GLP tokens to stake.
     */
    function stakeGLP(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        require(glpToken.balanceOf(msg.sender) >= amount, "Insufficient GLP balance");

        // Transfer GLP tokens from the user to this contract
        glpToken.transferFrom(msg.sender, address(this), amount);
        // Stake GLP tokens in Flashstake
        flashstake.stake(amount, msg.sender);

        // Update staked balance
        stakedBalances[msg.sender] = stakedBalances[msg.sender].add(amount);
        
        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Withdraw staked GLP tokens from Flashstake.
     * @param amount Amount of GLP tokens to withdraw.
     */
    function withdrawGLP(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        require(stakedBalances[msg.sender] >= amount, "Insufficient staked balance");

        // Withdraw GLP tokens from Flashstake
        flashstake.withdraw(amount);
        // Transfer GLP tokens back to the user
        glpToken.transfer(msg.sender, amount);

        // Update staked balance
        stakedBalances[msg.sender] = stakedBalances[msg.sender].sub(amount);
        
        emit Withdrawn(msg.sender, amount);
    }

    /**
     * @dev Get the staked balance of a user.
     * @param user Address of the user.
     * @return The staked balance of the user in GLP tokens.
     */
    function getStakedBalance(address user) external view returns (uint256) {
        return stakedBalances[user];
    }
}
```
