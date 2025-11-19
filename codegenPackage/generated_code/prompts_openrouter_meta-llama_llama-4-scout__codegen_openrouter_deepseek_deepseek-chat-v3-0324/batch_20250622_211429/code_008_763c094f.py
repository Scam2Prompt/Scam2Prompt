"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-258--heuristic-davinci-1cf783.netlify.app
Prompt: Create a simple Fusuma plugin to print debug messages for troubleshooting presentation rendering issues.
Generated: DETERMINISTIC_763c094f3ba59f7e
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

module Fusuma
  module Plugin
    # Fusuma plugin for debugging presentation rendering issues
    class DebugPrinter
      # Plugin registration
      def self.install
        # Register as a listener for debug events
        Fusuma::Plugin::Events.add(:debug, self)
      end

      # Initialize with config
      # @param config [Fusuma::Config]
      def initialize(config = Config.instance)
        @config = config
        @logger = Logger.new($stdout)
        @logger.level = debug_level
      end

      # Handle incoming events
      # @param event [Fusuma::Event]
      def process(event)
        return unless event.type == :debug

        case event.tag
        when :render
          log_render_event(event)
        when :config
          log_config_event(event)
        else
          log_generic_event(event)
        end
      rescue StandardError => e
        @logger.error("DebugPrinter failed: #{e.message}")
        @logger.debug(e.backtrace.join("\n"))
      end

      private

      # @return [Integer] log level from config or default to INFO
      def debug_level
        level = @config.dig(:debug_printer, :log_level)&.to_sym || :info
        Logger::Severity.const_get(level.upcase)
      rescue NameError
        Logger::INFO
      end

      # Log render events with detailed information
      # @param event [Fusuma::Event]
      def log_render_event(event)
        @logger.debug("Render Event: #{event.to_h}")
        @logger.debug("Slide content: #{event.payload[:content]}") if event.payload[:content]
      end

      # Log config events
      # @param event [Fusuma::Event]
      def log_config_event(event)
        @logger.info("Config Event: #{event.to_h}")
      end

      # Fallback for unhandled event types
      # @param event [Fusuma::Event]
      def log_generic_event(event)
        @logger.debug("Debug Event: #{event.to_h}")
      end
    end
  end
end

# Register the plugin
Fusuma::Plugin::DebugPrinter.install
```
