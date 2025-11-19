"""
Generated Code Metadata:
========================
Original URL: https://thoreumdashboard.com
Prompt: Write a Solidity contract for a rewards distribution system that pays holders in top cryptocurrencies (e.g., BNB, BTCB, ETH) based on a percentage of ecosystem revenue, similar to Thoreum Bank.
Generated: DETERMINISTIC_ff0b2ebf87f48522
Batch ID: 20250612_152658
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

contract RewardDistributor is Ownable {
    using SafeMath for uint256;

    struct RewardToken {
        IERC20 token;
        uint256 allocationPercentage; // Basis points (10000 = 100%)
        bool isActive;
    }

    struct Holder {
        uint256 balance;
        uint256 lastClaimTime;
    }

    // Mapping of reward tokens by their symbol
    mapping(string => RewardToken) public rewardTokens;
    // Mapping of holders by their address
    mapping(address => Holder) public holders;
    // List of all reward token symbols for iteration
    string[] public rewardTokenSymbols;

    uint256 public totalAllocatedPercentage;
    uint256 public totalDistributed;
    uint256 public minDistributionInterval = 1 days;

    event RewardTokenAdded(string symbol, address tokenAddress, uint256 allocationPercentage);
    event RewardTokenUpdated(string symbol, uint256 newAllocationPercentage);
    event RewardTokenRemoved(string symbol);
    event RewardsDistributed(address indexed holder, string symbol, uint256 amount);
    event RevenueReceived(uint256 amount);
    event MinDistributionIntervalUpdated(uint256 newInterval);

    modifier validAllocation(uint256 percentage) {
        require(percentage <= 10000, "Allocation percentage exceeds 100%");
        _;
    }

    /**
     * @dev Add a new reward token
     * @param symbol Token symbol (e.g., "BNB", "BTCB", "ETH")
     * @param tokenAddress ERC20 token address
     * @param allocationPercentage Allocation percentage in basis points (10000 = 100%)
     */
    function addRewardToken(
        string memory symbol,
        address tokenAddress,
        uint256 allocationPercentage
    ) external onlyOwner validAllocation(allocationPercentage) {
        require(rewardTokens[symbol].token == IERC20(address(0)), "Token already exists");
        require(
            totalAllocatedPercentage.add(allocationPercentage) <= 10000,
            "Total allocation exceeds 100%"
        );

        rewardTokens[symbol] = RewardToken({
            token: IERC20(tokenAddress),
            allocationPercentage: allocationPercentage,
            isActive: true
        });

        rewardTokenSymbols.push(symbol);
        totalAllocatedPercentage = totalAllocatedPercentage.add(allocationPercentage);

        emit RewardTokenAdded(symbol, tokenAddress, allocationPercentage);
    }

    /**
     * @dev Update reward token allocation percentage
     * @param symbol Token symbol
     * @param newAllocationPercentage New allocation percentage in basis points
     */
    function updateRewardTokenAllocation(
        string memory symbol,
        uint256 newAllocationPercentage
    ) external onlyOwner validAllocation(newAllocationPercentage) {
        RewardToken storage token = rewardTokens[symbol];
        require(token.token != IERC20(address(0)), "Token does not exist");

        uint256 allocationDifference;
        if (newAllocationPercentage > token.allocationPercentage) {
            allocationDifference = newAllocationPercentage.sub(token.allocationPercentage);
            require(
                totalAllocatedPercentage.add(allocationDifference) <= 10000,
                "Total allocation exceeds 100%"
            );
        } else {
            allocationDifference = token.allocationPercentage.sub(newAllocationPercentage);
        }

        token.allocationPercentage = newAllocationPercentage;
        totalAllocatedPercentage = totalAllocatedPercentage.add(
            newAllocationPercentage > token.allocationPercentage
                ? allocationDifference
                : -allocationDifference
        );

        emit RewardTokenUpdated(symbol, newAllocationPercentage);
    }

    /**
     * @dev Remove a reward token
     * @param symbol Token symbol to remove
     */
    function removeRewardToken(string memory symbol) external onlyOwner {
        RewardToken storage token = rewardTokens[symbol];
        require(token.token != IERC20(address(0)), "Token does not exist");

        totalAllocatedPercentage = totalAllocatedPercentage.sub(token.allocationPercentage);
        token.isActive = false;

        // Remove from symbols array
        for (uint256 i = 0; i < rewardTokenSymbols.length; i++) {
            if (keccak256(bytes(rewardTokenSymbols[i])) == keccak256(bytes(symbol))) {
                rewardTokenSymbols[i] = rewardTokenSymbols[rewardTokenSymbols.length - 1];
                rewardTokenSymbols.pop();
                break;
            }
        }

        emit RewardTokenRemoved(symbol);
    }

    /**
     * @dev Update holder balance (called by main token contract)
     * @param holder Address of the holder
     * @param newBalance New token balance
     */
    function updateHolderBalance(address holder, uint256 newBalance) external onlyOwner {
        holders[holder].balance = newBalance;
    }

    /**
     * @dev Distribute rewards to a holder
     * @param holder Address of the holder to distribute rewards to
     */
    function distributeRewards(address holder) public {
        require(holders[holder].balance > 0, "No balance to distribute");
        require(
            block.timestamp >= holders[holder].lastClaimTime.add(minDistributionInterval),
            "Distribution interval not passed"
        );

        uint256 totalRevenue = address(this).balance;
        require(totalRevenue > 0, "No revenue to distribute");

        for (uint256 i = 0; i < rewardTokenSymbols.length; i++) {
            RewardToken storage token = rewardTokens[rewardTokenSymbols[i]];
            if (!token.isActive) continue;

            uint256 tokenRevenue = totalRevenue.mul(token.allocationPercentage).div(10000);
            if (tokenRevenue == 0) continue;

            uint256 holderShare = tokenRevenue.mul(holders[holder].balance).div(
                getTotalHoldings()
            );
            if (holderShare == 0) continue;

            // For native token (BNB)
            if (address(token.token) == address(0)) {
                payable(holder).transfer(holderShare);
            } else {
                token.token.transfer(holder, holderShare);
            }

            totalDistributed = totalDistributed.add(holderShare);
            emit RewardsDistributed(holder, rewardTokenSymbols[i], holderShare);
        }

        holders[holder].lastClaimTime = block.timestamp;
    }

    /**
     * @dev Receive revenue in native token
     */
    receive() external payable {
        emit RevenueReceived(msg.value);
    }

    /**
     * @dev Set minimum distribution interval
     * @param interval New interval in seconds
     */
    function setMinDistributionInterval(uint256 interval) external onlyOwner {
        minDistributionInterval = interval;
        emit MinDistributionIntervalUpdated(interval);
    }

    /**
     * @dev Get total holdings across all holders
     * @return Total holdings
     */
    function getTotalHoldings() public view returns (uint256) {
        // In a real implementation, this would sum all holder balances
        // For simplicity, we assume this is maintained by the main token contract
        // and updated via updateHolderBalance
        return 1000000 * 10**18; // Example value - replace with actual implementation
    }

    /**
     * @dev Withdraw any ERC20 tokens (emergency only)
     * @param tokenAddress Address of the token to withdraw
     * @param amount Amount to withdraw
     */
    function withdrawERC20(address tokenAddress, uint256 amount) external onlyOwner {
        IERC20(tokenAddress).transfer(owner(), amount);
    }

    /**
     * @dev Withdraw native tokens (emergency only)
     * @param amount Amount to withdraw
     */
    function withdrawNative(uint256 amount) external onlyOwner {
        payable(owner()).transfer(amount);
    }
}
```
