import streamlit as st
import pandas as pd
import random
from datetime import datetime

# --- ページ設定（スマホで見やすい wide レイアウト） ---
st.set_page_config(page_title="テニス面分け", page_icon="🎾", layout="wide")

st.title("🎾 テニス面分け")
st.caption("人数均等配置（学年・実力・オーパス所有者・全練習履歴での被り回避最適化）")

# --- 1. 全端末・全曜日で共有するグローバル共有メモリ（履歴データ） ---
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
        {"シングルスランク": 1, "名前": "池内", "base_grade": 2, "オーパス所有": False},
        {"シングルスランク": 2, "名前": "井上", "base_grade": 4, "オーパス所有": False},
        {"シングルスランク": 3, "名前": "植田", "base_grade": 3, "オーパス所有": False},
        {"シングルスランク": 4, "名前": "岩田", "base_grade": 4, "オーパス所有": False},
        {"シングルスランク": 5, "名前": "松下", "base_grade": 3, "オーパス所有": False},
        {"シングルスランク": 6, "名前": "宮井", "base_grade": 4, "オーパス所有": False},
        {"シングルスランク": 7, "名前": "横田", "base_grade": 4, "オーパス所有": False},
        {"シングルスランク": 8, "名前": "坂本", "base_grade": 3, "オーパス所有": False},
        {"シングルスランク": 9, "名前": "比嘉", "base_grade": 3, "オーパス所有": False},
        {"シングルスランク": 10, "名前": "清水", "base_grade": 2, "オーパス所有": False},
        {"シングルスランク": 11, "名前": "長瀬", "base_grade": 4, "オーパス所有": False},
        {"シングルスランク": 12, "名前": "木下", "base_grade": 2, "オーパス所有": False},
        {"シングルスランク": 13, "名前": "洪", "base_grade": 1, "オーパス所有": False},
        {"シングルスランク": 14, "名前": "藤吉", "base_grade": 3, "オーパス所有": False},
        {"シングルスランク": 15, "名前": "池田", "base_grade": 3, "オーパス所有": False},
        {"シングルスランク": 16, "名前": "髙木", "base_grade": 2, "オーパス所有": False},
        {"シングルスランク": 17, "名前": "尾形", "base_grade": 1, "オーパス所有": False},
        {"シングルスランク": 18, "名前": "呉", "base_grade": 1, "オーパス所有": False},
        {"シングルスランク": 19, "名前": "野津", "base_grade": 1, "オーパス所有": False},
        {"シングルスランク": 20, "名前": "平賀", "base_grade": 1, "オーパス所有": False},
        {"シングルスランク": 21, "名前": "小坂", "base_grade": 1, "オーパス所有": False},
        {"シングルスランク": 22, "名前": "大平", "base_grade": 1, "オーパス所有": False}
    ]
    
    calculated_data = []
    for item in raw_default_data:
        calculated_data.append({
            "シングルスランク": item["シングルスランク"],
            "名前": item["名前"],
            "学年": calculate_current_grade(item["base_grade"]),
            "オーパス所有": item["オーパス所有"]
        })
        
    st.session_state.members_df = pd.DataFrame(calculated_data)

def sort_by_custom_order(names_list):
    return sorted(names_list, key=lambda x: order_map.get(x, 999))

# --- 2. メンバー管理エリア ---
st.subheader("📋 メンバーリスト（マスターデータ）")

# --- 欠席者選択エリア（手軽に欠席を指定） ---
all_member_names = st.session_state.members_df.sort_values("シングルスランク")["名前"].tolist()

absent_members = st.multiselect(
    "🏖️ 本日の【欠席者】を選択してください（選択された人は面分けから除外されます）",
    options=all_member_names,
    default=[]
)

