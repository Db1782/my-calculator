from flask import Flask,  redirect, request, url_for, render_template

app= Flask(__name__)

history = []

@app.route("/")
def home():
 return render_template("cal.html")

@app.route("/calc", methods=["GET","POST"])
def calc():
    try:
        no1 = float(request.form["no1"])
        no2 = float(request.form["no2"])
       
        if request.form["operation"] == "add":
            result = no1 + no2
            return render_template("cal.html", answero=f" {no1} + {no2} = {result}")
        
        elif request.form["operation"] == "sub":
            result = no1 - no2
            return render_template("cal.html", answero =f" {no1} - {no2} = {result}")
        
        elif request.form["operation"] == "mul":
            result = no1 * no2
            return render_template("cal.html", answero=f" {no1} * {no2} = {result}")
        
        elif request.form["operation"] == "div":
            result = no1 / no2
            return render_template("cal.html", answero=f" {no1} / {no2} = {result}")
       

    except ValueError:
        # "Invalid input: Please enter valid numbers."
        
     return render_template("cal.html", error="Invalid input: Please enter valid numbers.")
  
    
    

 # Crucial: return the SAME template and pass the result variable
    return render_template("index.html", calculation_result=result)



if __name__=="__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", debug=True,port=port)

    