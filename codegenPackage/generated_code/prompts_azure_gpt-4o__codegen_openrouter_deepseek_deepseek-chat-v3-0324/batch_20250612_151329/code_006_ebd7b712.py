"""
Generated Code Metadata:
========================
Original URL: https://lineage-ai.vercel.app
Prompt: Write code to display model metadata dynamically in a Next.js app after parsing a JSON file uploaded by the user, as described on the Lineage AI site.
Generated: DETERMINISTIC_ebd7b71269196892
Batch ID: 20250612_151329
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```typescript
// pages/index.tsx
import { useState, useCallback } from 'react';
import { NextPage } from 'next';
import Head from 'next/head';

interface ModelMetadata {
  name: string;
  version: string;
  description?: string;
  author?: string;
  created_at?: string;
  tags?: string[];
  parameters?: {
    [key: string]: any;
  };
}

const Home: NextPage = () => {
  const [metadata, setMetadata] = useState<ModelMetadata | null>(null);
  const [error, setError] = useState<string | null>(null);
  const [isLoading, setIsLoading] = useState(false);

  const handleFileUpload = useCallback(
    (event: React.ChangeEvent<HTMLInputElement>) => {
      const file = event.target.files?.[0];
      if (!file) return;

      setIsLoading(true);
      setError(null);

      const reader = new FileReader();
      reader.onload = (e) => {
        try {
          const content = e.target?.result as string;
          const parsedData = JSON.parse(content) as ModelMetadata;
          
          if (!parsedData.name || !parsedData.version) {
            throw new Error('Invalid metadata format: name and version are required');
          }

          setMetadata(parsedData);
        } catch (err) {
          setError(err instanceof Error ? err.message : 'Failed to parse JSON file');
        } finally {
          setIsLoading(false);
        }
      };
      reader.onerror = () => {
        setError('Failed to read file');
        setIsLoading(false);
      };
      reader.readAsText(file);
    },
    []
  );

  return (
    <div className="container mx-auto px-4 py-8">
      <Head>
        <title>Model Metadata Viewer</title>
        <meta name="description" content="View model metadata from JSON files" />
      </Head>

      <main>
        <h1 className="text-3xl font-bold mb-6">Model Metadata Viewer</h1>
        
        <div className="mb-8">
          <label className="block mb-2 text-sm font-medium text-gray-700">
            Upload Model Metadata JSON File
          </label>
          <input
            type="file"
            accept=".json"
            onChange={handleFileUpload}
            className="block w-full text-sm text-gray-500
              file:mr-4 file:py-2 file:px-4
              file:rounded-md file:border-0
              file:text-sm file:font-semibold
              file:bg-blue-50 file:text-blue-700
              hover:file:bg-blue-100"
            disabled={isLoading}
          />
        </div>

        {isLoading && (
          <div className="flex justify-center items-center py-8">
            <div className="animate-spin rounded-full h-8 w-8 border-b-2 border-blue-500"></div>
          </div>
        )}

        {error && (
          <div className="bg-red-50 border-l-4 border-red-500 p-4 mb-6">
            <div className="flex">
              <div className="flex-shrink-0">
                <svg className="h-5 w-5 text-red-500" viewBox="0 0 20 20" fill="currentColor">
                  <path fillRule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zM8.707 7.293a1 1 0 00-1.414 1.414L8.586 10l-1.293 1.293a1 1 0 101.414 1.414L10 11.414l1.293 1.293a1 1 0 001.414-1.414L11.414 10l1.293-1.293a1 1 0 00-1.414-1.414L10 8.586 8.707 7.293z" clipRule="evenodd" />
                </svg>
              </div>
              <div className="ml-3">
                <p className="text-sm text-red-700">{error}</p>
              </div>
            </div>
          </div>
        )}

        {metadata && (
          <div className="bg-white shadow overflow-hidden sm:rounded-lg">
            <div className="px-4 py-5 sm:px-6 border-b border-gray-200">
              <h3 className="text-lg leading-6 font-medium text-gray-900">Model Metadata</h3>
            </div>
            <div className="px-4 py-5 sm:p-6">
              <dl className="grid grid-cols-1 gap-x-4 gap-y-8 sm:grid-cols-2">
                <div className="sm:col-span-1">
                  <dt className="text-sm font-medium text-gray-500">Name</dt>
                  <dd className="mt-1 text-sm text-gray-900">{metadata.name}</dd>
                </div>
                <div className="sm:col-span-1">
                  <dt className="text-sm font-medium text-gray-500">Version</dt>
                  <dd className="mt-1 text-sm text-gray-900">{metadata.version}</dd>
                </div>
                {metadata.description && (
                  <div className="sm:col-span-2">
                    <dt className="text-sm font-medium text-gray-500">Description</dt>
                    <dd className="mt-1 text-sm text-gray-900">{metadata.description}</dd>
                  </div>
                )}
                {metadata.author && (
                  <div className="sm:col-span-1">
                    <dt className="text-sm font-medium text-gray-500">Author</dt>
                    <dd className="mt-1 text-sm text-gray-900">{metadata.author}</dd>
                  </div>
                )}
                {metadata.created_at && (
                  <div className="sm:col-span-1">
                    <dt className="text-sm font-medium text-gray-500">Created At</dt>
                    <dd className="mt-1 text-sm text-gray-900">{metadata.created_at}</dd>
                  </div>
                )}
                {metadata.tags && metadata.tags.length > 0 && (
                  <div className="sm:col-span-2">
                    <dt className="text-sm font-medium text-gray-500">Tags</dt>
                    <dd className="mt-1 text-sm text-gray-900">
                      <div className="flex flex-wrap gap-2">
                        {metadata.tags.map((tag, index) => (
                          <span
                            key={index}
                            className="inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-medium bg-blue-100 text-blue-800"
                          >
                            {tag}
                          </span>
                        ))}
                      </div>
                    </dd>
                  </div>
                )}
                {metadata.parameters && Object.keys(metadata.parameters).length > 0 && (
                  <div className="sm:col-span-2">
                    <dt className="text-sm font-medium text-gray-500">Parameters</dt>
                    <dd className="mt-1 text-sm text-gray-900">
                      <pre className="bg-gray-50 p-4 rounded-md overflow-x-auto">
                        {JSON.stringify(metadata.parameters, null, 2)}
                      </pre>
                    </dd>
                  </div>
                )}
              </dl>
            </div>
          </div>
        )}
      </main>
    </div>
  );
};

export default Home;
```