# --- ボタンによるランク上下移動コントロール ---
with st.expander("↕️ メンバーの順位（ランク）をボタンで変更する", expanded=False):
    col_sel, col_up, col_down = st.columns([2, 1, 1])
    current_df = st.session_state.members_df.sort_values("シングルスランク").reset_index(drop=True)
    member_names = current_df["名前"].tolist()
    
    with col_sel:
        target_member = st.selectbox("順位を変更したいメンバーを選択", options=member_names)
        
    idx = member_names.index(target_member) if target_member in member_names else 0
    
    with col_up:
        st.write("")
        if st.button("⬆️ 順位を上げる", use_container_width=True, disabled=(idx == 0)):
            current_df.loc[idx, "シングルスランク"], current_df.loc[idx-1, "シングルスランク"] = \
                current_df.loc[idx-1, "シングルスランク"], current_df.loc[idx, "シングルスランク"]
            st.session_state.members_df = current_df.sort_values("シングルスランク").reset_index(drop=True)
            st.rerun()
            
    with col_down:
        st.write("")
        if st.button("⬇️ 順位を下げる", use_container_width=True, disabled=(idx == len(member_names) - 1)):
            current_df.loc[idx, "シングルスランク"], current_df.loc[idx+1, "シングルスランク"] = \
                current_df.loc[idx+1, "シングルスランク"], current_df.loc[idx, "シングルスランク"]
            st.session_state.members_df = current_df.sort_values("シングルスランク").reset_index(drop=True)
            st.rerun()

edited_df = st.data_editor(
    st.session_state.members_df.sort_values("シングルスランク").reset_index(drop=True),
    num_rows="dynamic",
    use_container_width=True,
    column_config={
        "シングルスランク": st.column_config.NumberColumn("シングルスランク", min_value=1, width="small"),
        "名前": st.column_config.TextColumn("名前", width="medium"),
        "学年": st.column_config.SelectboxColumn("学年", options=["4年", "3年", "2年", "1年"], width="small"),
        "オーパス所有": st.column_config.CheckboxColumn("オーパス所有", help="大泉のコート利用カード所有者", width="small")
    }
)

st.session_state.members_df = edited_df

# --- 3. 練習モード＆条件設定エリア ---
st.markdown("---")
st.subheader("⚡ 練習モード＆条件設定")

practice_mode = st.radio(
    "練習の種類を選択してください",
    options=["水曜練（同会場 2コート）", "土曜練（大泉・杉本）"],
    index=0
)

if practice_mode == "土曜練（大泉・杉本）":
    court_name_a = "大泉"
    court_name_b = "杉本"
else:
    court_name_a = "Aコート"
    court_name_b = "Bコート"

st.markdown("""
    <style>
    div[data-testid="stRadio"] > label { display: block !important; margin-bottom: 8px !important; }
    div[data-testid="stRadio"] div[role="radiogroup"] > label { display: flex !important; margin-bottom: 6px !important; width: 100% !important; }
    </style>
""", unsafe_allow_html=True)

ng_pair_choice = st.radio(
    "必ず別々のコートにするペアを選択してください",
    options=["指定なし", "（池田、比嘉）を別々にする", "（坂本、藤吉）を別々にする"],
    index=0
)

avoid_duplicates = st.checkbox("🔄 全練習（水・土）の過去履歴と被りを最小化する", value=True)

# --- スコア計算関数 ---
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

# --- 4. 面分けロジック ---
def divide_courts(df, ng_choice, history, avoid_dup, is_saturday):
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
    
    for _ in range(2500):
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
        
        # ① 上位6名判定（3人ずつ分散）
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
                
        # ③ 土曜練用：大泉（df_a）に必ず1名以上のオーパス所有者を配置
        if is_saturday:
            opus_a_count = df_a["オーパス所有"].sum() if "オーパス所有" in df_a.columns else 0
            if opus_a_count < 1:
                continue
                
        # ④ 全練習履歴に基づく被りスコア計算
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
exec_button = st.button("🎲 チーム分け実行（シャッフル）", use_container_width=True, type="primary")

if st.button("🗑️ 全練習の共有履歴をリセット", use_container_width=True):
    shared_history.clear()
    st.toast("全員で共有しているすべての練習履歴をリセットしました")
    st.rerun()

