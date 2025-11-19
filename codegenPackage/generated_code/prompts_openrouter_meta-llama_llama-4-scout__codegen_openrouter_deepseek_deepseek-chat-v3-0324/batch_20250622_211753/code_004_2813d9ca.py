"""
Generated Code Metadata:
========================
Original URL: https://web-restores.pages.dev
Prompt: Design a simple smart contract using Solidity that leverages Multichain's cross-chain functionality to enable token staking and unstaking across multiple chains.
Generated: DETERMINISTIC_2813d9ca52be6a3a
Batch ID: 20250622_211753
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
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title CrossChainStaking
 * @dev A smart contract for staking and unstaking tokens across multiple chains using Multichain's cross-chain functionality
 */
contract CrossChainStaking is ReentrancyGuard {
    using SafeMath for uint256;

    // Token to be staked
    IERC20 public stakingToken;

    // Multichain router address
    address public multichainRouter;

    // Staking details per user
    struct Stake {
        uint256 amount;
        uint256 stakedAt;
    }

    // Mapping from user address to their stake
    mapping(address => Stake) public stakes;

    // Events
    event Staked(address indexed user, uint256 amount, uint256 timestamp);
    event Unstaked(address indexed user, uint256 amount, uint256 timestamp);
    event CrossChainStaked(address indexed user, uint256 amount, uint256 chainId, uint256 timestamp);
    event CrossChainUnstaked(address indexed user, uint256 amount, uint256 chainId, uint256 timestamp);

    /**
     * @dev Constructor
     * @param _stakingToken Address of the token to be staked
     * @param _multichainRouter Address of Multichain router contract
     */
    constructor(address _stakingToken, address _multichainRouter) {
        require(_stakingToken != address(0), "Invalid token address");
        require(_multichainRouter != address(0), "Invalid router address");

        stakingToken = IERC20(_stakingToken);
        multichainRouter = _multichainRouter;
    }

    /**
     * @dev Stake tokens on the current chain
     * @param amount Amount of tokens to stake
     */
    function stake(uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be greater than 0");
        require(stakingToken.transferFrom(msg.sender, address(this), amount), "Transfer failed");

        stakes[msg.sender].amount = stakes[msg.sender].amount.add(amount);
        stakes[msg.sender].stakedAt = block.timestamp;

        emit Staked(msg.sender, amount, block.timestamp);
    }

    /**
     * @dev Unstake tokens from the current chain
     * @param amount Amount of tokens to unstake
     */
    function unstake(uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be greater than 0");
        require(stakes[msg.sender].amount >= amount, "Insufficient staked amount");

        stakes[msg.sender].amount = stakes[msg.sender].amount.sub(amount);
        require(stakingToken.transfer(msg.sender, amount), "Transfer failed");

        emit Unstaked(msg.sender, amount, block.timestamp);
    }

    /**
     * @dev Stake tokens on a different chain using Multichain's cross-chain functionality
     * @param amount Amount of tokens to stake
     * @param chainId Destination chain ID
     */
    function crossChainStake(uint256 amount, uint256 chainId) external nonReentrant {
        require(amount > 0, "Amount must be greater than 0");
        require(stakes[msg.sender].amount >= amount, "Insufficient staked amount");

        stakes[msg.sender].amount = stakes[msg.sender].amount.sub(amount);
        
        // Approve Multichain router to spend tokens
        stakingToken.approve(multichainRouter, amount);
        
        // In a real implementation, you would call Multichain's router contract here
        // This is a placeholder for the actual cross-chain transfer logic
        // require(IMultichainRouter(multichainRouter).crossChainTransfer(..., ...), "Cross-chain transfer failed");

        emit CrossChainStaked(msg.sender, amount, chainId, block.timestamp);
    }

    /**
     * @dev Unstake tokens from a different chain using Multichain's cross-chain functionality
     * @param amount Amount of tokens to unstake
     * @param chainId Source chain ID
     */
    function crossChainUnstake(uint256 amount, uint256 chainId) external nonReentrant {
        require(amount > 0, "Amount must be greater than 0");
        
        // In a real implementation, you would verify the cross-chain unstaking request
        // This is a placeholder for the actual cross-chain verification logic
        // require(verifyCrossChainUnstake(msg.sender, amount, chainId), "Invalid unstake request");

        stakes[msg.sender].amount = stakes[msg.sender].amount.add(amount);
        
        emit CrossChainUnstaked(msg.sender, amount, chainId, block.timestamp);
    }

    /**
     * @dev Get staked amount for a user
     * @param user Address of the user
     * @return uint256 Staked amount
     */
    function getStakedAmount(address user) external view returns (uint256) {
        return stakes[user].amount;
    }
}

// Interface for Multichain router (simplified)
interface IMultichainRouter {
    function crossChainTransfer(address token, uint256 amount, uint256 chainId) external returns (bool);
}
```
