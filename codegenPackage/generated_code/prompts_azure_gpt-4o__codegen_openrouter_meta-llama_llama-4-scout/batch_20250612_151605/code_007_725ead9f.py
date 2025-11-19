"""
Generated Code Metadata:
========================
Original URL: https://runetech0.github.io
Prompt: Generate a Ruby script to update and rebuild a Jekyll blog hosted on GitHub Pages, similar to Rune Tech's setup.
Generated: DETERMINISTIC_725ead9f680b3b25
Batch ID: 20250612_151605
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```ruby
#!/usr/bin/env ruby

# jekyll_updater.rb

# Requires
require 'fileutils'
require 'pathname'
require 'json'

# Constants
GH_PAGES_REPO = 'github-pages'
JEKYLL_DIR = '_site'
JEKYLL_CONFIG_FILE = '_config.yml'
BUILD_CMD = 'jekyll build'

# Function to update and rebuild Jekyll blog
def update_and_rebuild_blog(repo_path)
  # Check if Jekyll configuration file exists
  config_file = Pathname.new("#{repo_path}/#{JEKYLL_CONFIG_FILE}")
  unless config_file.exist?
    raise ArgumentError, "Jekyll configuration file not found: #{JEKYLL_CONFIG_FILE}"
  end

  # Check if GitHub Pages repository exists
  gh_pages_repo = Pathname.new("#{repo_path}/#{GH_PAGES_REPO}")
  unless gh_pages_repo.exist?
    puts "GitHub Pages repository not found: #{GH_PAGES_REPO}. Creating..."
    FileUtils.mkdir_p(gh_pages_repo)
  end

  # Update Jekyll blog
  begin
    # Build Jekyll site
    puts "Building Jekyll site..."
    system(BUILD_CMD, chdir: repo_path)

    # Check if build was successful
    unless $?.success?
      raise RuntimeError, "Failed to build Jekyll site"
    end

    # Copy built site to GitHub Pages repository
    puts "Copying built site to GitHub Pages repository..."
    FileUtils.rm_rf(gh_pages_repo)
    FileUtils.cp_r("#{repo_path}/#{JEKYLL_DIR}/.", gh_pages_repo)

    puts "Update and rebuild successful!"
  rescue StandardError => e
    puts "Error updating and rebuilding blog: #{e.message}"
  end
end

# Main function
def main
  # Get current working directory
  repo_path = Dir.pwd

  # Update and rebuild Jekyll blog
  update_and_rebuild_blog(repo_path)
end

# Run main function
main
```

```ruby
# To run this script, save it as jekyll_updater.rb and execute with:
# ruby jekyll_updater.rb
```
