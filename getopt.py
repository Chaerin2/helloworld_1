getopt() -> 옵션을 분석할 수 있게 제공하는 시스템 호출
int getopt(int argc, char * const argv[], const char *optstring);
1.argc,argv : main() 함수가 받은 파라미터를 그대로 전달
2.optstring : 파싱해야 할 파라미터를 씀, 옵션이 별도의 파라미터를 받는 경우 콜론을 함꼐 씀

#include <unistd.h> 
int getopt(int argc, char *const argv[],const char *optstring)

extern char *optarg;
extern int optind, opterr, optopt;

->getopt를 사용하기 위해서는 unistd.h 헤더파일을 추가해야함
argv에 있는 명령어를 계속 파싱함
정상적으로 파싱이 되면 optstring 에서 지정된 문자열이 반환되고
파싱이 전부되었다면 최종적으로 -1을 반환

