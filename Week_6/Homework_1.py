from collections import deque

# --- 題目初始設定 ---
player_gold = 150
orders = [
    {"unit": "劍士", "cost": 20},
    {"unit": "弓手", "cost": 30},
    {"unit": "騎士", "cost": 50},
    {"unit": "投石車", "cost": 40}
]

queue_A = deque(maxlen=2)
queue_B = deque(maxlen=2)

# --- 核心邏輯 ---
# 拿掉 enumerate 後面的 1，讓回合數從 0 開始
for round_num, order in enumerate(orders):
    print(f"\n--- 第 {round_num} 回合 ---")
    
    # ==========================================
    # 階段 1：偶數回合優先處理出列 (Dequeue & Underflow 防護)
    # ==========================================
    if round_num % 2 == 0:
        # A 廠出列邏輯
        if len(queue_A) == 0:
            print("A 廠沒東西可做 (Underflow 防護成功)")
        else:
            finished_unit = queue_A.popleft()
            print(f"A 廠生產完成: {finished_unit} 出列!")
            
        # B 廠出列邏輯
        if len(queue_B) == 0:
            print("B 廠沒東西可做 (Underflow 防護成功)")
        else:
            finished_unit = queue_B.popleft()
            print(f"B 廠生產完成: {finished_unit} 出列!")

    # ==========================================
    # 階段 2：處理玩家派單 (Enqueue & 檢核邏輯)
    # ==========================================
    if not order:
        print("玩家本回合無動作，單純推進時間")
    else:
        unit_name = order.get("unit")
        cost = order.get("cost")
        
        # 檢核 1：Overflow 防禦
        if len(queue_A) == 2 and len(queue_B) == 2:
            print(f"產線全滿！{unit_name} 訂單拒絕")
        # 檢核 2：資源檢核
        elif player_gold < cost:
            print(f"黃金不足，無法生產 {unit_name}")
        # 檢核 3：負載平衡與派單
        else:
            player_gold -= cost
            if len(queue_A) <= len(queue_B):
                queue_A.append(unit_name)
                print(f"{unit_name} 分派至 A 廠 (剩餘黃金: {player_gold})")
            else:
                queue_B.append(unit_name)
                print(f"{unit_name} 分派至 B 廠 (剩餘黃金: {player_gold})")

    # ==========================================
    # 階段 3：印出廠房狀態
    # ==========================================
    # 將 deque 轉為 list 才能印出完美的 [''] 括號格式
    print(f"A: {list(queue_A)} | B: {list(queue_B)}")