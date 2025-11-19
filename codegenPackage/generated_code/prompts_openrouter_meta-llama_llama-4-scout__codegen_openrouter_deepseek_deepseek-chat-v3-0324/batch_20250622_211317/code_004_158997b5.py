"""
Generated Code Metadata:
========================
Original URL: https://dcqqx.com
Prompt: "How can smart contracts be utilized in a platform like dcqqx for DeFi applications on Ethereum?"
Generated: DETERMINISTIC_158997b50a690969
Batch ID: 20250622_211317
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
 * @title DeFiPlatform
 * @dev A smart contract for DeFi applications on Ethereum
 */
contract DeFiPlatform is Ownable, ReentrancyGuard {
    // Token contract address
    IERC20 public token;

    // Mapping to track user balances
    mapping(address => uint256) public userBalances;

    // Mapping to track approved spenders
    mapping(address => mapping(address => uint256)) public allowances;

    // Events
    event Deposit(address indexed user, uint256 amount);
    event Withdraw(address indexed user, uint256 amount);
    event Transfer(address indexed from, address indexed to, uint256 amount);
    event Approval(address indexed owner, address indexed spender, uint256 amount);

    /**
     * @dev Constructor that sets the token address
     * @param _tokenAddress Address of the ERC20 token contract
     */
    constructor(address _tokenAddress) {
        require(_tokenAddress != address(0), "Invalid token address");
        token = IERC20(_tokenAddress);
    }

    /**
     * @dev Deposit tokens into the platform
     * @param amount Amount of tokens to deposit
     */
    function deposit(uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be greater than 0");
        
        bool success = token.transferFrom(msg.sender, address(this), amount);
        require(success, "Token transfer failed");
        
        userBalances[msg.sender] += amount;
        emit Deposit(msg.sender, amount);
    }

    /**
     * @dev Withdraw tokens from the platform
     * @param amount Amount of tokens to withdraw
     */
    function withdraw(uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be greater than 0");
        require(userBalances[msg.sender] >= amount, "Insufficient balance");

        userBalances[msg.sender] -= amount;
        bool success = token.transfer(msg.sender, amount);
        require(success, "Token transfer failed");

        emit Withdraw(msg.sender, amount);
    }

    /**
     * @dev Transfer tokens to another user within the platform
     * @param to Recipient address
     * @param amount Amount of tokens to transfer
     */
    function transfer(address to, uint256 amount) external nonReentrant {
        require(to != address(0), "Invalid recipient address");
        require(amount > 0, "Amount must be greater than 0");
        require(userBalances[msg.sender] >= amount, "Insufficient balance");

        userBalances[msg.sender] -= amount;
        userBalances[to] += amount;

        emit Transfer(msg.sender, to, amount);
    }

    /**
     * @dev Approve another address to spend tokens on your behalf
     * @param spender Address to approve
     * @param amount Amount of tokens to approve
     */
    function approve(address spender, uint256 amount) external {
        require(spender != address(0), "Invalid spender address");

        allowances[msg.sender][spender] = amount;
        emit Approval(msg.sender, spender, amount);
    }

    /**
     * @dev Transfer tokens from one address to another using allowance
     * @param from Sender address
     * @param to Recipient address
     * @param amount Amount of tokens to transfer
     */
    function transferFrom(address from, address to, uint256 amount) external nonReentrant {
        require(from != address(0), "Invalid sender address");
        require(to != address(0), "Invalid recipient address");
        require(amount > 0, "Amount must be greater than 0");
        require(userBalances[from] >= amount, "Insufficient balance");
        require(allowances[from][msg.sender] >= amount, "Allowance exceeded");

        userBalances[from] -= amount;
        userBalances[to] += amount;
        allowances[from][msg.sender] -= amount;

        emit Transfer(from, to, amount);
    }

    /**
     * @dev Get user balance
     * @param user Address of the user
     * @return User's balance
     */
    function getBalance(address user) external view returns (uint256) {
        return userBalances[user];
    }

    /**
     * @dev Get allowance for a spender
     * @param owner Address of the owner
     * @param spender Address of the spender
     * @return Remaining allowance
     */
    function getAllowance(address owner, address spender) external view returns (uint256) {
        return allowances[owner][spender];
    }
}

/**
 * @title StakingContract
 * @dev A smart contract for staking tokens and earning rewards
 */
contract StakingContract is Ownable, ReentrancyGuard {
    IERC20 public stakingToken;
    IERC20 public rewardToken;

    uint256 public rewardRate;
    uint256 public lastUpdateTime;
    uint256 public rewardPerTokenStored;

    mapping(address => uint256) public userRewardPerTokenPaid;
    mapping(address => uint256) public rewards;
    mapping(address => uint256) private _balances;

    uint256 private _totalSupply;

    event Staked(address indexed user, uint256 amount);
    event Withdrawn(address indexed user, uint256 amount);
    event RewardPaid(address indexed user, uint256 reward);

    constructor(address _stakingToken, address _rewardToken) {
        stakingToken = IERC20(_stakingToken);
        rewardToken = IERC20(_rewardToken);
    }

    function totalSupply() external view returns (uint256) {
        return _totalSupply;
    }

    function balanceOf(address account) external view returns (uint256) {
        return _balances[account];
    }

    function rewardPerToken() public view returns (uint256) {
        if (_totalSupply == 0) {
            return rewardPerTokenStored;
        }
        return rewardPerTokenStored + 
            (((block.timestamp - lastUpdateTime) * rewardRate * 1e18) / _totalSupply);
    }

    function earned(address account) public view returns (uint256) {
        return ((_balances[account] * 
                (rewardPerToken() - userRewardPerTokenPaid[account])) / 1e18) + rewards[account];
    }

    modifier updateReward(address account) {
        rewardPerTokenStored = rewardPerToken();
        lastUpdateTime = block.timestamp;
        
        if (account != address(0)) {
            rewards[account] = earned(account);
            userRewardPerTokenPaid[account] = rewardPerTokenStored;
        }
        _;
    }

    function stake(uint256 amount) external nonReentrant updateReward(msg.sender) {
        require(amount > 0, "Cannot stake 0");
        
        _totalSupply += amount;
        _balances[msg.sender] += amount;
        
        bool success = stakingToken.transferFrom(msg.sender, address(this), amount);
        require(success, "Token transfer failed");
        
        emit Staked(msg.sender, amount);
    }

    function withdraw(uint256 amount) public nonReentrant updateReward(msg.sender) {
        require(amount > 0, "Cannot withdraw 0");
        
        _totalSupply -= amount;
        _balances[msg.sender] -= amount;
        
        bool success = stakingToken.transfer(msg.sender, amount);
        require(success, "Token transfer failed");
        
        emit Withdrawn(msg.sender, amount);
    }

    function getReward() public nonReentrant updateReward(msg.sender) {
        uint256 reward = rewards[msg.sender];
        if (reward > 0) {
            rewards[msg.sender] = 0;
            
            bool success = rewardToken.transfer(msg.sender, reward);
            require(success, "Token transfer failed");
            
            emit RewardPaid(msg.sender, reward);
        }
    }

    function exit() external {
        withdraw(_balances[msg.sender]);
        getReward();
    }

    function setRewardRate(uint256 _rewardRate) external onlyOwner {
        rewardRate = _rewardRate;
        lastUpdateTime = block.timestamp;
    }
}
```
