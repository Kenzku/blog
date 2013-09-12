__author__ = 'Ken'
from flask import Flask, request, session, g, redirect, url_for, \
     abort, render_template, flash

app = Flask(__name__)

with app.test_request_context('/?name=Peter'):
    assert request.path == '/'
    assert request.args['name'] == 'Peter'