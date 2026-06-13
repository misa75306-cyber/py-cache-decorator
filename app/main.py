from typing import Callable


def cache(func: Callable) -> Callable:
    storage = {}

    def wrapper(*args, **kwargs) -> Callable:
        key = (args, tuple(sorted(kwargs.items())))

        if key in storage:
            print("Getting from cache")
            return storage[key]
        else:
            print("Calculating new result")
            result = func(*args, **kwargs)
            storage[key] = result  # <-- ОСЬ ЦЕЙ РЯДОК ОБОВ'ЯЗКОВО ТРЕБА ДОДАТИ!
            return result

    return wrapper