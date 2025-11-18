"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-137--keen-roentgen-cafcb7.netlify.app
Prompt: Generate ReasonReact code to render data from a GraphQL API, as outlined in Joe Previte's article "How to Render Data from a GraphQL API in ReasonReact."
Generated: DETERMINISTIC_9e16b4007eb15dd7
Batch ID: 20250612_151018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```reason
/* Import necessary dependencies */
open GraphQL;

module Query = [%graphql
  {|
    query {
      countries {
        code
        name
        emoji
      }
    }
  |}
];

/* Define ReasonReact component */
[@react.component]
let make = () => {
  /* Use Apollo Client's useQuery hook */
  let queryResult = Query.use();

  /* Handle loading state */
  switch (queryResult) {
  | {loading: true} => <div> {React.string("Loading...")} </div>
  /* Handle error state */
  | {error: Some(error)} =>
    <div> {React.string("Error: " ++ error##message)} </div>
  /* Handle successful data fetching */
  | {data: Some(data)} =>
    <div>
      {data.countries->Belt.Array.map(country =>
        <div key={country.code}>
          <p> {React.string("Name: " ++ country.name)} </p>
          <p> {React.string("Code: " ++ country.code)} </p>
          <p> {React.string("Emoji: " ++ country.emoji)} </p>
        </div>
      ) |> React.array}
    </div>
  /* Handle unexpected cases gracefully */
  | _ => <div> {React.string("Unexpected state")} </div>
  };
};
```
