from fastapi import FastAPI, Request
import uvicorn

app = FastAPI()

@app.get("/api2/hello")
async def read_root(request: Request):
    print(f"API2 Log: Received request from {request.client.host}")
    return {"message": "Hello from API2!"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8001)