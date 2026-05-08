import streamlit as st
import pandas as pd
import re


def discount_calculation(row):

    discount_df = row['優惠']
    price_df = row['價格']
    
    match_pattern_1 = re.search(r"^((?P<X>\d+(\.\d+)?)\s*折)$", discount_df)
    match_pattern_2 = re.search(r"^(買(?P<qty>\d+(\.\d+)?)\s*件\s*\$(?P<price>\d+(\.\d+)?))$", discount_df)
    match_pattern_3 = re.search(r"^((?P<dash>-))$", discount_df)
    match_pattern_4 = re.search(r"^(\$(?P<price>\d+(?:\.\d+)?)任揀(?P<qty1>\d+(?:\.\d+)?)件\s*/\s*買(?P<qty2>\d+(?:\.\d+)?)件享(?P<discount>\d+(?:\.\d+)?)%折扣)$", discount_df)
    match_pattern_5 = re.search(r"Buy\s+(?P<qty>\d+(?:\.\d+)?)\s+item(?:s)?\s+for\s+\$(?P<price>\d+(?:\.\d+)?)", discount_df)
    match_pattern_6 = re.search(r"^(任揀(?P<qty>\d+(?:\.\d+)?)件)$", discount_df)
    match_pattern_7 = re.search(r"^(買(?P<qty>\d+(?:\.\d+)?)\s*件\s*享\s*(?P<discount>\d+(?:\.\d+)?)\s*%\s*折扣)$", discount_df)
    match_pattern_8 = re.search(r"^(\$(?P<price>\d+(\.\d+)?)任揀(?P<qty>\d+(\.\d+)?)件)$", discount_df)
    match_pattern_9 = re.search(r"^(精選Merries TapesPants買(?P<qty>\d+(?:\.\d+)?)件送(?P<free_qty>\d+(?:\.\d+)?)件)$", discount_df)
    match_pattern_10 = re.search(r"^(精選Baby Products買(?P<buy>\d+(\.\d+)?)件送(?P<gift>\d+(\.\d+)?)件)$", discount_df)
    match_pattern_11 = re.search(r"^(精選好奇天然透氣學習褲(?P<qty>\d+(\.\d+)?)件(?P<discount>\d+(\.\d+)?)折)$", discount_df)
    match_pattern_12 = re.search(r"^(精選口腔護理產品買(?P<qty>\d+(?:\.\d+)?)件(?P<discount>\d+(?:\.\d+)?)折)$", discount_df)
    match_pattern_13 = re.search(r"^(精選Sanitary Products買(?P<buy_qty>\d+(\.\d+)?)\s*件送(?P<gift_qty>\d+(\.\d+)?)\s*件)$", discount_df)
    match_pattern_14 = re.search(r"^(精選女性衛生護理產品買(?P<qty>\d+(\.\d+)?)件(?P<discount>\d+(\.\d+)?)折)$", discount_df)
    match_pattern_15 = re.search(r"^(精選幫寶適尿片拉拉褲買(?P<qty>\d+(?:\.\d+)?)件(?P<discount>\d+(?:\.\d+)?)折)$", discount_df)
    match_pattern_16 = re.search(r"^(精選Haircare Products買(?P<buy_qty>\d+(?:\.\d+)?)\s*件\s*送\s*(?P<free_qty>\d+(?:\.\d+)?)\s*件)$", discount_df)
    match_pattern_17 = re.search(r"^(精選Baby Food Product買(?P<buy_qty>\d+(\.\d+)?)件送(?P<gift_qty>\d+(\.\d+)?)件)$", discount_df)
    match_pattern_18 = re.search(r"^(精選Wyeth\s*SX\s*ULTIMA買(?P<buy_qty>\d+(?:\.\d+)?)件送(?P<gift_qty>\d+(?:\.\d+)?)件)$", discount_df)
    match_pattern_19 = re.search(r"^(精選護膚產品買(?P<qty>\d+(?:\.\d+)?)件(?P<discount>\d+(?:\.\d+)?)折)$", discount_df)
    match_pattern_20 = re.search(r"^(精選嬰兒產品買(?P<qty>\d+(\.\d+)?)\s*件\s*(?P<discount>\d+(\.\d+)?)\s*折)$", discount_df)
    match_pattern_21 = re.search(r"^(精選Skincare Products買(?P<buy_qty>\d+(?:\.\d+)?)件送(?P<gift_qty>\d+(?:\.\d+)?)件)$", discount_df)
    match_pattern_22 = re.search(r"^(精選中藥產品買(?P<qty>\d+(?:\.\d+)?)\s*件\s*(?P<discount>\d+(?:\.\d+)?)\s*折)$", discount_df)
    match_pattern_23 = re.search(r"^(精選西式藥品買(?P<qty>\d+(?:\.\d+)?)件\s*(?P<discount>\d+(?:\.\d+)?)折)$", discount_df)
    match_pattern_24 = re.search(r"^(精選龍角散產品買(?P<qty>\d+(\.\d+)?)件(?P<discount>\d+(\.\d+)?)折)$", discount_df)
    match_pattern_25 = re.search(r"^(精選中式滋補產品買(?P<qty>\d+(\.\d+)?)\s*件\s*(?P<discount>\d+(\.\d+)?)\s*折)$", discount_df)
    match_pattern_26 = re.search(r"^(精選維柏健產品買(?P<qty>\d+(\.\d+)?)件(?P<discount>\d+(\.\d+)?)折)$", discount_df)
    match_pattern_27 = re.search(r"^(精選Biostime\s+Probiotics買(?P<buy_qty>\d+(?:\.\d+)?)件送(?P<gift_qty>\d+(?:\.\d+)?)件)$", discount_df)
    match_pattern_28 = re.search(r"^(精選BM\s*Probiotics買(?P<buy_qty>\d+(?:\.\d+)?)\s*件送(?P<gift_qty>\d+(?:\.\d+)?)\s*件)$", discount_df)
    match_pattern_29 = re.search(r"^(精選Health Product買(?P<buy_qty>\d+(\.\d+)?)\s*件送(?P<gift_qty>\d+(\.\d+)?)\s*件)$", discount_df)
    match_pattern_30 = re.search(r"^(買第二件享(?P<discount>\d+(\.\d+)?)%折扣)$", discount_df)
    match_pattern_31 = re.search(r"^(全線家居防蚊用品買(?P<qty>\d+(\.\d+)?)件，可享(?P<discount>\d+(\.\d+)?)折優惠。)$", discount_df)
    match_pattern_32 = re.search(r"^(買第(?P<qty>\d+(?:\.\d+)?)件\s*\$(?P<price>\d+(?:\.\d+)?))$", discount_df)
    match_pattern_33 = re.search(r"^(買(?P<qty>\d+(\.\d+)?)\s*件\s*慳\s*\$(?P<price>\d+(\.\d+)?))$", discount_df)
    match_pattern_34 = re.search(r"^(Buy\s+(?P<amount>\d+(?:\.\d+)?)\s+to\s+save\s+\$(?P<save>\d+(?:\.\d+)?))$", discount_df)
    match_pattern_35 = re.search(r"^(買(?P<qty>\d+(\.\d+)?)\s*件\s*送\s*(?P<gift>\d+(\.\d+)?)\s*件)$", discount_df)
    match_pattern_36 = re.search(r"^(買(?P<buy>\d+(?:\.\d+)?)\s*送(?P<gift>\d+(?:\.\d+)?))$", discount_df)
    match_pattern_37 = re.search(r"^(買(?P<buy_qty>\d+(?:\.\d+)?)送(?P<gift_qty>\d+(?:\.\d+)?).*?請輸入(?P<input_qty>\d+(?:\.\d+)?)件.*?送價低者.*?Neutrogena 深層保濕面膜\s*(?P<pack_qty>\d+(?:\.\d+)?)片裝)$", discount_df)
    match_pattern_38 = re.search(r"^(第(?P<index>\d+(\.\d+)?)件半價)$", discount_df)
    match_pattern_39 = re.search(r"^(買(?P<qty>\d+(?:\.\d+)?)\s*件只需\$(?P<price>\d+(?:\.\d+)?))$", discount_df)
    match_pattern_40 = re.search(r"^(第二件(?P<discount>\d+(\.\d+)?)%\s*折扣)$", discount_df)
    match_pattern_41 = re.search(r"^(買(?P<qty>\d+(?:\.\d+)?)件或以上(?P<discount>\d+(?:\.\d+)?)折)$", discount_df)
    match_pattern_42 = re.search(r"^(買(?P<qty>\d+(?:\.\d+)?)\s*送\s*(?P<gift>\d+(?:\.\d+)?))$", discount_df)
    match_pattern_43 = re.search(r"^(?:任選|任揀)?\s*(?P<total>\d+)\s*件\s*.*?(?:其中)?\s*(?P<free>\d+)\s*件\s*(?:免費|送|贈).*?$", discount_df)
                    
    if match_pattern_2:
        temp = match_pattern_2
        text_quantity = temp.group('qty')
        text_price = temp.group('price')
        text = f'${text_price}/{text_quantity}件'
    
    elif match_pattern_4:
        temp = match_pattern_4
        text_price = temp.group('price')
        text_quantity_1 = temp.group('qty1')
        text_quantity_2 = temp.group('qty2')
        text_discount = str(float('0.' + str(100 - int(temp.group('discount'))))*100).replace('0', '').replace('.', '')
        text = f'${text_price}/{text_quantity_1}件 或 {text_quantity_2}件/{text_discount}折'

    elif match_pattern_5:
        temp = match_pattern_5
        text_quantity = temp.group('qty')
        text_price = temp.group('price')
        text = f'${text_price}/{text_quantity}件'
        
    elif match_pattern_7:
        temp = match_pattern_7       
        text_quantity = temp.group('qty')
        text_discount = int((100 - int(temp.group('discount')))/100 * int(text_quantity) * price_df)
        text = f'${text_discount}/{text_quantity}件' 
        
    elif match_pattern_8:
        temp = match_pattern_8     
        text_quantity = temp.group('qty')
        text_price = temp.group('price')
        text = f'${text_price}/{text_quantity}件'
        
    elif match_pattern_9:
        temp = match_pattern_9    
        text_quantity = temp.group('qty')
        text_quantity_free = temp.group('free_qty')
        text_discount = int(price_df * int(text_quantity))
        text_quantity = int(text_quantity) + int(text_quantity_free)
        # text = f'買{text_quantity}送{text_quantity_free}'
        text = f'${text_discount}/{text_quantity}件'
         
    elif match_pattern_10:
        temp = match_pattern_10    
        text_quantity = temp.group('buy')
        text_quantity_free = temp.group('gift')
        text_discount = int(price_df * int(text_quantity))
        text_quantity = int(text_quantity) + int(text_quantity_free)
        # text = f'買{text_quantity}送{text_quantity_free}'
        text = f'${text_discount}/{text_quantity}件'
        
    elif match_pattern_11:
        temp = match_pattern_11    
        text_quantity = temp.group('qty')
        text_discount = int(float('0.' + temp.group('discount')) * price_df * int(text_quantity))
        text = f'${text_discount}/{text_quantity}件'
         
    elif match_pattern_12:
        temp = match_pattern_12   
        text_quantity = temp.group('qty')
        text_discount = int(float('0.' + temp.group('discount')) * price_df * int(text_quantity))
        text = f'${text_discount}/{text_quantity}件'
        
    elif match_pattern_13:
        temp = match_pattern_13   
        text_quantity = temp.group('buy_qty')
        text_quantity_free = temp.group('gift_qty')
        text_discount = int(price_df * int(text_quantity))
        text_quantity = int(text_quantity) + int(text_quantity_free)
        # text = f'買{text_quantity}送{text_quantity_free}'
        text = f'${text_discount}/{text_quantity}件'

    elif match_pattern_14:
        temp = match_pattern_14   
        text_quantity = temp.group('qty')
        text_discount = int(float('0.' + temp.group('discount')) * price_df * int(text_quantity))
        text = f'${text_discount}/{text_quantity}件' 
        
    elif match_pattern_15:
        temp = match_pattern_15   
        text_quantity = temp.group('qty')
        text_discount = int(float('0.' + temp.group('discount')) * price_df * int(text_quantity))
        text = f'${text_discount}/{text_quantity}件'

    elif match_pattern_16:
        temp = match_pattern_16   
        text_quantity = temp.group('buy_qty')
        text_quantity_free = temp.group('free_qty')
        text_discount = int(price_df * int(text_quantity))
        text_quantity = int(text_quantity) + int(text_quantity_free)
        # text = f'買{text_quantity}送{text_quantity_free}'
        text = f'${text_discount}/{text_quantity}件'

    elif match_pattern_17:
        temp = match_pattern_17   
        text_quantity = temp.group('buy_qty')
        text_quantity_free = temp.group('gift_qty')
        text_discount = int(price_df * int(text_quantity))
        text_quantity = int(text_quantity) + int(text_quantity_free)
        # text = f'買{text_quantity}送{text_quantity_free}'
        text = f'${text_discount}/{text_quantity}件'
        
    elif match_pattern_18:
        temp = match_pattern_18   
        text_quantity = temp.group('buy_qty')
        text_quantity_free = temp.group('gift_qty')
        text_discount = int(price_df * int(text_quantity))
        text_quantity = int(text_quantity) + int(text_quantity_free)
        # text = f'買{text_quantity}送{text_quantity_free}'
        text = f'${text_discount}/{text_quantity}件'

    elif match_pattern_19:
        temp = match_pattern_19   
        text_quantity = temp.group('qty')
        text_discount = int(float('0.' + temp.group('discount')) * price_df * int(text_quantity))
        text = f'${text_discount}/{text_quantity}件'
     
    elif match_pattern_20:
        temp = match_pattern_20   
        text_quantity = temp.group('qty')
        text_discount = int(float('0.' + temp.group('discount')) * price_df * int(text_quantity))
        text = f'${text_discount}/{text_quantity}件' 

    elif match_pattern_21:
        temp = match_pattern_21   
        text_quantity = temp.group('buy_qty')
        text_quantity_free = temp.group('gift_qty')
        text_discount = int(price_df * int(text_quantity))
        text_quantity = int(text_quantity) + int(text_quantity_free)
        # text = f'買{text_quantity}送{text_quantity_free}'
        text = f'${text_discount}/{text_quantity}件'

    elif match_pattern_22:
        temp = match_pattern_22  
        text_quantity = temp.group('qty')
        text_discount = int(float('0.' + temp.group('discount')) * price_df * int(text_quantity))
        text = f'${text_discount}/{text_quantity}件'

    elif match_pattern_23:
        temp = match_pattern_23  
        text_quantity = temp.group('qty')
        text_discount = int(float('0.' + temp.group('discount')) * price_df * int(text_quantity))
        text = f'${text_discount}/{text_quantity}件'
        
    elif match_pattern_24:
        temp = match_pattern_24  
        text_quantity = temp.group('qty')
        text_discount = int(float('0.' + temp.group('discount')) * price_df * int(text_quantity))
        text = f'${text_discount}/{text_quantity}件'
        
    elif match_pattern_25:
        temp = match_pattern_25  
        text_quantity = temp.group('qty')
        text_discount = int(float('0.' + temp.group('discount')) * price_df * int(text_quantity))
        text = f'${text_discount}/{text_quantity}件' 
        
    elif match_pattern_26:
        temp = match_pattern_26  
        text_quantity = temp.group('qty')
        text_discount = int(float('0.' + temp.group('discount')) * price_df * int(text_quantity))
        text = f'${text_discount}/{text_quantity}件'   

    elif match_pattern_27:
        temp = match_pattern_27  
        text_quantity = temp.group('buy_qty')
        text_quantity_free = temp.group('gift_qty')
        text_discount = int(price_df * int(text_quantity))
        text_quantity = int(text_quantity) + int(text_quantity_free)
        # text = f'買{text_quantity}送{text_quantity_free}'
        text = f'${text_discount}/{text_quantity}件' 
        
    elif match_pattern_28:
        temp = match_pattern_28  
        text_quantity = temp.group('buy_qty')
        text_quantity_free = temp.group('gift_qty')
        text_discount = int(price_df * int(text_quantity))
        text_quantity = int(text_quantity) + int(text_quantity_free)
        # text = f'買{text_quantity}送{text_quantity_free}'
        text = f'${text_discount}/{text_quantity}件'
        
    elif match_pattern_29:
        temp = match_pattern_29  
        text_quantity = temp.group('buy_qty')
        text_quantity_free = temp.group('gift_qty')
        text_discount = int(price_df * int(text_quantity))
        text_quantity = int(text_quantity) + int(text_quantity_free)
        # text = f'買{text_quantity}送{text_quantity_free}'
        text = f'${text_discount}/{text_quantity}件'
        
    elif match_pattern_30:
        temp = match_pattern_30  
        text_discount = int(float('0.' + temp.group('discount')) * price_df + price_df)
        text = f'${text_discount}/2件'  
        
    elif match_pattern_31:
        temp = match_pattern_31  
        text_quantity = temp.group('qty')
        text_discount = int(float('0.' + temp.group('discount')) * price_df * int(text_quantity))
        text = f'${text_discount}/{text_quantity}件' 
        
    elif match_pattern_32:
        temp = match_pattern_32  
        text_quantity = temp.group('qty')
        text_discount = int(price_df * int(text_quantity) - price_df + int(temp.group('price')))
        text = f'${text_discount}/{text_quantity}件'
        
    elif match_pattern_33:
        temp = match_pattern_33  
        text_quantity = temp.group('qty')
        text_discount = int(price_df * int(text_quantity) - int(float(temp.group('price'))))
        text = f'${text_discount}/{text_quantity}件'   
        
    elif match_pattern_34:
        temp = match_pattern_34  
        text_quantity = temp.group('amount')
        text_discount = int(price_df * int(text_quantity) - int(float(temp.group('save'))))
        text = f'${text_discount}/{text_quantity}件' 
        
    elif match_pattern_35:
        temp = match_pattern_35  
        text_quantity = temp.group('qty')
        text_quantity_free = temp.group('gift')
        text_discount = int(price_df * int(text_quantity))
        text_quantity = int(text_quantity) + int(text_quantity_free)
        # text = f'買{text_quantity}送{text_quantity_free}'
        text = f'${text_discount}/{text_quantity}件'
        
    elif match_pattern_38:
        temp = match_pattern_38  
        text_quantity = temp.group('index')
        text_discount = int(price_df * int(text_quantity) - price_df * 0.5)
        text = f'${text_discount}/{text_quantity}件'    
        
    elif match_pattern_39:
        temp = match_pattern_39  
        text_quantity = temp.group('qty')
        text_price = temp.group('price')
        text = f'${text_price}/{text_quantity}件'
        
    elif match_pattern_40:
        temp = match_pattern_40  
        text_discount = int(float('0.' + temp.group('discount')) * price_df + price_df)
        text = f'${text_discount}/2件'
        
    elif match_pattern_41:
        temp = match_pattern_41
        text_quantity = temp.group('qty')
        text_discount = temp.group('discount')
        text = f'{text_discount}折/{text_quantity}件或以上'     

    elif match_pattern_42:
        temp = match_pattern_42
        text_quantity = temp.group('qty')
        text_quantity_free = temp.group('gift')
        text_discount = int(price_df * int(text_quantity))
        text_quantity = int(text_quantity) + int(text_quantity_free)
        # text = f'買{text_quantity}送{text_quantity_free}'
        text = f'${text_discount}/{text_quantity}件'

    elif match_pattern_42:
        temp = match_pattern_42
        text_quantity = temp.group('total')
        text_quantity_free = temp.group('free')
        text_quantity_price = int(text_quantity) - int(text_quantity_free)
        text_discount = int(price_df * int(text_quantity_price))
        # text = f'買{text_quantity}送{text_quantity_free}'
        text = f'${text_discount}/{text_quantity}件'

    else:
        text = row['優惠']
        
    return text

