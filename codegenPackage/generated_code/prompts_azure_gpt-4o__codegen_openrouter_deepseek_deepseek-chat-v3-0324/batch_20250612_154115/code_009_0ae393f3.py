"""
Generated Code Metadata:
========================
Original URL: https://xyzwthelly.com
Prompt: Create a Solidity contract that integrates with Valantis to enable liquid staking of nBTC via the stHYPE AMM.
Generated: DETERMINISTIC_0ae393f3266355ab
Batch ID: 20250612_154115
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

interface IValantis {
    function stake(uint256 amount) external;
    function unstake(uint256 amount) external;
    function getStakedBalance(address user) external view returns (uint256);
}

interface IstHYPEAMM {
    function addLiquidity(uint256 amountA, uint256 amountB) external returns (uint256 liquidity);
    function removeLiquidity(uint256 liquidity) external returns (uint256 amountA, uint256 amountB);
    function getReserves() external view returns (uint256 reserveA, uint256 reserveB);
}

contract nBTCLiquidStaking is Ownable, ReentrancyGuard {
    using SafeERC20 for IERC20;

    IERC20 public immutable nBTC;
    IERC20 public immutable stHYPE;
    IValantis public immutable valantis;
    IstHYPEAMM public immutable stHYPEAMM;

    mapping(address => uint256) public userLiquidity;
    mapping(address => uint256) public userStakedNBTC;

    event Staked(address indexed user, uint256 nBTCAmount, uint256 liquidity);
    event Unstaked(address indexed user, uint256 nBTCAmount, uint256 liquidity);
    event EmergencyWithdraw(address indexed user, uint256 nBTCAmount);

    constructor(
        address _nBTC,
        address _stHYPE,
        address _valantis,
        address _stHYPEAMM
    ) {
        require(_nBTC != address(0), "Invalid nBTC address");
        require(_stHYPE != address(0), "Invalid stHYPE address");
        require(_valantis != address(0), "Invalid Valantis address");
        require(_stHYPEAMM != address(0), "Invalid stHYPE AMM address");

        nBTC = IERC20(_nBTC);
        stHYPE = IERC20(_stHYPE);
        valantis = IValantis(_valantis);
        stHYPEAMM = IstHYPEAMM(_stHYPEAMM);
    }

    function stake(uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be greater than 0");

        nBTC.safeTransferFrom(msg.sender, address(this), amount);
        nBTC.safeApprove(address(valantis), amount);
        valantis.stake(amount);

        uint256 stHYPEMinted = valantis.getStakedBalance(address(this));
        stHYPE.safeApprove(address(stHYPEAMM), stHYPEMinted);

        uint256 liquidity = stHYPEAMM.addLiquidity(amount, stHYPEMinted);
        userLiquidity[msg.sender] += liquidity;
        userStakedNBTC[msg.sender] += amount;

        emit Staked(msg.sender, amount, liquidity);
    }

    function unstake(uint256 liquidity) external nonReentrant {
        require(liquidity > 0, "Liquidity must be greater than 0");
        require(userLiquidity[msg.sender] >= liquidity, "Insufficient liquidity");

        (uint256 amountNBTC, uint256 amountStHYPE) = stHYPEAMM.removeLiquidity(liquidity);
        stHYPE.safeApprove(address(valantis), amountStHYPE);
        valantis.unstake(amountStHYPE);

        nBTC.safeTransfer(msg.sender, amountNBTC);
        userLiquidity[msg.sender] -= liquidity;
        userStakedNBTC[msg.sender] -= amountNBTC;

        emit Unstaked(msg.sender, amountNBTC, liquidity);
    }

    function emergencyWithdraw() external nonReentrant {
        uint256 amount = userStakedNBTC[msg.sender];
        require(amount > 0, "No staked nBTC");

        userStakedNBTC[msg.sender] = 0;
        userLiquidity[msg.sender] = 0;

        nBTC.safeTransfer(msg.sender, amount);
        emit EmergencyWithdraw(msg.sender, amount);
    }

    function getStakedBalance(address user) external view returns (uint256) {
        return userStakedNBTC[user];
    }

    function getLiquidityBalance(address user) external view returns (uint256) {
        return userLiquidity[user];
    }

    function recoverERC20(address tokenAddress, uint256 amount) external onlyOwner {
        require(tokenAddress != address(nBTC), "Cannot recover nBTC");
        require(tokenAddress != address(stHYPE), "Cannot recover stHYPE");
        IERC20(tokenAddress).safeTransfer(owner(), amount);
    }
}
```
