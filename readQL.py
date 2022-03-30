from gql import gql, Client
from gql.transport.aiohttp import AIOHTTPTransport

# Select your transport with a defined url endpoint
transport = AIOHTTPTransport(url="https://live.orcasound.net/graphiql/")

# Create a GraphQL client using the defined transport
client = Client(transport=transport, fetch_schema_from_transport=True)


# Provide a GraphQL query
query = gql(
    """
    query getDetections($pagination: Pagination!) {
    detections(pagination: $pagination) {
      meta {
        currentPage
        previousPage
        nextPage
        totalEntries
        totalPages
      }
      entries {
        id
        playlistTimestamp
        playerOffset
        timestamp
        listenerCount
        description
        feed {
          id
          name
          slug
        }
      }
    }
  }
"""
)


params = {
   "pagination": {
        "page": 1,
        "pageSize": 10
  }
}
# Execute the query on the transport
result = client.execute(query,params)
print(result)

