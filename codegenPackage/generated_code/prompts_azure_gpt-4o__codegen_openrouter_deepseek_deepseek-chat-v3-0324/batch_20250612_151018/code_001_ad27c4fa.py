"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-140--keen-roentgen-cafcb7.netlify.app
Prompt: Create a custom MDX note component similar to the one described in Joe Previte's article "Writing a Custom Note Component for MDX." Ensure the component supports custom styling and Markdown syntax.
Generated: DETERMINISTIC_ad27c4fa48fb2e29
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
import { MDXProvider } from '@mdx-js/react';
import styled, { css } from 'styled-components';

type NoteVariant = 'info' | 'warning' | 'error' | 'success';

interface NoteProps {
  variant?: NoteVariant;
  children: React.ReactNode;
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
};

const NoteContainer = styled.div<{ variant: NoteVariant }>`
  padding: 1rem;
  margin: 1rem 0;
  border-radius: 0.375rem;
  ${({ variant }) => variantStyles[variant]}

  & > *:first-child {
    margin-top: 0;
  }

  & > *:last-child {
    margin-bottom: 0;
  }
`;

const NoteTitle = styled.div`
  font-weight: 600;
  margin-bottom: 0.5rem;
`;

const titleMap: Record<NoteVariant, string> = {
  info: 'Info',
  warning: 'Warning',
  error: 'Error',
  success: 'Success',
};

const Note: React.FC<NoteProps> = ({ variant = 'info', children }) => {
  return (
    <NoteContainer variant={variant}>
      <NoteTitle>{titleMap[variant]}</NoteTitle>
      {children}
    </NoteContainer>
  );
};

const components = {
  Note,
};

interface MDXNoteProviderProps {
  children: React.ReactNode;
}

export const MDXNoteProvider: React.FC<MDXNoteProviderProps> = ({ children }) => {
  return <MDXProvider components={components}>{children}</MDXProvider>;
};

export default Note;
```
