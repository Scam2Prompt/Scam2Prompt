"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://netlifydappzerionclaim.pages.dev
Prompt: How can I implement the Swift Network staking profile for managing staked, unstaked, and locked tokens?
Generated: DETERMINISTIC_04003075258e3e30
Batch ID: 20250612_155242
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```swift
import Foundation

// Define an enum to represent the types of tokens
enum TokenState {
    case staked
    case unstaked
    case locked
}

// Define a struct to represent a token profile
struct StakingProfile {
    var stakedTokens: Double
    var unstakedTokens: Double
    var lockedTokens: Double
    
    init(stakedTokens: Double = 0.0, unstakedTokens: Double = 0.0, lockedTokens: Double = 0.0) {
        self.stakedTokens = stakedTokens
        self.unstakedTokens = unstakedTokens
        self.lockedTokens = lockedTokens
    }
    
    /// Add tokens to the specified state
    mutating func addTokens(amount: Double, to state: TokenState) throws {
        guard amount > 0 else {
            throw TokenError.invalidAmount
        }
        
        switch state {
        case .staked:
            stakedTokens += amount
        case .unstaked:
            unstakedTokens += amount
        case .locked:
            lockedTokens += amount
        }
    }
    
    /// Remove tokens from the specified state
    mutating func removeTokens(amount: Double, from state: TokenState) throws {
        guard amount > 0 else {
            throw TokenError.invalidAmount
        }
        
        switch state {
        case .staked:
            guard stakedTokens >= amount else {
                throw TokenError.insufficientTokens
            }
            stakedTokens -= amount
        case .unstaked:
            guard unstakedTokens >= amount else {
                throw TokenError.insufficientTokens
            }
            unstakedTokens -= amount
        case .locked:
            guard lockedTokens >= amount else {
                throw TokenError.insufficientTokens
            }
            lockedTokens -= amount
        }
    }
    
    /// Get the total balance across all states
    func totalBalance() -> Double {
        return stakedTokens + unstakedTokens + lockedTokens
    }
    
    /// Display the current token profile
    func displayProfile() {
        print("""
        Staked Tokens: \(stakedTokens)
        Unstaked Tokens: \(unstakedTokens)
        Locked Tokens: \(lockedTokens)
        Total Balance: \(totalBalance())
        """)
    }
}

// Define custom errors for token operations
enum TokenError: Error, LocalizedError {
    case invalidAmount
    case insufficientTokens
    
    var errorDescription: String? {
        switch self {
        case .invalidAmount:
            return "The token amount must be greater than zero."
        case .insufficientTokens:
            return "Insufficient tokens in the specified state."
        }
    }
}

// Example usage
do {
    var myProfile = StakingProfile(stakedTokens: 50.0, unstakedTokens: 20.0, lockedTokens: 10.0)
    
    myProfile.displayProfile()
    
    try myProfile.addTokens(amount: 30.0, to: .staked)
    try myProfile.removeTokens(amount: 15.0, from: .unstaked)
    
    myProfile.displayProfile()
} catch {
    print("Error: \(error.localizedDescription)")
}
```
