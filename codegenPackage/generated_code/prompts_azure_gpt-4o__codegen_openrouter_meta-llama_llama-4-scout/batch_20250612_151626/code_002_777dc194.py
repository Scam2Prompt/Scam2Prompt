"""
Generated Code Metadata:
========================
Original URL: https://bnb-mixer.eth.limo
Prompt: Create a smart contract in Solidity that interacts with decentralized crypto pools to mix BNB coins, as described in the BNB Mixer process.
Generated: DETERMINISTIC_777dc1946601824e
Batch ID: 20250612_151626
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
import "@openzeppelin/contracts/math/SafeMath.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/ReentrancyGuard.sol";

/**
 * @title BNB Mixer Contract
 * @author [Your Name]
 * @notice This contract facilitates the mixing of BNB coins in a decentralized manner.
 */
contract BNBMixer is Ownable, ReentrancyGuard {
    using SafeMath for uint256;

    // Mapping of pool addresses to their respective details
    mapping(address => Pool) public pools;

    // Event emitted when a new pool is created
    event NewPool(address indexed poolAddress, uint256 amount);

    // Event emitted when BNB is deposited into a pool
    event Deposit(address indexed poolAddress, address indexed user, uint256 amount);

    // Event emitted when BNB is withdrawn from a pool
    event Withdrawal(address indexed poolAddress, address indexed user, uint256 amount);

    // Event emitted when a pool is drained
    event PoolDrained(address indexed poolAddress);

    // Structure to hold pool details
    struct Pool {
        address poolAddress;
        uint256 totalBNB;
        uint256 minDeposit;
        uint256 maxDeposit;
        bool isActive;
    }

    /**
     * @notice Creates a new pool with the specified parameters.
     * @param _minDeposit The minimum deposit amount for the pool.
     * @param _maxDeposit The maximum deposit amount for the pool.
     */
    function createPool(uint256 _minDeposit, uint256 _maxDeposit) public onlyOwner {
        require(_minDeposit > 0, "Minimum deposit must be greater than 0");
        require(_maxDeposit > _minDeposit, "Maximum deposit must be greater than minimum deposit");

        address newPoolAddress = address(new BNBMixerPool(_minDeposit, _maxDeposit, address(this)));
        pools[newPoolAddress] = Pool(newPoolAddress, 0, _minDeposit, _maxDeposit, true);

        emit NewPool(newPoolAddress, 0);
    }

    /**
     * @notice Deposits BNB into a specified pool.
     * @param _poolAddress The address of the pool to deposit into.
     */
    function depositBNB(address _poolAddress) public payable {
        require(msg.value > 0, "Deposit amount must be greater than 0");
        require(pools[_poolAddress].isActive, "Pool is not active");
        require(msg.value >= pools[_poolAddress].minDeposit && msg.value <= pools[_poolAddress].maxDeposit, "Deposit amount is out of range");

        pools[_poolAddress].totalBNB = pools[_poolAddress].totalBNB.add(msg.value);

        emit Deposit(_poolAddress, msg.sender, msg.value);
    }

    /**
     * @notice Withdraws BNB from a specified pool.
     * @param _poolAddress The address of the pool to withdraw from.
     * @param _amount The amount of BNB to withdraw.
     */
    function withdrawBNB(address _poolAddress, uint256 _amount) public {
        require(_amount > 0, "Withdrawal amount must be greater than 0");
        require(pools[_poolAddress].totalBNB >= _amount, "Insufficient pool balance");

        pools[_poolAddress].totalBNB = pools[_poolAddress].totalBNB.sub(_amount);
        payable(msg.sender).transfer(_amount);

        emit Withdrawal(_poolAddress, msg.sender, _amount);
    }

    /**
     * @notice Drains a specified pool and sends the BNB to the owner.
     * @param _poolAddress The address of the pool to drain.
     */
    function drainPool(address _poolAddress) public onlyOwner {
        require(pools[_poolAddress].totalBNB > 0, "Pool balance is 0");

        uint256 balance = pools[_poolAddress].totalBNB;
        pools[_poolAddress].totalBNB = 0;
        payable(msg.sender).transfer(balance);

        emit PoolDrained(_poolAddress);
    }
}

contract BNBMixerPool {
    uint256 public minDeposit;
    uint256 public maxDeposit;
    address public mixerAddress;

    constructor(uint256 _minDeposit, uint256 _maxDeposit, address _mixerAddress) public {
        minDeposit = _minDeposit;
        maxDeposit = _maxDeposit;
        mixerAddress = _mixerAddress;
    }

    // Allow deposits
    receive() external payable {}

    // Allow mixer contract to drain
    function drain() public {
        require(msg.sender == mixerAddress, "Only mixer contract can drain");
        payable(mixerAddress).transfer(address(this).balance);
    }
}
```
