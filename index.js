/***************************************************************//코드잇 자바스크립트 기초 공부//******************************************/
                                                           //과제9. 자료형 응용하기
//숫자형을 담고 있는 변수(material1,material3,material5)과 문자열을 담고 있는 변수(material2,material4)가 있다
//변수끼리 연산해 result1에는 문자열 '34'를 result2에는 숫자형 34를 담아라.

let material1 = 3;
let material2 = '3';
let material3 = 10;
let material4 = '4';
let material5 = 4;
//결과 나타냄
let result1;
let result2;
//그래서 연산값을 넣어줘야함
result1 = material2 + material4;
result2 = material1 * material3 + material5

// 테스트 코드
console.log(result1);
console.log(typeof result1);
console.log(result2);
console.log(typeof result2);                                                                                                    /* typeof 는 형식은 문자열인지 숫자형인지 판가름 하는거임*/


                                                           //과제8. 템플릿 문자열 실습
//근무자 이름(name),근무시간(time),시급(wege)을 전달 받고 총 급여 계산을 위한total변수 주어짐

function calcWage(name,time,wege){
  let total = time * wege;
                                                                                                                              /* 자바스크립트에서는 ${} 이것으로 표현한다!! */
  console.log(`${name}님의 근무 시간은 총${time}시간이며, 최종 급여는 ${total}원 입니다.`);
}

//테스트 코드
calcWage('김윤식',208,11340);
calcWage('성규재',175,12160);
calcWage('손태웅',161,13070);
calcWage('허우선',222,10980);


                                                           //과제7-1. 문자열 실습2
//함수 문자열 개념이용 문장 출력하기
// 영화 '베테랑'에서 "어이가 없네~"라는 대사가 유명했다.

console.log(`영와 '베테랑'에서 "어이가 없네~"라는 대사가 유명했다.`)


                                                           //과제7. 문자열 실습1

//함수 문자열 개념을 이용 두 문장을 출력하라
// 한국 영화 역사상 아카데미상을 받은 것은 '기생충'이 처음이다.
// 아리스토텔레스는 "인간은 사회적 동물이다."라고 말했다.

console.log(`한국 영와 역사상 아카데미상을 받은 것은 '기생충'이 처음이다.\n아리스토텔레스는 "인간은 사회적동물이다."라고 말했다.`)

                                                                                                                             /* 자바 스크립트에서는 console.log에서 출력할때 '' 이거랑 "" 이거랑 `` 이거 다 가능!!! */

                                                           //과제6. 파라미터 응용 함수 호출 계산2

//맡긴 금액 (amount), 맡기는 기간(term), 이자율(rate)를 입력 받으면 이자를 계산해 주는 함수(interestcalculator)함수를 작성하라

function interestcalculator (amount, trem, rate){
    return amount * trem * rate / 100;
}                                                                              // 선언한 함수의 계산 값을 return 해서 돌려줘야한다!!!
let myMoney = 3650000;                                                         // 그래서 return이 필요하다!!
let myInterest = interestcalculator(myMoney, 1, 4);
let totalMoney = myMoney + myInterest;


console.log('맡긴 금액은 ' + myMoney + '원 입니다.');
console.log('이자는 ' + myInterest + '원 입니다.');
console.log('최종 받을 금액은 ' + totalMoney + '원 입니다.');


                                                           //과제5. 파라미터 응용 함수 호출 계산

 function interestCalculator(amount, saveTerm, interestRate){
  let money = amount * saveTerm * interestRate / 100;
  let total = amount + money
 
  console.log('맡긴 금액은 ' + amount + '원 입니다.');
  console.log('이자는 ' + money +'원 입니다.');
  console.log('최종 받을 금액은 ' + total + '원 입니다.');
}
interestCalculator(3650000, 1, 4);


                                                           //과제4. 파라미터 응용 함수 호출 계산

function bmiCalculator(name,weight,height){
    console.log(name + `님의 체질량지수는 `+ weight/(height*height/10000)+`입니다.`);
}
  
  // 테스트 코드
  bmiCalculator('홀쭉이', 43.52, 160);
  bmiCalculator('코린이', 61.25, 175);
  bmiCalculator('통통이', 77.76, 180);


                                                           //과제3. 파라미터 응용 함수 호출함

  function teraToGiga(a){
    console.log(a + 'TB는');
    console.log(a * 1024 +'GB 입니다.');
    
}
  function teraToMega(b){
    console.log(b + 'TB는');
    console.log(b * 1024 * 1024 +'MB 입니다.');
}
  teraToGiga(2);
  teraToMega(2);


                                                           //과제2. 함수 이용 출력하기
  function printChorus(){
    console.log(`무구궁화 삼천리 화려 강산\n대한 사람 대한으로 길이 보전하세`);
}
                                                                                                //function 함수를 호출하고 정의한다
                                                                                                //JS 에서는 'let'

console.log('1절');
console.log('동해 물과 백두산이 마르고 닳도록');
console.log('하느님이 보우하사 우리나라 만세');
 
console.log('2절');
console.log('남산 위에 저 소나무 철갑을 두른 듯');
console.log('바람서리 불변함은 우리 기상일세');
 
console.log('3절');
console.log('가을 하늘 공활한데 높고 구름 없이');
console.log('밝은 달은 우리 가슴 일편단심일세');
 
console.log('4절');
console.log('이 기상과 이 맘으로 충성을 다하여');
console.log('괴로우나 즐거우나 나라 사랑하세');

                                                              
 
                                                           //과제1. 15라는 숫자 3번 입력해 보기
                                                                                                 //자바 스크립트에서는 출력할 때 console.log 사용
console.log(10+5);
console.log(10*3/2);
console.log(45/3);


