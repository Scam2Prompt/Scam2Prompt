"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bitcoin-minetrix.web.app
Prompt: Generate Solidity code for an ERC-20 staking contract that mimics the "Stake-to-Mine" functionality described on the Bitcoin Minetrix website, where staked tokens generate non-tradable mining credits.
Generated: DETERMINISTIC_78bd435937e571a0
Batch ID: 20250612_152620
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
 * @title StakeToMine
 * @notice ERC-20 staking contract for generating non-tradable mining credits.
 */
contract StakeToMine {
    // State variables
    IERC20 public stakingToken; // The ERC-20 token users will stake
    address public owner;       // Contract owner

    uint256 public totalStaked; // Total tokens staked by all users

    mapping(address => uint256) public stakedBalances; // Tracks each user's staked balance
    mapping(address => uint256) public miningCredits;  // Tracks each user's generated mining credits
    uint256 public miningRate;                         // Mining credits generated per staked token per second

    // Events
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event MiningCreditsGenerated(address indexed user, uint256 credits);
    event OwnerWithdrawn(address indexed owner, uint256 amount);

    // Modifiers
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    /**
     * @notice Constructor to initialize the contract.
     * @param _stakingToken Address of the ERC-20 token to be staked.
     * @param _miningRate Mining credits generated per staked token per second.
     */
    constructor(IERC20 _stakingToken, uint256 _miningRate) {
        stakingToken = _stakingToken;
        miningRate = _miningRate;
        owner = msg.sender;
    }

    /**
     * @notice Allows users to stake tokens and start generating mining credits.
     * @param _amount Amount of tokens to stake.
     */
    function stake(uint256 _amount) external {
        require(_amount > 0, "Stake amount must be greater than zero");
        require(stakingToken.transferFrom(msg.sender, address(this), _amount), "Token transfer failed");

        // Generate pending mining credits for the user
        generateMiningCredits(msg.sender);

        // Update staking balances
        stakedBalances[msg.sender] += _amount;
        totalStaked += _amount;

        emit Staked(msg.sender, _amount);
    }

    /**
     * @notice Allows users to unstake tokens. Mining credits are unaffected and remain available.
     * @param _amount Amount of tokens to unstake.
     */
    function unstake(uint256 _amount) external {
        require(_amount > 0, "Unstake amount must be greater than zero");
        require(stakedBalances[msg.sender] >= _amount, "Insufficient staked balance");

        // Generate pending mining credits for the user
        generateMiningCredits(msg.sender);

        // Update staking balances
        stakedBalances[msg.sender] -= _amount;
        totalStaked -= _amount;

        require(stakingToken.transfer(msg.sender, _amount), "Token transfer failed");

        emit Unstaked(msg.sender, _amount);
    }

    /**
     * @notice Generates mining credits for a user based on their staked balance and time.
     * @param _user Address of the user to generate credits for.
     */
    function generateMiningCredits(address _user) internal {
        uint256 userStakedBalance = stakedBalances[_user];
        if (userStakedBalance > 0) {
            // Calculate new mining credits
            uint256 newCredits = userStakedBalance * miningRate;
            miningCredits[_user] += newCredits;

            emit MiningCreditsGenerated(_user, newCredits);
        }
    }

    /**
     * @notice Allows users to view their total mining credits.
     * @param _user Address of the user.
     * @return Total mining credits.
     */
    function getMiningCredits(address _user) external view returns (uint256) {
        return miningCredits[_user];
    }

    /**
     * @notice Allows the owner to withdraw staking tokens from the contract.
     * @param _amount Amount of tokens to withdraw.
     */
    function ownerWithdraw(uint256 _amount) external onlyOwner {
        require(_amount <= stakingToken.balanceOf(address(this)), "Insufficient contract balance");
        require(stakingToken.transfer(owner, _amount), "Token transfer failed");

        emit OwnerWithdrawn(owner, _amount);
    }
}

// Interface for ERC-20 tokens
interface IERC20 {
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function transfer(address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}
```
