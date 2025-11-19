"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-137--keen-roentgen-cafcb7.netlify.app
Prompt: Explain how to contribute to Rust open source projects, referencing Joe Previte's insights and experiences.
Generated: DETERMINISTIC_ea5c727a0b633d14
Batch ID: 20250612_163408
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```rust
// Contributing to Rust Open Source Projects
// =======================================

// Based on insights and experiences from Joe Previte

use std::fs::File;
use std::io::{BufReader, BufRead};
use std::path::Path;

/// Structure to hold information about a contributor
#[derive(Debug)]
struct Contributor {
    name: String,
    github_handle: String,
}

impl Contributor {
    /// Create a new contributor
    fn new(name: String, github_handle: String) -> Self {
        Contributor { name, github_handle }
    }
}

/// Function to get contributors from a file
/// 
/// Reads a file with lines in the format: "Name <GitHub Handle>"
/// 
/// # Errors
/// 
/// * If the file does not exist
/// * If a line is not in the correct format
fn get_contributors(file_path: &str) -> Result<Vec<Contributor>, std::io::Error> {
    let file = File::open(file_path)?;
    let reader = BufReader::new(file);
    let mut contributors = Vec::new();

    for line in reader.lines() {
        let line = line?;
        let parts: Vec<&str> = line.split_whitespace().collect();
        
        if parts.len() != 2 {
            eprintln!("Skipping invalid line: {}", line);
            continue;
        }

        let name: String = parts[0..1].join(" ");
        let github_handle = parts[1].trim_start_matches('<').trim_end_matches('>');
        contributors.push(Contributor::new(name, github_handle.to_string()));
    }

    Ok(contributors)
}

/// Function to print contributors
fn print_contributors(contributors: Vec<Contributor>) {
    for contributor in contributors {
        println!("* {} ({})", contributor.name, contributor.github_handle);
    }
}

fn main() -> Result<(), std::io::Error> {
    let file_path = "contributors.txt"; // replace with actual file path
    let contributors = get_contributors(file_path)?;

    println!("Contributors:");
    print_contributors(contributors);

    Ok(())
}
```
