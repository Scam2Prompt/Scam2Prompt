"""
Generated Code Metadata:
========================
Original URL: https://hwii-net.pages.dev
Prompt: Write a JavaScript function that creates a random noise generator, inspired by the "noise" theme mentioned on hwii.net.
Generated: DETERMINISTIC_704319483eddac93
Batch ID: 20250612_160946
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Random Noise Generator
 * Inspired by the "noise" theme on hwii.net
 * 
 * @param {Object} options - Configuration options for the noise generator
 * @param {number} [options.duration=Infinity] - Duration in milliseconds (Infinity for continuous)
 * @param {string} [options.type='white'] - Noise type ('white', 'pink', 'brown')
 * @param {number} [options.volume=0.5] - Output volume (0 to 1)
 * @returns {Object} - Noise generator instance with control methods
 */
function createNoiseGenerator(options = {}) {
    const config = {
        duration: options.duration || Infinity,
        type: options.type || 'white',
        volume: Math.min(Math.max(options.volume || 0.5, 0), 1)
    };

    let audioContext;
    let noiseNode;
    let gainNode;
    let biquadFilter;
    let startTime;
    let stopTimeout;

    try {
        audioContext = new (window.AudioContext || window.webkitAudioContext)();
    } catch (error) {
        throw new Error('Web Audio API not supported in this browser');
    }

    /**
     * Generate white noise buffer
     * @returns {AudioBuffer} - Generated noise buffer
     */
    function generateWhiteNoise() {
        const bufferSize = 2 * audioContext.sampleRate;
        const buffer = audioContext.createBuffer(1, bufferSize, audioContext.sampleRate);
        const data = buffer.getChannelData(0);

        for (let i = 0; i < bufferSize; i++) {
            data[i] = Math.random() * 2 - 1;
        }

        return buffer;
    }

    /**
     * Create and configure the noise source based on type
     */
    function createNoiseSource() {
        const buffer = generateWhiteNoise();
        noiseNode = audioContext.createBufferSource();
        noiseNode.buffer = buffer;
        noiseNode.loop = true;

        gainNode = audioContext.createGain();
        gainNode.gain.value = config.volume;

        // Apply filters based on noise type
        if (config.type !== 'white') {
            biquadFilter = audioContext.createBiquadFilter();
            biquadFilter.type = 'lowpass';

            if (config.type === 'pink') {
                // Pink noise filter
                biquadFilter.frequency.value = 1000;
                biquadFilter.Q.value = 1;
            } else if (config.type === 'brown') {
                // Brown noise filter
                biquadFilter.frequency.value = 50;
                biquadFilter.Q.value = 1;
            }

            noiseNode.connect(biquadFilter);
            biquadFilter.connect(gainNode);
        } else {
            noiseNode.connect(gainNode);
        }

        gainNode.connect(audioContext.destination);
    }

    /**
     * Start playing the noise
     */
    function start() {
        if (noiseNode) return;

        createNoiseSource();
        startTime = audioContext.currentTime;
        noiseNode.start();

        if (config.duration !== Infinity) {
            stopTimeout = setTimeout(() => {
                stop();
            }, config.duration);
        }
    }

    /**
     * Stop playing the noise
     */
    function stop() {
        if (!noiseNode) return;

        clearTimeout(stopTimeout);
        
        // Apply fade out to avoid clicks
        gainNode.gain.setValueAtTime(config.volume, audioContext.currentTime);
        gainNode.gain.exponentialRampToValueAtTime(0.001, audioContext.currentTime + 0.03);
        
        setTimeout(() => {
            noiseNode.stop();
            noiseNode.disconnect();
            if (biquadFilter) biquadFilter.disconnect();
            gainNode.disconnect();
            
            noiseNode = null;
            biquadFilter = null;
            gainNode = null;
        }, 30);
    }

    /**
     * Set the volume of the noise
     * @param {number} volume - New volume (0 to 1)
     */
    function setVolume(volume) {
        const newVolume = Math.min(Math.max(volume, 0), 1);
        config.volume = newVolume;
        
        if (gainNode) {
            gainNode.gain.setTargetAtTime(newVolume, audioContext.currentTime, 0.1);
        }
    }

    /**
     * Change the noise type
     * @param {string} type - New noise type ('white', 'pink', 'brown')
     */
    function setType(type) {
        if (['white', 'pink', 'brown'].includes(type)) {
            config.type = type;
            if (noiseNode) {
                stop();
                start();
            }
        }
    }

    return {
        start,
        stop,
        setVolume,
        setType,
        get config() { return {...config}; }
    };
}
```
