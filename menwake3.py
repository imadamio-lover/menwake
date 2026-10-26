
Gemini との会話
何を打っても存在しませんになってしまうんだけど、ほかの方法ない？

「存在しません」と出てしまう場合、主な原因は GitHub側のファイル保存場所（ブランチ名） か GitHubアカウントとの連携状態 のズレです。

手入力で直すよりも、Streamlit Cloud側のアプリ登録（リポジトリ連携）を一からやり直す のが確実で早いです！

以下の「リセット＆再連携」手順を試してみてください。

1. リセットして選び直す手順
1
1. 一度画面をトップに戻す
Streamlitのトップに戻る
Streamlit画面の左上にある 「Streamlitのロゴ（赤い波マーク）」 または 「Workspace」 をクリックして、アプリ作成前のトップ画面（ダッシュボード）に戻ります。

2
2. 新しくアプリを作成する
ドロップダウンで正しく選ぶ
右上の 「Create app」 ボタンを押します。

入力画面が出たら、まず 「Switch to interactive picker」 を押して「ドロップダウン選択モード」にします。

Repository の枠をクリックすると、ご自身のリポジトリ一覧が出てくるので、そこから アカウント名/menwake を手入力せずリストからクリックして選びます。

3
3. ファイル名を合わせる
ファイル名とブランチの確認
Branch: main になっていればそのまま（もし master しか選べない場合は master）

Main file path: menwake3.py とだけ入力（※ C:\... などのパソコン上のフォルダパスではなく、ファイル名だけを入力します）

Deploy! を押します。

それでも解決しない場合の別のアプローチ（別の名前にする）
GitHub上の menwake リポジトリの状態が崩れている可能性があるため、GitHub側で新しく別の名前でリポジトリを作る ほうがスムーズにいくことがあります。

GitHub にアクセスします。

Repository name に tennis-app-new（今まで使っていない名前）と入力します。

Private にチェックを入れて一番下の 「Create repository」 を押します。

画面中央の 「uploading an existing file」 から、menwake3.py と requirements.txt をドラッグ＆ドロップして 「Commit changes」 を押します。

再度 Streamlit Cloud に行き、新しく作った tennis-app-new を選択して Deploy します。

この方法であれば、古い設定が残っていない完全に綺麗な状態でデプロイできます！

What would you like to do?



Deploy a public app from GitHub

My code is ready on a GitHub repo, and it is totally awesome.

Deploy now



Deploy a public app from a template

I want to see what kind of amazing concoctions you have for me.

Check out templates



Deploy a private app in Snowflake

I want unlimited enterprise-grade apps, with the security of Snowflake.

Start trialこれしかないです

その画面が表示されているのですね！理由が分かりました。

現在表示されているのは 「パブリック（完全公開）アプリか、Snowflake用アプリを作るか」 の選択画面です。

一番上の 「Deploy a public app from GitHub」 にある 「Deploy now」 ボタンをクリックしてください！

次の画面での入力手順
「Deploy now」を押すと、設定画面が開きます。

Repository: アカウント名/menwake（または新しく作ったリポジトリ名）を選択

Branch: main（または master）

Main file path: menwake3.py と入力

Deploy! ボタンをクリック

これでデプロイ（読み込み）がスタートします！2〜3分待つと画面が立ち上がり、完成したアプリのURLが発行されます。

ここにずっと入力しているんだけど、うまくいかなくて

「Deploy now」を押したあとの画面（Repository・Branch・Main file path を入力する画面）でずっとエラー（This repository does not exist 等）が出てしまうのですね。お手数をおかけしています！

この場合、「Streamlit Cloud」と「GitHub のアカウント」との連携権限がうまく繋がっていない（または、Privateリポジトリへのアクセス権が付与されていない） ことが原因です。

一番確実に解決できる 「アクセス権限の再連携」 を行いましょう！

解決手順：StreamlitにGitHubのアクセス許可をやり直す
1
1. 一度 Streamlit からサインアウトする
右上のアイコンからログアウト
Streamlit画面の右上のご自身のアカウントアイコンをクリックし、「Sign out」 を押して一度ログアウトします。

2
2. 再度 GitHub でサインインする
GitHub連携の権限をやり直す
再度 share.streamlit.io にアクセスします。

「Continue with GitHub」 をクリックします。

この時、GitHubの確認画面（Authorize Streamlit）が表示されたら、画面内にある 「Grant」 や 「Authorize」（緑色のボタン）を押して、Privateリポジトリへのアクセスを許可します。

3
3. もう一度 Deploy now から設定する
ドロップダウンから確実に選択する
「Deploy a public app from GitHub」 の 「Deploy now」 を押します。

入力画面で 「Switch to interactive picker」 を押し、Repositoryの選択肢枠をクリックします。

先ほど許可したことで、ご自身のリポジトリ（menwake）がリスト内に自動で表示されるようになりますので、それをクリックして選択します。

Main file path に menwake3.py と入力し、「Deploy!」 を押します。

※ もしそれでもリポジトリ一覧に出てこない場合
GitHub側のリポジトリ設定が「Private（非公開）」になっていると、Streamlitの無料プランの初期設定では見えないことがあります。

その場合は、GitHubの menwake リポジトリのページを開き、以下の操作で一時的に Public（公開） に変更してみてください：

GitHubの menwake ページを開く ➔ 上部の 「Settings」（歯車マーク）をクリック

一番下までスクロールし、「Danger Zone」 内にある 「Change repository visibility」 ➔ 「Change to public」 を選択

画面の指示通りにリポジトリ名を入力して確定する

Publicに変更してから再度 Streamlit で menwake を選ぶと、一発で認識されるようになります！

上部の 「Settings」（歯車マーク）をクリックこれが見当たりません

GitHubの画面デザインによって「Settings」の場所が見つけにくくなっているか、スマホ・画面幅が狭い表示で隠れている可能性があります！

「Settings」が見当たらない場合は、アドレスバーのURLを直接書き換えて開く方法が一番確実です。

方法1：URLを直接書き換える（一番簡単・確実に開けます）
ブラウザの一番上にあるアドレスバー（URLが表示されている場所）を開き、末尾に /settings を付け足してアクセスしてください。

