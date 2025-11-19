"""
Generated Code Metadata:
========================
Original URL: https://crudoprotocol-io.web.app
Prompt: "Develop a Solidity smart contract code for the CRUDO token, including its utility, tokenomics, and distribution phases as described in the Crudo Protocol's whitepaper."
Generated: DETERMINISTIC_3c470dcd9f62480f
Batch ID: 20250622_204837
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

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/token/ERC20/extensions/ERC20Burnable.sol";
import "@openzeppelin/contracts/token/ERC20/extensions/ERC20Snapshot.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/Pausable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title CRUDO Token Contract
 * @dev Implements the CRUDO token with utility functions, tokenomics, and distribution phases
 */
contract CRUDOToken is ERC20, ERC20Burnable, ERC20Snapshot, Ownable, Pausable {
    using SafeMath for uint256;

    // Token distribution phases
    enum DistributionPhase {
        PrivateSale,
        PublicSale,
        Team,
        Advisors,
        Ecosystem,
        Reserve
    }

    // Token allocation percentages (in basis points)
    uint256 public constant PRIVATE_SALE_ALLOCATION = 1500; // 15%
    uint256 public constant PUBLIC_SALE_ALLOCATION = 2500; // 25%
    uint256 public constant TEAM_ALLOCATION = 2000; // 20%
    uint256 public constant ADVISORS_ALLOCATION = 1000; // 10%
    uint256 public constant ECOSYSTEM_ALLOCATION = 2000; // 20%
    uint256 public constant RESERVE_ALLOCATION = 1000; // 10%

    // Vesting schedules
    struct VestingSchedule {
        uint256 startTime;
        uint256 cliff;
        uint256 duration;
        uint256 totalAmount;
        uint256 releasedAmount;
    }

    // Total supply: 1 billion tokens with 18 decimals
    uint256 private constant TOTAL_SUPPLY = 1_000_000_000 * 10**18;

    // Distribution addresses
    address public privateSaleWallet;
    address public publicSaleWallet;
    address public teamWallet;
    address public advisorsWallet;
    address public ecosystemWallet;
    address public reserveWallet;

    // Vesting schedules mapping
    mapping(address => VestingSchedule) public vestingSchedules;

    // Phase allocation tracking
    mapping(DistributionPhase => uint256) public distributedAmounts;

    // Events
    event TokensDistributed(DistributionPhase phase, address recipient, uint256 amount);
    event VestingScheduleCreated(address beneficiary, uint256 startTime, uint256 cliff, uint256 duration, uint256 amount);
    event TokensReleased(address beneficiary, uint256 amount);

    /**
     * @dev Constructor that initializes the token distribution
     */
    constructor(
        address _privateSaleWallet,
        address _publicSaleWallet,
        address _teamWallet,
        address _advisorsWallet,
        address _ecosystemWallet,
        address _reserveWallet
    ) ERC20("CRUDO Token", "CRUDO") {
        require(_privateSaleWallet != address(0), "Invalid private sale wallet");
        require(_publicSaleWallet != address(0), "Invalid public sale wallet");
        require(_teamWallet != address(0), "Invalid team wallet");
        require(_advisorsWallet != address(0), "Invalid advisors wallet");
        require(_ecosystemWallet != address(0), "Invalid ecosystem wallet");
        require(_reserveWallet != address(0), "Invalid reserve wallet");

        privateSaleWallet = _privateSaleWallet;
        publicSaleWallet = _publicSaleWallet;
        teamWallet = _teamWallet;
        advisorsWallet = _advisorsWallet;
        ecosystemWallet = _ecosystemWallet;
        reserveWallet = _reserveWallet;

        // Mint total supply to contract
        _mint(address(this), TOTAL_SUPPLY);

        // Distribute initial allocations
        _distributeInitialTokens();
    }

    /**
     * @dev Distributes initial token allocations according to tokenomics
     */
    function _distributeInitialTokens() private {
        uint256 privateSaleAmount = TOTAL_SUPPLY.mul(PRIVATE_SALE_ALLOCATION).div(10000);
        uint256 publicSaleAmount = TOTAL_SUPPLY.mul(PUBLIC_SALE_ALLOCATION).div(10000);
        uint256 ecosystemAmount = TOTAL_SUPPLY.mul(ECOSYSTEM_ALLOCATION).div(10000);
        uint256 reserveAmount = TOTAL_SUPPLY.mul(RESERVE_ALLOCATION).div(10000);

        // Transfer immediately distributable tokens
        _transfer(address(this), privateSaleWallet, privateSaleAmount);
        _transfer(address(this), publicSaleWallet, publicSaleAmount);
        _transfer(address(this), ecosystemWallet, ecosystemAmount);
        _transfer(address(this), reserveWallet, reserveAmount);

        // Set up vesting for team and advisors
        uint256 teamAmount = TOTAL_SUPPLY.mul(TEAM_ALLOCATION).div(10000);
        uint256 advisorsAmount = TOTAL_SUPPLY.mul(ADVISORS_ALLOCATION).div(10000);

        // Team vesting: 12 month cliff, 36 month duration
        _createVestingSchedule(teamWallet, block.timestamp, 365 days, 1095 days, teamAmount);
        
        // Advisors vesting: 6 month cliff, 24 month duration
        _createVestingSchedule(advisorsWallet, block.timestamp, 180 days, 730 days, advisorsAmount);

        // Update distributed amounts
        distributedAmounts[DistributionPhase.PrivateSale] = privateSaleAmount;
        distributedAmounts[DistributionPhase.PublicSale] = publicSaleAmount;
        distributedAmounts[DistributionPhase.Team] = teamAmount;
        distributedAmounts[DistributionPhase.Advisors] = advisorsAmount;
        distributedAmounts[DistributionPhase.Ecosystem] = ecosystemAmount;
        distributedAmounts[DistributionPhase.Reserve] = reserveAmount;

        emit TokensDistributed(DistributionPhase.PrivateSale, privateSaleWallet, privateSaleAmount);
        emit TokensDistributed(DistributionPhase.PublicSale, publicSaleWallet, publicSaleAmount);
        emit TokensDistributed(DistributionPhase.Ecosystem, ecosystemWallet, ecosystemAmount);
        emit TokensDistributed(DistributionPhase.Reserve, reserveWallet, reserveAmount);
    }

    /**
     * @dev Creates a new vesting schedule for a beneficiary
     */
    function _createVestingSchedule(
        address beneficiary,
        uint256 startTime,
        uint256 cliff,
        uint256 duration,
        uint256 amount
    ) private {
        require(beneficiary != address(0), "Invalid beneficiary address");
        require(cliff <= duration, "Cliff must be less than or equal to duration");
        require(amount > 0, "Amount must be greater than 0");
        require(vestingSchedules[beneficiary].totalAmount == 0, "Vesting schedule already exists");

        vestingSchedules[beneficiary] = VestingSchedule({
            startTime: startTime,
            cliff: startTime.add(cliff),
            duration: duration,
            totalAmount: amount,
            releasedAmount: 0
        });

        emit VestingScheduleCreated(beneficiary, startTime, cliff, duration, amount);
    }

    /**
     * @dev Releases vested tokens to the beneficiary
     */
    function releaseVestedTokens(address beneficiary) external whenNotPaused {
        VestingSchedule storage schedule = vestingSchedules[beneficiary];
        require(schedule.totalAmount > 0, "No vesting schedule found");

        uint256 unreleased = _releasableAmount(schedule);
        require(unreleased > 0, "No tokens to release");

        schedule.releasedAmount = schedule.releasedAmount.add(unreleased);
        _transfer(address(this), beneficiary, unreleased);

        emit TokensReleased(beneficiary, unreleased);
    }

    /**
     * @dev Calculates the releasable amount of tokens
     */
    function _releasableAmount(VestingSchedule memory schedule) private view returns (uint256) {
        if (block.timestamp < schedule.cliff) {
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
     * @dev Returns the releasable amount for a beneficiary
     */
    function releasableAmount(address beneficiary) public view returns (uint256) {
        return _releasableAmount(vestingSchedules[beneficiary]);
    }

    /**
     * @dev Creates a snapshot of token balances
     */
    function snapshot() public onlyOwner {
        _snapshot();
    }

    /**
     * @dev Pauses all token transfers
     */
    function pause() public onlyOwner {
        _pause();
    }

    /**
     * @dev Unpauses
