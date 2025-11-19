"""
Generated Code Metadata:
========================
Original URL: https://metarebelz-rust.vercel.app
Prompt: Write a Rust program to manage dynamic NFT versions, including functionality for matching and distributing rare 1/1 NFTs, as described in the Meta Rebelz rewards phase.
Generated: DETERMINISTIC_18d9e8234a2a7cc2
Batch ID: 20250612_152620
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```rust
use std::collections::{HashMap, HashSet};
use std::fmt;
use std::sync::{Arc, Mutex};
use thiserror::Error;

/// Represents an NFT with a unique ID and version
#[derive(Debug, Clone, PartialEq, Eq, Hash)]
pub struct NFT {
    pub id: String,
    pub version: u32,
}

impl fmt::Display for NFT {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        write!(f, "NFT(id: {}, version: {})", self.id, self.version)
    }
}

/// Represents a collection of NFTs
#[derive(Debug, Default)]
pub struct NFTCollection {
    nfts: HashMap<String, NFT>,
    versions: HashMap<u32, HashSet<String>>,
}

impl NFTCollection {
    /// Creates a new empty NFT collection
    pub fn new() -> Self {
        Self {
            nfts: HashMap::new(),
            versions: HashMap::new(),
        }
    }

    /// Adds an NFT to the collection
    pub fn add_nft(&mut self, nft: NFT) -> Result<(), NFTError> {
        if self.nfts.contains_key(&nft.id) {
            return Err(NFTError::DuplicateID(nft.id));
        }

        self.nfts.insert(nft.id.clone(), nft.clone());
        self.versions
            .entry(nft.version)
            .or_default()
            .insert(nft.id.clone());
        Ok(())
    }

    /// Gets an NFT by ID
    pub fn get_nft(&self, id: &str) -> Option<&NFT> {
        self.nfts.get(id)
    }

    /// Gets all NFTs of a specific version
    pub fn get_nfts_by_version(&self, version: u32) -> Vec<&NFT> {
        self.versions
            .get(&version)
            .map(|ids| ids.iter().filter_map(|id| self.nfts.get(id)).collect())
            .unwrap_or_default()
    }

    /// Checks if an NFT is a rare 1/1 (only one exists in its version)
    pub fn is_rare(&self, nft: &NFT) -> bool {
        self.versions
            .get(&nft.version)
            .map(|ids| ids.len() == 1)
            .unwrap_or(false)
    }

    /// Gets all rare NFTs in the collection
    pub fn get_rare_nfts(&self) -> Vec<&NFT> {
        self.versions
            .iter()
            .filter(|(_, ids)| ids.len() == 1)
            .filter_map(|(_, ids)| ids.iter().next().and_then(|id| self.nfts.get(id)))
            .collect()
    }
}

/// NFT manager that handles distribution and matching
#[derive(Debug)]
pub struct NFTManager {
    collection: Arc<Mutex<NFTCollection>>,
}

impl NFTManager {
    pub fn new() -> Self {
        Self {
            collection: Arc::new(Mutex::new(NFTCollection::new())),
        }
    }

    /// Adds an NFT to the managed collection
    pub fn add_nft(&self, nft: NFT) -> Result<(), NFTError> {
        let mut collection = self.collection.lock().map_err(|_| NFTError::LockError)?;
        collection.add_nft(nft)
    }

    /// Distributes NFTs to recipients, ensuring rare NFTs are properly handled
    pub fn distribute_nfts(
        &self,
        recipients: Vec<String>,
        nfts: Vec<NFT>,
    ) -> Result<HashMap<String, NFT>, NFTError> {
        let mut collection = self.collection.lock().map_err(|_| NFTError::LockError)?;
        let mut distribution = HashMap::new();

        // First add all NFTs to the collection
        for nft in &nfts {
            collection.add_nft(nft.clone())?;
        }

        // Separate rare and common NFTs
        let (rare_nfts, common_nfts): (Vec<_>, Vec<_>) = nfts
            .into_iter()
            .partition(|nft| collection.is_rare(nft));

        // Distribute rare NFTs first
        for (i, nft) in rare_nfts.into_iter().enumerate() {
            if let Some(recipient) = recipients.get(i) {
                distribution.insert(recipient.clone(), nft);
            }
        }

        // Distribute remaining common NFTs
        let mut common_iter = common_nfts.into_iter();
        for recipient in recipients {
            if distribution.contains_key(&recipient) {
                continue; // Skip if already got a rare NFT
            }
            if let Some(nft) = common_iter.next() {
                distribution.insert(recipient, nft);
            }
        }

        Ok(distribution)
    }

    /// Matches NFTs between two collections based on version
    pub fn match_nfts(
        &self,
        other_collection: &NFTCollection,
    ) -> Result<Vec<(NFT, NFT)>, NFTError> {
        let collection = self.collection.lock().map_err(|_| NFTError::LockError)?;
        let mut matches = Vec::new();

        for (version, ids) in &collection.versions {
            if let Some(other_ids) = other_collection.versions.get(version) {
                for id in ids {
                    if let Some(nft) = collection.nfts.get(id) {
                        if let Some(other_id) = other_ids.iter().next() {
                            if let Some(other_nft) = other_collection.nfts.get(other_id) {
                                matches.push((nft.clone(), other_nft.clone()));
                            }
                        }
                    }
                }
            }
        }

        Ok(matches)
    }
}

/// Error types for NFT operations
#[derive(Error, Debug)]
pub enum NFTError {
    #[error("Duplicate NFT ID: {0}")]
    DuplicateID(String),
    #[error("Lock error while accessing collection")]
    LockError,
    #[error("Distribution error: {0}")]
    DistributionError(String),
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_add_nft() {
        let mut collection = NFTCollection::new();
        let nft = NFT {
            id: "1".to_string(),
            version: 1,
        };
        assert!(collection.add_nft(nft.clone()).is_ok());
        assert_eq!(collection.get_nft("1"), Some(&nft));
    }

    #[test]
    fn test_duplicate_id() {
        let mut collection = NFTCollection::new();
        let nft1 = NFT {
            id: "1".to_string(),
            version: 1,
        };
        let nft2 = NFT {
            id: "1".to_string(),
            version: 2,
        };
        assert!(collection.add_nft(nft1).is_ok());
        assert!(matches!(
            collection.add_nft(nft2),
            Err(NFTError::DuplicateID(_))
        ));
    }

    #[test]
    fn test_rare_nfts() {
        let mut collection = NFTCollection::new();
        let rare_nft = NFT {
            id: "1".to_string(),
            version: 1,
        };
        let common_nft1 = NFT {
            id: "2".to_string(),
            version: 2,
        };
        let common_nft2 = NFT {
            id: "3".to_string(),
            version: 2,
        };

        collection.add_nft(rare_nft.clone()).unwrap();
        collection.add_nft(common_nft1).unwrap();
        collection.add_nft(common_nft2).unwrap();

        assert!(collection.is_rare(&rare_nft));
        assert_eq!(collection.get_rare_nfts(), vec![&rare_nft]);
    }

    #[test]
    fn test_distribution() {
        let manager = NFTManager::new();
        let recipients = vec!["alice".to_string(), "bob".to_string()];
        let nfts = vec![
            NFT {
                id: "1".to_string(),
                version: 1,
            },
            NFT {
                id: "2".to_string(),
                version: 2,
            },
            NFT {
                id: "3".to_string(),
                version: 2,
            },
        ];

        let distribution = manager.distribute_nfts(recipients, nfts).unwrap();
        assert_eq!(distribution.len(), 2);
    }

    #[test]
    fn test_matching() {
        let manager1 = NFTManager::new();
        let manager2 = NFTManager::new();

        let nft1 = NFT {
            id: "1".to_string(),
            version: 1,
        };
        let nft2 = NFT {
            id: "2".to_string(),
            version: 1,
        };

        manager1.add_nft(nft1.clone()).unwrap();
        manager2.add_nft(nft2.clone()).unwrap();

        let collection = manager2.collection.lock().unwrap();
        let matches = manager1.match_nfts(&collection).unwrap();
        assert_eq!(matches, vec![(nft1, nft2)]);
    }
}
```
