#include <stdio.h>

int main() {
    char hexDigits[] = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"; // 16진수 문자
    int decNum; // 10진수 숫자
    char base26Str[100]; // 26진법 문자열
    int digitIndex, strIndex; // 숫자 인덱스, 문자열 인덱스

    for (decNum = 1; decNum <= 25; decNum++) {
        strIndex = 0; // 문자열 인덱스 초기화
        int tempNumber = decNum; // 임시 숫자 변수

        while (tempNumber > 0) {
            int remainder = tempNumber % 26; // 26으로 나눈 나머지
            base26Str[strIndex] = hexDigits[remainder]; // 해당 문자 할당
            strIndex++;
            tempNumber = tempNumber / 26; // 몫 계산
        }
        base26Str[strIndex] = '\0'; // 문자열 마지막에 널 문자 추가

        // 변환된 26진법 숫자 출력
        printf("%d -> %s\n", decNum, base26Str);
    }
    return 0;
}
