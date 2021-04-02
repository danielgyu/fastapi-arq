from loguru import logger


async def print_content(arq_redis, model):
    print("arq model content: ", model.content)


async def print_with_args(arq_redis, num1, num2=None):
    return num1 + num2


async def startup(redis_arq):
    logger.info("worker startup")


async def shutdown(redis_arq):
    logger.info("worker shutdown")


class WorkerSettings:
    functions = [print_content, print_with_args]
    on_startup = startup
    on_shutdown = shutdown
