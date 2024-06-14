import uvicorn

from collections.abc import AsyncIterator
from contextlib import asynccontextmanager
import time

from redis import asyncio as aioredis
from redis.asyncio.connection import ConnectionPool

from fastapi import Depends, FastAPI
from fastapi_users import FastAPIUsers, fastapi_users
from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend
from fastapi_cache.decorator import cache

from auth.auth import auth_backend
from auth.manager import get_user_manager
from auth.models import User
from auth.shemas import UserCreate, UserRead

from operations.router import router as router_operation


async def lifespan(_: FastAPI) -> AsyncIterator[None]:
    redis = aioredis.from_url("redis://localhost")
    FastAPICache.init(RedisBackend(redis), prefix="fastapi-cache")
    yield


app = FastAPI(title="Trading app", lifespan=lifespan)


@app.get("/long_operation")
@cache(expire=60)
def get_long_op():
    time.sleep(2)
    return "Куча данных"


fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend],
)
app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth/jwt",
    tags=["auth"],
)


app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"],
)

app.include_router(router_operation)


current_user = fastapi_users.current_user()


@app.get("/protected-route")
def protected_route(user: User = Depends(current_user)):
    return f"Hello, {user.username}"


@app.get("/unprotected-route")
def protected_route():
    return f"Hello, anonym!"


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
