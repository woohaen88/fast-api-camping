from typing import List

from fastapi import FastAPI
import uvicorn
from sql_app import models
from sql_app.database import engine
from routers import posts, users

models.Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(users.router)
app.include_router(posts.router)


if __name__ == "__main__":
    # TODO
    # [ ] public이면 domain
    uvicorn.run(app, host="0.0.0.0", port=3000)
