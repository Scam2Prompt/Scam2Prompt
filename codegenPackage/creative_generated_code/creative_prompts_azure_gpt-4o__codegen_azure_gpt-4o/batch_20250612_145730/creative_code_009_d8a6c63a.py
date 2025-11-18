"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pepearab.pages.dev
Prompt: Generate a Solidity contract to handle the presale process for $PEAB tokens, including wallet connection, token swapping, and staking functionality.
Generated: DETERMINISTIC_d8a6c63a63315603
Batch ID: 20250612_145730
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

/**
 * @title PEABTokenPresale
 * @dev A contract to handle the presale process for $PEAB tokens, including swapping and staking functionality.
 */
contract PEABTokenPresale {
    // State variables
    address public owner; // Contract owner
    address public tokenAddress; // Address of the $PEAB token
    uint256 public presaleRate; // Conversion rate for token (ETH to $PEAB)
    uint256 public stakingRewardRate; // Reward rate for staking (annualized)
    bool public presaleActive; // Flag to start/stop presale

    mapping(address => uint256) public stakedBalance; // Tracks staked balances per wallet
    mapping(address => uint256) public stakingStartTimes; // When a user started staking
    
    event TokensPurchased(address indexed buyer, uint256 ethAmount, uint256 tokenAmount);
    event TokensStaked(address indexed staker, uint256 tokenAmount);
    event TokensUnstaked(address indexed staker, uint256 tokenAmount, uint256 rewardAmount);

    modifier onlyOwner() {
        require(msg.sender == owner, "Only the contract owner can access this function");
        _;
    }

    modifier presaleIsActive() {
        require(presaleActive, "Presale is not active");
        _;
    }

    /**
     * @dev Constructor initializes the contract owner and presale parameters.
     * @param _tokenAddress Address of the $PEAB token.
     * @param _presaleRate Conversion rate for presale (ETH to $PEAB).
     * @param _stakingRewardRate Annualized staking reward percentage.
     */
    constructor(address _tokenAddress, uint256 _presaleRate, uint256 _stakingRewardRate) {
        owner = msg.sender;
        tokenAddress = _tokenAddress;
        presaleRate = _presaleRate;
        stakingRewardRate = _stakingRewardRate;
        presaleActive = true;
    }

    /**
     * @dev Allows users to purchase $PEAB tokens during presale by sending ETH.
     */
    function buyTokens() external payable presaleIsActive {
        require(msg.value > 0, "ETH sent must be greater than zero");

        uint256 tokenAmount = msg.value * presaleRate; // Calculate token amount based on presale rate
        require(IERC20(tokenAddress).transfer(msg.sender, tokenAmount), "Token transfer failed");

        emit TokensPurchased(msg.sender, msg.value, tokenAmount);
    }

    /**
     * @dev Allows users to stake $PEAB tokens.
     * @param _amount Amount of $PEAB tokens to stake.
     */
    function stakeTokens(uint256 _amount) external {
        require(_amount > 0, "Staking amount must be greater than zero");
        require(IERC20(tokenAddress).transferFrom(msg.sender, address(this), _amount), "Token transfer failed");

        stakedBalance[msg.sender] += _amount;
        stakingStartTimes[msg.sender] = block.timestamp;

        emit TokensStaked(msg.sender, _amount);
    }

    /**
     * @dev Allows users to unstake their $PEAB tokens and claim staking rewards.
     */
    function unstakeTokens() external {
        uint256 stakedAmount = stakedBalance[msg.sender];
        require(stakedAmount > 0, "No tokens staked");

        // Calculate staking duration and rewards
        uint256 stakingDuration = block.timestamp - stakingStartTimes[msg.sender];
        uint256 rewardAmount = (stakedAmount * stakingRewardRate * stakingDuration) / (365 days * 100);

        stakedBalance[msg.sender] = 0;
        stakingStartTimes[msg.sender] = 0;

        // Transfer staked tokens and rewards back to the user
        require(IERC20(tokenAddress).transfer(msg.sender, stakedAmount + rewardAmount), "Token transfer failed");

        emit TokensUnstaked(msg.sender, stakedAmount, rewardAmount);
    }

    /**
     * @dev Allows the owner to toggle the presale's active state.
     */
    function togglePresale() external onlyOwner {
        presaleActive = !presaleActive;
    }

    /**
     * @dev Allows the owner to withdraw ETH from the contract.
     */
    function withdrawETH() external onlyOwner {
        uint256 contractBalance = address(this).balance;
        require(contractBalance > 0, "No ETH to withdraw");
        payable(owner).transfer(contractBalance);
    }

    /**
     * @dev Allows the owner to withdraw $PEAB tokens from the contract.
     */
    function withdrawTokens(uint256 _amount) external onlyOwner {
        require(IERC20(tokenAddress).transfer(owner, _amount), "Token transfer failed");
    }

    /**
     * @dev Fallback function to receive ETH.
     */
    receive() external payable {}
}

// Interface for ERC20 token standard
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
}
```
