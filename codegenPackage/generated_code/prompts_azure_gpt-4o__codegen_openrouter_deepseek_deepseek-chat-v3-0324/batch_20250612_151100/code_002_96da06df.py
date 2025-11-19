"""
Generated Code Metadata:
========================
Original URL: https://ta-orch-api.agoric-sdk.pages.dev
Prompt: Provide a detailed example of creating and installing a Zoe contract facet bundle using the Agoric SDK, ensuring the `yarn build` step is included to generate the contract facet bundle.
Generated: DETERMINISTIC_96da06df7e0f8683
Batch ID: 20250612_151100
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// File: contracts/myContract.js
import { E } from '@endo/eventual-send';
import { Far } from '@endo/marshal';
import { makeZoeKit } from '@agoric/zoe';

const start = async (zcf) => {
  const creatorFacet = Far('creatorFacet', {
    makeInvitation: () => zcf.makeInvitation(() => 'Hello from contract', 'myInvitation'),
  });

  const publicFacet = Far('publicFacet', {
    getStatus: () => 'Contract is running',
  });

  return harden({ creatorFacet, publicFacet });
};

harden(start);
export { start };
```

```javascript
// File: scripts/deploy.js
import { makeHelpers } from '@agoric/deploy-script-support';
import { resolve as importMetaResolve } from 'import-meta-resolve';
import bundleSource from '@endo/bundle-source';
import { E } from '@endo/eventual-send';

/** @type {import('@agoric/deploy-script-support/src/externalTypes.js').ProposalBuilder} */
export const defaultProposalBuilder = async ({ publishRef, install }) => {
  // Bundle the contract
  const contractPath = new URL(
    '../contracts/myContract.js',
    importMetaResolve(import.meta.url),
  ).pathname;
  const contractBundle = await bundleSource(contractPath);
  
  // Install the bundle
  const installation = await install(contractBundle);
  await publishRef(installation);
  
  return harden({
    sourceSpec: contractPath,
    getManifestCall: [
      'getManifestForMyContract',
      {
        installation,
      },
    ],
  });
};

export default async (homeP, endowments) => {
  const { install } = await makeHelpers(homeP, endowments);
  return defaultProposalBuilder({ publishRef: () => {}, install });
};
```

```javascript
// File: scripts/getManifestForMyContract.js
import { makeHelpers } from '@agoric/deploy-script-support';

/** @type {import('@agoric/deploy-script-support/src/externalTypes.js').ManifestBuilder} */
export const defaultManifestBuilder = async ({ installation }) => {
  return harden({
    manifest: {
      myContract: {
        installation,
        instance: {
          storagePath: 'myContract',
        },
      },
    },
    installations: {
      myContract: installation,
    },
  });
};

export default async (homeP, endowments) => {
  const helper = await makeHelpers(homeP, endowments);
  return defaultManifestBuilder(helper);
};
```

```json
// File: package.json
{
  "name": "my-agoric-contract",
  "version": "1.0.0",
  "scripts": {
    "build": "agoric run --allow-read --eval true",
    "deploy": "agoric deploy scripts/deploy.js"
  },
  "dependencies": {
    "@agoric/deploy-script-support": "^0.6.0",
    "@agoric/zoe": "^0.24.0",
    "@endo/bundle-source": "^2.0.0",
    "@endo/eventual-send": "^4.0.0",
    "@endo/marshal": "^4.0.0",
    "import-meta-resolve": "^2.0.0"
  }
}
```
