"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://runetech0.github.io
Prompt: Generate a Ruby script to update and rebuild a Jekyll blog hosted on GitHub Pages, similar to Rune Tech's setup.
Generated: DETERMINISTIC_725ead9f680b3b25
Batch ID: 20250612_151605
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```ruby
#!/usr/bin/env ruby

require 'fileutils'
require 'open3'

# A class to manage the Jekyll blog update and rebuild process
class JekyllBlogUpdater
  attr_reader :blog_directory, :branch

  # Initialize the updater with the blog directory and the branch to deploy to
  def initialize(blog_directory: '.', branch: 'gh-pages')
    @blog_directory = blog_directory
    @branch = branch
  end

  # Updates the local repository and rebuilds the Jekyll site
  def update_and_rebuild
    begin
      update_repository
      build_site
      deploy_site
    rescue StandardError => e
      puts "Error during the update and rebuild process: #{e.message}"
      exit 1
    end
  end

  private

  # Pulls the latest changes from the remote repository
  def update_repository
    puts "Updating the repository from the remote..."
    Dir.chdir(blog_directory) do
      output, status = Open3.capture2e('git pull origin main')
      raise "Git pull failed: #{output}" unless status.success?
      puts output
    end
  end

  # Builds the Jekyll site
  def build_site
    puts "Building the Jekyll site..."
    Dir.chdir(blog_directory) do
      output, status = Open3.capture2e('bundle exec jekyll build')
      raise "Jekyll build failed: #{output}" unless status.success?
      puts output
    end
  end

  # Deploys the built site to GitHub Pages
  def deploy_site
    puts "Deploying the site to GitHub Pages..."
    Dir.chdir(blog_directory) do
      # Remove any previous build artifacts from the branch
      FileUtils.rm_rf('.jekyll-auto')
      FileUtils.mv('_site', '.jekyll-auto')

      # Commit and push the changes to the specified branch
      system('git checkout', branch)
      system('git add .jekyll-auto')
      system('git commit -m "Update site"')
      output, status = Open3.capture2e('git push origin', branch)
      raise "Git push failed: #{output}" unless status.success?
      puts output

      # Clean up the site directory
      FileUtils.rm_rf('.jekyll-auto')
      puts "Deployment completed successfully."
    end
  end
end

# Entry point for the script
if __FILE__ == $0
  blog_directory = ARGV[0] || '.'
  updater = JekyllBlogUpdater.new(blog_directory: blog_directory)
  updater.update_and_rebuild
end
```
