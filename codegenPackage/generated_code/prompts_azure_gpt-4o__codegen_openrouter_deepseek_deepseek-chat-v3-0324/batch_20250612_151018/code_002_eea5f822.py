"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-140--keen-roentgen-cafcb7.netlify.app
Prompt: Implement a ReasonReact component that fetches and renders data from a GraphQL API, as outlined in Joe Previte's article "How to Render Data from a GraphQL API in ReasonReact."
Generated: DETERMINISTIC_eea5f822aeb50b71
Batch ID: 20250612_151018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```reason
module Query = [%graphql
  {|
    query GetData {
      data {
        id
        name
        description
      }
    }
  |}
];

module GetDataQuery = ReasonApollo.CreateQuery(Query);

type state = {
  loading: bool,
  error: option(string),
  data: option(Query.t),
};

type action =
  | Loading
  | Error(string)
  | DataLoaded(Query.t);

let component = ReasonReact.reducerComponent("DataFetcher");

let make = _children => {
  ...component,
  initialState: () => {loading: true, error: None, data: None},
  reducer: (action, _state) =>
    switch (action) {
    | Loading => ReasonReact.Update({loading: true, error: None, data: None})
    | Error(msg) => ReasonReact.Update({loading: false, error: Some(msg), data: None})
    | DataLoaded(data) => ReasonReact.Update({loading: false, error: None, data: Some(data)})
    },
  render: self =>
    <GetDataQuery>
      ...{({result}) =>
        switch (result) {
        | Loading =>
          <div>
            {ReasonReact.string("Loading...")}
          </div>
        | Error(error) =>
          <div>
            {ReasonReact.string("Error: " ++ error.message)}
          </div>
        | Data(response) =>
          switch (response.data) {
          | None =>
            <div>
              {ReasonReact.string("No data received")}
            </div>
          | Some(data) =>
            <div>
              <h1> {ReasonReact.string("Data from GraphQL API")} </h1>
              <ul>
                {data.data
                 ->Belt.Option.map(data =>
                     data
                     ->Belt.Array.map(item =>
                         <li key={item.id}>
                           <h2> {ReasonReact.string(item.name)} </h2>
                           <p> {ReasonReact.string(item.description)} </p>
                         </li>
                       )
                     ->ReasonReact.array
                   )
                 ->Belt.Option.getWithDefault(ReasonReact.null)}
              </ul>
            </div>
          }
        }
      }
    </GetDataQuery>,
};
```
