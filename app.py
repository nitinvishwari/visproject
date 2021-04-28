from flask import Flask, render_template, request, jsonify, Response
import numpy as np
import pandas as pd
import random
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.manifold import MDS
from sklearn import metrics
# import scipy.spatial.distance
import json, math

app = Flask(__name__)
# app.config['JSON_SORT_KEYS'] = False


@app.route('/')
def hello():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
