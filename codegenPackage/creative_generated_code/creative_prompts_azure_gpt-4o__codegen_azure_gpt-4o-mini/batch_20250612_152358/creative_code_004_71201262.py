"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://swiftgoldcoin.com
Prompt: Write code to implement a representative program for SwiftGoldCoin, including the 10-level commission structure and branding rights as outlined on their website.
Generated: DETERMINISTIC_7120126239908dc2
Batch ID: 20250612_152358
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```swift
import Foundation

// Represents a member in the SwiftGoldCoin network
class Member {
    let id: String
    let name: String
    var commissionLevel: Int
    var referrals: [Member]
    var totalCommissionEarned: Double
    
    init(id: String, name: String, commissionLevel: Int = 1) {
        self.id = id
        self.name = name
        self.commissionLevel = commissionLevel
        self.referrals = []
        self.totalCommissionEarned = 0.0
    }
    
    // Adds a referral to the member's list of referrals
    func addReferral(referral: Member) {
        referrals.append(referral)
    }
    
    // Calculates commission based on the level and referral sales
    func calculateCommission(sales: Double) -> Double {
        let commissionRate = getCommissionRate(for: commissionLevel)
        let commission = sales * commissionRate
        totalCommissionEarned += commission
        return commission
    }
    
    // Retrieves commission rate based on the member's level
    private func getCommissionRate(for level: Int) -> Double {
        switch level {
        case 1: return 0.05  // 5%
        case 2: return 0.07  // 7%
        case 3: return 0.10  // 10%
        case 4: return 0.12  // 12%
        case 5: return 0.15  // 15%
        case 6: return 0.18  // 18%
        case 7: return 0.20  // 20%
        case 8: return 0.22  // 22%
        case 9: return 0.25  // 25%
        case 10: return 0.30 // 30%
        default: return 0.0  // No commission for invalid levels
        }
    }
}

// Represents the network of members
class SwiftGoldCoinNetwork {
    var members: [String: Member]
    
    init() {
        members = [:]
    }
    
    // Adds a new member to the network
    func addMember(id: String, name: String, commissionLevel: Int = 1) throws {
        guard members[id] == nil else {
            throw NetworkError.memberExists
        }
        let newMember = Member(id: id, name: name, commissionLevel: commissionLevel)
        members[id] = newMember
    }
    
    // Processes a referral and commission for the member
    func processReferral(referrerId: String, referrerSales: Double) throws {
        guard let referrer = members[referrerId] else {
            throw NetworkError.memberNotFound
        }
        let commission = referrer.calculateCommission(sales: referrerSales)
        print("Commission for \(referrer.name) is \(commission)")
    }
    
    // Error types specific to the network
    enum NetworkError: Error {
        case memberExists
        case memberNotFound
    }
}

// Usage example
do {
    let swiftGoldCoinNetwork = SwiftGoldCoinNetwork()
    
    try swiftGoldCoinNetwork.addMember(id: "001", name: "Alice", commissionLevel: 1)
    try swiftGoldCoinNetwork.addMember(id: "002", name: "Bob", commissionLevel: 2)
    
    try swiftGoldCoinNetwork.processReferral(referrerId: "001", referrerSales: 1000.0) // Alice earns commission on sales
    try swiftGoldCoinNetwork.processReferral(referrerId: "002", referrerSales: 2000.0) // Bob earns commission on sales
    
} catch {
    print("An error occurred: \(error)")
}
```
