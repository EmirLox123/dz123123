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