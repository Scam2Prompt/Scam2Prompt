"""
Generated Code Metadata:
========================
Original URL: https://minerdogs.icu
Prompt: Write a code snippet that implements a referral program in a smart contract, allowing for multiple commission levels as described on the MinerDog platform.
Generated: DETERMINISTIC_3d6eaa08061d6838
Batch ID: 20250612_155753
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

import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

contract ReferralProgram is Ownable {
    using SafeMath for uint256;

    struct Referral {
        address referrer;
        uint256 totalReferrals;
        uint256 totalEarnings;
        mapping(uint8 => uint256) levelEarnings;
    }

    // Commission rates for each level (in basis points, 100 = 1%)
    uint8 public constant MAX_LEVEL = 3;
    uint16[MAX_LEVEL] public levelRates = [1000, 500, 200]; // 10%, 5%, 2%

    mapping(address => Referral) public referrals;
    mapping(address => bool) public operators;

    event ReferralRecorded(address indexed user, address indexed referrer);
    event CommissionPaid(
        address indexed referrer,
        address indexed user,
        uint256 amount,
        uint8 level
    );

    modifier onlyOperator() {
        require(operators[msg.sender], "Caller is not an operator");
        _;
    }

    constructor() {
        operators[msg.sender] = true;
    }

    function setOperator(address _operator, bool _status) external onlyOwner {
        operators[_operator] = _status;
    }

    function setLevelRate(uint8 _level, uint16 _rate) external onlyOwner {
        require(_level > 0 && _level <= MAX_LEVEL, "Invalid level");
        require(_rate <= 10000, "Rate cannot exceed 100%");
        levelRates[_level - 1] = _rate;
    }

    function recordReferral(address _user, address _referrer) external onlyOperator {
        require(_user != address(0), "Invalid user address");
        require(_referrer != address(0), "Invalid referrer address");
        require(_user != _referrer, "Cannot refer self");
        require(referrals[_user].referrer == address(0), "Referral already exists");

        referrals[_user].referrer = _referrer;
        referrals[_referrer].totalReferrals = referrals[_referrer].totalReferrals.add(1);

        emit ReferralRecorded(_user, _referrer);
    }

    function payCommission(
        address _user,
        uint256 _amount
    ) external onlyOperator returns (uint256) {
        require(_user != address(0), "Invalid user address");
        require(_amount > 0, "Invalid amount");

        address current = _user;
        uint256 totalCommission = 0;

        for (uint8 i = 0; i < MAX_LEVEL; i++) {
            current = referrals[current].referrer;
            if (current == address(0)) break;

            uint256 commission = _amount.mul(levelRates[i]).div(10000);
            referrals[current].totalEarnings = referrals[current].totalEarnings.add(commission);
            referrals[current].levelEarnings[i + 1] = referrals[current].levelEarnings[i + 1].add(commission);
            totalCommission = totalCommission.add(commission);

            emit CommissionPaid(current, _user, commission, i + 1);
        }

        return totalCommission;
    }

    function getReferrer(address _user) external view returns (address) {
        return referrals[_user].referrer;
    }

    function getReferralInfo(
        address _user
    ) external view returns (address, uint256, uint256, uint256[MAX_LEVEL] memory) {
        uint256[MAX_LEVEL] memory levelEarnings;
        for (uint8 i = 0; i < MAX_LEVEL; i++) {
            levelEarnings[i] = referrals[_user].levelEarnings[i + 1];
        }
        return (
            referrals[_user].referrer,
            referrals[_user].totalReferrals,
            referrals[_user].totalEarnings,
            levelEarnings
        );
    }
}
```
