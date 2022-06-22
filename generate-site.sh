#!/bin/bash

cd hugo-site

hugo --cacheDir "$PWD/hugo_cache" --environment production --destination ../docs
