"""
Generated Code Metadata:
========================
Original URL: https://fi-dapp-git-aleks-featfeedback-page-etherfi.vercel.app
Prompt: Provide a code example for initiating a (re)staking journey with eETH on etherfi, ensuring compatibility with DeFi protocols.
Generated: DETERMINISTIC_b4b664b40d4e2140
Batch ID: 20250612_153526
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

/**
 * @title EtherFi eETH Staking Contract
 * @notice Allows users to stake and restake eETH tokens with EtherFi protocol
 * @dev Implements SafeERC20 for secure token transfers and ReentrancyGuard for security
 */
contract EtherFiStaking is ReentrancyGuard {
    using SafeERC20 for IERC20;

    // eETH token contract
    IERC20 public immutable eETHToken;
    
    // EtherFi staking contract address
    address public immutable etherFiStakingContract;

    // Events
    event Staked(address indexed user, uint256 amount);
    event Restaked(address indexed user, uint256 amount);
    event Withdrawn(address indexed user, uint256 amount);

    /**
     * @dev Constructor initializes the contract with eETH token and EtherFi staking contract addresses
     * @param _eETHToken Address of the eETH token contract
     * @param _etherFiStakingContract Address of the EtherFi staking contract
     */
    constructor(address _eETHToken, address _etherFiStakingContract) {
        require(_eETHToken != address(0), "Invalid eETH token address");
        require(_etherFiStakingContract != address(0), "Invalid staking contract address");
        
        eETHToken = IERC20(_eETHToken);
        etherFiStakingContract = _etherFiStakingContract;
    }

    /**
     * @notice Stake eETH tokens with EtherFi protocol
     * @param amount Amount of eETH to stake
     */
    function stake(uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be greater than 0");
        
        // Transfer eETH from user to this contract
        eETHToken.safeTransferFrom(msg.sender, address(this), amount);
        
        // Approve EtherFi staking contract to spend eETH
        eETHToken.safeApprove(etherFiStakingContract, amount);
        
        // Call EtherFi staking contract (implementation depends on EtherFi's interface)
        (bool success, ) = etherFiStakingContract.call(
            abi.encodeWithSignature("stake(uint256)", amount)
        );
        require(success, "Staking failed");
        
        emit Staked(msg.sender, amount);
    }

    /**
     * @notice Restake accumulated rewards (implementation depends on EtherFi's rewards mechanism)
     * @param amount Amount to restake
     */
    function restake(uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be greater than 0");
        
        // Call EtherFi restaking function (implementation depends on EtherFi's interface)
        (bool success, ) = etherFiStakingContract.call(
            abi.encodeWithSignature("restake(uint256)", amount)
        );
        require(success, "Restaking failed");
        
        emit Restaked(msg.sender, amount);
    }

    /**
     * @notice Withdraw staked eETH from EtherFi protocol
     * @param amount Amount to withdraw
     */
    function withdraw(uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be greater than 0");
        
        // Call EtherFi withdrawal function (implementation depends on EtherFi's interface)
        (bool success, ) = etherFiStakingContract.call(
            abi.encodeWithSignature("withdraw(uint256)", amount)
        );
        require(success, "Withdrawal failed");
        
        // Transfer eETH back to user
        eETHToken.safeTransfer(msg.sender, amount);
        
        emit Withdrawn(msg.sender, amount);
    }

    /**
     * @notice Emergency function to recover ERC20 tokens sent to this contract by mistake
     * @param tokenAddress Address of the token to recover
     * @param amount Amount to recover
     */
    function recoverERC20(address tokenAddress, uint256 amount) external onlyOwner {
        require(tokenAddress != address(eETHToken), "Cannot recover eETH");
        IERC20(tokenAddress).safeTransfer(msg.sender, amount);
    }

    // Modifier to restrict functions to contract owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can call this function");
        _;
    }
    
    // Contract owner address
    address public owner;
    
    /**
     * @dev Sets the contract owner
     * @param _owner Address of the owner
     */
    function setOwner(address _owner) external onlyOwner {
        require(_owner != address(0), "Invalid owner address");
        owner = _owner;
    }
}
```
