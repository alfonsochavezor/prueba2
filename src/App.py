from flask import Flask,render_template,request,redirect,url_for,flash
from flask_mysqldb import MySQL
from datetime import date
from datetime import datetime
app = Flask(__name__)
##conexion de mysql
app.config['MYSQL_HOST']='bgumajwbm1ne6t3glgeg-mysql.services.clever-cloud.com'
app.config['MYSQL_USER']='uzlyqwzf1mfgezvj'
app.config['MYSQL_PASSWORD']='SVk6PsCcJTcDPMqfKFo0'
app.config['MYSQL_DB']='bgumajwbm1ne6t3glgeg'
mysql=MySQL(app)




#configuracion
app.secret_key='mysecretkey'

@app.route('/')
def index():
    cur = mysql.connection.cursor()
    cur.execute('select * from clientes')
    datos = cur.fetchall()
    return render_template('index.html',contacts=datos)

@app.route('/sucursal2')
def segundasuc():
    cur = mysql.connection.cursor()
    cur.execute('select * from clientes ')
    datos = cur.fetchall()
    return render_template('suc2.html',contacts=datos)

@app.route('/sucursal3')
def tercersuc():
    cur = mysql.connection.cursor()
    cur.execute('select * from clientes ')
    datos = cur.fetchall()
    return render_template('suc3.html',contacts=datos)

@app.route('/add_phone', methods=['POST'])
def add_phone():
    if request.method=='POST':
        sucursal=request.form['Sucursal']
        nombre=request.form['Nombre']
        telefono=request.form['Telefono']
        tipo_rep=request.form['Tipo_Rep']
        modelo=request.form['Modelo']
        imei=request.form['Imei']
        fecha=date.today()
        Estadorep=request.form['Estadorep']
        cur = mysql.connection.cursor()
        cur.execute('INSERT INTO clientes (Sucursal,nombre_cliente,Numero_cliente,Tipo_rep,Modelo,imei,Fecha,Estadorep) VALUES(%s,%s,%s,%s,%s,%s,%s,%s)',
        (sucursal,nombre,telefono,tipo_rep,modelo,imei,fecha,Estadorep))
        mysql.connection.commit()
        mensajecorrecto='La informacion del cliente se guardo correctamente'
        flash(mensajecorrecto)
        print(sucursal)
        if sucursal=='Nuevo hermosillo':
            return redirect(url_for('tercersuc'))
        if sucursal=='Xolotl':
             return redirect(url_for('segundasuc'))

        return redirect(url_for('index'))
        


    
@app.route('/edit/<id>')
def editar(id):
    cur = mysql.connection.cursor()
    cur.execute('select * from clientes where idclientes=%s',(id))
    data=cur.fetchall()
    print (data[0])
    return render_template('edit-cliente.html', contact = data[0])


@app.route('/update/<id>', methods=['POST'])
def update_user(id):
    cur=mysql.connection.cursor()
    if request.method=='POST':
        sucursal=request.form['Sucursal']
        nombre_cliente=request.form['Nombre']
        telefono=request.form['Telefono']
        tipo_rep=request.form['Tipo_Rep']
        modelo=request.form['Modelo']
        Estadorep=request.form['Estadorep']
        cur.execute("""
        update clientes
        set Nombre_cliente =%s,
            Numero_cliente=%s,
            Tipo_rep=%s,
            Modelo=%s,
            Estadorep=%s
        where idclientes=%s""",(nombre_cliente,telefono,tipo_rep,modelo,Estadorep,id))
        mysql.connection.commit()
        actualizado='Datos del cliente actualizados'
        flash(actualizado)
        print(sucursal)
        if sucursal=='Nuevo hermosillo':
            return redirect(url_for('tercersuc'))
        if sucursal=='Xolotl':
             return redirect(url_for('segundasuc'))

        return redirect(url_for('index'))



@app.route('/delete/<string:id>')
def eliminar(id):
    cur2 = mysql.connection.cursor()
    cur2.execute('select Sucursal from clientes where idclientes=%s',(id))
    aux=cur2.fetchall()
    aux2=aux[0]
    sucursal=aux2[0]
    print (sucursal)
    cur= mysql.connection.cursor()
    cur.execute('delete from clientes where idclientes={0}'.format(id))
    mysql.connection.commit()
    eliminado='Dispositivo eliminado correctamente'
    flash(eliminado)
    if sucursal=='Nuevo hermosillo':
         return redirect(url_for('tercersuc'))
    if sucursal=='Xolotl':
         return redirect(url_for('segundasuc'))

    return redirect(url_for('index'))


@app.route('/estado/<id>')
def estado(id):
    return 'estado del telefono'

if __name__ == '__main__':
    app.run(port=8080, debug=True)
