"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-137--keen-roentgen-cafcb7.netlify.app
Prompt: Create a custom MDX note component similar to the one described by Joe Previte in his article "Writing a Custom Note Component for MDX." Ensure the component supports customizable styles.
Generated: DETERMINISTIC_7853606154b22291
Batch ID: 20250612_151018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```typescript
import React from 'react';
import styled, { css } from 'styled-components';

type NoteVariant = 'info' | 'warning' | 'error' | 'success' | 'default';

interface NoteProps {
  variant?: NoteVariant;
  children: React.ReactNode;
  className?: string;
}

const variantStyles = {
  info: css`
    background-color: #e0f2fe;
    border-left: 4px solid #38bdf8;
    color: #0369a1;
  `,
  warning: css`
    background-color: #fef9c3;
    border-left: 4px solid #facc15;
    color: #854d0e;
  `,
  error: css`
    background-color: #fee2e2;
    border-left: 4px solid #f87171;
    color: #991b1b;
  `,
  success: css`
    background-color: #dcfce7;
    border-left: 4px solid #4ade80;
    color: #166534;
  `,
  default: css`
    background-color: #f3f4f6;
    border-left: 4px solid #9ca3af;
    color: #4b5563;
  `,
};

const StyledNote = styled.div<{ variant: NoteVariant }>`
  padding: 1rem;
  margin: 1rem 0;
  border-radius: 0 4px 4px 0;
  font-size: 0.95rem;
  line-height: 1.5;

  ${({ variant }) => variantStyles[variant]}

  & > :first-child {
    margin-top: 0;
  }

  & > :last-child {
    margin-bottom: 0;
  }
`;

const Note: React.FC<NoteProps> = ({
  variant = 'default',
  children,
  className,
}) => {
  return (
    <StyledNote variant={variant} className={className}>
      {children}
    </StyledNote>
  );
};

export default Note;
```
