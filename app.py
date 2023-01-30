from functools import reduce
from flask import Flask, render_template, url_for, request, redirect, session
import sql

app = Flask(__name__)

app.secret_key = "key"

@app.route('/', methods=['POST', 'GET'])
def index():
    #If there are an session active redirect to the homepage
    if 'user' in session:
        return redirect(url_for('home'))
    else:
        if request.method == 'POST':
            
            #Load the user sended by the user and the list of usersnames in db 
            user = request.form['user']
            users = sql.request('users', 'user')

            #If the user sended by the user is in the list of users
            if user in users:
                #Load the password sended by the user and the list of passwords in db
                passwd = request.form['passwd']
                passwds = sql.request('users','passwd', f'user = "{user}"')
                if passwd in passwds:
                    #Set in session the user and redirect to the homepage
                    session['user'] = user
                    return redirect(url_for('home'))
                else:
                    return 'putocmdsql'

            else:
                return 'user dont exist'
        else:
            return render_template('login.html', user = False)

@app.route('/home')
def home():
    #Check if there are a session active 
    if "user" in session:
        return render_template('home.html', user = True)

    #If there aren't a session active the user is sended to the login page
    return redirect('/')

@app.route('/inventory')
def inventory():
    #Check if there are a session active 
    if 'user' in session:
        #Render inventriy
        return render_template('inventory.html', user = True)

    #If there aren't a session active the user is sended to the login page
    return redirect(url_for('index'))  

#AGENTS
@app.route('/agents', methods = ['POST', 'GET'])
def agents():
    ltsagents = []
    if 'user' in session:
        reqagents = sql.request('agents')
        for agent in reqagents:
            ltsagents.append(str(agent).replace("')","").replace("'","").replace(" ","").split(","))

        if request.method == 'POST':
            filt = []
            srname = request.form['sr-name'].lower()
            srlastname = request.form['sr-lastname'].lower()

            if srname != '' and srlastname != '':
                for i in ltsagents:
                    if srname in i and srlastname in i:
                        filt.append(i)

            elif srname != '' and srlastname == '':
                for i in ltsagents:
                    if srname in i:
                        filt.append(i)

            elif srname == '' and srlastname !='':
                for i in ltsagents:
                    if srlastname in i:
                        filt.append(i)                        
            else:
                return render_template('agents.html', user = True, agents = ltsagents)
            
            return render_template('agents.html', user = True, agents = filt)
            
        else:
            print('this is not a post')            
            
        return render_template('agents.html', user = True, agents = ltsagents)

    return redirect(url_for('index'))

@app.route('/addagent', methods=['POST', 'GET'])
def addagent():

    if 'user' in session:
        if request.method == 'POST':
            addname = request.form['add-name']
            addlastname = request.form['add-lastname']
            sql.add_agent(addname.lower(),addlastname.lower())
            return redirect(url_for("agents"))

        else:
            return render_template('addagent.html', user=True)

    return redirect(url_for('index'))

@app.route('/deleteagent', methods = ['POST', 'GET'])
def deleteagent():
    if 'user' in session:
        name = request.args.get('name', None)
        lastname = request.args.get('lastname', None)
        if name != None and lastname != None:
            sql.delete_agent(name, lastname)

        return redirect(url_for('agents'))

    return redirect(url_for('index'))

@app.route('/editagent', methods = ['POST', 'GET'])
def editagent():
    ltsagent = []

    if 'user' in session:
        ltsagent.append(request.args.get('name', None))
        ltsagent.append(request.args.get('lastname', None))
        
        if request.method == 'POST':
            name = request.form['name']
            lastname = request.form['lastname']
            sql.update('agents', f'name = "{name.lower()}", lastname = "{lastname.lower()}"',
            f'name="{ltsagent[0]}" AND lastname = "{ltsagent[1]}"')
            return redirect(url_for('agents'))
        
        else:
            return render_template('editagent.html', user = True, agent = ltsagent)
        
    return redirect(url_for('index'))

