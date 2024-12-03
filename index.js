//코드잇 자바스크립트 공부
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

  //과제4.   same
  function bmiCalculator(name,weight,height){
    console.log(name + `님의 체질량지수는 `+ weight/(height*height/10000)+`입니다.`);
  }
  
  // 테스트 코드
  bmiCalculator('홀쭉이', 43.52, 160);
  bmiCalculator('코린이', 61.25, 175);
  bmiCalculator('통통이', 77.76, 180);