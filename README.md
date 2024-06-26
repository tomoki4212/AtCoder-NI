# お役立ちサイト集
[コレクション](https://www.google.com/collections/s/list/CK3fhkAQQiqRXI2X_8TCXg/3hcwyjEn2g8)

# Gitの使い方
用語がわからなくなったらbacklogにまとまってる  
<https://n-insight.backlog.com/alias/wiki/3426385>
## GitHubのアカウントを発行
共同制作者に追加する

## vscodeでターミナルを開く
参考  
<https://www.javadrive.jp/vscode/terminal/index1.html>

## クローン
自分が作業したいディレクトリにターミナルで移動し、下記を貼り付けてクローンする

### ターミナルでの操作
`pwd` カレントディレクトリのパスを表示
```
cd test.html  # testテストというファイルに移動する
cd ~/  #ホームディレクトリに移動する
cd ..  #一つ上の階層のファイルに移動する
```

```
git clone https://github.com/tomoki4212/Atcoder-NI.git
```
こんな感じ
![image](https://github.com/NIikeda/AtCoder-NI/assets/158264039/96f6aca1-85c1-42fd-b7f3-2d8a2526661b)

## ブランチを作成

リポジトリに移動
```
cd AtCoder-NI
```

新しいブランチを作成し、切り替えまで一気に行う
```
git checkout -b <new-branch-name>
```
例
```
git checkout -b "feature-ikeda"
```
![image](https://github.com/NIikeda/AtCoder-NI/assets/158264039/9aacff54-dee0-4fa4-8d01-2b5b5b04d976)

## 問題を解く
がんば！！

## コミットする
```
git add .
```
```
git commit -m "I solved Q1."
```
-mの後はこのコミットが何をしたかをコメントする。なんでもいいが何かしら記述しないとコミットできない。  
今回の場合、解いた問題番号でも書いておくのがいいだろう

## pushする
ローカルリポジトリをリモートリポに反映する
### step1
- push前に一度リモートリポの内容をローカルリポジトリに反映する(pull)
  - pullしないと誰かがリモートリポジトリを更新していた場合、古い情報のまま反映してしまい、バグが起きる可能性があるから
    - 今回の場合は、その可能性は限りなく低いが、今後gitを使うことを考えて癖をつけておこう
   
```
git pull <remote_name> <branch-name>
```
`<remote_name>`: `git remote -v`で確認が可能。通常は自動で`origin`となっているので`origin`を入れれば大丈夫  
`<branch-name>`: 反映させたいブランチ名を入れる。要するに、今回のケースなら`main`  

例
```
git pull origin main
```
今回はこのままコピペすればOK

### step2
pushする
```
git push <remote_name> <branch-name>
```
`<remote_name>`: `git remote -v`で確認が可能。通常は自動で`origin`となっているので`origin`を入れれば大丈夫  
`<branch-name>`: 反映するブランチ名を入れる。要するに、自分が作成したbranch名。今回のケースなら`feature-ikeda`  
例
```
git push origin feature-ikeda
```

## プルリク送る
https://note.com/ym202110/n/n20379357fdd5  

この時、レビュワーをきちんと設定する

## レビューが終わったらmainにマージする
これは池田がやります

## ローカルリポのmainブランチをpull(更新)する
リモートリポが更新されている状態なので、それをローカルに反映する  
ブランチをmainに切り替える
```
git checkout main
```
ローカルに反映
```
git pull origin main
```


## プルリク後のマージする前に他の問題を解く場合、次の問題を解くための新たなブランチを作成