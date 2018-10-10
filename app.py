#importing files
from flask import Flask,render_template,request,redirect,url_for,send_from_directory
import os
import extractData


#app name
app=Flask(__name__)


#app route for main page
@app.route('/', methods=['GET', 'POST'])
def home():
	#deleting all file in the folder
	# folder = 'static/temp/'
	# for the_file in os.listdir(folder):
	# 	file_path = os.path.join(folder, the_file)
	# 	try:
	# 		if os.path.isfile(file_path):
	# 			os.unlink(file_path)
	# 	except Exception as e:
	# 		print(e)
	if request.method == 'GET':
#IF taking csv input
#move code from get to Post


		print("GET req")
		data_list=extractData.cleandata()
		length=len(data_list)
		return render_template("index.html",data_list=data_list,len=length)
	elif request.method == 'POST':
			data_list=extractData.cleandata()
			length=len(data_list)
			return render_template("index.html",data_list=data_list,len=length)


			
			
	
	return render_template("index.html",data_list=data_list)

if(__name__=='__main__'):
	app.run(debug=True,use_reloader=True)