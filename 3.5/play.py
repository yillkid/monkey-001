import random

balance = 1000
while True:
    print("本金 " + str(balance))
    # 擲骰子
    print("請擲骰子:")
    points = random.randint(1, 6)
    print("點數為: " + str((points)))

    # if 機會

    # if 命運

    # if 賺錢
    print("需要賺錢嗎?")
    deposit = input()

    # if 扣錢
    print("需要扣錢嗎?")
    withdrawal = input()

    balance = balance + int(deposit)
    balance = balance - int(withdrawal)

    print("我的本金剩下: " + str(balance))

