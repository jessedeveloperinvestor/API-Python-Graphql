from flask import Flask
from graphql_server import GraphQLServer

app = Flask(_name_)

# Define your GraphQL schema here (explained later)

server = GraphQLServer(schema)

@app.route('/graphql')
def graphql_endpoint():
  return server.execute(request.data.decode('utf-8'))

if _name_ == '_main_':
  app.run(debug=True)
