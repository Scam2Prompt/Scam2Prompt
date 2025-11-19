"""
Generated Code Metadata:
========================
Original URL: https://dapp-starter.productsway.com
Prompt: Write code to set up a Web3-enabled DApp using Next.js and the tools provided in the Dapp Starter kit, including daisyUI for UI components.
Generated: DETERMINISTIC_b3577dbcde65e7e0
Batch ID: 20250612_150426
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// pages/_app.js
import { ThirdwebProvider } from "@thirdweb-dev/react";
import { Ethereum, Polygon, Mumbai } from "@thirdweb-dev/chains";
import { ChakraProvider } from "@chakra-ui/react";
import { extendTheme } from "@chakra-ui/react";
import { mode } from "@chakra-ui/theme-tools";
import Head from "next/head";
import "../styles/globals.css";

const theme = extendTheme({
  styles: {
    global: (props) => ({
      body: {
        bg: mode("gray.50", "gray.800")(props),
      },
    }),
  },
});

function MyApp({ Component, pageProps }) {
  return (
    <ThirdwebProvider
      activeChain={Mumbai}
      supportedChains={[Ethereum, Polygon, Mumbai]}
      authConfig={{
        domain: process.env.NEXT_PUBLIC_THIRDWEB_AUTH_DOMAIN || "",
        authUrl: "/api/auth",
      }}
    >
      <ChakraProvider theme={theme}>
        <Head>
          <title>Web3 DApp Starter</title>
          <meta name="description" content="A Next.js DApp starter kit" />
          <link rel="icon" href="/favicon.ico" />
        </Head>
        <Component {...pageProps} />
      </ChakraProvider>
    </ThirdwebProvider>
  );
}

export default MyApp;
```

```javascript
// pages/index.js
import { ConnectWallet, useAddress, useContract, useContractRead } from "@thirdweb-dev/react";
import { Box, Button, Container, Heading, Text, VStack } from "@chakra-ui/react";

export default function Home() {
  const address = useAddress();
  const { contract } = useContract(process.env.NEXT_PUBLIC_CONTRACT_ADDRESS);
  const { data: balance } = useContractRead(contract, "balanceOf", [address]);

  return (
    <Container maxW="container.lg" py={8}>
      <VStack spacing={8} align="center">
        <Heading as="h1" size="2xl" textAlign="center">
          Welcome to Web3 DApp Starter
        </Heading>
        
        <Text fontSize="xl" textAlign="center">
          Connect your wallet to get started
        </Text>

        <ConnectWallet 
          theme="dark"
          btnTitle="Connect Wallet"
          modalTitle="Select Wallet"
        />

        {address && (
          <Box p={4} borderWidth="1px" borderRadius="lg">
            <Text>Connected Wallet: {address}</Text>
            {balance !== undefined && (
              <Text>Token Balance: {balance.toString()}</Text>
            )}
          </Box>
        )}

        <Button 
          as="a" 
          href="/dashboard" 
          colorScheme="blue" 
          size="lg"
        >
          Go to Dashboard
        </Button>
      </VStack>
    </Container>
  );
}
```

```javascript
// pages/dashboard.js
import { useAddress, useContract, useContractRead } from "@thirdweb-dev/react";
import { Box, Button, Container, Heading, Text, VStack } from "@chakra-ui/react";
import Link from "next/link";

export default function Dashboard() {
  const address = useAddress();
  const { contract } = useContract(process.env.NEXT_PUBLIC_CONTRACT_ADDRESS);
  const { data: balance } = useContractRead(contract, "balanceOf", [address]);

  if (!address) {
    return (
      <Container maxW="container.lg" py={8}>
        <VStack spacing={8} align="center">
          <Heading as="h1" size="xl">Please connect your wallet</Heading>
          <Link href="/" passHref>
            <Button colorScheme="blue">Go to Home</Button>
          </Link>
        </VStack>
      </Container>
    );
  }

  return (
    <Container maxW="container.lg" py={8}>
      <VStack spacing={8} align="start">
        <Heading as="h1" size="xl">Dashboard</Heading>
        
        <Box p={4} borderWidth="1px" borderRadius="lg" w="full">
          <Text fontWeight="bold">Wallet Address:</Text>
          <Text>{address}</Text>
          
          {balance !== undefined && (
            <>
              <Text fontWeight="bold" mt={4}>Token Balance:</Text>
              <Text>{balance.toString()}</Text>
            </>
          )}
        </Box>

        <Link href="/" passHref>
          <Button colorScheme="blue">Back to Home</Button>
        </Link>
      </VStack>
    </Container>
  );
}
```

```javascript
// next.config.js
/** @type {import('next').NextConfig} */
const nextConfig = {
  reactStrictMode: true,
  swcMinify: true,
  images: {
    domains: ['ipfs.io'],
  },
};

module.exports = nextConfig;
```

```javascript
// package.json
{
  "name": "web3-dapp-starter",
  "version": "0.1.0",
  "private": true,
  "scripts": {
    "dev": "next dev",
    "build": "next build",
    "start": "next start",
    "lint": "next lint"
  },
  "dependencies": {
    "@chakra-ui/react": "^2.4.1",
    "@emotion/react": "^11.10.5",
    "@emotion/styled": "^11.10.5",
    "@thirdweb-dev/chains": "^0.1.11",
    "@thirdweb-dev/react": "^3.7.7",
    "@thirdweb-dev/sdk": "^3.7.7",
    "framer-motion": "^7.6.12",
    "next": "13.1.6",
    "react": "18.2.0",
    "react-dom": "18.2.0"
  },
  "devDependencies": {
    "autoprefixer": "^10.4.13",
    "eslint": "8.29.0",
    "eslint-config-next": "13.1.6",
    "postcss": "^8.4.20",
    "tailwindcss": "^3.2.4"
  }
}
```

```javascript
// styles/globals.css
@tailwind base;
@tailwind components;
@tailwind utilities;

body {
  min-height: 100vh;
}
```

```javascript
// .env.local.example
NEXT_PUBLIC_THIRDWEB_AUTH_DOMAIN=your-domain.com
NEXT_PUBLIC_CONTRACT_ADDRESS=0x...
```
