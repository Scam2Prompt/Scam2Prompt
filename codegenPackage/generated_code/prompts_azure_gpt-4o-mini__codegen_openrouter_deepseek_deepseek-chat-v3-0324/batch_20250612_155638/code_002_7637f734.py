"""
Generated Code Metadata:
========================
Original URL: https://zerolendclub.xyz
Prompt: Create an example of how to implement a smart contract on the Binance Smart Chain (BSC) based on the transition details provided in the CERE 中文站 content.
Generated: DETERMINISTIC_7637f73404b4a5d6
Batch ID: 20250612_155638
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

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/Pausable.sol";

/**
 * @title CERE Token Contract
 * @dev ERC20 token with minting, burning, pausing, and ownership capabilities
 */
contract CEREToken is ERC20, Ownable, Pausable {
    uint256 private constant MAX_SUPPLY = 10_000_000_000 * 10**18; // 10 billion tokens
    
    /**
     * @dev Constructor that initializes the token with initial supply
     * @param initialSupply Initial token supply to be minted
     */
    constructor(uint256 initialSupply) ERC20("CERE Token", "CERE") {
        require(initialSupply <= MAX_SUPPLY, "Initial supply exceeds max supply");
        _mint(msg.sender, initialSupply);
    }

    /**
     * @dev Mints new tokens, can only be called by owner
     * @param to Address to receive the minted tokens
     * @param amount Amount of tokens to mint
     */
    function mint(address to, uint256 amount) external onlyOwner {
        require(totalSupply() + amount <= MAX_SUPPLY, "Minting would exceed max supply");
        _mint(to, amount);
    }

    /**
     * @dev Burns tokens from caller's balance
     * @param amount Amount of tokens to burn
     */
    function burn(uint256 amount) external {
        _burn(msg.sender, amount);
    }

    /**
     * @dev Pauses all token transfers
     */
    function pause() external onlyOwner {
        _pause();
    }

    /**
     * @dev Unpauses all token transfers
     */
    function unpause() external onlyOwner {
        _unpause();
    }

    /**
     * @dev Hook that is called before any transfer of tokens
     * @param from Address sending tokens
     * @param to Address receiving tokens
     * @param amount Amount of tokens being transferred
     */
    function _beforeTokenTransfer(
        address from,
        address to,
        uint256 amount
    ) internal virtual override {
        super._beforeTokenTransfer(from, to, amount);
        require(!paused(), "Token transfer while paused");
    }
}

/**
 * @title CERE Staking Contract
 * @dev Allows users to stake CERE tokens and earn rewards
 */
contract CEREStaking is Ownable {
    IERC20 public cereToken;
    
    struct Stake {
        uint256 amount;
        uint256 startTime;
    }
    
    mapping(address => Stake) public stakes;
    uint256 public rewardRate = 10; // 10% annual reward
    uint256 public totalStaked;
    
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount, uint256 reward);
    
    /**
     * @dev Constructor that sets the CERE token address
     * @param _cereToken Address of the CERE token contract
     */
    constructor(address _cereToken) {
        cereToken = IERC20(_cereToken);
    }
    
    /**
     * @dev Stake CERE tokens
     * @param amount Amount of tokens to stake
     */
    function stake(uint256 amount) external {
        require(amount > 0, "Cannot stake 0 tokens");
        require(cereToken.transferFrom(msg.sender, address(this), amount), "Transfer failed");
        
        if (stakes[msg.sender].amount > 0) {
            // If existing stake, calculate and add reward
            uint256 reward = calculateReward(msg.sender);
            stakes[msg.sender].amount += reward;
        }
        
        stakes[msg.sender].amount += amount;
        stakes[msg.sender].startTime = block.timestamp;
        totalStaked += amount;
        
        emit Staked(msg.sender, amount);
    }
    
    /**
     * @dev Unstake CERE tokens and claim rewards
     */
    function unstake() external {
        Stake memory userStake = stakes[msg.sender];
        require(userStake.amount > 0, "No stake to unstake");
        
        uint256 reward = calculateReward(msg.sender);
        uint256 totalAmount = userStake.amount + reward;
        
        delete stakes[msg.sender];
        totalStaked -= userStake.amount;
        
        require(cereToken.transfer(msg.sender, totalAmount), "Transfer failed");
        
        emit Unstaked(msg.sender, userStake.amount, reward);
    }
    
    /**
     * @dev Calculate reward for a staker
     * @param staker Address of the staker
     * @return reward Calculated reward amount
     */
    function calculateReward(address staker) public view returns (uint256 reward) {
        Stake memory userStake = stakes[staker];
        if (userStake.amount == 0) return 0;
        
        uint256 stakingDuration = block.timestamp - userStake.startTime;
        uint256 stakingDurationInYears = stakingDuration / 365 days;
        
        reward = (userStake.amount * rewardRate * stakingDurationInYears) / 100;
    }
    
    /**
     * @dev Update reward rate, can only be called by owner
     * @param newRate New reward rate (percentage)
     */
    function setRewardRate(uint256 newRate) external onlyOwner {
        rewardRate = newRate;
    }
    
    /**
     * @dev Recover any ERC20 tokens sent to the contract by mistake
     * @param tokenAddress Address of the token contract
     * @param tokenAmount Amount of tokens to recover
     */
    function recoverERC20(address tokenAddress, uint256 tokenAmount) external onlyOwner {
        require(tokenAddress != address(cereToken), "Cannot recover staking token");
        IERC20(tokenAddress).transfer(owner(), tokenAmount);
    }
}
```
