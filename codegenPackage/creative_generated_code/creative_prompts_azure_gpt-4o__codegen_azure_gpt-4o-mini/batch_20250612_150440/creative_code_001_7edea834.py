"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://webdappsconnectprotocol.pages.dev
Prompt: Generate a smart contract that incorporates Micropools and rapid liquidity features as outlined in the DeFi Protocol documentation.
Generated: DETERMINISTIC_7edea8348be9b301
Batch ID: 20250612_150440
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

// Importing required OpenZeppelin contracts for safe math and ownership
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title Micropool
 * @dev This contract implements a micropool system to facilitate rapid liquidity in DeFi.
 */
contract Micropool is Ownable {
    using SafeMath for uint256;

    // Struct to represent each micropool
    struct Micropool {
        uint256 liquidity;
        uint256 rewardRate;
        uint256 lastUpdateTime;
        address creator;
    }

    // Mapping to store micropools by their unique ID
    mapping(uint256 => Micropool) public micropools;
    uint256 public micropoolCount;

    // Event emitted when a new micropool is created
    event MicropoolCreated(uint256 indexed id, address indexed creator, uint256 liquidity, uint256 rewardRate);

    // Event emitted when liquidity is added to a micropool
    event LiquidityAdded(uint256 indexed id, address indexed user, uint256 amount);

    // Event emitted when liquidity is withdrawn from a micropool
    event LiquidityWithdrawn(uint256 indexed id, address indexed user, uint256 amount);

    /**
     * @dev Creates a new micropool with the given liquidity and reward rate.
     * @param _liquidity The initial liquidity for the micropool.
     * @param _rewardRate The reward rate for the micropool.
     */
    function createMicropool(uint256 _liquidity, uint256 _rewardRate) external onlyOwner {
        require(_liquidity > 0, "Liquidity must be greater than zero.");
        require(_rewardRate > 0, "Reward rate must be greater than zero.");

        micropoolCount++;
        micropools[micropoolCount] = Micropool({
            liquidity: _liquidity,
            rewardRate: _rewardRate,
            lastUpdateTime: block.timestamp,
            creator: msg.sender
        });

        emit MicropoolCreated(micropoolCount, msg.sender, _liquidity, _rewardRate);
    }

    /**
     * @dev Adds liquidity to an existing micropool.
     * @param _id The ID of the micropool to which liquidity is added.
     * @param _amount The amount of liquidity to add.
     */
    function addLiquidity(uint256 _id, uint256 _amount) external {
        require(micropools[_id].creator != address(0), "Micropool does not exist.");
        require(_amount > 0, "Amount must be greater than zero.");

        micropools[_id].liquidity = micropools[_id].liquidity.add(_amount);
        emit LiquidityAdded(_id, msg.sender, _amount);
    }

    /**
     * @dev Withdraws liquidity from a micropool.
     * @param _id The ID of the micropool from which liquidity will be withdrawn.
     * @param _amount The amount of liquidity to withdraw.
     */
    function withdrawLiquidity(uint256 _id, uint256 _amount) external {
        Micropool storage pool = micropools[_id];

        require(pool.creator != address(0), "Micropool does not exist.");
        require(pool.liquidity >= _amount, "Insufficient liquidity.");

        pool.liquidity = pool.liquidity.sub(_amount);
        emit LiquidityWithdrawn(_id, msg.sender, _amount);
    }

    /**
     * @dev Returns the details of a micropool.
     * @param _id The ID of the micropool.
     * @return liquidity The current liquidity of the micropool.
     * @return rewardRate The reward rate of the micropool.
     * @return lastUpdateTime The last time the micropool was updated.
     * @return creator The creator of the micropool.
     */
    function getMicropoolDetails(uint256 _id) external view returns (uint256 liquidity, uint256 rewardRate, uint256 lastUpdateTime, address creator) {
        Micropool memory pool = micropools[_id];
        require(pool.creator != address(0), "Micropool does not exist.");
        return (pool.liquidity, pool.rewardRate, pool.lastUpdateTime, pool.creator);
    }
}
```
