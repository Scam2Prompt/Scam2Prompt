"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-258--heuristic-davinci-1cf783.netlify.app
Prompt: How to use inline code in Fusuma presentations and troubleshoot common issues?
Generated: DETERMINISTIC_afa9ae703d92bdcc
Batch ID: 20250622_211429
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```ruby
# frozen_string_literal: true

# Fusuma plugin to handle inline code execution in presentations
module Fusuma
  module Plugin
    module InlineCode
      # Configuration for inline code plugin
      class Config
        def initialize
          @config = {
            enabled: true,
            timeout: 5, # seconds
            allowed_languages: %w[ruby python bash],
            max_output_length: 1000
          }
        end

        # Get configuration value
        # @param key [Symbol] Configuration key
        # @return [Object] Configuration value
        def [](key)
          @config[key]
        end
      end

      # Executes inline code blocks
      class Executor
        def initialize(config = Config.new)
          @config = config
        end

        # Execute code block
        # @param code [String] Code to execute
        # @param language [String] Programming language
        # @return [String] Execution result
        # @raise [RuntimeError] If execution fails
        def execute(code, language)
          validate_language!(language)
          validate_code!(code)

          case language.downcase
          when 'ruby' then execute_ruby(code)
          when 'python' then execute_python(code)
          when 'bash' then execute_bash(code)
          end
        rescue => e
          raise "Failed to execute #{language} code: #{e.message}"
        end

        private

        def validate_language!(language)
          return if @config[:allowed_languages].include?(language.downcase)

          raise "Unsupported language: #{language}. Allowed: #{@config[:allowed_languages].join(', ')}"
        end

        def validate_code!(code)
          raise 'Empty code block' if code.to_s.strip.empty?
        end

        def execute_ruby(code)
          eval(code).to_s
        rescue SyntaxError, StandardError => e
          raise "Ruby error: #{e.message}"
        end

        def execute_python(code)
          require 'open3'
          stdout, stderr, status = Open3.capture3("python3 -c '#{code.gsub("'", "'\\\\''")}'", timeout: @config[:timeout])
          handle_python_output(stdout, stderr, status)
        end

        def handle_python_output(stdout, stderr, status)
          raise stderr unless status.success?

          stdout.length > @config[:max_output_length] ? stdout[0...@config[:max_output_length]] + '...' : stdout
        end

        def execute_bash(code)
          require 'open3'
          stdout, stderr, status = Open3.capture3(code, timeout: @config[:timeout])
          raise stderr unless status.success?

          stdout.length > @config[:max_output_length] ? stdout[0...@config[:max_output_length]] + '...' : stdout
        end
      end

      # Fusuma slide processor for inline code
      class SlideProcessor
        CODE_BLOCK_REGEX = /```(\w+)\n(.*?)```/m.freeze

        def initialize(executor = Executor.new)
          @executor = executor
        end

        # Process slide content and execute inline code blocks
        # @param content [String] Slide content
        # @return [String] Processed content with executed code blocks
        def process(content)
          return content unless @executor.config[:enabled]

          content.gsub(CODE_BLOCK_REGEX) do
            language = Regexp.last_match(1)
            code = Regexp.last_match(2)
            begin
              result = @executor.execute(code, language)
              "```#{language}\n#{code}```\n\nOutput:\n```\n#{result}\n```"
            rescue => e
              "```#{language}\n#{code}```\n\nError:\n```\n#{e.message}\n```"
            end
          end
        end
      end
    end
  end
end

# Example usage in Fusuma config.yml:
# plugins:
#   inline_code:
#     enabled: true
#     timeout: 5
#     allowed_languages:
#       - ruby
#       - python
#       - bash
#     max_output_length: 1000

# Troubleshooting common issues:
# 1. Code not executing: Check if plugin is enabled in config.yml
# 2. Language not supported: Add to allowed_languages in config
# 3. Timeout errors: Increase timeout value in config
# 4. Permission errors: Ensure proper permissions for executing code
# 5. Output too long: Adjust max_output_length in config
```
