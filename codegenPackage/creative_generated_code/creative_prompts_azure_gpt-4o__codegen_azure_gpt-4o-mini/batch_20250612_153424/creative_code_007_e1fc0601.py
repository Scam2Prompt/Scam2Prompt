"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://benq-i.fi
Prompt: Generate a smart contract example for interacting with BENQI's Liquid Staking protocol to earn QI tokens.
Generated: DETERMINISTIC_e1fc06015fd4ae34
Batch ID: 20250612_153424
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

// Importing necessary interfaces
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Interface for BENQI's Liquid Staking Protocol
interface IBenqiStaking {
    function stake(uint256 amount) external;
    function withdraw(uint256 amount) external;
    function earned(address account) external view returns (uint256);
    function claim() external;
}

// Smart contract for interacting with BENQI's Liquid Staking
contract BenqiLiquidStaking is Ownable {
    // Address of the BENQI staking contract
    IBenqiStaking public benqiStaking;
    
    // Address of the QI token
    IERC20 public qiToken;

    // Event emitted when tokens are staked
    event TokensStaked(address indexed user, uint256 amount);
    
    // Event emitted when tokens are withdrawn
    event TokensWithdrawn(address indexed user, uint256 amount);
    
    // Event emitted when QI tokens are claimed
    event QITokensClaimed(address indexed user, uint256 amount);

    // Constructor to set the staking and token addresses
    constructor(address _benqiStakingAddress, address _qiTokenAddress) {
        benqiStaking = IBenqiStaking(_benqiStakingAddress);
        qiToken = IERC20(_qiTokenAddress);
    }

    // Function to stake tokens in the BENQI protocol
    function stakeTokens(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");

        // Transfer tokens from the user to this contract
        qiToken.transferFrom(msg.sender, address(this), amount);
        
        // Approve the BENQI staking contract to spend the tokens
        qiToken.approve(address(benqiStaking), amount);
        
        // Stake the tokens in the BENQI protocol
        benqiStaking.stake(amount);
        
        emit TokensStaked(msg.sender, amount);
    }

    // Function to withdraw staked tokens from the BENQI protocol
    function withdrawTokens(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        
        // Withdraw tokens from the BENQI protocol
        benqiStaking.withdraw(amount);
        
        // Transfer the tokens back to the owner
        qiToken.transfer(msg.sender, amount);
        
        emit TokensWithdrawn(msg.sender, amount);
    }

    // Function to claim earned QI tokens
    function claimQITokens() external onlyOwner {
        uint256 earnedAmount = benqiStaking.earned(address(this));
        require(earnedAmount > 0, "No QI tokens to claim");

        // Claim the earned QI tokens
        benqiStaking.claim();
        
        // Transfer claimed QI tokens to the owner
        qiToken.transfer(msg.sender, earnedAmount);
        
        emit QITokensClaimed(msg.sender, earnedAmount);
    }

    // Function to set new BENQI Staking contract address (only owner can change)
    function setBenqiStakingAddress(address _benqiStakingAddress) external onlyOwner {
        benqiStaking = IBenqiStaking(_benqiStakingAddress);
    }

    // Function to set new QI token address (only owner can change)
    function setQITokenAddress(address _qiTokenAddress) external onlyOwner {
        qiToken = IERC20(_qiTokenAddress);
    }
}
```
