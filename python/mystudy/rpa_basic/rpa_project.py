# Project) 나도코딩에서 구독자 분들을 대상으로 파이썬 특강을 진행합니다.
# 참여 신청은 이메일을 통해서 가능하며 메일 수신 시간 기준으로 선착순 3명이 선정됩니다.
# 아래 조건에 해당하는 메일을 자동으로 조회하여 선정되신 분들께는 선정 안내 메일을,
# 아쉽게 선정되지 못한 분들께는 대기 번호 안내 메일을 자동으로 발신하고,
# 선정된 3명의 명단을 엑셀 파일로 저장하는 자동화 프로그램을 작성하시오.

# [신청 메일 양식]
# 제목 : 파이썬 특강 신청합니다.
# 본문 : 닉네임/전화번호 뒤 4자리 (Random)
#     (예) 나도코딩 / 1234

# [선정 안내 메일]
# 제목 : 파이썬 특강 안내 [선정]
# 본문 : xx님 축하드립니다. 특강 대상자로 선정되셨습니다. (선정순번 1번)

# [탈락 안내 메일]
# 제목 : 파이썬 특강 안내 [탈락]
# 본문 : xx님 아쉽게도 탈락입니다. 취소 인원이 발생하는 경우 연락드리겠습니다. (대기순번 1번)

# [선정 명단 엑셀]
# 순번 닉네임 전화번호
# 1   유재석  9429
# 2   박명수  2463
# 3   정형돈  9236


from account import *
import smtplib
from imap_tools import MailBox
from email.message import EmailMessage
from random import *

def send_email(from_email_address, from_email_password, to_email_address, subject, msg):
    msg = EmailMessage()
    msg["Subject"] = subject
    msg["From"] = from_email_address
    msg["To"] = to_email_address
    msg.set_content(msg)
    
    with smtplib.SMTP("smtp.google.com", 587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.login(from_email_address, from_email_password)
        smtp.send_message(msg)    
        
subject = "파이썬 특강 신청합니다."
nickname = "유재석"
phone_number = randint(1000, 9999)

content = f"{nickname}/{phone_number}"
send_email(EMAIL_ADDRESS, EMAIL_PASSWORD, EMAIL_ADDRESS, subject, content)