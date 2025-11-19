"""
Generated Code Metadata:
========================
Original URL: https://interface-git-fork-chenxsan-bugfix-fix-scroll-top-uniswap.vercel.app
Prompt: Generate code to debug scrolling issues in a React-based application, referencing the Uniswap Interface as an example.
Generated: DETERMINISTIC_e95c2d3dfa7a2c8a
Batch ID: 20250612_150024
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```typescript
import React, { useEffect, useRef, useState } from 'react';
import { FixedSizeList, ListOnScrollProps } from 'react-window';
import AutoSizer from 'react-virtualized-auto-sizer';
import debounce from 'lodash/debounce';

interface ScrollDebuggerProps {
  listData: any[];
  itemSize?: number;
  onScroll?: (props: ListOnScrollProps) => void;
}

const ScrollDebugger: React.FC<ScrollDebuggerProps> = ({
  listData,
  itemSize = 56,
  onScroll,
}) => {
  const listRef = useRef<FixedSizeList>(null);
  const [scrollInfo, setScrollInfo] = useState<ListOnScrollProps | null>(null);
  const [scrollDirection, setScrollDirection] = useState<'up' | 'down' | null>(null);
  const [performanceMetrics, setPerformanceMetrics] = useState({
    fps: 0,
    lastRenderTime: 0,
  });

  // Debounced scroll handler to avoid performance issues
  const handleScroll = debounce((props: ListOnScrollProps) => {
    setScrollInfo(props);
    setScrollDirection(props.scrollDirection);
    onScroll?.(props);

    // Performance monitoring
    const now = performance.now();
    const fps = 1000 / (now - performanceMetrics.lastRenderTime);
    setPerformanceMetrics({
      fps: Math.round(fps),
      lastRenderTime: now,
    });
  }, 16); // ~60fps

  // Reset scroll position when data changes
  useEffect(() => {
    listRef.current?.scrollTo(0);
  }, [listData]);

  // Debug rendering
  useEffect(() => {
    console.log('Scroll Debug Info:', {
      scrollInfo,
      scrollDirection,
      performanceMetrics,
    });
  }, [scrollInfo, scrollDirection, performanceMetrics]);

  const Row = ({ index, style }: { index: number; style: React.CSSProperties }) => (
    <div style={style}>
      {listData[index]}
    </div>
  );

  return (
    <div className="scroll-debug-container">
      <div className="scroll-debug-info">
        <p>Scroll Direction: {scrollDirection || 'none'}</p>
        <p>FPS: {performanceMetrics.fps}</p>
        {scrollInfo && (
          <>
            <p>Offset: {scrollInfo.scrollOffset}</p>
            <p>Update Was Requested: {scrollInfo.scrollUpdateWasRequested.toString()}</p>
          </>
        )}
      </div>

      <div className="list-container">
        <AutoSizer>
          {({ height, width }) => (
            <FixedSizeList
              ref={listRef}
              height={height}
              width={width}
              itemSize={itemSize}
              itemCount={listData.length}
              onScroll={handleScroll}
              overscanCount={5} // Adjust based on performance needs
            >
              {Row}
            </FixedSizeList>
          )}
        </AutoSizer>
      </div>
    </div>
  );
};

export default ScrollDebugger;
```

```typescript
// Example usage in a parent component
import React from 'react';
import ScrollDebugger from './ScrollDebugger';

const App: React.FC = () => {
  const mockData = Array.from({ length: 1000 }, (_, i) => `Item ${i + 1}`);

  return (
    <div style={{ height: '100vh', width: '100vw' }}>
      <h1>Scroll Debugger Example</h1>
      <ScrollDebugger 
        listData={mockData}
        onScroll={(props) => {
          // Additional scroll handling logic can go here
          console.log('Parent scroll handler:', props);
        }}
      />
    </div>
  );
};

export default App;
```

```css
/* Optional styling for the debugger */
.scroll-debug-container {
  display: flex;
  flex-direction: column;
  height: 100%;
}

.scroll-debug-info {
  padding: 1rem;
  background: #f5f5f5;
  border-bottom: 1px solid #ddd;
  font-family: monospace;
}

.list-container {
  flex: 1;
  overflow: hidden;
}
```
