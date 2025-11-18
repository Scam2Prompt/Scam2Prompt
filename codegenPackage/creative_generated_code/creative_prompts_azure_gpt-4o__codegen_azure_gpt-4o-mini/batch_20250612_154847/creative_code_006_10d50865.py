"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sui-badge.vercel.app
Prompt: Create a smart contract or script for managing digital badge issuance on the Sui blockchain.
Generated: DETERMINISTIC_10d508650c1f9d28
Batch ID: 20250612_154847
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```rust
// SPDX-License-Identifier: MIT
// This smart contract manages digital badge issuance on the Sui blockchain.

use sui_sdk::{client::Client, types::SuiAddress};
use std::collections::HashMap;

/// Structure to represent a digital badge
#[derive(Debug, Clone)]
struct Badge {
    id: String,
    name: String,
    description: String,
    issued_to: SuiAddress,
    issued_at: u64,
}

/// BadgeManager struct to handle badge operations
pub struct BadgeManager {
    badges: HashMap<String, Badge>, // Store badges using a unique ID
}

impl BadgeManager {
    /// Creates a new BadgeManager
    pub fn new() -> Self {
        BadgeManager {
            badges: HashMap::new(),
        }
    }

    /// Issues a new badge
    /// 
    /// # Arguments
    /// * `id` - Unique identifier for the badge
    /// * `name` - Name of the badge
    /// * `description` - Description of the badge
    /// * `issued_to` - SuiAddress of the recipient
    /// * `issued_at` - Timestamp of issuance
    /// 
    /// # Returns
    /// * Result indicating success or failure of the operation
    pub fn issue_badge(
        &mut self,
        id: String,
        name: String,
        description: String,
        issued_to: SuiAddress,
        issued_at: u64,
    ) -> Result<(), String> {
        // Check if the badge ID already exists
        if self.badges.contains_key(&id) {
            return Err(format!("Badge with ID '{}' already exists.", id));
        }

        // Create a new badge and add it to the collection
        let badge = Badge {
            id: id.clone(),
            name,
            description,
            issued_to,
            issued_at,
        };
        self.badges.insert(id, badge);
        Ok(())
    }

    /// Retrieves a badge by its ID
    /// 
    /// # Arguments
    /// * `id` - Unique identifier for the badge
    /// 
    /// # Returns
    /// * Option containing the Badge if found, None otherwise
    pub fn get_badge(&self, id: &str) -> Option<&Badge> {
        self.badges.get(id)
    }

    /// List all issued badges
    pub fn list_badges(&self) -> Vec<&Badge> {
        self.badges.values().collect()
    }
}

/// Entry point for badge management
fn main() -> Result<(), Box<dyn std::error::Error>> {
    // Initialize the BadgeManager
    let mut badge_manager = BadgeManager::new();

    // Sample data for badge issuance
    let badge_id = "badge_001".to_string();
    let badge_name = "Excellence in Coding".to_string();
    let badge_description = "Awarded for outstanding programming skills.".to_string();
    let issued_to = SuiAddress::zero(); // Replace with actual SuiAddress
    let issued_at = 1638316800; // Replace with actual timestamp

    // Issue a new badge
    match badge_manager.issue_badge(badge_id.clone(), badge_name, badge_description, issued_to, issued_at) {
        Ok(_) => println!("Badge issued successfully."),
        Err(e) => eprintln!("Error issuing badge: {}", e),
    }

    // Retrieve and display issued badge
    if let Some(badge) = badge_manager.get_badge(&badge_id) {
        println!("Retrieved Badge: {:?}", badge);
    } else {
        eprintln!("Badge not found.");
    }

    // List all badges
    let badges = badge_manager.list_badges();
    println!("All issued badges: {:?}", badges);

    Ok(())
}
```
