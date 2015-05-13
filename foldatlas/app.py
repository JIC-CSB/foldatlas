from flask import Flask, render_template, request
from sys import argv
from controllers import GenomeBrowser, AlignmentViewer

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
	genome_browser = GenomeBrowser()
	return render_template("index.html", settings=settings, genome_browser=genome_browser)

# Transcript - initialise the genome browser with custom parameters to center on the gene of interest.
# Also show the transcript's details
@app.route("/transcripts/<transcript_id>")
def get_transcript():
	chromosomes = GenomeBrowser().get_chromosomes()
	viewer = AlignmentViewer()
	viewer.build_alignment_entries(transcript_id)
	return render_template("index.html", settings=settings, chromosomes=chromosomes, viewer=viewer)

@app.route("/ajax/genome-browser/genes")
def get_genes_ajax():
	return GenomeBrowser().get_genes(request)

@app.route("/ajax/genome-browser/transcripts")
def get_transcripts_ajax():
	return GenomeBrowser().get_transcripts(request)

@app.route("/ajax/transcript/<transcript_id>")
def get_transcript_ajax(transcript_id):
	return render_template("alignment-viewer.html", viewer=viewer)

if __name__ == "__main__": 
	# if we're in here, we're using `python3 app.py [blah...]`
	if (len(argv) > 1 and argv[1] == "hydratedb"):
		# reset the database
		database.hydrate_db()
		
	else:
		# dev server: get the party started
		app.run(host='0.0.0.0', debug=True)
