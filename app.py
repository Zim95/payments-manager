# third-party
from fastapi import FastAPI
import uvicorn

# modules
'''
Our DB and Migrations have already been set up by browseterm_db initializer.
Hence, we can directly connect to the DB using DBConfig.

All migrations related operations are handled by our browseterm_db library.
'''

# fastapi app
app: FastAPI = FastAPI()


def hello_world() -> dict:
    return {"message": "Hello, World!"}

# routes
app.add_api_route(path="/", endpoint=hello_world, methods=["GET"])


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
