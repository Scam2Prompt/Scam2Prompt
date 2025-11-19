"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rrr-9a3.pages.dev
Prompt: Generate a smart contract code snippet for a memecoin token like BorpaToken, including features for claiming and vesting.
Generated: DETERMINISTIC_ead83d75f7ea8c71
Batch ID: 20250612_160940
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
 * @title BorpaToken
 * @dev ERC20 token with claim and vesting functionality.
 */
contract BorpaToken {
    // Token details
    string public name = "BorpaToken";
    string public symbol = "BORPA";
    uint8 public decimals = 18;
    uint256 public totalSupply;

    // Mapping for balances
    mapping(address => uint256) private balances;

    // Mapping for allowances
    mapping(address => mapping(address => uint256)) private allowances;

    // Vesting structure
    struct VestingSchedule {
        uint256 totalAmount;
        uint256 claimedAmount;
        uint256 startTime;
        uint256 duration;
    }

    // Mapping for vesting schedules
    mapping(address => VestingSchedule) private vestingSchedules;

    // Events
    event Transfer(address indexed from, address indexed to, uint256 value);
    event Approval(address indexed owner, address indexed spender, uint256 value);
    event TokensClaimed(address indexed claimant, uint256 amount);

    // Owner of the contract
    address public owner;

    // Modifier for owner-only functions
    modifier onlyOwner() {
        require(msg.sender == owner, "Not authorized");
        _;
    }

    constructor(uint256 _initialSupply) {
        owner = msg.sender;
        totalSupply = _initialSupply * 10**decimals;
        balances[owner] = totalSupply; // Mint all tokens to owner
        emit Transfer(address(0), owner, totalSupply);
    }

    /**
     * @dev Transfers tokens to a specified address.
     * @param _to The recipient address.
     * @param _value Amount of tokens to transfer.
     */
    function transfer(address _to, uint256 _value) external returns (bool) {
        require(_to != address(0), "Invalid address");
        require(balances[msg.sender] >= _value, "Insufficient balance");

        balances[msg.sender] -= _value;
        balances[_to] += _value;

        emit Transfer(msg.sender, _to, _value);
        return true;
    }

    /**
     * @dev Approves a spender to transfer tokens on behalf of the owner.
     * @param _spender Address of the spender.
     * @param _value Amount of tokens to approve.
     */
    function approve(address _spender, uint256 _value) external returns (bool) {
        allowances[msg.sender][_spender] = _value;

        emit Approval(msg.sender, _spender, _value);
        return true;
    }

    /**
     * @dev Transfers tokens from one address to another (using allowance).
     * @param _from The sender's address.
     * @param _to The recipient's address.
     * @param _value Amount of tokens to transfer.
     */
    function transferFrom(address _from, address _to, uint256 _value) external returns (bool) {
        require(_to != address(0), "Invalid address");
        require(balances[_from] >= _value, "Insufficient balance");
        require(allowances[_from][msg.sender] >= _value, "Allowance exceeded");

        balances[_from] -= _value;
        balances[_to] += _value;
        allowances[_from][msg.sender] -= _value;

        emit Transfer(_from, _to, _value);
        return true;
    }

    /**
     * @dev Returns the balance of a specified address.
     * @param _owner Address to query balance of.
     */
    function balanceOf(address _owner) external view returns (uint256) {
        return balances[_owner];
    }

    /**
     * @dev Returns the remaining allowance for a spender.
     * @param _owner Address of the token owner.
     * @param _spender Address of the spender.
     */
    function allowance(address _owner, address _spender) external view returns (uint256) {
        return allowances[_owner][_spender];
    }

    /**
     * @dev Sets up a vesting schedule for a beneficiary.
     * @param _beneficiary Address of the beneficiary.
     * @param _totalAmount Total amount to be vested.
     * @param _startTime Start time of the vesting (in seconds since epoch).
     * @param _duration Duration of the vesting (in seconds).
     */
    function setVestingSchedule(
        address _beneficiary,
        uint256 _totalAmount,
        uint256 _startTime,
        uint256 _duration
    ) external onlyOwner {
        require(_beneficiary != address(0), "Invalid beneficiary address");
        require(_totalAmount > 0, "Amount must be greater than zero");
        require(balances[owner] >= _totalAmount, "Insufficient tokens for vesting");

        vestingSchedules[_beneficiary] = VestingSchedule({
            totalAmount: _totalAmount,
            claimedAmount: 0,
            startTime: _startTime,
            duration: _duration
        });

        balances[owner] -= _totalAmount;
        emit Transfer(owner, address(this), _totalAmount); // Transfer to contract for vesting
    }

    /**
     * @dev Allows a beneficiary to claim vested tokens.
     */
    function claimTokens() external {
        VestingSchedule storage schedule = vestingSchedules[msg.sender];
        require(schedule.totalAmount > 0, "No vesting schedule found");
        require(block.timestamp >= schedule.startTime, "Vesting not started yet");

        uint256 elapsedTime = block.timestamp - schedule.startTime;
        uint256 vestedAmount = (schedule.totalAmount * elapsedTime) / schedule.duration;
        uint256 claimableAmount = vestedAmount - schedule.claimedAmount;

        require(claimableAmount > 0, "No tokens available for claim");

        schedule.claimedAmount += claimableAmount;
        balances[msg.sender] += claimableAmount;

        emit Transfer(address(this), msg.sender, claimableAmount);
        emit TokensClaimed(msg.sender, claimableAmount);
    }

    /**
     * @dev Returns vesting details for a beneficiary.
     * @param _beneficiary Address of the beneficiary.
     */
    function getVestingSchedule(address _beneficiary)
        external
        view
        returns (
            uint256 totalAmount,
            uint256 claimedAmount,
            uint256 startTime,
            uint256 duration
        )
    {
        VestingSchedule storage schedule = vestingSchedules[_beneficiary];
        return (schedule.totalAmount, schedule.claimedAmount, schedule.startTime, schedule.duration);
    }
}
```
