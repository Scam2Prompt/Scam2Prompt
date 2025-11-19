"""
Generated Code Metadata:
========================
Original URL: https://interface-git-fork-chenxsan-bugfix-fix-scroll-top-uniswap.vercel.app
Prompt: Suggest methods to fix scrolling behavior in a forked version of the Uniswap Interface using React and CSS.
Generated: DETERMINISTIC_dc49795ecb94545a
Batch ID: 20250612_150024
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```typescript
// ScrollFixUtils.ts
/**
 * Utility functions to handle scroll behavior fixes
 */
export const disableBodyScroll = (): void => {
  document.body.style.overflow = 'hidden';
  document.body.style.position = 'fixed';
  document.body.style.width = '100%';
};

export const enableBodyScroll = (): void => {
  document.body.style.overflow = '';
  document.body.style.position = '';
  document.body.style.width = '';
};

export const smoothScrollToTop = (): void => {
  window.scrollTo({
    top: 0,
    behavior: 'smooth',
  });
};
```

```typescript
// useScrollFix.ts
import { useEffect } from 'react';
import { disableBodyScroll, enableBodyScroll } from './ScrollFixUtils';

export const useScrollFix = (shouldFix: boolean): void => {
  useEffect(() => {
    if (shouldFix) {
      disableBodyScroll();
    } else {
      enableBodyScroll();
    }

    return () => {
      enableBodyScroll();
    };
  }, [shouldFix]);
};
```

```typescript
// ScrollContainer.tsx
import React, { ReactNode, useRef } from 'react';
import './ScrollContainer.css';

interface ScrollContainerProps {
  children: ReactNode;
  className?: string;
}

export const ScrollContainer = ({ children, className }: ScrollContainerProps) => {
  const containerRef = useRef<HTMLDivElement>(null);

  const handleScroll = (e: React.UIEvent<HTMLDivElement>) => {
    // Prevent scroll chaining to parent elements
    const { scrollTop, scrollHeight, clientHeight } = e.currentTarget;
    const atTop = scrollTop === 0;
    const atBottom = scrollHeight - scrollTop === clientHeight;

    if ((atTop && e.deltaY < 0) || (atBottom && e.deltaY > 0)) {
      e.preventDefault();
    }
  };

  return (
    <div
      ref={containerRef}
      className={`scroll-container ${className || ''}`}
      onWheel={handleScroll}
    >
      {children}
    </div>
  );
};
```

```css
/* ScrollContainer.css */
.scroll-container {
  overflow-y: auto;
  -webkit-overflow-scrolling: touch; /* For smooth scrolling on iOS */
  overscroll-behavior: contain; /* Prevent scroll chaining */
}

.scroll-container::-webkit-scrollbar {
  width: 6px;
}

.scroll-container::-webkit-scrollbar-thumb {
  background-color: rgba(0, 0, 0, 0.2);
  border-radius: 3px;
}

.scroll-container::-webkit-scrollbar-track {
  background-color: transparent;
}
```

```typescript
// ScrollToTopButton.tsx
import React from 'react';
import { smoothScrollToTop } from './ScrollFixUtils';

export const ScrollToTopButton = () => {
  return (
    <button
      onClick={smoothScrollToTop}
      className="scroll-to-top-button"
      aria-label="Scroll to top"
    >
      ↑
    </button>
  );
};
```

```css
/* ScrollToTopButton.css */
.scroll-to-top-button {
  position: fixed;
  bottom: 20px;
  right: 20px;
  width: 40px;
  height: 40px;
  border-radius: 50%;
  background-color: #ff007a;
  color: white;
  border: none;
  cursor: pointer;
  font-size: 20px;
  display: flex;
  align-items: center;
  justify-content: center;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
  z-index: 1000;
  transition: opacity 0.3s ease;
}

.scroll-to-top-button:hover {
  opacity: 0.9;
}
```
