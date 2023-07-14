# gitbash 사용법
## 기초 문법
1. **touch ~~~** : 파일생성
2. **mkdir ~~~** : 새 디렉토 리 생성
3. **ls** : 현재 작업 중인 디렉토리 내부의 폴더/파일 목록을 출력
4. **cd.** 현재 **cd..** 뒤로
5. **start ~~~** : ~를 실행
6. **rm ~** : 파일 삭제

* **경로 확인이 중요하다**

## commit 작성자 설정 및 확인
1. **git config --global user.name 이름**
2. **git config --global user.email 메일주소**
* **git config --global -1**
: 이름, 주소 확인
## git 실행 및 취소
1. **git init** : 실행
---   
2. **git add ~~** : 워킹 -> 스테이징
   1. **git status** : add 상태 확인
   2. **git reset** : 다시 워킹디렉토리로
---
3. **git commit -m '~~~'** : 스테이징 -> 리포짓
   1. **git log** : commit 상태 확인
   2. **rm -rf .git** : git 삭제
---
* **rm -rf ~~** : 파일 삭제
* **echo > ~ > ~~ > ~~~** : 여러 파일 한 번에 생성
* **echo ~.~~ >> .gitignore** : 깃의 영향을 안받는 이그노어 생성

## 푸시와 풀
1. **git remote add 이름 url** : commit한 파일을 생성
   1. **git remote -v** : 확인용
2. **git push 이름 master** :  깃허브에 푸시하기

---
1. **git pull 이름 master** : 변경사항만 받기
2. **git clone url** : 전체 파일 받기

* 이름을 변경하여 저장하는데 커밋한 장소는 변경하면 안된다 +master는 강제로 실행되어 데이터가 날아갈 수 있다?