# i日目に登録されたユーザ名のペアをいれる辞書と、ユーザ名の辞書を作成
s_dict : dict = {}
s_set = {""}

# n入力
n = int(input())

for i in range(1, n+1):

    # S1～Si入力→日数とユーザ名のペアを辞書に追加
    # 内包表記で他の表現知ってたら教えて下さい
    s_dict[i] = input()
    s_set.add(s_dict[i])

for i,k in s_dict.items():

    #ユーザ名の集合に名前が初めて見つかった場合は削除
    #日数をprintし、次以降のループで同ユーザ名が見つかってもprintしないように集合から消す
    if s_dict[i] in s_set:
        print(i)
        s_set.remove(k)