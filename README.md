# 챗봇(Chat-bot) '숭실이'
# (Soongsil University Open Source Project)
---------------------------------------------------------------------------------------------------------
## 목차

### 프로젝트 소개
- 배경 기대효과
- 구성
- 구현 방법

### 설치 및 사용 메뉴얼
- 카카오톡에서 '숭실이' 추가하기
- '숭실이'와 대화하기

### Reference
- 프로젝트 제작에 참고한 참고문헌, 서적, URL
---------------------------------------------------------------------------------------------------------

### 프로젝트 소개
#### 배경 및 기대효과
- 숭실대학교 학생들은 '유세인트', '슈케치', '숭실대학교 공식 홈페이지', '스마트포탈' 등 다양한 웹과 어플을 통해 교내 정보를 확인할 수 있다. 이처럼 획일화 되어 있지 않고 분산된 정보들로 인해, 많은 학생들이 혼란을 겪는다.
- 우리 팀은 이런 배경에서 정보 열람의 절차가 까다롭고 정보 제공 서비스가 분산되어 있다는 문제를 인지하였다. 이를 해결하기 위한 논의 결과, 카카오톡의 챗봇으로 정보 제공 서비스를 제공하는 방안을 채택했다. 챗봇을 통해 교내 정보 제공처를 획일화 하고 정보의 접근성을 높여 많은 학생들이 쉽게 교내 정보를 얻을 수 있기를 기대한다.

#### 구성
- **식단**: 학생 식당, 도담 식당, 기숙사 식당의 당일 메뉴를 알 수 있다.
- **학사 일정**: 1년 간의 교내 주요 학사 일정의 정보를 확인할 수 있다.
- **공지사항**: 학교 측에서 올려주는 공지사항들을 확인할 수 있다.
- **학사 정보**: 학과 정보(학과/학부 사무실 위치, 전화 번호, 학사/학부 홈페이지)와 특정 학사 정보(군 휴학, 조기졸업 등)을 알 수 있다.
- **비교과 프로그램**: 교과목에 포함되지 않는 프로그램들과 공모전의 정보를 알 수 있다.
- **도서관 정보**: 중앙도서관의 운영시간, 열람실 이용현황 등을 알 수 있다.

#### 구현 방법
- **챗봇 제작 플랫폼 선정**: '카카오 i 오픈 빌더'를 이용하면 쉽게 챗봇을 생성할 수 있고, 지식+와 스킬 등 다양한 기능을 사용하여 데이터의 저장, 수정, 통신에도 용이하다.
- **카테고리 분류**: 정보가 유동적으로 변화함(A그룹), 정보 변동이 없음(B그룹)
    - A그룹: 열람실 이용현황, 비교과프로그램, 공지사항, 식단 --> 웹 크롤링 or API 사용
    - B그룹: 학사 일정, 학사 정보, 도서관 정보 --> csv파일 정리 후, 지식+ 기능 활용
- **일러스트 제작 및 활용**
    - 사용자 UI를 위해 카테고리 별로 일러스트 제작
    - 홈 버튼과 사용법 제작에 활용

---------------------------------------------------------------------------------------------------------

### 설치 및 사용 메뉴얼
- 카카오톡에서 '숭실이' 추가하기
    - 카카오톡 메인 화면 우측 상단의 돋보기 버튼을 클릭한다.
![1](https://user-images.githubusercontent.com/61671097/101186777-e29f0a00-3696-11eb-9209-be2f3fdeb54b.PNG)

    - 검색창에 '숭실이'를 검색한다.
![2](https://user-images.githubusercontent.com/61671097/101186779-e337a080-3696-11eb-8ea2-83be0c7b2f70.PNG)

    - '채팅하기'를 눌러 '숭실이'와 대화를 시작한다.
![3](https://user-images.githubusercontent.com/61671097/101186781-e3d03700-3696-11eb-94a1-ef91c9fad6d7.PNG)


