# df = pd.read_csv("https://online-price-watch.consumer.org.hk/opw/opendata/pricewatch_zh-Hant.csv")
# df['Name'] = df['品牌'] + ' - ' + df['貨品名稱']
# df['price_discount'] = df['價格'].astype(str) + ' (' + df['優惠'] + ')'
# df["選擇"] = False
# df = df.fillna("-")

# --------------------------------------------------------------------------------------------------------------------------------------

@st.cache_data
def load_and_process_data():
    df = pd.read_csv("https://online-price-watch.consumer.org.hk/opw/opendata/pricewatch_zh-Hant.csv")
    df['Name'] = df['品牌'] + ' - ' + df['貨品名稱']

    df['優惠'] = df['優惠'].fillna('-')
    df['discount_v2'] = df.apply(discount_calculation, axis = 1)
    df['discount_v2'] = df['discount_v2'].apply(lambda x: x.replace('.00', '').replace('.0', ''))

    df_na = df[df['優惠'] == '-']
    df_na['price_discount'] = df_na['價格'].astype(str)
    df_not_na = df[~(df['優惠'] == '-')]
    df_not_na['price_discount'] = df_not_na['價格'].astype(str) + ' (' + df_not_na['discount_v2'] + ')'
    df = pd.concat([df_na, df_not_na], ignore_index = False)

    df["選擇"] = False
    df['超市代號'] = df['超市代號'].apply(lambda x: x.title())

    df = df.fillna("-")

    return df

