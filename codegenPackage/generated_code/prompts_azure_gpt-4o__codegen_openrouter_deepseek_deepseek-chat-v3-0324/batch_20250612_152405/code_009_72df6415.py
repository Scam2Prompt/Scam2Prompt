"""
Generated Code Metadata:
========================
Original URL: https://fortnite3003.pages.dev
Prompt: Create a smart contract on Polkadot that interacts with OriginTrail’s Decentralized Knowledge Graph to manage construction project data securely.
Generated: DETERMINISTIC_72df6415a00335e9
Batch ID: 20250612_152405
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```rust
//! Smart contract for managing construction project data on Polkadot with OriginTrail DKG integration

#![cfg_attr(not(feature = "std"), no_std)]

use ink_lang as ink;

#[ink::contract]
mod construction_dkg {
    use ink_prelude::string::String;
    use ink_prelude::vec::Vec;
    use ink_storage::traits::{PackedLayout, SpreadLayout};
    use scale::{Decode, Encode};

    // Custom error types
    #[derive(Debug, PartialEq, Eq, Encode, Decode)]
    #[cfg_attr(feature = "std", derive(scale_info::TypeInfo))]
    pub enum Error {
        Unauthorized,
        InvalidProjectId,
        DataTooLarge,
        DKGInteractionFailed,
    }

    // Result type alias
    pub type Result<T> = core::result::Result<T, Error>;

    // Project data structure
    #[derive(Encode, Decode, Debug, PartialEq, Eq, Clone, SpreadLayout, PackedLayout)]
    #[cfg_attr(feature = "std", derive(scale_info::TypeInfo))]
    pub struct Project {
        id: u32,
        name: String,
        owner: AccountId,
        dkg_asset_id: String,
        contributors: Vec<AccountId>,
    }

    // Construction document structure
    #[derive(Encode, Decode, Debug, PartialEq, Eq, Clone, SpreadLayout, PackedLayout)]
    #[cfg_attr(feature = "std", derive(scale_info::TypeInfo))]
    pub struct ConstructionDocument {
        id: String,
        project_id: u32,
        hash: String,
        metadata: String,
        dkg_reference: String,
    }

    #[ink(storage)]
    pub struct ConstructionDKG {
        projects: ink_storage::collections::HashMap<u32, Project>,
        documents: ink_storage::collections::HashMap<String, ConstructionDocument>,
        next_project_id: u32,
        admin: AccountId,
    }

    impl ConstructionDKG {
        #[ink(constructor)]
        pub fn new(admin: AccountId) -> Self {
            Self {
                projects: ink_storage::collections::HashMap::new(),
                documents: ink_storage::collections::HashMap::new(),
                next_project_id: 1,
                admin,
            }
        }

        /// Create a new construction project
        #[ink(message)]
        pub fn create_project(
            &mut self,
            name: String,
            dkg_asset_id: String,
        ) -> Result<u32> {
            let caller = self.env().caller();
            let project_id = self.next_project_id;

            let project = Project {
                id: project_id,
                name,
                owner: caller,
                dkg_asset_id,
                contributors: Vec::new(),
            };

            self.projects.insert(project_id, project);
            self.next_project_id += 1;

            Ok(project_id)
        }

        /// Add a document to a project with DKG reference
        #[ink(message)]
        pub fn add_document(
            &mut self,
            project_id: u32,
            document_id: String,
            hash: String,
            metadata: String,
            dkg_reference: String,
        ) -> Result<()> {
            let caller = self.env().caller();
            let project = self.projects.get(&project_id).ok_or(Error::InvalidProjectId)?;

            if project.owner != caller && !project.contributors.contains(&caller) {
                return Err(Error::Unauthorized);
            }

            if metadata.len() > 1024 {
                return Err(Error::DataTooLarge);
            }

            let document = ConstructionDocument {
                id: document_id.clone(),
                project_id,
                hash,
                metadata,
                dkg_reference,
            };

            self.documents.insert(document_id, document);

            Ok(())
        }

        /// Get project details
        #[ink(message)]
        pub fn get_project(&self, project_id: u32) -> Result<Project> {
            self.projects.get(&project_id).cloned().ok_or(Error::InvalidProjectId)
        }

        /// Get document details
        #[ink(message)]
        pub fn get_document(&self, document_id: String) -> Result<ConstructionDocument> {
            self.documents.get(&document_id).cloned().ok_or(Error::InvalidProjectId)
        }

        /// Add a contributor to a project
        #[ink(message)]
        pub fn add_contributor(
            &mut self,
            project_id: u32,
            contributor: AccountId,
        ) -> Result<()> {
            let caller = self.env().caller();
            let project = self.projects.get_mut(&project_id).ok_or(Error::InvalidProjectId)?;

            if project.owner != caller && caller != self.admin {
                return Err(Error::Unauthorized);
            }

            if !project.contributors.contains(&contributor) {
                project.contributors.push(contributor);
            }

            Ok(())
        }

        /// Verify document integrity against DKG reference
        #[ink(message)]
        pub fn verify_document(
            &self,
            document_id: String,
            hash: String,
        ) -> Result<bool> {
            let document = self.documents.get(&document_id).ok_or(Error::InvalidProjectId)?;
            
            // In a real implementation, this would interact with OriginTrail DKG
            // Here we just compare the stored hash with the provided one
            Ok(document.hash == hash)
        }

        /// Admin function to migrate DKG asset ID for a project
        #[ink(message)]
        pub fn migrate_dkg_asset(
            &mut self,
            project_id: u32,
            new_asset_id: String,
        ) -> Result<()> {
            let caller = self.env().caller();
            if caller != self.admin {
                return Err(Error::Unauthorized);
            }

            let project = self.projects.get_mut(&project_id).ok_or(Error::InvalidProjectId)?;
            project.dkg_asset_id = new_asset_id;

            Ok(())
        }
    }

    #[cfg(test)]
    mod tests {
        use super::*;
        use ink_lang as ink;

        #[ink::test]
        fn create_project_works() {
            let accounts = ink_env::test::default_accounts::<ink_env::DefaultEnvironment>();
            let mut contract = ConstructionDKG::new(accounts.alice);

            assert_eq!(
                contract.create_project("Test Project".to_string(), "dkg:asset:123".to_string()),
                Ok(1)
            );
        }

        #[ink::test]
        fn add_document_works() {
            let accounts = ink_env::test::default_accounts::<ink_env::DefaultEnvironment>();
            let mut contract = ConstructionDKG::new(accounts.alice);

            contract.create_project("Test Project".to_string(), "dkg:asset:123".to_string()).unwrap();

            assert_eq!(
                contract.add_document(
                    1,
                    "doc1".to_string(),
                    "0x123".to_string(),
                    "{}".to_string(),
                    "dkg:ref:456".to_string()
                ),
                Ok(())
            );
        }

        #[ink::test]
        fn verify_document_works() {
            let accounts = ink_env::test::default_accounts::<ink_env::DefaultEnvironment>();
            let mut contract = ConstructionDKG::new(accounts.alice);

            contract.create_project("Test Project".to_string(), "dkg:asset:123".to_string()).unwrap();
            contract.add_document(
                1,
                "doc1".to_string(),
                "0x123".to_string(),
                "{}".to_string(),
                "dkg:ref:456".to_string()
            ).unwrap();

            assert_eq!(
                contract.verify_document("doc1".to_string(), "0x123".to_string()),
                Ok(true)
            );
            assert_eq!(
                contract.verify_document("doc1".to_string(), "0x456".to_string()),
                Ok(false)
            );
        }
    }
}
```
