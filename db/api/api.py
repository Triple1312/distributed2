from flask import Flask, render_template, redirect, request, url_for
import requests
import redis
import time


app = Flask(__name__)
cache = redis.Redis(host='redis', port=6379)

if __name__ = '__main__':
    app.run(host="localhost", port=5001)