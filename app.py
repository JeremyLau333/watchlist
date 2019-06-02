from flask import Flask
app = Flask(__name__)

from flask import url_for
# ...
@app.route('/')
def hello():
    return 'Hello'
@app.route('/user/<name>')
def user_page(name):
    return 'User: %s' % name
@app.route('/test')
def test_url_for():
# 下面是一些调用示例：
    #print(url_for('hello')) # 输出：/
	#print(url_for('user_page', name='greyli')) # 输出：/user/greyli
	#print(url_for('test_url_for')) # 输出：/test
	print(url_for('test_url_for', num=2)) # 输出：/test?num=2
	return 'Test page'
    
	
