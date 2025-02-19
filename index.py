/*********************************************************//코드잇 파이썬 기초 공부//****************************************************/

/*-------------------------------------------------------------------------------------------------------------------------------------*/
#세 수의 곱을 알려주는 프로그램을 만들려고 합니다.
#파라미터로 정수 값 세 개를 받고, 세 수의 곱을 출력하는 함수 multiply_three_numbers를 만들어 보세요.

def multiply_three_numbers(A,B,C)  #테스트 코드 참고해 함수 선언하고 파라미터 값을 넣기위해 대충 ABC 채웠음
  print(A * B * C)                 #세 수의 곱을 출력 한댔으니 이렇게


#테스트 코드
multiply_three_numbers(7, 3, 5)           #105
multiply_three_numbers(21, 4, 9)          #756
multiply_three_numbers(-7, 6, 3)          #-126


/*-------------------------------------------------------------------------------------------------------------------------------------*/
#함수를 이용한 계산.
#동욱이는 얼마 전 카페 알바를 시작했습니다. 그런데 아직 초짜이다 보니 실수가 잦네요. 실수를 좀 줄이기 위해, 카페 모카의 레시피를 출력하는 함수를 만들어 보려 합니다.
#아래의 레시피를 한 줄씩 그대로 출력하여 실습 결과와 같아지도록 함수 cafe_mocha_recipe를 작성하세요.

#1. 준비된 컵에 초코 소스를 넣는다.
#2. 에스프레소를 추출하고 잔에 부어 준다.
#3. 초코 소스와 커피를 잘 섞어 준다.
#4. 거품기로 우유 거품을 내고, 잔에 부어 준다.
#5. 생크림을 얹어 준다.

def cafe_mocha_recipe():   #테스트 코드를 참고해 함수를 선언했다. Python 에서는 함수를 호출 할 때 def 를 쓴다. Javascript 에서는 function을 쓰고 C언어는....기억이 안난다 ㅈ댓네..
  print("1. 준비된 컵에 초코 소스를 넣는다.\n2. 에스프레소를 추출하고 잔에 부어 준다.\n3. 초코 소스와 커피를 잘 섞어 준다.\n4. 거품기로 우유 거품을 내고, 잔에 부어 준다.\n5. 생크림을 얹어 준다.")

# 들여쓰기 스페이스 4번이 기본 아니면 Tab키 쓰거나 잊지말기!! 그리고 함수 선언할때 : 클론 써야 하는것 잊으면 안됨!!! ;세미클론 아님!! C++나 Javascript 아님!!!

#테스트 코드
cafe_mocha_recipe()            #임의의 함수를 호출해 출력을 하는거임 그래서 위에 순서 레시피가 출력 되어야함
cafe_mocha_recipe()

/*-------------------------------------------------------------------------------------------------------------------------------------*/
#변수를 선언해 계산.
'''kitkat: 190 칼로리
   oreos: 502 칼로리
   pringles: 292 칼로리
   twix: 135.9 칼로리
   cheetos: 485 칼로리'''

kitkat = 190                #파이썬에서는 별도의 변수를 선언 할 때 그... Javascript에 let 이런거나 C언어에서 int 이딴거 안 붙여도 된다.Java 는 Public calss 어쩌고..였는데 모름 까묵음...
oreos = 502
pringles = 292
twix = 135.9
cheetos = 485

#테스트 코드
print(kitkat + oreos * 2)
print(cheetos * 4)
print(pringles + oreos + twix)
print(pringles * 3 + oreos * 2)



/*-------------------------------------------------------------------------------------------------------------------------------------*/
#첫 번째 파이썬 코드.
#다양한 방식으로 100 출력
print(100)
print(100 * 3)              # Python에서 출력은 그냥 print 이다. C 에서는 printf 였는데...
print(300 / 3)
a = 100
b = 3
print(a * b // 3)
