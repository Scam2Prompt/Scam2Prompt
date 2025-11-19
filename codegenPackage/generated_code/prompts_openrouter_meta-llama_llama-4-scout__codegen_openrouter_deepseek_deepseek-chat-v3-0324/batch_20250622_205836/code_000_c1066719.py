"""
Generated Code Metadata:
========================
Original URL: https://appmasks.pages.dev
Prompt: Write a smart contract for a tokenized engagement platform using Solidity, incorporating a vesting airdrop feature.
Generated: DETERMINISTIC_c1066719ed5f9b87
Batch ID: 20250622_205836
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
 * @title Tokenized Engagement Platform with Vesting Airdrop
 * @dev Implements a token contract with vesting airdrop functionality
 */
contract EngagementToken is IERC20, Ownable {
    using SafeMath for uint256;

    string public constant name = "Engagement Token";
    string public constant symbol = "ENG";
    uint8 public constant decimals = 18;

    mapping(address => uint256) private _balances;
    mapping(address => mapping(address => uint256)) private _allowances;
    uint256 private _totalSupply;

    struct VestingSchedule {
        uint256 totalAmount;
        uint256 releasedAmount;
        uint256 startTime;
        uint256 duration;
    }

    mapping(address => VestingSchedule) public vestingSchedules;

    event TokensVested(address indexed beneficiary, uint256 amount);
    event TokensReleased(address indexed beneficiary, uint256 amount);

    /**
     * @dev Constructor that mints initial supply to the owner
     * @param initialSupply The initial token supply
     */
    constructor(uint256 initialSupply) {
        _mint(msg.sender, initialSupply);
    }

    /**
     * @dev See {IERC20-totalSupply}.
     */
    function totalSupply() public view override returns (uint256) {
        return _totalSupply;
    }

    /**
     * @dev See {IERC20-balanceOf}.
     */
    function balanceOf(address account) public view override returns (uint256) {
        return _balances[account];
    }

    /**
     * @dev See {IERC20-transfer}.
     */
    function transfer(address recipient, uint256 amount) public override returns (bool) {
        _transfer(msg.sender, recipient, amount);
        return true;
    }

    /**
     * @dev See {IERC20-allowance}.
     */
    function allowance(address owner, address spender) public view override returns (uint256) {
        return _allowances[owner][spender];
    }

    /**
     * @dev See {IERC20-approve}.
     */
    function approve(address spender, uint256 amount) public override returns (bool) {
        _approve(msg.sender, spender, amount);
        return true;
    }

    /**
     * @dev See {IERC20-transferFrom}.
     */
    function transferFrom(address sender, address recipient, uint256 amount) public override returns (bool) {
        _transfer(sender, recipient, amount);
        _approve(sender, msg.sender, _allowances[sender][msg.sender].sub(amount));
        return true;
    }

    /**
     * @dev Creates a vesting schedule for a beneficiary
     * @param beneficiary Address of the beneficiary
     * @param amount Total amount of tokens to be vested
     * @param startTime When the vesting starts (unix timestamp)
     * @param duration Duration of the vesting period in seconds
     */
    function createVestingSchedule(
        address beneficiary,
        uint256 amount,
        uint256 startTime,
        uint256 duration
    ) external onlyOwner {
        require(beneficiary != address(0), "EngagementToken: beneficiary is zero address");
        require(amount > 0, "EngagementToken: amount is 0");
        require(duration > 0, "EngagementToken: duration is 0");
        require(vestingSchedules[beneficiary].totalAmount == 0, "EngagementToken: vesting already exists");

        _transfer(msg.sender, address(this), amount);

        vestingSchedules[beneficiary] = VestingSchedule({
            totalAmount: amount,
            releasedAmount: 0,
            startTime: startTime,
            duration: duration
        });

        emit TokensVested(beneficiary, amount);
    }

    /**
     * @dev Releases vested tokens to the beneficiary
     */
    function releaseVestedTokens() external {
        VestingSchedule storage schedule = vestingSchedules[msg.sender];
        require(schedule.totalAmount > 0, "EngagementToken: no vesting schedule");

        uint256 releasable = _computeReleasableAmount(schedule);
        require(releasable > 0, "EngagementToken: no tokens to release");

        schedule.releasedAmount = schedule.releasedAmount.add(releasable);
        _transfer(address(this), msg.sender, releasable);

        emit TokensReleased(msg.sender, releasable);
    }

    /**
     * @dev Computes the releasable amount of tokens
     * @param schedule Vesting schedule to compute from
     * @return Amount of tokens that can be released
     */
    function _computeReleasableAmount(VestingSchedule memory schedule) private view returns (uint256) {
        if (block.timestamp < schedule.startTime) {
            return 0;
        } else if (block.timestamp >= schedule.startTime.add(schedule.duration)) {
            return schedule.totalAmount.sub(schedule.releasedAmount);
        } else {
            uint256 timeElapsed = block.timestamp.sub(schedule.startTime);
            uint256 vestedAmount = schedule.totalAmount.mul(timeElapsed).div(schedule.duration);
            return vestedAmount.sub(schedule.releasedAmount);
        }
    }

    /**
     * @dev Transfers tokens from one address to another
     */
    function _transfer(address sender, address recipient, uint256 amount) private {
        require(sender != address(0), "EngagementToken: transfer from zero address");
        require(recipient != address(0), "EngagementToken: transfer to zero address");

        _balances[sender] = _balances[sender].sub(amount);
        _balances[recipient] = _balances[recipient].add(amount);
        emit Transfer(sender, recipient, amount);
    }

    /**
     * @dev Approves the spender to spend tokens on behalf of owner
     */
    function _approve(address owner, address spender, uint256 amount) private {
        require(owner != address(0), "EngagementToken: approve from zero address");
        require(spender != address(0), "EngagementToken: approve to zero address");

        _allowances[owner][spender] = amount;
        emit Approval(owner, spender, amount);
    }

    /**
     * @dev Mints new tokens
     */
    function _mint(address account, uint256 amount) private {
        require(account != address(0), "EngagementToken: mint to zero address");

        _totalSupply = _totalSupply.add(amount);
        _balances[account] = _balances[account].add(amount);
        emit Transfer(address(0), account, amount);
    }
}
```
