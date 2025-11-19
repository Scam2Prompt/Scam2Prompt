"""
Generated Code Metadata:
========================
Original URL: https://hoststandart.ru
Prompt: Create a smart contract in Solidity that integrates with Belt Finance to automate reinvestment of earned tokens into liquidity pools.
Generated: DETERMINISTIC_3a81589629fafe2b
Batch ID: 20250612_155024
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
import "@openzeppelin/contracts/math/SafeMath.sol";
import "@openzeppelin/contracts/utils/Address.sol";

contract BeltFinanceReinvestor {
    using SafeMath for uint256;
    using Address for address;

    // Belt Finance LP Token
    IERC20 public beltLpToken;

    // Belt Finance Reward Token
    IERC20 public beltRewardToken;

    // Belt Finance Router
    address public beltRouter;

    // Reinvestment threshold
    uint256 public reinvestThreshold;

    // Mapping of users to their reinvestment status
    mapping(address => bool) public userReinvestmentStatus;

    // Event emitted when reinvestment occurs
    event Reinvest(address indexed user, uint256 amount);

    // Event emitted when reinvestment status is updated
    event UpdateReinvestmentStatus(address indexed user, bool status);

    /**
     * @param _beltLpToken Belt Finance LP Token address
     * @param _beltRewardToken Belt Finance Reward Token address
     * @param _beltRouter Belt Finance Router address
     * @param _reinvestThreshold Reinvestment threshold
     */
    constructor(
        address _beltLpToken,
        address _beltRewardToken,
        address _beltRouter,
        uint256 _reinvestThreshold
    ) public {
        require(_beltLpToken != address(0), "Belt LP Token address cannot be zero");
        require(_beltRewardToken != address(0), "Belt Reward Token address cannot be zero");
        require(_beltRouter != address(0), "Belt Router address cannot be zero");
        require(_reinvestThreshold > 0, "Reinvestment threshold must be greater than zero");

        beltLpToken = IERC20(_beltLpToken);
        beltRewardToken = IERC20(_beltRewardToken);
        beltRouter = _beltRouter;
        reinvestThreshold = _reinvestThreshold;
    }

    /**
     * @dev Update reinvestment status for a user
     * @param _user User address
     * @param _status Reinvestment status
     */
    function updateReinvestmentStatus(address _user, bool _status) public {
        require(msg.sender == _user, "Only the user can update their reinvestment status");

        userReinvestmentStatus[_user] = _status;
        emit UpdateReinvestmentStatus(_user, _status);
    }

    /**
     * @dev Reinvest earned tokens into liquidity pool
     */
    function reinvest() public {
        require(userReinvestmentStatus[msg.sender], "Reinvestment is not enabled for this user");

        uint256 rewardBalance = beltRewardToken.balanceOf(msg.sender);
        require(rewardBalance >= reinvestThreshold, "Reward balance is less than the reinvestment threshold");

        // Approve Belt Router to spend reward tokens
        beltRewardToken.approve(beltRouter, rewardBalance);

        // Call Belt Router to add liquidity
        // NOTE: This assumes the Belt Router has a function to add liquidity
        //       and that the function signature is (IERC20, IERC20, uint256)
        IRouter(beltRouter).addLiquidity(
            beltLpToken,
            beltRewardToken,
            rewardBalance
        );

        emit Reinvest(msg.sender, rewardBalance);
    }
}

// Interface for Belt Finance Router
interface IRouter {
    function addLiquidity(
        IERC20 _lpToken,
        IERC20 _rewardToken,
        uint256 _amount
    ) external;
}
```
