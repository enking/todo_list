#챗 지피티가 추천한는 프로젝트 num1
#할일 목록 프로젝트 
#사용자가 작업을 추가, 편집 및 삭제할 수 있는 기본적인 할 일 목록 애플리케이션을 만들어보세요. 마감일 설정 또는 작업 우선순위 설정과 같은 기능도 구현할 수 있습니다.
#그래서 이걸 메모장에 저장 삭제 관여 할 수 있게 메모장 제목은 사용자가 지정해서 만들도록 
#최초에 파일이 없으면 조회된 파일이 없다고 뜨게 하고 
#파일이 있으면 조회해서 열 수 있는 목록을 고르게 해주게까지


#여기서 이제 목록을 조회해서 저장된 기존 메모가 있는지 확인

#만약에 없으면 새 파일을 추천 해줌 
#있으면 선택을 하게 함 

#선택을 하게 하던 새 파일을 만들던 목록 추가, 삭제, 편집을 할 수 있게 만들어 준다.
#모든 작성한 내용은 sql에 저장이 되며 불러오고 편집이 가능함 

#목록 추가 기능
# 1. 업무 입력, 마감일 설정, 중요도 설정 -> 고오급 기능을 구현하면 여기서 이제 sort를 해서 중요도 판단을 추천해주는거지 

#목록 삭제 기능
#선택한 목록을 다 했다고 지우는 기능 또는 할 필요가 없던 어쨋든 삭제를 하게 해주는 기능 

import tkinter #파이썬 구이 설정
import sqlite3  # 파이썬 sql 불러옴 

window=tkinter.Tk()

window.title("To Do List") # 창 제목 투 두 리스트로 설정
window.geometry("800x600+600+200") # 창 사이즈 설정 x를 사용하며, 최초 사이즈 정하고 좌에서 얼마나 멀리 + 우에서 얼마나 멀리 설정할지 정하는 것임
window.resizable(True, True) # 창의 크기를 조정할 수 있는 설정 False로 설정시 창 크기 조절이 불가


label = tkinter.Label(window, text="Welcome! This is Your To Do List Checklist") # 창 안에서 내가 띄우고 싶은 문구를 띄워줌 
label.pack() # tkinter에서 pack이라는 메소드를 사용 
#######################여기까지 만든게 이제 창의 제목을 띄워주고 창에서 소개 문구를 띄워줌############################################################

'''다음의 할일은 라디오 버튼것을 만들어서 next를 누르면 다음 창이 나오고 그 창에서 이제 나오는 목록을 만들어줘야되는거임 <- 이제 업그레이드를 하면 여기가 그냥 나오고 바로 사라지게 설정 
목록에서는 이제 기본 화면으로 오늘 날짜에 맞는 월력 캘린더를 띄우고 작성할 수 있는 칸을 그림으로 그려주며
이 모든 정보를 sql 디비를 활용해서 저장 편집이 가능하게 해줌
이 정보들을 이제 저 창에서 실행하며 작업할 수 있게 함 
일단 창 구성을 다 하고 
db연동하고
그러면 이제 거의 끝나는거 같은데 구이 디자인 하고 구이에 동작 기능까지 추가하는 것
현재 시간 맞춰서 캘린더 띄워주고 까지 
구이 디자인, db 공부 막상 정리하고 보니까 존1나 쉽네 시2발  1)구이 기능 공부 2) db 기능 공부
'''



window.mainloop() # 파이썬 구이 마무리