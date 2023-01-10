from flask import Flask, render_template, request, url_for, redirect, session,jsonify
import pymongo
import bcrypt
import pandas as pd
import numpy as np
import joblib
from logger.logger import 


model= joblib.load("model.pkl")
log.addLog("INFO","model loaded")

first_half_columns=joblib.load("first_half_columns.pkl")
log.addLog("INFO","columns loaded")

sec_half_columns= joblib.load("sec_half_columns.pkl")
log.addLog("INFO","columns loaded")

all_cols= joblib.load("all_cols.pkl")
log.addLog("INFO","columns loaded")














if __name__ == "__main__":
    app.run(debug=False)