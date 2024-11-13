#!/bin/bash

cd app
/Users/benberinsky/anaconda3/bin/uvicorn main:app --reload --log-level debug

