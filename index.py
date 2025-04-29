/*********************************************************//코드잇 파이썬 기초 공부//****************************************************/

# 쿼리 파라미터 사용 GET 요청
import requests
import json

def test_get_comments_with_query_param():
  target_post_id = 1
  print(f"Fetching comments for postId: {target_post_id}")
  url = "https://jsonplaceholder.typicode.com/comments"  # 댓글 목록 가져올 url 저장함
  
  # 지시사항에 따라 해당 값인 쿼리 파라미터 딕셔너리 생성함
  query_params = {  
    'postId':1
  }
  try:
    response = requests.get(url,json=query_params)  # url 과 query_params 를 이용해 get 요청을 보냄
    response.raise_for_status()                     # 그런 다음 response 의 상태 코드를 검증함 .raise_for_status 성공인지 실팬지
    comments = response.json()                      # response 값을 json으로 변환
    assert len(comments) > 0, "No comments received" # 응답이 비어있는 않은지 확인
    first_comment_post_id = comments[0].get('postId')
    print(f"First comment Post ID: {first_comment_post_id}")
    assert first_comment_post_id == target_post_id ,"postId does not match target"  # 지시사항대로 같은지 검증하는것임
    print(f"Successfully verified comments for postId {target_post_id}.")

  except requests.exceptions.RequestException as e:
    print(f"Error during requests: {e}")
  except (AssertionError, IndexError) as e:
    print(f"Assertion or data processing error: {e}")
  except Exception as e:
    print(f"An unexpected error occurred: {e}")
    # 출력 결과 : Fetching comments for postId: 1
                 First comment Post ID: 1
                 Successfully verified comments for postId 1.  
/*-------------------------------------------------------------------------------------------------------------------------------------*/
# DELETE 요청 보내고 상태코드 확인
import requests

post_id_to_delete = 1 # 삭제할 게시글 아이디 예시임
target_url = f"https://jsonplaceholder.typicode.com/posts/{post_id_to_delete}"  # url 완성시켜줬음
try:
  response = requests.delete(target_url)     # url 로 delete 요청 보냄
  print('Status Code after DELETE:",response.status_code)
  if response.status_code == 200 or response.status_code == 204:
        print("Post successfully deleted (or simulated deletion).")
    else:
        print(f"Failed to delete post. Status code: {response.status_code}")
except requests.exceptions.RequestException as e:
    print(f"Error sending DELETE request: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")      
# 출력 결과 : Status Code after DELETE: 200
             Post successfully deleted (or simulated deletion).
/*-------------------------------------------------------------------------------------------------------------------------------------*/
# PUT요청 보내고 응답 내용 확인
import requests
import json

post_id_to_update = 1 # 수정할 게시글 ID 예시임
target_url = f"https://jsonplaceholder.typicode.com/posts/{post_id_to_update}"  # 이런식으로 가능함
updated_post_data = {          #put 요청으로 보낼 데이터 딕셔너리로 정의
  "title":"Updated Post Title",
  "id": 1,
  "name":"bin"
}
try:
  response = requests.put(target_url, json=updated_post_data)    # put 요청 보냄
  updated_post = response.json()        # json 형식으로..
  print("Updated Post Title:",updated_post['title']) # put 으로 보낸 데이터에서 title 값 출력
  except requests.exceptions.RequestException as e:
    print(f"Error sending PUT request: {e}")
except KeyError:
    print("Error: 'title' key not found in the response.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
# 출력 결과 : Updated Post Title: Updated Post Title
/*-------------------------------------------------------------------------------------------------------------------------------------*/
# POST 요청 보내고 생성 리소스 ID 확인
import requests
import json

url = "https://jsonplaceholder.typicode.com/posts"

new_post_data = {   # 대충 post 요청으로 보낼 데이터임 - 딕셔너리 형태
  "name":"jin"
}
try:
  response = requests.post(url, json=new_post_data) # url 에 post 요청 보내는데 new_post_data 를 json 형태로 보냄 했던걸 response로 저장
  new_post = response.json() # 거를 json() 형태로 변환함
  print("Created New Post ID:",new_post['id']) # 새로 post 된 것의 id 값을 출력함
except requests.exceptions.RequestException as e:
    print(f"Error sending POST request: {e}")
except KeyError:
    print("Error: 'id' key not found in the response.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
# 출력 결과 : Created Post ID: 101
/*-------------------------------------------------------------------------------------------------------------------------------------*/
# GET 요청 후 응답 내용 확인
import requests

url = "https://jsonplaceholder.typicode.com/posts/1"
try:
  response = requests.get(url)  # GET 요청 보내서 response 변수로 저장
  response.raise_for_status()   # .raise_for_status 가 요청 성공 했는지 확인/ 200 ok 아니면 예외 처리
  json = response.json()        # response의 응답내용을 JSON() 형식으로 변환해서 변수 json 으로 저장
  print("Post Title:",json['title']) # 변수 json 데이터에서 title 값을 출력함
except requests.exceptions.RequestException as e:
    print(f"Error: {e}")
except KeyError:
    print("Error: 'title' key not found in the response.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

# 출력 결과 : Post Title: sunt aut facere repellat provident occaecati excepturi optio reprehenderit
/*-------------------------------------------------------------------------------------------------------------------------------------*/
# GET 요청 보내고 상태 코드 확인
import requests

url = "https://jsonplaceholder.typicode.com/posts/1"

try:
  response = requests.get(url) # GET 요청 보냄
  print('Status Code:',response.status_code) # 응답 상태 코드 출력함  status_code 코드 상태 나옴

except requests.exceptions.RequestException as e:
  print(f"Error: {e}")

# 출력 결과 : Status Code: 200
/*-------------------------------------------------------------------------------------------------------------------------------------*/
name = "김아무개"
ment = "안녕하세요?"

print(f"나는 {name} 입니다.\n{ment})      #Python 에서 출력할 때 변수 넣을려면 (f"{변수}) 이런 형식 이거나 ("{}블라블라".format(변수)) 이런 형태여야함 
#출력 결과는 : 나는 김아무개 입니다.
#             안녕하세요?






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
