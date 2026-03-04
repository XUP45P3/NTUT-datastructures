Dict = {}

while True :

    action = input("\n請選擇操作選項：（a 註冊,b 登入,c 退出）？").strip()

    if action == 'a' :
        account = input("請輸出帳號：").strip()
        password = input("\n請輸入密碼：").strip()

        if account not in Dict:
            Dict[account] = password
            print("註冊成功！")
        else:
            print("帳號已存在，請重新輸入！")

    elif action == 'b' :
        account = input("\n請輸出帳號：").strip()
        password = input("\n請輸入密碼：").strip()

        if account in Dict :
            if password  == Dict[account] :
                print("登入成功！")

            else :
                print("帳號密碼錯誤，登入失敗！")

        else:
            print("找不到帳號，請先註冊！")

    elif action == 'c' :
        print("\n已退出！")
        break

    else :
        print("請輸入 a、b、c！")