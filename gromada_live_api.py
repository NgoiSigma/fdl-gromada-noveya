# 🌐 Gromada Live API
# FastAPI-based interface for interacting with FDL agents and compiler

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fdl_compiler import FDLCompiler
from typing import List

app = FastAPI(title="Gromada Live API")

compiler = FDLCompiler()

class FDLRequest(BaseModel):
    source: str

class CompileResponse(BaseModel):
    status: str
    ast: dict | None = None
    errors: List[str] | None = None

@app.post("/compile", response_model=CompileResponse)
def compile_fdl(req: FDLRequest):
    result = compiler.compile(req.source)
    if result['status'] == 'error':
        return CompileResponse(status="error", errors=result['errors'])
    return CompileResponse(status="success", ast=result['ast'])

@app.get("/")
def root():
    return {"message": "Welcome to the Gromada FDL Live API"}

# Run with: uvicorn gromada_live_api:app --reload
