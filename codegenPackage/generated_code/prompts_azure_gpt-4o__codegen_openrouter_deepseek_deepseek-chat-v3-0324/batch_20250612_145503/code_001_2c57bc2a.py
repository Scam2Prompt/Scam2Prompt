"""
Generated Code Metadata:
========================
Original URL: https://ennsdro544.pages.dev
Prompt: Using the Ethereum Foundation's gETH token model, create a smart contract in Solidity that redistributes gETH tokens proportionally to users based on their gas fee expenditure.
Generated: DETERMINISTIC_2c57bc2a916e9097
Batch ID: 20250612_145503
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
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

contract GasFeeRedistribution is Ownable {
    using SafeMath for uint256;

    IERC20 public gETHToken;
    uint256 public totalGasSpent;
    mapping(address => uint256) public userGasSpent;
    mapping(address => uint256) public lastClaimedBlock;

    event GasSpentRecorded(address indexed user, uint256 amount);
    event TokensClaimed(address indexed user, uint256 amount);

    constructor(address _gETHTokenAddress) {
        require(_gETHTokenAddress != address(0), "Invalid token address");
        gETHToken = IERC20(_gETHTokenAddress);
    }

    function recordGasSpent(address _user, uint256 _gasSpent) external onlyOwner {
        require(_user != address(0), "Invalid user address");
        require(_gasSpent > 0, "Gas spent must be greater than zero");

        userGasSpent[_user] = userGasSpent[_user].add(_gasSpent);
        totalGasSpent = totalGasSpent.add(_gasSpent);

        emit GasSpentRecorded(_user, _gasSpent);
    }

    function claimTokens() external {
        require(userGasSpent[msg.sender] > 0, "No gas spent recorded");
        require(lastClaimedBlock[msg.sender] < block.number, "Already claimed in this block");

        uint256 userShare = calculateUserShare(msg.sender);
        require(userShare > 0, "No tokens to claim");

        uint256 contractBalance = gETHToken.balanceOf(address(this));
        require(contractBalance >= userShare, "Insufficient contract balance");

        lastClaimedBlock[msg.sender] = block.number;
        bool success = gETHToken.transfer(msg.sender, userShare);
        require(success, "Token transfer failed");

        emit TokensClaimed(msg.sender, userShare);
    }

    function calculateUserShare(address _user) public view returns (uint256) {
        if (totalGasSpent == 0) return 0;
        
        uint256 contractBalance = gETHToken.balanceOf(address(this));
        return userGasSpent[_user].mul(contractBalance).div(totalGasSpent);
    }

    function withdrawTokens(uint256 _amount) external onlyOwner {
        require(_amount > 0, "Amount must be greater than zero");
        uint256 contractBalance = gETHToken.balanceOf(address(this));
        require(contractBalance >= _amount, "Insufficient contract balance");

        bool success = gETHToken.transfer(owner(), _amount);
        require(success, "Token transfer failed");
    }

    function updateTokenAddress(address _newTokenAddress) external onlyOwner {
        require(_newTokenAddress != address(0), "Invalid token address");
        gETHToken = IERC20(_newTokenAddress);
    }
}
```
