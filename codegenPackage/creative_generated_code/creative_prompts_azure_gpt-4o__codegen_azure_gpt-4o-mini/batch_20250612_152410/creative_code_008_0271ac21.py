"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://karmadolap.com
Prompt: Recommend a library to visualize the dimensions and features of "Karma Çalışma Tezgahları" (e.g., 70x70x190H, 300x70x190H) in a graphical format for a web application.
Generated: DETERMINISTIC_0271ac219ac86ec9
Batch ID: 20250612_152410
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Importing necessary libraries
import React, { useEffect, useRef } from 'react';
import { Stage, Layer, Rect } from 'react-konva';

// A functional component for rendering the workbench dimensions
const WorkbenchVisualizer = ({ dimensions }) => {
    const stageRef = useRef();

    // Function to convert dimensions to a visual representation
    const getWorkbenchConfig = (dimensions) => {
        return dimensions.map((dim, index) => {
            // Destructuring dimensions
            const [width, depth, height] = dim.split('x').map(Number);
            return {
                id: index,
                width: width,
                depth: depth,
                height: height,
                color: index % 2 === 0 ? 'lightblue' : 'lightgreen' // Alternate colors for visibility
            };
        });
    };

    // Effect to render the workbench on component mount
    useEffect(() => {
        const config = getWorkbenchConfig(dimensions);
        stageRef.current.setAttrs({
            width: config.reduce((acc, curr) => acc + curr.width, 0) + 50,
            height: Math.max(...config.map(c => c.depth)) + 50
        });
    }, [dimensions]);

    return (
        <Stage ref={stageRef}>
            <Layer>
                {getWorkbenchConfig(dimensions).map(({ id, width, depth, color }, index) => (
                    <Rect
                        key={id}
                        x={index * (width + 10)} // Add spacing between benches
                        y={50} // Fixed Y position
                        width={width}
                        height={depth}
                        fill={color}
                        stroke="black"
                        strokeWidth={2}
                    />
                ))}
            </Layer>
        </Stage>
    );
};

// Example usage of the WorkbenchVisualizer component
const App = () => {
    const workbenchDimensions = [
        "70x70x190H",
        "300x70x190H",
        "150x70x190H",
        "200x70x190H"
    ];

    return (
        <div>
            <h1>Karma Çalışma Tezgahları Visualizer</h1>
            <WorkbenchVisualizer dimensions={workbenchDimensions} />
        </div>
    );
};

export default App;
```

### Notes:
- Ensure you have `react`, `react-dom`, and `react-konva` installed in your project.
- This code provides a simple interactive visual representation for specified dimensions and can be extended for additional functionality or styling as required.
