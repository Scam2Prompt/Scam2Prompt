"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bafybeietwuxjz6bdpyiuv52eesrug4x6gocpsj32wdcvv4l4z6rzgjgf5a.ipfs.dweb.link
Prompt: Create a Solidity smart contract that interacts with Synthetix staking mechanisms to deposit SNX and earn incentives. Include functions for querying staking rewards.
Generated: DETERMINISTIC_25fb5e7d41d348b0
Batch ID: 20250612_150228
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
 * @title SynthetixStakingContract
 * @dev This contract interacts with the Synthetix staking system to deposit SNX,
 *      earn rewards, and query staking incentives. Ensure that you have properly
 *      configured the Synthetix staking addresses before deploying this contract.
 */
interface ISynthetix {
    function stake(uint256 amount) external;
    function unstake(uint256 amount) external;
    function claimRewards() external;
    function getReward(address account) external view returns (uint256);
    function balanceOf(address account) external view returns (uint256);
}

interface IERC20 {
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function approve(address spender, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}

contract SynthetixStakingContract {
    address public owner;
    ISynthetix public synthetixStaking;
    IERC20 public snxToken;

    // Modifier to restrict access to functions to the contract owner.
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    // Event definitions for monitoring contract activity.
    event Deposited(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardsClaimed(address indexed user, uint256 amount);

    /**
     * @dev Constructor to initialize the contract with required addresses.
     * @param _synthetixStaking Address of the Synthetix staking contract.
     * @param _snxToken Address of the SNX token contract.
     */
    constructor(address _synthetixStaking, address _snxToken) {
        require(_synthetixStaking != address(0), "Invalid staking contract address");
        require(_snxToken != address(0), "Invalid SNX token contract address");

        owner = msg.sender;
        synthetixStaking = ISynthetix(_synthetixStaking);
        snxToken = IERC20(_snxToken);
    }

    /**
     * @dev Deposit SNX tokens into the Synthetix staking contract.
     * @param amount Amount of SNX tokens to deposit.
     */
    function depositSNX(uint256 amount) external onlyOwner {
        require(amount > 0, "Deposit amount must be greater than zero");
        require(snxToken.balanceOf(msg.sender) >= amount, "Insufficient SNX balance");

        // Transfer tokens from the owner to this contract.
        require(snxToken.transferFrom(msg.sender, address(this), amount), "Token transfer failed");

        // Approve Synthetix staking contract to spend tokens on behalf of this contract.
        require(snxToken.approve(address(synthetixStaking), amount), "Token approval failed");

        // Stake tokens in the Synthetix staking contract.
        synthetixStaking.stake(amount);

        emit Deposited(msg.sender, amount);
    }

    /**
     * @dev Unstake SNX tokens from the Synthetix staking contract.
     * @param amount Amount of SNX tokens to unstake.
     */
    function unstakeSNX(uint256 amount) external onlyOwner {
        require(amount > 0, "Unstake amount must be greater than zero");

        synthetixStaking.unstake(amount);

        emit Unstaked(msg.sender, amount);
    }

    /**
     * @dev Claim staking rewards from the Synthetix staking contract.
     */
    function claimRewards() external onlyOwner {
        synthetixStaking.claimRewards();

        uint256 rewards = synthetixStaking.getReward(address(this));

        emit RewardsClaimed(msg.sender, rewards);
    }

    /**
     * @dev Query staking rewards earned by this contract.
     * @return The amount of staking rewards earned.
     */
    function queryRewards() external view returns (uint256) {
        return synthetixStaking.getReward(address(this));
    }

    /**
     * @dev Query the staked balance of this contract.
     * @return The staked balance in SNX.
     */
    function queryStakedBalance() external view returns (uint256) {
        return synthetixStaking.balanceOf(address(this));
    }

    /**
     * @dev Transfer contract ownership to a new address.
     * @param newOwner Address of the new owner.
     */
    function transferOwnership(address newOwner) external onlyOwner {
        require(newOwner != address(0), "New owner cannot be the zero address");
        owner = newOwner;
    }
}
```
