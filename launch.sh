#!/bin/bash

pushd backend
python3 app.py &
popd

pushd frontend
php -S 0.0.0.0:3003
popd

kill %%

