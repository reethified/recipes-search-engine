from flask import Flask, redirect, url_for, render_template, request, flash
import os
from flask import Flask, render_template
from json2html import *
import requests
import json
import os
from elasticsearch import Elasticsearch

INDEX_NAME="recipes_idx1"
es = Elasticsearch(['localhost','0.0.0.0'], port=9200)
def searchEs(term):
   query = json.dumps({
        "query": {
            "match": {
                "title": term
            }
        }
    })
   res = es.search(index=INDEX_NAME, body=query)
   return json2html.convert(json = res)


def autosuggestES(query):
    esquery = json.dumps({
                "suggest": {
                    "text": query,
                    "recipes": {
                        "term": {
                            "field": "title"
                            }
                    }
                }
            })
    print(query)
    suggestRes= es.search(index=INDEX_NAME, body=esquery)
    print(suggestRes)
    return suggestRes