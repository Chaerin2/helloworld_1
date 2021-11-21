SED (Stream Editor) 

-n : 옵션 사용시 자동출력을 하지 않음, -n을 사용하지 않고 sed 명령을 해보시면
눈에 띠게 많은 데이터가 출력되는 것을 확인할 수 있음

-e : 옵션 다음으로 우리가 사용할 command를 가지고 텍스트 파일을 가공해줌
, 맨 마지막에는 가공할 원본파일을 지정해주면 됨

-p (print) 특정 행 출력
-d (delete) 특정 행 삭제
-s (substitute) 단어 치환
-a,i (append,insert) 문자열 추가
-c (change) 특정 행 내용 전부 교체
-r(read) 특정 행에 파일의 내용을 추가 
