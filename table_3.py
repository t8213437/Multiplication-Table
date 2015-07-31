class Demo:
    def mult(self):
        for x in range(10):
            if x == 0:
                continue
            for y in range(10):
                if y == 0:
                    continue
                print(x * y, end= "\t")
            print()

if __name__ == "__main__":
    d = Demo()
    d.mult()