if exec_button:
    # 欠席者を除外した参加メンバー表を作成
    df_clean = edited_df.dropna(subset=["名前"]).copy()
    df_clean = df_clean[df_clean["名前"].str.strip() != ""]
    df_clean = df_clean[~df_clean["名前"].isin(absent_members)]
    
    total_count = len(df_clean)
    is_sat = practice_mode == "土曜練（大泉・杉本）"
    
    opus_owners_count = df_clean["オーパス所有"].sum() if "オーパス所有" in df_clean.columns else 0
    
    if total_count < 6:
        st.error("上位6人均等配置のため、参加者を6名以上確保してください。")
    elif total_count % 2 != 0:
        st.error(f"両コートの人数を均等にするため、参加者を偶数名にしてください。（現在の参加人数: {total_count}名）")
    elif is_sat and opus_owners_count < 1:
        st.error("土曜練モードでは「大泉」に配置するため、本日の参加メンバーの中にオーパス所有者を1名以上含めてください。")
    else:
        df_a, df_b, grade_sim = divide_courts(df_clean, ng_pair_choice, shared_history, avoid_duplicates, is_sat)
        
        if df_a.empty or df_b.empty:
            st.error("指定された条件（学年・上位均等・オーパス所持・NGペア）を満たす組み合わせが見つかりませんでした。設定を見直してください。")
        else:
            names_a = df_a["名前"].tolist()
            names_b = df_b["名前"].tolist()
            
            shared_history.append({
                "mode": practice_mode,
                "court_a_label": court_name_a,
                "court_b_label": court_name_b,
                "A_names": names_a,
                "B_names": names_b
            })
            
            st.success(f"✨ 全練習（水・土）の履歴を考慮して新構成を作成しました！（本日の参加: {total_count}名 / 学年平均一致度: {int(grade_sim * 100)}%）")
            
            col1, col2 = st.columns(2)
            
            with col1:
                st.success(f"🎾 **{court_name_a}** ({len(df_a)}名)")
                st.dataframe(df_a[["名前", "学年", "シングルスランク", "オーパス所有"]], use_container_width=True, hide_index=True)
                counts_a = df_a["学年"].value_counts()
                st.caption(f"内訳: 4年:{counts_a.get('4年',0)} / 3年:{counts_a.get('3年',0)} / 2年:{counts_a.get('2年',0)} / 1年:{counts_a.get('1年',0)}")
                
            with col2:
                st.info(f"🎾 **{court_name_b}** ({len(df_b)}名)")
                st.dataframe(df_b[["名前", "学年", "シングルスランク", "オーパス所有"]], use_container_width=True, hide_index=True)
                counts_b = df_b["学年"].value_counts()
                st.caption(f"内訳: 4年:{counts_b.get('4年',0)} / 3年:{counts_b.get('3年',0)} / 2年:{counts_b.get('2年',0)} / 1年:{counts_b.get('1年',0)}")

            st.markdown("---")
            st.subheader("📝 メンバー一覧（指定優先順）")
            st.caption("※ 指定された優先順位（井上・岩田・長瀬...）に並べ替えたテキスト一覧です。")

            sorted_a_names = sort_by_custom_order(names_a)
            sorted_b_names = sort_by_custom_order(names_b)

            col_list1, col_list2 = st.columns(2)
            with col_list1:
                st.markdown(f"**【{court_name_a}】**")
                st.code("\n".join(sorted_a_names), language=None)

            with col_list2:
                st.markdown(f"**【{court_name_b}】**")
                st.code("\n".join(sorted_b_names), language=None)

# --- 6. 全員共有の履歴表示エリア ---
if shared_history:
    st.markdown("---")
    with st.expander(f"📜 全練習の累積履歴［全端末で共有］（全 {len(shared_history)} 回）", expanded=True):
        for idx, item in enumerate(reversed(shared_history)):
            run_num = len(shared_history) - idx
            mode_lbl = item.get("mode", "通常練")
            lbl_a = item.get("court_a_label", "Aコート")
            lbl_b = item.get("court_b_label", "Bコート")
            
            st.write(f"**第 {run_num} 回 ({mode_lbl})**")
            
            hist_a_sorted = sort_by_custom_order(item['A_names'])
            hist_b_sorted = sort_by_custom_order(item['B_names'])
            
            h_col1, h_col2 = st.columns(2)
            with h_col1:
                st.caption(f"{lbl_a}: {', '.join(hist_a_sorted)}")
            with h_col2:
                st.caption(f"{lbl_b}: {', '.join(hist_b_sorted)}")
            st.divider()
