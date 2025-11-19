"""
Generated Code Metadata:
========================
Original URL: https://kodiak-finance.org
Prompt: Create a smart contract in Solidity that mimics Kodiak Finance's automated yield strategies by dynamically reallocating funds across DeFi protocols based on real-time yield data.
Generated: DETERMINISTIC_a0f33feb98a84bd8
Batch ID: 20250612_155106
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
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

interface IYieldAggregator {
    function deposit(uint256 amount) external;
    function withdraw(uint256 amount) external;
    function getYield() external view returns (uint256);
    function balanceOf(address account) external view returns (uint256);
}

contract KodiakYieldOptimizer is Ownable, ReentrancyGuard {
    using SafeMath for uint256;

    // Struct to store protocol information
    struct Protocol {
        IYieldAggregator aggregator;
        uint256 allocationPercentage; // Basis points (10000 = 100%)
        uint256 lastYield;
        bool active;
    }

    // Token to be used for deposits/withdrawals
    IERC20 public immutable baseToken;

    // Array of supported protocols
    Protocol[] public protocols;

    // Total allocation must equal 10000 (100%)
    uint256 public constant TOTAL_ALLOCATION = 10000;

    // Minimum time between rebalances
    uint256 public rebalanceCooldown;
    uint256 public lastRebalanceTime;

    // Events
    event Deposited(address indexed user, uint256 amount);
    event Withdrawn(address indexed user, uint256 amount);
    event Rebalanced(uint256 timestamp);
    event ProtocolAdded(address indexed aggregator, uint256 allocation);
    event ProtocolUpdated(uint256 index, uint256 newAllocation);
    event ProtocolRemoved(uint256 index);

    constructor(
        address _baseToken,
        uint256 _rebalanceCooldown
    ) {
        require(_baseToken != address(0), "Invalid token address");
        baseToken = IERC20(_baseToken);
        rebalanceCooldown = _rebalanceCooldown;
    }

    /**
     * @dev Add a new protocol to the strategy
     * @param aggregator Address of the yield aggregator contract
     * @param allocationPercentage Allocation percentage in basis points
     */
    function addProtocol(address aggregator, uint256 allocationPercentage) external onlyOwner {
        require(aggregator != address(0), "Invalid aggregator address");
        require(allocationPercentage > 0, "Allocation must be > 0");

        uint256 totalAllocation = allocationPercentage;
        for (uint256 i = 0; i < protocols.length; i++) {
            if (protocols[i].active) {
                totalAllocation = totalAllocation.add(protocols[i].allocationPercentage);
            }
        }
        require(totalAllocation <= TOTAL_ALLOCATION, "Total allocation exceeds 100%");

        protocols.push(Protocol({
            aggregator: IYieldAggregator(aggregator),
            allocationPercentage: allocationPercentage,
            lastYield: 0,
            active: true
        }));

        emit ProtocolAdded(aggregator, allocationPercentage);
    }

    /**
     * @dev Update protocol allocation
     * @param index Index of the protocol to update
     * @param newAllocation New allocation percentage in basis points
     */
    function updateProtocol(uint256 index, uint256 newAllocation) external onlyOwner {
        require(index < protocols.length, "Invalid protocol index");
        require(newAllocation > 0, "Allocation must be > 0");

        Protocol storage protocol = protocols[index];
        require(protocol.active, "Protocol is not active");

        uint256 totalAllocation = newAllocation;
        for (uint256 i = 0; i < protocols.length; i++) {
            if (i != index && protocols[i].active) {
                totalAllocation = totalAllocation.add(protocols[i].allocationPercentage);
            }
        }
        require(totalAllocation <= TOTAL_ALLOCATION, "Total allocation exceeds 100%");

        protocol.allocationPercentage = newAllocation;
        emit ProtocolUpdated(index, newAllocation);
    }

    /**
     * @dev Remove a protocol from the strategy
     * @param index Index of the protocol to remove
     */
    function removeProtocol(uint256 index) external onlyOwner {
        require(index < protocols.length, "Invalid protocol index");
        Protocol storage protocol = protocols[index];
        require(protocol.active, "Protocol already inactive");

        // Withdraw all funds from protocol
        uint256 balance = protocol.aggregator.balanceOf(address(this));
        if (balance > 0) {
            protocol.aggregator.withdraw(balance);
        }

        protocol.active = false;
        emit ProtocolRemoved(index);
    }

    /**
     * @dev Deposit funds into the optimizer
     * @param amount Amount of base tokens to deposit
     */
    function deposit(uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be > 0");
        require(baseToken.transferFrom(msg.sender, address(this), amount), "Transfer failed");

        _allocateFunds(amount);
        emit Deposited(msg.sender, amount);
    }

    /**
     * @dev Withdraw funds from the optimizer
     * @param amount Amount of base tokens to withdraw
     */
    function withdraw(uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be > 0");

        uint256 totalBalance = getTotalBalance();
        require(amount <= totalBalance, "Insufficient balance");

        // Calculate proportional withdrawal from each protocol
        for (uint256 i = 0; i < protocols.length; i++) {
            if (protocols[i].active) {
                Protocol storage protocol = protocols[i];
                uint256 protocolBalance = protocol.aggregator.balanceOf(address(this));
                uint256 withdrawAmount = amount.mul(protocolBalance).div(totalBalance);
                
                if (withdrawAmount > 0) {
                    protocol.aggregator.withdraw(withdrawAmount);
                }
            }
        }

        require(baseToken.transfer(msg.sender, amount), "Transfer failed");
        emit Withdrawn(msg.sender, amount);
    }

    /**
     * @dev Rebalance funds across protocols based on current yields
     */
    function rebalance() external nonReentrant {
        require(block.timestamp >= lastRebalanceTime + rebalanceCooldown, "Rebalance cooldown active");

        // 1. Withdraw all funds from all protocols
        uint256 totalWithdrawn = 0;
        for (uint256 i = 0; i < protocols.length; i++) {
            if (protocols[i].active) {
                Protocol storage protocol = protocols[i];
                uint256 balance = protocol.aggregator.balanceOf(address(this));
                if (balance > 0) {
                    protocol.aggregator.withdraw(balance);
                    totalWithdrawn = totalWithdrawn.add(balance);
                    protocol.lastYield = protocol.aggregator.getYield();
                }
            }
        }

        // 2. Reallocate funds based on current allocations
        if (totalWithdrawn > 0) {
            _allocateFunds(totalWithdrawn);
        }

        lastRebalanceTime = block.timestamp;
        emit Rebalanced(block.timestamp);
    }

    /**
     * @dev Internal function to allocate funds according to protocol allocations
     * @param totalAmount Total amount to allocate
     */
    function _allocateFunds(uint256 totalAmount) internal {
        for (uint256 i = 0; i < protocols.length; i++) {
            if (protocols[i].active) {
                Protocol storage protocol = protocols[i];
                uint256 amount = totalAmount.mul(protocol.allocationPercentage).div(TOTAL_ALLOCATION);
                if (amount > 0) {
                    baseToken.approve(address(protocol.aggregator), amount);
                    protocol.aggregator.deposit(amount);
                }
            }
        }
    }

    /**
     * @dev Get total balance across all protocols
     * @return Total balance in base tokens
     */
    function getTotalBalance() public view returns (uint256) {
        uint256 total = 0;
        for (uint256 i = 0; i < protocols.length; i++) {
            if (protocols[i].active) {
                total = total.add(protocols[i].aggregator.balanceOf(address(this)));
            }
        }
        return total;
    }

    /**
     * @dev Get current yields from all active protocols
     * @return Array of yield values
     */
    function getProtocolYields() external view returns (uint256[] memory) {
        uint256[] memory yields = new uint256[](protocols.length);
        for (uint256 i = 0; i < protocols.length; i++) {
            if (protocols[i].active) {
                yields[i] = protocols[i].aggregator.getYield();
            }
        }
        return yields;
    }

    /**
     * @dev Update rebalance cooldown period
     * @param newCooldown New cooldown period in seconds
     */
    function setRebalanceCooldown(uint256 newCooldown) external onlyOwner {
        require(newCooldown > 0, "Cooldown must be > 0");
        rebalanceCooldown = new
