import streamlit as st
import pandas as pd

# df = pd.read_csv("https://online-price-watch.consumer.org.hk/opw/opendata/pricewatch_zh-Hant.csv")
# df['stock_name'] = df['品牌'] + ' - ' + df['貨品名稱']
# df['price_discount'] = df['價格'].astype(str) + ' (' + df['優惠'] + ')'
# df["選擇"] = False
# df = df.fillna("-")

df = pd.read_csv("https://online-price-watch.consumer.org.hk/opw/opendata/pricewatch_zh-Hant.csv")
df['stock_name'] = df['品牌'] + ' - ' + df['貨品名稱']
df_na = df[df['優惠'].isna()]
df_na['price_discount'] = df_na['價格'].astype(str)
df_not_na = df[~(df['優惠'].isna())]
df_not_na['price_discount'] = df_not_na['價格'].astype(str) + ' (' + df_not_na['優惠'] + ')'
df = pd.concat([df_na, df_not_na], ignore_index = False)
df["選擇"] = False
df['超市代號'] = df['超市代號'].apply(lambda x: x.title())
df = df.fillna("-")

# --------------------------------------------------------------------------------------------------------------------------------------

# 初始化
if "cart" not in st.session_state:
    st.session_state.cart = set()

if "page" not in st.session_state:
    st.session_state.page = "shop"

if 'shop_list_deafult' not in st.session_state:
    st.session_state.shop_list_deafult = ['Parknshop', 'Wellcome']

if 'cat1_deafult' not in st.session_state:
    st.session_state.cat1_deafult = 0

if 'cat2_deafult' not in st.session_state:
    st.session_state.cat2_deafult = 0

if 'cat1_deafult_text' not in st.session_state:
    st.session_state.cat1_deafult_text = ""

if 'cat2_deafult_text' not in st.session_state:
    st.session_state.cat2_deafult_text = ""

# --------------------------------------------------------------------------------------------------------------------------------------

st.markdown('''<style>
            .block-container { padding-top: 3rem; padding-bottom: 0rem; padding-left: 5rem; padding-right: 5rem; }
            [data-testid="stSidebar"] { min-width: 400px; max-width: 400px; }
            [data-testid="stSidebarUserContent"] { padding-top: 0rem; }
            [data-testid="stSidebarCollapseButton"] { display: none !important; }
            [data-testid="stTable"] th { text-align: center !important; } 
            [data-testid="stDataFrame"] td { text-align: center !important; }
            div[data-testid="stTextInput"] label p { font-size: 18px !important;}
            div.st-key-clear_button button { background-color: #910101 !important; color: white !important; border: none; }
            div.st-key-clear_button button:hover { background-color: #b80202 !important; color: white !important; }
            div.st-key-clear_button_2 button { background-color: #910101 !important; color: white !important; border: none; }
            div.st-key-clear_button_2 button:hover { background-color: #b80202 !important; color: white !important; }
            div.st-key-save_button button { background-color: #015701 !important; color: white !important; border: none; }
            div.st-key-save_button button:hover { background-color: #018001 !important; color: white !important; }
            </style>
            '''
            , unsafe_allow_html=True)

st.set_page_config(layout="wide")

# --------------------------------------------------------------------------------------------------------------------------------------

def update_cart(pivot_df):

    state = st.session_state["my_editor"]

    for row_idx, changes in state["edited_rows"].items():
        if "選擇" in changes:
            item_name = pivot_df.iloc[row_idx]["stock_name"]
            
            if changes["選擇"]:
                st.session_state.cart.add(item_name)
            else:
                st.session_state.cart.discard(item_name)

# --------------------------------------------------------------------------------------------------------------------------------------

def estimate_width(series):
    max_len = series.astype(str).map(len).max()
    return int(min(400, max(120, max_len * 14)))

def clear_text():
    st.session_state.search_word = ""

@st.fragment
def show_editor(pivot_df):
    edited_df = st.data_editor(pivot_df, 
                                column_order=tuple(['選擇'] + original_columns),
                                width = "content",
                                height=min(int(len(pivot_df) * 37.5 + 40), 720),
                                column_config=column_config_dict,
                                hide_index=True,
                                key="my_editor",
                                on_change=update_cart,
                                args=(pivot_df,),
                                num_rows="fixed"
                                )

# --------------------------------------------------------------------------------------------------------------------------------------

if 'selected_stock_names' not in st.session_state:
    st.session_state.selected_stock_names = set()

