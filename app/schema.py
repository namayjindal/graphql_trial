from typing import List, Optional
import strawberry
from app.types import Movie, MovieInput
from app.db import MovieRepository

repo = MovieRepository()

@strawberry.type
class Query:
    @strawberry.field
    def movies(self) -> List[Movie]:
        return repo.get_all_movies()

    @strawberry.field
    def movie(self, id: int) -> Optional[Movie]:
        return repo.get_movie_by_id(id)

    @strawberry.field
    def movies_by_genre(self, genre: str) -> List[Movie]:
        return repo.get_movies_by_genre(genre)

    @strawberry.field
    def recommend_movies(self, movie_id: int, limit: int = 3) -> List[Movie]:
        return repo.recommend_movies(movie_id, limit)

@strawberry.type
class Mutation:
    @strawberry.mutation
    def add_movie(self, movie_data: MovieInput) -> Movie:
        return repo.add_movie(movie_data.__dict__)

schema = strawberry.Schema(query=Query, mutation=Mutation)