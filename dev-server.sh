#!/bin/bash

cd hugo-site
hugo server --cacheDir "$PWD/hugo_cache"
