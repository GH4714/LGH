#파이썬 버전의, GUI, 윈도우~~~~

from tkinter import *
import csv
## 함수 선언 부
def makeEmptySheet(r, w) :
    retList = []
    for i in range(0, rowNum):
        tmpList = []
        for k in range(0, colNum):
            ent = Entry(window, text='', width=10)
            ent.grid(row=i, column=k)
            tmpList.append(ent)
        retList.append(tmpList)
    return retList

## 전역 변수부
csvList = []
rowNum, colNum = 0, 0
workSheet = []

## 메인 코드부
window = Tk()

with open("C:/CookAnalysis/CSV/singer1.csv", "r") as inFp :
    #csv 모듈에서 제공하는 함수를 이용함.
    csvReader = csv.reader(inFp)
    #csvReader csv 값이 다 있음. next함수를 이용해서, 한줄씩읽기.
    header_list = next(csvReader)
    #첫 행은 컬럼. 헤더 부분.
    csvList.append(header_list)
    
    #반복문 2번째 행, 실제 데이터를, 추가하는 부분
    for row_list in csvReader:
        csvList.append(row_list)

rowNum = len(csvList)
colNum = len(csvList[0])
workSheet = makeEmptySheet(rowNum, colNum)


#csvList csv파일의 내용이 임시로 저장되어있는 이중 리스트
idx = 2 # 평균 키의 인덱스
for i in range(0, rowNum) : # 워크시트에 리스트값 채우기. (= 각 빈 셀에 값 넣기)
    for k in range(0, colNum) :
        #각행의 6번째 컬럼의 타입이 일단 숫자인지 체크
        if ( csvList[i][idx].isnumeric() ) :
            #해당 각행의 6번째 컬럼의 값의 조건 167이상이 맞는지
            if ( int(csvList[i][idx]) >= 6) :
                #각행의 셀에 대해서
                ent = workSheet[i][k]
                #각행의 배경색 노란색 변경
                ent.configure(bg='yellow')

        #GUI 각 셀에 값을 입력을 하는 부분.
        #csvList에 실제 값이 들어 있음.
      
        workSheet[i][k].insert(0, csvList[i][k])

window.mainloop()