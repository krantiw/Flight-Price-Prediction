# -*- coding: utf-8 -*-

from flask import Flask, request, render_template
import pickle
import pandas as pd


app = Flask(__name__)
model = pickle.load(open("model_randomforest.pkl", "rb"))


@app.route("/")

def home():
    return render_template("index.html")



@app.route("/predict", methods=["GET", "POST"])
# @cross_origin()
def predict():
    if request.method == "POST":

        # Date of journey/Departure
        dep_date = request.form["Departure_Time"]

        dep_day = int(pd.to_datetime(dep_date, format="%Y-%m-%dT%H:%M").day)
        dep_month = int(pd.to_datetime(
            dep_date, format="%Y-%m-%dT%H:%M").month)
        print(dep_day, dep_month)

        # Deaprture
        dep_hour = int(pd.to_datetime(dep_date, format="%Y-%m-%dT%H:%M").hour)
        dep_minute = int(pd.to_datetime(
            dep_date, format="%Y-%m-%dT%H:%M").minute)
        print(dep_hour, dep_minute)

        # Arrival
        arr_date = request.form["Arrival_Time"]
        arrival_hour = int(pd.to_datetime(
            arr_date, format="%Y-%m-%dT%H:%M").hour)
        arrival_minute = int(pd.to_datetime(
            arr_date, format="%Y-%m-%dT%H:%M").minute)
        print("Arrival:", arrival_hour, arrival_minute)

        # Duration
        dur_hour = abs(arrival_hour - dep_hour)
        dur_minute = abs(arrival_minute - dep_minute)
        print("Duration:", dur_hour, dur_minute)

        # Number of stops
        total_stops = int(request.form["stops"])
        print(total_stops)

        # Source
        source = request.form["Source"]
        if (source == "Delhi"):
            s_Delhi = 1
            s_Kolkata = 0
            s_Mumbai = 0
            s_Chennai = 0
        elif (source == "Kolkata"):
            s_Delhi = 0
            s_Kolkata = 0
            s_Mumbai = 0
            s_Chennai = 0
        elif (source == "Mumbai"):
            s_Delhi = 0
            s_Kolkata = 0
            s_Mumbai = 1
            s_Chennai = 0
        elif (source == "Chennai"):
            s_Delhi = 0
            s_Kolkata = 0
            s_Mumbai = 0
            s_Chennai = 1
        else:
            s_Delhi = 0
            s_Kolkata = 0
            s_Mumbai = 0
            s_Chennai = 0

        # Destination
        destination = request.form["Destination"]
        if (destination == "Cochin"):
            d_Cochin = 1
            d_Delhi = 0
            d_New_Delhi = 0
            d_Hyderabad = 0
            d_Kolkata = 0

        elif (destination == "Delhi"):
            d_Cochin = 0
            d_Delhi = 1
            d_New_Delhi = 0
            d_Hyderabad = 0
            d_Kolkata = 0

        elif (destination == "New_Delhi"):
            d_Cochin = 0
            d_Delhi = 0
            d_New_Delhi = 1
            d_Hyderabad = 0
            d_Kolkata = 0

        elif (destination == "Hyderabad"):
            d_Cochin = 0
            d_Delhi = 0
            d_New_Delhi = 0
            d_Hyderabad = 1
            d_Kolkata = 0

        elif (destination == "Kolkata"):
            d_Cochin = 0
            d_Delhi = 0
            d_New_Delhi = 0
            d_Hyderabad = 0
            d_Kolkata = 1

        else:
            d_Cochin = 0
            d_Delhi = 0
            d_New_Delhi = 0
            d_Hyderabad = 0
            d_Kolkata = 0

        # Airlines
        airlines = request.form["airline"]
        if (airlines == "Jet Airways"):
            Jet_Airways = 1
            IndiGo = 0
            Air_India = 0
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 0
            GoAir = 0
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 0
            Vistara_Premium_economy = 0
            Trujet = 0

        elif(airlines == "Indigo"):
            Jet_Airways = 0
            IndiGo = 1
            Air_India = 0
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 0
            GoAir = 0
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 0
            Vistara_Premium_economy = 0
            Trujet = 0
        elif(airlines == "Air_India"):
            Jet_Airways = 0
            IndiGo = 0
            Air_India = 1
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 0
            GoAir = 0
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 0
            Vistara_Premium_economy = 0
            Trujet = 0
        elif(airlines == "Multiple_carriers"):
            Jet_Airways = 0
            IndiGo = 0
            Air_India = 0
            Multiple_carriers = 1
            SpiceJet = 0
            Vistara = 0
            GoAir = 0
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 0
            Vistara_Premium_economy = 0
            Trujet = 0
        elif(airlines == "SpiceJet"):
            Jet_Airways = 0
            IndiGo = 0
            Air_India = 0
            Multiple_carriers = 0
            SpiceJet = 1
            Vistara = 0
            GoAir = 0
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 0
            Vistara_Premium_economy = 0
            Trujet = 0
        elif(airlines == "Vistara"):
            Jet_Airways = 0
            IndiGo = 0
            Air_India = 0
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 1
            GoAir = 0
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 0
            Vistara_Premium_economy = 0
            Trujet = 0
        elif(airlines == "GoAir"):
            Jet_Airways = 0
            IndiGo = 0
            Air_India = 0
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 0
            GoAir = 1
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 0
            Vistara_Premium_economy = 0
            Trujet = 0
        elif(airlines == "Multiple_carriers_Premium_economy"):
            Jet_Airways = 0
            IndiGo = 0
            Air_India = 0
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 0
            GoAir = 0
            Multiple_carriers_Premium_economy = 1
            Jet_Airways_Business = 0
            Vistara_Premium_economy = 0
            Trujet = 0
        elif(airlines == "Jet_Airways_Business"):
            Jet_Airways = 0
            IndiGo = 0
            Air_India = 0
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 0
            GoAir = 0
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 1
            Vistara_Premium_economy = 0
            Trujet = 0
        elif(airlines == "Vistara_Premium_economy"):
            Jet_Airways = 0
            IndiGo = 0
            Air_India = 0
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 0
            GoAir = 0
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 0
            Vistara_Premium_economy = 1
            Trujet = 0
        elif(airlines == "Trujet"):
            Jet_Airways = 0
            IndiGo = 0
            Air_India = 0
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 0
            GoAir = 0
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 0
            Vistara_Premium_economy = 0
            Trujet = 1

        else:
            Jet_Airways = 0
            IndiGo = 0
            Air_India = 0
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 0
            GoAir = 0
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 0
            Vistara_Premium_economy = 0
            Trujet = 0

            # ['Total_Stops', 'Journey_month', 'Journey_day', 'Dep_Time_hour',
       #'Dep_Time_minute', 'Arrival_Time_hour', 'Arrival_Time_minute',
       #'duration_hours', 'duration_minutes', 'Airline_Air India',
       #'Airline_GoAir', 'Airline_IndiGo', 'Airline_Jet Airways',
       #'Airline_Jet Airways Business', 'Airline_Multiple carriers',
       #'Airline_Multiple carriers Premium economy', 'Airline_SpiceJet',
       #'Airline_Trujet', 'Airline_Vistara', 'Airline_Vistara Premium economy',
       #'Source_Chennai', 'Source_Delhi', 'Source_Kolkata', 'Source_Mumbai',
       #'Destination_Cochin', 'Destination_Delhi', 'Destination_Hyderabad',
       # 'Destination_Kolkata', 'Destination_New Delhi']

        predictions = model.predict([[
            total_stops,
            dep_month,
            dep_day, dep_hour, dep_minute,
            arrival_hour, arrival_minute, dur_hour, dur_minute, Air_India, GoAir, IndiGo, Jet_Airways,
            Jet_Airways_Business, Multiple_carriers, Multiple_carriers_Premium_economy, SpiceJet,
            Trujet, Vistara, Vistara_Premium_economy, s_Chennai, s_Delhi, s_Kolkata, s_Mumbai,
            d_Cochin, d_Delhi, d_Hyderabad, d_Kolkata, d_New_Delhi]])

        result = round(predictions[0], 2)


        return render_template('index.html', prediction_text="Your Flight price is Rs. {}".format(result))

    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
