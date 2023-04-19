import shioaji as sj  #引入shioaji套件，命名為sj
api = sj.Shioaji(simulation=True)  #建立shioaji api物件，simulation=True代表使用模擬環境
api.login(   #登入
    person_id="PAPIUSER08",  #帳號
    passwd="2222",  #密碼
    contracts_cb=lambda security_type: print(f"{repr(security_type)} fetch done.")
)