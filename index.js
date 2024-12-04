/***************************************************************//코드잇 자바스크립트 공부//***************************************** */
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


