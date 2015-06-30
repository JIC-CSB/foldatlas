from flask import Flask, render_template, request
from sys import argv
from controllers import GenomeBrowser, TranscriptView, TranscriptSearcher, CoverageSearcher

import settings
import database

app = Flask(__name__)

@app.after_request
def after_request(response):
	response.headers.add('Access-Control-Allow-Origin', '*')
	return response

# The index should show the genome browser and also a search box.
# Maybe also some introductory text.
@app.route("/")
def index():
	return render_template("index.html", settings=settings, genome_browser=GenomeBrowser())

@app.route("/search")
def search():
	return render_template("index.html", settings=settings, genome_browser=GenomeBrowser(), search=True)	

# Transcript - initialise the genome browser with custom parameters to center on the gene of interest.
# Also show the transcript's details
@app.route("/transcript/<transcript_id>")
def view_transcript(transcript_id):
	return render_template("index.html", 
		settings=settings, 
		genome_browser=GenomeBrowser(), 
		transcript_view=TranscriptView(transcript_id))

@app.route("/ajax/genome-browser/genes")
def get_genes_ajax():
	return GenomeBrowser().get_genes(request)

@app.route("/ajax/genome-browser/transcripts")
def get_transcripts_ajax():
	return GenomeBrowser().get_transcripts(request)

@app.route("/ajax/search-transcript/<search_string>")
def search_transcripts_ajax(search_string):
	return TranscriptSearcher().search(search_string)

@app.route("/ajax/search-coverage/<page_num>")
def search_coverage_ajax(page_num):
	return render_template(
		"coverage-search.html", 
		transcript_data=CoverageSearcher().fetch_transcript_data(page_num)
	)

@app.route("/ajax/transcript/<transcript_id>")
def view_transcript_ajax(transcript_id):
	return render_template("transcript-view.html", transcript_view=TranscriptView(transcript_id))

if __name__ == "__main__": 
	# if we're in here, we're using `python3 app.py [blah...]`
	if (len(argv) > 1 and argv[1] == "hydratedb"):
		# reset the database
		database.hydrate_db()
		
	else:
		# dev server: get the party started
		app.run(host='0.0.0.0', debug=True)
