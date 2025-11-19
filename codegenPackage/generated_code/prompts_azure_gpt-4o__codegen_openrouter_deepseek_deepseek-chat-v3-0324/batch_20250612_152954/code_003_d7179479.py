"""
Generated Code Metadata:
========================
Original URL: https://sonic-explorer.skavel.cz
Prompt: Write code to troubleshoot JavaScript compatibility issues when using Sonic Explorer for audio exploration.
Generated: DETERMINISTIC_d717947936c819f7
Batch ID: 20250612_152954
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Sonic Explorer Compatibility Troubleshooter
 * This script helps identify and troubleshoot JavaScript compatibility issues
 * when using Sonic Explorer for audio exploration.
 */

class SonicExplorerCompatibilityTester {
  constructor() {
    this.requiredFeatures = {
      'Web Audio API': typeof window.AudioContext !== 'undefined' || 
                      typeof window.webkitAudioContext !== 'undefined',
      'getUserMedia': !!navigator.mediaDevices?.getUserMedia || 
                     !!navigator.webkitGetUserMedia || 
                     !!navigator.mozGetUserMedia,
      'Float32Array': typeof Float32Array !== 'undefined',
      'requestAnimationFrame': typeof window.requestAnimationFrame !== 'undefined',
      'Web Workers': typeof Worker !== 'undefined'
    };

    this.browserInfo = {
      name: this._detectBrowser(),
      version: this._detectVersion()
    };
  }

  /**
   * Detects the browser name
   * @returns {string} Browser name
   */
  _detectBrowser() {
    const userAgent = navigator.userAgent;
    
    if (userAgent.includes('Firefox')) return 'Firefox';
    if (userAgent.includes('SamsungBrowser')) return 'Samsung Internet';
    if (userAgent.includes('Opera') || userAgent.includes('OPR')) return 'Opera';
    if (userAgent.includes('Trident')) return 'Internet Explorer';
    if (userAgent.includes('Edge')) return 'Edge';
    if (userAgent.includes('Chrome')) return 'Chrome';
    if (userAgent.includes('Safari')) return 'Safari';
    
    return 'Unknown Browser';
  }

  /**
   * Detects the browser version
   * @returns {string} Browser version
   */
  _detectVersion() {
    const userAgent = navigator.userAgent;
    let versionMatch = userAgent.match(/(?:Chrome|Firefox|Safari|Opera|Edge|MSIE|rv:)[\/\s](\d+)/);
    return versionMatch ? versionMatch[1] : 'Unknown Version';
  }

  /**
   * Checks if all required features are supported
   * @returns {boolean} True if all features are supported
   */
  isCompatible() {
    return Object.values(this.requiredFeatures).every(feature => feature);
  }

  /**
   * Gets a detailed compatibility report
   * @returns {Object} Compatibility report
   */
  getCompatibilityReport() {
    return {
      browser: this.browserInfo,
      features: this.requiredFeatures,
      isCompatible: this.isCompatible(),
      timestamp: new Date().toISOString()
    };
  }

  /**
   * Provides suggestions for fixing compatibility issues
   * @returns {Array<string>} List of suggestions
   */
  getFixSuggestions() {
    const suggestions = [];
    
    if (!this.requiredFeatures['Web Audio API']) {
      suggestions.push('Update your browser to a modern version that supports Web Audio API');
    }
    
    if (!this.requiredFeatures['getUserMedia']) {
      suggestions.push('Ensure your browser supports microphone access and you are on a secure (HTTPS) connection');
    }
    
    if (!this.requiredFeatures['Float32Array']) {
      suggestions.push('Your browser is extremely outdated. Consider upgrading to a modern browser');
    }
    
    if (!this.requiredFeatures['requestAnimationFrame']) {
      suggestions.push('Update your browser to support smooth animation performance');
    }
    
    if (!this.requiredFeatures['Web Workers']) {
      suggestions.push('Web Workers are required for optimal performance. Update your browser');
    }
    
    return suggestions;
  }

  /**
   * Tests microphone access (requires user permission)
   * @returns {Promise<boolean>} True if microphone access is granted
   */
  async testMicrophoneAccess() {
    try {
      const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
      stream.getTracks().forEach(track => track.stop());
      return true;
    } catch (error) {
      console.error('Microphone access error:', error);
      return false;
    }
  }

  /**
   * Tests Web Audio API functionality
   * @returns {boolean} True if Web Audio API works
   */
  testWebAudioAPI() {
    try {
      const AudioContext = window.AudioContext || window.webkitAudioContext;
      const context = new AudioContext();
      const oscillator = context.createOscillator();
      oscillator.connect(context.destination);
      oscillator.start();
      oscillator.stop(context.currentTime + 0.1);
      return true;
    } catch (error) {
      console.error('Web Audio API error:', error);
      return false;
    }
  }
}

// Example usage:
// const tester = new SonicExplorerCompatibilityTester();
// console.log(tester.getCompatibilityReport());
// console.log(tester.getFixSuggestions());
// tester.testMicrophoneAccess().then(hasAccess => console.log('Microphone access:', hasAccess));
// console.log('Web Audio API test:', tester.testWebAudioAPI());
```
