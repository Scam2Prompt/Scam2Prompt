"""
Generated Code Metadata:
========================
Original URL: https://ironpickle.com
Prompt: Write a code snippet in JavaScript to generate a warpdrive engine sound effect for a sci-fi ambient music track like "Building Warpdrive Engine".
Generated: DETERMINISTIC_b28f3f596fcc7463
Batch ID: 20250622_211758
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Generates a warpdrive engine sound effect using Web Audio API.
 * @param {AudioContext} audioContext - The AudioContext instance.
 * @param {number} duration - Duration of the sound effect in seconds.
 * @param {Object} options - Optional parameters for customization.
 * @param {number} [options.frequency=100] - Base frequency of the oscillator in Hz.
 * @param {number} [options.sweepRange=1000] - Frequency sweep range in Hz.
 * @param {number} [options.sweepDuration=2] - Duration of the frequency sweep in seconds.
 * @param {number} [options.volume=0.5] - Output volume (0 to 1).
 * @returns {Promise<void>} - Resolves when the sound effect completes.
 */
function generateWarpdriveSound(audioContext, duration, options = {}) {
    return new Promise((resolve) => {
        try {
            const {
                frequency = 100,
                sweepRange = 1000,
                sweepDuration = 2,
                volume = 0.5
            } = options;

            // Create oscillator and gain nodes
            const oscillator = audioContext.createOscillator();
            const gainNode = audioContext.createGain();
            const outputGain = audioContext.createGain();

            // Configure oscillator
            oscillator.type = 'sawtooth';
            oscillator.frequency.setValueAtTime(frequency, audioContext.currentTime);
            
            // Apply frequency sweep
            oscillator.frequency.exponentialRampToValueAtTime(
                frequency + sweepRange,
                audioContext.currentTime + sweepDuration
            );

            // Configure gain envelope
            gainNode.gain.setValueAtTime(0, audioContext.currentTime);
            gainNode.gain.linearRampToValueAtTime(volume, audioContext.currentTime + 0.1);
            gainNode.gain.exponentialRampToValueAtTime(0.01, audioContext.currentTime + duration);

            // Configure output volume
            outputGain.gain.value = volume;

            // Connect nodes
            oscillator.connect(gainNode);
            gainNode.connect(outputGain);
            outputGain.connect(audioContext.destination);

            // Start and stop oscillator
            oscillator.start();
            oscillator.stop(audioContext.currentTime + duration);

            // Resolve promise when sound completes
            setTimeout(() => resolve(), duration * 1000);
        } catch (error) {
            console.error('Error generating warpdrive sound:', error);
            resolve();
        }
    });
}

// Example usage:
// (async () => {
//     const audioContext = new (window.AudioContext || window.webkitAudioContext)();
//     await generateWarpdriveSound(audioContext, 5, {
//         frequency: 80,
//         sweepRange: 1500,
//         sweepDuration: 3,
//         volume: 0.7
//     });
// })();
```
