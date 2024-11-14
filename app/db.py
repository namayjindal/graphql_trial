from typing import List, Optional
from app.types import Movie

# In-memory database for demonstration
movies_db = [
    Movie(
        id=1,
        title="The Shawshank Redemption",
        genre="Drama",
        release_date="1994-09-23",
        rating=9.3,
        director="Frank Darabont",
        description="Two imprisoned men bond over a number of years..."
    ),
    Movie(
        id=2,
        title="The Godfather",
        genre="Crime",
        release_date="1972-03-24",
        rating=9.2,
        director="Francis Ford Coppola",
        description="The aging patriarch of an organized crime dynasty..."
    ),
]

class MovieRepository:
    def get_all_movies(self) -> List[Movie]:
        return movies_db

    def get_movie_by_id(self, id: int) -> Optional[Movie]:
        return next((movie for movie in movies_db if movie.id == id), None)

    def get_movies_by_genre(self, genre: str) -> List[Movie]:
        return [movie for movie in movies_db if movie.genre.lower() == genre.lower()]

    def add_movie(self, movie_data: dict) -> Movie:
        new_id = max(movie.id for movie in movies_db) + 1
        new_movie = Movie(id=new_id, **movie_data)
        movies_db.append(new_movie)
        return new_movie

    def recommend_movies(self, movie_id: int, limit: int = 3) -> List[Movie]:
        source_movie = self.get_movie_by_id(movie_id)
        if not source_movie:
            return []
        
        # Simple recommendation based on same genre
        similar_movies = [
            movie for movie in movies_db 
            if movie.genre == source_movie.genre and movie.id != source_movie.id
        ]
        return sorted(similar_movies, key=lambda x: x.rating, reverse=True)[:limit]
