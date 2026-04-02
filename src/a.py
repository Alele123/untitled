import random
import time


def fibonacci(n):
    a, b = 0, 1
    result = []
    for _ in range(n):
        result.append(a)
        a, b = b, a + b
    return result


def guess_number_game():
    print("=== 猜数字游戏 ===")
    secret = random.randint(1, 100)
    attempts = 0

    while True:
        try:
            guess = int(input("猜一个 1-100 之间的数字: "))
        except ValueError:
            print("请输入有效数字！")
            continue

        attempts += 1
        if guess < secret:
            print("太小了，再试试！")
        elif guess > secret:
            print("太大了，再试试！")
        else:
            print(f"恭喜！你用了 {attempts} 次猜中了 {secret}！")
            break


def main():
    print("Fibonacci 数列 (前10项):", fibonacci(10))
    print()

    words = ["Python", "世界", "你好", "编程", "简单"]
    print("随机打乱单词:", random.sample(words, len(words)))
    print()

    print(f"当前时间戳: {time.strftime('%Y-%m-%d %H:%M:%S')}")
    print()

    guess_number_game()


if __name__ == "__main__":
    main()
