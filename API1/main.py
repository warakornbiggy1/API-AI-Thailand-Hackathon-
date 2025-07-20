from fastapi import FastAPI, Request
import httpx
import uvicorn
import os

app = FastAPI()

API2_URL = os.getenv("API2_URL", "http://api2:8001/api2/hello")

@app.get("/api1/hello")
async def read_root(request: Request):
    print(f"API1 Log: Received request from {request.client.host}")
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(API2_URL)
            response.raise_for_status()
            api2_response = response.json()
            print(f"API1 Log: Successfully received response from API2: {api2_response}")
            return {"message_from_api1": "Hello from API1!", "message_from_api2": api2_response}
    except httpx.RequestError as exc:
        print(f"API1 Log: An error occurred while requesting API2: {exc}")
        return {"message_from_api1": "Hello from API1!", "error": f"Could not connect to API2: {exc}"}
    except httpx.HTTPStatusError as exc:
        print(f"API1 Log: HTTP error from API2: {exc.response.status_code}")
        return {"message_from_api1": "Hello from API1!", "error": f"API2 returned error: {exc.response.status_code}"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)