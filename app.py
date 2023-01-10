from flask import Flask, render_template, request, url_for, redirect, session,jsonify
import pymongo
import bcrypt
import pandas as pd
import numpy as np
import joblib
from logger.logger import 


model=joblib.load("model.pkl")
log.addLog("INFO","model loaded")

data_columns=joblib.load("data_columns.pkl")
log.addLog("INFO","columns loaded")

model_cols=joblib.load("data_cols.pkl")
log.addLog("INFO","columns loaded")














if __name__ == "__main__":
    app.run(debug=False)