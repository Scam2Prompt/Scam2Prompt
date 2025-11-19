"""
Generated Code Metadata:
========================
Original URL: https://bafybeidtnckzvkdfd4adyg7s3vhgnsxy3sxyvceyaty6bcbuxmmlfvut3a.ipfs.dweb.link
Prompt: Generate a smart contract code in Solidity that utilizes Pendle's AMM and vePENDLE staking mechanism.
Generated: DETERMINISTIC_204bb491670c49af
Batch ID: 20250622_205111
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
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

interface IPendleMarket {
    function swapExactTokensForTokens(
        uint256 amountIn,
        uint256 amountOutMin,
        address[] calldata path,
        address to,
        uint256 deadline
    ) external returns (uint256[] memory amounts);
    
    function getAmountsOut(uint256 amountIn, address[] calldata path) external view returns (uint256[] memory amounts);
}

interface IvePENDLE {
    function create_lock(uint256 _value, uint256 _unlock_time) external;
    function increase_amount(uint256 _value) external;
    function increase_unlock_time(uint256 _unlock_time) external;
    function withdraw() external;
    function balanceOf(address account) external view returns (uint256);
}

contract PendleAMMStaker is ReentrancyGuard {
    using SafeERC20 for IERC20;
    using SafeMath for uint256;
    
    address public immutable pendleToken;
    address public immutable vePendle;
    address public immutable pendleMarket;
    
    constructor(
        address _pendleToken,
        address _vePendle,
        address _pendleMarket
    ) {
        pendleToken = _pendleToken;
        vePendle = _vePendle;
        pendleMarket = _pendleMarket;
    }
    
    /**
     * @dev Swaps tokens via Pendle AMM and stakes the resulting PENDLE
     * @param amountIn Amount of input tokens to swap
     * @param amountOutMin Minimum amount of PENDLE to receive
     * @param path Swap path (must end with PENDLE token)
     * @param lockDuration Duration to lock PENDLE (in seconds)
     * @param deadline Transaction deadline
     */
    function swapAndStake(
        uint256 amountIn,
        uint256 amountOutMin,
        address[] calldata path,
        uint256 lockDuration,
        uint256 deadline
    ) external nonReentrant {
        require(path.length >= 2, "Invalid path");
        require(path[path.length - 1] == pendleToken, "Path must end with PENDLE");
        
        IERC20 inputToken = IERC20(path[0]);
        inputToken.safeTransferFrom(msg.sender, address(this), amountIn);
        inputToken.safeApprove(pendleMarket, amountIn);
        
        uint256[] memory amounts = IPendleMarket(pendleMarket).swapExactTokensForTokens(
            amountIn,
            amountOutMin,
            path,
            address(this),
            deadline
        );
        
        uint256 pendleAmount = amounts[amounts.length - 1];
        _stakePendle(pendleAmount, lockDuration);
    }
    
    /**
     * @dev Stakes PENDLE tokens into vePENDLE contract
     * @param amount Amount of PENDLE to stake
     * @param lockDuration Duration to lock PENDLE (in seconds)
     */
    function stakePendle(uint256 amount, uint256 lockDuration) external nonReentrant {
        IERC20(pendleToken).safeTransferFrom(msg.sender, address(this), amount);
        _stakePendle(amount, lockDuration);
    }
    
    function _stakePendle(uint256 amount, uint256 lockDuration) internal {
        IERC20(pendleToken).safeApprove(vePendle, amount);
        
        uint256 unlockTime = block.timestamp.add(lockDuration);
        
        if (IvePENDLE(vePendle).balanceOf(address(this)) == 0) {
            IvePENDLE(vePendle).create_lock(amount, unlockTime);
        } else {
            IvePENDLE(vePendle).increase_amount(amount);
            IvePENDLE(vePendle).increase_unlock_time(unlockTime);
        }
    }
    
    /**
     * @dev Withdraws staked PENDLE tokens after lock period expires
     */
    function withdraw() external nonReentrant {
        IvePENDLE(vePendle).withdraw();
        uint256 balance = IERC20(pendleToken).balanceOf(address(this));
        IERC20(pendleToken).safeTransfer(msg.sender, balance);
    }
    
    /**
     * @dev Estimates amount of PENDLE received from a swap
     * @param amountIn Amount of input tokens
     * @param path Swap path
     * @return Estimated amount of PENDLE received
     */
    function estimateSwap(
        uint256 amountIn,
        address[] calldata path
    ) external view returns (uint256) {
        require(path.length >= 2, "Invalid path");
        require(path[path.length - 1] == pendleToken, "Path must end with PENDLE");
        
        uint256[] memory amounts = IPendleMarket(pendleMarket).getAmountsOut(amountIn, path);
        return amounts[amounts.length - 1];
    }
    
    /**
     * @dev Gets current vePENDLE balance for this contract
     * @return Current vePENDLE balance
     */
    function getVePendleBalance() external view returns (uint256) {
        return IvePENDLE(vePendle).balanceOf(address(this));
    }
}
```
