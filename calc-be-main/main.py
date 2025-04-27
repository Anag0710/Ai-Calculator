from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from apps.calculator.route import router as calculator_router
from constants import SERVER_URL, PORT, ENV

@asynccontextmanager
async def lifespan(app: FastAPI):
    yield

app = FastAPI(lifespan=lifespan)

# Update CORS to allow all origins during testing
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # For testing, in production use specific origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get('/')
async def root():
    return {"message": "Server is running"}

@app.get("/status")
async def status():
    return {"status": "ok", "message": "API is running", "endpoints": ["/calculate"]}

@app.post("/calculate")
async def calculate_route(request_data: YourRequestSchema):
    # Your calculation logic
    return {"data": [{"expr": "your_expression", "result": "your_result", "assign": False}]}

app.include_router(calculator_router, prefix="/calculate", tags=["calculate"])

if __name__ == "__main__":
    uvicorn.run("main:app", host=SERVER_URL, port=int(PORT), reload=(ENV == "dev"))
