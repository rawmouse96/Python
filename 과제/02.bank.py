import sys, os, joblib
import bank_util as bu

# 계좌는 계좌번호, 소유주, 잔액으로 구성됨
# 계좌번호는 생성된 시점의 시간, 분, 초 6자리로 구성
filename = 'account.jl'
if os.path.exists(filename):
    account = joblib.load(filename)
else:
    account = []
    
while True:
    try:
        menu = int(input('1:계좌생성, 2:계좌목록, 3:입금, 4: 출금, 5: 종료>>  '))
    except:
        print('잘못된 명령입니다.\n')
        continue

    if menu == 5:
        joblib.dump(account, filename)
        sys.exit()
    if menu == 1:
        bu.create_account(account)
    elif menu == 2:
        for list in account:
            for key, val in list.items():
                if key == '잔액':
                    print(f'{key}: {val:,d}', end='\t')
                else:
                    print(f'{key}: {val}', end='\t')
            print()
    elif menu == 3:
        bu.deposit(account)
    elif menu == 4:
        bu.withdraw(account)
    print()
