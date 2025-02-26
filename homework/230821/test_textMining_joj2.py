from collections import defaultdict, OrderedDict
text = '''
"부산 버스와 도시철도 요금이 오는 10월부터 최대 29% 오른다. 요금 인상률이 서울 인천 등과 비교해 전국 최고 수준이어서 대중교통 이용자 부담이 한층 가중될 전망이다.
부산시는 지난 18일 물가대책위원회 심의를 통해 시내버스·도시철도 요금을 각각 350원, 300원 인상하기로 했다고 20일 밝혔다.
 도시철도는 300원을 올리되 오는 10월 6일과 내년 5월 3일 150원씩 두 차례에 나눠 인상토록 했다. 버스 요금이 오르는 것은 2013년 이후 10년만이고, 
 도시철도 요금은 2017년 이후 6년 만이다. 인상된 요금은 오는 10월 6일 오전 4시부터 적용된다.
시내버스(일반) 요금은 성인 교통카드 기준으로 1200원에서 1550원으로 무려 29.1%(350원)나 한꺼번에 오른다. 
좌석버스는 1700원에서 2050원으로 20.5% 오른다. 심야 일반버스는 1950원, 심야 좌석버스는 2450원으로 오른다. 
현금은 교통카드 요금에 150원이 각각 추가된다. 다만 청소년 요금은 동결, 어린이는 무료다. 도시철도 요금은 두 번에 걸쳐 오른다.
 오는 10월 6일 150원이 오른 1450원(성인 교통카드 기준·1구간), 내년 5월 3일 다시 150원을 인상한 1600원(23% 인상)이 된다.
   2구간은 1800원으로 20% 인상이다. 현금은 카드 요금에서 100원 추가된다. 청소년 요금은 동결, 어린이는 무료다. 
   부산~김해 경전철은 오는 10월 300원 올리는 것으로 결정됐으나 김해시와 협의를 거친 뒤 시행될 예정이다. 마을버스 요금은 시내버스와 동일한 최대 350원 범위 내에서 각 구·군이 조정한다.
이 같은 인상 폭·요금은 서울을 넘어선 전국 최고 수준이어서 시민 부담이 과중하다는 지적이 나온다. 서울시는 지난 12일 버스요금을 300원(1500원) 올렸고,
 도시철도 요금은 오는 10월과 내년 상반기 두 차례에 나눠 150원씩 올리기로 했다. 또 인천과 울산은 버스 요금을 250원 올리는 것으로 결정했다. 
 시 관계자는 “서울과 부산의 버스 요금 책정 기준이 다르다”며 “요금을 10년 만에 올리는 데다, 시의 재정 부담도 심각한 수준”이라고 설명했다. 
 이어 시는 지난 1일부터 시행한 ‘동백패스(대중교통 월 4만5000원 이상 사용 시 초과분을 동백전 인센티브로 돌려주는 것)’를 통해 혜택을 돌려주겠다고 밝혔다."
'''.lower().split()
news_text = defaultdict(lambda: 0)
for news in text:
    news_text[news] += 1

news_short = OrderedDict(
    sorted(news_text.items(), key=lambda t: t[1], reverse=True)).items()
news = list(news_short)

for i in range(10):
    print(news[i])
