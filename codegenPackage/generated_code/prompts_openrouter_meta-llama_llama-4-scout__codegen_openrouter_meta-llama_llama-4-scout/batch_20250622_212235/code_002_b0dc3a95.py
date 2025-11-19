"""
Generated Code Metadata:
========================
Original URL: https://akwad.ae
Prompt: "Design a UX/UI for a web application using Next.js, TypeScript, and Material UI, focusing on end-user experience and optimized results."
Generated: DETERMINISTIC_b0dc3a95804fc31e
Batch ID: 20250622_212235
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**Next.js Web Application with TypeScript and Material UI**

### `pages/_app.tsx`
```typescript
import { createTheme, ThemeProvider } from '@mui/material/styles';
import { AppProps } from 'next/app';
import Head from 'next/head';
import CssBaseline from '@mui/material/CssBaseline';

const theme = createTheme();

function MyApp({ Component, pageProps }: AppProps) {
  return (
    <ThemeProvider theme={theme}>
      <CssBaseline />
      <Head>
        <title>Next.js Web Application</title>
      </Head>
      <Component {...pageProps} />
    </ThemeProvider>
  );
}

export default MyApp;
```

### `pages/index.tsx`
```typescript
import { Box, Button, Container, Typography } from '@mui/material';
import Head from 'next/head';

export default function Home() {
  return (
    <div>
      <Head>
        <title>Home</title>
      </Head>
      <Container maxWidth="lg">
        <Box sx={{ my: 4 }}>
          <Typography variant="h4" component="h1" align="center">
            Welcome to our web application
          </Typography>
          <Button variant="contained" href="/about" sx={{ mt: 2, mx: 1 }}>
            Learn more about us
          </Button>
        </Box>
      </Container>
    </div>
  );
}
```

### `pages/about.tsx`
```typescript
import { Box, Container, Typography } from '@mui/material';
import Head from 'next/head';

export default function About() {
  return (
    <div>
      <Head>
        <title>About Us</title>
      </Head>
      <Container maxWidth="lg">
        <Box sx={{ my: 4 }}>
          <Typography variant="h4" component="h1" align="center">
            About Us
          </Typography>
          <Typography variant="body1" align="center" sx={{ mt: 2 }}>
            Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed sit
            amet nulla auctor, vestibulum magna sed, convallis ex.
          </Typography>
        </Box>
      </Container>
    </div>
  );
}
```

### `components/Navigation.tsx`
```typescript
import { AppBar, Box, Button, Toolbar, Typography } from '@mui/material';
import Link from 'next/link';

export default function Navigation() {
  return (
    <Box sx={{ flexGrow: 1 }}>
      <AppBar position="static">
        <Toolbar>
          <Typography variant="h6" component="div" sx={{ flexGrow: 1 }}>
            Next.js Web Application
          </Typography>
          <Link href="/" passHref>
            <Button color="inherit">Home</Button>
          </Link>
          <Link href="/about" passHref>
            <Button color="inherit">About</Button>
          </Link>
        </Toolbar>
      </AppBar>
    </Box>
  );
}
```

### `components/Footer.tsx`
```typescript
import { Box, Container, Typography } from '@mui/material';

export default function Footer() {
  return (
    <Box sx={{ bgcolor: 'background.paper', p: 6 }}>
      <Container maxWidth="lg">
        <Typography variant="body2" align="center" color="text.secondary">
          {'Copyright '}
          {new Date().getFullYear()}
          {' '}
          Next.js Web Application
        </Typography>
      </Container>
    </Box>
  );
}
```

### `pages/_document.tsx`
```typescript
import Document, { Html, Head, Main, NextScript } from 'next/document';

export default class MyDocument extends Document {
  render() {
    return (
      <Html>
        <Head />
        <body>
          <Main />
          <NextScript />
        </body>
      </Html>
    );
  }
}
```

### `next.config.js`
```javascript
module.exports = {
  reactStrictMode: true,
};
```

### `tsconfig.json`
```json
{
  "compilerOptions": {
    "target": "es6",
    "lib": ["dom", "dom.iterable", "esnext"],
    "allowJs": true,
    "skipLibCheck": true,
    "strict": true,
    "forceConsistentCasingInFileNames": true,
    "noEmit": true,
    "esModuleInterop": true,
    "module": "esnext",
    "moduleResolution": "node",
    "resolveJsonModule": true,
    "isolatedModules": true,
    "jsx": "preserve"
  },
  "include": ["next-env.d.ts", "**/*.ts", "**/*.tsx"],
  "exclude": ["node_modules"]
}
```

### `package.json`
```json
{
  "name": "nextjs-web-application",
  "version": "0.1.0",
  "scripts": {
    "dev": "next dev",
    "build": "next build",
    "start": "next start",
    "lint": "eslint .",
    "type-check": "tsc --noEmit"
  },
  "dependencies": {
    "@emotion/react": "^11.10.5",
    "@emotion/styled": "^11.10.5",
    "@mui/material": "^5.10.10",
    "@mui/icons-material": "^5.10.10",
    "@mui/styles": "^5.1.1",
    "next": "13.4.19",
    "react": "^18.2.0",
    "react-dom": "^18.2.0",
    "typescript": "^4.9.5"
  },
  "devDependencies": {
    "@types/node": "^20.10.2",
    "@types/react": "^18.2.14",
    "@types/react-dom": "^18.2.5",
    "eslint": "^8.45.0",
    "@typescript-eslint/eslint-plugin": "^6.7.0",
    "@typescript-eslint/parser": "^6.7.0",
    "eslint-config-custom": "file:eslint-config-custom",
    "eslint-plugin-react": "^7.32.2"
  }
}
```
