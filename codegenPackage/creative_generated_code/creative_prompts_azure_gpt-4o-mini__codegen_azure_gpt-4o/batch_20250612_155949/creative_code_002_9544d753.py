"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metarestore.vercel.app
Prompt: Can you provide examples of how to use Next.js features mentioned on the MetaRestore documentation page?
Generated: DETERMINISTIC_9544d753361b2999
Batch ID: 20250612_155949
URLs Found: 3
Malicious URLs: 0

Oracle Results:
{
  "https://api.example.com/metarestore": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://api.example.com/metarestore/${id}`": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://api.example.com/metarestore/ids": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```javascript
// Example usage of Next.js features based on MetaRestore documentation

// pages/index.js - Example of static site generation (SSG) with `getStaticProps`
import Head from 'next/head';

export async function getStaticProps() {
  // Simulate fetching data for static generation
  const data = await fetch('https://api.example.com/metarestore').then((res) =>
    res.json()
  );

  return {
    props: {
      metaData: data,
    },
  };
}

export default function Home({ metaData }) {
  return (
    <>
      <Head>
        <title>MetaRestore Example</title>
        <meta name="description" content="A Next.js example using MetaRestore" />
      </Head>
      <main>
        <h1>MetaRestore Data</h1>
        <pre>{JSON.stringify(metaData, null, 2)}</pre>
      </main>
    </>
  );
}

// pages/api/metaData.js - Example of API route implementation
export default async function handler(req, res) {
  try {
    // Simulate fetching metadata for the API response
    const metaData = await fetch('https://api.example.com/metarestore').then(
      (response) => response.json()
    );

    res.status(200).json(metaData);
  } catch (error) {
    console.error('Error fetching metadata:', error);
    res.status(500).json({ error: 'Failed to fetch metadata' });
  }
}

// pages/dynamic/[id].js - Example of dynamic routing with `getStaticPaths` and `getStaticProps`
import Head from 'next/head';

export async function getStaticPaths() {
  // Simulate fetching IDs for dynamic paths
  const data = await fetch('https://api.example.com/metarestore/ids').then((res) =>
    res.json()
  );

  const paths = data.ids.map((id) => ({ params: { id: id.toString() } }));

  return {
    paths,
    fallback: false, // If true, paths not returned by `getStaticPaths` will be generated on-demand
  };
}

export async function getStaticProps({ params }) {
  const { id } = params;

  // Simulate fetching data for a specific dynamic page
  const dynamicData = await fetch(
    `https://api.example.com/metarestore/${id}`
  ).then((res) => res.json());

  return {
    props: {
      dynamicData,
    },
  };
}

export default function DynamicPage({ dynamicData }) {
  return (
    <>
      <Head>
        <title>Dynamic MetaRestore - {dynamicData.title}</title>
        <meta name="description" content={dynamicData.description} />
      </Head>
      <main>
        <h1>{dynamicData.title}</h1>
        <p>{dynamicData.content}</p>
      </main>
    </>
  );
}

// Components/MetaRestoreCard.js - Example of reusable component
import Link from 'next/link';

export default function MetaRestoreCard({ id, title, description }) {
  return (
    <div className="meta-card">
      <h2>{title}</h2>
      <p>{description}</p>
      <Link href={`/dynamic/${id}`}>View More</Link>
      <style jsx>{`
        .meta-card {
          border: 1px solid #ddd;
          padding: 16px;
          margin: 16px 0;
          border-radius: 8px;
        }
      `}</style>
    </div>
  );
}

// pages/metaList.js - Example of Client-side Rendering (CSR)
import { useState, useEffect } from 'react';
import MetaRestoreCard from '../components/MetaRestoreCard';

export default function MetaList() {
  const [metaDataList, setMetaDataList] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    async function fetchMetaData() {
      try {
        const response = await fetch('/api/metaData');
        const data = await response.json();
        setMetaDataList(data);
        setLoading(false);
      } catch (error) {
        console.error('Error fetching metadata:', error);
        setLoading(false);
      }
    }

    fetchMetaData();
  }, []);

  if (loading) {
    return <p>Loading...</p>;
  }

  return (
    <main>
      <h1>MetaRestore List</h1>
      {metaDataList.map((meta) => (
        <MetaRestoreCard
          key={meta.id}
          id={meta.id}
          title={meta.title}
          description={meta.description}
        />
      ))}
    </main>
  );
}
```
