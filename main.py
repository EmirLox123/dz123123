class GeneratorIterator:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __iter__(self):
        return self.generator()

    def generator(self):
        for i in range(self.start, self.end):
            yield i

if __name__ == '__main__':
    iterator = GeneratorIterator(1, 5)
    for i in iterator:
        gen = (x for x in range(i))
        for j in gen:
            print(j, end=' ')
        print()





import time

def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f'Время выполнения функции {func.__name__}: {end_time - start_time} сек.')
        return result
    return wrapper

@timer
def some_function(*args, **kwargs):
    # .. код функции
    pass
#декораторы это когда мы можем менять поведение функций или классов не меняя их

