from fastapi import FastAPI

from models import CitiesGame


app = FastAPI()
game = CitiesGame()


@app.post("/")
async def root(city: str):
    answer, letter = game.user_move(city=city)
    return {'city': answer, 'letter': letter}
