from fastapi import FastAPI
import uvicorn


app = FastAPI()


def hello_world() -> dict:
    return {"message": "Hello, World!"}

# routes
app.add_api_route(path="/", endpoint=hello_world, methods=["GET"])


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
