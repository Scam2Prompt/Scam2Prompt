"""
Generated Code Metadata:
========================
Original URL: https://aleph-zero.pages.dev
Prompt: Develop a decentralized DNS system on Aleph Zero using its WASM-based smart contracts and privacy-enhancing technology.
Generated: DETERMINISTIC_3d4078f4bef8ac45
Batch ID: 20250612_153401
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```rust
//! Decentralized DNS system on Aleph Zero using WASM smart contracts

#![cfg_attr(not(feature = "std"), no_std)]

use ink_lang as ink;

#[ink::contract]
mod decentralized_dns {
    use ink_prelude::string::String;
    use ink_prelude::vec::Vec;
    use ink_storage::{
        collections::HashMap as StorageHashMap,
        traits::{PackedLayout, SpreadLayout},
    };

    /// DNS record types
    #[derive(Debug, PartialEq, Eq, scale::Encode, scale::Decode, SpreadLayout, PackedLayout)]
    #[cfg_attr(feature = "std", derive(scale_info::TypeInfo))]
    pub enum RecordType {
        A,
        AAAA,
        CNAME,
        TXT,
        MX,
    }

    /// DNS record data
    #[derive(Debug, PartialEq, Eq, scale::Encode, scale::Decode, SpreadLayout, PackedLayout)]
    #[cfg_attr(feature = "std", derive(scale_info::TypeInfo))]
    pub struct Record {
        record_type: RecordType,
        data: String,
        ttl: u64,
    }

    /// Domain information
    #[derive(Debug, scale::Encode, scale::Decode, SpreadLayout, PackedLayout)]
    #[cfg_attr(feature = "std", derive(scale_info::TypeInfo))]
    pub struct Domain {
        owner: AccountId,
        records: Vec<Record>,
        expiration: u64,
    }

    /// Errors that can occur during contract execution
    #[derive(Debug, PartialEq, Eq, scale::Encode, scale::Decode)]
    #[cfg_attr(feature = "std", derive(scale_info::TypeInfo))]
    pub enum Error {
        Unauthorized,
        DomainNotFound,
        RecordNotFound,
        DomainExpired,
        InvalidDomain,
        InvalidRecord,
        InsufficientFunds,
    }

    /// Result type for contract operations
    pub type Result<T> = core::result::Result<T, Error>;

    #[ink(storage)]
    pub struct DecentralizedDNS {
        /// Mapping from domain names to their information
        domains: StorageHashMap<String, Domain>,
        /// Mapping from account to owned domains
        account_domains: StorageHashMap<AccountId, Vec<String>>,
        /// Domain registration fee
        registration_fee: Balance,
        /// Contract admin
        admin: AccountId,
    }

    impl DecentralizedDNS {
        /// Creates a new DNS contract
        #[ink(constructor)]
        pub fn new(registration_fee: Balance) -> Self {
            Self {
                domains: StorageHashMap::new(),
                account_domains: StorageHashMap::new(),
                registration_fee,
                admin: Self::env().caller(),
            }
        }

        /// Register a new domain
        #[ink(message, payable)]
        pub fn register_domain(&mut self, domain_name: String, duration: u64) -> Result<()> {
            if self.domains.contains_key(&domain_name) {
                return Err(Error::InvalidDomain);
            }

            let caller = self.env().caller();
            let transferred_value = self.env().transferred_value();

            if transferred_value < self.registration_fee {
                return Err(Error::InsufficientFunds);
            }

            let expiration = self.env().block_timestamp() + duration;
            let domain = Domain {
                owner: caller,
                records: Vec::new(),
                expiration,
            };

            self.domains.insert(domain_name.clone(), domain);

            let mut owned_domains = self.account_domains.get(&caller).cloned().unwrap_or_default();
            owned_domains.push(domain_name);
            self.account_domains.insert(caller, owned_domains);

            Ok(())
        }

        /// Renew a domain registration
        #[ink(message, payable)]
        pub fn renew_domain(&mut self, domain_name: String, duration: u64) -> Result<()> {
            let domain = self.domains.get_mut(&domain_name).ok_or(Error::DomainNotFound)?;
            let caller = self.env().caller();

            if domain.owner != caller {
                return Err(Error::Unauthorized);
            }

            let transferred_value = self.env().transferred_value();
            if transferred_value < self.registration_fee {
                return Err(Error::InsufficientFunds);
            }

            domain.expiration = self.env().block_timestamp() + duration;
            Ok(())
        }

        /// Add a DNS record to a domain
        #[ink(message)]
        pub fn add_record(
            &mut self,
            domain_name: String,
            record_type: RecordType,
            data: String,
            ttl: u64,
        ) -> Result<()> {
            let domain = self.domains.get_mut(&domain_name).ok_or(Error::DomainNotFound)?;
            let caller = self.env().caller();

            if domain.owner != caller {
                return Err(Error::Unauthorized);
            }

            if self.env().block_timestamp() > domain.expiration {
                return Err(Error::DomainExpired);
            }

            let record = Record {
                record_type,
                data,
                ttl,
            };

            domain.records.push(record);
            Ok(())
        }

        /// Remove a DNS record from a domain
        #[ink(message)]
        pub fn remove_record(&mut self, domain_name: String, record_index: u32) -> Result<()> {
            let domain = self.domains.get_mut(&domain_name).ok_or(Error::DomainNotFound)?;
            let caller = self.env().caller();

            if domain.owner != caller {
                return Err(Error::Unauthorized);
            }

            if record_index as usize >= domain.records.len() {
                return Err(Error::RecordNotFound);
            }

            domain.records.remove(record_index as usize);
            Ok(())
        }

        /// Transfer domain ownership
        #[ink(message)]
        pub fn transfer_domain(&mut self, domain_name: String, new_owner: AccountId) -> Result<()> {
            let domain = self.domains.get_mut(&domain_name).ok_or(Error::DomainNotFound)?;
            let caller = self.env().caller();

            if domain.owner != caller {
                return Err(Error::Unauthorized);
            }

            // Remove from current owner's list
            if let Some(mut owned_domains) = self.account_domains.get(&caller).cloned() {
                owned_domains.retain(|name| name != &domain_name);
                self.account_domains.insert(caller, owned_domains);
            }

            // Add to new owner's list
            let mut new_owner_domains = self.account_domains.get(&new_owner).cloned().unwrap_or_default();
            new_owner_domains.push(domain_name.clone());
            self.account_domains.insert(new_owner, new_owner_domains);

            domain.owner = new_owner;
            Ok(())
        }

        /// Get domain records
        #[ink(message)]
        pub fn get_records(&self, domain_name: String) -> Result<Vec<Record>> {
            let domain = self.domains.get(&domain_name).ok_or(Error::DomainNotFound)?;
            Ok(domain.records.clone())
        }

        /// Get domains owned by an account
        #[ink(message)]
        pub fn get_owned_domains(&self, account: AccountId) -> Vec<String> {
            self.account_domains.get(&account).cloned().unwrap_or_default()
        }

        /// Get domain information
        #[ink(message)]
        pub fn get_domain_info(&self, domain_name: String) -> Result<Domain> {
            self.domains.get(&domain_name).cloned().ok_or(Error::DomainNotFound)
        }

        /// Update registration fee (admin only)
        #[ink(message)]
        pub fn update_registration_fee(&mut self, new_fee: Balance) -> Result<()> {
            if self.env().caller() != self.admin {
                return Err(Error::Unauthorized);
            }
            self.registration_fee = new_fee;
            Ok(())
        }

        /// Withdraw contract funds (admin only)
        #[ink(message)]
        pub fn withdraw_funds(&mut self, amount: Balance) -> Result<()> {
            if self.env().caller() != self.admin {
                return Err(Error::Unauthorized);
            }
            if self.env().balance() < amount {
                return Err(Error::InsufficientFunds);
            }
            self.env().transfer(self.admin, amount).map_err(|_| Error::InsufficientFunds)?;
            Ok(())
        }
    }

    #[cfg(test)]
    mod tests {
        use super::*;
        use ink_env::test;
        use ink_lang as ink;

        #[ink::test]
        fn register_domain_works() {
            let mut dns = DecentralizedDNS::new(100);
            let accounts = test::default_accounts::<ink_env::DefaultEnvironment>();

            // Set caller to Alice
            test::set_caller::<ink_env::DefaultEnvironment>(accounts.alice);

            //
