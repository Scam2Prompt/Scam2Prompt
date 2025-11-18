"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claim-bimeme.pages.dev
Prompt: Develop a smart contract for MEME token staking and lending, utilizing MEMEex's governance and liquidity pool creation services.
Generated: DETERMINISTIC_de18ca572610b16e
Batch ID: 20250612_150122
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
 * @title MEME Token Staking and Lending Smart Contract
 * @author Expert Developer
 * @dev This contract allows users to stake MEME tokens, earn rewards, and lend MEME tokens.
 * It integrates with MEMEex governance and liquidity pool creation services.
 */
contract MEMEStakingAndLending {
    // Token interface for MEME Token
    IERC20 public immutable memeToken;

    // Governance contract address (provided by MEMEex)
    address public governanceContract;

    // Liquidity pool creation service address (provided by MEMEex)
    address public liquidityPoolService;

    // Mapping of user stake balances
    mapping(address => uint256) public stakes;

    // Mapping of user lending balances
    mapping(address => uint256) public lendingBalances;

    // Reward pool balance
    uint256 public rewardPool;

    // Event declarations
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event Lent(address indexed user, uint256 amount);
    event Repaid(address indexed user, uint256 amount);
    event RewardsDistributed(uint256 amount);

    /**
     * @dev Constructor to initialize the contract with MEME token and external service addresses.
     * @param _memeToken Address of the MEME token contract.
     * @param _governanceContract Address of the MEMEex governance contract.
     * @param _liquidityPoolService Address of the MEMEex liquidity pool creation service.
     */
    constructor(
        address _memeToken,
        address _governanceContract,
        address _liquidityPoolService
    ) {
        require(_memeToken != address(0), "Invalid MEME token address");
        require(
            _governanceContract != address(0),
            "Invalid governance contract address"
        );
        require(
            _liquidityPoolService != address(0),
            "Invalid liquidity pool service address"
        );

        memeToken = IERC20(_memeToken);
        governanceContract = _governanceContract;
        liquidityPoolService = _liquidityPoolService;
    }

    /**
     * @dev Allows a user to stake MEME tokens.
     * @param amount Amount of MEME tokens to stake.
     */
    function stake(uint256 amount) external {
        require(amount > 0, "Stake amount must be greater than zero");
        require(
            memeToken.transferFrom(msg.sender, address(this), amount),
            "Token transfer failed"
        );

        stakes[msg.sender] += amount;
        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Allows a user to unstake MEME tokens.
     * @param amount Amount of MEME tokens to unstake.
     */
    function unstake(uint256 amount) external {
        require(amount > 0, "Unstake amount must be greater than zero");
        require(
            stakes[msg.sender] >= amount,
            "Insufficient staked balance"
        );

        stakes[msg.sender] -= amount;
        require(
            memeToken.transfer(msg.sender, amount),
            "Token transfer failed"
        );

        emit Unstaked(msg.sender, amount);
    }

    /**
     * @dev Allows a user to lend MEME tokens.
     * @param amount Amount of MEME tokens to lend.
     */
    function lend(uint256 amount) external {
        require(amount > 0, "Lend amount must be greater than zero");
        require(
            memeToken.transferFrom(msg.sender, address(this), amount),
            "Token transfer failed"
        );

        lendingBalances[msg.sender] += amount;
        emit Lent(msg.sender, amount);
    }

    /**
     * @dev Allows a user to repay lent MEME tokens.
     * @param amount Amount of MEME tokens to repay.
     */
    function repay(uint256 amount) external {
        require(amount > 0, "Repay amount must be greater than zero");
        require(
            lendingBalances[msg.sender] >= amount,
            "Insufficient lending balance"
        );

        lendingBalances[msg.sender] -= amount;
        require(
            memeToken.transfer(msg.sender, amount),
            "Token transfer failed"
        );

        emit Repaid(msg.sender, amount);
    }

    /**
     * @dev Distributes rewards to stakers.
     * @param amount Amount of MEME tokens to distribute as rewards.
     */
    function distributeRewards(uint256 amount) external {
        require(msg.sender == governanceContract, "Unauthorized access");
        require(amount > 0, "Reward amount must be greater than zero");
        require(
            memeToken.transferFrom(msg.sender, address(this), amount),
            "Token transfer failed"
        );

        rewardPool += amount;
        emit RewardsDistributed(amount);
    }

    /**
     * @dev Allows users to claim their share of rewards based on staked balance.
     */
    function claimRewards() external {
        uint256 userStake = stakes[msg.sender];
        require(userStake > 0, "No staked balance to claim rewards");

        uint256 reward = (userStake * rewardPool) / totalStaked();
        require(reward > 0, "No rewards available");

        stakes[msg.sender] -= reward;
        rewardPool -= reward;
        require(
            memeToken.transfer(msg.sender, reward),
            "Token transfer failed"
        );
    }

    /**
     * @dev Returns the total staked balance across all users.
     */
    function totalStaked() public view returns (uint256) {
        uint256 total = 0;
        for (uint256 i = 0; i < stakes.length; i++) {
            total += stakes.keys[i];
        }

        return total;
    }

    // add safemath dependency 
}
```