@app.route('/detailagent')
def detailagent():
    if 'user' in session:
        _name = request.args.get('name', None)
        _lastname = request.args.get('lastname', None)
        
        return render_template('agentdetail.htm', user=True, name = _name, lastname = _lastname)

    return redirect(url_for('index'))

@app.route('/activeagent', methods = ['POST', 'GET'])
def activeagent():
    if 'user' in session:
        name = request.args.get('name', None)
        lastname = request.args.get('lastname', None)

        if name != None and lastname != None:
            sql.active(name, lastname)

        return redirect(url_for('agents'))
    
    return redirect(url_for('index'))

@app.route('/dismissagent', methods = ['POST', 'GET'])
def dismissagent():
    if 'user' in session:
        name = request.args.get('name', None)
        lastname = request.args.get('lastname', None)

        if name != None and lastname != None:
            sql.dismiss(name, lastname)

        return redirect(url_for('agents'))

    return redirect(url_for('index'))

#MONITORS
@app.route('/monitors', methods = ['POST', 'GET'])
def monitors():
    ltsmonitors = []
    if 'user' in session:
        reqmonitors = sql.request('monitors')
        for monitor in reqmonitors:
            ltsmonitors.append(str(monitor).replace("')","").replace("'","").replace(" ","").split(","))

        return render_template('monitors.html', user = True, monitors = ltsmonitors)

    return redirect(url_for('index'))

@app.route('/addmonitor', methods=['POST', 'GET'])
def addmonitors():

    if 'user' in session:
        if request.method == 'POST':
            addbrand = request.form['add-brand']
            addsize = request.form['add-size']
            addserialnumber = request.form['add-serialnumber']
            sql.add_monitor(addbrand, addsize, addserialnumber)
            return redirect(url_for("monitors"))
        else:
            return render_template('addmonitor.html', user = True)

    return redirect(url_for('/'))

@app.route('/deletemonitor')
def deletemonitor():
    if 'user' in session:
        sn = request.args.get('serialnumber', None)
        sql.delete(sn, 'monitors')

        return redirect(url_for('monitors'))
    
    return redirect(url_for('index'))

#LAPTOPS
@app.route('/laptops')
def laptops():
    if 'user' in session:
        ltslaptops = []
        reqlaptops = sql.request('laptops')
        for laptop in reqlaptops:
            ltslaptops.append(str(laptop).replace("')","").replace("'","").replace(" ","").split(","))

        return render_template('laptops.html', user = True, laptops = ltslaptops)

    return redirect(url_for('/'))

@app.route('/addlaptop', methods = ['POST', 'GET'])
def addlaptop():
    if 'user' in session:
        if request.method == 'POST':
            addbrand = request.form['add-brand']
            addserialnumber = request.form['add-serialnumber']
            sql.add_laptop(addbrand, addserialnumber)
            return redirect(url_for('laptops'))
        return render_template('addlaptop.html', user=True )

    return redirect(url_for('/'))

@app.route('/deletelaptop')
def deletelaptop():
    if 'user' in session:
        sn = request.args.get('serialnumber', None)
        sql.delete(sn, 'laptops')
        return redirect(url_for('laptops'))

    return redirect(url_for('index'))

@app.route('/inv_floormap', methods=['POST', 'GET'])
def inv_floormap():

    if 'user' in session:

        if request.method == 'POST':
            adddesk = request.form['add-desk']
            addfloor = request.form['add-floor']
            addsnmonitor = request.form['add-snmonitor']

        return render_template('inv_floormap.html', user=True)

    return redirect(url_for('/'))

@app.route('/logout')
def logout():

    if 'user' in session:
        session.pop('user', None)

    return redirect('/')

@app.errorhandler(404)
def error404(error):
    return render_template('error404.html'), 404


if __name__ == "__main__":
    app.run(debug = True, host="0.0.0.0")