from arq import create_pool
from arq.connections import RedisSettings
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Print(BaseModel):
    content: str


@app.on_event("startup")
async def startup_event():
    redis = await create_pool(RedisSettings())
    app.state.redis = redis


@app.get("/")
async def test():
    await app.state.redis.enqueue_job(
        "print_content",
        Print(content="Hello")
    )
    return "arq success"


@app.get("/args")
async def args():
    res = await app.state.redis.enqueue_job(
        "print_with_args",
        num1=1,
        num2=98,
    )
    res = await res.result(timeout=3)
    return {"result": res}
