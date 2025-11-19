"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-137--keen-roentgen-cafcb7.netlify.app
Prompt: Generate a code snippet for rendering data from a GraphQL API using ReasonReact as described by Joe Previte.
Generated: DETERMINISTIC_dbdd676d589880a2
Batch ID: 20250612_163408
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```reason
/*
 * GraphQL query definition using ReasonML's graphql-ppx
 * Fetches a list of items with id and name fields
 */
module ItemsQuery = [%graphql
  {|
    query Items {
      items {
        id
        name
      }
    }
  |}
];

/*
 * ReasonReact component that fetches and renders data from GraphQL
 * Uses the useQuery hook from ReasonApolloHooks
 */
[@react.component]
let make = () => {
  // Apollo query hook with loading, error, and data states
  let (simple, _full) = ItemsQuery.use();

  switch (simple) {
  | Loading => <div> {React.string("Loading...")} </div>
  | Error(error) =>
    <div>
      {React.string("Error: " ++ ApolloClient.ErrorUtils.toString(error))}
    </div>
  | Data(data) =>
    <div>
      <h1> {React.string("Items")} </h1>
      <ul>
        {data.items
         ->Belt.Array.map(item =>
             <li key={item.id}> {React.string(item.name)} </li>
           )
         ->React.array}
      </ul>
    </div>
  };
};
```
