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

require 'fileutils'
require 'open3'
require 'optparse'
require 'yaml'

# JekyllBlogUpdater - A script to update and rebuild a Jekyll blog hosted on GitHub Pages
class JekyllBlogUpdater
  attr_reader :config, :options

  def initialize
    @options = parse_options
    load_config
    validate_config
  end

  def run
    puts "Starting Jekyll blog update process..."
    
    Dir.chdir(config['site_directory']) do
      update_git_repository
      install_dependencies
      build_site
      deploy_site if options[:deploy]
    end

    puts "Update process completed successfully!"
  rescue StandardError => e
    abort "Error: #{e.message}"
  end

  private

  def parse_options
    options = {}
    OptionParser.new do |opts|
      opts.banner = "Usage: #{File.basename($PROGRAM_NAME)} [options]"

      opts.on("-d", "--deploy", "Deploy changes after building") do
        options[:deploy] = true
      end

      opts.on("-c", "--config PATH", "Path to config file (default: config.yml)") do |path|
        options[:config_path] = path
      end

      opts.on("-h", "--help", "Prints this help") do
        puts opts
        exit
      end
    end.parse!

    options
  end

  def load_config
    config_path = options[:config_path] || 'config.yml'
    @config = YAML.load_file(config_path)
  rescue Errno::ENOENT
    raise "Config file not found at #{config_path}"
  rescue Psych::SyntaxError => e
    raise "Invalid YAML in config file: #{e.message}"
  end

  def validate_config
    required_keys = %w[site_directory git_remote]
    missing_keys = required_keys.reject { |k| config.key?(k) }

    unless missing_keys.empty?
      raise "Missing required config keys: #{missing_keys.join(', ')}"
    end

    unless File.directory?(config['site_directory'])
      raise "Site directory not found: #{config['site_directory']}"
    end
  end

  def update_git_repository
    puts "Updating Git repository..."
    run_command("git fetch #{config['git_remote']}")
    run_command("git checkout #{config['git_branch'] || 'main'}")
    run_command("git pull #{config['git_remote']} #{config['git_branch'] || 'main'}")
  end

  def install_dependencies
    puts "Installing dependencies..."
    run_command("bundle install")
  end

  def build_site
    puts "Building Jekyll site..."
    run_command("JEKYLL_ENV=production bundle exec jekyll build")
  end

  def deploy_site
    puts "Deploying changes..."
    run_command("git add .")
    run_command("git commit -m 'Automated site update'")
    run_command("git push #{config['git_remote']} #{config['git_branch'] || 'main'}")
  end

  def run_command(cmd)
    puts "Running: #{cmd}"
    stdout, stderr, status = Open3.capture3(cmd)

    unless status.success?
      puts "Command failed with status #{status.exitstatus}"
      puts "STDOUT: #{stdout}" unless stdout.empty?
      puts "STDERR: #{stderr}" unless stderr.empty?
      raise "Command failed: #{cmd}"
    end
  end
end

# Main execution
if __FILE__ == $PROGRAM_NAME
  updater = JekyllBlogUpdater.new
  updater.run
end
```
