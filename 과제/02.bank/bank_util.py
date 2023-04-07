# 이름과 금액을 입력으로 받아 account에 새로운 항목을 추가
import datetime

def create_account(a):
    try:
        account_name = input('이름입력: >> ')
    except:
        print('입력이 잘못되었습니다.')
        return
    now = datetime.datetime.now()
    ano = now.strftime('%H%M%S')
    a.append({'소유주':account_name, '계좌번호':ano, '잔액':0})
   
# 이름과 금액을 입력으로 받아 account의 금액을 추가
def deposit(account):
    try:
        cmd = input('계좌번호와 입금할 금액입력>>  ').split()
    except:
        print('입력이 잘못되었습니다.')
        return
    ano, amount = cmd[0], int(cmd[1])

    for acc in account:
        if acc['계좌번호'] == ano:
            acc['잔액'] += amount
            return

# 이름과 금액을 입력으로 받아 account의 금액을 차감
def withdraw(account):
    try:
        cmd = input('이름과 입금할 금액입력>>  ').split()
    except:
        print('입력이 잘못되었습니다.')
        return
    ano, amount = cmd[0], int(cmd[1])
    for acc in account:
        if acc['계좌번호'] == ano:
            acc['잔액'] -= amount
            return
