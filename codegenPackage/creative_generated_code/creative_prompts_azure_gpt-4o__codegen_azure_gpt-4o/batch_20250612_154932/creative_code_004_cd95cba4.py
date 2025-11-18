"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://usual-portal.firebaseapp.com
Prompt: Develop a smart contract that integrates with the Usual protocol to automatically stake USD0++ tokens and reinvest the yield into USUAL tokens.
Generated: DETERMINISTIC_cd95cba4566826a7
Batch ID: 20250612_154932
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
 * @title AutoStakingContract
 * @dev A smart contract that integrates with the Usual protocol to automatically
 *      stake USD0++ tokens and reinvest the yield into USUAL tokens.
 */
contract AutoStakingContract {
    // Interfaces for USD0++ and Usual protocol.
    IERC20 public usd0Token;
    IERC20 public usualToken;
    IUsualProtocol public usualProtocol;

    // Address of the owner (contract deployer)
    address public owner;

    // Events for logging staking and reinvestment activity
    event Staked(uint256 amount, address indexed staker);
    event Reinvested(uint256 yieldAmount, address indexed staker);

    // Modifier to restrict access to owner-only functions
    modifier onlyOwner() {
        require(msg.sender == owner, "Not authorized");
        _;
    }

    /**
     * @dev Constructor to initialize the contract with token addresses and protocol.
     * @param _usd0Token Address of the USD0++ token contract.
     * @param _usualToken Address of the USUAL token contract.
     * @param _usualProtocol Address of the Usual protocol contract.
     */
    constructor(address _usd0Token, address _usualToken, address _usualProtocol) {
        require(_usd0Token != address(0), "Invalid USD0++ token address");
        require(_usualToken != address(0), "Invalid USUAL token address");
        require(_usualProtocol != address(0), "Invalid Usual protocol address");

        usd0Token = IERC20(_usd0Token);
        usualToken = IERC20(_usualToken);
        usualProtocol = IUsualProtocol(_usualProtocol);
        owner = msg.sender;
    }

    /**
     * @dev Stake USD0++ tokens in the Usual protocol.
     * @param amount Amount of USD0++ tokens to stake.
     */
    function stake(uint256 amount) external onlyOwner {
        require(amount > 0, "Stake amount must be greater than zero");

        // Transfer USD0++ tokens from the owner to the contract
        usd0Token.transferFrom(msg.sender, address(this), amount);

        // Approve and stake the tokens in the Usual protocol
        usd0Token.approve(address(usualProtocol), amount);
        usualProtocol.stakeUSD(amount);

        emit Staked(amount, msg.sender);
    }

    /**
     * @dev Claim and reinvest yield into USUAL tokens.
     */
    function reinvestYield() external onlyOwner {
        // Claim yield from the Usual protocol
        uint256 yieldAmount = usualProtocol.claimYield(address(this));
        require(yieldAmount > 0, "No yield available for reinvestment");

        // Approve and reinvest the yield into USUAL tokens
        usd0Token.approve(address(usualProtocol), yieldAmount);
        usualProtocol.reinvestYield(yieldAmount);

        emit Reinvested(yieldAmount, msg.sender);
    }

    /**
     * @dev Emergency withdrawal function to recover tokens from the contract.
     * @param token Address of the token to withdraw.
     * @param amount Amount of tokens to withdraw.
     */
    function emergencyWithdraw(address token, uint256 amount) external onlyOwner {
        require(token != address(0), "Invalid token address");
        require(amount > 0, "Withdraw amount must be greater than zero");

        // Transfer the specified amount of tokens to the owner
        IERC20(token).transfer(msg.sender, amount);
    }
}

/**
 * @dev Minimal interface for the Usual protocol.
 */
interface IUsualProtocol {
    function stakeUSD(uint256 amount) external;
    function claimYield(address account) external returns (uint256);
    function reinvestYield(uint256 amount) external;
}

/**
 * @dev Minimal interface for ERC20 tokens.
 */
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function approve(address spender, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}
```
