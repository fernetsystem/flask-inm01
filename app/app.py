from flask import Flask, render_template, request, redirect, url_foor, flash, session
import json
app=Flask(__name__)

@app.route('/')
def index():
	#return '<h2>Wecolme</h2>'
	products = ['Applications WEB', 'Applications Mobile', 'Cloud Computing', 'Migrations (on premise - cloud)', 'Blockchain']

	data = {
		'tittle': 'VECSA',
		'introduction': 'Technology on demand',
		'products': products,
		'total_products': len(products)
	}

	url = "was"
	headers = {'Authorization': ''}
	response = request.request('POST', url, header=headers)
	data = json.loads(response.read())
	print(data)
	
	return render_template('index.html', data=data)
@app.route('/getData')
def getData():	
	url = "was"
	headers = {'Authorization': ''}
	response = request.request('POST', url, header=headers)
	data = json.loads(response.read())
	print(data)
	return render_template('index.html', data=data)

	
if __name__=='__main__':
	app.run(debug=True,host='0.0.0.0', port=80)
