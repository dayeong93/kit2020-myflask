from flask import Flask, request, render_template, redirect, url_for, abort
app = Flask(__name__)

#'127.0.0.1:5000/input/' 뒤에 '/', '/hello/', '/hello/00' 를 넣으면 각각 메인페이지, HELLO WORLD, HELLO00가 뜸.
@app.route('/')
def index():
    return '메인페이지'

# '127.0.0.1:5000/input/' 뒤에 '/hello/' 대신 '/hello'를 적어도 '리다이트'로 '/hello/'와 같은 결과가 뜸
@app.route('/hello/')
def hello():
    return 'Hello, World!'

@app.route('/hello/<name>')
def helloval(name):
    return 'Hello, {}!'.format(name)   

#'127.0.0.1:5000/input/' 뒤에 '1,2,3' 을 넣으면 각각 도라에몽, 진구, 퉁퉁이 그외의 숫자를 넣으면 없어요가 뜸.
@app.route('/input/<int:num>')
def input_num(num):
    if num == 1:
        return "도라에몽"
    elif num == 2:
        return "진구"
    elif num == 3:
        return "퉁퉁이"
    else:
        return "없어요"
    # return 'Hello, {}!'.format(name) 


# 8주차 과제 로그인폼 
@app.route('/login', methods=['GET','POST'])
def login():
    if request.method =='GET' : 
       return render_template('login.html')
    else:
        id = request.form['id']
        pw = request.form['pw']
        # id와 pw가 임의로 정한 값이랑 비교 해서 맞으면 맞다 틀리면 틀리다
        if id == 'abc' and pw == '1234': 
            return "안녕하세요~ {}님".format(id)
        else:
            return "아이디 또는 패스워드를 확인하세요"

@app.route('/form')
def form():
    return render_template('test.html')

@app.route('/method', methods=['GET','POST'])
def method():
    if request.method == 'GET':
        return 'GET 으로 전송이다.'
    else:
        num = request.form['num']
        name = request.form['name']
        print(num, name)
        return 'POST 이다. 학번은 : {} 이름은 : {}'.format(num, name)

# 'redirect' = url로 페이지를 이동시킴 
@app.route('/naver')
def naver():
    return redirect("https://www.naver.com/")

# 'redirect' = url로 페이지를 이동시킴 
@app.route('/kakao')
def daum():
    return redirect("https://www.daum.net/") 
 
# 루트이름이 url_test이지만, 'daum'의 값인 kakao를 불렀기 때문에 카카오의 주소 다음으로 이동한다. 즉 함수명만 바꿔주면 주소를 변경가능.  
@app.route('/url_test')
def url_test():
    return redirect(url_for('daum')) 

@app.route('/url_test1')
def url_test1():
    return redirect(url_for('naver')) 

#9주차과제
@app.route('/move/<site>')
def move_site(site):
    if site == 'naver':
      return redirect(url_for('naver')) 
    elif site == 'daum':
      return redirect(url_for('daum'))
    else:
        abort(404)
@app.errorhandler(404) 
def page_not_found(error): 
    return "페이지가 없습니다. URL를 확인 하세요", 404

@app.route('/img')
def img():
    return render_template("image.html")


if __name__ == '__main__':
    with app.test_request_context():
        print(url_for('daum'))
    app.run(debug=True)