"""
Generated Code Metadata:
========================
Original URL: https://www.staderlabs.fi
Prompt: Design a smart contract on BNB Chain that integrates with Stader Labs' liquid staking solution, allowing users to stake BNB and earn rewards while maintaining liquidity.
Generated: DETERMINISTIC_182e84b33e30e2c4
Batch ID: 20250622_211123
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

interface IStaderBNB {
    function deposit() external payable;
    function withdraw(uint256 _amount) external;
    function getExchangeRate() external view returns (uint256);
    function balanceOf(address account) external view returns (uint256);
}

contract BNBLiquidStaking is Ownable, ReentrancyGuard {
    IStaderBNB public staderBNB;
    IERC20 public staderBNBToken;

    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardsClaimed(address indexed user, uint256 amount);
    event EmergencyWithdraw(address indexed user, uint256 amount);

    /**
     * @dev Constructor to initialize the Stader BNB contract address
     * @param _staderBNBAddress Address of Stader BNB contract
     * @param _staderBNBTokenAddress Address of Stader BNB token (liquid staking token)
     */
    constructor(address _staderBNBAddress, address _staderBNBTokenAddress) {
        require(_staderBNBAddress != address(0), "Invalid Stader BNB address");
        require(_staderBNBTokenAddress != address(0), "Invalid Stader BNB token address");
        
        staderBNB = IStaderBNB(_staderBNBAddress);
        staderBNBToken = IERC20(_staderBNBTokenAddress);
    }

    /**
     * @dev Stake BNB and receive liquid staking tokens
     */
    function stake() external payable nonReentrant {
        require(msg.value > 0, "Amount must be greater than 0");
        
        uint256 balanceBefore = staderBNBToken.balanceOf(address(this));
        staderBNB.deposit{value: msg.value}();
        uint256 balanceAfter = staderBNBToken.balanceOf(address(this));
        uint256 receivedAmount = balanceAfter - balanceBefore;

        require(staderBNBToken.transfer(msg.sender, receivedAmount), "Transfer failed");
        
        emit Staked(msg.sender, msg.value);
    }

    /**
     * @dev Unstake by burning liquid staking tokens and receiving BNB
     * @param _amount Amount of liquid staking tokens to unstake
     */
    function unstake(uint256 _amount) external nonReentrant {
        require(_amount > 0, "Amount must be greater than 0");
        
        uint256 bnbAmount = (_amount * staderBNB.getExchangeRate()) / 1e18;
        require(bnbAmount > 0, "Invalid BNB amount");

        require(staderBNBToken.transferFrom(msg.sender, address(this), _amount), "Transfer failed");
        staderBNB.withdraw(_amount);
        
        (bool success, ) = msg.sender.call{value: bnbAmount}("");
        require(success, "BNB transfer failed");
        
        emit Unstaked(msg.sender, _amount);
    }

    /**
     * @dev Emergency withdraw for admin to recover funds (onlyOwner)
     * @param _tokenAddress Address of token to withdraw
     * @param _amount Amount to withdraw
     */
    function emergencyWithdraw(address _tokenAddress, uint256 _amount) external onlyOwner {
        require(_amount > 0, "Amount must be greater than 0");
        
        if (_tokenAddress == address(0)) {
            (bool success, ) = owner().call{value: _amount}("");
            require(success, "BNB transfer failed");
        } else {
            IERC20 token = IERC20(_tokenAddress);
            require(token.transfer(owner(), _amount), "Token transfer failed");
        }
        
        emit EmergencyWithdraw(owner(), _amount);
    }

    /**
     * @dev Get the current exchange rate from Stader
     * @return Current exchange rate (1e18 precision)
     */
    function getExchangeRate() external view returns (uint256) {
        return staderBNB.getExchangeRate();
    }

    /**
     * @dev Get user's staked balance in liquid staking tokens
     * @param _user Address of user
     * @return User's balance
     */
    function getUserBalance(address _user) external view returns (uint256) {
        return staderBNBToken.balanceOf(_user);
    }

    // Allow contract to receive BNB
    receive() external payable {}
}
```
