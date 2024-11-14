from typing import List, Optional
import strawberry
from datetime import datetime

@strawberry.type
class Movie:
    id: int
    title: str
    genre: str
    release_date: str
    rating: float
    director: str
    description: Optional[str] = None

@strawberry.input
class MovieInput:
    title: str
    genre: str
    release_date: str
    rating: float
    director: str
    description: Optional[str] = None