if "search_word" not in st.session_state:
    st.session_state.search_word = ""

# ================================================================================================================================================

if st.session_state.page == "shop":

    # Side Bar

    if 'is_cat2_expanded' not in st.session_state:
        st.session_state['is_cat2_expanded'] = False
    else:
        st.session_state['is_cat2_expanded'] = True

    st.sidebar.header("📂 貨品分類搜尋")

    try:
        shop_list = ["全部"] + list(df['超市代號'].unique())
        # with st.sidebar.expander(f"超市：{st.session_state.get('shop', '全部')}"):
        selected_shop = st.sidebar.multiselect("選擇超市", shop_list, key="shop", default = st.session_state.shop_list_deafult)
        st.session_state.shop_list_deafult = selected_shop

        df_shop = df[df['超市代號'].isin(selected_shop)] if "全部" not in selected_shop else df

        cat1_list = ["全部"] + list(df_shop['貨品分類1'].unique())
        cat1_display_text = cat1_list[st.session_state.cat1_deafult]

        with st.sidebar.expander(f"主分類：{st.session_state.get('cat1', cat1_display_text)}"):
            selected_cat1 = st.radio("選擇主分類", cat1_list, key="cat1", index = st.session_state.cat1_deafult)
            st.session_state.cat1_deafult = cat1_list.index(selected_cat1)
            st.session_state.cat1_deafult_text = selected_cat1

        df_cat1 = df_shop[df_shop['貨品分類1'] == selected_cat1] if selected_cat1 != "全部" else df_shop

        cat2_list = ["全部"] + list(df_cat1['貨品分類2'].unique())

        if st.session_state.cat2_deafult_text not in cat2_list:
            st.session_state.cat2_deafult = 0

            with st.sidebar.expander(f"次分類：全部", expanded=st.session_state.get('is_cat2_expanded', False)): 
                selected_cat2 = st.radio("選擇次分類", cat2_list, key="cat2", index = st.session_state.cat2_deafult)
                st.session_state.cat2_deafult = cat2_list.index(selected_cat2)
                st.session_state.cat2_deafult_text = selected_cat2
        
        else:
            with st.sidebar.expander(f"次分類：{st.session_state.get('cat2', cat2_list[st.session_state.cat2_deafult])}", expanded=st.session_state.get('is_cat2_expanded', False)): 
                selected_cat2 = st.radio("選擇次分類", cat2_list, key="cat2", index = st.session_state.cat2_deafult)
                st.session_state.cat2_deafult = cat2_list.index(selected_cat2)
                st.session_state.cat2_deafult_text = selected_cat2


        filtered_df = df_cat1.copy()
        if selected_cat2 != "全部":
            filtered_df = filtered_df[filtered_df['貨品分類2'] == selected_cat2]
    
    except:
        st.write(f"請選擇超市")


    # ---------------------------------------------------------------------------------------------------------------------------------------

    # Display Table
    if not filtered_df.empty:

        # Search Bar and button
        col1, col2 = st.columns([10, 1.55], gap="small") # 調整比例讓按鈕在右側
        with col1:
            search_term = st.text_input("🔍 搜尋商品名稱", placeholder="輸入名稱...", key="search_word")
        with col2:
            sub_col1, sub_col2 = st.columns([1, 2], gap = 'small')
            with sub_col1:
                st.markdown('<p style="margin-top:34px;"></p>', unsafe_allow_html=True)
                submitted = st.button("搜尋")
            with sub_col2:
                st.markdown('<p style="margin-top:34px;"></p>', unsafe_allow_html=True)
                clear = st.button("🧹 清除搜尋", key="clear_button_2", on_click=clear_text)

        

        col1, col2, col3 = st.columns([1.1, 1, 7.9], vertical_alignment="bottom", gap = "small")
        with col1:
            st.markdown("#### 📊 價格比較")

        with col2:
            st.html(""" <style> div[data-testid="stButton"] button { padding-top: 0px; padding-bottom: 0px; height: 32px;min-height: 32px; } </style> """)
            if st.button("Save", key = "save_button"):
                pass
    
        st.write(f"當前分類：{' & '.join(selected_shop)} > {selected_cat1} > {selected_cat2}")

    # --------------------------------------------------------------------------------------------------------------------------------------

        if not filtered_df.empty:

            pivot_df = filtered_df.pivot_table(index=['stock_name', '選擇'], 
                                                # index = ['品牌', '貨品名稱'],
                                            columns='超市代號', 
                                            values='price_discount', 
                                            aggfunc='first',
                                            fill_value='-'
                                            ).reset_index()


            # Action when Pressing Enter
            if submitted or search_term:
                pivot_df = pivot_df[pivot_df['stock_name'].str.contains(search_term, case=False, na=False)]

            column_config_dict = {col: st.column_config.Column(width=estimate_width(pivot_df[col]), disabled=True) for col in pivot_df.columns}
            column_config_dict["選擇"] = st.column_config.CheckboxColumn("Selected",help="勾選欲購買的商品",default=False)
            
            original_columns = [x for x in pivot_df.columns if x != '選擇']
            pivot_df['選擇'] = pivot_df['stock_name'].apply( lambda x: x in st.session_state.cart )

            pivot_df = pivot_df[pivot_df.any(axis=1)] 

            show_editor(pivot_df)
            
    # ----------------------------------------------------------------------------------------------------------------------------------------

        st.sidebar.title("🛒 Bookmark")
        if st.session_state.cart:

            st.sidebar.write(f"- 已選擇{len(st.session_state.cart)}件貨品")

            col1, col2 = st.sidebar.columns([4,6])

            with col1:
                sub_col1, sub_col2 = st.columns([1, 1], gap = 'small')
                with sub_col1:
                    button_1 = st.button("比較", use_container_width=True)
                    if button_1:
                        st.session_state.page = "checkout"
                        st.rerun()

                with sub_col2:
            # with col2:
                    button_2 = st.button("清除", key="clear_button", use_container_width=True)
                    if button_2:
                        st.session_state.cart = set()
                        st.rerun()

        else:
            st.sidebar.write("- Bookmark是空的")


        # # if st.session_state.selected_stock_names:
        # st.sidebar.subheader("🛒 購物車明細")
        # for name in st.session_state.selected_stock_names:
        #     st.sidebar.write(f"- {name}")
            
            # if st.sidebar.button("清空購物車"):
            #     st.session_state.selected_stock_names.clear()
            #     st.rerun()

    # ----------------------------------------------------------------------------------------------------------------------------------------

    else:
        st.warning("請選擇超市")

