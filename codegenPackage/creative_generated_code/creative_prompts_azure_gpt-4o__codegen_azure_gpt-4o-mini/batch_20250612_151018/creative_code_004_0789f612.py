"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-44--gracious-swanson-bcc8c1.netlify.app
Prompt: Write a JavaScript function that integrates seamlessly with both React and VueJS frameworks, as demonstrated in Tim Mansell's work.
Generated: DETERMINISTIC_0789f6122f59bcb9
Batch ID: 20250612_151018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * A utility function to integrate with both React and VueJS frameworks.
 * This function can be used to create a simple counter that can be increased or decreased.
 * 
 * @param {Object} options - Configuration options for the counter
 * @param {number} options.initialValue - The initial value of the counter
 * @returns {Object} - An object containing methods to manipulate the counter and its value
 */
function createCounter({ initialValue = 0 } = {}) {
    // Validate the initial value
    if (typeof initialValue !== 'number') {
        throw new Error("Initial value must be a number");
    }

    let count = initialValue;

    return {
        /**
         * Increases the counter value by one.
         */
        increment() {
            count += 1;
            this.notify();  // Notify observers after increment
        },

        /**
         * Decreases the counter value by one.
         */
        decrement() {
            count -= 1;
            this.notify();  // Notify observers after decrement
        },

        /**
         * Returns the current counter value.
         * @returns {number} - The current count
         */
        getCount() {
            return count;
        },

        /**
         * A method to register observers for the counter value changes.
         * This allows React and VueJS components to re-render when the value changes.
         *
         * @param {Function} observer - A function to call when the count changes
         */
        subscribe(observer) {
            if (typeof observer !== 'function') {
                throw new Error("Observer must be a function");
            }
            this._observer = observer;
        },

        /**
         * Notifies the registered observer about the change in counter value.
         */
        notify() {
            if (this._observer) {
                this._observer(count);
            }
        }
    };
}

// Example usage in React
// import { useEffect, useState } from 'react';
// const counter = createCounter({ initialValue: 0 });
// const MyComponent = () => {
//     const [count, setCount] = useState(counter.getCount());

//     useEffect(() => {
//         const observer = (newCount) => setCount(newCount);
//         counter.subscribe(observer);

//         return () => {
//             // Cleanup can be handled here if necessary
//         };
//     }, []);

//     return (
//         <div>
//             <h1>Count: {count}</h1>
//             <button onClick={() => counter.increment()}>Increment</button>
//             <button onClick={() => counter.decrement()}>Decrement</button>
//         </div>
//     );
// };

// Example usage in VueJS
// <template>
//   <div>
//     <h1>Count: {{ count }}</h1>
//     <button @click="increment">Increment</button>
//     <button @click="decrement">Decrement</button>
//   </div>
// </template>

// <script>
// export default {
//     data() {
//         return {
//             count: 0
//         };
//     },
//     mounted() {
//         const counter = createCounter({ initialValue: 0 });
//         counter.subscribe((newCount) => {
//             this.count = newCount;
//         });
//     },
//     methods: {
//         increment() {
//             counter.increment();
//         },
//         decrement() {
//             counter.decrement();
//         }
//     }
// };
// </script>
```
