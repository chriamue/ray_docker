import time
import ray


ray.init(redis_address="localhost:6379")

@ray.remote
def f():
    time.sleep(1)
    return 1

results = ray.get([f.remote() for i in range(32)])