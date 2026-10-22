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