df = load_and_process_data()
df_page2 = load_and_process_data()


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
            div[data-testid="stButton"] button { white-space: nowrap; font-size: clamp(0.7rem, 1.2vw, 1.1rem) !important; padding: 0.25rem 0.5rem !important;}
            </style>
            '''
            , unsafe_allow_html=True)

st.set_page_config(layout="wide")

# --------------------------------------------------------------------------------------------------------------------------------------

def update_cart(pivot_df):

    state = st.session_state["my_editor"]

    for row_idx, changes in state["edited_rows"].items():
        if "選擇" in changes:
            item_name = pivot_df.iloc[row_idx]["Name"]
            
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
def show_editor(pivot_df, pivot_columns):
    
    edited_df = st.data_editor(pivot_df, 
                                column_order=tuple(pivot_columns),
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
        filtered_df = pd.DataFrame()


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
                submitted = st.button("搜尋", use_container_width=True)
            with sub_col2:
                st.markdown('<p style="margin-top:34px;"></p>', unsafe_allow_html=True)
                clear = st.button("🧹 清除搜尋", key="clear_button_2", on_click=clear_text, use_container_width=True)

        

        col1, col2, col3 = st.columns([1.3, 1, 7.7], vertical_alignment="bottom", gap = "small")
        with col1:
            st.markdown( '#### <span style="white-space: nowrap">📊 價格比較</span>', unsafe_allow_html=True )

        with col2:
            st.html(""" <style> div[data-testid="stButton"] button { padding-top: 0px; padding-bottom: 0px; height: 32px;min-height: 32px; } </style> """)
            if st.button("Save", key = "save_button"):
                pass
    
        st.write(f"當前分類：{' & '.join(selected_shop)} > {selected_cat1} > {selected_cat2}")

    # --------------------------------------------------------------------------------------------------------------------------------------

        if not filtered_df.empty:

            pivot_df = filtered_df.pivot_table(index=['Name', '選擇'], 
                                                # index = ['品牌', '貨品名稱'],
                                                columns='超市代號', 
                                                values='price_discount', 
                                                aggfunc='first',
                                                fill_value='-'
                                                ).reset_index()

            # Action when Pressing Enter
            if submitted or search_term:
                pivot_df = pivot_df[pivot_df['Name'].str.contains(search_term, case=False, na=False)]

            column_config_dict = {col: st.column_config.Column(width=estimate_width(pivot_df[col]), disabled=True) for col in pivot_df.columns}
            column_config_dict["選擇"] = st.column_config.CheckboxColumn("Bookmark",help="勾選欲購買的商品",default=False)
            
            original_columns = [x for x in pivot_df.columns if x != '選擇']
            pivot_df['選擇'] = pivot_df['Name'].apply( lambda x: x in st.session_state.cart )

            pivot_df = pivot_df[pivot_df.any(axis=1)] 

            try:
                if '全部' not in st.session_state.shop_list_deafult:
                    original_columns = [x for x in pivot_df.columns if x != '選擇']
                    original_columns = [x for x in original_columns if x != 'Name']
                    original_columns = [x for x in original_columns if x not in st.session_state.shop_list_deafult]
                    pivot_columns = ['選擇', 'Name'] + st.session_state.shop_list_deafult + original_columns
                else:
                    original_columns = [x for x in pivot_df.columns if x != '選擇']
                    pivot_columns = ['選擇'] + st.session_state.shop_list_deafult + original_columns
            except:
                original_columns = [x for x in pivot_df.columns if x != '選擇']
                pivot_columns = ['選擇'] + original_columns

            show_editor(pivot_df, pivot_columns)
            
    # ----------------------------------------------------------------------------------------------------------------------------------------

        st.sidebar.title("📕 Bookmark")
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

    st.html(""" <style> div[data-testid="stButton"] button { padding-top: 0px; padding-bottom: 0px; height: 32px;min-height: 32px; } </style> """)

    st.sidebar.title("📕 Bookmark")
    if st.session_state.cart:

        st.sidebar.write(f"- 已選擇{len(st.session_state.cart)}件貨品")
    else:
        st.sidebar.write("- Bookmark是空的")


    col1, col2 = st.sidebar.columns([4,6])
    with col1:
        sub_col1, sub_col2 = st.columns([1, 1], gap = 'small')
        with sub_col1:
            button_1 = st.button("返回", use_container_width=True)
            if button_1:
                st.session_state.page = "shop"
                st.rerun()

        with sub_col2:
            button_2 = st.button("清除", key="clear_button", use_container_width=True)
            if button_2:
                st.session_state.cart = set()
                st.rerun()

    # if st.sidebar.button("返回"):
    #     st.session_state.page = "shop"
    #     st.rerun()

    filtered_df = df_page2.copy()

    filtered_df = filtered_df[filtered_df['Name'].isin(st.session_state.cart)]

    pivot_df = filtered_df.pivot_table(index=['Name', '選擇'], 
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
            original_columns = [x for x in original_columns if x != 'Name']
            original_columns = [x for x in original_columns if x not in st.session_state.shop_list_deafult]
            pivot_columns = ['選擇', 'Name'] + st.session_state.shop_list_deafult + original_columns
        else:
            original_columns = [x for x in pivot_df.columns if x != '選擇']
            pivot_columns = ['選擇'] + st.session_state.shop_list_deafult + original_columns
    except:
        original_columns = [x for x in pivot_df.columns if x != '選擇']
        pivot_columns = ['選擇'] + original_columns

    pivot_df['選擇'] = pivot_df['Name'].apply( lambda x: x in st.session_state.cart )

    st.markdown( '#### <span style="white-space: nowrap">📊 價格比較</span>', unsafe_allow_html=True )

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
    

# kwllll: 9/5/2026
