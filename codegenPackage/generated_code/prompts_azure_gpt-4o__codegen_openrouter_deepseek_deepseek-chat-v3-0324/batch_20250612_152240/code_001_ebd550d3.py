"""
Generated Code Metadata:
========================
Original URL: https://bafybeifq4glolowymafy6kuniwbsh4kspbnetu3fgelnegknbnkai2ahje.ipfs.dweb.link
Prompt: Generate code to deploy a decentralized finance (DeFi) dapp on Linea's ecosystem, ensuring compatibility with its 100% EVM bytecode.
Generated: DETERMINISTIC_ebd550d35cc001cd
Batch ID: 20250612_152240
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

/**
 * @title DeFiDapp
 * @dev A simple decentralized finance application compatible with Linea's EVM
 */
contract DeFiDapp is Ownable, ReentrancyGuard {
    IERC20 public token;
    uint256 public totalStaked;
    uint256 public rewardRate = 100; // 100 tokens per block
    uint256 public lastUpdateBlock;
    uint256 public rewardPerTokenStored;

    mapping(address => uint256) public userRewardPerTokenPaid;
    mapping(address => uint256) public rewards;
    mapping(address => uint256) public balances;

    event Staked(address indexed user, uint256 amount);
    event Withdrawn(address indexed user, uint256 amount);
    event RewardPaid(address indexed user, uint256 reward);

    constructor(address _token) {
        token = IERC20(_token);
        lastUpdateBlock = block.number;
    }

    /**
     * @dev Updates reward for a given account
     * @param account The account to update rewards for
     */
    modifier updateReward(address account) {
        rewardPerTokenStored = rewardPerToken();
        lastUpdateBlock = block.number;
        if (account != address(0)) {
            rewards[account] = earned(account);
            userRewardPerTokenPaid[account] = rewardPerTokenStored;
        }
        _;
    }

    /**
     * @dev Calculates the reward per token
     * @return The reward per token
     */
    function rewardPerToken() public view returns (uint256) {
        if (totalStaked == 0) {
            return rewardPerTokenStored;
        }
        return rewardPerTokenStored + 
            ((block.number - lastUpdateBlock) * rewardRate * 1e18) / totalStaked;
    }

    /**
     * @dev Calculates the earned rewards for an account
     * @param account The account to check rewards for
     * @return The earned rewards
     */
    function earned(address account) public view returns (uint256) {
        return ((balances[account] * 
                (rewardPerToken() - userRewardPerTokenPaid[account])) / 1e18) 
                + rewards[account];
    }

    /**
     * @dev Stake tokens to earn rewards
     * @param amount The amount of tokens to stake
     */
    function stake(uint256 amount) external nonReentrant updateReward(msg.sender) {
        require(amount > 0, "Cannot stake 0");
        totalStaked += amount;
        balances[msg.sender] += amount;
        require(token.transferFrom(msg.sender, address(this), amount), "Transfer failed");
        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Withdraw staked tokens
     * @param amount The amount of tokens to withdraw
     */
    function withdraw(uint256 amount) public nonReentrant updateReward(msg.sender) {
        require(amount > 0, "Cannot withdraw 0");
        require(balances[msg.sender] >= amount, "Insufficient balance");
        totalStaked -= amount;
        balances[msg.sender] -= amount;
        require(token.transfer(msg.sender, amount), "Transfer failed");
        emit Withdrawn(msg.sender, amount);
    }

    /**
     * @dev Claim earned rewards
     */
    function getReward() public nonReentrant updateReward(msg.sender) {
        uint256 reward = rewards[msg.sender];
        if (reward > 0) {
            rewards[msg.sender] = 0;
            require(token.transfer(msg.sender, reward), "Transfer failed");
            emit RewardPaid(msg.sender, reward);
        }
    }

    /**
     * @dev Exit the contract by withdrawing all staked tokens and claiming rewards
     */
    function exit() external {
        withdraw(balances[msg.sender]);
        getReward();
    }

    /**
     * @dev Update the reward rate (owner only)
     * @param _rewardRate The new reward rate
     */
    function setRewardRate(uint256 _rewardRate) external onlyOwner {
        rewardRate = _rewardRate;
    }

    /**
     * @dev Recover ERC20 tokens sent by mistake (owner only)
     * @param tokenAddress The token contract address
     * @param tokenAmount The amount to recover
     */
    function recoverERC20(address tokenAddress, uint256 tokenAmount) external onlyOwner {
        require(tokenAddress != address(token), "Cannot withdraw the staking token");
        IERC20(tokenAddress).transfer(owner(), tokenAmount);
    }
}
```