# ================================================================================================================================================

if st.session_state.page == "checkout":

    st.sidebar.title("🛒 我的購物車")
    if st.session_state.cart:

        st.sidebar.write(f"- 已選擇{len(st.session_state.cart)}件貨品")
    else:
        st.sidebar.write("- 購物車是空的")

    if st.sidebar.button("返回"):
        st.session_state.page = "shop"
        st.rerun()


    filtered_df = df.copy()

    filtered_df = filtered_df[filtered_df['stock_name'].isin(st.session_state.cart)]

    pivot_df = filtered_df.pivot_table(index=['stock_name', '選擇'], 
                                        # index = ['品牌', '貨品名稱'],
                                        columns='超市代號', 
                                        values='price_discount', 
                                        aggfunc='first',
                                        fill_value='-'
                                        ).reset_index()

    column_config_dict = {col: st.column_config.Column(width=estimate_width(pivot_df[col]), disabled=True) for col in pivot_df.columns}
    column_config_dict["選擇"] = st.column_config.CheckboxColumn("Selected",help="勾選欲購買的商品",default=False)
    
    try:
        if '全部' not in st.session_state.shop_list_deafult:
            original_columns = [x for x in pivot_df.columns if x != '選擇']
            original_columns = [x for x in original_columns if x != 'stock_name']
            original_columns = [x for x in original_columns if x not in st.session_state.shop_list_deafult]
            pivot_columns = ['選擇', 'stock_name'] + st.session_state.shop_list_deafult + original_columns
    except:
        original_columns = [x for x in pivot_df.columns if x != '選擇']
        pivot_columns = ['選擇'] + original_columns

    pivot_df['選擇'] = pivot_df['stock_name'].apply( lambda x: x in st.session_state.cart )

    pivot_df = pivot_df[pivot_df.any(axis=1)] 

    st.markdown("### 📊 價格比較")

    edited_df = st.data_editor(pivot_df, 
                                column_order=tuple(pivot_columns),
                                width = "content",
                                height=min(len(pivot_df) * 50 + 10, 700),
                                column_config=column_config_dict,
                                hide_index=True,
                                key="my_editor",
                                on_change=update_cart,
                                args=(pivot_df,),
                                num_rows="fixed"
                                )
