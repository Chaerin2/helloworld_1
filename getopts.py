getopts 명령은 매개변수 리스트에서 옵션 및 옵션 인수를 검색하는 Korn/POSIX 쉘 내장 명령

+(더하기 부호) 또는 -(빼기 부호)로 시작하고 그 뒤에 문자가 옴
+ or - 로 시작하지 않는 옵션은 OptionString을 종료함

-a, -p는 명령행 옵션으로 이를 처리하기 위해선 getopt 함수를 
OPTARG, OPTIND 와 함께 사용하면 됨

OPTARG 는 getopt 했을 때 붙어있는 인자값
OPTIND 는 getopt로 처리하고 남은 다음 처리할 인덱스 번호가 됨

