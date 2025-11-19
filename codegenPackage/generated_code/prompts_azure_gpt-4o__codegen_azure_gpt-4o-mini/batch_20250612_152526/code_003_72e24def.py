"""
Generated Code Metadata:
========================
Original URL: https://satoshivmsquad.army
Prompt: Create a smart contract in Solidity for staking tokens and distributing airdrops, inspired by the SatoshiVM Squad staking model.
Generated: DETERMINISTIC_72e24defdb3dad2e
Batch ID: 20250612_152526
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
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title Staking and Airdrop Contract
 * @dev This contract allows users to stake ERC20 tokens and receive airdrops based on their stake.
 */
contract StakingAirdrop is Ownable {
    using SafeMath for uint256;

    // Token to be staked
    IERC20 public stakingToken;

    // Struct to hold user staking information
    struct Stake {
        uint256 amount;
        uint256 timestamp;
    }

    // Mapping of user addresses to their stakes
    mapping(address => Stake) public stakes;

    // Total staked amount
    uint256 public totalStaked;

    // Airdrop amount per staked token
    uint256 public airdropAmount;

    // Event emitted when tokens are staked
    event Staked(address indexed user, uint256 amount);

    // Event emitted when tokens are unstaked
    event Unstaked(address indexed user, uint256 amount);

    // Event emitted when airdrop is distributed
    event AirdropDistributed(address indexed user, uint256 amount);

    /**
     * @dev Constructor to initialize the staking token and airdrop amount.
     * @param _stakingToken Address of the ERC20 token to be staked.
     * @param _airdropAmount Amount of tokens to be distributed as airdrop per staked token.
     */
    constructor(IERC20 _stakingToken, uint256 _airdropAmount) {
        stakingToken = _stakingToken;
        airdropAmount = _airdropAmount;
    }

    /**
     * @dev Allows users to stake tokens.
     * @param amount Amount of tokens to stake.
     */
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        require(stakingToken.transferFrom(msg.sender, address(this), amount), "Transfer failed");

        // Update user's stake
        stakes[msg.sender].amount = stakes[msg.sender].amount.add(amount);
        stakes[msg.sender].timestamp = block.timestamp;
        totalStaked = totalStaked.add(amount);

        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Allows users to unstake their tokens.
     * @param amount Amount of tokens to unstake.
     */
    function unstake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        require(stakes[msg.sender].amount >= amount, "Insufficient staked amount");

        // Update user's stake
        stakes[msg.sender].amount = stakes[msg.sender].amount.sub(amount);
        totalStaked = totalStaked.sub(amount);
        require(stakingToken.transfer(msg.sender, amount), "Transfer failed");

        emit Unstaked(msg.sender, amount);
    }

    /**
     * @dev Distributes airdrop to stakers based on their stake.
     */
    function distributeAirdrop() external onlyOwner {
        for (uint256 i = 0; i < totalStaked; i++) {
            address user = address(uint160(i)); // Placeholder for user address retrieval
            uint256 userStake = stakes[user].amount;

            if (userStake > 0) {
                uint256 airdropAmountToDistribute = userStake.mul(airdropAmount);
                require(stakingToken.transfer(user, airdropAmountToDistribute), "Airdrop transfer failed");
                emit AirdropDistributed(user, airdropAmountToDistribute);
            }
        }
    }

    /**
     * @dev Allows the owner to update the airdrop amount.
     * @param newAirdropAmount New airdrop amount per staked token.
     */
    function updateAirdropAmount(uint256 newAirdropAmount) external onlyOwner {
        airdropAmount = newAirdropAmount;
    }

    /**
     * @dev Returns the stake information of a user.
     * @param user Address of the user.
     * @return amount Staked amount.
     * @return timestamp Timestamp of the last stake.
     */
    function getStakeInfo(address user) external view returns (uint256 amount, uint256 timestamp) {
        Stake memory userStake = stakes[user];
        return (userStake.amount, userStake.timestamp);
    }
}
```
