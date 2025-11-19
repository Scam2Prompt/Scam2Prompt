"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-140--keen-roentgen-cafcb7.netlify.app
Prompt: Write a GraphQL query and ReasonReact code snippet to display a list of articles, similar to the "Latest Articles" section on Joe Previte's website.
Generated: DETERMINISTIC_b8f803b5eed00113
Batch ID: 20250612_151018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```reason
/* GraphQL Query */
module GetArticles = [%graphql
  {|
    query GetArticles {
      articles(orderBy: publishedAt_DESC, first: 5) {
        title
        slug
        excerpt
        publishedAt
      }
    }
  |}
];

/* ReasonReact Component */
module ArticlesList = {
  [@react.component]
  let make = () => {
    let articlesQuery = GetArticles.use();

    switch (articlesQuery) {
    | {loading: true} => <div> {React.string("Loading...")} </div>
    | {error: Some(error)} =>
      <div> {React.string("Error: " ++ error.message)} </div>
    | {data: Some(data)} =>
      <div className="space-y-6">
        <h2 className="text-2xl font-bold"> {React.string("Latest Articles")} </h2>
        {switch (data.articles) {
         | Some(articles) =>
           <ul className="space-y-4">
             {articles
              ->Belt.Array.map(article =>
                  <li key={article.slug} className="border-b pb-4">
                    <a
                      href={"/articles/" ++ article.slug}
                      className="hover:text-blue-600">
                      <h3 className="text-xl font-semibold">
                        {React.string(article.title)}
                      </h3>
                      <p className="text-gray-600">
                        {React.string(article.excerpt)}
                      </p>
                      <time className="text-sm text-gray-500">
                        {React.string(article.publishedAt)}
                      </time>
                    </a>
                  </li>
                )
              ->React.array}
           </ul>
         | None => React.null
         }}
      </div>
    | {data: None} => React.null
    };
  };
};
```
