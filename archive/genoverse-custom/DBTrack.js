// Custom gene loading component
// Talks to RNA browser endpoint to fetch genome data

// TODO rename to GffSQL
Genoverse.Track.DBTrack = Genoverse.Track.extend({
  id     : 'genes',
  name   : 'Genes',
  height : 200,

  populateMenu: function (feature) {
    // return false
    // get the transcript ID
    // do something with the transcript ID
    // console.log(feature)
  },
  2000000: {
    // This one applies when > 2M base-pairs per screen
    // Show a message
    labels : false
  },
  100000: { // mid range zoom - show genes as bars
    labels : false,
    model  : Genoverse.Track.Model.Gene.DBGene,
    view   : Genoverse.Track.View.Gene.DBGene
  },
  1: { // > 1 base-pair, but less then 100K
    labels : true,
    model  : Genoverse.Track.Model.Transcript.DBTranscript,
    view   : Genoverse.Track.View.Transcript.DBTranscript
  }
});
