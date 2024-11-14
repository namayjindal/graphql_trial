from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter
from app.schema import schema

app = FastAPI(title="Movie Recommender GraphQL API")

graphql_app = GraphQLRouter(schema)
app.include_router(graphql_app, prefix="/graphql")

@app.get("/")
async def root():
    return {"message": "Welcome to Movie Recommender API. Visit /graphql for the GraphQL playground"}