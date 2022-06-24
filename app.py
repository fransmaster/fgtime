from flask import Flask,render_template,request,redirect,url_for,flash
import sqlite3 as sql
app= Flask(__name__)
@app.route('/')
def home():
	con=sql.connect("fgtime.db")
	cur=con.cursor()
	cur.execute("select * from relojes")
	relojes= cur.fetchall()
	con.commit()
	con.close()

	nombre='Francis Guerra'
	return render_template('inicio.html', nombre=nombre, data=relojes)

@app.route('/nuevo_reloj',methods=['POST','GET'])
def nuevos_relojes():
	if request.method=='POST':
		modelo=request.form['modelo']
		marca=request.form['marca']
		precio=request.form['precio']
		con=sql.connect("fgtime.db")
		cur=con.cursor()
		cur.execute("insert into relojes(modelo,marca,precio) values (?,?,?)",(modelo,marca,precio))
		con.commit()
		con.close()
		flash('nuevo_reloj','success')
		return redirect(url_for("home"))


	return render_template('nuevos_relojes.html')

@app.route("/editar_reloj/<string:id>",methods=['POST','GET'])
def editar_reloj(id):
	con=sql.connect("fgtime.db")
	con.row_factory=sql.Row
	cur=con.cursor()
	cur.execute("select * from relojes where id=?",(id,))
	data=cur.fetchone()
	if request.method=='POST':
		modelo=request.form['modelo']
		marca=request.form['marca']
		precio=request.form['precio']
		con=sql.connect("fgtime.db")
		cur=con.cursor()
		cur.execute("update relojes set modelo=?, marca=?, precio=? where id=?",(modelo,marca,precio,id))
		con.commit()
		flash('User Updated','success')
		return redirect(url_for("home"))
	return render_template("editar_reloj.html",data=data)

@app.route("/delete_reloj/<string:id>",methods=['GET'])
def delete_reloj(id):
	con=sql.connect("fgtime.db")
	cur=con.cursor()
	cur.execute("delete from relojes where ID=?",(id,))
	con.commit()
	flash('reloj Deleted','warning')
	return redirect(url_for("home"))

    	




if __name__=='__main__':
	app.secret_key='fgtime'
	app.run(debug=True)
