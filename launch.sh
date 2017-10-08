#!/bin/bash

pushd frontend
php -S 0.0.0.0:3003 &
popd

pushd backend
python3 app.py
popd

kill %%

