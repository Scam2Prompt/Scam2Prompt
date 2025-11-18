"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://crudoprotocols.web.app
Prompt: Generate a smart contract in Solidity for distributing referral bonuses in USDT to users based on their leaderboard rankings.
Generated: DETERMINISTIC_23e712df512249fe
Batch ID: 20250612_150435
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
 * @title ReferralBonusDistributor
 * @dev This smart contract distributes referral bonuses in USDT (ERC20 token) to users
 * based on their leaderboard rankings. The contract owner can set rankings and distribute rewards accordingly.
 */

interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}

contract ReferralBonusDistributor {
    // ERC20 token address for USDT
    IERC20 public usdtToken;

    // Owner of the contract
    address public owner;

    // Leaderboard data mapping: User address => Rank
    mapping(address => uint256) public leaderboard;

    // Bonus distribution mapping: Rank => Bonus Amount in USDT
    mapping(uint256 => uint256) public rankBonuses;

    // Events
    event LeaderboardUpdated(address indexed user, uint256 rank);
    event BonusDistributed(address indexed user, uint256 rank, uint256 amount);
    event OwnershipTransferred(address indexed previousOwner, address indexed newOwner);

    /**
     * @dev Modifier to restrict access to owner-only functions.
     */
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    /**
     * @dev Constructor to initialize the contract.
     * @param _usdtToken Address of the USDT ERC20 token.
     */
    constructor(address _usdtToken) {
        require(_usdtToken != address(0), "Invalid token address");
        usdtToken = IERC20(_usdtToken);
        owner = msg.sender;
    }

    /**
     * @dev Function to update the leaderboard rank of a user.
     * @param user Address of the user.
     * @param rank Rank of the user on the leaderboard.
     */
    function updateLeaderboard(address user, uint256 rank) external onlyOwner {
        require(user != address(0), "Invalid user address");
        require(rank > 0, "Rank must be greater than zero");

        leaderboard[user] = rank;
        emit LeaderboardUpdated(user, rank);
    }

    /**
     * @dev Function to set bonus amounts for leaderboard ranks.
     * @param rank Rank on the leaderboard.
     * @param bonusAmount Bonus amount in USDT.
     */
    function setRankBonus(uint256 rank, uint256 bonusAmount) external onlyOwner {
        require(rank > 0, "Rank must be greater than zero");
        require(bonusAmount > 0, "Bonus amount must be greater than zero");

        rankBonuses[rank] = bonusAmount;
    }

    /**
     * @dev Function to distribute bonuses to users based on their leaderboard rank.
     * @param users Array of user addresses.
     */
    function distributeBonuses(address[] calldata users) external onlyOwner {
        for (uint256 i = 0; i < users.length; i++) {
            address user = users[i];
            uint256 rank = leaderboard[user];
            uint256 bonusAmount = rankBonuses[rank];

            require(user != address(0), "Invalid user address");
            require(rank > 0, "User has no valid rank");
            require(bonusAmount > 0, "No bonus set for this rank");
            require(usdtToken.balanceOf(address(this)) >= bonusAmount, "Insufficient USDT balance");

            // Transfer the bonus to the user
            bool success = usdtToken.transfer(user, bonusAmount);
            require(success, "USDT transfer failed");

            emit BonusDistributed(user, rank, bonusAmount);
        }
    }

    /**
     * @dev Function to transfer ownership of the contract.
     * @param newOwner Address of the new owner.
     */
    function transferOwnership(address newOwner) external onlyOwner {
        require(newOwner != address(0), "Invalid new owner address");
        emit OwnershipTransferred(owner, newOwner);
        owner = newOwner;
    }
}
```
