

from flask import Flask, render_template, request
import json

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index_page():
   return render_template('index.html')


@app.route("/calculate_percentage", methods=["POST"])
def calculate_percentage():
    student_name = str(request.form.get("student_name"))
 
    maths_marks = int(request.form.get("maths_marks"))
    science_marks = int(request.form.get("science_marks"))
    social_science_marks = int(request.form.get("social_science_marks"))
    language = int(request.form.get("language_marks"))
    alternative_marks = int(request.form.get("alternative_marks"))

    print("Calculating", student_name, maths_marks, science_marks, social_science_marks, alternative_marks, language)


    total_marks = maths_marks + science_marks + social_science_marks + alternative_marks + language

    print("Total", total_marks)

    percentage = int(total_marks) * ( 100 / 500 )

    rounded_percentage = round(percentage, 2)

    print("Percentage", rounded_percentage)

    # json
    data = {
        "student_name": student_name,
        "maths_marks": maths_marks,
        "science_marks":science_marks,
        "social_science_marks": social_science_marks,
        "language": language,
        "alternative_marks": alternative_marks,
        "total_marks": total_marks,
        "percentage" : rounded_percentage
    }


    file = open('data.json', 'a')
    file.write(json.dumps(data))

    return render_template('result.html', data={ "name": student_name, "percentage": rounded_percentage, "total_marks": total_marks })


if __name__ =='__main__':  
    app.run(host="0.0.0.0",port=5000,debug = True)