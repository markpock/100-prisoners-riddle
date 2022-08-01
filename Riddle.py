import random
from typing import Generator


class Room:
    def __init__(self, length: int = 10, seq: Generator = None):
        self.length = length
        if not seq:
            seq = Room.rand(length ** 2)
        self.x = {}
        for num in range(self.length):
            self.x[num] = {}
        for col in self.x:
            row = self.x[col]
            for num in range(self.length):
                row[num] = next(seq)

    def __getitem__(self, value) -> int:
        return self.x[value // self.length][value % self.length]

    def __str__(self) -> str:
        result = '   0   1   2   3   4   5   6   7   8   9\n'
        for col in self.x:
            alt = [f'{str(val)}  ' for val in list(self.x[col].values())]
            for pos in range(len(alt)):
                if len(alt[pos]) < 4:
                    alt[pos] += ' '
            result += f'{str(col)}  {"".join(alt)}\n'
        return result

    @staticmethod
    def rand(size: int = 100) -> Generator:
        orig = [num for num in range(0, size)]
        for _ in range(size):
            result = orig[random.randint(0, len(orig) - 1)]
            orig.remove(result)
            yield result


class Prisoner:
    def __init__(self, id: int):
        self.id = id
        self.position = id
        self.found = False

    def next(self, room: Room) -> bool:
        self.found = room[self.position] == self.id
        if not self.found:
            self.position = room[self.position]
        return self.found


def main():
    prisoners = [Prisoner(num) for num in range(100)]
    success = 0
    failure = 0

    for _ in range(10000):
        room = Room()
        print("Room: " + str(_ + 1))
        everyone_has_succeeded = True
        for prisoner in prisoners:
            num_of_boxes, cont = 0, True
            while num_of_boxes < 50 and not prisoner.found:
                prisoner.next(room)
                num_of_boxes += 1
            everyone_has_succeeded = everyone_has_succeeded and prisoner.found
        if everyone_has_succeeded:
            success += 1
        else:
            failure += 1
    print(f'Number of successes: {success}\nNumber of failures: {failure}')


if __name__ == "__main__":
    main()
