"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.qbt.finance
Prompt: Generate a smart contract in Solidity that integrates with Qubit Finance to automatically supply BUSD and claim rewards based on the "Supply APR" and "Reward APR" values.
Generated: DETERMINISTIC_c9809ed3f5cbb31f
Batch ID: 20250612_154207
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

// Import interfaces for Qubit Finance protocols
interface IQubitToken {
    function balanceOf(address account) external view returns (uint256);
    function claimRewards() external;
}

interface IQubitFinance {
    function supply(address token, uint256 amount) external;
}

interface IERC20 {
    function transferFrom(address from, address to, uint256 value) external returns (bool);
    function approve(address spender, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}

contract AutoSupplyAndClaim {
    // Address of the Qubit Finance supply contract
    address public immutable qubitFinanceContract;

    // Address of the Qubit reward token (QBT)
    address public immutable qubitRewardToken;

    // Address of the BUSD token
    address public immutable busdToken;

    // Owner of the contract
    address public immutable owner;

    // Event emitted when BUSD is supplied
    event BUSDsupplied(uint256 amount);

    // Event emitted when rewards are claimed
    event RewardsClaimed(uint256 amount);

    // Modifier to restrict access to the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Not the contract owner");
        _;
    }

    /**
     * @dev Constructor to initialize the contract with necessary addresses.
     * @param _qubitFinanceContract Address of the Qubit Finance supply contract.
     * @param _qubitRewardToken Address of the QBT token contract.
     * @param _busdToken Address of the BUSD token contract.
     */
    constructor(
        address _qubitFinanceContract,
        address _qubitRewardToken,
        address _busdToken
    ) {
        require(
            _qubitFinanceContract != address(0) &&
            _qubitRewardToken != address(0) &&
            _busdToken != address(0),
            "Invalid address provided"
        );

        qubitFinanceContract = _qubitFinanceContract;
        qubitRewardToken = _qubitRewardToken;
        busdToken = _busdToken;
        owner = msg.sender;
    }

    /**
     * @dev Supplies BUSD to Qubit Finance for earning Supply APR.
     * @param _amount Amount of BUSD to supply.
     */
    function supplyBUSD(uint256 _amount) external onlyOwner {
        require(_amount > 0, "Amount must be greater than zero");

        // Transfer BUSD from owner to this contract
        require(
            IERC20(busdToken).transferFrom(msg.sender, address(this), _amount),
            "BUSD transfer failed"
        );

        // Approve the Qubit Finance contract to spend BUSD
        require(
            IERC20(busdToken).approve(qubitFinanceContract, _amount),
            "Approval failed"
        );

        // Supply BUSD to Qubit Finance
        IQubitFinance(qubitFinanceContract).supply(busdToken, _amount);

        emit BUSDsupplied(_amount);
    }

    /**
     * @dev Claims rewards (QBT tokens) from Qubit Finance based on Reward APR.
     */
    function claimRewards() external onlyOwner {
        // Claim rewards from Qubit Finance
        IQubitToken(qubitRewardToken).claimRewards();

        // Get the balance of QBT tokens after claiming
        uint256 rewardsBalance = IERC20(qubitRewardToken).balanceOf(address(this));
        require(rewardsBalance > 0, "No rewards available to claim");

        // Transfer claimed rewards to the owner
        require(
            IERC20(qubitRewardToken).transferFrom(address(this), owner, rewardsBalance),
            "Reward transfer failed"
        );

        emit RewardsClaimed(rewardsBalance);
    }

    /**
     * @dev Fallback function for receiving BNB (if required by Qubit Finance).
     */
    receive() external payable {}

    /**
     * @dev Function to withdraw any accidentally sent funds (BNB or other tokens).
     * @param _token Address of the token to withdraw, or address(0) for BNB.
     */
    function rescueFunds(address _token) external onlyOwner {
        if (_token == address(0)) {
            // Withdraw BNB
            payable(owner).transfer(address(this).balance);
        } else {
            // Withdraw ERC20 tokens
            uint256 balance = IERC20(_token).balanceOf(address(this));
            require(balance > 0, "No token balance available");
            IERC20(_token).transfer(owner, balance);
        }
    }
}
```
