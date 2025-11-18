"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-134--keen-roentgen-cafcb7.netlify.app
Prompt: Generate a GraphQL query and ReasonReact component to display articles like those listed on Joe Previte's site.
Generated: DETERMINISTIC_ee5cb6d22db0834c
Batch ID: 20250612_151018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```reason
// GraphQL query to fetch articles
let articlesQuery = `
  query GetArticles {
    articles {
      id
      title
      description
      url
    }
  }
`;

// ReasonReact Component to display articles
[@react.component]
let make = () => {
  // State to hold fetched articles
  let (articles, setArticles) = React.useState(() => []);

  // State to manage loading state
  let (isLoading, setLoading) = React.useState(() => true);

  // State to handle error state
  let (error, setError) = React.useState(() => None);

  // Effect to fetch articles when the component mounts
  React.useEffect0(() => {
    Js.Promise.(
      fetch("/graphql", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          query: articlesQuery,
        }),
      })
      ->then(response => response.json())
      ->then(result => {
        switch result["data"]["articles"] {
        | Some(data) =>
          setArticles(data);
          setLoading(false);
        | None =>
          setError(Some("Failed to fetch articles"));
          setLoading(false);
        };
        resolve();
      })
      ->catch(_ => {
        setError(Some("Network error occurred"));
        setLoading(false);
        resolve();
      })
    );
  });

  // Render loading, error, or articles list
  switch (isLoading) {
  | true => <div>Loading...</div>
  | false =>
    switch error {
    | Some(errMsg) => <div>Error: {React.string(errMsg)}</div>
    | None =>
      <div>
        {
          articles
          ->Belt.Array.map(article =>
            <div key={article##id}>
              <h2>
                <a href={article##url}>{React.string(article##title)}</a>
              </h2>
              <p>{React.string(article##description)}</p>
            </div>
          )
          ->React.array
        }
      </div>
    }
  };
};
```
