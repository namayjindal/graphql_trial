# Movie Recommender GraphQL API

A simple movie recommendation API built with FastAPI and Strawberry GraphQL.

## Features
- Query movies by ID or genre
- Get movie recommendations based on a movie ID
- Add new movies to the database
- In-memory database for demonstration purposes

## Setup
1. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the server:
   ```bash
   uvicorn app.main:app --reload
   ```

4. Visit http://localhost:8000/graphql for the GraphQL playground

## Example Queries

Query all movies:
```graphql
query {
  movies {
    id
    title
    genre
    rating
    director
  }
}
```

Get movie recommendations:
```graphql
query {
  recommendMovies(movieId: 1, limit: 2) {
    title
    genre
    rating
  }
}
```

Add a new movie:
```graphql
mutation {
  addMovie(
    movieData: {
      title: "Inception"
      genre: "Sci-Fi"
      releaseDate: "2010-07-16"
      rating: 8.8
      director: "Christopher Nolan"
      description: "A thief who steals corporate secrets..."
    }
  ) {
    id
    title
    genre
  }
}
```