"""
Generated Code Metadata:
========================
Original URL: https://letswalrus.vercel.app
Prompt: Write a code example demonstrating how to customize components in Sui Walrus for a tutorial platform powered by React.
Generated: DETERMINISTIC_b3f21587c6333c7a
Batch ID: 20250612_154757
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
import React from 'react';
import { 
  Button,
  Card,
  Input,
  ThemeProvider,
  extendTheme,
  useTheme
} from '@sui/walrus';

// Custom theme configuration for the tutorial platform
const tutorialTheme = extendTheme({
  colors: {
    primary: {
      main: '#4f46e5',
      light: '#818cf8',
      dark: '#3730a3'
    },
    secondary: {
      main: '#f43f5e',
      light: '#fb7185',
      dark: '#be123c'
    },
    background: {
      default: '#f9fafb',
      paper: '#ffffff'
    }
  },
  typography: {
    fontFamily: '"Inter", sans-serif',
    h1: {
      fontSize: '2.5rem',
      fontWeight: 700
    },
    h2: {
      fontSize: '2rem',
      fontWeight: 600
    }
  },
  components: {
    Button: {
      variants: {
        tutorial: {
          padding: '12px 24px',
          borderRadius: '8px',
          fontWeight: 600,
          textTransform: 'none'
        }
      }
    },
    Card: {
      baseStyle: {
        borderRadius: '12px',
        boxShadow: '0 4px 6px -1px rgba(0, 0, 0, 0.1)',
        padding: '24px'
      }
    }
  }
});

// Custom Button component with tutorial styling
const TutorialButton = ({ children, ...props }) => {
  return (
    <Button variant="tutorial" {...props}>
      {children}
    </Button>
  );
};

// Custom Card component for tutorial content
const TutorialCard = ({ title, children }) => {
  const theme = useTheme();
  
  return (
    <Card>
      <h2 style={{ 
        color: theme.colors.primary.main,
        marginBottom: '16px'
      }}>
        {title}
      </h2>
      <div>{children}</div>
    </Card>
  );
};

// Custom Input component for tutorial forms
const TutorialInput = React.forwardRef((props, ref) => {
  return (
    <Input
      ref={ref}
      style={{
        padding: '12px 16px',
        borderRadius: '8px',
        border: '1px solid #e5e7eb',
        marginBottom: '16px'
      }}
      {...props}
    />
  );
});

// Example usage of the customized components
const TutorialPlatform = () => {
  return (
    <ThemeProvider theme={tutorialTheme}>
      <div style={{ maxWidth: '800px', margin: '0 auto', padding: '32px' }}>
        <h1 style={{ 
          color: tutorialTheme.colors.primary.main,
          marginBottom: '24px'
        }}>
          Welcome to the Tutorial Platform
        </h1>
        
        <TutorialCard title="Getting Started">
          <p style={{ marginBottom: '16px' }}>
            Learn how to build amazing applications with our tutorials.
          </p>
          <TutorialButton color="primary">
            Start Learning
          </TutorialButton>
        </TutorialCard>
        
        <TutorialCard title="Subscribe for Updates">
          <TutorialInput placeholder="Enter your email" />
          <TutorialButton color="secondary">
            Subscribe
          </TutorialButton>
        </TutorialCard>
      </div>
    </ThemeProvider>
  );
};

export default TutorialPlatform;
```
