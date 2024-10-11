'''
created on 2024/10/11

@author Kiwa

'''
print("Hello, Python world!")

a = 10
b = 0.000001
c = 'string'
d = 10; e = 0.000001; f = 'string'

print(a,b,c)
print(d,e,f)
for x in {1,2,3}:
    print(x)
    
"""
2021/01/25
@Yuya Shimizu

クイックソート
"""

def quick_sort(data):

    #分割できなくなる(リスト要素が1以下)であれば，そのままデータを返す(並べ替えの必要なし)
    if len(data) <= 1:
        return data

    pivot = data.pop(0)     #リストの先頭をピボットとして取り出す

    # ピボットより小さいものでリストを作る
    left = [i for i in data if i <= pivot]
    # ピボットより大きいものでリストを作る
    right = [i for i in data if i > pivot]

    left = quick_sort(left)       #入力に対する左側リストを形成する
    right = quick_sort(right)   #入力に対する右側リストを形成する

    #########再帰しきった結果のみ，quick_sort関数の出力として返される
    #########それ以外のreturnは上のleft = quick_sort(right), left = quick_sort(right)
    return left + [pivot] + right


print(quick_sort([1,3,5,2,4,8,7,10,6]))

"""
じゃんけん

"""
# Kiwa
# import random

# hand_a = random.randint(0,2)
# hand_b = random.randint(0,2)

# print(hand_a,hand_b)

# if hand_a == hand_b :
#     print("引き分け")
# elif (hand_a == 0 and hand_b == 1) or (hand_a == 1 and hand_b == 2) or (hand_a == 2 and hand_b == 0):
#     print("aの勝ち")
# else:
#     print("bの勝ち")

# Chat
# import random

# # ジャンケンの選択肢
# choices = ["グー", "チョキ", "パー"]

# # 勝敗の判定関数
# def judge(player_choice, computer_choice):
#     # 引き分けの場合
#     if player_choice == computer_choice:
#         return "引き分け"
#     # 勝ち負けの判定（グー vs チョキ、チョキ vs パー、パー vs グー）
#     elif (player_choice == 0 and computer_choice == 1) or \
#          (player_choice == 1 and computer_choice == 2) or \
#          (player_choice == 2 and computer_choice == 0):
#         return "あなたの勝ち！"
#     else:
#         return "コンピュータの勝ち！"

# # ランダムにジャンケンを実行
# def play_janken():
#     # プレイヤーとコンピュータの選択をランダムに決定
#     player_choice = random.randint(0, 2)
#     computer_choice = random.randint(0, 2)

#     # 選択の表示
#     print(f"あなたの選択: {choices[player_choice]}")
#     print(f"コンピュータの選択: {choices[computer_choice]}")

#     # 勝敗の判定
#     result = judge(player_choice, computer_choice)
#     print(f"結果: {result}")

# # ジャンケンを実行
# if __name__ == "__main__":
#     play_janken()

import random

# ジャンケンの選択肢
choices = ["グー", "チョキ", "パー"]

# 勝敗の判定関数 (複数プレイヤーの手を比較)
def judge(player_choices):
    unique_choices = set(player_choices)

    # 全員が同じ手の場合は引き分け
    if len(unique_choices) == 1:
        return -1  # 引き分け

    # グー、チョキ、パーが全て出ている場合も引き分け
    if len(unique_choices) == 3:
        return -1  # 引き分け

    # 勝つ手を決める
    if 0 in unique_choices and 1 in unique_choices:
        winner_hand = 0  # グーが勝つ
    elif 1 in unique_choices and 2 in unique_choices:
        winner_hand = 1  # チョキが勝つ
    else:
        winner_hand = 2  # パーが勝つ

    # 勝った手を出したプレイヤーをリスト化
    winners = [i for i, choice in enumerate(player_choices) if choice == winner_hand]
    return winners

# 3回勝負を実行
def play_janken(num_players=3):
    # 各プレイヤーの勝利数を記録
    wins = [0] * num_players

    # 3回勝負
    for round_num in range(3):
        print(f"\n--- {round_num + 1}回戦 ---")
        
        # 各プレイヤーの手をランダムに生成
        player_choices = [random.randint(0, 2) for _ in range(num_players)]

        # 各プレイヤーの手を表示
        for i, choice in enumerate(player_choices):
            print(f"プレイヤー {i+1}: {choices[choice]}")

        # 勝敗を判定
        result = judge(player_choices)
        if result == -1:
            print("引き分け！")
        else:
            # 勝利者を表示し、勝利数を加算
            for winner in result:
                print(f"プレイヤー {winner + 1} が勝ちました！")
                wins[winner] += 1

    # 最終結果の表示
    print("\n--- 最終結果 ---")
    for i, win_count in enumerate(wins):
        print(f"プレイヤー {i + 1}: {win_count}勝")

    # 優勝者を判定
    max_wins = max(wins)
    winners = [i + 1 for i, win_count in enumerate(wins) if win_count == max_wins]

    if len(winners) == 1:
        print(f"\n優勝はプレイヤー {winners[0]} です！")
    else:
        print(f"\nプレイヤー {'、'.join(map(str, winners))} の引き分けです！")

# ジャンケンを実行
if __name__ == "__main__":
    play_janken(num_players=4)  # 4人でじゃんけん