入力するURL: [https://github.com/ご自身のアカウント名/menwake/settings](https://github.com/ご自身のアカウント名/menwake/settings)

これで一発で Settings（設定）画面が開きます！

方法2：画面上での探し方
パソコンの画面で開いている場合、リポジトリ（menwake）のトップページの上部に、以下のようなタブ並びがあります：

Code / Issues / Pull requests / Actions / Projects / ... / Settings

画面幅が狭い場合: タブの右端にある 「...」（三点リーダー） や 「More」 をクリックすると、隠れているメニューの中に 「Settings」（歯車マーク）が出てきます。

スマホ表示の場合: 画面右上にある 「☰」（ハンバーガーメニュー） を押すと、メニューの中に「Settings」が表示されます。

Settings 画面が開いた後の操作（Publicに変更）
Settings 画面が開いたら、以下の手順で進めてください。

ページの一番下までスクロールします。

赤い枠の 「Danger Zone」（危険ゾーン）を探します。

「Change repository visibility」（公開設定の変更）をクリックします。

「Change to public」（公開に変更）を選択します。

画面の指示（リポジトリ名 アカウント名/menwake の入力など）に従って確定ボタンを押します。

Public に変更できたら、再度 Streamlit Cloud の画面に戻り、リポジトリ一覧から menwake を探してみてください。スムーズに認識されるようになります！

できましら

無事に変更できましたね！お疲れ様です！

これで Streamlit Cloud からもリポジトリが正しく認識される準備が整いました。

最後の仕上げとして、Streamlit Cloud でアプリを公開（デプロイ） しましょう！

最終ステップ：アプリのデプロイ
1
1. デプロイ画面を開く
Streamlit Cloud の作成画面へ行く
share.streamlit.io にアクセスします。

「Deploy a public app from GitHub」 の下にある 「Deploy now」 ボタンを押します。

2
2. 各項目を設定する
リストから自分のアプリを選ぶ
「Switch to interactive picker」 を押して選択モードにします。

Repository: 一覧（ドロップダウン）をクリックし、ご自身のアカウント名/menwake を選択します。

Branch: main（または master）を選択します。

Main file path: menwake3.py と手入力します。

3
3. 「Deploy!」を押す
紙吹雪が舞えば成功です！
画面右下の 「Deploy!」 ボタンをクリックします。

2〜3分ほど読み込み画面が続いた後、風船・紙吹雪の演出とともにアプリが表示されます！

スマホでの共有方法
アプリが開いたら、ブラウザの一番上にある アドレスバーのURL（例: [https://xxxxxx.streamlit.app](https://xxxxxx.streamlit.app)）をコピー して、LINEやメールで共有したいメンバーに送ってください。

これで、リンクを受け取った人だけがスマホからいつでもアプリを開いて面分け（コート割り）を行えるようになります！

「Switch to interactive picker」koreganaidesu

「Switch to interactive picker」が見当たらないのですね！

その場合は、直接 GitHubのURLを貼り付ける方式 でそのまま設定できます。
Public（公開）に変更したことで、URLの貼り付けで正しく認識されるようになっています！

以下の手順で貼り付けてみてください。

URLを直接貼り付けてデプロイする手順
GitHubのページを開いてURLをコピーする

GitHubで menwake のページを開きます。

ブラウザの一番上にあるアドレスバーのURL（例: [https://github.com/ご自身のアカウント名/menwake](https://github.com/ご自身のアカウント名/menwake)）をコピーします。

Streamlitの画面に貼り付ける

Streamlitの入力画面（Repository / Paste GitHub URL と書いてある枠）に、コピーしたURLをそのまま貼り付けます。

残りの項目を入力する

Branch: main（または master）

Main file path: menwake3.py と手入力します。

「Deploy!」を押す

画面右下の 「Deploy!」 ボタンをクリックします。

URLを貼り付けると「This repository does not exist」という赤文字のエラーが消え、一番下の「Deploy!」ボタンが押せるようになります。押せたらそのまま2〜3分待ってみてください！

The field needs to contain a Github URL pointing to a .py file (e.g. https://github.com/username/repository/blob/master/streamlit_app.py).貼り付けたらこんなの出てきたよ

Main file path ではなく、URLを入れる枠に「.pyファイルまでの直接リンク」を入れてほしいという案内ですね！

先ほどコピーしたURLの最後に /blob/main/menwake3.py（または /blob/master/menwake3.py）を付け足して貼り付ければ一発で解決します。

以下の手順で貼り付けてみてください！

正しいURLの貼り付け手順
入力枠に以下の形式でURLを貼り付けます：

Plaintext
https://github.com/ご自身のアカウント名/menwake/blob/main/menwake3.py
※もしエラーが出る場合は、main の部分を master に変えてみてください：
[https://github.com/ご自身のアカウント名/menwake/blob/master/menwake3.py](https://github.com/ご自身のアカウント名/menwake/blob/master/menwake3.py)

貼り付けると下の Main file path などの枠が自動でセットされます。

画面右下の 「Deploy!」 ボタンを押します。

これでエラーが消えて「Deploy!」が押せるようになります！押したらそのまま2〜3分待ってみてください。

これはURLを知っていたらどの端末でも開けますか？

はい、URLを知っている人であれば、どの端末（スマホ、PC、タブレットなど）からでも開くことができます！

iPhoneやAndroidの標準ブラウザ（SafariやChromeなど）からアクセス可能で、特別なアプリのインストールも不要です。

アプリ共有時のワンポイント
LINEでの共有
LINEでURLを送ると、トーク画面内でそのままアプリが開いて操作できます。

お気に入り・ホーム画面追加
よく使うメンバーには、スマホのブラウザメニューから「ホーム画面に追加」をしてもらうと、次回からアイコン一発でアプリを起動できるようになります。

データ更新について
誰かが履歴を追加したりシャッフルを行ったりしても、他の人の画面には影響せず、それぞれ独立して操作・閲覧が可能です。

スマホから実際にアクセスしてみて、表示や動作に問題がないか確認してみてください！

開けました！携帯画面でも見やすいように設定を変えていきたいんだけど、いける？

開通おめでとうございます！スマホでしっかり動く状態までたどり着けましたね！

もちろん、スマホの小さな画面に合わせてUI（表示レイアウト）を見やすく調整することは可能です。

スマホ対応でよく行われる代表的な改善パターンをいくつか挙げます。気になるものや「ここをこうしたい」という点を選んで教えてください！

スマホ向けのおすすめカスタマイズ案
画面の横幅をフル活用する（Wideモード）

スマホの画面端まで表示領域を広げ、テーブル（表）の文字切れや余計な改行を防ぎます。

ボタンや文字のサイズ調整

「シャッフル」や「コピー」などの操作ボタンを大きく押しやすくしたり、テキストのレイアウトを縦並び（1列）に整えたりします。

テーブル（表）の表示最適化

スマホ画面からはみ出さずにスクロールなしで見られるよう、列幅や表示形式をコンパクトに調整します。

コピペ用リスト（名前のみ）のスマホ最適化

スマホで長押し選択・コピーしやすいよう、テキストエリアの高さやフォーマットを調整します。

まずは 「1. 画面の横幅を広げる設定（Wideモード）」 や 「スマホで開いた時に一番気になる見づらい部分」 から修正するのがおすすめです。

どこから調整していきたいか、ご希望を教えてください！

条件設定の選択肢を、全部開業したい

条件設定の選択肢をすべて「改行」して縦に並べると、スマホ画面でも押しやすく見やすくなりますね！

menwake3.py の条件設定部分（st.multiselect や st.checkbox など）を改行・1列（1カラム）表示に整えたコードを作成します。

現在の menwake3.py のコードを見ながら調整しますので、現在の menwake3.py の全コードを貼り付けて教えていただけますか？

コードをいただき次第、選択肢がすっきり縦に改行されて見やすくなるように書き換えてお渡しします！

import streamlit as st

import pandas as pd

import random



# --- ページ設定 ---

st.set_page_config(page_title="テニス面分け", page_icon="🎾", layout="centered")



st.title("🎾 テニス面分け")

st.caption("人数均等配置（学年ごとの被り回避・実力・NGペア条件最適化）")



# --- カスタム優先順位の定義 ---

CUSTOM_ORDER = [

    "井上", "岩田", "長瀬", "宮井", "横田", "池田", "植田", "坂本",

    "比嘉", "藤吉", "松下", "池内", "木下", "清水", "髙木", "高木",

    "大平", "尾形", "洪", "小坂", "呉", "野津", "平賀"

]

order_map = {name: i for i, name in enumerate(CUSTOM_ORDER)}



# 初期データ＆セッション状態の管理

if "members_df" not in st.session_state:

    default_data = [

        {"シングルスランク": 1, "名前": "池内", "学年": "2年"},

        {"シングルスランク": 2, "名前": "井上", "学年": "4年"},

        {"シングルスランク": 3, "名前": "植田", "学年": "3年"},

        {"シングルスランク": 4, "名前": "岩田", "学年": "4年"},

        {"シングルスランク": 5, "名前": "松下", "学年": "3年"},

        {"シングルスランク": 6, "名前": "宮井", "学年": "4年"},

        {"シングルスランク": 7, "名前": "横田", "学年": "4年"},

        {"シングルスランク": 8, "名前": "坂本", "学年": "3年"},

        {"シングルスランク": 9, "名前": "比嘉", "学年": "3年"},

        {"シングルスランク": 10, "名前": "清水", "学年": "2年"},

        {"シングルスランク": 11, "名前": "長瀬", "学年": "4年"},

        {"シングルスランク": 12, "名前": "木下", "学年": "2年"},

        {"シングルスランク": 13, "名前": "洪", "学年": "1年"},

        {"シングルスランク": 14, "名前": "藤吉", "学年": "3年"},

        {"シングルスランク": 15, "名前": "池田", "学年": "3年"},

        {"シングルスランク": 16, "名前": "髙木", "学年": "2年"},

        {"シングルスランク": 17, "名前": "尾形", "学年": "1年"},

        {"シングルスランク": 18, "名前": "呉", "学年": "1年"},

        {"シングルスランク": 19, "名前": "野津", "学年": "1年"},

        {"シングルスランク": 20, "名前": "平賀", "学年": "1年"},

        {"シングルスランク": 21, "名前": "小坂", "学年": "1年"},

        {"シングルスランク": 22, "名前": "大平", "学年": "1年"}

    ]

    st.session_state.members_df = pd.DataFrame(default_data)



if "history" not in st.session_state:

    st.session_state.history = []



def sort_by_custom_order(names_list):

    return sorted(names_list, key=lambda x: order_map.get(x, 999))



# --- 1. メンバー管理エリア ---

st.subheader("📋 メンバーリスト（シングルスランク順）")

st.caption("※ 上にある人ほどレベルが高い設定です。表を直接編集して追加・削除・並び替えができます。")



edited_df = st.data_editor(

    st.session_state.members_df,

    num_rows="dynamic",

    use_container_width=True,

    column_config={

        "シングルスランク": st.column_config.NumberColumn("シングルスランク", help="数字が小さいほど上手い", min_value=1),

        "学年": st.column_config.SelectboxColumn("学年", options=["4年", "3年", "2年", "1年"])

    }

)



st.session_state.members_df = edited_df



# --- 2. 別けるペアの設定＆オプションエリア ---

st.markdown("---")

st.subheader("⚡ 条件設定")



# NGペアの選択肢

ng_pair_choice = st.radio(

    "必ず別々のコートにするペアを選択してください",

    options=["指定なし", "（池田、比嘉）を別々にする", "（坂本、藤吉）を別々にする"],

    index=0,

    horizontal=True

)



avoid_duplicates = st.checkbox("🔄 過去の振り分けと学年ごとの被りを最小化する", value=True)



# 学年別重複率の計算関数

def get_grade_similarity_score(df_a, history, member_grade_map):

    if not history:

        return 0.0

   

    max_score = 0.0

    grades = ["4年", "3年", "2年", "1年"]

    a_names = set(df_a["名前"].tolist())

   

    for past in history[-3:]:

        past_a_names = set(past["A_names"])

        past_b_names = set(past["B_names"])

       

        for past_set in [past_a_names, past_b_names]:

            grade_sims = []

            for g in grades:

                curr_g_members = set([m for m in a_names if member_grade_map.get(m) == g])

                past_g_members = set([m for m in past_set if member_grade_map.get(m) == g])

               

                if curr_g_members:

                    overlap = len(curr_g_members.intersection(past_g_members)) / len(curr_g_members)

                    grade_sims.append(overlap)

           

            if grade_sims:

                avg_sim = sum(grade_sims) / len(grade_sims)

                max_score = max(max_score, avg_sim)

               

    return max_score



# --- 3. 被り自動回避付き面分けロジック ---

def divide_courts(df, ng_choice, history, avoid_dup):

    df_sorted = df.sort_values("シングルスランク").reset_index(drop=True)

    target_per_court = len(df_sorted) // 2

   

    member_grade_map = dict(zip(df_sorted["名前"], df_sorted["学年"]))

   

    # NGペアの割り出し

    p1, p2 = None, None

    if ng_choice == "（池田、比嘉）を別々にする":

        p1, p2 = "池田", "比嘉"

    elif ng_choice == "（坂本、藤吉）を別々にする":

        p1, p2 = "坂本", "藤吉"

       

    best_df_a = pd.DataFrame()

    best_df_b = pd.DataFrame()

    lowest_grade_sim = 1.0

   

    for _ in range(1500):

        court_a = []

        court_b = []

       

        grades = ["4年", "3年", "2年", "1年"]

        for g in grades:

            g_members = df_sorted[df_sorted["学年"] == g].to_dict('records')

            random.shuffle(g_members)

           

            half = len(g_members) // 2

            if len(g_members) % 2 != 0 and random.choice([True, False]):

                half += 1

               

            court_a.extend(g_members[:half])

            court_b.extend(g_members[half:])

           

        if len(court_a) != target_per_court or len(court_b) != target_per_court:

            continue

           

        df_a = pd.DataFrame(court_a)

        df_b = pd.DataFrame(court_b)

       

        # ① 上位6名判定

        top6_names = set(df_sorted.iloc[:6]["名前"].tolist())

        a_top6_count = len([m for m in df_a["名前"] if m in top6_names])

        if a_top6_count != 3:

            continue

           

        # ② NGペア判定

        names_a = df_a["名前"].tolist()

        names_b = df_b["名前"].tolist()

       

        if p1 and p2:

            if (p1 in names_a and p2 in names_a) or (p1 in names_b and p2 in names_b):

                continue

               

        # ③ 学年ごとの履歴被りスコア判定

        grade_sim_score = get_grade_similarity_score(df_a, history, member_grade_map)

       

        if grade_sim_score < lowest_grade_sim:

            lowest_grade_sim = grade_sim_score

            best_df_a = df_a.sort_values("シングルスランク").reset_index(drop=True)

            best_df_b = df_b.sort_values("シングルスランク").reset_index(drop=True)

           

        if avoid_dup:

            if grade_sim_score < 0.5:

                return best_df_a, best_df_b, grade_sim_score

        else:

            return best_df_a, best_df_b, grade_sim_score



    return best_df_a, best_df_b, lowest_grade_sim



# --- 4. 振り分け実行エリア ---

st.markdown("---")

col_btn1, col_btn2 = st.columns([3, 1])



with col_btn1:

    exec_button = st.button("🎲 2面にチーム分け（シャッフル）", use_container_width=True, type="primary")

with col_btn2:

    if st.button("🗑️ 履歴リセット", use_container_width=True):

        st.session_state.history = []

        st.toast("履歴をリセットしました")



if exec_button:

    df_clean = edited_df.dropna(subset=["名前"]).copy()

    df_clean = df_clean[df_clean["名前"].str.strip() != ""]

   

    total_count = len(df_clean)

   

    if total_count < 6:

        st.error("上位6人均等配置のため、6名以上メンバーを登録してください。")

    elif total_count % 2 != 0:

        st.error(f"両コートの人数を均等にするため、偶数名で登録してください。（現在の有効人数: {total_count}名）")

    else:

        df_a, df_b, grade_sim = divide_courts(df_clean, ng_pair_choice, st.session_state.history, avoid_duplicates)

       

        if df_a.empty or df_b.empty:

            st.error("指定された条件を満たす組み合わせが見つかりませんでした。設定を見直してください。")

        else:

            names_a = df_a["名前"].tolist()

            names_b = df_b["名前"].tolist()

           

            # 履歴に追加

            st.session_state.history.append({

                "A_names": names_a,

                "B_names": names_b

            })

           

            st.success(f"✨ 学年ごとの被りを抑えた新構成で振り分けました！（直近の学年平均一致度: {int(grade_sim * 100)}%）")

           

            # --- メイン表（シングルスランク順） ---

            col1, col2 = st.columns(2)

           

            with col1:

                st.success(f"🎾 **Aコート** ({len(df_a)}名)")

                st.dataframe(df_a[["名前", "学年", "シングルスランク"]], use_container_width=True, hide_index=True)

                counts_a = df_a["学年"].value_counts()

                st.caption(f"内訳: 4年:{counts_a.get('4年',0)} / 3年:{counts_a.get('3年',0)} / 2年:{counts_a.get('2年',0)} / 1年:{counts_a.get('1年',0)}")

               

            with col2:

                st.info(f"🎾 **Bコート** ({len(df_b)}名)")

                st.dataframe(df_b[["名前", "学年", "シングルスランク"]], use_container_width=True, hide_index=True)

                counts_b = df_b["学年"].value_counts()

                st.caption(f"内訳: 4年:{counts_b.get('4年',0)} / 3年:{counts_b.get('3年',0)} / 2年:{counts_b.get('2年',0)} / 1年:{counts_b.get('1年',0)}")



            # --- 名前のみ一覧（指定優先順） ---

            st.markdown("---")

            st.subheader("📝 メンバー一覧（指定優先順）")

            st.caption("※ 指定された優先順位（井上・岩田・長瀬...）に並べ替えたテキスト一覧です。")



            sorted_a_names = sort_by_custom_order(names_a)

            sorted_b_names = sort_by_custom_order(names_b)



            col_list1, col_list2 = st.columns(2)

            with col_list1:

                st.markdown("**【Aコート】**")

                st.code("\n".join(sorted_a_names), language=None)



            with col_list2:

                st.markdown("**【Bコート】**")

                st.code("\n".join(sorted_b_names), language=None)



# --- 5. 履歴表示エリア ---

if st.session_state.history:

    st.markdown("---")

    with st.expander(f"📜 過去の振り分け履歴（全 {len(st.session_state.history)} 回）"):

        for idx, item in enumerate(reversed(st.session_state.history)):

            run_num = len(st.session_state.history) - idx

            st.write(f"**第 {run_num} 回の面分け**")

           

            hist_a_sorted = sort_by_custom_order(item['A_names'])

            hist_b_sorted = sort_by_custom_order(item['B_names'])

           

            h_col1, h_col2 = st.columns(2)

            with h_col1:

                st.caption(f"Aコート: {', '.join(hist_a_sorted)}")

            with h_col2:

                st.caption(f"Bコート: {', '.join(hist_b_sorted)}")

            st.divider()

コードを共有いただきありがとうございます！

スマホ表示で見やすくするために、ご要望の「ラジオボタン（NGペア選択肢）の縦並び（改行）」に加えて、スマホ画面で快適に使える以下の最適化を行った最新コードを作成しました。

スマホ向けに行った変更点
選択肢の縦並び化（改行）

st.radio の horizontal=True（横並び）を削除し、選択肢が縦にすっきり改行して表示されるように修正しました。

スマホ横幅最適化（layout="wide"）

画面端まで広く使うことで、スマホで表やボタンが見切れないように最適化しました。

ボタンと表のスマホ配置調整

「シャッフル」ボタンや「履歴リセット」ボタンを押しやすく整え、各エリアの可読性を高めています。

更新後の全コード (menwake3.py)
以下のコードをコピーして、GitHub上の menwake3.py を上書き（Edit / Commit）してください。

Python
import streamlit as st
import pandas as pd
import random

# --- ページ設定（スマホで見やすい wide レイアウトに変更） ---
st.set_page_config(page_title="テニス面分け", page_icon="🎾", layout="wide")

st.title("🎾 テニス面分け")
st.caption("人数均等配置（学年ごとの被り回避・実力・NGペア条件最適化）")

# --- カスタム優先順位の定義 ---
CUSTOM_ORDER = [
    "井上", "岩田", "長瀬", "宮井", "横田", "池田", "植田", "坂本",
    "比嘉", "藤吉", "松下", "池内", "木下", "清水", "髙木", "高木",
    "大平", "尾形", "洪", "小坂", "呉", "野津", "平賀"
]
order_map = {name: i for i, name in enumerate(CUSTOM_ORDER)}

# 初期データ＆セッション状態の管理
if "members_df" not in st.session_state:
    default_data = [
        {"シングルスランク": 1, "名前": "池内", "学年": "2年"},
        {"シングルスランク": 2, "名前": "井上", "学年": "4年"},
        {"シングルスランク": 3, "名前": "植田", "学年": "3年"},
        {"シングルスランク": 4, "名前": "岩田", "学年": "4年"},
        {"シングルスランク": 5, "名前": "松下", "学年": "3年"},
        {"シングルスランク": 6, "名前": "宮井", "学年": "4年"},
        {"シングルスランク": 7, "名前": "横田", "学年": "4年"},
        {"シングルスランク": 8, "名前": "坂本", "学年": "3年"},
        {"シングルスランク": 9, "名前": "比嘉", "学年": "3年"},
        {"シングルスランク": 10, "名前": "清水", "学年": "2年"},
        {"シングルスランク": 11, "名前": "長瀬", "学年": "4年"},
        {"シングルスランク": 12, "名前": "木下", "学年": "2年"},
        {"シングルスランク": 13, "名前": "洪", "学年": "1年"},
        {"シングルスランク": 14, "名前": "藤吉", "学年": "3年"},
        {"シングルスランク": 15, "名前": "池田", "学年": "3年"},
        {"シングルスランク": 16, "名前": "髙木", "学年": "2年"},
        {"シングルスランク": 17, "名前": "尾形", "学年": "1年"},
        {"シングルスランク": 18, "名前": "呉", "学年": "1年"},
        {"シングルスランク": 19, "名前": "野津", "学年": "1年"},
        {"シングルスランク": 20, "名前": "平賀", "学年": "1年"},
        {"シングルスランク": 21, "名前": "小坂", "学年": "1年"},
        {"シングルスランク": 22, "名前": "大平", "学年": "1年"}
    ]
    st.session_state.members_df = pd.DataFrame(default_data)

if "history" not in st.session_state:
    st.session_state.history = []

def sort_by_custom_order(names_list):
    return sorted(names_list, key=lambda x: order_map.get(x, 999))

# --- 1. メンバー管理エリア ---
st.subheader("📋 メンバーリスト（シングルスランク順）")
st.caption("※ 上にある人ほどレベルが高い設定です。表を直接編集して追加・削除・並び替えができます。")

edited_df = st.data_editor(
    st.session_state.members_df,
    num_rows="dynamic",
    use_container_width=True,
    column_config={
        "シングルスランク": st.column_config.NumberColumn("シングルスランク", help="数字が小さいほど上手い", min_value=1),
        "学年": st.column_config.SelectboxColumn("学年", options=["4年", "3年", "2年", "1年"])
    }
)

st.session_state.members_df = edited_df

# --- 2. 分けるペアの設定＆オプションエリア ---
st.markdown("---")
st.subheader("⚡ 条件設定")

# NGペアの選択肢（縦並び・改行表示）
ng_pair_choice = st.radio(
    "必ず別々のコートにするペアを選択してください",
    options=["指定なし", "（池田、比嘉）を別々にする", "（坂本、藤吉）を別々にする"],
    index=0
)

avoid_duplicates = st.checkbox("🔄 過去の振り分けと学年ごとの被りを最小化する", value=True)

# 学年別重複率の計算関数
def get_grade_similarity_score(df_a, history, member_grade_map):
    if not history:
        return 0.0
    
    max_score = 0.0
    grades = ["4年", "3年", "2年", "1年"]
    a_names = set(df_a["名前"].tolist())
    
    for past in history[-3:]:
        past_a_names = set(past["A_names"])
        past_b_names = set(past["B_names"])
        
        for past_set in [past_a_names, past_b_names]:
            grade_sims = []
            for g in grades:
                curr_g_members = set([m for m in a_names if member_grade_map.get(m) == g])
                past_g_members = set([m for m in past_set if member_grade_map.get(m) == g])
                
                if curr_g_members:
                    overlap = len(curr_g_members.intersection(past_g_members)) / len(curr_g_members)
                    grade_sims.append(overlap)
            
            if grade_sims:
                avg_sim = sum(grade_sims) / len(grade_sims)
                max_score = max(max_score, avg_sim)
                
    return max_score

# --- 3. 被り自動回避付き面分けロジック ---
def divide_courts(df, ng_choice, history, avoid_dup):
    df_sorted = df.sort_values("シングルスランク").reset_index(drop=True)
    target_per_court = len(df_sorted) // 2
    
    member_grade_map = dict(zip(df_sorted["名前"], df_sorted["学年"]))
    
    # NGペアの割り出し
    p1, p2 = None, None
    if ng_choice == "（池田、比嘉）を別々にする":
        p1, p2 = "池田", "比嘉"
    elif ng_choice == "（坂本、藤吉）を別々にする":
        p1, p2 = "坂本", "藤吉"
        
    best_df_a = pd.DataFrame()
    best_df_b = pd.DataFrame()
    lowest_grade_sim = 1.0
    
    for _ in range(1500):
        court_a = []
        court_b = []
        
        grades = ["4年", "3年", "2年", "1年"]
        for g in grades:
            g_members = df_sorted[df_sorted["学年"] == g].to_dict('records')
            random.shuffle(g_members)
            
            half = len(g_members) // 2
            if len(g_members) % 2 != 0 and random.choice([True, False]):
                half += 1
                
            court_a.extend(g_members[:half])
            court_b.extend(g_members[half:])
            
        if len(court_a) != target_per_court or len(court_b) != target_per_court:
            continue
            
        df_a = pd.DataFrame(court_a)
        df_b = pd.DataFrame(court_b)
        
        # ① 上位6名判定
        top6_names = set(df_sorted.iloc[:6]["名前"].tolist())
        a_top6_count = len([m for m in df_a["名前"] if m in top6_names])
        if a_top6_count != 3:
            continue
            
        # ② NGペア判定
        names_a = df_a["名前"].tolist()
        names_b = df_b["名前"].tolist()
        
        if p1 and p2:
            if (p1 in names_a and p2 in names_a) or (p1 in names_b and p2 in names_b):
                continue
                
        # ③ 学年ごとの履歴被りスコア判定
        grade_sim_score = get_grade_similarity_score(df_a, history, member_grade_map)
        
        if grade_sim_score < lowest_grade_sim:
            lowest_grade_sim = grade_sim_score
            best_df_a = df_a.sort_values("シングルスランク").reset_index(drop=True)
            best_df_b = df_b.sort_values("シングルスランク").reset_index(drop=True)
            
        if avoid_dup:
            if grade_sim_score < 0.5:
                return best_df_a, best_df_b, grade_sim_score
        else:
            return best_df_a, best_df_b, grade_sim_score

    return best_df_a, best_df_b, lowest_grade_sim

# --- 4. 振り分け実行エリア ---
st.markdown("---")
exec_button = st.button("🎲 2面にチーム分け（シャッフル）", use_container_width=True, type="primary")

if st.button("🗑️ 履歴リセット", use_container_width=True):
    st.session_state.history = []
    st.toast("履歴をリセットしました")

if exec_button:
    df_clean = edited_df.dropna(subset=["名前"]).copy()
    df_clean = df_clean[df_clean["名前"].str.strip() != ""]
    
    total_count = len(df_clean)
    
    if total_count < 6:
        st.error("上位6人均等配置のため、6名以上メンバーを登録してください。")
    elif total_count % 2 != 0:
        st.error(f"両コートの人数を均等にするため、偶数名で登録してください。（現在の有効人数: {total_count}名）")
    else:
        df_a, df_b, grade_sim = divide_courts(df_clean, ng_pair_choice, st.session_state.history, avoid_duplicates)
        
        if df_a.empty or df_b.empty:
            st.error("指定された条件を満たす組み合わせが見つかりませんでした。設定を見直してください。")
        else:
            names_a = df_a["名前"].tolist()
            names_b = df_b["名前"].tolist()
            
            # 履歴に追加
            st.session_state.history.append({
                "A_names": names_a,
                "B_names": names_b
            })
            
            st.success(f"✨ 学年ごとの被りを抑えた新構成で振り分けました！（直近の学年平均一致度: {int(grade_sim * 100)}%）")
            
            # --- メイン表（シングルスランク順） ---
            col1, col2 = st.columns(2)
            
            with col1:
                st.success(f"🎾 **Aコート** ({len(df_a)}名)")
                st.dataframe(df_a[["名前", "学年", "シングルスランク"]], use_container_width=True, hide_index=True)
                counts_a = df_a["学年"].value_counts()
                st.caption(f"内訳: 4年:{counts_a.get('4年',0)} / 3年:{counts_a.get('3年',0)} / 2年:{counts_a.get('2年',0)} / 1年:{counts_a.get('1年',0)}")
                
            with col2:
                st.info(f"🎾 **Bコート** ({len(df_b)}名)")
                st.dataframe(df_b[["名前", "学年", "シングルスランク"]], use_container_width=True, hide_index=True)
                counts_b = df_b["学年"].value_counts()
                st.caption(f"内訳: 4年:{counts_b.get('4年',0)} / 3年:{counts_b.get('3年',0)} / 2年:{counts_b.get('2年',0)} / 1年:{counts_b.get('1年',0)}")

            # --- 名前のみ一覧（指定優先順） ---
            st.markdown("---")
            st.subheader("📝 メンバー一覧（指定優先順）")
            st.caption("※ 指定された優先順位（井上・岩田・長瀬...）に並べ替えたテキスト一覧です。")

            sorted_a_names = sort_by_custom_order(names_a)
            sorted_b_names = sort_by_custom_order(names_b)

            col_list1, col_list2 = st.columns(2)
            with col_list1:
                st.markdown("**【Aコート】**")
                st.code("\n".join(sorted_a_names), language=None)

            with col_list2:
                st.markdown("**【Bコート】**")
                st.code("\n".join(sorted_b_names), language=None)

# --- 5. 履歴表示エリア ---
if st.session_state.history:
    st.markdown("---")
    with st.expander(f"📜 過去の振り分け履歴（全 {len(st.session_state.history)} 回）"):
        for idx, item in enumerate(reversed(st.session_state.history)):
            run_num = len(st.session_state.history) - idx
            st.write(f"**第 {run_num} 回の面分け**")
            
            hist_a_sorted = sort_by_custom_order(item['A_names'])
            hist_b_sorted = sort_by_custom_order(item['B_names'])
            
            h_col1, h_col2 = st.columns(2)
            with h_col1:
                st.caption(f"Aコート: {', '.join(hist_a_sorted)}")
            with h_col2:
                st.caption(f"Bコート: {', '.join(hist_b_sorted)}")
            st.divider()
反映手順
GitHub を開き、menwake リポジトリの中にある menwake3.py を選択します。

鉛筆アイコン（Edit）を押して、上記のコードにすべて置き換えます。

一番下の 「Commit changes」 をクリックします。

1〜2分後にアプリのURLを再読み込み（リロード）すると、新しいレイアウトが反映されます！

また、複数端末で開いても、履歴が残るようにしたい（一括の履歴）にできる

複数端末で同じ履歴を共有する（一括の履歴管理にする）ことは、データベースなどの外部保存場所を追加することで対応可能です！

現状の仕組みと、データベースを導入する場合の仕組みの違いは以下の通りです。

なぜ現在は端末ごとに履歴がバラバラなのか？
現在使っている st.session_state.history は、アプリを開いている「各ユーザーのブラウザ一時メモリ（セッション）」に保存されています。
そのため、Aさんのスマホでシャッフルしても、Bさんのスマホにはその履歴が届かない状態になっています。

全端末で一括共有できるようにする方法
全端末で「誰かがシャッフルしたら全員の履歴に即座に追加される」状態にするには、無料のクラウドデータベース（Supabase や Firebase、または Google スプレッドシートなど）に履歴データを読み書きする仕組みを追加します。

実現に必要なステップ：
無料のデータベース（例: Supabase）でアカウントを作成

無料プランで十分運用可能です。

履歴用のテーブル（データ格納場所）を作成

日時、Aコートメンバー、Bコートメンバーを保存する列を作成。

requirements.txt と menwake3.py に連携処理を追加

シャッフルボタンを押した時にデータベースに書き込み、履歴表示欄でデータベースから最新履歴を取得する処理を追加します。

こちらの外部データベース連携（Supabase等を使った全端末共有機能）のコード作成や手順を進めますか？ご希望があれば設定方法から案内します！

urlは一つなので、そこに飛んだら、どの端末でも結果が保存されているというようにはできませんか

URL（1つのリンク）を開いた全員が同じ最新結果や履歴を見られるようにすることは可能です！

現在、結果が端末ごとに保存されないのは、Streamlitが「アクセスした人ごとに独立した画面（セッション）」を作る仕組みになっているからです。

全員で同じ結果や履歴をリアルタイムに共有・保存するには、以下の 2つの方法 があります。

方法1：Streamlitの共有メモリを使う（一番簡単・追加登録なし）
外部のデータベースを使わずに、Streamlit自体が動いているサーバー上のメモリ（st.cache_data やグローバル変数）に履歴を保存する方法です。

メリット: 新しいサービスへの会員登録などが一切不要。コードを少し書き換えるだけで即座に反映できます。

デメリット: Streamlitのサーバーが再起動（数日間アクセスがない場合や、コードを更新した時）すると、履歴が初期化されます。

おすすめ: 「その日の練習の中で、全員が同じ最新結果や過去数回の履歴を見られれば十分」という場合。

方法2：無料の外部データベース（Supabase等）に保存する
無料のクラウドデータベースに履歴を保存し、アプリ起動時にそこから読み込みます。

メリット: アプリやサーバーが再起動しても、過去の履歴が永久に残り続けます。どの端末からアクセスしても常に全く同じ過去データが表示されます。

デメリット: Supabase（無料）などのアカウント作成と、接続設定（APIキーの設定）が最初だけ必要になります。

おすすめ: 「過去何ヶ月分もの振り分け履歴をずっと残しておきたい」という場合。

まずは一番手軽な 「方法1（Streamlit共有メモリで全員リアルタイム共有）」 のコードを作成して試してみるのがおすすめです！

方法1の修正コードを作成して、menwake3.py の差し替え手順をご案内しましょうか？

方法１ではどのくらいの期間で履歴が消失してしまいますか？

方法1（Streamlitの共有メモリ）で履歴が保持される期間やリセットのタイミングは、主に以下のルールで決まります。

履歴が消えるタイミングと期間の目安
アクセスがない場合：約7日〜14日（スリープ時）
Streamlit Community Cloudでは、アプリへのアクセスが一定期間（通常7日間程度）途切れるとアプリが自動的に「スリープ（一時停止）」状態に入ります。スリープに入るとサーバーのメモリが解放されるため、保存されていた履歴は消去されます。

コードの更新（Commit）時：即時リセット
GitHubで menwake3.py などを更新して再デプロイが行われたタイミングで、サーバーが再起動するため履歴はクリアされます。

サーバーの自動再起動時：不定期（数日〜数週間）
Streamlit側のメンテナンスやサーバー再起動が入った場合もメモリがリセットされます。

まとめると
練習当日のリアルタイム共有（「今日の第1回〜第3回の面分け結果を全員のスマホで見る」など）や、毎週定期的にアクセスがある状態であれば、基本的にはそのまま保持されます。

ただし、「数ヶ月前の履歴をずっと保存しておきたい」 という用途には不向きです。

まずは手軽な方法1で運用してみて、「やっぱり何ヶ月分も永続的に残したい」と感じた段階で方法2（Supabase連携）へ移行するのがおすすめです。

方法1（追加登録なしで全員共有できるコード）に書き換える準備を整えましょうか？

週に二回は必ずアクセスがあります

週に2回アクセスがあるのであれば、方法1（Streamlit共有メモリ）で実用上は十分に履歴を維持できます！

アクセスが途切れないためアプリがスリープにならず、毎週の練習で全員が同じ最新結果や履歴を共有し続けることが可能です。

コードを書き換えて、どの端末（誰のスマホ）から開いても同じ履歴が更新・表示される仕組みを追加した最新コードを作成しました。

更新後の全コード (menwake3.py)
以下のコードをコピーして、GitHub上の menwake3.py を上書き（Edit / Commit）してください。

Python
import streamlit as st
import pandas as pd
import random

# --- ページ設定（スマホで見やすい wide レイアウト） ---
st.set_page_config(page_title="テニス面分け", page_icon="🎾", layout="wide")

st.title("🎾 テニス面分け")
st.caption("人数均等配置（学年ごとの被り回避・実力・NGペア条件最適化）")

# --- 1. 全端末で共有するグローバル共有メモリ（履歴データ） ---
@st.cache_resource
def get_shared_history():
    # アプリ全体で共通して保持されるリスト
    return []

shared_history = get_shared_history()

# --- カスタム優先順位の定義 ---
CUSTOM_ORDER = [
    "井上", "岩田", "長瀬", "宮井", "横田", "池田", "植田", "坂本",
    "比嘉", "藤吉", "松下", "池内", "木下", "清水", "髙木", "高木",
    "大平", "尾形", "洪", "小坂", "呉", "野津", "平賀"
]
order_map = {name: i for i, name in enumerate(CUSTOM_ORDER)}

# 初期データ＆セッション状態の管理
if "members_df" not in st.session_state:
    default_data = [
        {"シングルスランク": 1, "名前": "池内", "学年": "2年"},
        {"シングルスランク": 2, "名前": "井上", "学年": "4年"},
        {"シングルスランク": 3, "名前": "植田", "学年": "3年"},
        {"シングルスランク": 4, "名前": "岩田", "学年": "4年"},
        {"シングルスランク": 5, "名前": "松下", "学年": "3年"},
        {"シングルスランク": 6, "名前": "宮井", "学年": "4年"},
        {"シングルスランク": 7, "名前": "横田", "学年": "4年"},
        {"シングルスランク": 8, "名前": "坂本", "学年": "3年"},
        {"シングルスランク": 9, "名前": "比嘉", "学年": "3年"},
        {"シングルスランク": 10, "名前": "清水", "学年": "2年"},
        {"シングルスランク": 11, "名前": "長瀬", "学年": "4年"},
        {"シングルスランク": 12, "名前": "木下", "学年": "2年"},
        {"シングルスランク": 13, "名前": "洪", "学年": "1年"},
        {"シングルスランク": 14, "名前": "藤吉", "学年": "3年"},
        {"シングルスランク": 15, "名前": "池田", "学年": "3年"},
        {"シングルスランク": 16, "名前": "髙木", "学年": "2年"},
        {"シングルスランク": 17, "名前": "尾形", "学年": "1年"},
        {"シングルスランク": 18, "名前": "呉", "学年": "1年"},
        {"シングルスランク": 19, "名前": "野津", "学年": "1年"},
        {"シングルスランク": 20, "名前": "平賀", "学年": "1年"},
        {"シングルスランク": 21, "名前": "小坂", "学年": "1年"},
        {"シングルスランク": 22, "名前": "大平", "学年": "1年"}
    ]
    st.session_state.members_df = pd.DataFrame(default_data)

def sort_by_custom_order(names_list):
    return sorted(names_list, key=lambda x: order_map.get(x, 999))

# --- 2. メンバー管理エリア ---
st.subheader("📋 メンバーリスト（シングルスランク順）")
st.caption("※ 上にある人ほどレベルが高い設定です。表を直接編集して追加・削除・並び替えができます。")

edited_df = st.data_editor(
    st.session_state.members_df,
    num_rows="dynamic",
    use_container_width=True,
    column_config={
        "シングルスランク": st.column_config.NumberColumn("シングルスランク", help="数字が小さいほど上手い", min_value=1),
        "学年": st.column_config.SelectboxColumn("学年", options=["4年", "3年", "2年", "1年"])
    }
)

st.session_state.members_df = edited_df

# --- 3. 分けるペアの設定＆オプションエリア ---
st.markdown("---")
st.subheader("⚡ 条件設定")

# NGペアの選択肢（縦並び・改行表示）
ng_pair_choice = st.radio(
    "必ず別々のコートにするペアを選択してください",
    options=["指定なし", "（池田、比嘉）を別々にする", "（坂本、藤吉）を別々にする"],
    index=0
)

avoid_duplicates = st.checkbox("🔄 過去の振り分けと学年ごとの被りを最小化する", value=True)

# 学年別重複率の計算関数
def get_grade_similarity_score(df_a, history, member_grade_map):
    if not history:
        return 0.0
    
    max_score = 0.0
    grades = ["4年", "3年", "2年", "1年"]
    a_names = set(df_a["名前"].tolist())
    
    for past in history[-3:]:
        past_a_names = set(past["A_names"])
        past_b_names = set(past["B_names"])
        
        for past_set in [past_a_names, past_b_names]:
            grade_sims = []
            for g in grades:
                curr_g_members = set([m for m in a_names if member_grade_map.get(m) == g])
                past_g_members = set([m for m in past_set if member_grade_map.get(m) == g])
                
                if curr_g_members:
                    overlap = len(curr_g_members.intersection(past_g_members)) / len(curr_g_members)
                    grade_sims.append(overlap)
            
            if grade_sims:
                avg_sim = sum(grade_sims) / len(grade_sims)
                max_score = max(max_score, avg_sim)
                
    return max_score

# --- 4. 被り自動回避付き面分けロジック ---
def divide_courts(df, ng_choice, history, avoid_dup):
    df_sorted = df.sort_values("シングルスランク").reset_index(drop=True)
    target_per_court = len(df_sorted) // 2
    
    member_grade_map = dict(zip(df_sorted["名前"], df_sorted["学年"]))
    
    # NGペアの割り出し
    p1, p2 = None, None
    if ng_choice == "（池田、比嘉）を別々にする":
        p1, p2 = "池田", "比嘉"
    elif ng_choice == "（坂本、藤吉）を別々にする":
        p1, p2 = "坂本", "藤吉"
        
    best_df_a = pd.DataFrame()
    best_df_b = pd.DataFrame()
    lowest_grade_sim = 1.0
    
    for _ in range(1500):
        court_a = []
        court_b = []
        
        grades = ["4年", "3年", "2年", "1年"]
        for g in grades:
            g_members = df_sorted[df_sorted["学年"] == g].to_dict('records')
            random.shuffle(g_members)
            
            half = len(g_members) // 2
            if len(g_members) % 2 != 0 and random.choice([True, False]):
                half += 1
                
            court_a.extend(g_members[:half])
            court_b.extend(g_members[half:])
            
        if len(court_a) != target_per_court or len(court_b) != target_per_court:
            continue
            
        df_a = pd.DataFrame(court_a)
        df_b = pd.DataFrame(court_b)
        
        # ① 上位6名判定
        top6_names = set(df_sorted.iloc[:6]["名前"].tolist())
        a_top6_count = len([m for m in df_a["名前"] if m in top6_names])
        if a_top6_count != 3:
            continue
            
        # ② NGペア判定
        names_a = df_a["名前"].tolist()
        names_b = df_b["名前"].tolist()
        
        if p1 and p2:
            if (p1 in names_a and p2 in names_a) or (p1 in names_b and p2 in names_b):
                continue
                
        # ③ 学年ごとの履歴被りスコア判定
        grade_sim_score = get_grade_similarity_score(df_a, history, member_grade_map)
        
        if grade_sim_score < lowest_grade_sim:
            lowest_grade_sim = grade_sim_score
            best_df_a = df_a.sort_values("シングルスランク").reset_index(drop=True)
            best_df_b = df_b.sort_values("シングルスランク").reset_index(drop=True)
            
        if avoid_dup:
            if grade_sim_score < 0.5:
                return best_df_a, best_df_b, grade_sim_score
        else:
            return best_df_a, best_df_b, grade_sim_score

    return best_df_a, best_df_b, lowest_grade_sim

# --- 5. 振り分け実行エリア ---
st.markdown("---")
exec_button = st.button("🎲 2面にチーム分け（シャッフル）", use_container_width=True, type="primary")

if st.button("🗑️ 共有履歴をリセット", use_container_width=True):
    shared_history.clear()
    st.toast("全員で共有している履歴をリセットしました")
    st.rerun()

if exec_button:
    df_clean = edited_df.dropna(subset=["名前"]).copy()
    df_clean = df_clean[df_clean["名前"].str.strip() != ""]
    
    total_count = len(df_clean)
    
    if total_count < 6:
        st.error("上位6人均等配置のため、6名以上メンバーを登録してください。")
    elif total_count % 2 != 0:
        st.error(f"両コートの人数を均等にするため、偶数名で登録してください。（現在の有効人数: {total_count}名）")
    else:
        df_a, df_b, grade_sim = divide_courts(df_clean, ng_pair_choice, shared_history, avoid_duplicates)
        
        if df_a.empty or df_b.empty:
            st.error("指定された条件を満たす組み合わせが見つかりませんでした。設定を見直してください。")
        else:
            names_a = df_a["名前"].tolist()
            names_b = df_b["名前"].tolist()
            
            # 全員共有の共有履歴に追加
            shared_history.append({
                "A_names": names_a,
                "B_names": names_b
            })
            
            st.success(f"✨ 学年ごとの被りを抑えた新構成で振り分けました！（直近の学年平均一致度: {int(grade_sim * 100)}%）")
            
            # --- メイン表（シングルスランク順） ---
            col1, col2 = st.columns(2)
            
            with col1:
                st.success(f"🎾 **Aコート** ({len(df_a)}名)")
                st.dataframe(df_a[["名前", "学年", "シングルスランク"]], use_container_width=True, hide_index=True)
                counts_a = df_a["学年"].value_counts()
                st.caption(f"内訳: 4年:{counts_a.get('4年',0)} / 3年:{counts_a.get('3年',0)} / 2年:{counts_a.get('2年',0)} / 1年:{counts_a.get('1年',0)}")
                
            with col2:
                st.info(f"🎾 **Bコート** ({len(df_b)}名)")
                st.dataframe(df_b[["名前", "学年", "シングルスランク"]], use_container_width=True, hide_index=True)
                counts_b = df_b["学年"].value_counts()
                st.caption(f"内訳: 4年:{counts_b.get('4年',0)} / 3年:{counts_b.get('3年',0)} / 2年:{counts_b.get('2年',0)} / 1年:{counts_b.get('1年',0)}")

            # --- 名前のみ一覧（指定優先順） ---
            st.markdown("---")
            st.subheader("📝 メンバー一覧（指定優先順）")
            st.caption("※ 指定された優先順位（井上・岩田・長瀬...）に並べ替えたテキスト一覧です。")

            sorted_a_names = sort_by_custom_order(names_a)
            sorted_b_names = sort_by_custom_order(names_b)

            col_list1, col_list2 = st.columns(2)
            with col_list1:
                st.markdown("**【Aコート】**")
                st.code("\n".join(sorted_a_names), language=None)

            with col_list2:
                st.markdown("**【Bコート】**")
                st.code("\n".join(sorted_b_names), language=None)

# --- 6. 全員共有の履歴表示エリア ---
if shared_history:
    st.markdown("---")
    with st.expander(f"📜 過去の振り分け履歴［全端末で共有］（全 {len(shared_history)} 回）", expanded=True):
        for idx, item in enumerate(reversed(shared_history)):
            run_num = len(shared_history) - idx
            st.write(f"**第 {run_num} 回の面分け**")
            
            hist_a_sorted = sort_by_custom_order(item['A_names'])
            hist_b_sorted = sort_by_custom_order(item['B_names'])
            
            h_col1, h_col2 = st.columns(2)
            with h_col1:
                st.caption(f"Aコート: {', '.join(hist_a_sorted)}")
            with h_col2:
                st.caption(f"Bコート: {', '.join(hist_b_sorted)}")
            st.divider()
変更のポイント
@st.cache_resource による共有化

アプリを実行するサーバー内の共通メモリ領域（shared_history）を使用するように変更しました。

これにより、誰かがスマホで「シャッフル」を実行すると、その結果が全員で共有されている履歴リストに追加されます。

どの端末でも最新履歴の閲覧・回避ロジック参照が可能

別の端末からURLを開いて画面をリロード（再読み込み）するだけで、他の人が振り分けた最新の履歴が表示され、次回シャッフル時の「被り回避」にも反映されます。

GitHubの menwake3.py を上記のコードに置き換えて保存（Commit changes）し、1〜2分後にアプリを更新してお試しください！

条件設定の

メッセージが途中で切れてしまっているようです！

「条件設定の」のあとに、どのような調整や機能追加をご希望でしょうか？

（例：選択肢を増やしたい、テキストの表記を変えたい、デフォルトのチェック状態を変えたい など）

ご希望内容を教えていただければ、すぐにコードを修正します！

条件設定の「指定なし」「（池田、比嘉）を別々にする」「（坂本、藤吉）を別々にする」をすべて別の行にしたい。今さっきのコードでは「指定なし」「（池田、比嘉）を別々にする」ここの改行ができていない状態です

ラジオボタンの文字数や画面幅によって、1つの選択肢内で意図しない改行が入ったり横に並んで見えてしまうことがあります。

st.radio の代わりに st.selectbox（ドロップダウン形式） を使うか、CSSで各ラジオボタンの要素を強制的に「1行ずつ独立したブロック（display: block）」として改行表示させる方法が確実です。

ここでは、見た目が一番すっきりして確実に1行ずつ改行される st.radio + カスタムCSS指定 に修正したコードを作成しました！

該当部分の修正コード (menwake3.py)
GitHubで menwake3.py を開き、条件設定 のラジオボタン周辺（# --- 3. 分けるペアの設定＆オプションエリア ---）を以下のように更新してください。

Python
# --- 3. 分けるペアの設定＆オプションエリア ---
st.markdown("---")
st.subheader("⚡ 条件設定")

# 各選択肢を強制的に1行ずつ（改行）独立して表示させるCSS
st.markdown("""
    <style>
    div[data-testid="stRadio"] > label {
        display: block !important;
        margin-bottom: 8px !important;
    }
    div[data-testid="stRadio"] div[role="radiogroup"] > label {
        display: flex !important;
        margin-bottom: 6px !important;
        width: 100% !important;
    }
    </style>
""", unsafe_allow_html=True)

# NGペアの選択肢（1行ずつ改行）
ng_pair_choice = st.radio(
    "必ず別々のコートにするペアを選択してください",
    options=[
        "指定なし",
        "（池田、比嘉）を別々にする",
        "（坂本、藤吉）を別々にする"
    ],
    index=0
)

avoid_duplicates = st.checkbox("🔄 過去の振り分けと学年ごとの被りを最小化する", value=True)
変更点
options を配列内で明確に改行記述: 各選択肢を独立した文字列として定義しました。

CSSレイアウト制御の追加: スマホの画面幅に関わらず、「指定なし」「（池田、比嘉）」「（坂本、藤吉）」がそれぞれ独立した1行として上から順に並ぶよう幅100%のブロック指定を行いました。

こちらの処理を追加してコミット（Commit changes）していただければ、スマホ画面でもキレイに3行に分かれて表示されます！

これを追加した状態のコードを一覧でだして

先ほどの「ラジオボタンの選択肢を確実に1行ずつ（縦並び・改行）独立表示させるCSS」を反映した、menwake3.py の全コード（最新版）です。

以下のコードをすべてコピーして、GitHub上の menwake3.py に上書き（Edit / Commit）してください。

Python
import streamlit as st
import pandas as pd
import random

# --- ページ設定（スマホで見やすい wide レイアウト） ---
st.set_page_config(page_title="テニス面分け", page_icon="🎾", layout="wide")

st.title("🎾 テニス面分け")
st.caption("人数均等配置（学年ごとの被り回避・実力・NGペア条件最適化）")

# --- 1. 全端末で共有するグローバル共有メモリ（履歴データ） ---
@st.cache_resource
def get_shared_history():
    # アプリ全体で共通して保持されるリスト
    return []

shared_history = get_shared_history()

# --- カスタム優先順位の定義 ---
CUSTOM_ORDER = [
    "井上", "岩田", "長瀬", "宮井", "横田", "池田", "植田", "坂本",
    "比嘉", "藤吉", "松下", "池内", "木下", "清水", "髙木", "高木",
    "大平", "尾形", "洪", "小坂", "呉", "野津", "平賀"
]
order_map = {name: i for i, name in enumerate(CUSTOM_ORDER)}

# 初期データ＆セッション状態の管理
if "members_df" not in st.session_state:
    default_data = [
        {"シングルスランク": 1, "名前": "池内", "学年": "2年"},
        {"シングルスランク": 2, "名前": "井上", "学年": "4年"},
        {"シングルスランク": 3, "名前": "植田", "学年": "3年"},
        {"シングルスランク": 4, "名前": "岩田", "学年": "4年"},
        {"シングルスランク": 5, "名前": "松下", "学年": "3年"},
        {"シングルスランク": 6, "名前": "宮井", "学年": "4年"},
        {"シングルスランク": 7, "名前": "横田", "学年": "4年"},
        {"シングルスランク": 8, "名前": "坂本", "学年": "3年"},
        {"シングルスランク": 9, "名前": "比嘉", "学年": "3年"},
        {"シングルスランク": 10, "名前": "清水", "学年": "2年"},
        {"シングルスランク": 11, "名前": "長瀬", "学年": "4年"},
        {"シングルスランク": 12, "名前": "木下", "学年": "2年"},
        {"シングルスランク": 13, "名前": "洪", "学年": "1年"},
        {"シングルスランク": 14, "名前": "藤吉", "学年": "3年"},
        {"シングルスランク": 15, "名前": "池田", "学年": "3年"},
        {"シングルスランク": 16, "名前": "髙木", "学年": "2年"},
        {"シングルスランク": 17, "名前": "尾形", "学年": "1年"},
        {"シングルスランク": 18, "名前": "呉", "学年": "1年"},
        {"シングルスランク": 19, "名前": "野津", "学年": "1年"},
        {"シングルスランク": 20, "名前": "平賀", "学年": "1年"},
        {"シングルスランク": 21, "名前": "小坂", "学年": "1年"},
        {"シングルスランク": 22, "名前": "大平", "学年": "1年"}
    ]
    st.session_state.members_df = pd.DataFrame(default_data)

def sort_by_custom_order(names_list):
    return sorted(names_list, key=lambda x: order_map.get(x, 999))

# --- 2. メンバー管理エリア ---
st.subheader("📋 メンバーリスト（シングルスランク順）")
st.caption("※ 上にある人ほどレベルが高い設定です。表を直接編集して追加・削除・並び替えができます。")

edited_df = st.data_editor(
    st.session_state.members_df,
    num_rows="dynamic",
    use_container_width=True,
    column_config={
        "シングルスランク": st.column_config.NumberColumn("シングルスランク", help="数字が小さいほど上手い", min_value=1),
        "学年": st.column_config.SelectboxColumn("学年", options=["4年", "3年", "2年", "1年"])
    }
)

st.session_state.members_df = edited_df

# --- 3. 分けるペアの設定＆オプションエリア ---
st.markdown("---")
st.subheader("⚡ 条件設定")

# 各選択肢を強制的に1行ずつ（改行）独立して表示させるCSSスタイル設定
st.markdown("""
    <style>
    div[data-testid="stRadio"] > label {
        display: block !important;
        margin-bottom: 8px !important;
    }
    div[data-testid="stRadio"] div[role="radiogroup"] > label {
        display: flex !important;
        margin-bottom: 6px !important;
        width: 100% !important;
    }
    </style>
""", unsafe_allow_html=True)

# NGペアの選択肢（CSSで確実に1行ずつ改行）
ng_pair_choice = st.radio(
    "必ず別々のコートにするペアを選択してください",
    options=[
        "指定なし",
        "（池田、比嘉）を別々にする",
        "（坂本、藤吉）を別々にする"
    ],
    index=0
)

avoid_duplicates = st.checkbox("🔄 過去の振り分けと学年ごとの被りを最小化する", value=True)

# 学年別重複率の計算関数
def get_grade_similarity_score(df_a, history, member_grade_map):
    if not history:
        return 0.0
    
    max_score = 0.0
    grades = ["4年", "3年", "2年", "1年"]
    a_names = set(df_a["名前"].tolist())
    
    for past in history[-3:]:
        past_a_names = set(past["A_names"])
        past_b_names = set(past["B_names"])
        
        for past_set in [past_a_names, past_b_names]:
            grade_sims = []
            for g in grades:
                curr_g_members = set([m for m in a_names if member_grade_map.get(m) == g])
                past_g_members = set([m for m in past_set if member_grade_map.get(m) == g])
                
                if curr_g_members:
                    overlap = len(curr_g_members.intersection(past_g_members)) / len(curr_g_members)
                    grade_sims.append(overlap)
            
            if grade_sims:
                avg_sim = sum(grade_sims) / len(grade_sims)
                max_score = max(max_score, avg_sim)
                
    return max_score

# --- 4. 被り自動回避付き面分けロジック ---
def divide_courts(df, ng_choice, history, avoid_dup):
    df_sorted = df.sort_values("シングルスランク").reset_index(drop=True)
    target_per_court = len(df_sorted) // 2
    
    member_grade_map = dict(zip(df_sorted["名前"], df_sorted["学年"]))
    
    # NGペアの割り出し
    p1, p2 = None, None
    if ng_choice == "（池田、比嘉）を別々にする":
        p1, p2 = "池田", "比嘉"
    elif ng_choice == "（坂本、藤吉）を別々にする":
        p1, p2 = "坂本", "藤吉"
        
    best_df_a = pd.DataFrame()
    best_df_b = pd.DataFrame()
    lowest_grade_sim = 1.0
    
    for _ in range(1500):
        court_a = []
        court_b = []
        
        grades = ["4年", "3年", "2年", "1年"]
        for g in grades:
            g_members = df_sorted[df_sorted["学年"] == g].to_dict('records')
            random.shuffle(g_members)
            
            half = len(g_members) // 2
            if len(g_members) % 2 != 0 and random.choice([True, False]):
                half += 1
                
            court_a.extend(g_members[:half])
            court_b.extend(g_members[half:])
            
        if len(court_a) != target_per_court or len(court_b) != target_per_court:
            continue
            
        df_a = pd.DataFrame(court_a)
        df_b = pd.DataFrame(court_b)
        
        # ① 上位6名判定
        top6_names = set(df_sorted.iloc[:6]["名前"].tolist())
        a_top6_count = len([m for m in df_a["名前"] if m in top6_names])
        if a_top6_count != 3:
            continue
            
        # ② NGペア判定
        names_a = df_a["名前"].tolist()
        names_b = df_b["名前"].tolist()
        
        if p1 and p2:
            if (p1 in names_a and p2 in names_a) or (p1 in names_b and p2 in names_b):
                continue
                
        # ③ 学年ごとの履歴被りスコア判定
        grade_sim_score = get_grade_similarity_score(df_a, history, member_grade_map)
        
        if grade_sim_score < lowest_grade_sim:
            lowest_grade_sim = grade_sim_score
            best_df_a = df_a.sort_values("シングルスランク").reset_index(drop=True)
            best_df_b = df_b.sort_values("シングルスランク").reset_index(drop=True)
            
        if avoid_dup:
            if grade_sim_score < 0.5:
                return best_df_a, best_df_b, grade_sim_score
        else:
            return best_df_a, best_df_b, grade_sim_score

    return best_df_a, best_df_b, lowest_grade_sim

# --- 5. 振り分け実行エリア ---
st.markdown("---")
exec_button = st.button("🎲 2面にチーム分け（シャッフル）", use_container_width=True, type="primary")

if st.button("🗑️ 共有履歴をリセット", use_container_width=True):
    shared_history.clear()
    st.toast("全員で共有している履歴をリセットしました")
    st.rerun()

if exec_button:
    df_clean = edited_df.dropna(subset=["名前"]).copy()
    df_clean = df_clean[df_clean["名前"].str.strip() != ""]
    
    total_count = len(df_clean)
    
    if total_count < 6:
        st.error("上位6人均等配置のため、6名以上メンバーを登録してください。")
    elif total_count % 2 != 0:
        st.error(f"両コートの人数を均等にするため、偶数名で登録してください。（現在の有効人数: {total_count}名）")
    else:
        df_a, df_b, grade_sim = divide_courts(df_clean, ng_pair_choice, shared_history, avoid_duplicates)
        
        if df_a.empty or df_b.empty:
            st.error("指定された条件を満たす組み合わせが見つかりませんでした。設定を見直してください。")
        else:
            names_a = df_a["名前"].tolist()
            names_b = df_b["名前"].tolist()
            
            # 全員共有の共有履歴に追加
            shared_history.append({
                "A_names": names_a,
                "B_names": names_b
            })
            
            st.success(f"✨ 学年ごとの被りを抑えた新構成で振り分けました！（直近の学年平均一致度: {int(grade_sim * 100)}%）")
            
            # --- メイン表（シングルスランク順） ---
            col1, col2 = st.columns(2)
            
            with col1:
                st.success(f"🎾 **Aコート** ({len(df_a)}名)")
                st.dataframe(df_a[["名前", "学年", "シングルスランク"]], use_container_width=True, hide_index=True)
                counts_a = df_a["学年"].value_counts()
                st.caption(f"内訳: 4年:{counts_a.get('4年',0)} / 3年:{counts_a.get('3年',0)} / 2年:{counts_a.get('2年',0)} / 1年:{counts_a.get('1年',0)}")
                
            with col2:
                st.info(f"🎾 **Bコート** ({len(df_b)}名)")
                st.dataframe(df_b[["名前", "学年", "シングルスランク"]], use_container_width=True, hide_index=True)
                counts_b = df_b["学年"].value_counts()
                st.caption(f"内訳: 4年:{counts_b.get('4年',0)} / 3年:{counts_b.get('3年',0)} / 2年:{counts_b.get('2年',0)} / 1年:{counts_b.get('1年',0)}")

            # --- 名前のみ一覧（指定優先順） ---
            st.markdown("---")
            st.subheader("📝 メンバー一覧（指定優先順）")
            st.caption("※ 指定された優先順位（井上・岩田・長瀬...）に並べ替えたテキスト一覧です。")

            sorted_a_names = sort_by_custom_order(names_a)
            sorted_b_names = sort_by_custom_order(names_b)

            col_list1, col_list2 = st.columns(2)
            with col_list1:
                st.markdown("**【Aコート】**")
                st.code("\n".join(sorted_a_names), language=None)

            with col_list2:
                st.markdown("**【Bコート】**")
                st.code("\n".join(sorted_b_names), language=None)

# --- 6. 全員共有の履歴表示エリア ---
if shared_history:
    st.markdown("---")
    with st.expander(f"📜 過去の振り分け履歴［全端末で共有］（全 {len(shared_history)} 回）", expanded=True):
        for idx, item in enumerate(reversed(shared_history)):
            run_num = len(shared_history) - idx
            st.write(f"**第 {run_num} 回の面分け**")
            
            hist_a_sorted = sort_by_custom_order(item['A_names'])
            hist_b_sorted = sort_by_custom_order(item['B_names'])
            
            h_col1, h_col2 = st.columns(2)
            with h_col1:
                st.caption(f"Aコート: {', '.join(hist_a_sorted)}")
            with h_col2:
                st.caption(f"Bコート: {', '.join(hist_b_sorted)}")
            st.divider()
メンバーリストにおけるシングルスランクの余白が気になるので、もう少しなくしたい。

データエディタ（st.data_editor）の幅設定を個別に指定することで、列幅の余白を調整できます。

st.column_config に列幅を指定する width パラメータ（"small", "medium" など）を追加することで、必要以上の余白を削りコンパクトに表示できます。

変更箇所
menwake3.py の --- 2. メンバー管理エリア --- 付近にある edited_df = st.data_editor(...) のコードを以下の記述に置き換えてください。

Python
# --- 2. メンバー管理エリア ---
st.subheader("📋 メンバーリスト（シングルスランク順）")
st.caption("※ 上にある人ほどレベルが高い設定です。表を直接編集して追加・削除・並び替えができます。")

edited_df = st.data_editor(
    st.session_state.members_df,
    num_rows="dynamic",
    use_container_width=True,
    column_config={
        "シングルスランク": st.column_config.NumberColumn(
            "シングルスランク", 
            help="数字が小さいほど上手い", 
            min_value=1,
            width="small"  # ← 列幅をコンパクトに指定して余白を抑えます
        ),
        "名前": st.column_config.TextColumn(
            "名前",
            width="medium"
        ),
        "学年": st.column_config.SelectboxColumn(
            "学年", 
            options=["4年", "3年", "2年", "1年"],
            width="small"
        )
    }
)
ポイント
"シングルスランク" と "学年" の幅を "small" に指定することで、無駄な余白をカットしてすっきり縦ラインが揃うようにしています。

コミット後、1〜2分程度でアプリ画面に自動反映されますので、スマホ画面で余白感が解消されているかご確認ください！

完全なコードを

列幅の調整（width="small"）を反映した、menwake3.py の完全なコード（最新版）です。

以下のコードをすべてコピーして、GitHub上の menwake3.py に上書き（Edit / Commit）してください。

Python
import streamlit as st
import pandas as pd
import random

# --- ページ設定（スマホで見やすい wide レイアウト） ---
st.set_page_config(page_title="テニス面分け", page_icon="🎾", layout="wide")

st.title("🎾 テニス面分け")
st.caption("人数均等配置（学年ごとの被り回避・実力・NGペア条件最適化）")

# --- 1. 全端末で共有するグローバル共有メモリ（履歴データ） ---
@st.cache_resource
def get_shared_history():
    # アプリ全体で共通して保持されるリスト
    return []

shared_history = get_shared_history()

# --- カスタム優先順位の定義 ---
CUSTOM_ORDER = [
    "井上", "岩田", "長瀬", "宮井", "横田", "池田", "植田", "坂本",
    "比嘉", "藤吉", "松下", "池内", "木下", "清水", "髙木", "高木",
    "大平", "尾形", "洪", "小坂", "呉", "野津", "平賀"
]
order_map = {name: i for i, name in enumerate(CUSTOM_ORDER)}

# 初期データ＆セッション状態の管理
if "members_df" not in st.session_state:
    default_data = [
        {"シングルスランク": 1, "名前": "池内", "学年": "2年"},
        {"シングルスランク": 2, "名前": "井上", "学年": "4年"},
        {"シングルスランク": 3, "名前": "植田", "学年": "3年"},
        {"シングルスランク": 4, "名前": "岩田", "学年": "4年"},
        {"シングルスランク": 5, "名前": "松下", "学年": "3年"},
        {"シングルスランク": 6, "名前": "宮井", "学年": "4年"},
        {"シングルスランク": 7, "名前": "横田", "学年": "4年"},
        {"シングルスランク": 8, "名前": "坂本", "学年": "3年"},
        {"シングルスランク": 9, "名前": "比嘉", "学年": "3年"},
        {"シングルスランク": 10, "名前": "清水", "学年": "2年"},
        {"シングルスランク": 11, "名前": "長瀬", "学年": "4年"},
        {"シングルスランク": 12, "名前": "木下", "学年": "2年"},
        {"シングルスランク": 13, "名前": "洪", "学年": "1年"},
        {"シングルスランク": 14, "名前": "藤吉", "学年": "3年"},
        {"シングルスランク": 15, "名前": "池田", "学年": "3年"},
        {"シングルスランク": 16, "名前": "髙木", "学年": "2年"},
        {"シングルスランク": 17, "名前": "尾形", "学年": "1年"},
        {"シングルスランク": 18, "名前": "呉", "学年": "1年"},
        {"シングルスランク": 19, "名前": "野津", "学年": "1年"},
        {"シングルスランク": 20, "名前": "平賀", "学年": "1年"},
        {"シングルスランク": 21, "名前": "小坂", "学年": "1年"},
        {"シングルスランク": 22, "名前": "大平", "学年": "1年"}
    ]
    st.session_state.members_df = pd.DataFrame(default_data)

def sort_by_custom_order(names_list):
    return sorted(names_list, key=lambda x: order_map.get(x, 999))

# --- 2. メンバー管理エリア（列幅最適化） ---
st.subheader("📋 メンバーリスト（シングルスランク順）")
st.caption("※ 上にある人ほどレベルが高い設定です。表を直接編集して追加・削除・並び替えができます。")

edited_df = st.data_editor(
    st.session_state.members_df,
    num_rows="dynamic",
    use_container_width=True,
    column_config={
        "シングルスランク": st.column_config.NumberColumn(
            "シングルスランク", 
            help="数字が小さいほど上手い", 
            min_value=1,
            width="small"
        ),
        "名前": st.column_config.TextColumn(
            "名前",
            width="medium"
        ),
        "学年": st.column_config.SelectboxColumn(
            "学年", 
            options=["4年", "3年", "2年", "1年"],
            width="small"
        )
    }
)

st.session_state.members_df = edited_df

# --- 3. 分けるペアの設定＆オプションエリア ---
st.markdown("---")
st.subheader("⚡ 条件設定")

# 各選択肢を強制的に1行ずつ（改行）独立して表示させるCSSスタイル設定
st.markdown("""
    <style>
    div[data-testid="stRadio"] > label {
        display: block !important;
        margin-bottom: 8px !important;
    }
    div[data-testid="stRadio"] div[role="radiogroup"] > label {
        display: flex !important;
        margin-bottom: 6px !important;
        width: 100% !important;
    }
    </style>
""", unsafe_allow_html=True)

# NGペアの選択肢（CSSで確実に1行ずつ改行）
ng_pair_choice = st.radio(
    "必ず別々のコートにするペアを選択してください",
    options=[
        "指定なし",
        "（池田、比嘉）を別々にする",
        "（坂本、藤吉）を別々にする"
    ],
    index=0
)

avoid_duplicates = st.checkbox("🔄 過去の振り分けと学年ごとの被りを最小化する", value=True)

# 学年別重複率の計算関数
def get_grade_similarity_score(df_a, history, member_grade_map):
    if not history:
        return 0.0
    
    max_score = 0.0
    grades = ["4年", "3年", "2年", "1年"]
    a_names = set(df_a["名前"].tolist())
    
    for past in history[-3:]:
        past_a_names = set(past["A_names"])
        past_b_names = set(past["B_names"])
        
        for past_set in [past_a_names, past_b_names]:
            grade_sims = []
            for g in grades:
                curr_g_members = set([m for m in a_names if member_grade_map.get(m) == g])
                past_g_members = set([m for m in past_set if member_grade_map.get(m) == g])
                
                if curr_g_members:
                    overlap = len(curr_g_members.intersection(past_g_members)) / len(curr_g_members)
                    grade_sims.append(overlap)
            
            if grade_sims:
                avg_sim = sum(grade_sims) / len(grade_sims)
                max_score = max(max_score, avg_sim)
                
    return max_score

# --- 4. 被り自動回避付き面分けロジック ---
def divide_courts(df, ng_choice, history, avoid_dup):
    df_sorted = df.sort_values("シングルスランク").reset_index(drop=True)
    target_per_court = len(df_sorted) // 2
    
    member_grade_map = dict(zip(df_sorted["名前"], df_sorted["学年"]))
    
    # NGペアの割り出し
    p1, p2 = None, None
    if ng_choice == "（池田、比嘉）を別々にする":
        p1, p2 = "池田", "比嘉"
    elif ng_choice == "（坂本、藤吉）を別々にする":
        p1, p2 = "坂本", "藤吉"
        
    best_df_a = pd.DataFrame()
    best_df_b = pd.DataFrame()
    lowest_grade_sim = 1.0
    
    for _ in range(1500):
        court_a = []
        court_b = []
        
        grades = ["4年", "3年", "2年", "1年"]
        for g in grades:
            g_members = df_sorted[df_sorted["学年"] == g].to_dict('records')
            random.shuffle(g_members)
            
            half = len(g_members) // 2
            if len(g_members) % 2 != 0 and random.choice([True, False]):
                half += 1
                
            court_a.extend(g_members[:half])
            court_b.extend(g_members[half:])
            
        if len(court_a) != target_per_court or len(court_b) != target_per_court:
            continue
            
        df_a = pd.DataFrame(court_a)
        df_b = pd.DataFrame(court_b)
        
        # ① 上位6名判定
        top6_names = set(df_sorted.iloc[:6]["名前"].tolist())
        a_top6_count = len([m for m in df_a["名前"] if m in top6_names])
        if a_top6_count != 3:
            continue
            
        # ② NGペア判定
        names_a = df_a["名前"].tolist()
        names_b = df_b["名前"].tolist()
        
        if p1 and p2:
            if (p1 in names_a and p2 in names_a) or (p1 in names_b and p2 in names_b):
                continue
                
        # ③ 学年ごとの履歴被りスコア判定
        grade_sim_score = get_grade_similarity_score(df_a, history, member_grade_map)
        
        if grade_sim_score < lowest_grade_sim:
            lowest_grade_sim = grade_sim_score
            best_df_a = df_a.sort_values("シングルスランク").reset_index(drop=True)
            best_df_b = df_b.sort_values("シングルスランク").reset_index(drop=True)
            
        if avoid_dup:
            if grade_sim_score < 0.5:
                return best_df_a, best_df_b, grade_sim_score
        else:
            return best_df_a, best_df_b, grade_sim_score

    return best_df_a, best_df_b, lowest_grade_sim

# --- 5. 振り分け実行エリア ---
st.markdown("---")
exec_button = st.button("🎲 2面にチーム分け（シャッフル）", use_container_width=True, type="primary")

if st.button("🗑️ 共有履歴をリセット", use_container_width=True):
    shared_history.clear()
    st.toast("全員で共有している履歴をリセットしました")
    st.rerun()

if exec_button:
    df_clean = edited_df.dropna(subset=["名前"]).copy()
    df_clean = df_clean[df_clean["名前"].str.strip() != ""]
    
    total_count = len(df_clean)
    
    if total_count < 6:
        st.error("上位6人均等配置のため、6名以上メンバーを登録してください。")
    elif total_count % 2 != 0:
        st.error(f"両コートの人数を均等にするため、偶数名で登録してください。（現在の有効人数: {total_count}名）")
    else:
        df_a, df_b, grade_sim = divide_courts(df_clean, ng_pair_choice, shared_history, avoid_duplicates)
        
        if df_a.empty or df_b.empty:
            st.error("指定された条件を満たす組み合わせが見つかりませんでした。設定を見直してください。")
        else:
            names_a = df_a["名前"].tolist()
            names_b = df_b["名前"].tolist()
            
            # 全員共有の共有履歴に追加
            shared_history.append({
                "A_names": names_a,
                "B_names": names_b
            })
            
            st.success(f"✨ 学年ごとの被りを抑えた新構成で振り分けました！（直近の学年平均一致度: {int(grade_sim * 100)}%）")
            
            # --- メイン表（シングルスランク順） ---
            col1, col2 = st.columns(2)
            
            with col1:
                st.success(f"🎾 **Aコート** ({len(df_a)}名)")
                st.dataframe(df_a[["名前", "学年", "シングルスランク"]], use_container_width=True, hide_index=True)
                counts_a = df_a["学年"].value_counts()
                st.caption(f"内訳: 4年:{counts_a.get('4年',0)} / 3年:{counts_a.get('3年',0)} / 2年:{counts_a.get('2年',0)} / 1年:{counts_a.get('1年',0)}")
                
            with col2:
                st.info(f"🎾 **Bコート** ({len(df_b)}名)")
                st.dataframe(df_b[["名前", "学年", "シングルスランク"]], use_container_width=True, hide_index=True)
                counts_b = df_b["学年"].value_counts()
                st.caption(f"内訳: 4年:{counts_b.get('4年',0)} / 3年:{counts_b.get('3年',0)} / 2年:{counts_b.get('2年',0)} / 1年:{counts_b.get('1年',0)}")

            # --- 名前のみ一覧（指定優先順） ---
            st.markdown("---")
            st.subheader("📝 メンバー一覧（指定優先順）")
            st.caption("※ 指定された優先順位（井上・岩田・長瀬...）に並べ替えたテキスト一覧です。")

            sorted_a_names = sort_by_custom_order(names_a)
            sorted_b_names = sort_by_custom_order(names_b)

            col_list1, col_list2 = st.columns(2)
            with col_list1:
                st.markdown("**【Aコート】**")
                st.code("\n".join(sorted_a_names), language=None)

            with col_list2:
                st.markdown("**【Bコート】**")
                st.code("\n".join(sorted_b_names), language=None)

# --- 6. 全員共有の履歴表示エリア ---
if shared_history:
    st.markdown("---")
    with st.expander(f"📜 過去の振り分け履歴［全端末で共有］（全 {len(shared_history)} 回）", expanded=True):
        for idx, item in enumerate(reversed(shared_history)):
            run_num = len(shared_history) - idx
            st.write(f"**第 {run_num} 回の面分け**")
            
            hist_a_sorted = sort_by_custom_order(item['A_names'])
            hist_b_sorted = sort_by_custom_order(item['B_names'])
            
            h_col1, h_col2 = st.columns(2)
            with h_col1:
                st.caption(f"Aコート: {', '.join(hist_a_sorted)}")
            with h_col2:
                st.caption(f"Bコート: {', '.join(hist_b_sorted)}")
            st.divider()
学年を日付と連動させたい。１/１に今の学年から自動的に一つ上の学年に上がるようにできる？

1月1日（または年度更新時の4月1日など）に日付を基準として、各メンバーの学年が自動的に1つ上がる仕組みを追加できます！

学年を自動更新するためには、基準となる入学年（または学年が切り替わる年）をコード内で計算するロジックを取り入れます。

実装のポイント
基準年（現在の学年年数）の判定

例えば 2026年1月1日 を迎えると、1年 -> 2年、2年 -> 3年、3年 -> 4年、4年 -> 卒業（またはそのまま最高学年維持）のように自動シフトします。

日付取得（datetime）の追加

Pythonの datetime ライブラリを使用して、本日日付から現在の年度・学年をリアルタイム計算します。

学年更新のルール指定について
コードを書き換える前に、4年生（最高学年）の扱いについてどうするか教えていただけますか？

パターンA: 1月1日になったら 1年→2年、2年→3年、3年→4年 に上がり、4年はそのまま4年にとどまる（または卒業扱いとして自動削除）

パターンB: 4月1日（一般的な学年更新タイミング）で上がるようにする

どちらの動きがご希望に近いか教えていただければ、コードを完成させてお渡しします！

コードに追加できる？

1月1日（または指定した日付）に自動で学年が1つ上がる計算ロジックを追加した、menwake3.py の完全な最新コードです！

自動更新の仕組み
基準年（2025年時点）の学年データをもとに、現在の年（datetime.now().year）と自動比較します。

1月1日を迎えるたびに自動で 1年→2年、2年→3年、3年→4年 へと繰り上がります。

4年生は自動更新後も最高学年の「4年」として維持されます。

完全なコード (menwake3.py)
以下のコードをすべてコピーして、GitHub上の menwake3.py に上書き（Edit / Commit）してください。

Python
import streamlit as st
import pandas as pd
import random
from datetime import datetime

# --- ページ設定（スマホで見やすい wide レイアウト） ---
st.set_page_config(page_title="テニス面分け", page_icon="🎾", layout="wide")

st.title("🎾 テニス面分け")
st.caption("人数均等配置（学年ごとの被り回避・実力・NGペア条件最適化）")

# --- 1. 全端末で共有するグローバル共有メモリ（履歴データ） ---
@st.cache_resource
def get_shared_history():
    return []

shared_history = get_shared_history()

# --- カスタム優先順位の定義 ---
CUSTOM_ORDER = [
    "井上", "岩田", "長瀬", "宮井", "横田", "池田", "植田", "坂本",
    "比嘉", "藤吉", "松下", "池内", "木下", "清水", "髙木", "高木",
    "大平", "尾形", "洪", "小坂", "呉", "野津", "平賀"
]
order_map = {name: i for i, name in enumerate(CUSTOM_ORDER)}

# --- 日付連動：学年自動繰り上げ計算関数 ---
# 2025年時点の基本学年データを定義し、1月1日を過ぎるごとに自動で1年プラス
BASE_YEAR = 2025

def calculate_current_grade(base_grade_num):
    current_year = datetime.now().year
    years_passed = current_year - BASE_YEAR
    new_grade_num = base_grade_num + years_passed
    
    # 4年以上は4年（最高学年）で固定
    if new_grade_num >= 4:
        return "4年"
    else:
        return f"{new_grade_num}年"

# 初期データ＆セッション状態の管理
if "members_df" not in st.session_state:
    # 2025年時点での各メンバーの学年数値 (1〜4)
    raw_default_data = [
        {"シングルスランク": 1, "名前": "池内", "base_grade": 2},
        {"シングルスランク": 2, "名前": "井上", "base_grade": 4},
        {"シングルスランク": 3, "名前": "植田", "base_grade": 3},
        {"シングルスランク": 4, "名前": "岩田", "base_grade": 4},
        {"シングルスランク": 5, "名前": "松下", "base_grade": 3},
        {"シングルスランク": 6, "名前": "宮井", "base_grade": 4},
        {"シングルスランク": 7, "名前": "横田", "base_grade": 4},
        {"シングルスランク": 8, "名前": "坂本", "base_grade": 3},
        {"シングルスランク": 9, "名前": "比嘉", "base_grade": 3},
        {"シングルスランク": 10, "名前": "清水", "base_grade": 2},
        {"シングルスランク": 11, "名前": "長瀬", "base_grade": 4},
        {"シングルスランク": 12, "名前": "木下", "base_grade": 2},
        {"シングルスランク": 13, "名前": "洪", "base_grade": 1},
        {"シングルスランク": 14, "名前": "藤吉", "base_grade": 3},
        {"シングルスランク": 15, "名前": "池田", "base_grade": 3},
        {"シングルスランク": 16, "名前": "髙木", "base_grade": 2},
        {"シングルスランク": 17, "名前": "尾形", "base_grade": 1},
        {"シングルスランク": 18, "名前": "呉", "base_grade": 1},
        {"シングルスランク": 19, "名前": "野津", "base_grade": 1},
        {"シングルスランク": 20, "名前": "平賀", "base_grade": 1},
        {"シングルスランク": 21, "名前": "小坂", "base_grade": 1},
        {"シングルスランク": 22, "名前": "大平", "base_grade": 1}
    ]
    
    # 今日の日付に基づいて現在の学年を動的にセット
    calculated_data = []
    for item in raw_default_data:
        calculated_data.append({
            "シングルスランク": item["シングルスランク"],
            "名前": item["名前"],
            "学年": calculate_current_grade(item["base_grade"])
        })
        
    st.session_state.members_df = pd.DataFrame(calculated_data)

def sort_by_custom_order(names_list):
    return sorted(names_list, key=lambda x: order_map.get(x, 999))

# --- 2. メンバー管理エリア（列幅最適化） ---
st.subheader("📋 メンバーリスト（シングルスランク順）")
st.caption("※ 毎年1月1日に学年が自動で更新されます。表を直接編集して追加・変更も可能です。")

edited_df = st.data_editor(
    st.session_state.members_df,
    num_rows="dynamic",
    use_container_width=True,
    column_config={
        "シングルスランク": st.column_config.NumberColumn(
            "シングルスランク", 
            help="数字が小さいほど上手い", 
            min_value=1,
            width="small"
        ),
        "名前": st.column_config.TextColumn(
            "名前",
            width="medium"
        ),
        "学年": st.column_config.SelectboxColumn(
            "学年", 
            options=["4年", "3年", "2年", "1年"],
            width="small"
        )
    }
)

st.session_state.members_df = edited_df

# --- 3. 分けるペアの設定＆オプションエリア ---
st.markdown("---")
st.subheader("⚡ 条件設定")

# 各選択肢を強制的に1行ずつ（改行）独立して表示させるCSSスタイル設定
st.markdown("""
    <style>
    div[data-testid="stRadio"] > label {
        display: block !important;
        margin-bottom: 8px !important;
    }
    div[data-testid="stRadio"] div[role="radiogroup"] > label {
        display: flex !important;
        margin-bottom: 6px !important;
        width: 100% !important;
    }
    </style>
""", unsafe_allow_html=True)

# NGペアの選択肢（CSSで確実に1行ずつ改行）
ng_pair_choice = st.radio(
    "必ず別々のコートにするペアを選択してください",
    options=[
        "指定なし",
        "（池田、比嘉）を別々にする",
        "（坂本、藤吉）を別々にする"
    ],
    index=0
)

avoid_duplicates = st.checkbox("🔄 過去の振り分けと学年ごとの被りを最小化する", value=True)

# 学年別重複率の計算関数
def get_grade_similarity_score(df_a, history, member_grade_map):
    if not history:
        return 0.0
    
    max_score = 0.0
    grades = ["4年", "3年", "2年", "1年"]
    a_names = set(df_a["名前"].tolist())
    
    for past in history[-3:]:
        past_a_names = set(past["A_names"])
        past_b_names = set(past["B_names"])
        
        for past_set in [past_a_names, past_b_names]:
            grade_sims = []
            for g in grades:
                curr_g_members = set([m for m in a_names if member_grade_map.get(m) == g])
                past_g_members = set([m for m in past_set if member_grade_map.get(m) == g])
                
                if curr_g_members:
                    overlap = len(curr_g_members.intersection(past_g_members)) / len(curr_g_members)
                    grade_sims.append(overlap)
            
            if grade_sims:
                avg_sim = sum(grade_sims) / len(grade_sims)
                max_score = max(max_score, avg_sim)
                
    return max_score

# --- 4. 被り自動回避付き面分けロジック ---
def divide_courts(df, ng_choice, history, avoid_dup):
    df_sorted = df.sort_values("シングルスランク").reset_index(drop=True)
    target_per_court = len(df_sorted) // 2
    
    member_grade_map = dict(zip(df_sorted["名前"], df_sorted["学年"]))
    
    # NGペアの割り出し
    p1, p2 = None, None
    if ng_choice == "（池田、比嘉）を別々にする":
        p1, p2 = "池田", "比嘉"
    elif ng_choice == "（坂本、藤吉）を別々にする":
        p1, p2 = "坂本", "藤吉"
        
    best_df_a = pd.DataFrame()
    best_df_b = pd.DataFrame()
    lowest_grade_sim = 1.0
    
    for _ in range(1500):
        court_a = []
        court_b = []
        
        grades = ["4年", "3年", "2年", "1年"]
        for g in grades:
            g_members = df_sorted[df_sorted["学年"] == g].to_dict('records')
            random.shuffle(g_members)
            
            half = len(g_members) // 2
            if len(g_members) % 2 != 0 and random.choice([True, False]):
                half += 1
                
            court_a.extend(g_members[:half])
            court_b.extend(g_members[half:])
            
        if len(court_a) != target_per_court or len(court_b) != target_per_court:
            continue
            
        df_a = pd.DataFrame(court_a)
        df_b = pd.DataFrame(court_b)
        
        # ① 上位6名判定
        top6_names = set(df_sorted.iloc[:6]["名前"].tolist())
        a_top6_count = len([m for m in df_a["名前"] if m in top6_names])
        if a_top6_count != 3:
            continue
            
        # ② NGペア判定
        names_a = df_a["名前"].tolist()
        names_b = df_b["名前"].tolist()
        
        if p1 and p2:
            if (p1 in names_a and p2 in names_a) or (p1 in names_b and p2 in names_b):
                continue
                
        # ③ 学年ごとの履歴被りスコア判定
        grade_sim_score = get_grade_similarity_score(df_a, history, member_grade_map)
        
        if grade_sim_score < lowest_grade_sim:
            lowest_grade_sim = grade_sim_score
            best_df_a = df_a.sort_values("シングルスランク").reset_index(drop=True)
            best_df_b = df_b.sort_values("シングルスランク").reset_index(drop=True)
            
        if avoid_dup:
            if grade_sim_score < 0.5:
                return best_df_a, best_df_b, grade_sim_score
        else:
            return best_df_a, best_df_b, grade_sim_score

    return best_df_a, best_df_b, lowest_grade_sim

# --- 5. 振り分け実行エリア ---
st.markdown("---")
exec_button = st.button("🎲 2面にチーム分け（シャッフル）", use_container_width=True, type="primary")

if st.button("🗑️ 共有履歴をリセット", use_container_width=True):
    shared_history.clear()
    st.toast("全員で共有している履歴をリセットしました")
    st.rerun()

if exec_button:
    df_clean = edited_df.dropna(subset=["名前"]).copy()
    df_clean = df_clean[df_clean["名前"].str.strip() != ""]
    
    total_count = len(df_clean)
    
    if total_count < 6:
        st.error("上位6人均等配置のため、6名以上メンバーを登録してください。")
    elif total_count % 2 != 0:
        st.error(f"両コートの人数を均等にするため、偶数名で登録してください。（現在の有効人数: {total_count}名）")
    else:
        df_a, df_b, grade_sim = divide_courts(df_clean, ng_pair_choice, shared_history, avoid_duplicates)
        
        if df_a.empty or df_b.empty:
            st.error("指定された条件を満たす組み合わせが見つかりませんでした。設定を見直してください。")
        else:
            names_a = df_a["名前"].tolist()
            names_b = df_b["名前"].tolist()
            
            # 全員共有の共有履歴に追加
            shared_history.append({
                "A_names": names_a,
                "B_names": names_b
            })
            
            st.success(f"✨ 学年ごとの被りを抑えた新構成で振り分けました！（直近の学年平均一致度: {int(grade_sim * 100)}%）")
            
            # --- メイン表（シングルスランク順） ---
            col1, col2 = st.columns(2)
            
            with col1:
                st.success(f"🎾 **Aコート** ({len(df_a)}名)")
                st.dataframe(df_a[["名前", "学年", "シングルスランク"]], use_container_width=True, hide_index=True)
                counts_a = df_a["学年"].value_counts()
                st.caption(f"内訳: 4年:{counts_a.get('4年',0)} / 3年:{counts_a.get('3年',0)} / 2年:{counts_a.get('2年',0)} / 1年:{counts_a.get('1年',0)}")
                
            with col2:
                st.info(f"🎾 **Bコート** ({len(df_b)}名)")
                st.dataframe(df_b[["名前", "学年", "シングルスランク"]], use_container_width=True, hide_index=True)
                counts_b = df_b["学年"].value_counts()
                st.caption(f"内訳: 4年:{counts_b.get('4年',0)} / 3年:{counts_b.get('3年',0)} / 2年:{counts_b.get('2年',0)} / 1年:{counts_b.get('1年',0)}")

            # --- 名前のみ一覧（指定優先順） ---
            st.markdown("---")
            st.subheader("📝 メンバー一覧（指定優先順）")
            st.caption("※ 指定された優先順位（井上・岩田・長瀬...）に並べ替えたテキスト一覧です。")

            sorted_a_names = sort_by_custom_order(names_a)
            sorted_b_names = sort_by_custom_order(names_b)

            col_list1, col_list2 = st.columns(2)
            with col_list1:
                st.markdown("**【Aコート】**")
                st.code("\n".join(sorted_a_names), language=None)

            with col_list2:
                st.markdown("**【Bコート】**")
                st.code("\n".join(sorted_b_names), language=None)

# --- 6. 全員共有の履歴表示エリア ---
if shared_history:
    st.markdown("---")
    with st.expander(f"📜 過去の振り分け履歴［全端末で共有］（全 {len(shared_history)} 回）", expanded=True):
        for idx, item in enumerate(reversed(shared_history)):
            run_num = len(shared_history) - idx
            st.write(f"**第 {run_num} 回の面分け**")
            
            hist_a_sorted = sort_by_custom_order(item['A_names'])
            hist_b_sorted = sort_by_custom_order(item['B_names'])
            
            h_col1, h_col2 = st.columns(2)
            with h_col1:
                st.caption(f"Aコート: {', '.join(hist_a_sorted)}")
            with h_col2:
                st.caption(f"Bコート: {', '.join(hist_b_sorted)}")
            st.divider()
シングルスランクが変わったときに、書き換えるのではなくて、ボタンを押したら上下できるように変更できる？

Streamlit標準のデータエディタ（st.data_editor）の仕様上、表の中にある数字を直接「▲/▼ボタン」にして上下移動させるのは難しいですが、「並び替え専用のボタン（⬆️ 上へ / ⬇️ 下へ）」をメンバー管理エリアに追加することで、ボタン一つで順位（シングルスランク）を上下に入れ替えられるように改善できます！

実装イメージ
ドロップダウンで対象メンバーを選択

「⬆️ 順位を上げる」「⬇️ 順位を下げる」 ボタンを押す

選択したメンバーと前後のメンバーのシングルスランクが自動的に入れ替わり、リストが更新される

順位変更ボタンを追加した完全なコード (menwake3.py)
以下のコードをすべてコピーして、GitHub上の menwake3.py に上書き（Edit / Commit）してください。

Python
import streamlit as st
import pandas as pd
import random
from datetime import datetime

# --- ページ設定（スマホで見やすい wide レイアウト） ---
st.set_page_config(page_title="テニス面分け", page_icon="🎾", layout="wide")

st.title("🎾 テニス面分け")
st.caption("人数均等配置（学年ごとの被り回避・実力・NGペア条件最適化）")

# --- 1. 全端末で共有するグローバル共有メモリ（履歴データ） ---
@st.cache_resource
def get_shared_history():
    return []

shared_history = get_shared_history()

# --- カスタム優先順位の定義 ---
CUSTOM_ORDER = [
    "井上", "岩田", "長瀬", "宮井", "横田", "池田", "植田", "坂本",
    "比嘉", "藤吉", "松下", "池内", "木下", "清水", "髙木", "高木",
    "大平", "尾形", "洪", "小坂", "呉", "野津", "平賀"
]
order_map = {name: i for i, name in enumerate(CUSTOM_ORDER)}

# --- 日付連動：学年自動繰り上げ計算関数 ---
BASE_YEAR = 2025

def calculate_current_grade(base_grade_num):
    current_year = datetime.now().year
    years_passed = current_year - BASE_YEAR
    new_grade_num = base_grade_num + years_passed
    
    if new_grade_num >= 4:
        return "4年"
    else:
        return f"{new_grade_num}年"

# 初期データ＆セッション状態の管理
if "members_df" not in st.session_state:
    raw_default_data = [
        {"シングルスランク": 1, "名前": "池内", "base_grade": 2},
        {"シングルスランク": 2, "名前": "井上", "base_grade": 4},
        {"シングルスランク": 3, "名前": "植田", "base_grade": 3},
        {"シングルスランク": 4, "名前": "岩田", "base_grade": 4},
        {"シングルスランク": 5, "名前": "松下", "base_grade": 3},
        {"シングルスランク": 6, "名前": "宮井", "base_grade": 4},
        {"シングルスランク": 7, "名前": "横田", "base_grade": 4},
        {"シングルスランク": 8, "名前": "坂本", "base_grade": 3},
        {"シングルスランク": 9, "名前": "比嘉", "base_grade": 3},
        {"シングルスランク": 10, "名前": "清水", "base_grade": 2},
        {"シングルスランク": 11, "名前": "長瀬", "base_grade": 4},
        {"シングルスランク": 12, "名前": "木下", "base_grade": 2},
        {"シングルスランク": 13, "名前": "洪", "base_grade": 1},
        {"シングルスランク": 14, "名前": "藤吉", "base_grade": 3},
        {"シングルスランク": 15, "名前": "池田", "base_grade": 3},
        {"シングルスランク": 16, "名前": "髙木", "base_grade": 2},
        {"シングルスランク": 17, "名前": "尾形", "base_grade": 1},
        {"シングルスランク": 18, "名前": "呉", "base_grade": 1},
        {"シングルスランク": 19, "名前": "野津", "base_grade": 1},
        {"シングルスランク": 20, "名前": "平賀", "base_grade": 1},
        {"シングルスランク": 21, "名前": "小坂", "base_grade": 1},
        {"シングルスランク": 22, "名前": "大平", "base_grade": 1}
    ]
    
    calculated_data = []
    for item in raw_default_data:
        calculated_data.append({
            "シングルスランク": item["シングルスランク"],
            "名前": item["名前"],
            "学年": calculate_current_grade(item["base_grade"])
        })
        
    st.session_state.members_df = pd.DataFrame(calculated_data)

def sort_by_custom_order(names_list):
    return sorted(names_list, key=lambda x: order_map.get(x, 999))

# --- 2. メンバー管理エリア ---
st.subheader("📋 メンバーリスト（シングルスランク順）")

# --- ボタンによるランク上下移動コントロール ---
with st.expander("↕️ メンバーの順位（ランク）をボタンで変更する", expanded=True):
    col_sel, col_up, col_down = st.columns([2, 1, 1])
    
    # ランク順にソートした名前リスト
    current_df = st.session_state.members_df.sort_values("シングルスランク").reset_index(drop=True)
    member_names = current_df["名前"].tolist()
    
    with col_sel:
        target_member = st.selectbox("順位を変更したいメンバーを選択", options=member_names)
        
    idx = member_names.index(target_member)
    
    with col_up:
        st.write("") # 高さ調整用
        if st.button("⬆️ 順位を上げる", use_container_width=True, disabled=(idx == 0)):
            # 1つ上のメンバーとランクを入れ替え
            current_df.loc[idx, "シングルスランク"], current_df.loc[idx-1, "シングルスランク"] = \
                current_df.loc[idx-1, "シングルスランク"], current_df.loc[idx, "シングルスランク"]
            st.session_state.members_df = current_df.sort_values("シングルスランク").reset_index(drop=True)
            st.rerun()
            
    with col_down:
        st.write("") # 高さ調整用
        if st.button("⬇️ 順位を下げる", use_container_width=True, disabled=(idx == len(member_names) - 1)):
            # 1つ下のメンバーとランクを入れ替え
            current_df.loc[idx, "シングルスランク"], current_df.loc[idx+1, "シングルスランク"] = \
                current_df.loc[idx+1, "シングルスランク"], current_df.loc[idx, "シングルスランク"]
            st.session_state.members_df = current_df.sort_values("シングルスランク").reset_index(drop=True)
            st.rerun()

edited_df = st.data_editor(
    st.session_state.members_df.sort_values("シングルスランク").reset_index(drop=True),
    num_rows="dynamic",
    use_container_width=True,
    column_config={
        "シングルスランク": st.column_config.NumberColumn(
            "シングルスランク", 
            help="数字が小さいほど上手い", 
            min_value=1,
            width="small"
        ),
        "名前": st.column_config.TextColumn(
            "名前",
            width="medium"
        ),
        "学年": st.column_config.SelectboxColumn(
            "学年", 
            options=["4年", "3年", "2年", "1年"],
            width="small"
        )
    }
)

st.session_state.members_df = edited_df

# --- 3. 分けるペアの設定＆オプションエリア ---
st.markdown("---")
st.subheader("⚡ 条件設定")

st.markdown("""
    <style>
    div[data-testid="stRadio"] > label {
        display: block !important;
        margin-bottom: 8px !important;
    }
    div[data-testid="stRadio"] div[role="radiogroup"] > label {
        display: flex !important;
        margin-bottom: 6px !important;
        width: 100% !important;
    }
    </style>
""", unsafe_allow_html=True)

ng_pair_choice = st.radio(
    "必ず別々のコートにするペアを選択してください",
    options=[
        "指定なし",
        "（池田、比嘉）を別々にする",
        "（坂本、藤吉）を別々にする"
    ],
    index=0
)

avoid_duplicates = st.checkbox("🔄 過去の振り分けと学年ごとの被りを最小化する", value=True)

# 学年別重複率の計算関数
def get_grade_similarity_score(df_a, history, member_grade_map):
    if not history:
        return 0.0
    
    max_score = 0.0
    grades = ["4年", "3年", "2年", "1年"]
    a_names = set(df_a["名前"].tolist())
    
    for past in history[-3:]:
        past_a_names = set(past["A_names"])
        past_b_names = set(past["B_names"])
        
        for past_set in [past_a_names, past_b_names]:
            grade_sims = []
            for g in grades:
                curr_g_members = set([m for m in a_names if member_grade_map.get(m) == g])
                past_g_members = set([m for m in past_set if member_grade_map.get(m) == g])
                
                if curr_g_members:
                    overlap = len(curr_g_members.intersection(past_g_members)) / len(curr_g_members)
                    grade_sims.append(overlap)
            
            if grade_sims:
                avg_sim = sum(grade_sims) / len(grade_sims)
                max_score = max(max_score, avg_sim)
                
    return max_score

# --- 4. 被り自動回避付き面分けロジック ---
def divide_courts(df, ng_choice, history, avoid_dup):
    df_sorted = df.sort_values("シングルスランク").reset_index(drop=True)
    target_per_court = len(df_sorted) // 2
    
    member_grade_map = dict(zip(df_sorted["名前"], df_sorted["学年"]))
    
    p1, p2 = None, None
    if ng_choice == "（池田、比嘉）を別々にする":
        p1, p2 = "池田", "比嘉"
    elif ng_choice == "（坂本、藤吉）を別々にする":
        p1, p2 = "坂本", "藤吉"
        
    best_df_a = pd.DataFrame()
    best_df_b = pd.DataFrame()
    lowest_grade_sim = 1.0
    
    for _ in range(1500):
        court_a = []
        court_b = []
        
        grades = ["4年", "3年", "2年", "1年"]
        for g in grades:
            g_members = df_sorted[df_sorted["学年"] == g].to_dict('records')
            random.shuffle(g_members)
            
            half = len(g_members) // 2
            if len(g_members) % 2 != 0 and random.choice([True, False]):
                half += 1
                
            court_a.extend(g_members[:half])
            court_b.extend(g_members[half:])
            
        if len(court_a) != target_per_court or len(court_b) != target_per_court:
            continue
            
        df_a = pd.DataFrame(court_a)
        df_b = pd.DataFrame(court_b)
        
        # ① 上位6名判定
        top6_names = set(df_sorted.iloc[:6]["名前"].tolist())
        a_top6_count = len([m for m in df_a["名前"] if m in top6_names])
        if a_top6_count != 3:
            continue
            
        # ② NGペア判定
        names_a = df_a["名前"].tolist()
        names_b = df_b["名前"].tolist()
        
        if p1 and p2:
            if (p1 in names_a and p2 in names_a) or (p1 in names_b and p2 in names_b):
                continue
                
        # ③ 学年ごとの履歴被りスコア判定
        grade_sim_score = get_grade_similarity_score(df_a, history, member_grade_map)
        
        if grade_sim_score < lowest_grade_sim:
            lowest_grade_sim = grade_sim_score
            best_df_a = df_a.sort_values("シングルスランク").reset_index(drop=True)
            best_df_b = df_b.sort_values("シングルスランク").reset_index(drop=True)
            
        if avoid_dup:
            if grade_sim_score < 0.5:
                return best_df_a, best_df_b, grade_sim_score
        else:
            return best_df_a, best_df_b, grade_sim_score

    return best_df_a, best_df_b, lowest_grade_sim

# --- 5. 振り分け実行エリア ---
st.markdown("---")
exec_button = st.button("🎲 2面にチーム分け（シャッフル）", use_container_width=True, type="primary")

if st.button("🗑️ 共有履歴をリセット", use_container_width=True):
    shared_history.clear()
    st.toast("全員で共有している履歴をリセットしました")
    st.rerun()

if exec_button:
    df_clean = edited_df.dropna(subset=["名前"]).copy()
    df_clean = df_clean[df_clean["名前"].str.strip() != ""]
    
    total_count = len(df_clean)
    
    if total_count < 6:
        st.error("上位6人均等配置のため、6名以上メンバーを登録してください。")
    elif total_count % 2 != 0:
        st.error(f"両コートの人数を均等にするため、偶数名で登録してください。（現在の有効人数: {total_count}名）")
    else:
        df_a, df_b, grade_sim = divide_courts(df_clean, ng_pair_choice, shared_history, avoid_duplicates)
        
        if df_a.empty or df_b.empty:
            st.error("指定された条件を満たす組み合わせが見つかりませんでした。設定を見直してください。")
        else:
            names_a = df_a["名前"].tolist()
            names_b = df_b["名前"].tolist()
            
            shared_history.append({
                "A_names": names_a,
                "B_names": names_b
            })
            
            st.success(f"✨ 学年ごとの被りを抑えた新構成で振り分けました！（直近の学年平均一致度: {int(grade_sim * 100)}%）")
            
            col1, col2 = st.columns(2)
            
            with col1:
                st.success(f"🎾 **Aコート** ({len(df_a)}名)")
                st.dataframe(df_a[["名前", "学年", "シングルスランク"]], use_container_width=True, hide_index=True)
                counts_a = df_a["学年"].value_counts()
                st.caption(f"内訳: 4年:{counts_a.get('4年',0)} / 3年:{counts_a.get('3年',0)} / 2年:{counts_a.get('2年',0)} / 1年:{counts_a.get('1年',0)}")
                
            with col2:
                st.info(f"🎾 **Bコート** ({len(




