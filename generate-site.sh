#!/bin/bash

cd hugo-site

[ -d hugo-site/public ] && rm hugo-site/public -rf
hugo --cacheDir "$PWD/hugo_cache" --environment production --destination ../docs
